#!/usr/bin/env python3
"""EC49AE exact rational certificate: one causal prefix dominates ALL for eta in [0,1/100].

Only Python 3 standard library Fraction is used.  No floating-point optimizers,
probability-grid sampling or symbolic black boxes are needed.
"""
from fractions import Fraction as F
from itertools import product
from functools import reduce
from math import gcd, lcm
import json

ZERO, ONE, ETA_MAX = F(0), F(1), F(1,100)
STATES = range(3)
ACTIONS = range(4)  # A0 A1 B0 B1
ATOM_KEYS = list(product(ACTIONS, range(2), STATES))
SAMPLES = (F(1,1000), F(9,2500), F(1,200), F(3,500),
           F(9,1250), F(3,400), F(9,1000))
CROSSING_POLYS = (
    (1,-286,64),
    (1,-268,100),
    (1,-176,-36),
    (1,-140,36),
    (13,-1798,448),
    (13,-1708,628),
)

def l_add(a,b): return (a[0]+b[0],a[1]+b[1])
def l_scale(a,k): return (a[0]*k,a[1]*k)
def l_mul(a,b): return (a[0]*b[0],a[0]*b[1]+a[1]*b[0],a[1]*b[1])
def p_add(a,b): return tuple(x+y for x,y in zip(a,b))
def p_sub(a,b): return tuple(x-y for x,y in zip(a,b))
def p_scale(a,s): return tuple(x*s for x in a)
def p_eval(a,t): return a[0]+a[1]*t+a[2]*t*t

def p_min_nonnegative(p,lo=ZERO,hi=ETA_MAX):
    """Certificate for exact non-negativity of quadratic on a rational interval."""
    values=[p_eval(p,lo),p_eval(p,hi)]
    if p[2]>0:
        stationary=-p[1]/(2*p[2])
        if lo<stationary<hi: values.append(p_eval(p,stationary))
    return min(values)>=0

def normalize_poly(p):
    den=1
    for t in p: den=lcm(den,t.denominator)
    nums=[int(t*den) for t in p]
    common=reduce(gcd,nums,0)
    if common: nums=[n//common for n in nums]
    if next((n for n in nums if n),0)<0: nums=[-n for n in nums]
    return tuple(nums)

def root_open_interval(p,hi=ETA_MAX):
    """Exact root existence for polynomial of degree <=2, open (0,hi)."""
    a,b,c=p
    if c==0:
        return b!=0 and ZERO < -a/b < hi
    if a==0:
        return b!=0 and ZERO < -b/c < hi
    fhi=p_eval(p,hi)
    if fhi==0:
        # One root exactly hi; a/c=hi*other.
        return ZERO < a/(c*hi) < hi
    if a*fhi<0: return True
    vertex=-b/(2*c)
    return ZERO<vertex<hi and a*p_eval(p,vertex)<=0

def tlin(w,u): return (F(1,2),F((2*u-1)*(1-w)))
def masses_linear(x):
    """Output linear-in-eta measures for all always-S observation states and STOP."""
    observed=[]
    for c,u,z in ATOM_KEYS:
        p=q=(ZERO,ZERO)
        for w in STATES:
            weighted=l_scale(tlin(w,u),x[w][c])
            p=l_add(p,l_scale(weighted,F(1,6) if w==z else F(1,12)))
            q=l_add(q,l_scale(weighted,F(1,9)))
        observed.append((p,q))
    stop=ONE-sum((sum(row) for row in x),ZERO)/3
    return observed,stop

def vertex(stop_history,b_history,a_tags,b_tag,b):
    x=[[ZERO]*4 for _ in STATES]
    stop_total=F(5,16)+b
    for w in STATES:
        sw=stop_total if w==stop_history else ZERO
        bw=b if w==b_history else ZERO
        assert sw+bw<=1
        x[w][a_tags[w]]+=ONE-sw-bw
        x[w][b_tag]+=bw
    return x

UNIVERSAL_PREFIX=[
    [ONE,ZERO,ZERO,ZERO],
    [ZERO,ONE,ZERO,ZERO],
    [F(9,16),ZERO,F(1,16),ZERO],
]
OBS_X,STOP_X=masses_linear(UNIVERSAL_PREFIX)
VERTICES=[masses_linear(vertex(i,j,tags,bt,b))
          for b in (ZERO,F(1,16)) for i,j,tags,bt in product(
              STATES,STATES,product((0,1),repeat=3),(2,3))]
ACTIVE_BREAKS=[j for j,(_,q) in enumerate(OBS_X) if q!=(ZERO,ZERO)]
# r=1 is a separate supporting-ratio kink contributed by the STOP atom.
# r=3/4 and r=3/2 need no enumeration: every raw leaf has P/Q in [3/4,3/2].
BREAKS=ACTIVE_BREAKS+['STOP_RATIO_1']
def reference(j):
    return ((ONE,ZERO),(ONE,ZERO)) if j=='STOP_RATIO_1' else OBS_X[j]

def cross(p,q,pj,qj):
    """q_j (p - (p_j/q_j) q): quadratic in eta."""
    return p_sub(l_mul(p,qj),l_mul(q,pj))

def support_gap_polynomial(j,obs,stop,sample):
    pj,qj=reference(j)
    no_sense=(qj[0]-pj[0],qj[1]-pj[1],ZERO)
    hx=hv=(ZERO,ZERO,ZERO)
    for p,q in OBS_X:
        poly=cross(p,q,pj,qj)
        if p_eval(poly,sample)>0: hx=p_add(hx,poly)
    if p_eval(no_sense,sample)>0:
        hx=p_add(hx,p_scale(no_sense,STOP_X))
    for p,q in obs:
        poly=cross(p,q,pj,qj)
        if p_eval(poly,sample)>0: hv=p_add(hv,poly)
    if p_eval(no_sense,sample)>0:
        hv=p_add(hv,p_scale(no_sense,stop))
    return p_sub(hx,hv)

def source_weight(w,u,z,src,eta):
    t=F(1,2)+F((2*u-1)*(1-w))*eta
    return t*(F(1,6) if w==z else F(1,12)) if src=='P' else t/F(9)

def fixed_prefix_costs():
    T=sum((sum(row) for row in UNIVERSAL_PREFIX),ZERO)
    b=sum((row[2]+row[3] for row in UNIVERSAL_PREFIX),ZERO)
    return ((T+b)/3,T/3)

def chosen_spectrum(eta):
    p=[];q=[]
    for pl,ql in OBS_X:
        p.append(pl[0]+pl[1]*eta)
        q.append(ql[0]+ql[1]*eta)
    return p,q

def low_at(eta,d):
    p,q=chosen_spectrum(eta)
    positive=sorted((p0/(p0-q0),p0,p0-q0) for p0,q0 in zip(p,q) if p0>q0)
    remaining=d; alpha=ZERO
    for ratio,p0,di in positive:
        r=min(ONE,remaining/di)
        alpha+=r*p0
        remaining-=r*di
        if remaining==0: break
    assert remaining==0
    return alpha

def run():
    assert len(VERTICES)==288 and len(ACTIVE_BREAKS)==18
    assert fixed_prefix_costs()==(F(43,48),F(7,8))
    # Source leaves remain strictly positive and normalized for the WHOLE interval:
    # each source weight is affine in eta, so the two exact endpoints suffice.
    for eta in (ZERO,ETA_MAX):
        for src in ('P','Q'):
            leaf=[source_weight(w,u,z,src,eta)
                  for w,u,z in product(STATES,range(2),STATES)]
            assert len(leaf)==18 and min(leaf)>0 and sum(leaf,ZERO)==ONE
    # All q_j stay strictly positive throughout the interval, by affine endpoint test.
    for j in ACTIVE_BREAKS:
        q=OBS_X[j][1]
        assert q[0]>0 and q[0]+q[1]*ETA_MAX>0
    # The ONLY possible inner crossings of support positive-part terms occur
    # at the six listed algebraic numbers (all roots of rational quadratics).
    relevant=set()
    for j in BREAKS:
        pj,qj=reference(j)
        for obs,_ in VERTICES:
            for p,q in obs:
                poly=cross(p,q,pj,qj)
                if poly!=(ZERO,ZERO,ZERO): relevant.add(poly)
        for p,q in OBS_X:
            poly=cross(p,q,pj,qj)
            if poly!=(ZERO,ZERO,ZERO): relevant.add(poly)
        # STOP term has sign of qj-pj (linear eta).
        stop_poly=(qj[0]-pj[0],qj[1]-pj[1],ZERO)
        if stop_poly!=(ZERO,ZERO,ZERO): relevant.add(stop_poly)
    observed_crossings=sorted({normalize_poly(poly) for poly in relevant
                               if root_open_interval(poly)})
    assert observed_crossings==sorted(CROSSING_POLYS),observed_crossings
    # Exact distinct-root ordering certified by sign changes in consecutive
    # rational sample points. Quadratics have one root in (0,1/100) each.
    for i,coeff in enumerate(CROSSING_POLYS):
        f=tuple(F(x) for x in coeff)
        assert p_eval(f,SAMPLES[i])*p_eval(f,SAMPLES[i+1])<0
    # On each of the seven open intervals, all support atom sign patterns
    # are fixed. Compare support of every admissible 288 endpoint at each
    # possible breakpoint of h_X. Their gaps are quadratic in eta there.
    # We certify each such quadratic is nonnegative on the LARGER [0,1/100],
    # so certainly on its actual segment; by continuity also at six roots.
    checked=0;zero_polynomials=0
    for s in SAMPLES:
        for j in BREAKS:
            for obs,stop in VERTICES:
                gap=support_gap_polynomial(j,obs,stop,s)
                assert p_min_nonnegative(gap), (s,j,gap)
                checked+=1
                if gap==(ZERO,ZERO,ZERO):zero_polynomials+=1
    assert checked==7*19*288
    # Piecewise signs of p-q for the universal prefix never change over the
    # entire eta interval.  The total positive mass is EXACTLY the constant
    # polynomial 59/576, and every negative atom has pointwise P=3(Q-P).
    positive_linear=(ZERO,ZERO)
    negative_linear=(ZERO,ZERO)
    positive_count=negative_count=0
    for p,q in OBS_X:
        d=(p[0]-q[0],p[1]-q[1])
        dl,dr=d[0],d[0]+d[1]*ETA_MAX
        assert dl*dr>=0
        if dl>0 or dr>0:
            positive_linear=l_add(positive_linear,d);positive_count+=1
        elif dl<0 or dr<0:
            negative_linear=l_add(negative_linear,d);negative_count+=1
            assert p[0]+3*d[0]==0 and p[1]+3*d[1]==0
    assert (positive_count,negative_count)==(8,10)
    assert positive_linear==(F(59,576),ZERO)
    assert negative_linear==(-F(59,576),ZERO)
    capacities={}
    fibers={}
    for eta in (ZERO,F(1,200),ETA_MAX):
        p,q=chosen_spectrum(eta)
        D=sum((pp-qq for pp,qq in zip(p,q) if pp>qq),ZERO)
        assert D==F(59,576)
        capacities[str(eta)]=str(D)
        fibers[str(eta)]={
            'delta':'1/12',
            'alpha_min':str(low_at(eta,F(1,12))),
            'alpha_max':str(ONE-3*F(1,12)),
        }
    assert fibers['1/100']['alpha_min']=='5411/17744'
    assert fibers['1/200']['alpha_min']=='1229/4016'
    return {
      'schema':'EC49AE_ETA_INTERVAL_PREFIX_DOMINANCE_V1',
      'eta_interval':['0','1/100'],
      'model_leaves_each_source':18,
      'costs':['43/48','7/8'],
      'universal_prefix':['w0=A0','w1=A1','w2=(9/16)A0+(1/16)B0+(3/8)STOP','always S after payment'],
      'endpoint_prefixes':288,
      'active_ratio_breakpoints':len(ACTIVE_BREAKS),
      'stop_ratio_breakpoint':'1',
      'distinct_nonzero_cross_polynomials':len(relevant),
      'interior_root_polynomials':[list(t) for t in CROSSING_POLYS],
      'ordered_rational_interval_samples':[str(t) for t in SAMPLES],
      'exact_quadratic_nonnegativity_checks':checked,
      'identically_zero_gap_polynomials':zero_polynomials,
      'discrimination_capacity':capacities,
      'fiber_delta_1_over_12':fibers,
      'status':'AUTHOR_PROVED / EXACT_FRACTION_CHECK_PASS / UNREVIEWED / NOT_ADMITTED',
      'scope':'All real fresh-coin causal strategies, fixed costs, eta in [0,1/100]; finite exact certificate + analytic convexity and support function argument'
    }

if __name__=='__main__':print(json.dumps(run(),ensure_ascii=False,indent=2))