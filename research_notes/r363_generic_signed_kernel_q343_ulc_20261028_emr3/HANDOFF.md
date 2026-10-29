# R363 Portable Handoff — author-side signed BRC research

Global knowledge frozen `main@9e4f20918edc20e0c038133379525bd2470c37a4`; EM normative source `main@aab9bee8c8338a4d83f6ed20bc4098fd35da1a50`. This PR branch is a **durable author-side research artifact**, not a canonical native Task Result or independent Driver review. P000 / ACTIVE worldview unchanged.

## Completed, do not replay as new

1. New general signed-kernel diagonal extraction theorem: when K(x,0)=2x, A(x,0)=1, deg_x K_a≤a+1, deg_x A_a≤a and c=K_1(1/2)≠0, then D(r+u,u)=(4c)^u H_r(u), deg H_r≤r. Full proof in R363_PROOF.zh-CN.md; 84 exact example checks, support-degree counterexample.
2. Q343 signed original K/J: 687/687 positive Newton coefficients, 685/685 strict ordinary Turán, Q342 regression, 8 direct minors; 687 integer rows SHA256 `019e7f8866384a1e5beed7ed05f69a77c784333932057106c3dd4a20dca90899`. R363_reproduce.py regenerates raw full rows.
3. R337..343 exact ULC finite shape: 4753 internal tests, 4358 failed and 395 passed, no equality; every r exactly one negative-to-positive change. Q343: j≤628 fail; j≥629 pass. R363_ulc_scan.py and R363_ULC_TRANSITIONS.csv reproduce.

## Next unsolved mathematical unit

Prove or refute globally the one-transition ULC sign shape, retaining signed provenance, then seek uniform all-(r,j) ordinary strict Turán/PF₂. Independently review the R348(A1-A5) / generalized degree-support and boundary proof; shared author checking is not independent acceptance.

## Reproduction and boundaries

`python R363_reproduce.py && python R363_ulc_scan.py && python R363_generic_theorem_check.py`, with existing `research_notes/r346_unbounded_interior_tp2_corank301_20261028_emr3/R346_verify.py` in same PR branch. All sign checks exact integer/Fraction. Native service read-only; live owner CONTROL_QUOTA; no original CLAIM/Source Result/Driver admission. No X6 physical transfer or full 2D TP₂ theorem. Full 687-line raw integer dataset, actual locally executed source, logs and SHA256 manifest also available as R363 downloadable research ZIP from this conversation.