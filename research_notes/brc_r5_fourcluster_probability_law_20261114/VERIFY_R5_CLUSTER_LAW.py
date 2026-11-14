#!/usr/bin/env python3
"""Exact polynomial law for R5 minimum-center-count under iid gap closures.
Pure stdlib. Source formula: SPARSE_BOOLEAN_DECOMPOSITION.md, immutable
e47ab205e5e5cdbe4ae5801d95595635fd98204c. Derived 1D observer only.
"""
from itertools import product
from math import comb
from fractions import Fraction
import json

GROUPS=((2,3,4,5,6),(8,9,10,11,12,13),(16,),(25,26,27))

def gains(x):
    return (
        int(bool(x[5] or x[6])) + int(bool(x[2] and x[3] and x[4] and (not x[5] or x[6]))),
        int(bool(x[8] or x[9])) + int(bool(x[12] and (x[13] or (x[10] and x[11] and (x[8] or not x[9]))))),
        x[16], x[25]*x[26]*x[27],
    )

def trim(a):
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def add(a,b):
    c=[0]*max(len(a),len(b))
    for i,v in enumerate(a):c[i]+=v
    for i,v in enumerate(b):c[i]+=v
    return trim(c)

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return trim(c)

def mul_z(a,b):
    c={}
    for i,x in a.items():
        for j,y in b.items():c[i+j]=add(c.get(i+j,[0]),mul(x,y))
    return c

def evaluation(poly,p):
    return sum((Fraction(c)*p**i for i,c in enumerate(poly)),Fraction(0))

def pgf_for_group(group,index):
    n=len(group);out={}
    for bits in product((0,1),repeat=n):
        x={i:0 for G in GROUPS for i in G};x.update(zip(group,bits))
        g=gains(x)[index];k=sum(bits)
        basis=[0]*(n+1)
        for j in range(n-k+1):basis[k+j]=(-1)**j*comb(n-k,j)
        out[g]=add(out.get(g,[0]),basis)
    return out

def main():
    factor=[pgf_for_group(G,j) for j,G in enumerate(GROUPS)]
    expected_A={0:[1,-2,1,-1,2,-1],1:[0,2,-1,1,-3,1],2:[0,0,0,0,1]}
    expected_B={0:[1,-2,0,1,2,-3,1],1:[0,2,0,-3,-2,4,-1],2:[0,0,0,2,0,-1]}
    assert factor[0]==expected_A,(factor[0],expected_A)
    assert factor[1]==expected_B,(factor[1],expected_B)
    assert factor[2]=={0:[1,-1],1:[0,1]}
    assert factor[3]=={0:[1,0,0,-1],1:[0,0,0,1]}
    law={0:[1]}
    for G in factor:law=mul_z(law,G)
    assert sorted(law)==list(range(7))
    normal=[0]
    for val in law.values():normal=add(normal,val)
    assert normal==[1]
    EY=[0];EY2=[0]
    for gain,coeff in law.items():
        EY=add(EY,[gain*x for x in coeff])
        EY2=add(EY2,[gain*gain*x for x in coeff])
    meanD=add([213],[-c for c in EY])
    assert meanD==[213,-5,1,-3,3,-3,1]
    var=add(EY2,[-c for c in mul(EY,EY)])
    q=[5,-5,6,-4,11,-7,5,-6,6,-3,1]
    assert var==mul([0,1,-1],q),(var,q)
    var_der=[i*var[i] for i in range(1,len(var))]
    assert len(var_der)==12
    tpoly=[sum(var_der[j]*comb(11-j,k-j) for j in range(k+1)) for k in range(12)]
    assert tpoly==[5,35,108,182,193,179,199,145,18,-56,-35,-9],tpoly
    signs=[1 if v>0 else -1 for v in tpoly]
    assert sum(signs[i]!=signs[i+1] for i in range(11))==1
    l,r=Fraction(631922,10**6),Fraction(631923,10**6)
    assert evaluation(var_der,l)>0 and evaluation(var_der,r)<0
    half=Fraction(1,2)
    assert evaluation(meanD,half)==Fraction(13471,64)
    assert evaluation(var,half)==Fraction(4115,4096)
    fair_counts=[int(evaluation(law[k],half)*32768) for k in range(7)]
    assert fair_counts==[539,4298,11404,11462,4413,624,28],fair_counts
    report={
      "status":"PASS_EXACT_R5_FOUR_CLUSTER_FULL_LAW",
      "science_pin":"435e77af0d180eac32bd1f9c4c464bc4010b7551",
      "source_formula_commit":"e47ab205e5e5cdbe4ae5801d95595635fd98204c",
      "observer":"derived one-dimensional radius-2 minimum center count",
      "group_pgf_coefficients_p_ascending":[{str(k):v for k,v in sorted(g.items())} for g in factor],
      "gain_pgf_coefficients_p_ascending":{str(k):v for k,v in sorted(law.items())},
      "mean_D_coefficients_p_ascending":meanD,
      "variance_D_coefficients_p_ascending":var,
      "variance_quotient_Q_coefficients_p_ascending":q,
      "transformed_variance_derivative_t_coefficients_ascending":tpoly,
      "unique_variance_maximum_rational_bracket":["631922/1000000","631923/1000000"],
      "fair_closure_reduced_histogram_gain_0_to_6":fair_counts,
      "fair_closure_mean_D":"13471/64","fair_closure_variance_D":"4115/4096",
      "validation":"exact integer polynomial convolution, 106 cluster assignments, Descartes sign change and exact rational bracket; dependent on earlier frozen-event formula"
    }
    print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=="__main__":main()
