# Stage170 — exact real interval and right-endpoint sharpness (author computation-assisted proof)

**Status:** AUTHOR_EXACT_PROOF; native Research Driver review and P000-native transfer NOT established. The theorem concerns only the external finite ternary IID sequential-testing model, not the Heartbeat native X6 Cell structure.

## Frozen inputs and model

GLOBAL_KNOWLEDGE_V1 **main@91502738ab6c509f1e3048394ea361bc8fa0776e**; Enterprise Math research source **main@21380852aafeb2b1092442d629c22efb7e7304a8**. P000 startup projection blob matches the canonical original P000 blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`. The ACTIVE residual-fidelity worldview, TASK route, BRC positive branch laws, and current portable research protocol have been read. Historical Stage169 mathematical input is exactly the immutable preceding proof `6da28497a0d69fec27648bd50b7611b3add67e89` and its Stage170 candidate `candidate170.json`.

For every finite ordered history, allow arbitrary history-dependent randomized stop/continue and final decision, with sample bound N=14, under the positive ternary laws
[
P=(1/8,1/24,5/6),\qquad Q=(1/12,1/12,5/6).
]
Define `e_P=P(decide Q)`, `e_Q=Q(decide P)`, `t_P=E_P tau`, `t_Q=E_Q tau`, and
[
V_{14}(\alpha)=\inf_{e_P,e_Q\le\alpha}\max(t_P,t_Q).
]

## Theorem (entire real interval)

Let
[
\alpha_{169}=\frac{882433753904177815735}{2530093150022563528704},\qquad
V_{169}=\frac{4191297370163761372757}{361441878574651932672},
]
and let `eta_170=152674215625/274532676868767744`. Then, for **every real** `0 <= delta <= eta_170`,
[
\boxed{V_{14}(\alpha_{169}+\delta)=V_{169}-\frac{28504525}{56787}\delta.}
]
The right endpoint and its optimum are
[
\boxed{\alpha_{170}=\frac{126062165849964145105}{361441878574651932672}},\qquad
\boxed{V_{170}=\frac{4191196473918241372757}{361441878574651932672}}.
]
The displayed supporting line is **strictly below** the optimum at every real `alpha>alpha_170` (sharpness of this support, not an assertion that the entire function ceases to be piecewise affine).

## Proof 1: exact Bellman bound for all ordered-history policies

For count state `s=(n,a,b)`, number of observations of symbols 0 and 1, `Q(history)/P(history)=ell(s)=2^(a+b)/3^a`. Set
[
K=\frac{4773735}{18929},\qquad L=\frac{14183320}{56787}.
]
For `n<14`, with `s+i` the appropriate next count state, define
[
H(s)=\min\{K\ell(s), L, 1+\sum_{i=0}^{2}P_iH(s+i)\},
]
omitting continuation at depth 14. This is the pointwise lower Bellman envelope for the objective `t_P+K e_Q+L e_P` weighted by P-prefix probability. Its exact root is
[
H(0,0,0)=\frac{290341590799397120042729}{1555410727388508585984}.
]
Exact rational induction covers all **680** count states and finds exactly **1,238** strictly positive nonminimum gaps, minimum `569/56787`, no negative gaps, and only two ties:
`R=(10,0,1): Q versus continue`; `T=(12,5,2): P versus continue`. All other minimizers are unique.

The count-state Bellman bound applies to *arbitrary ordered-history rules*, because conditional IID suffix laws are history-independent at a fixed count state. Thus `H(root)<=t_P+K e_Q+L e_P<=max(t_P,t_Q)+(K+L)alpha`, where `K+L=28504525/56787`, giving the desired universal supporting-line lower bound.

## Proof 2: ordered-prefix construction and all real coin parameters

At R, stop/decide Q with probability `r`; at T, stop/decide P with probability `u`; otherwise continue there, and everywhere else use the unique Bellman-minimizing action. The two first-hit ordered prefix cones **cannot intersect**. T is at depth 12 and has five symbols 0, whereas R is at depth 10 and has none: at most two extra observations could follow R to T, not five zeros. T is deeper so cannot precede R. This is a statement about *true ordered histories*, not only the two distinct count triples.

Independent literal integer-numerator unmerged ordered-prefix DFS and rational suffix recursion agree component-by-component on the full four corners `(r,u)=(0,0),(0,1),(1,0),(1,1)`. Integer branch numerators are `P:(3,1,20)/24` and `Q:(1,1,10)/12`; terminal masses under each law sum exactly to one at every corner. Ordered DFS terminal leaf counts are 234889, 214241, 234729 and 214081 respectively. True first-hit data are:
- `R`: 10 ordered histories; P mass `9765625/120932352`; Q mass `9765625/60466176`.
- `T`: 5162 ordered histories; P mass `8065625/73383542784`; Q mass `8065625/139314069504`.

Consequently the observer `M=(e_P,e_Q,t_P,t_Q)` is exactly affine in `(r,u)`; the mixed `ru` coefficient is zero for all four observers. Exact equality `e_P=e_Q` is equivalent to
[
\boxed{r(u)=\frac{8976558429259453}{11823616000000000}
+\frac{5541407}{3694880000}u}.
]
The entire interval `u in [0,1]` gives legal coins `0<r(u)<1`, balanced errors and strictly `t_P>t_Q`. At `u=0`, the observer is exactly the Stage169 inherited `(alpha_169,V_169)`. At `u=1`, it is exactly the `(alpha_170,V_170)` above. The errors grow linearly with strictly positive slope
[
\frac{d\alpha}{du}=\frac{152674215625}{274532676868767744}>0.
]
At the two endpoints (hence by affinity throughout) `t_P+K e_Q+L e_P=H(root)`. Since `t_P>t_Q`, every real alpha in this interval has an explicit legal primal rule attaining the universal dual lower bound. This completes the theorem.

## Proof 3: strict right-endpoint sharpness of this support

Suppose an arbitrary ordered-history randomized rule attained the same affine supporting bound at some real `alpha>alpha_170`. Because `K,L>0`, equality in the dual inequalities forces `e_P=e_Q=alpha`, `t_P=max(t_P,t_Q)`, and all actions on positive-mass histories to minimize the exact Bellman values. The 1,238 strictly positive gaps force effective randomization to occur only at R and T. At a given tied count state, every actual prefix has the same likelihood ratio `Q/P` and the same conditional suffix laws; hence heterogeneous history-dependent coins can be replaced by their P-first-hit-mass-weighted effective coin without changing `e_P,e_Q,t_P,t_Q`. Disjointness of the true cones makes the full observer exactly `M(r,u)`. Balanced errors then impose the unique relation `r=r(u)`. Among legal `0<=u<=1`, balanced alpha is strictly increasing and at most `alpha_170`, contradiction. Compactness of the finite ordered-history policy polytope ensures an optimum exists, so the supporting lower bound is strictly below the true optimum for every alpha beyond the endpoint.

## Numerical-free verification and admission boundary

`VERIFY_STAGE170.py` uses only Python integer and `fractions.Fraction` exact arithmetic, count-state Bellman induction, cached rational suffix recursion and structurally separate literal ordered-prefix integer DFS. No floating point, sampled-alpha extrapolation, unverified full-history quotient, or external numerical library is involved. It asserts the gap census, ties, first-hit masses, all four corner vectors, cross-term zero, inherited Stage169 endpoint, legal balanced coins, right endpoint, positive t_P-t_Q, and dual tightness. Its actual local run was PASS. This is **an author computation-assisted mathematical proof**, not an independent Driver review, Lean certificate, formally frozen Result, Source-native CLAIM, or P000 X6 embedding. Native control task list returned `CONTROL_QUOTA`; session_start returned `STATIC_READONLY_SCOPE_DENIED` and `operation_sent=false`; active native Owner remains unverified. Ordinary GitHub publication does not grant formal execution authority.

BRC use: exact ordered positive-rational branch provenance is retained before the count-state quotient; this is compatible with the finite-positive-rational branch carrier in `definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json` (at EM ref above). The Bellman count quotient is used only after proving the declared four observers factor through the IID conditional suffix law. There is no assertion of a native X6 Cell map.

## Next bounded research unit

An author exact **Stage171 dual candidate** from the R-preserving direction `dK=-1, dL=-10592/12501`, with T taking action P, is `K171=378837/1529, L171=1128472/4587`, new tied state `Z=(12,4,3):Q/C`, persistent `R=(10,0,1):Q/C`; 680 Bellman states, 1238 strictly positive gaps, min gap `3442966771823/94671649898496`, root `332293501648867121767/1807757198084800512`. **This is dual-only; no primal Stage171 theorem is claimed.** Next: exact R,Z first-hit mass / disjointness, four observer corners and maximal balanced-alpha boundary; obtain primal complete real interval or exact obstruction, then seek independent Driver review.
