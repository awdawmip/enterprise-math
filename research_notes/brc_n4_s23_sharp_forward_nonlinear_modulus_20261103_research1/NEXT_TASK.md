# Next executable scientific unit

The full three-view bank (baseline plus the two overwrite masks) has a **sharp all-scale forward modulus** `omega(eps)=1-(1-eps)^3` for every mask/constant choice. Its global sharp Lipschitz constant is 3. This exactly resolves the forward-Lipschitz question in the predecessor's `NEXT_TASK.md`; do not repeat its generic union-bound search.

**First discriminating continuation:** Remove the baseline view and compute the forward modulus for the overwrite-only pair, first for masks (3,31) with beta_N,beta_E in {0,1/2,1}. The baseline extremizer will no longer necessarily survive; derive candidate exact extremizers and an all-real piecewise bound by branching/coupling or finite multi-affine extremal certificates. Compare whether mask pairs still share the same constant.

**Alternative independent continuation:** For the full bank, combine this exact forward modulus with the previously proved sharp inverse coefficient `sigma=min(a,b^2/21)` or `min(a^2,b^2/21)`, and compare with single multiplicative attenuation, declaring noise semantics (adversarial TV budget per row versus independently sampled multinomial draws), number of observed labeled rows, time/operation cost, and sample allocation. Find an explicit budget region where one observation design dominates in a specified criterion.

Mother objective: preserve complete six-source causal state while minimizing observation and stable reconstruction effort. Keep frozen scientific pin `43ec6098b1330ae86d0a7863be336c5d97f6ef34`, original labels, four outcomes, and P000/ACTIVE worldview. Status: author analytic proof, exact rational test, pending independent review and native admission. No new CLAIM/Result is inferred from GitHub delivery.
