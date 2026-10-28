# R368 HANDOFF — signed BRC admissible formal numerator perturbation

**Research identity:** current author-side TASK_RESEARCH, locally assigned `EMR3-20261029-R368-LOCAL`; not a backend-authenticated session or claim. `UNREVIEWED / NOT_ADMITTED`.

**Frozen sources:** GLOBAL_KNOWLEDGE_V1 `main@861bd51a4cff39295fbcdd3e04065e08d13fb296` (bootstrap, manual, ACTIVE worldview/P000 projection); Enterprise Math control `main@a949aa10bd7c0bd9e873daa08a88046843d57ae8` (P000, portable research). Research parent: R365 exact row data, R367 exact sharp PF2 radius; original signed 12-K/J source `research_notes/r346_unbounded_interior_tp2_corank301_20261028_emr3/R346_verify.py` in this PR branch.

**New mathematical result:** in the graded signed kernel family `A_theta=A+theta*x*t`, `K_theta=K` (keep all signed K/J branches), for every real `|theta| <= 1/1792` and integer `345<=r<=352`, the 2r+1 Newton coefficients of `Q_theta,r` are strictly positive, strictly PF2 but not PFinfty; each generating polynomial has nonreal conjugate zeros. Nontrivial shape deformation at `r=345,j=0,1` verified. Proved for continuum by exact response polynomial `c+theta*a+theta^2*b` and rational global majorant `M`, not by sampling.

**Exact checks:** 5,584 baseline and response coefficients; 5,568 Turan inequalities and 8 ULC first-index guards, `T<U`; both theta endpoints check 5,568 strict Turan signs + 8 ULC failures; 16 directly reconstructed D-minor equalities. Linear-response SHA256 `8afe0b222252d60a7bd879ba92edab3762e13d1ebee42820bc8d1b9b00fd31d7`; quadratic `3b3b14660da0e25fea7d9ab9d34424eef056a9b2de3359d0ff9cbffd6708c77f`.

**Reproduce:** `R368_perturb.py <path-to-R365_Q345_352_FULL_COEFFICIENTS.txt>` from the project checkout; script requires the sibling prior R346 source and checks original row checksum `50bf1a56fabe89d4752ed71634cbb95d6c7c320d61b09aba1c501857650555a7`. Complete rows and logs in attached archive; no new credential or hidden file.

**Limit:** This is a formal admissible A-parameter variation, not an independently authorized physical BRC parameter or X6 bridge. R363 generic extraction is still author-side pending independent review. 1792 is only the smallest integer denominator certified by the current uniform M-majorant and R367 ball, not the sharp radius of this restricted nonlinear parameter curve.

**Next:** nontrivial perturbation of an original K-branch parameter; derive higher response and sharp/minor stable domain, compare to all-r PF2 conjecture. Source Owner read returned `CONTROL_QUOTA`; no native CLAIM, Driver review, or Result. Preserve draft PR.
