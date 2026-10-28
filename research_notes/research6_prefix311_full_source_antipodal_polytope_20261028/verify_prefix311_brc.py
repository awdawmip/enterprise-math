#!/usr/bin/env python3
"""Direct tagged-source BRC Q_0/Q_1/Q_i path-pair witness verification.
Requires local PREFIX311_RESULTS_ten.json and PREFIX311_RESULTS_eight.json
and p311_full.py; executes separately from vertex enumerator logic.
"""
import json
from fractions import Fraction as F
from p311_full import S4,S7,E
from pathlib import Path
Q=[(1,0),(0,1),(-1,0),(0,-1)]
Z=(F(0),F(0)); one=(F(1),F(0)); ii=(F(0),F(1))
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def mul(x,y):return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def conj(z):return (z[0],-z[1])
def scale(x,s):return (x[0]*s,x[1]*s)
def op(z,ref=None):
    paths=list(z)
    if ref is not None:paths.append(ref)
    # Exact ordered source-pair BRC mass; all origins retained even if zero.
    mass=Z
    for p in paths:
      for t in paths:
        mass=add(mass,mul(p,conj(t)))
    assert mass[1]==0 and mass[0]>=0
    return mass[0],len(paths)**2

def row_paths(row,v,qpow):
    # row has 3 integer Gaussian coefficients; source v/2; phase
    # inserted by D(q)=diag(1,q,q^2), total denominator 16.
    return [scale(mul(mul((F(c[0]),F(c[1])),qpow[j]),v[j]), F(1,16)) for j,c in enumerate(row)]

def parse_v(arr):return [(F(arr[2*i]),F(arr[2*i+1])) for i in range(3)]
def main():
    result=[]; count=0; masses=0; pairs=0; overlaps=0; basematch=0
    for mode in ('ten','eight'):
      data=json.loads((Path(__file__).resolve().parent / f'PREFIX311_RESULTS_{mode}.json').read_text())
      for r in data['results']:
        M=(S4 if r['family']=='S4' else S7)[r['orbit']-1]
        omit=None if r['omit'] is None else int(r['omit'][-1])-1
        ports=E + [[(re,im) for re,im in row] for row in M]
        measured=[0,1]+[i+2 for i in range(3) if i!=omit]
        base_v=parse_v(r['witness_v'])
        risk=sum(x*x+y*y for x,y in base_v)/4
        assert risk==F(r['gain'])
        for qi,q0 in enumerate(Q):
            q=(F(q0[0]),F(q0[1]));q2=mul(q,q)
            qpow=[one,q,q2];qinv=[conj(z) for z in qpow]
            v=[mul(z,qinv[j]) for j,z in enumerate(base_v)]
            vals={}
            for sign in (-1,1):
                trueports=[]
                for row in ports:
                    amplitudes=row_paths(row,v,qpow)
                    if sign<0:amplitudes=[scale(a,F(-1)) for a in amplitudes]
                    val,ct=op(amplitudes)
                    masses+=1;pairs+=ct
                    trueports.append((amplitudes,val))
                vals[sign]=trueports
            for j in range(5):
                assert vals[-1][j][1]==vals[1][j][1];basematch+=1
            for j in measured:
                for ref in (one,ii):
                    neg,n=op(vals[-1][j][0],ref)
                    pos,m=op(vals[1][j][0],ref)
                    assert m==n
                    masses+=2;pairs+=m+n
                    assert abs(pos-neg)<=2, (mode,r['family'],r['orbit'],q0,j,ref,abs(pos-neg))
                    overlaps+=1
            count+=1
            result.append([mode,r['family'],r['orbit'],qi,r['omit'],r['gain']])
    summary={'configurations_and_menus_including_4_phases':count,'base_mass_pair_equalities':basematch,'reference_interval_overlap_checks':overlaps,'direct_brc_mass_evaluations':masses,'tagged_ordered_source_pair_products':pairs,'coverage':'12 orbit representations * 4 C4 phases * (10-ref + 3 possible 8-ref menus) =192 cases; both antipodal states','result':'PASS'}
    (Path(__file__).resolve().parent / 'PREFIX311_BRC_CHECK.json').write_text(json.dumps(summary,indent=2))
    print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
