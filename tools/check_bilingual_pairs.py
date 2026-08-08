#!/usr/bin/env python3
import argparse
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "bilingual_pairs.json"
CJK_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")
HEADING_RE = re.compile(r"^(#{1,6})\s+", re.MULTILINE)


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def changed_files(base: str | None) -> set[str] | None:
    if not base or set(base) == {"0"}:
        return None
    try:
        git("cat-file", "-e", f"{base}^{{commit}}")
    except subprocess.CalledProcessError:
        return None
    out = git("diff", "--name-only", f"{base}...HEAD")
    return {line for line in out.splitlines() if line}


def heading_levels(text: str) -> list[int]:
    return [len(match.group(1)) for match in HEADING_RE.finditer(text)]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default=None, help="Base commit used to enforce same-change pairing")
    args = parser.parse_args()

    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    pairs = [tuple(pair) for pair in data["pairs"]]
    errors: list[str] = []
    registered = {path for pair in pairs for path in pair}

    for english, chinese in pairs:
        en_path = ROOT / english
        zh_path = ROOT / chinese

        if not en_path.is_file():
            fail(f"missing English pair member: {english}", errors)
        if not zh_path.is_file():
            fail(f"missing Chinese pair member: {chinese}", errors)
        if not en_path.is_file() or not zh_path.is_file():
            continue

        en_text = en_path.read_text(encoding="utf-8")
        zh_text = zh_path.read_text(encoding="utf-8")

        if CJK_RE.search(en_text):
            fail(f"Chinese character found in English prose file: {english}", errors)

        if heading_levels(en_text) != heading_levels(zh_text):
            fail(f"heading structure differs between pair: {english} <-> {chinese}", errors)

    for path in (ROOT / "docs").glob("*.en.md"):
        rel = path.relative_to(ROOT).as_posix()
        if rel not in registered:
            fail(f"unregistered English prose document: {rel}", errors)

    for path in (ROOT / "docs").glob("*.zh-CN.md"):
        rel = path.relative_to(ROOT).as_posix()
        if rel not in registered:
            fail(f"unregistered Chinese prose document: {rel}", errors)

    changed = changed_files(args.base)
    if changed is not None:
        for english, chinese in pairs:
            en_changed = english in changed
            zh_changed = chinese in changed
            if en_changed != zh_changed:
                fail(
                    f"paired documents must change together: {english} <-> {chinese}",
                    errors,
                )

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"PASS: {len(pairs)} bilingual document pairs are synchronized structurally.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
