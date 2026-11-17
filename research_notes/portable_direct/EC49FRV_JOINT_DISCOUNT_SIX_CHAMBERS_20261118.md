# EC49FRV — Six exact native-BRC Bellman price chambers under a pair of discounted named observations

**2026-11-18 | AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.** Parent frontier EC49FRU, [PR #2655](https://github.com/awdawmip/enterprise-math/pull/2655). Frozen scientific pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Independent portable scientific note, not a Task/CLAIM, formal Result or Review.

## Typed model and theorem

Original BRC class 16943; all **141 complete named-response states** representing 310 configurations, all **228 physical named observers** (144 terminal + 84 root), including native root-key and original joint-relation observers. Uniform distribution on named states (`lambda=0`), root/terminal base cost ratio `x=1`, base observer price `t>0`. Only native terminal observations **32 and 34** are discounted together to `(1-s)t`; every other native observation costs `t`. All prices are strictly positive for `0<=s<=3/5`.

For each valid complete adaptive tree Q let `U(Q)` be total physical observation uses across the 141 paths, and `K(Q)=n_32(Q)+n_34(Q)` its exact (named) discounted-observer uses. Hence `141*C_Q(s)/t=U(Q)-s*K(Q)`.

**Theorem.** The global optimum over *every* legal complete original-native tree, for all real `0<=s<=3/5`, equals

```text
141*V(s)/t =
  296 - 152*s       for 0      <= s <= 1/4
  297 - 156*s       for 1/4    <= s <= 1/3
  304 - 177*s       for 1/3    <= s <= 2/5
  306 - 182*s       for 2/5    <= s <= 1/2
  310 - 190*s       for 1/2    <= s <= 5/9
  315 - 199*s       for 5/9    <= s <= 3/5.
```

At shared endpoints both formulas agree. The six lines have distinct integer incidence pairs `(U,K)`; each is realized by a fully replayed native decision tree. Each line is uniquely optimal in its corresponding nonempty open interval; consequently **at least six fixed affine-incidence types** are necessary for a uniform optimal-menu covering the stated price interval, and six suffice.

At the endpoint `s=3/5`, the additional tree `(U,K)=(321,209)` also attains the Bellman value `978/5`. The type `(318,204)` is another exact tie there, but its optimality on an open interval is not asserted.

## Exact integer Bellman anchors (two original-input reconstructions)

Integer query prices use denominator q: `c32=c34=q-p`, `c_other=q` at `s=p/q`. The objective computed is `q*(141*V/t)`, an **integer**. A tie-breaking rule maximizes K among exact cost minimizers; this selects a right-hand witness at each anchor.

| s | q*(141 V/t) | witness U | witness K | number of reached DP subsets | witness maximum depth |
|---:|---:|---:|---:|---:|---:|
| 0 | 296 | 296 | 152 | 12404 | 3 |
| 1/4 | 1032 | 297 | 156 | 11691 | 3 |
| 1/3 | 735 | 304 | 177 | 11300 | 4 |
| 2/5 | 1166 | 306 | 182 | 10855 | 4 |
| 1/2 | 430 | 310 | 190 | 10173 | 4 |
| 5/9 | 1840 | 315 | 199 | 9704 | 4 |
| 3/5 | 978 | 321 | 209 | 9050 | 4 |

All seven anchors were computed with exact integer Bellman recursion on **all 228 named physical observations** and independently reconstructed original observer-response data. The two source parsers yield identical complete native responses and identical integer optimal values/usage vectors; they share the mathematical DP recurrence (not claimed to be two independently designed solvers). At each anchor, the entire extracted optimal tree was replayed on all 141 original response states; every state reached its correct unique leaf. The stored full tree witnesses and per-anchor results are produced by the accompanying verifier.

Bellman recurrence on a non-singleton state mask `S`:
```text
B(S) = min over every original named q that splits S:
       |S| * c_q + sum_{nonempty distinct response fibers T subset S} B(T)
B({state})=0.
```
Strict positivity means queries that leave S unchanged can be omitted from a minimum-cost complete tree. Thus all legal useful actions are exhausted by this recursion.

## Proof on the complete real interval

For any fixed complete identifying tree Q the cost `U(Q)-s*K(Q)` is affine in s. Their pointwise infimum `F(s)=141*V(s)/t` is concave. Fix any of the six consecutive intervals `[s_i,s_{i+1}]` in the anchor table and its indicated witness line `L_i(s)=U_i-s*K_i`. That exact complete tree gives `F(s)<=L_i(s)` on the entire interval. The two endpoint Bellman calculations verify `F(s_i)=L_i(s_i)` and `F(s_{i+1})=L_i(s_{i+1})`. Concavity gives `F(s)>=L_i(s)` between those endpoints. Combining the two inequalities yields equality across the full real interval, with no mesh approximation.

The six affine pairs are distinct and each has an open interval where it realizes this exact optimum. If a single fixed tree were optimal throughout two such open intervals, its affine cost would equal two different affine functions on intervals, impossible. This establishes the six-type menu lower bound.

## A new counterexample to extending the nonnegative-surcharge result

EC49FRU's four-surcharge menu, extrapolated outside its declared nonnegative domain, would yield `296-141s` along `a=b=-s, c=d=0`. Already for any `0<s<=1/4` the actual optimum is `296-152s`. The overestimate is exactly `11s*t/141` in expected cost. The reason is concrete: a base-cost-optimal native tree can use **both** original observations 32 and 34 along some paths, attaining `K=152` although the old five-witness menu uses at most 141 discounted visits. This is an exact native counterexample to the proposed continuation of that menu; it leaves EC49FRU's theorem on its original `a,b,c,d>=0` domain intact.

## Sources, scope, reproduction

Frozen originals (inside the EC49FRU local evidence archive): `source/frozen_original_master.txt` SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`; `source/EC49FPG_PROFILE.csv` SHA256 `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`. The existing original-data modules are `code/EC49FQI_NATIVE_DATA.py` and `code/EC49FRQ_INDEPENDENT_ALL228.py`. Extract the EC49FRU archive and run the accompanying `EC49FRV_JOINT_DISCOUNT_EXACT_CERTIFIER.py` with the extracted bundle root; the script regenerates exact Bellman values and full 141-state tree certificates.

This result is exact for the frozen finite, original-native class, uniform named-state prior, base price x=1 and `0<=s<=3/5`. The current paper does not assess the higher-discount interval, nonuniform source weights, or independently certify reviewer admission. P000 and the ACTIVE six-dimensional Heartbeat-world premises are unchanged; this is a typed finite observer/cost optimization subproblem, not a new space ontology.

**Next research:** certify remaining `3/5<s<1` phase chambers and the full exact 2D discount region for 32 and 34, preserving all original named observers; investigate whether varying nonuniform priors changes the six-incidence menu.
