# R5: a single parameter-independent support functional rules out the entire two-parameter I/J/K/L bypass family

**Date:** 2026-11-01 (Asia/Shanghai). **Evidence grade:** `AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING`.

## 1. Precise target and provenance

The R5 four-observer mother question asks for a strictly-positive finite two-law stopping experiment in which the convex hulls of the FULL-history and seedless LR-policy observation sets coincide, yet their **actual** real behavioral images differ. This paper completes the **negative classification of the specific two-parameter `I/J/K/L` bypass family** introduced in the predecessor; the mother question remains open outside this family.

- **Frozen science inputs, unchanged from the R5 lineage:** GLOBAL_KNOWLEDGE_V1 `main@a01383f825ef9d43b4b754254303298c64041568`, Enterprise Math `main@86149263e38c22292c9def1e0f69092efa1be77e`. This study uses the immediately preceding immutable author-side source `c1b418ef1b483ce6ee22d8fd3203aa2416769b13`, `research_notes/brc_r5_two_parameter_joint_gap_cancel_20261101_t2148/{RESEARCH.md,VERIFY.py}`.
- **Current normative snapshot separately verified in this run:** Global Knowledge `main@83c851a7e8a405aad52cee9fd5d779fbce317ba2`; Enterprise Math `main@8c21590456c07ad03baa2a1573cd8feffa186cb1`. The current project P000 startup projection's `canonical_blob_sha1=770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc` matches the actual full P000 original blob read at the global snapshot. ACTIVE `我眼中的世界.md`, current math/code/semantic policies, `docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context`, `docs/PORTABLE_RESEARCH_PROTOCOL.md`, and task/control entry were consulted. P000 and the protected worldview were not edited.
- **Scope/type:** a classical auxiliary positive-flow double-probability measure model. The four observations are not X6 native spatial coordinates. The source labels A1/A2/B/C and P/Q natural masses are retained until observation; signed coefficients appear only in linear separating functionals. No unproved native X6 embedding or physical statement is inferred.

## 2. Model and admissible range

The exact source-labelled flow is in `VERIFY.py`, derived from the preceding pinned verifier. Initial P/Q masses: A1=A2=(1/8,1/8), B=(1/4,1/8), C=(1/2,5/8). The four outputs are

`O = (eP,eQ,TP,TQ) = (Pr_P(final answer P),Pr_Q(final answer Q),E_P(stop time),E_Q(stop time))`.

A FULL strategy has 11 local real behavior parameters `(p1,p2,q1,q2,qB,r,k1,k2,l1,l2,lB)`; an LR strategy ties `p1=p2=p`, `q1=q2=qB=q`, `k1=k2=k`, `l1=l2=lB=l`, with `r` free. The shared genuine time/LR keys are `I=(1,1), J=(2,2), K=(3,8/5), L=(4,12/5)`. Each behavioral key appears at most once on a path. The strictly-positive parameter range is

`0 < η < 5/6, 0 < z < 1`.

From B at J, the continuing branch splits with `(P,Q)` probabilities `(6η/5,η)` toward L; its complement terminates at time 4 with common conditional answer Q-probability `z` and answer P-probability `1−z`. All other source branches are unchanged from the cited predecessor. The code checks each law's complete terminal probability mass equals exactly 1.

## 3. Uniform, exact all-real theorem

**Theorem.** For every admissible real pair `(η,z)` and every legal real behavioral policy, consider the **parameter-independent** signed functional

`M(O)=−211 eP + 10 eQ −113 TP`  (coefficient vector `m=(−211,10,−113,0)`).

Its support values over the two policy classes are **exactly**

`max_{FULL} M(O) = −238`,

`max_{LR} M(O) = −481/2`.

Consequently, the FULL/LR signed support gap equals **5/2** at every real parameter point in the entire strictly-positive two-dimensional family. A single FULL deterministic witness

`Wbits = (0,0,0,0,1,1,0,0,0,0,0)`

has the invariant observation

`W=(11/40,55/64,267/160,187/128)`,

so `M(W)=−238`. The LR deterministic policy `(p,q,r,k,l)=(0,1,1,0,0)` achieves `M=−481/2`, independently of `(η,z)`.

Therefore `conv O(FULL) != conv O(LR)` for **all** admissible real `(η,z)`, and the witness satisfies the explicit uniform quantitative lower bound

`dist_∞(W,conv O(LR)) >= (5/2)/(211+10+113) = 5/668`.

An additional simpler direction `m_short=(−5,1,−3,0)` independently has exact FULL maximum `−1767/320`, LR maximum `−89/16`, and gap `13/320` for the entire parameter domain; its witness distance bound is `13/2880`.

### Proof: no finite-grid inference

For a fixed **deterministic** FULL or LR policy, each terminal branch uses at most one B-high/low occurrence of `η` and then at most one B-low answer split `z`. Its terminal observer is therefore polynomial **bilinear** in nature parameters: `a+bη+cz+dηz`. Other sources do not depend on either parameter. On the closed algebraic rectangle `[0,5/6]×[0,1]`, each scalar observer is exactly the bilinear convex interpolation of its four corner values, with normalized interpolation parameters `u=6η/5`, `v=z` and weights `(1−u)(1−v)`, `(1−u)v`, `u(1−v)`, `uv`. The corners here are **polynomial verification points**, not assertions of strictly-positive natural edges at the boundary.

`VERIFY.py` enumerates all `2^11=2048` deterministic FULL policies and `2^5=32` deterministic LR policies at each of the four nature corners, computing complete P/Q rational terminal flows. It proves by exact Fraction arithmetic that, at **each** corner,

`max_FULL M = −238`, `max_LR M = −481/2`,

and for the short direction

`max_FULL M_short = −1767/320`, `max_LR M_short = −89/16`.

It verifies the same fixed Wbits and LR maximizing bits at every corner. Because all scalar objective values for each fixed deterministic policy are bilinear in `(η,z)`, the four-corner bounds extend to the whole real parameter rectangle by the nonnegative interpolation weights. Since the two stated deterministic witnesses attain their respective bounds for every parameter, these are **equalities**, not merely robust inequalities.

Finally, each trajectory visits any behavioral decision key at most once. Its output is separately affine in every one of the 11 FULL (respectively 5 LR) policy coordinates. Every real behavioral observation is therefore an explicit convex combination of deterministic observations, with nonnegative Bernoulli product weights. A linear functional has the same maximum over the whole real behavioral cube as over deterministic vertices. The exact two support equations follow for **all** real behavioral strategies, not just sampled policies. A separating signed functional remains valid on convex hulls. Hölder duality `|m·(W−V)| <= ||m||_1 ||W−V||_∞` gives the stated uniform distance bound for every `V in conv LR`. QED.

## 4. Scientific meaning and what changed

The predecessor constructed a nonempty strict-positive rectangle where two earlier independently signed support gaps H/J both vanished, then found an N-direction gap over that rectangle. The present global result supersedes **the restricted-rectangle necessity**: one unchanging functional M separates the full model across **the entire** open parameter box, including where H and J both vanish, and without needing a phase diagram or a tailored N for each parameter.

The uniform witness stops source B before its η/z-dependent continuation; its provenance-sensitive decision at J differs from the LR-shared action used by source A. The exact support calculation isolates an upstream source-coupling obstruction that the two B-tail parameters cannot repair in this fixed topology. This is an all-real finite auxiliary-model result, not a blanket impossibility for new topologies that modify upstream couplings or observations.

## 5. Verification, provenance and admission

The self-contained `VERIFY.py` uses only Python standard-library `fractions.Fraction` and `itertools.product`. Its actual `EXACT_OUTPUT.txt` records four exact maxima comparisons, **8,320** complete deterministic policy/parameter-corner observer calculations, P/Q mass normalization, and regression to the predecessor's nontrivial witness at `(η,z)=(1/2,3/4)`. Final validation token: `PASS_EXACT_R5_GLOBAL_TWO_PARAMETER_UNIFORM_SIGNED_SUPPORT_NO_GO`. The proof's only non-finite steps are explicit bilinear and behavioral multi-affine interpolation.

Native `em_status` returned `research_authority_granted=false`, `executor_binding_configured=false`, active quota `5/5`, `UPSTREAM_CODE_REVIEW_REQUIRED`; bounded active-owner query returned `CONTROL_QUOTA`. Accordingly, this note is **author-side preserved science** rather than a native CLAIM, Result, independent Driver review, admission or foundation promotion. A GitHub commit/PR receipt establishes storage, not independent mathematical acceptance.

## 6. Exact next unit

Treat this entire η/z two-parameter family as mathematically excluded. Preserve the upstream support certificate as a **cheap candidate-pruning tool**, then change an earlier source-sensitive J/I transition or add a genuinely independent bypass whose behavior changes the M-optimal decision tradeoff. For a new strictly-positive candidate, evaluate the single M direction first; if its gap vanishes, perform the complete all-signed FOUR-observer convex-hull test (exact rational mixtures of at most five LR deterministic vertices per FULL vertex, or Farkas separators). Only on full hull equality, test actual real LR image membership by a certified semialgebraic argument. Maintain source-positive branch provenance and frozen P000 semantics.
