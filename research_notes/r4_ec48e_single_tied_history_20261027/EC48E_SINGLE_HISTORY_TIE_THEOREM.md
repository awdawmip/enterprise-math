# EC48E — Generic-position equality of seedless and convex-hull BRC memory capacity

**Status:** Author-side complete algebraic proof; exact finite verification performed. Not a native Result, independent Driver review, Working Truth, Foundation theorem, or native Heartbeat/X6 physics.

**2026-10-27.** Source snapshot: GLOBAL_KNOWLEDGE_V1 `main@8ec98188025f60aafe48055520ba3a57c29cdb2c`; Enterprise Math control `main@5ea059eb5d9c5bbe726cdbed71d14a467f737f09`. P000 V4 read and P000_STARTUP canonical blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc` checked; ACTIVE worldview and current portable research protocol read. Reuses [EC48D](https://github.com/awdawmip/enterprise-math/blob/6b320868bc664072b722ed32bfa0dc87660c68a6/research_notes/r4_ec48d_two_bank_20261027/EC48D_TWO_BANK_THEOREM.md), including its bound `K_hull <= K_seed <= 2*K_hull`, and [EC48C](https://github.com/awdawmip/enterprise-math/blob/d582d2bd1487446008648fe9da1fae63d2c86b9c/research_notes/r4_ec48c_encoder_quotient_20261027/EC48C_ENCODER_QUOTIENT_THEOREM.md). Existing typed positive-weight BRC provenance retained, no signed/phase or physical transfer.

## Model

Fix nonempty finite alphabets `H` (source histories) and `Y` (future visible labels), strictly positive separately normalized joint laws `p(h,y),q(h,y)`, and `K>=1` private memory labels. An encoder `pi_h(m)` is a probability vector depending only on `h`; a decoder `u_m(y) in [0,1]` gives the terminal probability of declaring hypothesis P after seeing memory `m` and future label `y`. No persistent shared random seed is available. Thus

```text
w(h,y)  = sum_m pi_h(m)*u_m(y),
alpha   = sum_(h,y) p(h,y)*w(h,y),
beta    = sum_(h,y) q(h,y)*w(h,y).
```

Let `S_K` be the attainable (`alpha,beta`) pairs and let the full-history observation zonotope be
`Z = sum_(h,y) [0,(p(h,y),q(h,y))]`.
Define `K_seed=min{K:S_K=Z}`, `K_hull=min{K:conv(S_K)=Z}`. The four-coordinate readout here is exactly `(1-alpha,beta,2,2)`; both decision times are constant. Variable stopping depth and native X6 dynamics are outside scope.

Let `r(h,y)=p(h,y)/q(h,y)`, and for each ratio `r` let `H_r={h: some y has r(h,y)=r}`.

### Theorem EC48E.1 — One tied history at every breakpoint is sufficient

**If `|H_r|<=1` for every distinct likelihood ratio `r`, then**

```text
              K_seed = K_hull.
```

For each exposed support edge of `Z`, the entire edge can be realized by a *K_hull*-memory conditional encoder and a decoder, without a persistent random seed. Repeated equal ratios *within the same history* are allowed; all probabilities may be real and strictly positive. The finite checker uses rational data.

### Proof

**Lemma 1 (generic sign-profile vertex count).** At a positive support threshold `lambda` distinct from every `r(h,y)`, the unique cellwise maximizing decision for `alpha-lambda*beta` is
`v_lambda(h,y)=1{p(h,y)>lambda*q(h,y)}`.
Its (`alpha,beta`) vertex can be attained by K-memory seedless observers if and only if at most K distinct row words `v_lambda(h,-)` occur.

For sufficiency allocate one decoder memory row per distinct word and deterministically encode its history. For necessity, the strict support inequalities force `w(h,y)` to be precisely 0 or 1 at every cell. Since `w(h,y)` is a convex mixture of decoder entries in [0,1], every decoder row with positive encoder weight for a history must equal *all* bits of that history's row word. Distinct row words therefore need distinct memory labels. The vertices of the positive-generator zonotope `Z` arise from these sorted likelihood-ratio breakpoints, together with all-0 and all-1 endpoints. Therefore

```text
K_hull = max_(lambda>0, lambda not a ratio)
             number of distinct words (1{r(h,y)>lambda})_(y in Y).
```

The same conclusion follows from every zonotope vertex being reachable iff its convex hull is `Z`, using compactness of each `S_K`.

**Lemma 2 (critical edge with one tied history).** Fix a ratio `r` and its unique history `h0`. For all other histories, every cell is strict. Let `C` be the set of their forced binary row words `c_h(y)=1{r(h,y)>r}`. Define the two words of `h0` by `a(y)=1{r(h0,y)>=r}` and `b(y)=1{r(h0,y)>r}`. Both words agree on strict cells; they differ only at tied future labels. The sets `C union {a}` and `C union {b}` are exactly the generic sign words immediately below and above `r`; hence each has at most `K=K_hull` elements by Lemma 1.

Fix any `s in [0,1]`. We construct a genuinely seedless factorization with at most K memory labels whose declaration probabilities agree with every strict sign and equal `s` at *every* tied cell of `h0`.

* If **both** `a,b` belong to `C`, assign decoder rows to the words in `C`. Encode all other histories deterministically to their words, but for `h0` put private encoder weight `s` on word `a` and `1-s` on word `b`. It uses `|C|<=K` rows.
* Otherwise, at least one of `a,b` lies outside `C`. The corresponding generic side gives `|C|+1<=K`. Assign `|C|` fixed decoder rows to `C` and **one additional decoder row** `d_s(y)=s*a(y)+(1-s)*b(y)`. Encode every other history to its fixed row and `h0` deterministically to the dedicated row. It uses `|C|+1<=K` rows. This row may vary with the target point `s`; that is allowed because each point of `S_K` has its own control strategy, without a persistent seed.

In both cases, each cell with `p-rq>0` has declaration probability 1 and each cell with `p-rq<0` has probability 0. All tied cells have probability `s`. Let `Q_r=sum_{(h,y):p=r*q} q(h,y)>0`. Then

```text
alpha-r*beta = sum_(h,y) max(p(h,y)-r*q(h,y),0);
sum_(p=r*q) q(h,y)*w(h,y) = s*Q_r.
```

As s ranges over [0,1], this is the *entire* exposed support edge of Z, since the tied generators have common slope r. QED Lemma 2.

**Complete-region step.** Applying Lemma 2 at every positive ratio r covers all nontrivial exposed edges of Z with normals (1,-r). Decoder complementation `u -> 1-u` maps (`alpha,beta`) to (`1-alpha,1-beta`), covering the opposite edges. The remaining extremal endpoints are obtained from all-0/all-1 decoders. Furthermore `S_K` is star-shaped about (0,0): scaling every decoder entry by `t in [0,1]` scales both coordinates by t while respecting the same K memory labels. Every point of the convex body Z lies on a segment from 0 to its boundary. Thus `Z subseteq S_K`; the reverse inclusion is automatic, proving `S_K=Z` for `K=K_hull`. Since `K_hull<=K_seed`, equality follows. **QED.**

### Corollary EC48E.2 — A necessary algebraic obstruction to a counterexample

If `K_seed>K_hull` for a finite strictly positive two-stage BRC model, there must be **two distinct histories** `h!=k` and future labels `y,z` satisfying

```text
p(h,y)*q(k,z) - p(k,z)*q(h,y) = 0.
```

This cross-history equality is necessary but **not sufficient** for separation.

### Corollary EC48E.3 — Generic equality

In the relative interior of the product of the two probability simplexes, the finite union of cross-history collision equations above is a proper algebraic exceptional set of Lebesgue measure zero. Each individual equation is a nonzero polynomial (for example, take q uniform and choose unequal p-coordinates). Thus `K_seed=K_hull` on an open dense, full-measure subset of positive parameter space. This is a measure-theoretic/generic statement, not a resolution on the exceptional set and not an assumption that physical data are random.

## Executed exact check, provenance and limitations

The accompanying `EC48E_VERIFY.py` executes a deterministic Python `fractions.Fraction` check of the **actual decoder-bank and conditional-encoder factorizations** at all critical likelihood ratios for 357 cross-history-collision-free positive raw integer models (including one purpose-built model with repeated ratios within histories). This covered 3,795 support faces, 18,975 exact support/tie-mass checks at s=0,1/7,1/2,6/7,1, including 410 encoder-mixing and 3,385 dedicated-row constructions, all PASS. 94 other random models contained cross-history collisions and were **excluded by the stated theorem hypothesis**. The generated total was 450 plus one explicit model. No native BRC runtime, X6 trajectory, floating computation, or independent Driver review was executed.

The proof, rather than the finite tests, establishes the all-finite-alphabet theorem. Reuse classification: `REUSE_APPLIED` to EC48A sign-profile support law, EC48C support-face geometry and EC48D positive BRC typed decoder model; `EXTEND_EXISTING_TOOL` for an exact narrow rational verifier, not a new foundational BRC primitive.

**Current authority:** GitHub login `awdawmip` verified with project push permission. The native task/owner read returned `CONTROL_QUOTA`; direct native session start returned `STATIC_READONLY_SCOPE_DENIED` and `operation_sent=false`. This author-side activity has no canonical TASK CLAIM or review status. Do not interpret a source-branch theorem as accepted Foundation.

## Next EC48F

The unresolved general implication `conv(S_K)=Z => S_K=Z` is reduced to the algebraic locus with at least one exact **cross-history tied likelihood ratio**. Build structured collisions deliberately rather than generic random weights; first test a single cross-history tied pair and identify the smallest number of independently tied histories needed for disconnected support-face intervals. For any claimed counterexample, provide exact raw integer P,Q matrices, K, r, EC48C encoder graph components and an explicitly missing *rational* open interval. If the collision-free equality extends to one tied pair, prove an explicit reconfiguration lemma. Keep variable-depth 4-observer and native X6 questions separate.
