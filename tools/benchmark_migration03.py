#!/usr/bin/env python3
"""Bounded locally executed validation matrix; wall time is telemetry only."""
import argparse
import json
from pathlib import Path
import sys
import time
ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'tools/nollm_visual_toolkit')]
from nollm_visual_toolkit import multiplication_lab as lab

def main():
    p=argparse.ArgumentParser();p.add_argument('--count',type=int,required=True)
    p.add_argument('--modes',nargs='+',default=['golden','rank','zero'])
    p.add_argument('--scales',nargs='+',default=['1/2','1/1','3/2'])
    p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    spf=lab.smallest_factors(a.count);records=[]
    for mode in a.modes:
        phi=lab.phases(spf,lab.prime_phases(spf,mode))
        for scale in a.scales:
            sn,sd=map(int,scale.split('/'))
            start=time.perf_counter()
            exact=lab.diagnostics(phi,cell_scale=(sn,sd),exact_scale=10**12)
            seconds=time.perf_counter()-start
            old=lab.diagnostics(phi,sn/sd,exact_scale=10**12)
            assert exact['angular_counts'] == old['angular_counts']
            for key, value in old['angular_cv_squared_exact'].items():
                assert exact['angular_cv_squared_exact'][key] == value, key
            cells=exact['cell_membership_exact']
            record={'count':a.count,'mode':mode,'scale':[sn,sd],'status':cells['status'],
                    'unresolved':cells['unresolved_identities'],'ties':len(cells['tie_identities']),
                    'precision_counts':cells['precision_counts'],'integer_source_n_max_bits':(a.count-1).bit_length(),
                    'scaled_radicand_max_bits_at_64':((a.count-1)*(1<<128)).bit_length(),
                    'elapsed_seconds_telemetry':seconds}
            for k in ('occupied_cells','collision_groups','excess_identities_if_collapsed','max_cell_load'):
                record[k]={'certified':exact[k],'legacy':old[k]}
            records.append(record);print(json.dumps(record),flush=True)
            a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(records,indent=2)+'\n')
    return 0
if __name__=='__main__':raise SystemExit(main())
