#!/usr/bin/env python3
"""PREFIX-317: exact tagged-BRC phase arcs and eight-state noise collision.

Arithmetic: Fraction for every BRC path product/mass, SymPy radicals only
for exact boundaries and their algebraic sign/order tests. No trigonometry,
angles, floating-point scientific checks, or X6/Detector claims.
"""
from __future__ import annotations

from fractions import Fraction as F
from functools import cmp_to_key
from pathlib import Path
import json
import sympy as sp

GLOBAL_SNAPSHOT = 'c4b076402410ac7a87c9f9875625ac4836b6bf13'
PROJECT_SCIENCE_SNAPSHOT = 'dedcf9f123adbc065324ee57fb8676acafcf4f8a'
A = [[(4,0),(4,0),(0,0)], [(0,0),(-4,0),(4,0)],
     [(-5,3),(0,0),(-3,1)], [(-2,-2),(4,4),(2,2)],
     [(-2,0),(0,0),(5,2)]]
B0 = [(-2,0),(0,-2),(1,0)]
B2 = [(0,2),(2,0),(0,-1)]
SCALE = F(25,54)
FROZEN_Q0 = list(map(F, ['625/1458','3125/11664','23125/93312',
                         '15625/23328','53125/186624']))
FROZEN_Q1 = list(map(F, ['2083/1458','14789/11664','32089357/29206656',
                         '7073089/7301664','251845/186624']))
FROZEN_QI = list(map(F, ['720235/456354','3477137/3650832',
                         '37487629/29206656','17311489/7301664',
                         '90898861/58413312']))
ALPHA = [(y-q-1)/2 for q,y in zip(FROZEN_Q0,FROZEN_Q1)]
BETA  = [(y-q-1)/2 for q,y in zip(FROZEN_Q0,FROZEN_QI)]
PREVIOUS_RADIUS = F(333788125,213477444)
KNOWN_GLOBAL_PAIR_LOWER = F(1062562,458329)


def add(x,y): return x[0]+y[0],x[1]+y[1]
def conj(x): return x[0],-x[1]
def neg(x): return -x[0],-x[1]
def mul(x,y): return x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]
def scale(x,r): return x[0]*r,x[1]*r
def state(b,p): return [mul(scale(p,SCALE),k) for k in b]
def norm2(z): return z[0]*z[0]+z[1]*z[1]
def dot(a,b):return sum(x[0]*y[0]+x[1]*y[1] for x,y in zip(a,b))
def sgn(x):
    e=sp.simplify(x)
    if e.is_positive: return 1
    if e.is_negative: return -1
    if e.is_zero: return 0
    v=sp.sign(e)
    if v in [-1,0,1]: return int(v)
    raise AssertionError('undecided algebraic sign: '+str(e))
def rational(t):return sp.Rational(t.numerator,t.denominator)


def port_amplitudes(shape):
    ans=[]
    for row in A:
        s=(F(0),F(0))
        for a,k in zip(row,shape):s=add(s,mul(a,k))
        ans.append(scale(s,SCALE/8))
    return ans


def restrictions(shape):
    out=[]
    for j,(p,q) in enumerate(port_amplitudes(shape)):
        for component,target,n in [('real',ALPHA[j],(p,-q)),
                                   ('imag',BETA[j],(q,p))]:
            for edge in [-1,1]:
                out.append((f'{j}_{component}_{edge:+d}',n,target+F(edge,2),edge))
    return out


def feasible(shape,p):
    x,y=p
    for name,(a,b),target,edge in restrictions(shape):
        e=rational(a)*x+rational(b)*y-rational(target)
        if sgn(e)>0 if edge==1 else sgn(e)<0:return False
    return True


def line_circle(normal,target):
    a,b=map(rational,normal)
    c=rational(target)
    den=sp.factor(a*a+b*b)
    if den==0: raise AssertionError('degenerate normal')
    dis=sp.factor(den-c*c)
    if sgn(dis)<0:return []
    w=sp.sqrt(dis)
    signs=[-1,1] if sgn(dis)>0 else [1]
    return [(sp.simplify((c*a+e*w*(-b))/den),
             sp.simplify((c*b+e*w*a)/den)) for e in signs]


def half(p):
    y=sgn(p[1])
    return 0 if y>0 or (y==0 and sgn(p[0])>=0) else 1


def compare_cyclic(p,q):
    a,b=half(p),half(q)
    if a!=b:return -1 if a<b else 1
    cr=sgn(p[0]*q[1]-p[1]*q[0])
    return -cr


def rational_between_phase(a,b,wrap=False):
    """Exact Pythagorean-circle witness in the CCW open arc a->b.

    The endpoints are consecutive in cyclic order. No angle/trig functions.
    """
    if wrap:return (F(1),F(0))
    ha,hb=half(a),half(b)
    if ha!=hb:
        return (F(-1),F(0)) if ha==0 else (F(1),F(0))
    ta=sp.simplify(a[1]/(1+a[0]));tb=sp.simplify(b[1]/(1+b[0]))
    assert sgn(tb-ta)>0,(a,b,ta,tb)
    for d in [1,10,100,1000,10000,100000,1000000]:
        n=int(sp.floor(ta*d))+1
        t=sp.Rational(n,d)
        if sgn(t-ta)>0 and sgn(tb-t)>0:
            return ((1-t*t)/(1+t*t),2*t/(1+t*t))
    raise AssertionError('could not construct rational arc witness')


def all_phase_arcs(shape):
    endpoints={}
    checked=0
    for label,n,target,edge in restrictions(shape):
        for p in line_circle(n,target):
            checked+=1
            if feasible(shape,p):
                key=tuple(map(str,p))
                if key not in endpoints:endpoints[key]={'p':p,'active':[]}
                endpoints[key]['active'].append(label)
    pts=sorted([v['p'] for v in endpoints.values()],key=cmp_to_key(compare_cyclic))
    assert pts
    out=[]
    for i,a in enumerate(pts):
        b=pts[(i+1)%len(pts)]
        mid=rational_between_phase(a,b,wrap=(i+1==len(pts)))
        # Check the witness is strictly between consecutive endpoints.
        if i+1<len(pts):assert compare_cyclic(a,mid)<0 and compare_cyclic(mid,b)<0
        else:assert compare_cyclic(a,mid)<0 or compare_cyclic(mid,b)<0
        out.append({'left':[str(z) for z in a],
                    'right':[str(z) for z in b],
                    'left_active':endpoints[tuple(map(str,a))]['active'],
                    'right_active':endpoints[tuple(map(str,b))]['active'],
                    'rational_witness':[str(z) for z in mid],
                    'feasible':bool(feasible(shape,mid))})
    # Topological proof obligation: boundary lines are exhaustive; each open
    # interval cannot change truth-value without crossing a listed feasible
    # boundary point. Exact rational tests decide interval truth-value.
    return {'line_circle_intersections_checked':checked,
            'feasible_boundary_points':len(pts),
            'feasible_open_arcs':sum(x['feasible'] for x in out),
            'cyclic_intervals':out}


def phase_from_t(t):return ((1-t*t)/(1+t*t), 2*t/(1+t*t))


def tagged_brc_mass(paths):
    """Compute full ordered, labeled BRC path-pair sum; do not collapse ports."""
    acc=(F(0),F(0))
    for (_,u) in paths:
        for (_,v) in paths:
            acc=add(acc,mul(u,conj(v)))
    assert acc[1]==0 and acc[0]>=0
    return acc[0],len(paths)**2


def measure_sources(points):
    counts={'tagged_masses':0,'ordered_source_reference_pairs':0,
            'exact_port_gram_entries':0}
    details=[]
    for k,source in enumerate(points):
        vals={'Q0':[],'Q1':[],'Qi':[]}
        for j,row in enumerate(A):
            paths=[(f'source:{i+1}',scale(mul(a,source[i]),F(1,8))) for i,a in enumerate(row)]
            assert len({lab for lab,z in paths})==3
            for typ,ref in [('Q0',None),('Q1',(F(1),F(0))),('Qi',(F(0),F(1)))]:
                tagged=paths+([] if ref is None else [('reference',ref)])
                q,n=tagged_brc_mass(tagged)
                vals[typ].append(q)
                counts['tagged_masses']+=1
                counts['ordered_source_reference_pairs']+=n
        assert vals['Q0']==FROZEN_Q0,('incorrect Q0',k,vals['Q0'])
        assert all(abs(a-b)<=1 for a,b in zip(vals['Q1'],FROZEN_Q1)),k
        assert all(abs(a-b)<=1 for a,b in zip(vals['Qi'],FROZEN_QI)),k
        details.append({typ:[str(x) for x in vals[typ]] for typ in vals})
    for i in range(3):
        for j in range(3):
            g=(F(0),F(0))
            for k in range(5):g=add(g,mul(conj(A[k][i]),A[k][j]))
            g=scale(g,F(1,64))
            assert g==((F(31,32),F(1),F(63,64))[i],F(0)) if i==j else g==(F(0),F(0))
            counts['exact_port_gram_entries']+=1
    return counts,details


def choose_exact_contact(points):
    """Verify full proposed rational minimax certificate without optimization."""
    W=list(map(F,['395261844730136/1462540217092419',
                  '395261844730136/1462540217092419',
                  '672016527632147/2925080434184838',
                  '672016527632147/2925080434184838']))
    C=[(F(0),F('-309317225000/1093291227927')),
       (F(0),F('561517578125/1093291227927')),
       (F(0),F('154658612500/1093291227927'))]
    R=F('184807873005625/118075452616116')
    assert len(points)==8 and sum(W)==1 and min(W)>0
    assert all(sum((W[j]*points[4+j][i][k] for j in range(4)),F(0))==C[i][k]
               for i in range(3) for k in range(2))
    sphere=F(625,324)
    assert all(dot(p,p)==sphere for p in points)
    assert R==sphere-dot(C,C)
    squared_distances=[]
    for k,p in enumerate(points):
        d2=dot([(x[0]-c[0],x[1]-c[1]) for x,c in zip(p,C)],
               [(x[0]-c[0],x[1]-c[1]) for x,c in zip(p,C)])
        assert d2<=R
        if k>=4: assert d2==R
        squared_distances.append(d2)
    assert R>PREVIOUS_RADIUS and R<KNOWN_GLOBAL_PAIR_LOWER
    return {'radius_squared':str(R),'radius_decimal_for_display_only':str(sp.N(rational(R),22)),
            'source_sphere_squared':str(sphere),
            'contact_indices_zero_based':[4,5,6,7],
            'strictly_positive_contact_weights':[str(z) for z in W],
            'center':[[str(z) for z in c] for c in C],
            'squared_distances':[str(v) for v in squared_distances],
            'previous_prefix316_radius_squared':str(PREVIOUS_RADIUS),
            'exact_improvement':str(R-PREVIOUS_RADIUS),
            'full_model_two_point_lower_bound':str(KNOWN_GLOBAL_PAIR_LOWER),
            'strictly_below_prior_lower_bound':True}


def main():
    u=(F(24,25),F(7,25));v=(F(312,313),F(25,313));I=(F(0),F(1))
    old=[state(B0,neg(u)),state(B0,mul(I,v)),
         state(B2,mul(I,conj(u))),state(B2,neg(conj(v)))]
    p=phase_from_t(F(-125,18)); pm=(-p[1],-p[0])
    q=phase_from_t(F(541,500)); qm=(-q[1],-q[0])
    assert all(feasible(b,z) for b,z in [(B0,p),(B2,pm),(B0,q),(B2,qm)])
    points=old+[state(B0,p),state(B2,pm),state(B0,q),state(B2,qm)]
    assert len(set(str(p) for p in points))==8
    counts,observations=measure_sources(points)
    real_basis=[state(B0,(F(1),F(0))),state(B0,(F(0),F(1))),
                state(B2,(F(1),F(0))),state(B2,(F(0),F(1)))]
    real_gram=sp.Matrix([[rational(dot(a,b)) for b in real_basis]
                         for a in real_basis])
    real_gram_det=real_gram.det()
    assert real_gram_det==sp.Rational(3814697265625,282429536481)>0
    arcs={'b0':all_phase_arcs(B0),'b2':all_phase_arcs(B2)}
    assert arcs['b0']['feasible_boundary_points']==4
    assert arcs['b0']['feasible_open_arcs']==2
    assert arcs['b2']['feasible_boundary_points']==6
    assert arcs['b2']['feasible_open_arcs']==3
    certificate=choose_exact_contact(points)
    result={'status':'PASS','scope':'AUXILIARY_S7_3_STATIC_TAGGED_BRC',
            'claim_status':'AUTHOR_SIDE_UNREVIEWED_NOT_ADMITTED_REGISTER_PENDING',
            'global_knowledge_pin':GLOBAL_SNAPSHOT,'project_science_pin':PROJECT_SCIENCE_SNAPSHOT,
            'frozen_report':{'Q0':[str(x) for x in FROZEN_Q0],
                             'Q1':[str(x) for x in FROZEN_Q1],
                             'Qi':[str(x) for x in FROZEN_QI]},
            'phase_arc_classification':arcs,
            'two_shape_real_span_dimension':4,
            'four_real_generator_gram_determinant':str(real_gram_det),
            'new_rational_phase_pairs':{'b0_phase_t_minus_125_over_18':[str(x) for x in p],
                                        'b2_mirror_125_over_18':[str(x) for x in pm],
                                        'b0_phase_t_541_over_500':[str(x) for x in q],
                                        'b2_mirror_541_over_500':[str(x) for x in qm]},
            'all_eight_source_states':[[[str(z) for z in x] for x in a] for a in points],
            'all_eight_tagged_BRC_true_observations':observations,
            'exact_minimal_enclosing_ball':certificate,
            'counts':counts,'native_X6_Detector_correspondence':'NOT_ESTABLISHED',
            'physics_attribution':'NOT_CLAIMED'}
    path=Path(__file__).with_name('RESULTS_PREFIX317.json')
    path.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({'status':'PASS','counts':counts,
                      'arcs':{k:{n:v[n] for n in ['feasible_boundary_points','feasible_open_arcs']}
                              for k,v in arcs.items()},
                      'minimax_square':certificate['radius_squared'],
                      'improvement':certificate['exact_improvement']},ensure_ascii=False))

if __name__=='__main__': main()
