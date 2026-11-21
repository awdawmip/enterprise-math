# X6 R91 — Two-parameter BRC precision strip and five-way tie boundary

Date: 2026-11-22 (Asia/Shanghai). Status: SYMBOLIC_AUTHOR_PROOF / EXACT_INTEGER_AUTHOR_CROSSCHECK_PASS / NOT_INDEPENDENTLY_REVIEWED.
Scope: independent portable research, not a formal CLAIM/PROGRESS/Result/Review.
Frozen scientific input: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`. Predecessor: R90 (`2026-11-22_x6_r90_one_channel_ray_exact_phase_diagram.md`), plus R89.
Conditional model only: positive-count degree-four BRC star-histogram observer, unknown common additive offset. No claim of a native P000 operation-preserving projection.

## Exact problem and theorem

For nonzero `a=(x,y,z)∈Z³`, identify `±a` and use the representative whose first nonzero coordinate is positive. Define
```
q(a)=max(sum_i max(a_i,0),sum_i max(-a_i,0))
u=x+3y+6z, v=3x+12y+30z, h=7x+39y+126z
g(a)=(|u|,|v|,|h|,|v-u|,|h-u|,|h-v|)
F(a;w)=max_{ij=12,13,14,23,24,34} g_ij/(w_i+w_j)
eta*(p,w)=min { F(a;w): a != 0, q(a)<=p }.
```
Set `w=(1,1,S,T)` with independent `1<=S<5` and `T>0`, and define `s=(10,-5,1)`, `r=(6,-4,1)`, `j=(4,-1,0)`.

**R91.1: exact two-dimensional uniform strip.** For all real `1<=S<5`, all real `T>0`, and every integer `p>=11`,
```
eta*(p;(1,1,S,T)) =
    1/(1+T)      when 0<T<=1;
    1/2          when 1<=T<=23;
    12/(1+T)     when T>=23.
```
The *complete* optimal unoriented integer direction set is `{s}` for `0<T<23`, `{s,j,r}` at `T=23`, and `{r}` for `T>23`. The branch junction `T=1` changes no optimal direction. Their Port budgets are `q(s)=11,q(j)=4,q(r)=7`. Both value and all-ties atlas are constant throughout the stated S-strip.

**R91.2: sharp boundary.** At `(S,T)=(5,13)`, the global minimum is `1/2`. Exactly these five unoriented integer directions attain it in the unbounded lattice:
```
a=(1,0,0)     q=1    (u,v,h)=(1,3,7)
a=(5,-4,1)    q=6    (u,v,h)=(-1,-3,5)
a=(9,-5,1)    q=10   (u,v,h)=(0,-3,-6)
a=(10,-5,1)   q=11   (u,v,h)=(1,0,1)
a=(15,-9,2)   q=17   (u,v,h)=(0,-3,6)
```
Thus at this boundary there are exactly four minimizers for `11<=p<=16`, and five for `p>=17`. The strict upper strip edge `S<5` cannot be extended as an unchanged uniform *unique-optimum* statement: at `S=5,T=13` multiple new directions tie. Furthermore for any `S>5` choose `0<T<min(1,(S-5)/6)`; then `b=(14,-9,2)` (q=16) satisfies `F(b)=F(s)=1/(1+T)`. This last equality is a loss-of-uniqueness witness if s is still globally best, and does not assert s remains globally best outside the strip.

## Proof of R91.1: every integer direction, without an atlas assumption

The moment map has determinant 36, with inverse
```
x=(19u-8v+h)/2; y=(-14u+7v-h)/3; z=(11u-6v+h)/12.
```
Hence `v∈3Z`, `h≡u+6v (mod 12)`. If `v=0`, then `h≡u (mod 12)`; `u=v=0` iff `a=k r` for integer k.

Direct substitution gives
```
F(s)=max(1/2,1/(1+T)), F(r)=12/(1+T),
F(j)=max(1/2,12/(1+T))
```
because `S>=1`. These give feasible upper bounds in the proposed phases.

(I) If `0<T<1`, take `R=1/(1+T)`. A competitor with `F<=R` must satisfy `|u|<=2R<2`, and `|h|,|h-u|<=(1+T)R=1`. As `h≡u (mod 2)`, this forces `h=u∈{-1,0,1}`. Then `6v≡0 (mod 12)`, so v is even; since it is also a multiple of 3, `v∈6Z`. For nonzero v, `|h-v|>=5`, but `|h-v|<=(S+T)/(1+T)<5` since `S<5`. Thus v=0. The only nonzero solutions are `(u,v,h)=(1,0,1),(-1,0,-1)`, or `±s).

(II) If `1<=T<23`, take `R=1/2`. Then `|u|<=1`, `|v|,|v-u|<=(1+S)/2<3`. Thus v=0. The congruence `h≡u (mod12)` and inequalities `|h|,|h-u|<=(1+T)/2<12` leave only h=u with u=0,±1. Exclude zero; only `±s` remains.

(III) At `T=23`, the same u/v bounds hold, but `|h|,|h-u|<=12`; up to simultaneous sign the complete nonzero solutions are `(u,v,h)=(1,0,1),(1,0,-11),(0,0,12)`, yielding s,j,r. All are feasible and achieve 1/2.

(IV) If `T>23`, take `R=12/(1+T)<1/2`, achieved by r. Any `F<=R` direction has `|u|<=2R<1` and `|v|<=(1+S)R<(1+S)/2<3`, so u=v=0. It is `a=k r`; `F(k r)=|k|R` and only k=±1 minimize. This proves the exact all-lattice result. QED.

## Proof of sharpness and exact edge multiplicities

At S=5,T=13 pair denominators (12,13,14,23,24,34) are `(2,6,14,6,14,18)`. The candidate s has F=1/2. If any F<1/2 then |u|<1 and |v|<3, hence u=v=0 and a=k r, but `F(k r)>=12/14=6/7>1/2`, impossible. Thus global minimum is 1/2.

Any tied direction F<=1/2 obeys
```
|u|<=1, |v|<=3, |h|<=7,
|v-u|<=3, |h-u|<=7, |h-v|<=9.
```
Enumerating this **finite box in the moment coordinates** with v multiple of 3 and the three inverse-map integer divisibility conditions gives, modulo sign, precisely the five directions displayed above. Each satisfies all six inequalities, with at least one equality. This is a global certificate: *every* integer direction with F<=1/2 lies in this box, without a Port cutoff. The five q values give the 17-Port multiplicity transition.

For the outside-strip witness b=(14,-9,2), gaps are (1,6,1,5,0,5), so
```
F(b)=max(1/2,6/(1+S),1/(1+T),5/(1+S),5/(S+T)).
```
Under `0<T<min(1,(S-5)/6)`, all terms are <=1/(1+T), and the 14-pair term equals it. Thus b ties s. QED.

## Evidence, scope and next frontier

The companion exact checker `x6_r91_two_parameter_strip_verify.py` enumerates 47,305 nonzero unoriented q<=30 differences for 32 rational interior (S,T) points and one (5,13) boundary: 1,561,065 exact direction-parameter comparisons, with no below-theorem directions and exact predicted ties. It separately enumerates the *complete* u/v/h boundary box to obtain the same five-tie certificate, and checks the outside-strip (S,T)=(6,1/10) tie. Results are in `x6_r91_two_parameter_strip_results.json`. The unrestricted theorem rests on the preceding symbolic proof, not finite sampling.

This is conditional positive-count BRC, **not** a theorem about the full native P000 six-dimensional signed Cell torsor. The P000 named Ports, joint three-force events, provenance, path identity and heartbeat temporal order remain uncollapsed; no operation-preserving or future-horizon fiber theorem is claimed. No frozen scientific inputs are modified. Independent peer review is pending.

Original control requests `emr2-20261122-0210-x6-task-status-r91-v1` and `emr2-20261122-0210-x6-cont-status-r91-v1` both ended FAILED / SOURCE_TREE_TRUNCATED. No fresh authenticated owner/CLAIM or execution authorization could be established; no formal control mutation was made.

Next scientific question: classify the joint boundary arrangement for S>=5, its noncore directions, Port-sensitive multiway walls, and the native P000 full-triad/name/time observation fibers separately.
