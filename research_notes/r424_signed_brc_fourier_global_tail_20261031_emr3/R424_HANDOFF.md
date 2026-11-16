# R424 portable handoff (2026-10-31)

**Current frontier:** all integers s≥50,m≥1 satisfy strict original signed auxiliary BRC Turán D_(s+m,s)>0, by an analytic Fourier positive-half + retained negative-half proof. There is no m upper bound, no dependence on R419's large-m certificate. The exact counterexample at (s,m,r)=(2,1,3) gives D=-5 and refutes unconditional all-s strict positivity.

**Secondary results:** as q→∞, n/q→α∈[0,1], qδ_(q+n,q)/(2^n binom(2q,q))→(1+2α)^(-3/2). For q≥max(1,2n), 0≤1−F(q,n)≤(11n+8)/(3q).

**Inputs:** original R423 signed twelve-branch auxiliary δ,H,D definitions given in R424_PROOF.zh-CN.md. Global canonical read main d2d8c2f23743310331d91d020f43bbc30cdb20de, EM canonical source main 9e5ac99311a1be29a5ac8330a8857e96cb43c033, predecessor R423 PR head 7ae3dfd9cad5b0ca61f6becd107e44a6ba207da4.

**Reproduce:** python R424_VERIFY.py; prints R424_EXACT_PASS 3320 1680 3319 1 global_tail_samples 90 negative_edge -5 and generates full finite-data R424_EVIDENCE.json. Fixed in-repo proof plus regeneration script and summary are portable; full original local 15,225-byte raw JSON belongs to the packaged research artifact, whose SHA256 is recorded in summary.

**Actual publication and authority:** author-side GitHub publication only. Connected GitHub user awdawmip; native Directed Research authority_granted=false, owner check CONTROL_QUOTA, so source owner, formal CLAIM, Result, Driver Review and mathematical admission pending. Native X6 and physical bridge are separate obligations, P000 and ACTIVE worldview unchanged.

**Next exact unit:** classify all 1≤s≤49 by signed raw coefficient, especially boundary s=2,m=1; detect other counterexamples or lower the analytic s threshold. Check older fixed-s certificates against the same exact signed definition and their true domains, rather than inferring full positivity from finite tests. Preserve proper independent Driver review for admission.