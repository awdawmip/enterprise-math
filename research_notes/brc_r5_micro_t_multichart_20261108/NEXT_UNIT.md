# R5 next unit — scale-uniform small-t positive-residual bridge

Date 2026-11-08; frozen science pins Global a01383f825ef9d43b4b754254303298c64041568, EM 86149263e38c22292c9def1e0f69092efa1be77e.

This research branch proves, with 64 exact rational vertex certificates and a 1004-case Fraction regression, seedless equivalence on four slabs covering every real t in [10^-6,369/43076], p,q in [0,1], theta in [3/4,1], kappa=3/4. The chart ratio changes with each slab, avoiding the known sharp *fixed* C_(4/5) separator. PR #1804 provides [369/43076,1/5] with theta≥3/4, and PR #1803 provides theta≤3/4 for all t∈[0,1/5]. Therefore the current author-side union covers p,q,theta in [0,1] for t in [10^-6,1/5] at kappa=3/4. At t=0 the source is itself seedless.

Smallest unfinished scientific unit: **0<t<10^-6**, theta>3/4 at fixed kappa=3/4. Evidence is author-proved and unreviewed, not a formally accepted Result.

Suggested symbolic research: For each 0<epsilon<=10^-5 set tau=3/4+epsilon/4 and t in [epsilon/10,epsilon]. Use the 16 existing sparse vertex supports in VERIFY.py as initial rational templates. Parameterize the 23 calibrated equalities and solve their support-constrained rational linear systems over Q(epsilon); determine an exact positivity range for every resulting rational edge and target physical slack. Proving this for all real epsilon would cover the remaining interval by scaled slabs, not merely finite tests. Then investigate varying kappa away from 3/4 without dropping the likelihood-weighted joint-observer constraints.

Identity for this evidence: Researcher-ID EM-DIRECT-7CD960; RA-20FC5EC4B18E1949386AF83E; GitHub awdawmip. Native Task CLAIM/Owner and independent mathematical admission not confirmed. Verification: python3 VERIFY.py, check saved EXACT_OUTPUT.txt.
