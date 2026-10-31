# R5 17:40 — Time-only separator closes all terminal-error perturbations

**2026-10-31 / author-proved, exact-Fraction checked / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.** The FULL/seedless-LR study here concerns an auxiliary finite P/Q stopping process, not an accepted native X6 theorem.

## Full analytic result

Use the strict-positive two-hidden-origin P/Q stopping process from immutable source `e7916482f44a925e11ece98e406309f4655fb1f1`. At A (t=1, LR=1), STOP t1 or CONTINUE into stage-2 D,C,Y with Q conditional probabilities `(α_i,1−2α_i,α_i)` and LR `(1/2,1,3/2)`, with `0<α_i<1/2`. C is forced STOP t2. D STOP t2 or CONTINUE to t3: Q split 2/3 to residual LR 1/4 and 1/3 to common L LR1. Y STOP t2 or CONTINUE to t3: Q split 1/2 to residual LR2 and 1/2 to L LR1. At L STOP t3 or CONTINUE t4. Origins i=0,1 have Q and P prior weight 1/2 each. Transport each Q cylinder with P mass = LR × Q mass; normalization is exact. FULL decisions can use origin/path, seedless LR shares its stage/LR keys A,D,Y,L.

Allow **arbitrary admissible source/path/action-dependent terminal error probabilities at every terminal cylinder**, common to the two strategy classes, while preserving natural P/Q transition masses, action keys and terminal stopping times. Consider the four-observer `O=(error_P,error_Q,T_P,T_Q)` and the **error-independent** direction `H=13T_P−14T_Q`. For ALL real `α_0,α_1∈(0,1/2)`, define `φ(α)=max(−1,−2+11α/2)`. The exact support gap is

```text
sup_FULL H = [φ(α_0)+φ(α_1)]/2
sup_seedless_LR H = φ((α_0+α_1)/2)
Δ_H = [φ(α_0)+φ(α_1)]/2 − φ((α_0+α_1)/2) ≥ 0.
```

**Strictly positive iff** `(α_0−2/11)(α_1−2/11)<0`. This classifies *only this H observer*, not every possible four-dimensional separator. At the original `α_0=1/4, α_1=1/8`:

```text
sup_FULL H = −13/16
sup_LR H   = −31/32
Δ_H        = 5/32
min L∞ distance of a FULL witness to the entire LR hull ≥ 5/864.
```

These quantities hold for **every terminal error kernel**, including any changes at C, D, Y, A, L and both residual leaves, provided flows and times remain fixed. Therefore the full four-dimensional FULL/LR convex hulls are distinct for this entire family. Changing C-error (or any other error-only response) is now a mathematically closed search direction.

## Proof

Per unit Q probability at a terminal LR `λ`, time `t`, H contributes `r(λ,t)=(13λ−14)t`; errors cancel out of the observer. L STOP has reward −3 versus L CONTINUE −4, hence always STOP. D STOP: −15; D CONTINUE: `(2/3)(−129/4)+(1/3)(−3)=−45/2`, hence STOP. Y STOP: 11; Y CONTINUE: `(1/2)(36)+(1/2)(−3)=33/2`, hence CONTINUE. These are strict Bellman comparisons valid for both classes, all α and all terminal errors; the shared nodes create no conflicting optimal decisions.

A STOP has reward −1. A CONTINUE conditional on hidden origin i has optimum
`V_i=α_i(−15)+(1−2α_i)(−2)+α_i(33/2)=−2+11α_i/2`.
FULL chooses STOP or CONTINUE separately for i, giving mean of `φ(α_i)`; seedless LR uses one common A action, giving `φ` of the origin-average. Every key appears at most once per realized path, so each H expectation is multi-affine in real behavioral probabilities and maximum is attained by deterministic controls. Finally φ is convex and has its unique kink at `2/11`. Midpoint Jensen equality holds exactly when both α values are in one affine region (including its boundary); strict gap requires crossing the kink strictly. For the original source pair, `V_0=−5/8`, `V_1=−21/16`; FULL continues only source0, LR continues both. This gives the displayed exact supports, and the L∞ bound follows from the coefficient l1 norm `|13|+|−14|=27`. Q/P masses and stopping times are independent of terminal errors, so every asserted error-kernel quantifier follows. QED.

## Exact check, reproducible materials and limits

The downloadable **complete, nonempty evidence tarball** includes `RESEARCH.md` (expanded full proof, BRC provenance and limits), the actual executed standalone `VERIFY.py`, literal `EXACT_OUTPUT.txt`, and `NEXT_TASK.md`. The Fraction verifier enumerated **1024 FULL + 16 LR deterministic policies for each of 25 rational alpha pairs** (26,000 policy calculations), with P/Q normalization assertions, including source pair (1/4,1/8), the critical 2/11, same-side and strictly opposite-side parameters. It checked 8 strict and 17 zero-gap parameter pairs and printed `PASS_EXACT_R5_TIME_ONLY_TERMINAL_ERROR_NO_GO`. Universal all-real claim is proved by Bellman/Jensen algebra; grid tests supplement it.

Archive blob SHA-1: `945a1bf5c53a156637f8072ecf89071dc02c6bd7`. Archive SHA256: `b5212eb058fff0dd70d82953d8bff5587586d8836cf09c35f4aeb1fbee4b4bd4`.

Frozen source inputs: GLOBAL_KNOWLEDGE_V1 main@`a8ac2ca67df02b5e1050370145c00ea19607b4d4`, Enterprise Math main@`cd0d692a5510dddcc42991b056ed032933e0b164`. P000 canonical blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc` matches startup projection, ACTIVE worldview unchanged. BRC use is exact positive source/route/action path mass with LR Q→P transport and provenance-preserving time readout; no π/trigonometric/classical native model computation and no X6 transfer claim. Native service reported `research_authority_granted=false`, `executor_binding_configured=false` and owner inventory returned `CONTROL_QUOTA`: no certified owner, CLAIM, Result or independent Driver review.

## Corrected next unit

Change **natural time-flow or information coupling**, not only error kernels. Construct a minimal strictly positive source/history-preserving changed transition (e.g. a real C→L route with typed P/Q likelihood transport), first prove full **two-time-coordinate convex hull equality** or supply separation; then test all four observer coordinates with exact ≤5-vertex convex certificates or Farkas separation, full affine rank, and finally actual real seedless LR-image nonmembership. Preserve source pins, native boundary and all earlier proved results. Full continuation is included in archive `NEXT_TASK.md`.
