#!/usr/bin/env python3
"""Finite real-CLI producer -> report reader -> existing data consumer replay."""
from __future__ import annotations
import argparse
import contextlib
import hashlib
import io
import json
from pathlib import Path
import sys
import tempfile

ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'tools/nollm_visual_toolkit')]
from nollm_visual_toolkit import core, multiplicative as m, multiplicative_report as r


def digest(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--count',type=int,default=4096)
    p.add_argument('--schemes',nargs='+',default=['valuation','mixed','spiral','radial'])
    p.add_argument('--scales',nargs='+',default=['0.50','1','3/2'])
    p.add_argument('--out',type=Path,default=ROOT/'evidence/migration13/population_4096.json')
    a=p.parse_args();rows=[]
    a.out.parent.mkdir(parents=True,exist_ok=True)
    def save():
        result={'schema':'M13_FINITE_REPORT_REPLAY_MATRIX_V1','cases':len(rows),'rows':rows,
                'scope':'actual unchanged M12 CLI, current report replay, core.read_data/data consumers; no browser run or universal proof'}
        a.out.write_text(json.dumps(result,indent=2)+'\n')
    for scheme in a.schemes:
        for scale in a.scales:
            with tempfile.TemporaryDirectory() as td:
                source=Path(td)/'source.json'
                argv=sys.argv
                try:
                    sys.argv=['multiplicative','--count',str(a.count),'--scheme',scheme,
                              '--machine-only','--cell-scale',scale,'--report',str(source)]
                    with contextlib.redirect_stdout(io.StringIO()):
                        if m.main()!=0:raise AssertionError('producer failed')
                finally:sys.argv=argv
                report=r.load_machine_report(source)
                field=r.replay_machine_report(report)
                data=core.read_data(source)
                expected=m.hex_data(field)
                if data['records']!=expected['records']:raise AssertionError('identity mismatch')
                if data['metadata']['machine_report_import']['source_statistics']!=report['statistics']:
                    raise AssertionError('observation lost')
                for ext in ('json','csv'):
                    path=Path(td)/('cells.'+ext);core.write_data(data,path)
                    if core.read_data(path)!=data:raise AssertionError('roundtrip failed')
                # Existing analysis consumers run over imported certified cells.
                if core.collision_groups(data)!=core.collision_groups(expected):
                    raise AssertionError('consumer counts mismatch')
                seed=r.machine_report_startup(report,display_scale=2)
                if seed['cell_options']['scale']!=scale:raise AssertionError('source text lost')
                row={'count':a.count,'scheme':scheme,'scale_text':scale,
                     'status':field['cell_membership_exact']['status'],
                     'unresolved':len(field['cell_membership_exact']['unresolved_identities']),
                     'occupied_cells':field['cell_membership_exact']['occupied_cells'],
                     'original_report_sha256':digest(report),
                     'identity_records_sha256':digest(data['records']),
                     'summary_matched':m.cell_membership_summary(field)==report['cell_membership_exact'],
                     'complete_data_records_matched':True,'json_csv_roundtrip':True,
                     'existing_collision_consumer_matched':True,
                     'explicit_startup_source_preserved':True}
                rows.append(row);save();print(json.dumps(row),flush=True)
    result={'schema':'M13_FINITE_REPORT_REPLAY_MATRIX_V1','cases':len(rows),'rows':rows,
            'scope':'actual unchanged M12 CLI, current report replay, core.read_data/data consumers; no browser run or universal proof'}
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(result,indent=2)+'\n')
    return 0
if __name__=='__main__':raise SystemExit(main())
