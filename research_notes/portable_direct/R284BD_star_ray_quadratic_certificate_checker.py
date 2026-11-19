#!/usr/bin/env python3
"""R284BD: exact exhaustive ray-certificate checker, Python stdlib only.

Completely enumerates 2^9 strictly positive binary 3x3 matrices.
Does not rely on a numerical determinant, random sample, remote service, or floats.
"""
from itertools import product
import json

RAY = (40, 47, 53, 55, 45)  # d0,d1,d2,z1,z2 at t=1
MATRICES = tuple(product((1, 2), repeat=9))
L = RAY[0] * RAY[1] * RAY[2]

def det3(m):
    a,b,c,d,e,f,g,h,i = m
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)

def response(c, t):
    a,b,c02,d,e,f,g,h,i = c
    d0,d1,d2,z1,z2 = (t*value for value in RAY)
    return det3((d0-a,-b-z1,-c02-z2,-d,d1-e,-f,-g,-h,d2-i))

def check():
    rows = []
    for index, c in enumerate(MATRICES):
        c0 = response(c,0)
        p1 = response(c,1)
        pm1 = response(c,-1)
        numer_a = p1+pm1-2*c0
        numer_b = p1-pm1-2*L
        assert numer_a%2 == numer_b%2 == 0
        a = numer_a//2
        b = numer_b//2
        for t in (-13,-2,-1,0,1,2,11,1155,4667,4671,5000):
            assert response(c,t)==L*t**3+a*t**2+b*t+c0
        rows.append({'index':index,'A':a,'B':b,'C':c0,'y4667':response(c,4667)})
    assert len(rows)==512
    assert len(set((r['A'],r['B']) for r in rows))==512
    ranges = {k:[min(r[k] for r in rows),max(r[k] for r in rows)] for k in ('A','B','C')}
    assert ranges=={'A':[-23042,-11521],'B':[-620,532],'C':[-5,5]}
    equal_a_pairs = []
    for i,x in enumerate(rows):
        for j in range(i+1,len(rows)):
            y=rows[j]
            if x['A']==y['A']:
                equal_a_pairs.append((abs(x['B']-y['B']),i,j))
    assert len(equal_a_pairs)==3840
    smallest_slope = min(x[0] for x in equal_a_pairs)
    assert smallest_slope==3
    scale_results={}
    for t in (1,1155,4667,4671,5000):
        vals=sorted((response(c,t),i) for i,c in enumerate(MATRICES))
        min_gap=min(vals[j][0]-vals[j-1][0] for j in range(1,512))
        witness=next((vals[j-1][1], vals[j][1]) for j in range(1,512) if vals[j][0]-vals[j-1][0]==min_gap)
        assert min_gap>0
        scale_results[str(t)]={'t':t,'max_control':55*t,'distinct':512,'min_gap':min_gap,
            'min_output':vals[0][0],'max_output':vals[-1][0],
            'max_abs_output_bits':max(abs(v).bit_length() for v,i in vals),'nearest_pair_indices':list(witness)}
    assert scale_results['1']['min_gap']==1
    assert scale_results['1155']['min_gap']==3465
    assert scale_results['4667']['min_gap']==14001
    assert scale_results['4671']['min_gap']==14013
    assert scale_results['5000']['min_gap']==15000
    assert 14001>2*7000
    assert 55*4667==256685
    assert max(r['B'] for r in rows)-min(r['B'] for r in rows)==1152
    assert max(r['C'] for r in rows)-min(r['C'] for r in rows)==10
    # For every t>=1155, all pairs obey |difference| >= 3*t-10.
    # This follows by splitting Delta A != 0 or Delta A == 0, and not by sampled t values.
    for t in (1155,4667,4671,5000):
        assert t*t-1152*t-10>=3*t-10
        assert scale_results[str(t)]['min_gap'] >= 3*t-10
    return {'schema':'R284BD_EXACT_RAY_CERTIFICATE_V1','date':'2026-11-20',
        'status':'PASS','independent_review':'NOT_REVIEWED',
        'scope':'fixed three-channel integer star-Port auxiliary determinant; C in {1,2}^(3x3)',
        'candidate_count':512,'controls_direction':list(RAY),'common_cubic_coefficient':L,
        'coefficient_pair_distinct':512,'coefficient_ranges':ranges,
        'equal_A_pairs':len(equal_a_pairs),'minimum_equal_A_B_difference':smallest_slope,
        'output_gap_rigorous_lower_bound':'For every integer t>=1155, gap >=3*t-10',
        'scale_results':scale_results,'rows':rows,
        'all_rows_check_polynomial_at_t':[-13,-2,-1,0,1,2,11,1155,4667,4671,5000],
        'computation':'exact Python int, complete matrix enumeration, explicit 3x3 Leibniz determinant',
        'footnote':'Coefficient row index is zero-based lexicographic product((1,2),repeat=9); no NATIVE_X6 or physical model inference.'}

if __name__ == '__main__':
    data=check()
    out=json.dumps(data,ensure_ascii=False,separators=(',',':'),sort_keys=True)+'\n'
    print(out,end='')
