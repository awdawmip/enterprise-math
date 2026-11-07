# R5 — Complete timing-hull equality without lumpability; strict mixed O4 separation

2026-11-05. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. Researcher-ID: EM-DIRECT-8B2C5C (locally allocated, not MCP-signed). Activity: RA-63A1F44D61885FB2CCDD31B2 (registration separately verified).
Mother R5: strictly positive finite P/Q stopped BRC, equal full O4 convex hulls but different actual real-strategy O4 sets. Observer O4=(eP,eQ,TP,TQ). Frozen scientific pins preserved: global a01383f825ef9d43b4b754254303298c64041568; EM 86149263e38c22292c9def1e0f69092efa1be77e.
Scientific predecessor: timing Jensen obstruction at df0120601c8b11098242d778048bd6ea1e823298 (research_notes/brc_r5_timing_jensen_no_hull_candidate_20261105_t0440/RESEARCH.md).

## Theorem A — exactly two timing thresholds

At time 1, finitely many hidden source histories h have positive weights w_h (sum 1), identical P/Q likelihood ratio 1. Continuing reaches time-2 shared ratios r_j>0 with strictly positive Q kernel K_h(j), where Σ K_h(j)=Σ r_j K_h(j)=1. At each t=1,2 legal actions are STOP/P, STOP/Q, CONTINUE; continuing at t=2 reaches terminal t=3 via any strictly positive lawful P/Q nature kernel, followed by free P/Q declaration. FULL sees h; seedless LR sees only (t,r). Policies are arbitrary real behavioral policies.

For each K define F_K^-(t)=t−1+Σ K(j)(t−r_j)_+ and F_K^+(t)=1−t+Σ K(j)(r_j−t)_+, t≥0. Each has a unique zero: τ_-(K)∈(0,1] and τ_+(K)∈[1,∞). The FULL and LR convex hulls of the COMPLETE TWO-DIMENSIONAL timing projection (TP,TQ) are equal if and only if every hidden source has the same τ_- and the same τ_+.

Proof: For timing support normal (a,b), write S=a+b, Z_h(a,b)=a+b+Σ K_h(j)(a r_j+b)_+. The time-1 STOP score is S. At t=2 continuing contributes one additional time reward a r_j+b if positive, independently of source and of the terminal nature kernel (mean-preserving under P and Q). Bellman optimization therefore gives h_FULL=S+Σ_h w_h(Z_h)_+, h_LR=S+(Σ_h w_h Z_h)_+. Deterministic policies attain these linear supports, so these expressions cover all real behavioral policies. If a,b have the same weak sign, all Z_h have the same weak sign and the Jensen gap vanishes. In the two opposite-sign cones write (a,b)=u(−1,t) or u(1,−t), u,t>0, obtaining Z_h=uF^-_h(t) or uF^+_h(t). F^- is continuous strictly increasing, F^-(0)=−1, F^-(1)=ΣK(1−r)_+≥0. F^+ is continuous strictly decreasing, F^+(1)=ΣK(r−1)_+≥0, F^+(t)→−∞. Thus each function has precisely one root. Positive weights imply Σw(Z_h)_+−(Σw Z_h)_+ vanishes exactly when all Z_h have the same weak sign, and is strictly positive for any mix of strict positive and negative values. For every t this holds exactly when the source roots coincide in both cones. QED.

## Strictly positive nonlumpable construction with equal timing hulls

Use r=(1/4,1/2,1,3/2,7/4), K_0=(1/5,...,1/5), D=(9,−16,14,−16,9), K_A=K_0+D/1000=(209,184,214,184,209)/1000, K_B=K_0−D/1000=(191,216,186,216,191)/1000, w_A=w_B=1/2. All nature entries are positive; ΣK_A=ΣK_B=ΣrK_A=ΣrK_B=1. The signed perturbation obeys ΣD=ΣrD=0. For K_0, τ_-=23/28 and τ_+=33/28 (tail contribution 5/28 at each zero). At τ_-, the left-tail D projection equals (9·16−16·9)/28=0; at τ_+, the right-tail D projection is (−16·9+9·16)/28=0. Both K_A and K_B therefore have identical two thresholds, although K_A≠K_B. By Theorem A, all timing-only support directions coincide exactly.

Lawful strictly positive second-gate kernel: given time-2 ratio r_j, let terminal likelihood ratios s_{j,±}=r_j(1±1/100), each with conditional Q probability 1/2 and P probability (1±1/100)/2. Every P/Q transition is positive and normalized, E_Q[s]=r_j. All 10 terminal ratios are distinct. Source nature split at t1 is P(A)=Q(A)=P(B)=Q(B)=1/2. All legal stopping, continuing and declaration actions remain available; no hidden action restriction is used.

## Full O4 support still separates

Take n=(−1,−3/4,−3/20,0), k=3/4, λ=3/20. At time 2 the possible t2→t3 Bayes error reduction is at most (1/100)r_j because x↦min(k,x) is 1-Lipschitz and |s_{j,±}−r_j|=r_j/100. This is strictly less than the extra P-time cost λr_j. Hence time-2 CONTINUE is strictly dominated for n even though it is a legal action. Define G_h(k)=min(k,1)−ΣK_h(j)min(k,r_j). Direct exact arithmetic gives G_A=301/2000 and G_B=299/2000, with mean λ=3/20.

With time-1 STOP score S=−min(k,1)−λ=−9/10, FULL separately chooses the first continue gate and LR must share it. Exact Bellman supports are h_FULL(n)=S+( (G_A−λ)_++(G_B−λ)_+ )/2=−3599/4000, and h_LR(n)=S+( (G_A+G_B)/2−λ )_+=−9/10. Gap is exactly 1/4000.

A valid FULL policy CONTINUEs at time1 for source A, STOP/P on source B, and at time2 on A STOP/Q for ratios less than k and STOP/P for ratios greater than k. It realizes W=(eP,eQ,TP,TQ)=(577/8000,1607/2000,3/2,3/2), and n·W=−3599/4000. Thus W∉conv(O4(LR)), with dist_∞(W,conv(O4(LR)))≥(1/4000)/(1+3/4+3/20)=1/7600.

This is a constructive COUNTEREXAMPLE to the hypothesis “complete timing-hull equality implies full O4-hull equality.” It is not the sought mother-R5 hull-equal/non-image witness: its full O4 hulls differ. Crucially, the former 3-key symmetric timing obstruction does not generalize to all hidden kernels. The route now focuses on mixed error–time Bellman preference profiles.

## Verification / scope / next

VERIFY.py uses Python standard-library Fraction exclusively. It checks positive P/Q normalization at both gates, signed null moments, both shared threshold roots, 2401 integer timing support directions (−24≤a,b≤24), exact mixed-direction Bellman supports, strictly dominated t2 continuation, the FULL witness and distance inequality. EXACT_OUTPUT.txt is the actual output of the locally run full verifier. Theorem A covers arbitrary real a,b by proof; the 2401 cases are corroborating finite checks. BRC reuse: labelled positive P/Q masses and provenance, likelihood-ratio observer and occupancy Bellman support; signed D and support gaps are observer differences rather than branch mass.

Next: characterize simultaneous mixed-direction sign compatibility of all history-specific Bellman preference functions Z_h(n) for n∈R⁴. Search rational strictly positive kernels meeting these full-support conditions, then verify full-hull equality by exact certificates and actual-image nonmembership by polynomial constraints. P000, ACTIVE worldview, immutable frozen pins and current role/claim/admission authority remain unchanged.
