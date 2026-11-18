#!/usr/bin/env python3
"""PREFIX-904 complete two-source gap census (Python stdlib, exact integers).
Frozen science: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Run: python3 PREFIX904_R6_TWO_SOURCE_GAP_CENSUS.py > PREFIX904_R6_TWO_SOURCE_GAP_RESULTS.json
The 241 gap rows enumerate all covered positive ordered pairs; every witness
is reconstructed and checked, not sampled. E/P follow PREFIX-897/902.
"""
import json
from math import gcd
from collections import defaultdict

p=32
N=1<<p
T=33*N
LO,HI=262145,524287
Q=range(LO,HI+1,2)
COUNT=len(Q)
S={262147,280001,300001,320003,340007,360007,380003,400009,
   420001,440003,460001,480007,500383,510007,520001,524285}
P={510000+k+194*j for k in (1,3,5) for j in range(64)}
assert len(P)==192 and all(x in Q for x in P)
U=S | set(range(400011,400522,2)) | set(range(480011,480522,2))
U.update(q for q in Q if any(((1<<h)-1)%q==0 or ((1<<h)+1)%q==0
                              for h in range(1,32)))
assert len(U)==552 and not P&U
representations={}
for i in range(2,18):
    for j in range(1,i):
        for d,mode in (((1<<i)+(1<<j),'sum'),
                       ((1<<i)-(1<<j),'difference')):
            if d<=HI-LO:
                representations.setdefault(d,(i,j,mode))
dyadic={1<<h for h in range(1,18)}
gaps=sorted(set(representations)-dyadic)
assert len(gaps)==241

def covered_E(a,b):
    return (a*b<T or a in U or b in U or
            a//gcd(a,b)*b<N or
            33*((N+a-1)//a)>b or 33*((N+b-1)//b)>a)

def witness(a,b,i,j,mode):
    h=1<<j
    big=1<<i
    m=2*h
    if mode=='sum':
        x=(h-a%m)%m
        y=x+a
        v=y-h
        assert (y>>j)&1 and a-b==big+h
    else:
        x=(-a)%m
        y=x+a
        v=y+h
        assert ((y>>j)&1)==0 and a-b==big-h
    assert 0<=x<big and y<N and x+big<N and 0<=v<N
    assert (x^big)==x+big and (y^h)==v
    assert x%a==y%a and (x+big)%b==v%b
    return dict(a=a,b=b,i=i,j=j,mode=mode,x=x,y=y,
                first_end=x+big,second_end=v)

def main():
    rows=[]
    total=defaultdict(int)
    example=None
    for d in gaps:
        i,j,mode=representations[d]
        row=dict(d=d,i=i,j=j,mode=mode,pairs=0,E=0,P=0,
                 E_and_P=0,already_C902=0,new_C903=0)
        for a in range(LO+d,HI+1,2):
            b=a-d
            w=witness(a,b,i,j,mode)
            e=covered_E(a,b)
            panel=(a in P or b in P)
            row['pairs']+=1
            row['E']+=e
            row['P']+=panel
            row['E_and_P']+=e and panel
            row['already_C902']+=e or panel
            if not (e or panel):
                row['new_C903']+=1
                if example is None: example=w
        assert row['pairs']==COUNT-d//2
        assert row['already_C902']==row['E']+row['P']-row['E_and_P']
        assert row['new_C903']==row['pairs']-row['already_C902']
        rows.append(row)
        for k in ('pairs','E','P','E_and_P','already_C902','new_C903'):
            total[k]+=row[k]
    assert total['pairs']==sum(COUNT-d//2 for d in gaps)
    assert total['pairs']==total['already_C902']+total['new_C903']
    previous=7617211750
    added=2*total['new_C903']
    certified=previous+added
    assert certified<=COUNT**2
    return {
        'schema':'PREFIX904_R6_TWO_SOURCE_NONDYADIC_GAP_CERT_V1',
        'scientific_input_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
        'model':{'p':32,'N':N,'Q_first':LO,'Q_last':HI,'Q_size':COUNT,
                 'legal_trajectories':'Z_x and named F_x^i=(x,x XOR 2^i)',
                 'observer':'(start mod a, end mod b)'},
        'covered_gap_types':len(gaps),
        'gap_class_formula':'d=2^i +/- 2^j for 1<=j<i<=17, excluding dyadic d',
        'positive_gap_summary':dict(total),
        'ordered_gap_pairs':2*total['pairs'],
        'ordered_prior_union_intersection':2*total['already_C902'],
        'ordered_new_pairs_relative_to_PREFIX903':added,
        'prior_PREFIX903_union':previous,
        'certified_904_union':certified,
        'complement_outside_explicit_union':COUNT**2-certified,
        'first_new_concrete_witness':example,
        'gaps':rows
    }

if __name__=='__main__':
    print(json.dumps(main(),ensure_ascii=False,indent=2))
