#!/usr/bin/env python3
"""PREFIX-283: exact C4 ordered-source-pair BRC detector witness.

This executes a declared formal source-pair BRC observer, not the archived
Stage50 executable and not a native Heartbeat World detector.
Only Fraction arithmetic and Gaussian-rational ordered pairs are used.
"""
from __future__ import annotations
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

ZERO=(F(0), F(0)); ONE=(F(1), F(0))
C4=(ONE,(F(0),F(1)),(F(-1),F(0)),(F(0),F(-1)))
A=(-1,0,1)

def z(v):
    return (F(v),F(0)) if not isinstance(v,tuple) else (F(v[0]),F(v[1]))

def plus(x,y): return (x[0]+y[0],x[1]+y[1])
def conj(x): return (x[0],-x[1])
def mult(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def norm2(x): return x[0]*x[0]+x[1]*x[1]

def brc(a, E):
    """Full ordered pair sum, including diagonal, source and C4 identity."""
    assert len(E)==len(a) and all(len(r)==len(a) for r in E)
    Z=sum((norm2(x) for x in a),F(0))
    assert Z>0
    s=ZERO
    for j,x in enumerate(a):
        for k,y in enumerate(a):
            s=plus(s,mult(mult(conj(x),E[j][k]),y))
    assert s[1]==0,(s,E)
    return s[0]/Z

def toeplitz(d,lag1,lag2):
    ls=[z(d),z(lag1),z(lag2)]
    return [[ls[k-j] if k>=j else conj(ls[j-k]) for k in range(3)] for j in range(3)]

def general(diags,u01,u02,u12):
    D=[z(v) for v in diags]
    E=[[ZERO for k in range(3)] for j in range(3)]
    for j in range(3):E[j][j]=D[j]
    for (j,k),v in [((0,1),u01),((0,2),u02),((1,2),u12)]:
        E[j][k]=z(v);E[k][j]=conj(z(v))
    return E

def witness(E):
    """Closed-form contrast from exact ordered-pair coefficients."""
    return (-3*E[0][0][0]-9*E[1][1][0]+12*E[2][2][0]
            -12*E[0][1][0]+12*E[1][2][0])/F(33)

def enc(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,(tuple,list)):return [enc(t) for t in x]
    if isinstance(x,dict):return {str(k):enc(v) for k,v in x.items()}
    return x

def main():
    f=[z(v) for v in (1,4,4)]
    g=[z(v) for v in (2,5,2)]
    C=lambda a,r:sum((mult(a[j],conj(a[j+r]))[0] for j in range(len(a)-r)),F(0))
    assert [C(f,r) for r in range(3)]==[C(g,r) for r in range(3)]==[F(33),F(20),F(4)]
    cases=0
    toeplitz_count=0
    for d in A:
      for u in itertools.product(A,repeat=2):
        for v in itertools.product(A,repeat=2):
          E=toeplitz(d,u,v)
          assert brc(f,E)==brc(g,E)
          assert witness(E)==0
          toeplitz_count+=1
    hermitian_count=0
    cg=[z(u) for u in itertools.product(A,repeat=2)]
    for d in itertools.product(A,repeat=3):
      for u01 in cg:
        for u02 in cg:
          for u12 in cg:
            E=general(d,u01,u02,u12)
            assert brc(f,E)-brc(g,E)==witness(E)
            hermitian_count+=1
    masks=[]
    for d in itertools.product((0,1),repeat=3):
        E=general(d,ZERO,ZERO,ZERO)
        pf,pg=brc(f,E),brc(g,E)
        expected=F(-d[0]-3*d[1]+4*d[2],11)
        assert pf-pg==expected
        masks.append({'source_mask':list(d),'p_f':pf,'p_g':pg,'delta':pf-pg})
    best=max(abs(a['delta']) for a in masks)
    assert best==F(4,11)
    assert sum(abs(f[j][0]**2-g[j][0]**2) for j in range(3))/F(2*33)==best
    for c4 in C4:
        f2=[mult(c4,x) for x in f]
        g2=[mult(c4,x) for x in g]
        for d in itertools.product((0,1),repeat=3):
            E=general(d,ZERO,ZERO,ZERO)
            assert brc(f2,E)==brc(f,E)
            assert brc(g2,E)==brc(g,E)
            cases+=1
    values={
        'schema':'PREFIX283_FORMAL_C4_BRC_DETECTOR_EFFECT_WITNESS_V1',
        'status':'EXACT_AUTHOR_SIDE_CHECK_PASS__NO_NATIVE_DETECTOR_LAW',
        'model':'fixed-source, exact C4 gaussian-rational amplitude, ordered-source-pair BRC observer',
        'input_packets':{'f':[1,4,4],'g':[2,5,2]},
        'source_labels':[0,1,2],
        'Z':33,'autocorrelation':[33,20,4],
        'contrast_Q_numerator':[[-3,-6,0],[-6,-9,6],[0,6,12]],
        'general_hermitian_effects_tested':hermitian_count,
        'coefficient_domain':{'diagonals':list(A),'offdiagonal_re_im':list(A)},
        'toeplitz_hermitian_effects_tested':toeplitz_count,
        'source_binary_masks_tested':len(masks),'masks':masks,
        'max_source_mask_probability_gap':best,
        'optimal_masks':[m['source_mask'] for m in masks if abs(m['delta'])==best],
        'equal_prior_optimal_single_source_sample_success':(F(1)+best)/2,
        'global_C4_phase_invariance_checks':cases,
        'source_observation':'conditional source-addressed detector E=diag(mask); Stage50 packet_variance is source-visible software inspection, not established native measurement',
        'not_executed':['original_stage50_bundle_this_run','native_heartbeat_detector','full_model_law_id_Hn_to_Hn+1'],
        'reused_evidence':'PREFIX-282 verified original Stage50 40-call separation; not rerun or counted',
        'next':'PREFIX-284 seek actual sourced native detector E or prove restricted observable algebra; map Cell/Port/field/source/boundary/time with model_law_id'
    }
    output=enc(values)
    Path(__file__).with_name('RESULTS_PREFIX283.json').write_text(json.dumps(output,ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps({'status':'PREFIX283_EXACT_C4_BRC_PASS','hermitian':hermitian_count,'toeplitz':toeplitz_count,'binary_masks':len(masks),'c4_checks':cases,'max_gap':str(best)},ensure_ascii=False))

if __name__=='__main__':main()
