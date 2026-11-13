# R401 — Portable signed K₃ BRC corank-29 research handoff

**Frontier:** immutable previous R400 PR #1708 head 9a86fbbc3b1b120dad1cd1a1b8e5042a1e58113b. Original 12-branch R346 K/J→B→D retained; sole perturbation K₃[t²]=−8(1+θ), θ>−1.

**New proven finite result:** r=29, 59 Newton coefficients and 57 Turán defects. \(C_{29}(\theta)\in PF_2\) iff \(-1<\theta\le\eta_{29}\), where \(\eta_{29}\) is unique root of \(T_{29}\) between 1868683/10^6 and 1868684/10^6 (display 1.8686834603919513). A secondary simple crossing lies in (1871533/10^6,1871534/10^6), where c29<0, no PF₂ restoration. At θ*=15/8, ord c_{29+s}=2s (1≤s≤29), ord T_{29+s}=4s (1≤s≤28), c28,c29<0; c58=1002242216651368(30−16θ)^58 exactly.

**Reproducible sources:** r401_exact.py, r401_symbolic.py, r401_certify.py (run with Python 3 and SymPy in that order: python r401_symbolic.py && python r401_certify.py). Original standalone artifact includes R401_POLYNOMIALS.json and R401_EVIDENCE.json. The GitHub scripts regenerate both machine files and exact evidence digests listed in R401_EVIDENCE_INDEX.md; no binary GitHub download or external setup is necessary. Complete proof is R401_PROOF.zh-CN.md.

**Actual checks:** R401_SYMBOLIC_PASS / R401_EXACT_PASS; 812 independent Fraction point crosschecks; 120 certificate objects; 132 rational leaves; 139 Bernstein checks with 9500 strictly positive rational controls; max depth 12. An independent directory regenerated both JSONs byte-for-byte. Full local archive contains logs and SHA256SUMS.

**Bounds:** finite signed auxiliary BRC observer only, not all-r uniform PF₂, global Q, D-TP₂, native X6 or physical dynamics. P000/ACTIVE worldview not modified. This is AUTHOR_SIDE_EXACT / DRIVER_UNREVIEWED / NOT_ADMITTED / ACTIVITY_REGISTER_PENDING. No original owner CLAIM is assumed. Native service reported authority_granted=false and CONTROL_QUOTA; no Result/review status asserted.

**Next smallest unit:** derive or refute the all-r Catalan formula and odd/even degeneration order from original K/J algebra; alternatively independently certify r=30. Resume from verified current GitHub commit and regenerate evidence instead of rerunning r≤28.

**Pinned sources at research start:** GLOBAL_KNOWLEDGE_V1 main@a8b949c4cf3a47ae30a94b8d08e8ddeeb12e1e9d; enterprise-math main@154ab052d3f249639c7af245ed7d9899e9efd99a; R400 PR head 9a86fbbc3b1b120dad1cd1a1b8e5042a1e58113b. No credentials or session keys included.
