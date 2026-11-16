# R577 Research Handoff | 2026-11-06

Frozen scientific source: R462@18783e01e3646c72b7aab3b16d3f565e83e6446f.
Immediate frontier: R576@05de5b8b08acaa53243bf91bc7a2fac70c2408a6.
Scope: signed BRC auxiliary scalar Toeplitz–Hessenberg spectrum, not native X6 dynamics.

**New result (author-side exact certificate).** The entire limiting F(z)=sum_{j>=0}(-1)^j 24*8^j*z^j/(2j+4)! has precisely two zeros in |z|<14; both simple and conjugate. One lies in radius 10^-9 about 6.3392345102+9.4809517165i. They are globally minimal, with 11.4050137923<r_*<11.4050137944. Thus the R576 proven limit C=lim rho_k/k^2=1/r_* satisfies 1/11.4050137944 < C < 1/11.4050137923.

**Exact certificate:** R577_VERIFY.py runs 16384 rational-parameter polygon nodes, integer Gaussian Horner winding=2, exact global tail/derivative bounds, and exact local Taylor/Rouche inequalities. R577_PROOF.zh-CN.md gives a full proof; R577_EVIDENCE.txt stores execution transcript and PASS. No numerical tolerance is used for acceptance; printed decimal tail approximations are informational only.

**Pending:** independent mathematical Driver review and native formal CLAIM/Result. Native owner/activity status should be checked from current receipts, not inferred from prior historical runs.

**Next mathematical unit:** certify the second-nearest nonconjugate zero modulus gap and investigate irrationality of the nearest zero argument. If both hold, pursue a rigorous two-dominant-term asymptotic and sign-density theorem for L_m as m→infinity. Keep R462 branch/phase/provenance distinctions.
