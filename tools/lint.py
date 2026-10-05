"""Static checks for the mod, since the game itself can't run in CI.

Usage: python3 tools/lint.py [--cwe PATH_TO_CWE_CHECKOUT]
Exits non-zero if anything is wrong. --cwe also checks that every building
group a modifier names exists in CWE.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOM = b"\xef\xbb\xbf"
LOC_PATH = ROOT / "localization/english/agi_l_english.yml"
# Modifier types the game defines, checked against vanilla's
# common/modifier_type_definitions. Any other key must be defined by this mod,
# or the engine drops it with an "Unknown modifier type" error.
VANILLA_MODIFIER_TYPES = {
    "building_group_bg_service_employee_mult", "building_group_bg_service_throughput_add",
    "building_group_bg_manufacturing_employee_mult", "building_group_bg_manufacturing_throughput_add",
    "building_group_bg_mining_employee_mult", "building_group_bg_mining_throughput_add",
    "state_welfare_payments_add", "state_standard_of_living_add",
}


def script(path):
    """File text with comments and quoted strings removed."""
    text = path.read_text(encoding="utf-8-sig")
    text = re.sub(r'"[^"\n]*"', '""', text)
    return re.sub(r"#[^\n]*", "", text)


def top_level_keys(text):
    keys, depth = [], 0
    for token in re.findall(r"[\w.:]+(?=\s*=\s*\{)|[{}]", text):
        if token == "{":
            depth += 1
        elif token == "}":
            depth -= 1
        elif depth == 0:
            keys.append(token)
    return keys


def _defined(files, folder):
    return {k for p, t in files.items() if folder in p.as_posix() for k in top_level_keys(t)}


def _rule_texts(files):
    return [t for p, t in files.items() if "common/game_rules" in p.as_posix()]


def check_braces(files):
    return [f"{p.relative_to(ROOT)}: unbalanced braces" for p, t in files.items() if t.count("{") != t.count("}")]


def check_references(files):
    text = "\n".join(files.values())
    options = set(re.findall(r"^\t(\w+) = \{", "\n".join(_rule_texts(files)), re.M))
    checks = [
        ("scripted effect or trigger", r"\b(agi_\w+) = yes",
         _defined(files, "common/scripted_effects") | _defined(files, "common/scripted_triggers")),
        ("modifier", r"(?:add_modifier = \{ name|has_modifier|remove_modifier) = (agi_\w+)",
         _defined(files, "common/static_modifiers")),
        ("event", r"trigger_event = \{ id = ([\w.]+)", _defined(files, "events/")),
        ("game rule option", r"has_game_rule = (\w+)", options),
    ]
    return [f"undefined {kind}: {name}" for kind, pattern, known in checks
            for name in sorted(set(re.findall(pattern, text)) - known)]


def check_localisation(files):
    raw = LOC_PATH.read_bytes()
    errors = [] if raw.startswith(BOM + b"l_english:") else ["localisation must start with a UTF-8 BOM and 'l_english:'"]
    loc = set(re.findall(r"^ ([\w.]+):0 ", raw.decode("utf-8-sig"), re.M))
    text = "\n".join(files.values())
    rules = "\n".join(_rule_texts(files))
    options = re.findall(r"^\t(\w+) = \{", rules, re.M)
    needed = set(re.findall(r"(?:title|desc|name) = (agi\.[\w.]+)", text))
    named = _defined(files, "common/static_modifiers") | _defined(files, "common/modifier_type_definitions")
    needed |= {k for m in named for k in (m, m + "_desc")}
    needed |= {"rule_" + r for r in top_level_keys(rules)}
    needed |= {k for o in options for k in ("setting_" + o, "setting_" + o + "_desc")}
    return errors + [f"missing localisation key: {k}" for k in sorted(needed - loc)]


def check_modifier_types(files):
    defined = VANILLA_MODIFIER_TYPES | _defined(files, "common/modifier_type_definitions")
    modifiers = "\n".join(t for p, t in files.items() if "common/static_modifiers" in p.as_posix())
    used = set(re.findall(r"^\t(\w+) = -?[\d.]", modifiers, re.M))
    return [f"modifier type not defined: {k}" for k in sorted(used - defined)]


def check_employee_floor(files):
    """Other modifiers stack on ours, and a total of -1 leaves a sector with no jobs."""
    cuts = re.findall(r"(building_group_\w+_employee_mult) = (-[\d.]+)", "\n".join(files.values()))
    return [f"{key} = {value} is below the -0.8 floor" for key, value in cuts if float(value) < -0.8]


def check_cwe_building_groups(files, cwe):
    group_files = (cwe / "common/building_groups").glob("*.txt")
    known = {k for p in group_files for k in top_level_keys(script(p))}
    used = set(re.findall(r"building_group_(bg_\w+)_(?:employee_mult|throughput_add)", "\n".join(files.values())))
    return [f"building group not in CWE: {g}" for g in sorted(used - known)]


def main():
    files = {p: script(p) for d in ("common", "events") for p in (ROOT / d).rglob("*.txt")}
    errors = [] if files else ["no script files found"]
    errors += check_braces(files) + check_references(files) + check_localisation(files)
    errors += check_modifier_types(files) + check_employee_floor(files)
    if "--cwe" in sys.argv:
        errors += check_cwe_building_groups(files, Path(sys.argv[sys.argv.index("--cwe") + 1]))
    for e in errors:
        print(e)
    print(f"{len(errors)} problem(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
