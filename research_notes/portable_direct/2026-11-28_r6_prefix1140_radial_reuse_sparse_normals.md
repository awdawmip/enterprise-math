# PREFIX-1140 — Reusing archived radial moments through sparse annihilators

2026-11-28. R6 informed direct research; AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_AUXILIARY_COMPUTATION / CONDITIONAL_STAGE46_APPLICATION / NOT_REVIEWED. Frozen science P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d. Continue PREFIX-1139 at 3b6c5042be6e4c7ee3013c48f48959f715221d8b:research_notes/portable_direct/2026-11-28_r6_prefix1139_scale_localization.md. Use the certified point-conditioned affine transfer of PREFIX-1138 at 60d471d5de2cf566c263b759725f61eb59b5c816 and archived moment rows of PREFIX-1136 at 5398060227764faceb139720385c09dc87578bb1. Inherit Stage46 and the compact anchor exit obligation; no new native BRC operation, moment generation or anchor inversion. All observer coordinates are auxiliary algebraic quantities, not new native space axes. Global entries checked at immutable 4279409d2bdea648c044338c4d5b5adce428ef3a. Own previous registration status SUCCEEDED and nonrevoked owner-account custody metadata verified; current owner inventory r6-20261128-0252-owner-read RUNNING at observation, no live-owner conclusion or formal claim. Independent direct calculation, no task/Result mutation.

## 1. Sparse annihilator transport
Let the old point-conditioned seven-observer outer model be m+C[-1,1]^12+[-e,e] on integer grid G=10^125, with affine output L(rho,c)=(-aj*(rho-r), am*(c-u)-dj*(rho-r),0,...,0). Append the three previously unused certified radial moment rows k=11200,11600,12000 from extra_rows_1136.json. Use their original shared columns and complete error payments, giving ten observations ordered F,G,radial10000,radial10400,radial10800,coupled11200 channel1,channel2,radial11200,radial11600,radial12000. The first two errors include the one-grid-unit transfer payments verified in 1138; the new moments are independent of (rho,c), so no extra affine approximation is needed. The original compact coefficient vector is the same across all ten rows.

For any seven-coordinate subset I, form the 6-by-7 integer matrix of the restrictions of the first six shared columns. The signed maximal minors define an integer vector n_I (divide by its gcd if nonzero), and extend it with zeros off I. Laplace expansion of a determinant with a repeated row proves n_I annihilates all six chosen shared columns. All remaining shared columns and every error coordinate are paid. Set z=n dot m, S=sum_j |n dot C_j|+sum_i |n_i| e_i, a=-G(n_0 aj+n_1 dj), b=G n_1 am. Then every true parameter satisfies |a(rho-r)+b(c-u)-z|<=S. This follows directly from the support inequality of the common-coefficient outer model; using any subset of directions gives a valid outer bound, irrespective of whether they exhaust ten-dimensional facets.

By the inherited necessary conditions for a pair with q>=q0=544447235321021556325566186117974922693, let E=400000, K=d_hi+2E/q0, H=2K. Then (p/q,h/q)=(rho,c)+(-delta,eta), 0<=delta<=K/L^2, 0<=eta<=H/L. Thus writing x=p/q-r,y=h/q-u, the two necessary inequalities are
a*x+b*y-z <= S+max(0,-a)*K/L^2+max(0,b)*H/L,
z-a*x-b*y <= S+max(0,a)*K/L^2+max(0,-b)*H/L.
The support payments are signed, not an independent absolute-value bound on the two original parameter errors. Strict violation at L0=10^114 excludes the candidate for all L>=L0 by monotonicity.

## 2. Exact results
Verified all 127 original file hashes in PREFIX-1139-execution-evidence.zip. Reconstructed the targeted 43-direction section using the archived source inputs. Scanned 109 nonzero seven-coordinate annihilators involving F or G and at least one appended radial coordinate. Nine directions cut the current polygon; final outer polygon has six vertices. rho width 7.168522152245284e-102, c width 3.4399064697154946e-101 (old 4.101624829506882e-101 and 1.9683738383647722e-100). All sixteen persistent primitive lines from 1139 excluded for all L>=10^114. Four directions suffice; zero-based coordinate indices and newly eliminated indices (in sorted original 1139 line order):
I=(0,1,2,3,4,5,8): 1,4;
I=(0,1,2,3,4,5,9): 0,3,7,12;
I=(0,1,2,3,5,6,7): 2,6,10,11,14,15;
I=(0,1,2,3,5,6,8): 5,8,9,13.
Independent exact support checker used saved normals and no determinant solver or polygon clipping; confirmed annihilation, sign-specific payments and all sixteen exclusions. Minimum achieved ratio of violated left side to paid right side is 1.0700596966969693 (strict rational >1 checked). All 16 lines already exhaust the old necessary region at Q=10^69, L0=10^114, by 1139 exhaustive enumeration. Consequently b-a>=q>10^69 for every genuine pair under inherited premises at L>=10^114. No assertion that the new bound is optimal.

Retaining earlier covered dyadic windows and the inherited three-anomaly curvature q^2<4EL/d and close-pair q<=sqrt(L), first unexcluded dyadic starts on 10^8*2^j using this strict q bound:
L3=8461516400515182066584515942819469309803579941942799606843504579512394127824785226562421893628355646049167513920298986294476800000000 (~8.461516400515182e132);
L2=1109067877648325943831365673657233481374574830150326630068191832245848523122250249215989762441655831238956484384561428731589663129600000000 (~1.109067877648326e138).
Both 4 times 1139. Continuous integer endpoint unchanged 4.72478e43. True fixed spectrum unbounded separation and B_fix,odd(32) remain open.

## 3. Compact reproducible proof kernel
The inputs are the unmodified prior archive PREFIX-1139-execution-evidence.zip (manifest PREFIX1139_SHA256SUMS), specifically point_section_targeted1138.py, verify_section.py, compact1135.json, point1138.json, extra_coupled_1136.json, extra_rows_1136.json, check_extra_core.py, extend1139.json. These are pinned by the 1139 paper and archive. The following deterministic kernel regenerates the four directions and checks their complete signed support inequalities with Fraction; the full execution archive additionally contains actual scan1140.py, verify1140.py, scan1140.json and logs. Run from extracted prior archive.

```python
from fractions import Fraction as F
from pathlib import Path
import json
from math import ceil
from check_extra_core import dot,normal
ns={}
exec(Path('point_section_targeted1138.py').read_text().split('# verify previous basis')[0],ns)
m,cols,e=ns['m'],ns['cols'],ns['e']
G,aj,am,dj,r,u,d=[ns[k] for k in ('G','aj','am','dj','r0','cref','d')]
ex=json.load(open('extra_rows_1136.json'))
m=m+[v['m'] for v in ex]
cols=[v+[x['cols'][j] for x in ex] for j,v in enumerate(cols)]
e=e+[v['error'] for v in ex]
lines=[tuple(map(int,l)) for l in json.load(open('extend1139.json'))['runs'][-2]['lines']]
assert len(lines)==16
K=d[1]+F(800000,544447235321021556325566186117974922693)
H=2*K; L=10**114
remaining=set(range(16)); ratios=[]
for I in [(0,1,2,3,4,5,8),(0,1,2,3,4,5,9),(0,1,2,3,5,6,7),(0,1,2,3,5,6,8)]:
    w=normal([[v[i] for i in I] for v in cols[:6]])
    assert w is not None
    n=[0]*10
    for i,v in zip(I,w): n[i]=v
    assert all(dot(n,v)==0 for v in cols[:6])
    z=dot(n,m)
    S=sum(abs(dot(n,v)) for v in cols)+sum(abs(v)*t for v,t in zip(n,e))
    a=-G*(n[0]*aj+n[1]*dj); b=G*n[1]*am
    hits=[]
    for j in sorted(remaining):
        q,p,h=lines[j]
        v=a*(F(p,q)-r)+b*(F(h,q)-u)-z
        pos=S+max(0,-a)*K/L**2+max(0,b)*H/L
        neg=S+max(0,a)*K/L**2+max(0,-b)*H/L
        ratio=max(v/pos,-v/neg)
        if ratio>1: hits.append(j);ratios.append(ratio)
    print(I,hits)
    remaining.difference_update(hits)
assert not remaining and min(ratios)>1
print(float(min(ratios)))
```

## Next
Recompute the integer-coordinate basis against the new polygon and enlarge Q above 10^69, using the 1139 sliced enumeration. If persistent candidates remain, choose further sparse directions or new coupled moments after identifying the bottleneck. No formal task closure or independent review.