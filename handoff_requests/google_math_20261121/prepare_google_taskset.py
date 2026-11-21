#!/usr/bin/env python3
"""Prepare a local Objective + Task transaction with current native writers.

This script makes no remote calls. The candidate root must contain the current
contract files and genuine Source Driver authority records. Its local output is
not publication; the caller performs the fresh GitHub CAS and immutable readback.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys

SOURCE_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(SOURCE_ROOT))

import research_driver_authority
import research_objective_authority
from tools import research_task_records as records
from tools import research_taskbook


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--candidate-root', type=Path, required=True)
    parser.add_argument('--objective-payload', type=Path, required=True)
    parser.add_argument('--driver-id', required=True)
    parser.add_argument('--task-publisher-id', required=True)
    parser.add_argument('--task-publisher-role', choices=['RESEARCHER', 'RESEARCH_DRIVER'], required=True)
    parser.add_argument('--taskset', type=Path, required=True)
    args = parser.parse_args()
    root = args.candidate_root.resolve()
    if not research_driver_authority.contract_enabled(root):
        raise ValueError('Candidate root must contain the current Driver authority contract and authentic Source records')
    now = datetime.now(timezone.utc).isoformat()
    research_driver_authority.require_active_driver(args.driver_id, now, root)
    objective = json.loads(args.objective_payload.read_text())
    objective.update(publisher_id=args.driver_id, created_at=now)
    generation, head, selection = research_objective_authority.create_and_select(
        expected_previous_generation_id=None, root=root, **objective
    )
    taskset = json.loads(args.taskset.read_text())
    output = []
    for task in taskset:
        path = root / task['taskbook_path']
        meta, body = research_taskbook.split_taskbook(path.read_text())
        meta['parent_objective_id'] = generation['objective_id']
        meta['parent_objective_generation_id'] = generation['objective_generation_id']
        path.write_text(research_taskbook.render_taskbook(meta, body))
        records.prepare_taskbook(
            path, publisher_role=args.task_publisher_role,
            parent_objective_id=generation['objective_id'], root=root
        )
        meta, _ = records._prepared(path, root=root)
        record = records.build_record(
            meta, path=path, publisher_role=args.task_publisher_role,
            publisher_id=args.task_publisher_id, research_value=task['research_value'],
            published_at=datetime.now(timezone.utc).isoformat(),
            supersedes_publication_id=None, root=root
        )
        record_path = records.record_path(root, record['task_id'], record['publication_id'])
        records._save_json_exclusive(record_path, record)
        binding = research_objective_authority.resolve_authoritative_task_parent_binding(record, root)
        if not binding['objective_authority_verified']:
            raise ValueError('Native Objective binding was not verified')
        output.append({
            'task_id': record['task_id'], 'publication_id': record['publication_id'],
            'taskbook_path': path.relative_to(root).as_posix(),
            'record_path': record_path.relative_to(root).as_posix(),
            'taskbook_blob_sha1': record['taskbook_blob_sha1'],
            'taskbook_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
            'record_sha256': hashlib.sha256(record_path.read_bytes()).hexdigest(),
            'objective_authority_verified': True,
        })
    errors = records.audit(root) + research_objective_authority.audit(root)
    if errors:
        raise ValueError('\n'.join(errors))
    receipt = {
        'scope': 'LOCAL_NATIVE_FUNCTION_PREFLIGHT_ONLY',
        'remote_publication_performed': False,
        'objective_generation': generation,
        'objective_head': head,
        'objective_selection': selection,
        'tasks': output,
        'audit_errors': errors,
    }
    (root / 'local_preflight.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(receipt, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
