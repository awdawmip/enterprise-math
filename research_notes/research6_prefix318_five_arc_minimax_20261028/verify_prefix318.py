#!/usr/bin/env python3
"""PREFIX-318: exact continuous five-arc auxiliary tagged-BRC minimax certificate.

Inputs: frozen PREFIX-317/S7-3 static five-port report, q=1, r=25/54.
Proof arithmetic: SymPy rational radicals and exact sign decisions, no sampling,
no trigonometric/model-time operations. All BRC masses use ordered labeled pairs.
"""
from __future__ import annotations
import json
from pathlib import Path
import sympy as S
from functools import cmp_to_key

Q=S.Rational; I=S.I
r=Q(25,54)
A=S.Matrix([[4,4,0],[0,-4,4],[-5+3*I,0,-3+I],[-2-2*I,4+4*I,2+2*I],[-2,0,5+2*I]])
b0=S.Matrix([-2,-2*I,1]); b2=S.Matrix([2*I,2,-I])
Q0=S.Matrix([Q(x) for x in ['625/1458','3125/11664','23125/93312','15625/23328','53125/186624']])
Q1=S.Matrix([Q(x) for x in ['2083/1458','14789/11664','32089357/29206656','7073089/7301664','251845/186624']])
Qi=S.Matrix([Q(x) for x in ['720235/456354','3477137/3650832','37487629/29206656','17311489/7301664','90898861/58413312']])
alpha=(Q1-Q0-S.ones(5,1))/2
beta=(Qi-Q0-S.ones(5,1))/2

def simp(x): return S.simplify(S.expand_complex(x))
def sg(x):
    x=simp(x)
    if x==0 or x.is_zero: return 0
    if x.is_positive: return 1
    if x.is_negative: return -1
    y=S.sign(x)
    if y in (-1,0,1): return int(y)
    raise AssertionError('undecidable exact sign '+str(x))

def re(z):return simp(S.re(z))
def im(z):return simp(S.im(z))
def dot(v,w):return simp(S.re((v.conjugate().T*w)[0]))
def norm2(v):return dot(v,v)
def mirror(z):return simp(-I*S.conjugate(z))
def pt(z):return (re(z),im(z))
def xy(z):return z[0]+I*z[1]

def restrictions(b):
    """Each (name,(n_x,n_y),target) imposes n_x*x+n_y*y <= target."""
    w=r*A*b/8
    out=[]
    for j,z in enumerate(w):
        p,q=re(z),im(z)
        for label,normal,target in [('re',(p,-q),alpha[j]),('im',(q,p),beta[j])]:
            out.extend([(f'port{j+1}:{label}:upper',normal,target+Q(1,2)),
                        (f'port{j+1}:{label}:lower',tuple(-n for n in normal),-target+Q(1,2))])
    return out

def feasible(lines,z):
    x,y=z
    return all(sg(a*x+b*y-t)<=0 for _,(a,b),t in lines)

def unit_line_intersections(a,b,t):
    D=simp(a*a+b*b)
    assert sg(D)>0
    delta=simp(D-t*t)
    if sg(delta)<0:return []
    h=S.sqrt(delta)
    return [(simp((t*a-e*b*h)/D),simp((t*b+e*a*h)/D))
            for e in ((1,) if sg(delta)==0 else (-1,1))]

def half(z):
    y=sg(z[1]);return 0 if y>0 or (y==0 and sg(z[0])>=0) else 1

def cmp(z,w):
    a,b=half(z),half(w)
    if a!=b:return -1 if a<b else 1
    return -sg(simp(z[0]*w[1]-z[1]*w[0]))

def arc_witness(a,b,wrap):
    if wrap:return (Q(1),Q(0))
    ha,hb=half(a),half(b)
    if ha!=hb:return (Q(-1),Q(0)) if ha==0 else (Q(1),Q(0))
    ta=simp(a[1]/(1+a[0]));tb=simp(b[1]/(1+b[0]))
    assert sg(tb-ta)>0
    for d in [1,10,100,1000,10000,100000,1000000]:
        n=int(S.floor(ta*d))+1;t=Q(n,d)
        if sg(t-ta)>0 and sg(tb-t)>0:
            return ((1-t*t)/(1+t*t),2*t/(1+t*t))
    raise AssertionError('no rational open arc witness')

def arcs(b):
    lines=restrictions(b)
    # All 20 boundary lines and every real intersection with unit circle,
    # including points that fail other inequalities: exact finite coverage.
    all_points=[]
    for _,(a,c),t in lines:all_points+=unit_line_intersections(a,c,t)
    endpoints=[]
    for z in all_points:
        if feasible(lines,z) and not any(cmp(z,w)==0 for w in endpoints):
            endpoints.append(z)
    endpoints.sort(key=cmp_to_key(cmp))
    intervals=[]
    for i,a in enumerate(endpoints):
        j=(i+1)%len(endpoints);b_=endpoints[j]
        witness=arc_witness(a,b_,j==0)
        if j!=0:assert cmp(a,witness)<0 and cmp(witness,b_)<0
        intervals.append({'start':a,'end':b_,'open_witness':witness,
                          'feasible':feasible(lines,witness)})
    return len(all_points), endpoints, intervals

# Exact endpoints: first Port imaginary band = beta_1 +/- 1/2.
kP=simp((Q(1,2)-beta[0])/r)
kQ=simp((-Q(1,2)-beta[0])/r)
def left_solution(k):
    h=S.sqrt(2-k*k)
    return (simp((k-h)/2),simp((k+h)/2))
p=left_solution(kP);q=left_solution(kQ)
P=xy(p);Z=xy(q)

def pair_mean(z):
    x,y=z
    return S.Matrix([-2*I*r*y,-2*I*r*x,I*r*y])
mp=pair_mean(p);mq=pair_mean(q)
nP=norm2(mp);nQ=norm2(mq);cross=dot(mp,mq)
den=simp(nP+nQ-2*cross)
lam=simp((nQ-cross)/den)
h=S.simplify(lam*mp+(1-lam)*mq)
d2=simp((nP*nQ-cross**2)/den)
R2=simp(Q(625,324)-d2)

# Source-tracked exact BRC primitive: all ordered pairs, labels never merged.
def tagged_mass(paths):
    out=0
    for label_a,v in paths:
        for label_b,w in paths:out+=v*S.conjugate(w)
    return simp(out),len(paths)**2

def brc_state_measure(b,z):
    a=r*z*b
    obs={'Q0':[],'Q1':[],'Qi':[]}; count=0
    for row in A.tolist():
        paths=[(f'source:{j+1}',simp(row[j]*a[j]/8)) for j in range(3)]
        for key,ref in [('Q0',None),('Q1',1),('Qi',I)]:
            tagged=paths if ref is None else paths+[('reference',ref)]
            v,pairs=tagged_mass(tagged)
            obs[key].append(v);count+=pairs
    return obs,count

def main():
    assert kP==Q(7187,7825) and kQ==Q(-1943,1565)
    assert sg(p[0])<0 and sg(p[1])>0 and sg(q[0])<0 and sg(q[1])<0
    assert sg(den)>0 and sg(lam)>0 and sg(1-lam)>0
    assert sg(lam-Q(459,1000))>0 and sg(Q(460,1000)-lam)>0
    assert sg(R2-Q(1565258,1000000))>0 and sg(Q(1565260,1000000)-R2)>0
    old=Q(184807873005625,118075452616116)
    assert sg(R2-old)>0
    assert sg(Q(1062562,458329)-R2)>0
    assert all(sg(x)==0 for x in (norm2(mp)-nP,norm2(mq)-nQ,norm2(h)-d2))
    assert sg(dot(h,mp)-d2)==0 and sg(dot(h,mq)-d2)==0
    assert sg(norm2(r*P*b0)-Q(625,324))==0 and sg(norm2(r*Z*b0)-Q(625,324))==0
    # Equality on both mirrored endpoints, validating four support contacts.
    contacts=[r*P*b0,r*mirror(P)*b2,r*Z*b0,r*mirror(Z)*b2]
    for a in contacts:
        assert sg(dot(h,a)-d2)==0
        assert sg(norm2(a)-Q(625,324))==0
    assert all(sg(x)==0 for x in (h-(lam/2)*(contacts[0]+contacts[1])-(1-lam)/2*(contacts[2]+contacts[3])))

    # Immutable S7-3 source matrix must have its exact five-Port Gram identity.
    gram=S.simplify(A.conjugate().T*A/64)
    assert gram==S.diag(Q(31,32),1,Q(63,64))
    all_outputs={};total_BRC_pairs=0
    for name,b,begin,end,exp_endpoint_count,exp_arc_count in [
        ('b0',b0,p,q,4,2),('b2',b2,pt(mirror(Z)),pt(mirror(P)),6,3)]:
        count,endpoints,intervals=arcs(b)
        assert count==28 and len(endpoints)==exp_endpoint_count
        accepted=[x for x in intervals if x['feasible']]
        assert len(accepted)==exp_arc_count
        # The exactly determined feasible arcs all lie on the minor CCW circle
        # interval from begin to end. The chord at begin/end supports them.
        assert cmp(begin,end)<0
        assert all(cmp(begin,z)<=0 and cmp(z,end)<=0 for z in endpoints)
        assert all(cmp(begin,z)<=0 and cmp(z,end)<=0 for item in accepted
                   for z in (item['start'],item['end'],item['open_witness']))
        L=lambda z:dot(h,r*xy(z)*b)
        assert sg(L(begin)-d2)==0 and sg(L(end)-d2)==0
        assert sg(L((Q(-1),Q(0)) if name=='b0' else (Q(0),Q(1)))-d2)>0
        # Exact sign on endpoints + interval topology + the two chord
        # intersections imply L(z)>=d² everywhere on each entire closed arc.
        for item in accepted:
            for z in [item['start'],item['end'],item['open_witness']]:
                assert sg(L(z)-d2)>=0
        # Verify all 4 algebraic contact states via original labeled BRC mass.
        checks=[]
        for z in [P,Z] if name=='b0' else [mirror(P),mirror(Z)]:
            measures,n=brc_state_measure(b,z);total_BRC_pairs+=n
            assert all(sg(x-y)==0 for x,y in zip(measures['Q0'],Q0))
            for key,target in [('Q1',Q1),('Qi',Qi)]:
                assert all(sg(1-(x-y))>=0 and sg(1+(x-y))>=0
                           for x,y in zip(measures[key],target))
            checks.append('PASS')
        all_outputs[name]={'circle_boundary_intersections':count,
                           'feasible_endpoints':len(endpoints),
                           'closed_feasible_arcs':len(accepted),
                           'all_arcs_in_support_minor_circle_arc':True,
                           'chord_support_exact':True,
                           'algebraic_contact_BRC_checks':checks}
    result={
      'status':'PASS', 'classification':'AUTHOR_SIDE_EXACT_AUXILIARY_BRC_THEOREM_NOT_ADMITTED',
      'frozen_input':'S7-3; q=1; U=A/8; b0,b2; r=25/54; PREFIX-316 frozen 5 Q0 and 10 Q1/Qi',
      'global_knowledge_main_read_pin':'a796bc2faf7883195bf45b70fd6502ef5e22bfe4',
      'enterprise_math_current_main_read_pin':'f75dae1d65ef842089950d0a440c61cab20e42e2',
      'underlying_PREFIX317_science_pin':'dedcf9f123adbc065324ee57fb8676acafcf4f8a',
      'port1_imag_band_x_plus_y':{'p':str(kP),'q':str(kQ)},
      'p':list(map(str,p)),'q':list(map(str,q)),
      'contact_source_states':[[str(simp(v)) for v in a] for a in contacts],
      'center':[str(simp(z)) for z in h],
      'contact_weights':[str(simp(lam/2)),str(simp(lam/2)),str(simp((1-lam)/2)),str(simp((1-lam)/2))],
      'lambda':str(lam),
      'exact_distance_squared':str(d2),
      'exact_continuous_radius_squared':str(R2),
      'rigorous_interval_radius_squared':['1565258/1000000','1565260/1000000'],
      'previous_PREFIX317_eight_state_radius_squared':str(old),
      'strictly_exceeds_previous_finite_certificate':True,
      'still_below_full_auxiliary_two_state_bound':True,
      'source_sphere_squared':'625/324',
      'gaussian_rational_phase_supremum_equals_algebraic_continuous_optimum':True,
      'arcs':all_outputs,
      'exact_port_gram_entries_checked':9,
      'tagged_brc_masses_checked':60,
      'tagged_ordered_path_pairs':total_BRC_pairs,
      'no_native_X6_detector_physics_correspondence':True,
      'theorem_scope':'FIXED_REPORT_FIXED_SCALE_TWO_SOURCE_SHAPES_CONTINUOUS_PHASE_ARCS_ONLY'
    }
    dest=Path(__file__).with_name('RESULTS_PREFIX318.json')
    dest.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'PASS','R2_interval':result['rigorous_interval_radius_squared'],
          'arcs':{k:(v['feasible_endpoints'],v['closed_feasible_arcs']) for k,v in all_outputs.items()},
          'exact_port_gram_entries_checked':9,
          'tagged_brc_masses_checked':60,'tagged_ordered_path_pairs':total_BRC_pairs},ensure_ascii=False))
if __name__=='__main__':main()
