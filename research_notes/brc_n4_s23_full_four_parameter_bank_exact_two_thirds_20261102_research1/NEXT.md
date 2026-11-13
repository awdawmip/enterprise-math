# Next scientific unit — F4 sharp-bank obstruction and three-kernel reoptimization

Date: 2026-11-02. Source: this directory's PROOF.md and RUN_EVIDENCE.json.

Input: original six-source BRC S23 pinned at `43ec6098b1330ae86d0a7863be336c5d97f6ef34`; former `S18\cup J([0,1])\cup F([0,1]^3)` exact radius `3/5` with seven fixed and three free kernels; new witness `W4=F4(1/3,0,1,1/2)` where the *old fixed bank* has risk `2/3`.

**Smallest open question:** Determine the sharp three-free-kernel radius for `S18\cup J([0,1])\cup F([0,1]^3)\cup\{W4\}`. Current proved bounds: `[3/5,2/3]`. Attempt direct rational kernel repair at `3/5` with an explicit common-decoder coverage certificate; otherwise derive a compact incompatible assignment/event certificate giving a strict rational lower bound. Do not confuse an old-bank counterexample with a new lower bound for arbitrary redesigned kernels.

**Following question:** Extend a successful candidate to `F4([0,1]^4)`, using a common decoder at all 16 corners of each cell; adaptive grids or analytic polytopic coverage are permitted, while exact input and shared-source relations are preserved.

Verification: exact rational risks for all six labeled source rows, complete finite witnesses for any discrete infeasibility claim, and cell-corner certificates plus multi-affinity for a continuum upper bound. Keep author construction/review/native admission separate. Document upstream source and provenance.
