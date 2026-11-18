#!/usr/bin/env python3
"""Exact proof certificate for two remaining high-noise chambers of R5.

Usage: python VERIFY_R5_HIGH_NOISE_MIXED_FAULT.py INPUT_COHORTS.json [EXACT_R5_ALL_101_BUDGETS.json]
Input is immutable, SHA256 checked. Only exact Python integers are used.
"""
import json, hashlib, sys
from pathlib import Path

PIN='435e77af0d180eac32bd1f9c4c464bc4010b7551'
INPUT_SHA='a781cf89e534587009e207e51bbda2f411e4147746f7d6a0b72a1354e80f0d4d'
FULL_SHA='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
D3=1744659037213380157479321600000
H=1752576979999614335377735680000
D4=1882951873548292168718745600000
CHAMBERS=[
    (D3,H, (215,218,224,298), [(3,4,215),(4,10,218),(0,64,224),(16,32,298)]),
    (H,D4, (217,218,224,298), [(11,14,217),(4,10,218),(0,64,224),(16,32,298)]),
]

def checked(path,sha):
    raw=Path(path).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==sha,(path,'SHA256 mismatch')
    return json.loads(raw)

def reconstruct(compact):
    assert compact['scientific_input']==PIN
    assert len(compact['all_budget_coefficients'])==101
    counts={}
    for k in range(214,315):
        row=[0]*256
        for m,v in compact['all_budget_coefficients'][str(k)].items():
            row[int(m)]=int(v)
        for bit in range(8):
            for m in range(256):
                if m&(1<<bit):row[m]+=row[m^(1<<bit)]
        counts[k]=row
    return counts

def run(compact,full=None):
    T=reconstruct(compact)
    if full is not None:
        assert full['budget_range']==[214,314]
        for k,row in T.items():
            assert row==[int(v) for v in full['counts_and_cohorts'][str(k)]['counts']]
    out=[]
    for lo,hi,Q,dual in CHAMBERS:
        assert sum(w for _,_,w in dual)==sum(Q)
        # Upper certificate: 256 choose 2 exact pair comparisons.
        min_gap=None; saturating=[]
        for a in range(256):
            for b in range(a+1,256):
                gap=max(abs(T[k][a]-T[k][b]) for k in Q)
                if min_gap is None or gap<min_gap:
                    min_gap=gap;saturating=[[a,b]]
                elif gap==min_gap:
                    saturating.append([a,b])
        assert min_gap==hi,('upper certificate',lo,hi,min_gap)
        # Integer dual: 101 inequalities at inclusive left endpoint.
        for k in range(214,315):
            lhs=sum(w for a,b,w in dual if abs(T[k][a]-T[k][b])>lo)
            assert lhs<=k,('dual',lo,k,lhs)
        out.append({
            'tau_min_inclusive':str(lo),'tau_max_exclusive':str(hi),
            'budget_tuple':list(Q),'cost_coefficient':sum(Q),
            'saturating_pair_count':len(saturating),
            'saturating_pairs':saturating,
            'dual_witnesses':[[a,b,w] for a,b,w in dual],
            'dual_checked_budgets':101,'exact_pairs_checked':32640,
        })
    # Global obstruction: same candidate pair has no strong difference at or above D4.
    obstruction=(11,14)
    max_ob=max(abs(T[k][obstruction[0]]-T[k][obstruction[1]]) for k in T)
    assert max_ob==D4,('global obstruction',max_ob)
    witness_budgets=[k for k in T if abs(T[k][11]-T[k][14])==D4]
    assert witness_budgets==[217]
    return {
        'status':'PASS_R5_HIGH_NOISE_ALL_EF_CERTIFICATES',
        'scientific_input':PIN,
        'scope':{'budgets':[214,314], 'masks':256, 'pairs':32640, 'noise_parameter':'tau=2*eta',
                 'fault_multiplicity':'r=e+2*f+1 for all nonnegative e,f',
                 'cost':'sum of queried budget integers'},
        'exact_integer_counts':25856,
        'compared_with_independent_full_table':full is not None,
        'new_chambers':out,
        'global_impossibility':{'tau_min_inclusive':str(D4),'pair':[11,14],
                                'max_gap':str(max_ob),'max_gap_budgets':witness_budgets},
        'previous_nine_chamber_certificate_sha':'b369e8452f3a4f0e21167b30684629bb98f625c2',
    }

def main():
    if len(sys.argv) not in (2,3):raise SystemExit(__doc__)
    compact=checked(sys.argv[1],INPUT_SHA)
    full=checked(sys.argv[2],FULL_SHA) if len(sys.argv)==3 else None
    print(json.dumps(run(compact,full),ensure_ascii=False,indent=2))

if __name__=='__main__':main()
