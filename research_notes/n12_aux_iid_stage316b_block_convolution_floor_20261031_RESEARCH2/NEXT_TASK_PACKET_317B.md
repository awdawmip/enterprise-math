# Stage317-B — exact two-rate chamber envelope and first true global Pareto transition

Status: portable Research2 next scientific problem, UNREVIEWED / NOT_ADMITTED. It does not create a native Task, CLAIM, Result or Driver approval.

Read immutable Stage316-B proof and executed Fraction checker from this PR. Frozen science: S fair, Pr(J=S)=7/8, Pr(W=S)=3/4, Y~Bern(p_S), p0=1/4,p1=3/4; eight (a_h,b_h) masses /256 `(63,1),(21,3),(21,3),(7,9),(9,7),(3,21),(3,21),(1,63)`. Future Bernoulli rates locked per h. Public G=(W,Y), tagged S,J,G, all-F n=3 TV equivalent to worst allowed adaptive H/F.

New exact reduction: in every global tagged-risk optimum the four central rates are MAP (Stage315). The remaining four group into two identical complemented two-rate blocks (Stage316). For every feasible public budget z,

`F_3(z) = (12/256)D_3(p0,p1) + min_{s∈[a_3,z-a_3]}[C_3(s)+C_3(z-s)]`,

where `C_3(s)=min_{u,v∈[0,1], b_3(u,v)≤s} c_3(u,v)`, `a_3=min b_3`, and explicit `b_3,c_3` polynomials with absolute-value chambers occur in `PROOF_STAGE316B.md`. The exact global public lower bound has been increased to `P_n>5/7168` for every n≥3; do not treat this lower bound as the exact minimum.

**Smallest research unit:** symbolically partition the two-rate square [0,1]^2 by the four word-residual sign polynomials and the sign changes of D3(p0,u),D3(p1,u),D3(p0,v),D3(p1,v). Use exact elimination / Sturm / rational interval cells on the relevant public budget s to bound or determine C_3(s). Then solve the one-dimensional allocation minimization, paying attention to asymmetric optimizers. Obtain either a strict rational/algebraic competing 4-rate vector for epsilon in `(18117/4000000, epsilon_c≈0.00865532323)` or a certified nonzero expansion of Stage312's region; failing those, certify a new chamber exclusion with transparent region/coverage.

Provide: precise hypotheses/quantifiers, full proof or exact counterexample, runnable checker with actual stdout and rational certificate, correct provenance and continued incomplete questions. BRC external observer conclusion is not P000 native X6 proof. Do not borrow another owner's CLAIM; preserve portable author identity and independent review/admission semantics. Publish onto this authorized research PR with immutable readback when possible; if **GitHub connection/write capability** fails, follow the user's private EnterpriseMath-Handoffs Drive fallback with complete round-trip verification and no credentials or permission expansion. A platform security refusal must not be bypassed via Drive.
