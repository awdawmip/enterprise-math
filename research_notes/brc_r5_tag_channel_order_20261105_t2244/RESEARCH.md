# R5 — Finite-tag channel data processing, concavity, and universal sufficiency

Date: 2026-11-05 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Frontier and frozen inputs

Mother question R5: In a strictly positive finite P/Q stopping BRC, can FULL_HIST and seedless LR have equal **complete four-dimensional observation convex hulls** but different actual real-behavior observation sets? The present paper analyzes a globally valid **single-gate finite-history Bellman reduction at a fixed four-observer support direction**; full P/Q tree and all support directions remain the separate mother question.

Frozen GLOBAL scientific pin: `a01383f825ef9d43b4b754254303298c64041568`. Frozen EM scientific pin: `86149263e38c22292c9def1e0f69092efa1be77e`. Immediate immutable predecessor: `126745428ba15d75358743e88952144389dc06a6`, `research_notes/brc_r5_tag_mincut_20261105_t2145/RESEARCH.md`. The current normative control snapshot is separate from these scientific inputs. P000 and ACTIVE worldview are used as fixed in-scope premises, not altered.

## Carrier, observer, and hypotheses

Fix finite histories `I={1,...,m}`, strictly positive weights `w_i`, rational or real coefficients `A_i,u_i`, and finite tag alphabet `Y`. A row-stochastic channel `T_{iy}=Pr(y|i)` (nonnegative) describes a tag whose conditional law is the same under P and Q so no extra likelihood-ratio observation is leaked. Independently chosen upstream continuation probabilities `a_i in [0,1]` precede the tag. The downstream observer sees only the tag, selects `z_y in [0,1]`, and hence implements `t_i=sum_y T_{iy}z_y`. Assume all other stop/declaration options have already been incorporated in a **globally valid** Bellman reduction

`J=C+sum_i w_i a_i(A_i+u_i t_i)`.

The FULL_HIST observer may choose `z_i` independently instead. Set `[x]_+=max(x,0)`, `M_i=max(0,A_i,A_i+u_i)` and

`F=sum_i w_i M_i`,
`H(T)=max_{S subseteq Y} sum_i w_i[A_i+u_i T_i(S)]_+`,
`D(T)=F-H(T)`, `T_i(S)=sum_{y in S}T_{iy}`.

The predecessor proves that `D(T)` is precisely the FULL_HIST–TAG support-function gap at the fixed direction (the common constant `C` cancels) and equals a directed minimum cut. We reuse that exact equation, not a new graph construction.

## Theorem 1 — Blackwell data processing

For any stochastic postprocessing kernel `K:Y -> Z`, define `T'=TK`. Then

`0 <= D(T) <= D(TK)`.

**Proof.** Every downstream `Z`-decision `z'` induces a legal `Y`-decision `z_y=sum_z K_{yz}z'_z` in `[0,1]`; it gives exactly the same effective `t_i`. Therefore `H(TK)<=H(T)`. The fully informed optimum `F` is independent of the channel. The tagged feasible set is a subset of the FULL_HIST feasible set, so `H(T)<=F`. QED.

This is a data-processing statement for the declared *restricted Bellman decision class*, not a global comparison of all experiments or a new general Blackwell theorem.

## Theorem 2 — Concavity under unobserved mixing

For row-stochastic `T_0,T_1` on the same histories and tag alphabet and `lambda in [0,1]`, let `T_lambda=lambda*T_0+(1-lambda)*T_1`. Then

`D(T_lambda) >= lambda D(T_0) + (1-lambda)D(T_1)`.

Furthermore `D(T)` is continuous piecewise-linear and concave on the product of channel simplices. Every nonempty compact channel polytope contains a vertex minimizing `D` over that polytope.

**Proof.** For fixed binary decision `z_y in {0,1}` each summand `w_i[A_i+u_i(Tz)_i]_+` is convex as a function of the matrix entries of `T`. The maximum over the finite set of decisions `z` remains convex. Thus `H(T)` is convex, continuous and piecewise-linear, and `D=F-H` is concave, continuous and piecewise-linear. Any point in a polytope is a convex combination of its vertices; concavity makes at least one participating vertex no worse for minimizing `D`. QED.

**Strict example.** Two histories, `w=(1,1)`, `A=(1,-1)`, `u=(-2,2)`, `T_0=[[1,0],[0,1]]`, `T_1=[[0,1],[1,0]]`. Each channel perfectly reveals the history and gives `F=H=2`, `D=0`. Their equally weighted **unobserved** mixture has identical rows `(1/2,1/2)` and yields `H=1`, `D=1`. These are conditional Bellman inputs; no claim of a new strictly positive complete P/Q tree is made for this illustrative channel with deterministic endpoints.

## Theorem 3 — Exact total-variation stability

For two channels `T,R` with the same input and tag alphabets and fixed coefficients,

`|D(T)-D(R)| <= sum_i w_i |u_i| TV(T_i,R_i)`,

where `TV(p,q)=1/2 sum_y|p_y-q_y|`. If coefficients and channels are rational, the bound is exactly rational.

**Proof.** For any decision `0<=z_y<=1`, total variation gives `|sum_y(T_{iy}-R_{iy})z_y|<=TV(T_i,R_i)`. The function `[x]_+` is 1-Lipschitz. Thus the objective value of the *same* decision differs by at most the claimed right-hand side. Taking maxima in either direction preserves the bound. `F` is fixed, so the same bound holds for `D`. QED.

## Theorem 4 — Universal one-gate sufficiency criterion

Fix `m` positive history weights and a finite channel `T`. The property `D(T)=0` **for every possible choice of real Bellman coefficients** `A_i,u_i` is equivalent to pairwise disjoint row supports: for all distinct `i,j` and all `y`, `T_{iy}T_{jy}=0`.

**Proof.** If the supports are disjoint, choose `z_y` according to the individually optimal downstream decision of its unique source history; then the tag exactly implements every history-conditioned action, so `D=0`. Conversely, let `i,j` share a positive-probability tag output. Choose all other histories inactive (`A_k=-1,u_k=0`); for the selected histories use `A_i=1,u_i=-2` (strict preference for downstream stop) and `A_j=-1,u_j=2` (strict preference for continue). FULL realizes `w_i+w_j`. Equality for TAG would require simultaneously `T_i z=0` and `T_j z=1`; their shared tag forbids this. Compactness of the finite decision cube makes the optimum strictly lower. Hence `D(T)>0` for this coefficient choice. QED.

The universal coefficient quantifier matters: for one fixed four-observer direction a channel with overlapping rows may still have zero loss because preferences are aligned.

## Exact computation and scope

`VERIFY.py` uses `fractions.Fraction` and enumerates all binary tag rules in each finite example. It verifies the strict unobserved-mixing example, a nontrivial garbling `K=((3/4,1/4),(1/4,3/4))` with exact `D=1`, and 300 deterministic-seed rational samples of concavity, data processing and the total-variation bound (2–5 histories, 2–5 input tags, 2–4 output tags). Exact run output: `EXACT_OUTPUT.txt`.

For all finite tag channels, Theorems 1–4 are algebraic statements proved above. The 300 samples verify the implementation and selected examples, not the universal quantifiers. No formal Lean check or independent Driver review is claimed.

## BRC reuse and next discrimination

`REUSE_APPLIED`: positive weighted branch carrier; source-labelled histories as provenance; tag channel as an observer quotient; support-function / exact min-cut interface from the immutable predecessor. The new law quantifies how observation noise, random channel choice and subsequent information loss alter that quotient. Algorithmic arithmetic cost of exact subset enumeration in `VERIFY.py` is exponential in |Y|; the predecessor's min-cut algorithm can evaluate an already-derived direction polynomially in finite graph size. Exact rational bit complexity and construction of the global four-dimensional Bellman partition are separate costs.

Next: build a **fully specified strictly positive P/Q nonterminal merger** with a certified four-dimensional Bellman sign-cone decomposition. Test Blackwell garblings and zero-loss row-support patterns cone-by-cone, including boundaries, with the predecessor's exact min-cut evaluation. Then independently evaluate actual behavior-image convexity, the remaining R5 criterion.
