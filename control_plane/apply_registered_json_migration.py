#!/usr/bin/env python3
"""Apply an approved control migration by replacing only registered JSON values.

The normal ``json.dump`` round-trip is deliberately forbidden here because it
would reformat a large governance file and make semantic review needlessly hard.
This tool parses JSON while retaining exact character spans for every JSON
pointer, then replaces only the value spans named by approved migration-registry
entries. All bytes outside those spans remain byte-for-byte unchanged.

Safety model:

* every migration id must exist in the semantic migration registry;
* every migration must target one file and be in an explicitly patchable/proven
  state;
* the target file Git blob must equal every migration's baseline blob before the
  first patch, unless all requested fields are already at their target values;
* a registered field may be only its frozen legacy value or exact target value;
* protected selector fields in the same file are checked before and after;
* after patching, JSON is reparsed and the object with target pointers removed
  must be deeply identical to the pre-patch object with the same pointers
  removed;
* ``--write`` is required to modify the checkout. Dry-run is the default.

This is a control-plane byte-locality mechanism. It does not decide whether a
migration is mathematically/governance-semantically safe; that approval must
already exist in ``control_semantic_migration_registry.json``.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "control_plane" / "control_semantic_migration_registry.json"
PATCHABLE_STATES = {
    "READY_FOR_MECHANICAL_PATCH",
    "REFERENCE_CHECK_PASSED_READY_FOR_MECHANICAL_PATCH",
    "READY_FOR_MECHANICAL_PATCH_WITH_RUNTIME_POINTER_BUNDLE",
    "FIELD_LOCALITY_PROOF_PASSED_AWAITING_SAFE_WRITE_MECHANISM",
    "TARGET_MIGRATED",
}


class MigrationApplyError(ValueError):
    pass


@dataclass(frozen=True)
class Span:
    start: int
    end: int


class JsonSpanParser:
    """Minimal RFC-8259 parser that records exact value spans by JSON pointer."""

    def __init__(self, text: str):
        self.text = text
        self.n = len(text)
        self.spans: dict[str, Span] = {}

    @staticmethod
    def _escape(token: str) -> str:
        return token.replace("~", "~0").replace("/", "~1")

    def _skip_ws(self, i: int) -> int:
        while i < self.n and self.text[i] in " \t\r\n":
            i += 1
        return i

    def _string(self, i: int) -> tuple[str, int]:
        if i >= self.n or self.text[i] != '"':
            raise MigrationApplyError(f"expected JSON string at offset {i}")
        j = i + 1
        escaped = False
        while j < self.n:
            ch = self.text[j]
            if escaped:
                escaped = False
                j += 1
                continue
            if ch == "\\":
                escaped = True
                j += 1
                continue
            if ch == '"':
                raw = self.text[i : j + 1]
                try:
                    value = json.loads(raw)
                except json.JSONDecodeError as exc:
                    raise MigrationApplyError(f"invalid JSON string at offset {i}: {exc}") from exc
                return value, j + 1
            j += 1
        raise MigrationApplyError(f"unterminated JSON string at offset {i}")

    def _number_or_literal(self, i: int) -> int:
        j = i
        while j < self.n and self.text[j] not in " \t\r\n,]}:":
            j += 1
        if j == i:
            raise MigrationApplyError(f"expected JSON value at offset {i}")
        raw = self.text[i:j]
        try:
            json.loads(raw)
        except json.JSONDecodeError as exc:
            raise MigrationApplyError(f"invalid JSON scalar at offset {i}: {raw!r}") from exc
        return j

    def _value(self, i: int, pointer: str) -> int:
        i = self._skip_ws(i)
        start = i
        if i >= self.n:
            raise MigrationApplyError("unexpected end of JSON")
        ch = self.text[i]
        if ch == "{":
            i = self._object(i, pointer)
        elif ch == "[":
            i = self._array(i, pointer)
        elif ch == '"':
            _, i = self._string(i)
        else:
            i = self._number_or_literal(i)
        self.spans[pointer] = Span(start=start, end=i)
        return i

    def _object(self, i: int, pointer: str) -> int:
        i += 1
        i = self._skip_ws(i)
        if i < self.n and self.text[i] == "}":
            return i + 1
        while True:
            i = self._skip_ws(i)
            key, i = self._string(i)
            i = self._skip_ws(i)
            if i >= self.n or self.text[i] != ":":
                raise MigrationApplyError(f"expected ':' after object key at offset {i}")
            i += 1
            child = pointer + "/" + self._escape(key)
            i = self._value(i, child)
            i = self._skip_ws(i)
            if i >= self.n:
                raise MigrationApplyError("unterminated JSON object")
            if self.text[i] == "}":
                return i + 1
            if self.text[i] != ",":
                raise MigrationApplyError(f"expected ',' or '}}' at offset {i}")
            i += 1

    def _array(self, i: int, pointer: str) -> int:
        i += 1
        i = self._skip_ws(i)
        if i < self.n and self.text[i] == "]":
            return i + 1
        index = 0
        while True:
            child = pointer + f"/{index}"
            i = self._value(i, child)
            index += 1
            i = self._skip_ws(i)
            if i >= self.n:
                raise MigrationApplyError("unterminated JSON array")
            if self.text[i] == "]":
                return i + 1
            if self.text[i] != ",":
                raise MigrationApplyError(f"expected ',' or ']' at offset {i}")
            i += 1

    def parse(self) -> dict[str, Span]:
        end = self._value(0, "")
        end = self._skip_ws(end)
        if end != self.n:
            raise MigrationApplyError(f"trailing content after JSON at offset {end}")
        return self.spans


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise MigrationApplyError(f"{path}: JSON object required")
    return value


def _git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def _tokens(pointer: str) -> list[str]:
    if not pointer.startswith("/"):
        raise MigrationApplyError(f"invalid JSON pointer: {pointer!r}")
    return [part.replace("~1", "/").replace("~0", "~") for part in pointer.split("/")[1:]]


def _get(value: Any, pointer: str) -> Any:
    current = value
    for token in _tokens(pointer):
        if isinstance(current, dict):
            if token not in current:
                raise MigrationApplyError(f"pointer not found: {pointer}")
            current = current[token]
        elif isinstance(current, list) and token.isdigit():
            index = int(token)
            if index >= len(current):
                raise MigrationApplyError(f"array pointer out of range: {pointer}")
            current = current[index]
        else:
            raise MigrationApplyError(f"pointer not found: {pointer}")
    return current


def _delete(value: Any, pointer: str) -> None:
    tokens = _tokens(pointer)
    if not tokens:
        raise MigrationApplyError("root deletion forbidden")
    current = value
    for token in tokens[:-1]:
        if isinstance(current, dict) and token in current:
            current = current[token]
        elif isinstance(current, list) and token.isdigit() and int(token) < len(current):
            current = current[int(token)]
        else:
            raise MigrationApplyError(f"pointer not found: {pointer}")
    last = tokens[-1]
    if isinstance(current, dict) and last in current:
        del current[last]
    elif isinstance(current, list) and last.isdigit() and int(last) < len(current):
        del current[int(last)]
    else:
        raise MigrationApplyError(f"pointer not found: {pointer}")


def _field_rows(entry: dict[str, Any]) -> list[tuple[str, Any, Any]]:
    if "json_pointer" in entry:
        return [
            (
                str(entry["json_pointer"]),
                entry.get("observed_legacy_value"),
                entry.get("canonical_target_value"),
            )
        ]
    pointers = entry.get("json_pointers")
    olds = entry.get("observed_legacy_values")
    targets = entry.get("canonical_target_values")
    if not isinstance(pointers, list) or not isinstance(olds, list) or not isinstance(targets, list):
        raise MigrationApplyError(f"{entry.get('migration_id')}: malformed pointer bundle")
    if not (len(pointers) == len(olds) == len(targets)) or not pointers:
        raise MigrationApplyError(f"{entry.get('migration_id')}: pointer bundle length mismatch")
    return [(str(pointer), old, target) for pointer, old, target in zip(pointers, olds, targets, strict=True)]


def _format_replacement(original: str, target: Any) -> str:
    """Serialize only the target value, preserving multiline style when present."""
    if "\n" not in original or not isinstance(target, (list, dict)):
        return json.dumps(target, ensure_ascii=False, separators=(",", ":") if isinstance(target, dict) else None)

    first_newline = original.find("\n")
    continuation = original[first_newline + 1 :]
    leading = continuation[: len(continuation) - len(continuation.lstrip(" \t"))]
    rendered = json.dumps(target, ensure_ascii=False, indent=2)
    lines = rendered.splitlines()
    if len(lines) <= 1:
        return rendered
    return lines[0] + "\n" + "\n".join(leading + line for line in lines[1:])


def _approved_entries(
    registry: dict[str, Any], migration_ids: list[str]
) -> list[dict[str, Any]]:
    by_id = {
        row.get("migration_id"): row
        for row in registry.get("entries", [])
        if isinstance(row, dict) and isinstance(row.get("migration_id"), str)
    }
    entries: list[dict[str, Any]] = []
    for migration_id in migration_ids:
        row = by_id.get(migration_id)
        if row is None:
            raise MigrationApplyError(f"unknown migration_id: {migration_id}")
        state = str(row.get("state") or "")
        if state not in PATCHABLE_STATES:
            raise MigrationApplyError(
                f"{migration_id}: state {state!r} is not approved for mechanical patch"
            )
        entries.append(row)
    return entries


def plan(migration_ids: list[str], root: Path = ROOT) -> dict[str, Any]:
    if not migration_ids:
        raise MigrationApplyError("at least one --migration-id is required")
    registry = _load(root / "control_plane" / "control_semantic_migration_registry.json")
    entries = _approved_entries(registry, migration_ids)
    paths = {str(row.get("path") or "") for row in entries}
    if len(paths) != 1 or "" in paths:
        raise MigrationApplyError("all requested migrations must target exactly one nonempty path")
    path_value = next(iter(paths))
    path = root / path_value
    if not path.exists():
        raise MigrationApplyError(f"target file missing: {path_value}")

    raw = path.read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise MigrationApplyError(f"target file is not UTF-8: {path_value}") from exc
    source = json.loads(text)
    if not isinstance(source, dict):
        raise MigrationApplyError("target JSON root must be an object")
    spans = JsonSpanParser(text).parse()

    rows: list[tuple[str, Any, Any, str]] = []
    all_already_target = True
    baseline_values = {str(row.get("baseline_blob_sha1") or "") for row in entries}
    for entry in entries:
        migration_id = str(entry["migration_id"])
        for pointer, old, target in _field_rows(entry):
            actual = _get(source, pointer)
            if actual == old:
                all_already_target = False
            elif actual != target:
                raise MigrationApplyError(
                    f"{migration_id}: {pointer} has third-state value {actual!r}"
                )
            rows.append((pointer, old, target, migration_id))

    actual_blob = _git_blob_sha1(raw)
    if not all_already_target:
        if len(baseline_values) != 1 or "" in baseline_values:
            raise MigrationApplyError("requested pending migrations do not share one exact baseline blob")
        expected_blob = next(iter(baseline_values))
        if actual_blob != expected_blob:
            raise MigrationApplyError(
                f"target blob drifted before patch: expected {expected_blob}, got {actual_blob}"
            )

    target_pointers = {pointer for pointer, _, _, _ in rows}
    protected_rows = [
        row
        for row in registry.get("protected_selector_fields", [])
        if isinstance(row, dict) and row.get("path") == path_value
    ]
    protected_before: dict[str, Any] = {}
    for row in protected_rows:
        pointer = str(row.get("json_pointer") or "")
        required = row.get("required_value")
        actual = _get(source, pointer)
        if actual != required:
            raise MigrationApplyError(
                f"protected selector drift before patch: {path_value}{pointer}={actual!r}, required={required!r}"
            )
        protected_before[pointer] = copy.deepcopy(actual)
        if pointer in target_pointers:
            raise MigrationApplyError(
                f"registered migration pointer is also protected: {pointer}"
            )

    replacements: list[tuple[int, int, str, str]] = []
    before_values: dict[str, Any] = {}
    target_values: dict[str, Any] = {}
    for pointer, old, target, migration_id in rows:
        span = spans.get(pointer)
        if span is None:
            raise MigrationApplyError(f"no textual span for registered pointer: {pointer}")
        actual = _get(source, pointer)
        before_values[pointer] = copy.deepcopy(actual)
        target_values[pointer] = copy.deepcopy(target)
        if actual == target:
            continue
        original_value_text = text[span.start : span.end]
        replacement = _format_replacement(original_value_text, target)
        replacements.append((span.start, span.end, replacement, pointer))

    proposed = text
    for start, end, replacement, _ in sorted(replacements, reverse=True):
        proposed = proposed[:start] + replacement + proposed[end:]
    proposed_obj = json.loads(proposed)
    if not isinstance(proposed_obj, dict):
        raise MigrationApplyError("proposed JSON root must remain an object")

    for pointer, target in target_values.items():
        if _get(proposed_obj, pointer) != target:
            raise MigrationApplyError(f"post-patch target mismatch at {pointer}")
    protected_after: dict[str, Any] = {}
    for row in protected_rows:
        pointer = str(row.get("json_pointer") or "")
        required = row.get("required_value")
        actual = _get(proposed_obj, pointer)
        if actual != required:
            raise MigrationApplyError(
                f"protected selector changed by patch: {path_value}{pointer}={actual!r}, required={required!r}"
            )
        protected_after[pointer] = copy.deepcopy(actual)

    source_rest = copy.deepcopy(source)
    proposed_rest = copy.deepcopy(proposed_obj)
    for pointer in sorted(target_pointers, key=lambda item: item.count("/"), reverse=True):
        _delete(source_rest, pointer)
        _delete(proposed_rest, pointer)
    if source_rest != proposed_rest:
        raise MigrationApplyError("patch changes JSON structure outside registered pointers")

    # Construction proof: all unchanged textual segments are copied verbatim.
    original_unchanged: list[str] = []
    proposed_unchanged: list[str] = []
    ordered = sorted((start, end, replacement) for start, end, replacement, _ in replacements)
    old_cursor = 0
    new_cursor = 0
    for start, end, replacement in ordered:
        old_segment = text[old_cursor:start]
        new_segment = proposed[new_cursor : new_cursor + len(old_segment)]
        original_unchanged.append(old_segment)
        proposed_unchanged.append(new_segment)
        if old_segment != new_segment:
            raise MigrationApplyError("byte locality proof failed before a replacement span")
        old_cursor = end
        new_cursor += len(old_segment) + len(replacement)
    tail = text[old_cursor:]
    proposed_tail = proposed[new_cursor:]
    if tail != proposed_tail:
        raise MigrationApplyError("byte locality proof failed after final replacement span")
    original_unchanged.append(tail)
    proposed_unchanged.append(proposed_tail)

    proposed_bytes = proposed.encode("utf-8")
    return {
        "target_path": path_value,
        "source_blob_sha1": actual_blob,
        "proposed_blob_sha1": _git_blob_sha1(proposed_bytes),
        "migration_ids": migration_ids,
        "changed_pointers": [pointer for _, _, _, pointer in replacements],
        "before_values": before_values,
        "target_values": target_values,
        "protected_before": protected_before,
        "protected_after": protected_after,
        "non_target_structure_equal": True,
        "non_target_text_segments_byte_identical": True,
        "already_target": all_already_target,
        "proposed_text": proposed,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--migration-id", action="append", dest="migration_ids", required=True)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    try:
        result = plan(args.migration_ids)
        proposed_text = result.pop("proposed_text")
        if args.write and result["changed_pointers"]:
            path = ROOT / str(result["target_path"])
            path.write_text(proposed_text, encoding="utf-8")
            result["written"] = True
        else:
            result["written"] = False
    except (MigrationApplyError, OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}")
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    print("PASS: registered migration is exact-span local and safe to apply in this checkout.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
