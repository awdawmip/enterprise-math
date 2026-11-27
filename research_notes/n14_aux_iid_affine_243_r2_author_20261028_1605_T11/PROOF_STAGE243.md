# Stage243 exact all-real interval: external N=14 ternary IID stopping

**Classification:** `AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED` (2026-10-28). This is an author-side external mathematical auxiliary model, not a native Heartbeat/X6 evolution claim, canonical Source Result, active Task CLAIM, or independent Driver review. Local contributor for this run: `EM-R2-20261028-1605-T11-PORTABLE` (not a service-issued researcher/session ID). The prior immutable author frontier is Stage242, PR #1571 at `f12577e24d11dfe178f596935adfadf8c68f1496`.

## 1. Exact proposition

Let independent ordered observations take values in `{0,1,2}` with

`P=(3,1,20)/24`, `Q=(2,2,20)/24`, horizon `τ≤14`.

Any stopping rule, including arbitrary full-ordered-history randomization, outputs P or Q. Let `e_P=P(output Q)`, `e_Q=Q(output P)`, `t_P=E_P τ`, `t_Q=E_Q τ`, and

`V14(α)=inf{max(t_P,t_Q) : e_P≤α, e_Q≤α}`.

Put

`α242 = 1092145237285/2925595459584`,
`V242 = 2619507545471/365699432448`.

**Theorem (Stage243 author proof).** For **every real** `δ` satisfying

`0 ≤ δ ≤ 1462826275/3900793946112`,

we have exactly

`V14(α242 + δ) = V242 - (33611704152/292565255) δ`.

The new endpoint is

`α243 = 4372969427965/11702381838336`,
`V243 = 10415008236599/1462797729792`.

At the right endpoint a witness also has `t_Q=19294495501385/2925595459584 < t_P=V243`.

## 2. Rational dual certificate

At count state `s=(n,a,b)`, where `a=#(symbol 0)`, `b=#(symbol 1)` and `n≤14`, the prefix likelihood ratio is `r_s=Q(w)/P(w)=2^(a+b)/3^a`. The 680-state Bellman problem for the Lagrangian `t_P+λ_P e_P+λ_Q e_Q` is

`B(s)=min{λ_Q r_s, λ_P, 1 + Σ_j P_j B(s+j)}`,

omitting continuation when `n=14`. Exactly use

`λ_P=16197445464/292565255`,
`λ_Q=17414258688/292565255`,
`H=B(0,0,0)=9562472712223311917/191055263763400704`.

A symbolic reconstruction of these multipliers is possible from two independent policy-tie affine difference equations `P-C=0` at `(2,1,0)` and `Q-C=0` at `(3,1,1)`:

`-1 -(1/24) λ_P +(1/18) λ_Q=0`,

`-131322119/80621568 +(191164153/1934917632) λ_P -(70231801/1088391168) λ_Q=0`.

The downstream Bellman-minimal deterministic choices determine the affine continuation forms; both equations hold exactly for the stated rational multipliers. The reference code then recomputes **every** Bellman state by exact `Fraction`, without relying on discovery floating-point arithmetic. It obtains 13 binary tie states: `(2,1,0)`, `(3,1,1)` and `(n,1,0)` for `n=3,…,13`; all are `P/C` except `(3,1,1)` (`Q/C`). There are 1,227 strictly positive action gaps, smallest `1953125/2106469836`; no triple ties. Consequently every strategy (including full-history randomized ones) satisfies

`max(t_P,t_Q) ≥ t_P ≥ H-λ_P e_P-λ_Q e_Q ≥ H-(λ_P+λ_Q)α`.

## 3. Full-history scope and exact primal attainability

For each ordered prefix `w` with count state `s`, `Q(w)=r_s P(w)`. A history-dependent stopping/randomization survival factor multiplies both prefix masses equally. Conditional on survival to `s`, the two conditional distributions on the original ordered histories are identical. Therefore replacing an arbitrary full-history action by its conditional action law at `s` preserves all four quantities `(e_P,e_Q,t_P,t_Q)`; this is an **exact finite-IID sufficient-statistic theorem for this declared observer and stopping horizon**. It does not license a quotient of P000 X6 residual or provenance states.

A state is visited at most once (strictly increasing `n`), so the full set of Markov randomized Bellman-optimal policies is the convex hull of the `2^13=8192` deterministic tie-action tables, with choices in lexicographic tie-state order (least-significant mask bit first). The independent exact integer suffix DP and **full unmerged ordered-history DFS** agree for all 8,192 tables on the four integer numerators `24^14(e_P,e_Q,t_P,t_Q)`. The unmerged traversal visits 1,236,992 ordered-prefix nodes in total. At every corner `t_P>t_Q` and `t_P+λ_P e_P+λ_Q e_Q=H`.

Let `D=24^14`, `X=D(e_P-e_Q)` and `Y=D e_P`. The 8,192 corners produce 8,186 distinct integer `(X,Y)` points; their exact planar convex hull has five vertices. Two **global supporting edges** of that polygon, verified against every corner with integer determinants, are:

- lower edge A=`(-2591590131664158720,6742099893273231360)` to B=`(3205984270082375680,9226774636878888960)`;
- upper edge C=`(-2972925671028817920,6586558925383925760)` to D=`(3250719450805043200,9253835406169866240)`.

For any corner `(X,Y)` and ordered points `u=(x1,y1),v=(x2,y2)` define

`M_uv(X,Y)=(Y-y1)(x2-x1)-(y2-y1)(X-x1)`.

The code checks `M_AB≥0` and `M_CD≤0` for **all 8,192 exact corners**, hence for their convex hull. Their intersections with `X=0` give precisely the full interval of balanced-error values `e_P=e_Q=α` within this dual-optimal face:

- lower (`α242`) mixture of mask `5` and `8191`, weights `152873242859/276449890220` and `123576647361/276449890220`;
- upper (`α243`) mixture of mask `0` and `8187`, weights `620025530015/1187066101424` and `567040571409/1187066101424`.

The two endpoint mixtures satisfy `e_P=e_Q=α`, `t_P>t_Q` and `t_P=H-(λ_P+λ_Q)α` **exactly**. Mixing the endpoint randomized rules at the root with an arbitrary real coefficient covers every `α∈[α242,α243]`, including irrational `α`, and attains the universal dual lower bound. This completes the theorem. The two support inequalities also make this the complete balanced-error equality interval for this particular dual face; this is not a claim of maximality for the entire future minimax function.

## 4. Evidence and source boundary

`stage243_exact_analysis.py` is the actual executed standard-library-only Python source. It performs exact Bellman DP, 8,192 corner integer suffix DPs, 8,192 **unmerged** integer-weight DFS traversals, exact two-dimensional hull/support calculations, endpoint mixtures, and an additional independent forward-mass check at four boundary masks. Output ended with `STAGE243_EXACT_AUTHOR_PASS 8192`. The exact machine-readable certificate `CERT_STAGE243_EXACT.json` records all critical rational results. Discovery used a temporary numerical occupancy LP to locate a candidate; **all published theorem equalities and inequalities are recalculated with integer arithmetic / `Fraction`**, not floats.

Source snapshot for this author run: GLOBAL_KNOWLEDGE_V1 `main@858c07fc2fb6cb0294ec36eb1696506d70d3c7d7`; Enterprise Math `main@194319dde91018e04f609a3f81cd3dbfb22cdad6`, including applicable P000 V5, ACTIVE worldview, BRC provenance and portable research protocol. The native gateway reported `research_authority_granted=false`, and bounded owner lookup failed `CONTROL_QUOTA` for this run. Thus this GitHub author evidence does not imply a Source CLAIM, Source Result, independent Driver acceptance, or an X6 physical bridge.

**BRC method boundary:** `PN/QN` are exact positive integer branch masses, full history retains branch order/provenance for independent verification, and the sufficiency projection to counts is proved *for the declared four expectations and 14-step IID future operations*. No native typed BRC operator is claimed to have run. This meets the BRC observer gate at the auxiliary-model level (`REUSE_APPLIED`, not a native BRC execution).

## 5. Next unresolved problem

Stage244: identify the first genuine nonzero-width supporting face **strictly right of α243**, reconstruct exact multipliers from independent Bellman tie equations, enumerate or certify its optimal corner balanced slice, and prove the next all-real minimax segment or a rational obstruction. Approximate dual search is discovery only. Preserve Stage243 and earlier exact results without recomputation solely for bookkeeping; native mathematical admission and X6 lifting remain separate obligations.
