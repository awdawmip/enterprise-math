# X6 R76 — 四阶正权 BRC 双参数精度族的 125-Port 严格最优区域

Date: 2026-11-21 (Asia/Shanghai)
Status: CONDITIONAL_AUTHOR_PROOF / EXACT_RATIONAL_AUTHOR_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED
Frozen scientific source: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json` (P000 V5).
Lineage: R68, R72–R75. This is a conditional positive-count BRC histogram observation theorem, not native X6 Cell/Link/Port time dynamics. No P000 change or Result/Review admission.

## Question and definitions

For `D=4`, a nonzero integer histogram difference `a=(a2,a3,a4)` has population requirement
`q(a)=max(sum positive components, sum absolute negative components)`.
Define `z1=0`, `zk=sum_{d=2}^4 a_d(d^k-d)`, k=2,3,4. Measurements have one unknown common additive bias and independently bounded errors `|e_i|<=η w_i`. For the two-parameter family `w=(1,t,u,1)`, `t,u>0`, the pair collision radius is

`F(a;t,u)=1/2 max_{1<=i<j<=4} |z_i-z_j|/(w_i+w_j)`.

The optimal radius `η*_{p,4}` minimizes F over nonzero integer differences with `q(a)<=p`.

## Theorem R76 — exact full-dimensional winner chamber

The three explicit candidate differences are

| Name | a=(a2,a3,a4) | q | z=(z1,z2,z3,z4) |
|---|---|---:|---|
| S | (114,-56,11) | 125 | (0,24,0,0) |
| L | (10,-5,1) | 11 | (0,2,0,2) |
| H | (45,-21,4) | 49 | (0,12,6,0) |

Put `m(u)=min(max(1/2,1/(1+u)),3/(1+u))` and `E(t,u)=12/(t+min(1,u))`.

**For every real t,u>0 and every integer p>=125, S and -S are the only optimal integer differences if and only if E(t,u)<m(u).** Equivalently, the strict winning region is

```
0<u<=1:  t>12+11u
1<=u<=5: t>23
u>=5:    t>4u+3
```

Endpoints agree. At equality `E=m`, S ties L (u<=5) or H (u>=5). When `E>m`, S is strictly suboptimal.

Moreover, in the high-t region `(0<u<=5 and t>=1) or (u>5 and t>=2u+1)`,

`η*_{124,4}(1,t,u,1)=m(u)`

and for every integer `p>=125`,

`η*_{p,4}(1,t,u,1)=min(m(u),12/(t+min(1,u)))`.

Therefore the strict 124→125 drop on this region occurs exactly at the stated strict boundary. Outside the high-t region, the separate R72 exact 28-vector atlas gives the corresponding no-drop statement when S is suboptimal; that further corollary uses the author-verified R72 atlas as a dependency. The strict-winner theorem itself is independent of atlas completeness.

## Complete symbolic proof

1. The gaps not involving channel 2 give
`H_u(a)=max(|z3|/[2(1+u)],|z4|/4,|z4-z3|/[2(1+u)])`.
The remaining gaps give
`J_{t,u}(a)=max(|z2|/[2(t+1)],|z2-z3|/[2(t+u)],|z2-z4|/[2(t+1)])`.
Thus `F=max(H,J)`.

2. Integer `d^3-d` is divisible by 6 and `d^4-d` by 2, so `z3∈6Z,z4∈2Z`. If `z3=z4=0`, the equations reduce to `a2+4a3+10a4=0`, `11a3+56a4=0`. Since (114,-56,11) is primitive, the entire integer kernel is `Z·S`. Outside this kernel there are three cases. If `z3=0,z4!=0`, H is at least `max(1/2,1/(u+1))`; if `z3!=0,z4=0`, H is at least `3/(u+1)`; if both are nonzero, H is at least `max(1/2,3/(u+1))`. Consequently every nonkernel vector has `F>=H>=m(u)`.

3. S has fine gaps zero and radius E. Any nonzero integer multiple kS has radius |k|E. Hence E<m makes ±S the unique global minimizers for p>=125, without a finite atlas.

4. Conversely, compute directly:
`F(L)=max(max(1/2,1/(1+u)),1/(t+min(1,u)))`
and
`F(H)=max(3/(1+u),6/(t+1),3/(t+u))`.
When `u<=5`, `m=max(1/2,1/(1+u))` and `J(L)=E/12`. When `u>=5`, `m=3/(u+1)` and `J(H)<=E/2`. Thus if E=m, S ties L or H; if E>m, one of them strictly improves on S. This proves necessity and boundary claims. Evaluating m as `1/(1+u)` on (0,1], `1/2` on [1,5] and `3/(u+1)` on [5,infinity) yields the stated threshold formulas.

5. If u<=5 and t>=1, `J(L)<=H(L)=m(u)`; if u>5 and t>=2u+1, `J(H)<=H(H)=m(u)`. L requires 11 Ports and H 49 Ports. Every other nonkernel difference costs >=m; a nonzero kernel vector requires at least 125 Ports. Hence the exact 124-Port value is m. Adding S at p>=125 yields min(m,E); all other kernel multiples cost >=E. QED.

## Exact verification and limitations

The executable standard-library verifier `x6_r76_two_parameter_strict_winner_verify.py` checks 15,624 nonzero signed triples in [-12,12]^3 for congruences, kernel and gap lower bounds, and checks 48 rational (t,u) profiles using `fractions.Fraction` against all 28 R72 atlas vectors. All assertions PASS. Finite checks confirm examples; the general real-parameter claim follows from the symbolic proof, not sample extrapolation.

Verification files: `research_notes/portable_direct/x6_r76_two_parameter_strict_winner_verify.py`, `research_notes/portable_direct/x6_r76_two_parameter_strict_winner_results.json`.

The positive histogram observer does not restore named-port joint provenance, full triadic events, signed/phase state, source-native Cell/Link incidences or physical time-update laws. Next: exact four-weight optimality chambers, global pruning of 28 atlas candidates, and provenance-preserving native-to-BRC observation/fiber tests. Historical researcher provenance EM-X6-214D9C and Activity RA-545183ADD4EF71C3E4698AEE are *not* live execution authority; no native CLAIM, Activity mutation, formal PROGRESS or review is asserted.
