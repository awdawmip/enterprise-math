# PREFIX-1046 — Sharp O(1) negative-count error and local spectral-zero drift

Date: 2026-11-24 Asia/Shanghai. Parent: PREFIX-1045. Status: AUTHOR_CONDITIONAL_ANALYTIC_PROOF / HUMAN_RECHECKABLE / NOT_REVIEWED.

## Scope
Retain frozen P000 V5 (f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json), Stage46 signed BRC W=J12−6I12, initial incoming −e1, both exclusions of Link {0,e1}, exactly one outgoing negative step, full Cell–terminal-port–grade observer with signs, provenance, multiplicity and residual. This is a symbolic theorem about the inherited derived scalar spectral observer only (NATIVE_ATTRIBUTION_PENDING_BRC_REVALIDATION); no new phase computation, classical reference run, native propagation, numerical evaluation or claimed BRC execution. Current portable protocol and ACTIVE worldview retain these distinctions.

Immutable parent actually read: 9567f20ca52f44f4b33adc2535ca26a2985d193e:research_notes/portable_direct/2026-11-24_r6_prefix1045_uniform_boundary_cones_and_negative_density.md. Also read ebccbb436685bafe6d697ace256ad93b39c0c50f:research_notes/portable_direct/2026-11-23_r6_prefix1035_six_phase_picard_fuchs_frobenius.md. Inherit from 1045 its finite regular-band zero set, endpoint cones and Beta identity, with their original conditional status. In particular g is continuous, positive near 0,4,16,36 except the vanishing endpoints, and analytic on the three regular bands. No actual interior zero is assumed to exist.

Put h(t)=g(36t), N=n+1=m+k+2, p=(m+1)/N. Let X have Beta(Np,N(1−p)) law, so D_{m,k}=E[h(X)] and has the sign of E_{m,k}. The lattice means are p=j/N, j=1,...,N−1. Write ell=length{t:h(t)<0}=L/36.

## Main result
For every inherited finite zero set, with arbitrary finite multiplicities,
    #{j=1,...,n:D_{j−1,n−j}<0}=n ell+O(1).
The same O(1) holds counting <=0. This improves PREFIX-1045's O(1+n^(1−1/r_*)) for multiple roots to a bounded error independent of n. Every even-order zero has a fixed neighborhood in which all sufficiently high-degree coefficients have the sign of the first nonzero Taylor coefficient. Every odd-order zero has possible sign mismatches confined to O(1/N) of its position. Hence there are only boundedly many ambiguous lattice positions even if the zero has arbitrarily high (fixed) multiplicity.

## Proof 1: exact centered Beta recurrence
Let mu_l=E[(X−p)^l], v=p(1−p), w=1−2p. Then mu_0=1, mu_1=0 and, for l>=1,
    (N+l) mu_{l+1}=l(v mu_{l−1}+w mu_l).
Indeed the derivative of x(1−x) times the Beta density equals N(p−x) times that density; integrate by parts against (x−p)^l, with boundary term zero since both shape parameters are positive. Substitute x(1−x)=v+w(x−p)−(x−p)^2 and rearrange. For p in any compact subinterval of (0,1), induction yields uniformly, for each fixed q>=0,
    mu_{2q}=(2q−1)!! v^q N^(−q)+O(N^(−q−1)),
    mu_{2q+1}=O(N^(−q−1)).
Use (−1)!!=1, with mu_0=1 exactly. For the even induction, the odd term is one power smaller than the even predecessor; for the odd induction the two RHS terms have the same order. Thus even moments have positive uniform lower bounds times N^(−q). All constants here can depend on the fixed order and the chosen compact subinterval.

## Proof 2: local sign
At a zero z in normalized t-coordinates, write h(t)=a(t−z)^r+O(|t−z|^(r+1)), a !=0. This remainder bound extends to all t in [0,1] by continuity and compactness outside the local analytic interval. Put d=p−z, S=d^2+1/N. All estimates below are uniform for p in a sufficiently small compact neighborhood of z.

If r=2q (q>=1), Jensen applied to the nonnegative square, or the power-mean inequality, gives E[(X−z)^(2q)] >= (d^2+v/(N+1))^q >= c S^q. The remainder is O(S^(q+1/2)): E|X−z|^(2q+1) <= (E|X−z|^(2q+2))^((2q+1)/(2q+2)), and the latter even moment is O(S^(q+1)) by the binomial expansion and Proof 1 (or the triangle inequality in L^(2q+2)). Choose the neighborhood sufficiently small and N sufficiently large. The leading term then strictly dominates the remainder, proving the even-root assertion, including d=0. In a locally negative even root, its isolated zero may be filled by a negative coefficient; there is no artificial positive run.

If r=2q+1, expand E[(X−z)^r] by the centered binomial theorem. The terms with even centered power form
    d P_q(d^2,N), P_q=sum_{l=0}^q binom(r,2l) d^(2q−2l) mu_{2l}.
Every coefficient is positive for large N, and c S^q <= P_q <= C S^q by Proof 1. The odd-centered terms (including mu_1=0) are O(N^−1 S^q), since each is bounded by a constant times |d|^(2q−2l) N^(−l−1). The Taylor remainder is O(E|X−z|^(2q+2))=O(S^(q+1)). Consequently
    D=a d P_q + O(S^q (N^−1+d^2)).
For fixed a!=0, take the neighborhood radius sufficiently small so the d^2 term is less than one quarter of the leading lower bound after dividing by S^q. Then choose a sufficiently large fixed B so for |d|>B/N the N^−1 term is less than another quarter. D has the sign of a d and hence of h(p) there. This also covers simple roots q=0. The exceptional interval of width 2B/N contains at most 2B+2 lattice positions.

Outside the disjoint root neighborhoods, use the parent uniform continuity estimate and endpoint cones to obtain exact signs for all sufficiently large N. In particular possible zero-valued coefficients are restricted to the finitely many O(1/N) odd-root windows, since the even-root neighborhoods have strict signs. Counting the negative lattice means differs from n ell by O(1) (finitely many intervals and lattice spacing 1/N); even-root equality at a lattice point changes at most one count per root. Adding the bounded exceptional count proves both strict and nonstrict versions. Finite small n are absorbed in O(1). QED.

## Proof 3: signed drift of each odd-order zero
A sharper local asymptotic identifies the center of the exceptional window. Let r=2q+1 and h(t)=a(t−z)^r+b(t−z)^(r+1)+O(|t−z|^(r+2)); b may be zero. Set v0=z(1−z), w0=1−2z. Allow continuous Beta mean p=z+u/N for bounded real u (not just lattice means); shape parameters are positive for large N. The recurrence of Proof 1 gives the more precise odd leading term
    mu_{2q+1}= (2q+1)(2q−1)!! (2q/3) w v^q N^(−q−1)+O(N^(−q−2)).
For q=0 this is mu_1=0. Induction: if c_q is the leading odd coefficient, c_q=2q(v c_{q−1}+w(2q−1)!! v^q). Substitution of the claimed formula gives the identity, since (2q−1)(2q−3)!!=(2q−1)!!. All expansions are uniform on compact p-intervals.

For d=u/N, in the binomial expansion of E[(X−z)^r] only mu_r and r d mu_{r−1} contribute at N^(−q−1). All other terms are O(N^(−q−2)) by the even/odd estimates. Similarly E[(X−z)^(r+1)] has leading mu_{2q+2}=(2q+1)!! v0^(q+1) N^(−q−1). The global remainder is O(E|X−z|^(2q+3))=O(N^(−q−3/2)) by the next even moment. Therefore uniformly for bounded u,
    N^(q+1) E[h(X)]
      = a(2q+1)(2q−1)!! v0^q [u + (2q/3) w0 + (b/a) v0] + O(N^−1/2).
In particular the transition displacement in the normalized mean coordinate is
    u_* = −(2q/3)(1−2z) − (b/a)z(1−z).
Outside any fixed epsilon-neighborhood of u_*, bounded-u signs are determined for sufficiently large N. By continuity in p and opposite signs at u_*±epsilon, a zero of the continuously interpolated Beta average exists; all its zeros in this local neighborhood satisfy p=z+u_*/N+o(1/N), by Proof 2 and the uniform limit (choose B also larger than |u_*|+1). No uniqueness is asserted. On the discrete row, sign decisions reduce asymptotically to comparison of j with Nz+u_*, except in a shrinking o(1) window in j. If j happens to approach the threshold, further terms are needed. The formula is normalized: z=y_zero/36, and b/a=36 times the corresponding next/leading Taylor coefficient ratio in y. This distinguishes skewness drift from the asymmetry of the spectral zero itself.

## Consequence and next
One no longer needs a multiplicity-dependent growing exclusion zone to certify high-degree sign counts. The new O(1) estimate holds even if the Picard–Fuchs system permits high multiplicity, and the drift formula would let a verified root enclosure predict integer sign changes. It does not prove there are any roots, nor that g is globally nonnegative. Next use the inherited rational ODE to certify actual regular-band signs/root locations (or develop a suitable analytic positivity certificate); if a root is found, use the local Taylor coefficients in the drift rule. Native X6–signed BRC observer correspondence and mother question B_fix,odd(32) in {19,20} remain open.

Validation: complete symbolic Beta recurrence, induction, Taylor bounds and lattice count above, human recheckable. No model computation, formalization, independent review or numerical root search performed. The historic registration request r6-20261123-2358-session-start-own-v1 was read as SUCCEEDED (EM-DIRECT-780BBE / RA-0ABD84561C86E53067DB0322), not a formal execution authorization. Prior owner read r6-20261124-0346-leased-observe-v1 SUCCEEDED with empty LEASED selection as of 2026-11-23T19:49:03.421111Z; new r6-20261124-0445-leased-observe-v1 was submitted. This is independent portable research, no CLAIM or formal PROGRESS. Activity association remains pending current own-session binding/authorized source update.
