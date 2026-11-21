# X6 R79 — 任意正权四阶 BRC 星形矩：28 候选精确缩为最小九元充分核心

Date: 2026-11-21 (Asia/Shanghai)
Status: CONDITIONAL_AUTHOR_PROOF / EXACT_CERTIFICATE / NOT_INDEPENDENTLY_REVIEWED.
Frozen scientific pin: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`.
Direct source: R72 28-vector exhaustive finite atlas certificate; R78 nine strict open winning profiles.
Boundary: this is a **conditional positive-count BRC histogram observer**, not native six-axis X6 Cell/Link/Port/triadic time dynamics. Joint history, signed forces, provenance and future transitions are not removed from the original object.

## Claim (minimal nine-entry subatlas, all positive weights)

Let the maximum independent source degree be 4, population p>=125, and observe moments t=1,...,4 with one unknown shared additive offset and errors bounded by eta*w_t, where w=(A,B,C,D) has **arbitrary positive real entries**. For a=(a2,a3,a4)∈Z³\{0}, let
`q(a)=max(sum max(a_d,0),sum max(-a_d,0))`,
`z(a)=(0, 2a2+6a3+12a4, 6a2+24a3+60a4, 14a2+78a3+252a4)`, and
`F(a;w)=max_{i<j} |z_i-z_j|/[2(w_i+w_j)]`.

The R72 exact finite-cover atlas `T` has 28 unoriented vectors and covers all integer differences at each p>=4. Define the nine-vector subatlas

| q | (a2,a3,a4) | R72 zero-based atlas index |
|---:|---|---:|
|7|(6,-4,1)|14|
|10|(9,-5,1)|17|
|11|(10,-5,1)|18|
|16|(15,-6,1)|19|
|27|(24,-14,3)|21|
|39|(36,-16,3)|22|
|43|(39,-20,4)|23|
|49|(45,-21,4)|25|
|125|(114,-56,11)|27|

Then **for every** positive real w and every integer p>=125,
`eta*(p,w) = min_{a in T} F(a;w) = min_{a in S} F(a;w)`.
Moreover **no proper subset of the specified R72 atlas having fewer than nine entries** is sufficient for all w>0 at p>=125. Thus nine is the **exact minimum cardinality among subatlases of T**. The general equality with all feasible integer differences uses R72's separate finite-cover certificate. The new T→S reduction is a universal exact symbolic proof.

## Proof: 17 coordinatewise certificates, two combined witnesses

Write `g_{ij}(a)=|z_i-z_j|/2`, so `F(a;w)=max_{i<j} g_{ij}(a)/(w_i+w_j)`. The six gaps are listed in order (12,13,14,23,24,34). If `g(b)<=g(a)` in all six coordinates then `F(b;w)<=F(a;w)` for every positive w.

For 17 of the excluded 19 R72 entries, the companion program performs **all six exact integer inequalities** and records a selected core witness for each excluded vector. No large-weight approximation or positive-weight grid is needed for this quantifier. These 17 witnessed R72 indices are 0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,20. Their exact matchings are preserved in the results JSON.

The remaining R72 entries have Port demands 47 and 71 and indexed gap vectors

- `g_47=(0,12,12,12,12,0)`;
- `g_71=(12,12,0,0,12,12)`.

Using the four positive weight names (A,B,C,D), their objective functions are exactly

`F_47=12/(min(A,B)+min(C,D))`,
`F_71=12/(min(A,D)+min(B,C))`.

Two *included* core vectors have

`F_27=6/(C+min(A,B,D))`,
`F_39=6/(A+min(B,C,D))`.

Hence, setting `U=max(A+min(B,C,D), C+min(A,B,D))`,

`min(F_27,F_39)=6/U <=6/max(A,C)<=12/(A+C)`.

Both `min(A,B)+min(C,D)` and `min(A,D)+min(B,C)` are at most `A+C`. Therefore

`min(F_27,F_39) <= min(F_47,F_71)`,

and, more strongly, the same left-hand side is <= **each** of `F_47,F_71` for all w>0. This establishes coverage of both exceptions without assuming a fixed winner or any restrictions on weight ratios. Each pair witness requires no more than 39 Ports, below 47 and 71 respectively.

Thus every vector in T is no better than at least one member of S (for the exceptional two, one of the two members depends on w). This proves `min_T F=min_S F` for all positive w. For p>=125, all nine are feasible.

For minimality, R78 supplies nine separate *strict* unique winners of T at the exact positive-integer weight profiles stored again in the R79 verifier. At each profile, deleting its strict-winning S element increases the optimum against all remaining members of T. Therefore any universally sufficient subset of T contains every member of S, and nine is minimal. QED, conditional on the stated R72 atlas for the global integer-lattice reduction.

## Computable nine-term closed formula

The nine terms may be evaluated directly using the gap tuples
`(0,0,12,0,12,12)`,
`(0,3,6,3,6,3)`,
`(1,0,1,1,0,1)`,
`(3,3,3,0,6,6)`,
`(0,6,0,6,0,6)`,
`(6,6,6,0,0,0)`,
`(3,3,3,6,6,0)`,
`(6,3,0,3,6,3)`,
`(12,0,0,12,12,0)`
in the displayed S order. Divide each coordinate by the corresponding positive pair sum, take the max of six, then the min of nine. This gives at most 54 gap/denominator comparisons instead of 168 for T; it is a count of objective terms, **not** a measured runtime speedup.

## Reproduction, limitations, and next question

Run `node x6_r79_nine_core_exact_verify.js`: it reproduces all 28 gap vectors from source moment formulas, checks q, confirms 17 coordinatewise domination pairs, confirms the four exceptional structural vectors, checks all 9 strict winner profiles by exact BigInt cross-products, and independently spot-checks T/S equality over 6^4=1296 integer positive weight profiles. The universal equality is the algebraic argument above, not an inference from the finite grid.

This result is relative to the specific R72 28-vector *subatlas*: it does not establish that no alternative set of non-atlas integer vectors could replace one of S. R72's 21,492,159-case full covering and general cone reduction have author-checked certificates, not an independent mathematical admission. The native named Port/Cell/Link/whole-triadic event interface is an additional future research problem.

Next: derive **precise tie/chamber boundaries** of the nine-term formula, extend the q-filtered minimal subatlas to p<125, and separately construct a provenance-preserving native observer factor map or explicit counterexample at the frozen P000 Cell/Link/Port transition horizon.

Attribution: R72/R78 historical independent portable source EM-X6-214D9C; this scientific derivation preserves that source provenance. The historical Activity and current formal claim are separate from this paper's GitHub bytes.
