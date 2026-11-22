# X6 R103 — Heavy-center positive BRC ray: exact Port-28 tie and Port-39 transition

Date: 2026-11-22 (Asia/Shanghai). Status: SYMBOLIC_AUTHOR_PROOF / EXACT_INTEGER_AUTHOR_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED.
Scientific input pin (unchanged): `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`.
Predecessors: R89 (general positive weights), R99–R102 (complete results **only** for the separate `w=(1,1,S,T)` section). This note is an independent derivation for the asymmetric section `w=(T,1,1,1)`.

## Exact observer and scope

This is a *conditional auxiliary* four-channel positive-count BRC star-moment observer, **not** the native signed X6 Cell/Link/triadic-force/heartbeat dynamics. For nonzero `a=(x,y,z) in Z^3` identify `a` with `-a`, define
```
q(a) = max(x+ + y+ + z+, (-x)+ + (-y)+ + (-z)+)
u=x+3y+6z,  v=3x+12y+30z,  h=7x+39y+126z.
M(a)=max(|u|,|v|,|h|)
D(a)=max(|v-u|,|h-u|,|h-v|)
```
For positive weights `w=(T,1,1,1)`, with `T>=1`, the pairwise score (the normalized R89 star-gap observer) is exactly
```
F_T(a) = max( M(a)/(T+1), D(a)/2 ).
eta_p(T) = min { F_T(a): a != 0 unoriented, q(a)<=p },  p integer >=11.
```

Set `s=(10,-5,1)`, `b=(26,-11,2)`, `c=(36,-16,3)`, with Port costs `q(s)=11`, `q(b)=28`, and `q(c)=39`.

## Theorem R103 (all real T>=1 and all integer p>=11)

The exact optimum is
```
eta_p(T) = 1/2                         if p<=38 or T<=11,
           6/(T+1)                     if p>=39 and T>11.
```
The **entire** optimal unoriented direction set is:

| Range of T | 11<=p<=27 | 28<=p<=38 | p>=39 |
|---|---|---|---|
| 1<=T<11 | {s} | {s} | {s} |
| T=11 | {s} | {s,b} | {s,b,c} |
| T>11 | {s} | {s,b} | {c} |

Consequently, changing only the *first* weight creates two distinct sharp Port phenomena: a non-C10 tie appears at Port **28**, and the optimum strictly improves at Port **39** for T>11. The ten-direction kernel from R99 and Port-27 stabilization from R98–R102 are statements about `(1,1,S,T)` and do **not** extend to arbitrary four weights. The witness `b` is outside that kernel.

## Proof: integer lattice fibers

First, `s` has moment triple `(u,v,h)=(1,0,1)`, so `M(s)=D(s)=1`, `F_T(s)=1/2` for T>=1. Hence `eta_p<=1/2`.

For every integer triple the following exact divisibilities hold:
```
v in 3Z,  h-u in 6Z,  h-u-6v in 12Z.
```
Suppose `F_T(a)<1/2`. Then `D(a)<1` and D is a nonnegative integer, so `D(a)=0`; equivalently `u=v=h=t`. The last two congruences force `v=t in 6Z`. Alternatively the exact inverse map is
```
x=(h+19u)/2-4v,
y=(-h-14u+7v)/3,
z=(h+11u)/12-v/2.
```
Substituting `u=v=h=t` yields `a=(6t,-8t/3,t/2)`; integrality is equivalent to `t in 6Z`. Thus every possible strict improver is `a=k c` with nonzero integer k, with `q(k c)=39|k|` and `F_T(k c)=6|k|/(T+1)`.

If `p<=38`, no strict improver is feasible. If `T<=11`, every such diagonal direction has score >=1/2. In both cases `s` achieves the optimum. If `p>=39,T>11`, `c` achieves `6/(T+1)<1/2`; any competitor with `D>=1` costs >=1/2, and among `D=0` vectors `c` uniquely minimizes up to sign. This proves the exact value and the last table cell.

It remains to classify plateau ties, i.e. `F_T(a)=1/2` when `eta_p=1/2`. Necessarily `D(a)<=1`, so `|h-u|<=1`, but `h-u in 6Z` forces `h=u`. Put `delta=v-u in {-1,0,1}`. Since `h-u-6v in 12Z`, `v` is even; since `v in 3Z`, `v=6k` for an integer k. Substitution in the exact inverse gives the *complete* lattice-fiber parameterization
```
a=k c - delta s
 =(36k-10delta,-16k+5delta,3k-delta),  k in Z, delta in {-1,0,1},
M(a)=max(|6k|,|6k-delta|),  D(a)=|delta|.
```
Conversely all these are valid integer triples and have D<=1. A plateau tie therefore satisfies exactly `a!=0`, `q(a)<=p`, `M(a)<=(T+1)/2`, and (for delta=0) `F_T(a)=1/2` as well. The latter equality is automatic for every feasible nonzero `a` in a plateau region: if it were strict, it would contradict the already-proved plateau value.

When `1<=T<11`, `M<6` and hence k=0, giving only ±s. At T=11, `M<=6`, so |k|<=1; up to sign the remaining possibilities are s, `c-s=b` (M=6), and c (M=6), with respective q=11,28,39; `c+s` has M=7 and is excluded. Finally when T>11 but p<=38, `|k|>=2` entails `|x|>=62>38`, and the possible |k|=1 directions c (q=39), c+s (q=50), c-s=b (q=28) leave only b beside s. For T>11,p>=39, strict improvement already made c uniquely optimal. This proves the complete tie table. QED.

## Author-side exact verification

The accompanying `x6_r103_heavy_center_ray_verify.py` evaluates the integer score numerator `max(2M,(T+1)D)` over the **complete** 157,020 unoriented nonzero integer triples satisfying q<=45. It compares the *entire* optimal direction sets and exact values for each of 42 pairs: T=1,10,11,12,25,100 and p=11,27,28,38,39,40,45. All 42 cases passed. The exhaustive finite check corroborates the analytic all-integer proof; it does not substitute for it or constitute independent review.

## Scientific boundary and continuation

The exact Port-28 and Port-39 transitions are mathematical features of this positive observer. They have **not** been proved to be native P000 Cell/Link events or safe under future heartbeat updates. The new three-fiber relation `a=k c-delta s` is a reusable exact arithmetic interface.

Next: seek a general four-positive-weight finite or certified-infinite candidate reduction; classify which asymmetric weights admit arbitrarily many optimal ties; investigate native named-Port, ordered triadic event and path-provenance observer fibers, retaining the P000 original six-axis/time ontology. Existing shared owner/CLAIM/Activity, if any, are operationally separate and not asserted by this scientific note.
