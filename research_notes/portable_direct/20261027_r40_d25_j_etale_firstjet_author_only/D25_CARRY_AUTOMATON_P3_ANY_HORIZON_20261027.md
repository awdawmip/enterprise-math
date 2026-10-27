# D25 auxiliary finite-Cauchy coefficient: exact all-horizon p³ carry automaton

2026-10-27. **AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. This is a supporting arithmetic theorem, not an original-class H0/B0 calculation, native LIFT reduction, Source checkpoint, or independent review.

Parent: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication: TP2-B6F4FC938FF94941C1B7. Taskbook blob 53a3ef039325534e3715add837f0eee332289984. Frozen scientific source c47e13e4aba0e006366f989d6334d443f6333ae3 (not rebased). Reuse the same author's earlier Lucas/Kummer and finite signed-Cauchy results in this Draft PR; no new independence claimed.

## Exact theorem and proof

Let p>=5 be prime and n>=0. The already published author-side Legendre/Kummer identity for c_n=(3n)!(2n)!/(216^n(n!)^5)=binom(3n,n)binom(2n,n)^2/216^n is

\[
v_p(c_n)=\sum_{i\ge1}\left(\lfloor 3(n\bmod p^i)/p^i\rfloor+\lfloor2(n\bmod p^i)/p^i\rfloor\right).
\]

Reading the base-p digits d_i of n from least to most significant, start with (a_0,b_0)=(0,0) and update

\[
a_{i+1}=\lfloor(2d_i+a_i)/p\rfloor,\qquad b_{i+1}=\lfloor(3d_i+b_i)/p\rfloor.
\]

Then exactly \(v_p(c_n)=\sum_i(a_{i+1}+b_{i+1})\). An extra leading zero digit contributes no further valuation for p>=5. Thus exact support of c_n modulo p^3 is selected by cumulative cost <3. Surviving carry states are 0=(0,0), 1=(0,1), 2=(1,1), costing respectively 0,1,2 upon entry. State (1,2) costs 3 and is permanently rejected; from any retained state, (1,0) and (0,2) are impossible because 2d+a>=p implies 3d+b>=p, and 3d+b>=2p implies 2d+a>=p.

Put \(p=6r-1+2\delta\), where delta=0 for p≡5 mod6 and delta=1 for p≡1 mod6. Define \(q=2r+\delta,\ z=2r,\ t=r+\delta\). By splitting the exact digit intervals at the thresholds for the 2d and 3d carries, the transition-count matrix from old state rows 0,1,2 to new state columns 0,1,2 is

\[
A_p=\begin{pmatrix}q&r&r\\z&t&r-1+\delta\\z&r-1+\delta&t\end{pmatrix}.
\]

A transition into column j consumes valuation cost j, including its multiplicity. This yields an exact three-state weighted transducer for every digit word; it does not merely test a set of small primes.

For \(H_{p,e}=\#\{0\le n<p^e:v_p(c_n)<3\}\), we prove for every e>=0 that \(H_{p,0}=1\), \(H_{p,1}=q+2r\). For e>=2, with the last term absent when e<4,

\[
\boxed{H_{p,e}=q^e+2r(q^{e-1}+(e-1)zq^{e-2})
+r(t+(e-2)z)q^{e-2}
+\binom{e-2}{2}r^2z^2q^{e-4}.}
\]

The proof enumerates all possible costs <=2: no positive event contributes q^e. One event of cost 1 contributes r q^{e-1} if last and (e-1) r z q^{e-2} otherwise; one cost-2 event contributes identically. Two cost-1 events at adjacent positions contribute rt q^{e-2} if second last, else (e-2)rtz q^{e-3}; separated positions contribute (e-2)r²z q^{e-3} if second last and binom(e-2,2) r²z²q^{e-4} otherwise. Since t+r=q, combining gives the displayed formula. For p=6r-1 it simplifies to the particularly compact exact law

\[
\boxed{H_{p,e}=(2r)^e(e^2+7e+8)/8\quad(e\ge0).}
\]

For fixed p, H_{p,e}=O_p(e² q^e); q<p, hence the fraction of coefficients that can contribute modulo p³ decays as O_p(e²(q/p)^e).

For any arbitrary N, count n<N with the same carry states and an additional three-way comparison with N. Reading digits least-first, the most recent *higher unequal* digit overwrites the comparison; equal higher digits leave it unchanged. Split the digit range at 0,p,ceil((p-a)/2),ceil((p-b)/3),ceil((2p-b)/3), N_i and N_i+1. Each interval has constant destination/cost/comparison, and its length is the exact multiplicity. This computes the exact count in O(log_p(N+1)) integer state updates (not bit complexity; producing all indices has output-size cost).

## Signed finite-Cauchy application / observer audit

Let u_j=binom(2j,j)/8^j, W_N=sum_{k<N}(6k+1)c_k and S_N=sum_{j+k<N}(3(j+k)-1)u_j c_k. Let K_{p,N} be the indices k<N accepted by the transducer with valuation <=2. Since all u_j and signed integer weights are p-integral, both W_N and S_N are unchanged modulo p³ when terms with k outside K_{p,N} are omitted. The triangular cutoff and labelled (j,k) source relation are preserved; **no equality S_N=W_N or original LIFT conclusion is asserted**. A mask does not reconstruct nonzero unit residues or higher precision. BRC reuse: prior two carry channels and signed Cauchy ports, with an exact precision horizon. Arithmetic indices are external mathematical variables, not native Heartbeat X6 spatial cells; no native readout bridge has been proved.

## Executed author check and handoff

The full standard-library author checker (local file d25_finite_state_p3_carry_support_20261027.py) passed on primes 5,7,11,13,19,31,37,43. It checked all 24 transition rows, at least 22,353 independent factorial-Legendre oracle indices, closed counts through e=7, irregular bounds and five direct signed triangular sums beyond N=p. A compact reproducible checker and recorded result are in this PR. Exact formula/DP examples: p=5,e=8 yields 4096 out of 390625; p=7,e=8 yields 46413 out of 5764801; p=13,e=6 yields 111475 out of 4826809; p=373,e=4 yields 1567464719 out of 19356878641. Large counts were computed from the proved formula and digit DP, not brute-force enumeration.

Next LIFT obligation is the original-class Delta_p−R_p mod p and H0/B0–Frobenius/weighted-observer transfer; the p373 native evidence remains requested under Issue #1559. The original 94687-byte UR V2 bundle must be source-matched to SHA-256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76 before writer provenance. Gateway 0.6.11 returned CONTROL_QUOTA on own exact continuation, ACCESS_DENIED on own checkpoint list, and CONTROL_REQUEST_NOT_FOUND on old receipt. Source ownership/CLAIM/OPEN not established; if current-input-only seed arrives, read every input artifact, keep predecessor completed_units=[], and follow typed Source preparation only with real authority.

This note is author evidence stored on an existing GitHub Draft branch, not native publication or reviewer approval.
