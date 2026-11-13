# Next R5 unit — prove or disprove homogeneous-error sufficiency under source-uniform clocks

## Frontier consumed

Use sibling RESEARCH.md, VERIFY.py, EXACT_OUTPUT.txt from the same GitHub commit and the exact two earlier predecessors:
- `research_notes/brc_r5_k3_supercritical_alpha_nu_rigidity_20261104_t0735/RESEARCH.md` @ `5895ab8bbbb528c047d7b1822bb7755311fe2295`
- `research_notes/brc_r5_k3_uniform_superdiagonal_error_fiber_20261104_t0844/RESEARCH.md` (this unit)

Science remains pinned: GLOBAL_KNOWLEDGE_V1 `a01383f825ef9d43b4b754254303298c64041568`; Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Resolve current behavioral rules separately, retain the full four-source BRC model and P000/ACTIVE worldview.

Proved here, all real `0<r<v<1`: heterogeneous p or q yields strict four-hull separation despite equal time hulls. The exact residual at source j is
`(c_j*(p_j-pbar)/12, c_j*(q_j-qbar)/48,0,0)` on the clock face `(0,0,-nu,1)`.

## Discriminating next question

For fixed `r_s=r,v_s=v,p_s=p,q_s=q` across the four sources with `0<r,v,p,q<1`, is
`conv O(FULL) = conv O(seedless LR)`
true for **every** such real parameter tuple, including `v>r` and `v=r`? If yes, construct a symbolic per-FULL-deterministic-observer LR convex representation (Caratheodory: at most five LR vertices) with nonnegative coefficients that remain valid for the full parameter domain or a rigorous finite parameter partition. If not, exhibit a rational r,v,p,q with an exact four-normal / rational Farkas strict separator and classify its mechanism.

Suggested exact test inputs: `(r,v,p,q)=(1/5,2/5,1/2,1/2)` and `(2/5,4/5,1/2,1/2)`, then `r=v=1/3`. Enumerate 1,536 FULL and 16 LR vectors using sibling VERIFY.py's `observer`. Use exact rational primal LP or a checkable Farkas dual, recording each distinct FULL observer's certificate; floating LP is only exploratory and should be followed by exact checks.

A separate question arises after any **proven** four-convex-hull equality: characterize whether the actual real behavioral observation sets coincide. This requires an image/nonmembership proof, not just a signed-support comparison.

## Acceptance and provenance

Deliver a complete theorem proof or an explicit exact counterexample and its reproducible source/outputs; state the real parameter domain, model map and deterministic reduction; preserve provenance and scientific pins. Work on this line is author-side until the canonical Service permits an authenticated research session and winning CLAIM/Result/independent Driver review. The mother four-observer problem stays open.
