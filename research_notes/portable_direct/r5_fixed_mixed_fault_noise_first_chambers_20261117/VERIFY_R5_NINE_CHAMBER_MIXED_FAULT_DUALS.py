#!/usr/bin/env python3
"""Certified exact integer duals for nine fixed mixed-fault analog-noise chambers.
Usage: python VERIFY_R5_NINE_CHAMBER_MIXED_FAULT_DUALS.py INPUT_COHORTS.json [EXACT_R5_ALL_101_BUDGETS.json]
No optimization library, floating arithmetic, or unpinned dynamic input required.
"""
import json, hashlib, sys
from pathlib import Path
PIN='435e77af0d180eac32bd1f9c4c464bc4010b7551'
INPUT_SHA='a781cf89e534587009e207e51bbda2f411e4147746f7d6a0b72a1354e80f0d4d'
FULL_SHA='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
TRIPLES=[(214,223,294),(214,223,295),(214,223,296),(215,223,296),
 (216,223,296),(216,223,297),(217,223,297),(217,224,297),(217,224,298)]
GAPS=[76289178155959966960189440,3133722521542003559403356160,
 13883516118328421520506880000,25845652773852463277015040000,
 58182461585441404127941754880,92195224223274674159616000000,
 267753525139190986466918400000,651779164849779092423599718400,
 1744659037213380157479321600000]
# Each row gives an exact integer dual certificate as [(state_a, state_b, weight),...]
# for early, middle, late disjoint witness families.
EARLY=[
 [(9,12,214)],[(9,12,214)],[(9,12,214)],
 [(2,8,1),(9,12,214)],
 [(1,2,214),(2,8,2)],
 [(0,1,213),(1,2,1),(2,8,2)],
 [(1,2,2),(1,8,214),(11,14,1)],
 [(1,2,2),(2,9,214),(11,14,1)],
 [(0,4,214),(1,2,2),(11,14,1)],
]
MIDDLE=[[(0,64,q[1])] for q in TRIPLES]
LATE=[[(16,32,q[2])] for q in TRIPLES]
DUALS=list(zip(EARLY,MIDDLE,LATE))

def checked(path,sha):
    raw=Path(path).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==sha
    return json.loads(raw)

def main():
    if len(sys.argv) not in (2,3): raise SystemExit(__doc__)
    compact=checked(sys.argv[1], INPUT_SHA)
    assert compact['scientific_input']==PIN
    T={}
    for k in range(214,315):
        x=[0]*256
        for m,v in compact['all_budget_coefficients'][str(k)].items():x[int(m)]=int(v)
        for bit in range(8):
            for m in range(256):
                if m & (1<<bit):x[m]+=x[m^(1<<bit)]
        T[k]=x
    if len(sys.argv)==3:
        full=checked(sys.argv[2],FULL_SHA)
        assert full['budget_range']==[214,314]
        for k in T:
            assert T[k]==[int(v) for v in full['counts_and_cohorts'][str(k)]['counts']]
    assert all(GAPS[i]<GAPS[i+1] for i in range(len(GAPS)-1))
    result=[]
    for stage,(q,dual) in enumerate(zip(TRIPLES,DUALS)):
        tau=0 if stage==0 else GAPS[stage-1]
        expected=q[0]+q[1]+q[2]
        assert [sum(w for _,_,w in group) for group in dual]==list(q)
        for k in range(214,315):
            dual_cover=sum(w for group in dual for a,b,w in group if abs(T[k][a]-T[k][b])>tau)
            assert dual_cover<=k, (stage,k,dual_cover)
        mind=None; saturating=0
        for a in range(256):
            for b in range(a+1,256):
                d=max(abs(T[k][a]-T[k][b]) for k in q)
                if mind is None or d<mind:
                    mind=d;saturating=1
                elif d==mind:
                    saturating+=1
        assert mind==GAPS[stage]
        assert tau<mind
        result.append({'stage':stage+1, 'tau_lower_inclusive':str(tau),
                       'tau_upper_exclusive':str(mind), 'budget_triple':list(q),
                       'cost_coefficient':expected, 'saturating_pairs':saturating,
                       'dual':[{'group':group_name,'witnesses':[[a,b,w] for a,b,w in group]}
                               for group_name,group in zip(('early','middle','late'),dual)]})
    print(json.dumps({'status':'PASS_R5_NINE_CHAMBER_ALL_EF_INTEGER_DUALS',
                      'frozen_science_pin':PIN,'masks':256,'budgets':101,
                      'exact_zeta_values':25856,
                      'exact_pair_triple_comparisons':9*32640,
                      'exact_dual_budget_inequalities':9*101,
                      'independent_full_table_crosscheck':len(sys.argv)==3,
                      'formula':'cost=(e+2f+1)*cost_coefficient in each chamber',
                      'intervals':result},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
