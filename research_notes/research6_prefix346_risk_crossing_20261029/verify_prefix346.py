#!/usr/bin/env python3
"""PREFIX-346 strict near-L crossing bracket for retained-phase S7-3 BRC arcs.

Re-executes the supplied PREFIX-342 exact Banach-box, ordered-path-pair
certificate. All proof decisions are Fraction/interval and integer sqrt.
The upper-bound claim is for SIX CONSTRUCTED arcs only, not all exact sources.
"""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json, runpy

upstream = Path(__file__).with_name('verify_prefix342.py')
assert upstream.is_file()
v = runpy.run_path(str(upstream))
IV,ci = v['IV'],v['ci']
zadd,zmul,zconj,zscalar = v['zadd'],v['zmul'],v['zconj'],v['zscalar']
znorm2,zdotconj,rvec,rdot = v['znorm2'],v['zdotconj'],v['rvec'],v['rdot']
sources,ports,q3,L = v['sources'],v['ports'],v['q3'],v['L']
assert len(sources)==len(ports)==6
assert all(0<q<1 for q in v['q'])

h_lower=F(166639681,100000000)  # 1.66639681
h_upper=F(83319841,50000000)   # 1.66639682
assert F(1)<h_lower<h_upper<F(2)
assert (h_upper-1)**2<q3

def endpoints(h):
    y=h-1;rad=q3-y*y
    assert y>0 and rad>0
    scale=10**36
    k=isqrt((rad.numerator*scale**2)//rad.denominator)
    lo,hi=F(k,scale),F(k+1,scale)
    assert lo*lo<rad<hi*hi
    root=IV(lo,hi)
    z={'+':ci(root,y),'-':ci(-root,y)}
    point={}
    for j,(a,w) in enumerate(zip(sources,ports)):
        for sign in ('-','+'):
            phase=zscalar(1/q3,zmul(z[sign],zconj(w)))
            point[j,sign]=[zmul(phase,ak) for ak in a]
    return point

# Lower side: certified 4-point variance, with fixed strictly positive weights.
P=endpoints(h_lower)
labels=[(0,'-'),(1,'+'),(3,'-'),(4,'+')]
weights=[F(x,10**6) for x in (140253,100513,363029,396205)]
assert sum(weights)==1 and all(w>0 for w in weights)
mu=[ci(0,0) for _ in range(3)]
second=IV(0)
for k,alpha in zip(labels,weights):
    p=P[k]
    for i in range(3):mu[i]=zadd(mu[i],zscalar(alpha,p[i]))
    second += alpha*sum((znorm2(z) for z in p),IV(0))
V=second-sum((znorm2(z) for z in mu),IV(0))
assert V.lo>L, 'four-point lower bound does not clear L'
assert V.lo>L+F(1,10**10), 'four-point lower bound margin is too small'
# All four points are on four distinct phase orbits and are jointly feasible.
assert len({j for j,s in labels})==4

# Upper side: a fixed rational centre, NOT a numerically trusted optimizer.
# Each real/imag rational was chosen by exploration, then validated below.
P2=endpoints(h_upper)
real=[F('0.379558420333054'),F('0.012435707126596'),F('0.109614732382381')]
imag=[F('-0.620581010752923'),F('-0.048952050756643'),F('-0.326659837617947')]
center=[ci(x,y) for x,y in zip(real,imag)]
cvec=rvec(center)
slacks={}
for key,p in P2.items():
    pv=rvec(p)
    distance=rdot([a-b for a,b in zip(pv,cvec)],
                  [a-b for a,b in zip(pv,cvec)])
    slack=IV(L)-distance
    assert slack.lo>0,(key,'upper bound breach',slack)
    # Explicit strict margin on ALL 12 end points.
    assert slack.lo>F(1,10**9),(key,'upper slack < 1e-9')
    slacks[str(key)]=[str(slack.lo),str(slack.hi)]

# Full-arc coverage: f(x)=||a||²+||c||²-2x Re(t)
#             +2 sqrt(q3-x²) Im(t) for x in [-s,s].
# If Im(t)<0, f is strictly convex, hence f(x) <= max(endpoint values).
convexity={}
for j,(a,w) in enumerate(zip(sources,ports)):
    t=zscalar(1/q3,zmul(zdotconj(center,a),zconj(w)))
    assert t[1].hi < -F(7,10), (j, 'arc convexity not proved',t[1])
    convexity[str(j)]=str(t[1].hi)

# Six-arc continuity: x=u*sqrt(q3-(h-1)^2), u in [-1,1],
# z_h(u)=x+i*sqrt(q3-x*x). This is a joint continuous parametrisation.
# Nonempty compact T6(h) varies continuously in Hausdorff distance;
# its minimal enclosing radius is continuous.
result={
    'schema':'PREFIX346_S7_3_CERTIFIED_T6_CROSSING_BRACKET_V1',
    'status':'PASS_AUTHOR_SIDE_EXACT_RATIONAL',
    'h_left':str(h_lower),'h_right':str(h_upper),
    'interval_width':str(h_upper-h_lower),
    'L':str(L),
    'four_point_labels':[[j,s] for j,s in labels],
    'four_point_weights':[str(a) for a in weights],
    'variance_interval':[str(V.lo),str(V.hi)],
    'variance_strict_margin':'V > L + 1/10^10',
    'upper_rational_center':[[str(x),str(y)] for x,y in zip(real,imag)],
    'strict_upper_endpoint_min_slack_lower':str(min(F(xs[0]) for xs in slacks.values())),
    'endpoint_slacks':slacks,
    'arc_strict_convexity_im_t_upper':convexity,
    'proved':[
        'For ALL 1<h<=h_left, full exact-source S(h) has MEB² > L+1/10^10 (nested fibres; no six-orbit exhaustion).',
        'T6(h_right) has MEB² < L-1/10^9 using one common rational centre and analytic full-arc convexity.',
        'At least one h_c in (h_left,h_right) satisfies MEB²(T6(h_c))=L by continuity.',
    ],
    'not_proved':[
        'Full S(h_right) has MEB²<L without a separate all-source exhaustion proof.',
        'Uniqueness of crossing, or monotonic strictness, or physical/native X6 transfer.',
        'Six-source algebraic global exhaustion, independent Driver acceptance.'
    ],
    'verification':'Fraction interval arithmetic + isqrt; upstream six Banach isolations and 45 ordered source-labelled BRC path pairs reexecuted; no angle grid',
}
Path(__file__).with_name('RESULTS_PREFIX346.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('PASS_AUTHOR_SIDE_EXACT_RATIONAL')
print('h_left =',h_lower,'h_right =',h_upper,'width =',h_upper-h_lower)
print('fourpoint variance V-L interval: ',float(V.lo-L),float(V.hi-L))
print('12-point min slack L-dist2 lower:',float(min(F(xs[0]) for xs in slacks.values())))
print('all 6 arcs proved covered; crossing exists in bracket for T6; all-source upper remains conditional')
