#!/usr/bin/env python3
"""Finite 2**32 carrier checks; synthetic tick schedule, not Phase32 caller admission."""
from __future__ import annotations
import json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'tools/nollm_visual_toolkit')]
from nollm_visual_toolkit import certified_hex as c
M=1<<32;G=2654435761

def main():
    rows=[]
    for count in (1024,4096):
        phi=[None]+[(n*G)%M for n in range(1,count)]
        for n,d in ((1,2),(1,1),(3,2)):
            rec=c.certified_population(phi,n,d,phase_modulus=M,initial_bits=64,max_bits=192)
            rows.append({'count':count,'scale':[n,d],'status':rec['status'],
                'unresolved':len(rec['unresolved_identities']),'occupied_cells':rec['occupied_cells'],
                'precision_counts':rec['precision_counts'],'phase_modulus':rec['phase_modulus']})
    record={'schema':'M16_PHASE32_SYNTHETIC_POPULATION_V1','schedule':'tick[n]=n*2654435761 mod 2**32; not phase32_lab composite valuation schedule',
        'rows':rows,'all_certified':all(r['status']=='CERTIFIED_ALL' for r in rows),
        'all_at_initial_64_bits':all(r['precision_counts']=={'64':str(r['count'])} for r in rows),
        'finite_not_universal':True}
    out=ROOT/'evidence/migration16';out.mkdir(parents=True,exist_ok=True);(out/'population_matrix.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record,indent=2));return 0
if __name__=='__main__':raise SystemExit(main())
