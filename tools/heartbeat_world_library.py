#!/usr/bin/env python3
"""Read existing Heartbeat World tool/theorem records without granting authority.

A documentation/metadata adapter, not a new mathematical tool family. It does
not import research modules, claim tasks, change admission, or run a scheduler.
Follow the existing FREE discovery firewall before exposing this catalog.
"""
from __future__ import annotations
import argparse
import ast
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CATALOG = 'research_toolkits/heartbeat_world.json'


def _path(root: Path, relative: str) -> Path:
    root = root.resolve()
    path = (root / relative).resolve()
    if not path.is_relative_to(root):
        raise ValueError('library reference escapes repository')
    return path


def _json(root: Path, relative: str) -> dict[str, Any]:
    value = json.loads(_path(root, relative).read_text(encoding='utf-8'))
    if not isinstance(value, dict):
        raise ValueError(f'JSON object required: {relative}')
    return value


def _blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()


def resolve(root: Path = ROOT) -> dict[str, Any]:
    """Resolve exact existing IDs; retain each original theorem record verbatim."""
    catalog = _json(root, CATALOG)
    priority = _json(root, catalog['priority_ref'])
    tools, theorems, seen_methods, seen_theorems = [], [], set(), set()
    for entry in catalog['entries']:
        found = [m for m in _json(root, entry['inventory_ref'])['methods']
                 if m['method_id'] == entry['method_id']]
        if len(found) != 1 or entry['method_id'] in seen_methods:
            raise ValueError('missing or duplicated existing method ID')
        seen_methods.add(entry['method_id'])
        tools.append(found[0])
        ledger = _json(root, entry['ledger'])
        records = ledger.get('laws', ledger.get('theorems', []))
        ids = [r.get('id', r.get('theorem_id')) for r in records]
        if len(ids) != len(set(ids)):
            raise ValueError('duplicate source theorem IDs')
        for identifier in entry['theorem_ids']:
            if identifier not in ids or identifier in seen_theorems:
                raise ValueError('missing or duplicated selected theorem ID')
            seen_theorems.add(identifier)
            original = records[ids.index(identifier)]
            theorems.append({'id': identifier, 'ledger': entry['ledger'],
                'ledger_status': ledger['status'], 'original_record': original,
                'admission_by_this_catalog': False})
    return {'catalog': catalog, 'priority': priority, 'tools': tools,
            'theorems': theorems}


def validate(root: Path = ROOT) -> dict[str, Any]:
    """Validate catalog integrity only; no theorem proof/independent review claim."""
    data = resolve(root)
    catalog, priority = data['catalog'], data['priority']
    if priority['priority_tier'] != 'FIRST_TIER' or priority['grants_claim'] is not False:
        raise ValueError('priority tier or no-claim boundary changed')
    if catalog['new_theorems_claimed'] != 0 or catalog['new_mathematical_tool_families'] != 0:
        raise ValueError('extraction must not masquerade as new mathematics')
    wc = priority['world_contract']
    if (wc['spatial_dimension'], wc['time_dimension'], wc['time_is_spatial_axis']) != (6, 1, False):
        raise ValueError('native world type changed')
    exports = 0
    for entry, method in zip(catalog['entries'], data['tools']):
        for key in ('module', 'ledger', 'proof', 'test', 'inventory_ref'):
            if not _path(root, entry[key]).is_file():
                raise ValueError(f'missing reference: {entry[key]}')
        for key in ('module', 'ledger'):
            if _blob(_path(root, entry[key])) != entry['source_pin'][key + '_blob']:
                raise ValueError(f'source changed; revalidate catalog pin: {entry[key]}')
        tree = ast.parse(_path(root, entry['module']).read_text(encoding='utf-8'))
        available = {n.name for n in tree.body if isinstance(n, (ast.FunctionDef, ast.ClassDef))}
        if not set(method['api']) <= available:
            raise ValueError('registered export missing from source')
        exports += len(method['api'])
        if method['family_id'] != 'T0_BRC' or not method.get('hard_boundary'):
            raise ValueError('existing family or scope boundary missing')
    for theorem in data['theorems']:
        source = theorem['original_record']
        if not source.get('assumptions') or not (source.get('law') or source.get('statement')):
            raise ValueError('theorem assumptions or conclusion missing')
        proof = source.get('proof_ref', source.get('proof', '')).split('#')[0]
        test = source.get('test_ref', source.get('test', '')).split('::')[0]
        if not _path(root, proof).is_file() or not _path(root, test).is_file():
            raise ValueError('proof/test link missing')
    return {'status': 'PASS', 'methods': len(data['tools']), 'exports': exports,
            'theorem_candidates': len(data['theorems']), 'priority_tier': 'FIRST_TIER',
            'source_pins_checked': 2 * len(data['tools']),
            'mathematical_admission': False, 'scheduler_queue_rewritten': False}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['tools', 'theorems', 'priority', 'validate'])
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--query', default='')
    args = parser.parse_args(argv)
    try:
        if args.command == 'validate':
            output = validate(args.root)
        else:
            output = resolve(args.root)[args.command]
            if args.query and isinstance(output, list):
                output = [r for r in output if args.query.casefold() in
                          json.dumps(r, ensure_ascii=False).casefold()]
        print(json.dumps(output, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        parser.exit(2, f'Heartbeat library error: {exc}\n')


if __name__ == '__main__':
    raise SystemExit(main())
