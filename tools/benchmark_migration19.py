#!/usr/bin/env python3
"""Finite full-state Phase32 report roundtrips, not an independent numeric proof."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT/'src'), str(ROOT/'tools/nollm_visual_toolkit')]
from nollm_visual_toolkit import phase32_lab as p, phase32_report as r, core
from nollm_visual_toolkit.multiplicative import parse_cell_scale_text


def digest(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--count', type=int, default=4096)
    parser.add_argument('--mode', choices=('golden', 'hash', 'spiral'), default='golden')
    parser.add_argument('--pitches', nargs='+', default=['0.50', '1', '3/2'])
    args = parser.parse_args()
    rows = []
    out = ROOT/f'evidence/migration19/population_{args.count}_{args.mode}.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    for text in args.pitches:
        pair, source = parse_cell_scale_text(text)
        model = p.build(p.machine_config(args.count, args.mode), cell_pitch=pair, include_display=False)
        model['cell_pitch_source'] = source
        report = p.machine_report(model)
        with tempfile.TemporaryDirectory() as td:
            path = Path(td)/'r.json'; path.write_text(json.dumps(report), encoding='utf-8')
            loaded = r.load_machine_report(path)
            replayed = r.replay_machine_report(loaded)
            data = r._visual_data(replayed, loaded)
            csv = Path(td)/'d.csv'; core.write_data(data, csv)
            checks = dict(
                full_model_equal=replayed == model,
                full_certificates_equal=replayed['cell_membership_exact']['certificates'] == model['cell_membership_exact']['certificates'],
                complete_report_equal=loaded == report and p.machine_report(replayed) == report,
                identity_records_equal=data['records'] == p.hex_data(model)['records'],
                full_source_report_preserved=data['metadata']['source_machine_report'] == report,
                all_identities_retained=[x['id'] for x in data['records']] == [str(n) for n in range(args.count)],
                csv_roundtrip_equal=core.read_data(csv) == data,
                phase_modulus_preserved=replayed['cell_membership_exact']['phase_modulus'] == str(1 << 32),
            )
        if not all(checks.values()):
            raise AssertionError(checks)
        pop = model['cell_membership_exact']
        row = dict(count=args.count, mode=args.mode, pitch=text, checks=checks,
                   status=pop['status'], occupied_positive_cells=pop['occupied_cells'],
                   collision_excess=pop['collision_excess'], unresolved=len(pop['unresolved_identities']),
                   report_sha256=digest(report), full_model_sha256=digest(replayed),
                   certificates_sha256=digest(pop['certificates']), records_sha256=digest(data['records']))
        rows.append(row)
        out.write_text(json.dumps(dict(schema='M19_PHASE32_REPORT_POPULATION_V1', rows=rows,
                                       comparison='unchanged M18 producer vs M19 reader; finite not universal'), indent=2)+'\n')
        print(json.dumps(row), flush=True)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
