#!/usr/bin/env python3
"""C297: rigorous a priori dyadic width and dyadic-grid nonzero-sign
termination bound for the 125 frozen C293 path strips.

Stdlib-only; exact rational arithmetic throughout. This proves arithmetic
statements solely about the C195/H168 79-branch positive auxiliary F/Q.
It does not infer root existence, uniqueness, native BRC, or formal admission.
"""
import json,hashlib
from fractions import Fraction as R
from math import lcm
from pathlib import Path
import C275_STANDALONE_EXACT_REPLAY as src
import C288_ISOLATING_BOXES_EXACT as c288
from C296_DYADIC_INTERVAL_SIGNS import PositiveDyadicEvaluator

CANON=lambda x:json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode('utf-8')

def ceilq(x):
    return -(-x.numerator//x.denominator)

def poly_add(a,b):
    return [ (a[i] if i<len(a) else R(0))+(b[i] if i<len(b) else R(0)) for i in range(max(len(a),len(b)))]

def poly_mul(a,b):
    z=[R(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]+=x*y
    return z

def poly_eval(a,t):
    z=R(0)
    for x in reversed(a):z=z*t+x
    return z

def normalize_pair(n,d):
    """Rational-coefficient polynomial ratio -> integer N,D with SAME factor."""
    L=1
    for x in n+d:L=lcm(L,R(x).denominator)
    N=[int(L*R(x)) for x in n]
    D=[int(L*R(x)) for x in d]
    assert any(N) and any(D)
    return N,D

def polyl1(a):return sum(abs(v) for v in a)

def oriented(a,b,tlo,thi):
    assert poly_eval(a,tlo)>0 and poly_eval(a,thi)>0
    v0=poly_eval(b,tlo);v1=poly_eval(b,thi)
    assert v0 and v1 and (v0>0)==(v1>0)
    if v0<0:b=[-x for x in b]
    N,D=normalize_pair(a,b)
    assert poly_eval(D,tlo)>0 and poly_eval(D,thi)>0
    assert poly_eval(N,tlo)>0 and poly_eval(N,thi)>0
    return polyl1(D)

def base_poly_dnorm(w,d,tlo,thi):
    p=[w,d]
    sq=poly_mul(p,p)
    a=poly_add([R(2)],[-x for x in sq]); b=poly_add([R(3)],[-x for x in sq])
    ab=poly_mul(a,b)
    den=poly_mul(poly_mul(ab,ab),ab)
    assert poly_eval(den,tlo)>0 and poly_eval(den,thi)>0
    N,D=normalize_pair([src.A/src.H],den)
    assert poly_eval(D,tlo)>0 and poly_eval(D,thi)>0
    return polyl1(D)

def exact_records():
    raw=json.loads(Path('C293_125_REFINED_BRACKETS.json').read_text())
    assert len(raw['records'])==125
    assert hashlib.sha256(CANON(raw['records'])).hexdigest()==raw['records_sha256']
    paths,_=c288.build_paths()
    assert len(paths)==len(raw['records'])==125
    W,_=src.floor_fixed_masses()
    evaluator=PositiveDyadicEvaluator(W)
    result=[]
    for i,(row,path) in enumerate(zip(raw['records'],paths)):
        assert row[0]==i
        tlo=R(row[1],1<<24);thi=R(row[1]+1,1<<24)
        v0=tuple(w+tlo*d for w,d in zip(path['w'],path['d']))
        v1=tuple(w+thi*d for w,d in zip(path['w'],path['d']))
        assert 0<=tlo<thi<=1 and src.valid(v0) and src.valid(v1)
        # Affine coordinate and pole-gap predicates are strict at both endpoints;
        # the region between is valid by convexity of these linear constraints.
        assert all(src.U[k-1]<vv[x]<src.U[k+1] for vv in (v0,v1) for x,k in enumerate(src.I))
        assert all(vv[x]<vv[x+1] for vv in (v0,v1) for x in range(3))
        width_total=0
        height_bits=0
        for _,node,c in evaluator.fixed:
            width=1
            height_bits+=c.denominator.bit_length()
            for x,(w,d) in enumerate(zip(path['w'],path['d'])):
                r0=(src.Z-v0[x])/abs(node-v0[x]);r1=(src.Z-v1[x])/abs(node-v1[x]);Rmax=max(r0,r1)
                # Ratio of affine functions with fixed-sign denominator is monotone.
                width=ceilq(width*Rmax)+2
                height_bits+=oriented([src.Z-w,-d],[node-w,-d],tlo,thi).bit_length()
            width_total+=width
        for k,(w,d) in enumerate(zip(path['w'],path['d'])):
            width=1
            height_bits+=base_poly_dnorm(w,d,tlo,thi).bit_length()
            for j in src.J:
                r0=(src.Z-src.U[j])/abs(v0[k]-src.U[j]);r1=(src.Z-src.U[j])/abs(v1[k]-src.U[j]);Rmax=max(r0,r1)
                width=ceilq(width*Rmax)+2
                height_bits+=oriented([src.Z-src.U[j]],[w-src.U[j],d],tlo,thi).bit_length()
            for m,(wm,dm) in enumerate(zip(path['w'],path['d'])):
                if m==k:continue
                r0=(src.Z-v0[m])/abs(v0[k]-v0[m]);r1=(src.Z-v1[m])/abs(v1[k]-v1[m]);Rmax=max(r0,r1)
                width=ceilq(width*Rmax)+2
                height_bits+=oriented([src.Z-wm,-dm],[w-wm,d-dm],tlo,thi).bit_length()
            width_total+=width
        # Every source term has rational numerator/denominator polynomial degrees
        # fixed<=4 and moving<=12+75+3=90; sum over 75+4 terms <=660.
        assert width_total<1<<134,(i,width_total)
        result.append({'index':i,'C293_k24':str(row[1]),'max_sum_interval_width_integer_units':str(width_total),
                       'log2_common_positive_denominator_bound_bits':height_bits,
                       'nonzero_grid_sign_sufficient_precision':'P=660*b+H_i+134',
                       'H_i':height_bits})
    maximal_width=max(int(x['max_sum_interval_width_integer_units']) for x in result)
    maxh=max(x['H_i'] for x in result)
    audit={'schema':'EM_C297_UNIFORM_WIDTH_AND_HEIGHT_CERTIFICATE_V1',
           'model':'C195_H168_79_NODE_POSITIVE_RATIONAL_AUXILIARY',
           'paths':125,'strips':'C293_125_DYADIC_2^-24',
           'input_C293_records_sha256':raw['records_sha256'],
           'input_C284_records_sha256':c288.SOURCE_CERT_SHA,
           'uniform_width_strict_upper_power_of_two':134,
           'max_width_integer_units_exact':str(maximal_width),
           'max_denominator_height_bound_bits':maxh,
           'uniform_nonzero_dyadic_grid_precision_formula':f'P=660*b+{maxh}+134',
           'nonzero_only':True,
           'note':'Endpoint t at which f(t)=1 has zero margin; finite strict-sign certificate is impossible at equality.',
           'arithmetic':'Python Fraction and integer arithmetic; bounds cover all real t in each C293 short strip, all P>=0',
           'status':'AUTHOR_EXACT_CERTIFICATE_NOT_ADMITTED'}
    Path('C297_125_UNIFORM_WIDTH_AND_HEIGHT_AUDIT.json').write_text(json.dumps(audit,sort_keys=True,ensure_ascii=False,indent=2)+'\n')
    Path('C297_125_PATHWISE_BOUNDS.json').write_text(json.dumps({'schema':'EM_C297_PATHWISE_EXACT_BOUNDS_V1','records':result},ensure_ascii=False,indent=2,sort_keys=True)+'\n')
    print('C297_UNIFORM_WIDTH_HEIGHT_125_PASS',json.dumps(audit,sort_keys=True),flush=True)
    return audit

if __name__=='__main__':exact_records()
