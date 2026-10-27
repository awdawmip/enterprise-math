# R325 HANDOFF — Infinite tail witness + exact finite triangle

**Current author result:** For all integer r≥4, let s=4r−3. Then the formal z-adic lowest term is M_s(z)=−z^r+O(z^(r+1)), hence the degree-(7r−5) coefficient of B_s(t) equals −1 and q=7r−5>s. These are out-of-domain counterexamples to full F coefficient positivity, **not** counterexamples to prescribed 0≤q≤s Newton positivity.

**Proof dependency:** R324 finite-source rational U(x,z) from original n_i/δ_i. Put w=x(1−z), Q=1−z+𝓓, H=(1−z)(N−1)−𝓓, T=zw⁴. Weighted grading deg_w−4deg_z gives Q_0=1−T, Q_{−1}=−zw³(3+T), H_{−2}=zw²(1−T)², H_{−3}=zw(2−10T+7T²). Thus (U−1)_{−2}=zw²(1−T), (U−1)_{−3}=zw(2−5T−T³/(1−T)). Exactly one −1 coefficient on the claimed staircase for each r≥4. Full algebra/proof is in R325_TRIANGULAR_AND_NEGATIVE_TAIL_PROOF.zh-CN.md; SymPy certificate in R325_independent_weighted_check.py.

**Finite advance:** For every integer s=0..1024 and q=0..s, [t^q]B_s>0, 525825 exact positive integer entries. Triangle serialization SHA256 b007bb869980282dc2dc88101e762db65d2b55fa29d553e56a7ea5a237ac0821. Full B recurrence is 12-term fixed integer-polynomial transfer from R324; R325_scan_triangle_1024.py gives exact re-executable certificate. Independent original M recurrence crosschecks 32595 coefficients for s=0..192. Off-domain negative entries counted: 220525. Full scope/evidence in R325_EXACT_EVIDENCE.json.

**Authority:** GitHub login awdawmip and repo permission admin actually checked. Native em_control_tasks returned CONTROL_QUOTA; em_session_start returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. Active task Owner not authoritatively verified; no CLAIM, Result, Driver review or Foundation admission. Research activity RA-EMR3-20261027-R325-0820 is a direct-author metadata registration, not an authorization.

**Frozen sources:** GLOBAL_KNOWLEDGE_V1 main@14be18c2c5017e3831777d0a1e05026303527956; Enterprise Math main@bf16665ae130258a99c8516298361152e618c308; R324 immutable commit@42ec6917eeeb30b2f09c4cc43a65d1ba929aca73; P000 canonical blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc.

**One executable next mathematical unit:** Seek a positivity-preserving invariant cone for the 12-term B_s transfer **after** faithfully accounting for coefficients q>s, because K_2(t)=−t+4t²+4t³ prevents naive coefficientwise nonnegative induction. Either derive a valid whole-triangle positive decomposition for all s, or find a first exact negative coefficient with q≤s (none through 1024). This is independent of, and does not settle, D_d(n)>0 and N_peak=81. Do not interpret off-domain −1 staircase as physical phase cancellation.

**Persistence:** Research branch source files first; verify immutable Git commit and blob before declaring remote storage complete. EM activity checkpoint and account journal are separate write/readback phases. Formal admission pending.
