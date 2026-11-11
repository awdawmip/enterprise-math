# D25/LIFT — Exact observable-only conics for two finite Clausen ports

Date: 2026-11-11. Status: AUTHOR-PROVED / EXACT FINITE CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_SOURCE_CHECKPOINT.
Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, frozen scientific source c47e13e4aba0e006366f989d6334d443f6333ae3.

This new observer-only corollary uses the previous author-proved Lucas signed-norm identity and checks it by a separate direct raw-orbit method. It does not claim to advance native H0/B0 divided Frobenius.

For prime p>5 write p=6m+1+4epsilon, epsilon=0 or 1. For every legal orbit O in F_p minus {0,-1,-2}, let lambda=t+T(t), T(t)=-2(t+1)/(t+2), Delta=(lambda+4)^2-8, nu=1 if moving and 1/2 if fixed, N=-2^(-(2m+epsilon)), c=N*nu. Define the original normalized port outputs A=N sum_O V_epsilon(t), B=N sum_O V_epsilon(t)*w_epsilon(t), with U(t)=(t+1)(t+2)^2/t, V_epsilon=U^m(t+2)^epsilon, w_epsilon=(2-12epsilon-(3+10epsilon)t)/(t+2).

**Theorem (both branch conics, including fixed orbits).**

epsilon=0:

    (B-(2lambda+5)A)^2 = 4 Delta (A^2-2^(m+2)c^2).        (C0)

epsilon=1:

    (32A-(lambda+4)(B+13A))^2
        = Delta ((B+13A)^2 - 2^(m+10)c^2).                (C1)

**Proof.** The previous exact Lucas reconstruction gives, for epsilon=0, A=cL and B=c[(2lambda+5)L-2H]; hence B-(2lambda+5)A=-2cH. The independently proved universal norm H^2=Delta(L^2-2^(m+2)) implies (C0). For epsilon=1 let Q=((lambda+4)L+H)/2. The reconstruction A=cQ and B=c(16L-13Q) gives B+13A=16cL and 32A-(lambda+4)(B+13A)=16cH. Square and substitute the norm to get (C1). No division by Delta: fixed fibers also satisfy both identities. QED.

At Delta=0 the fixed branch weighted readout is uniquely determined: for epsilon=0, B=(2lambda+5)A; for epsilon=1, 32A=(lambda+4)(B+13A), with lambda+4 nonzero because (lambda+4)^2=8. At moving fibers Delta !=0, the equation offers at most two candidate B values for given (lambda,A,epsilon), and the actual signed H chooses the realized branch. This bounds residual information for this exact observer, without claiming that two choices are realized at every field point.

**Executed exact arithmetic:** A separate verifier independently evaluates raw U,V,w on every orbit, rather than using Lucas L,J,H for the conic sides. Both identities passed across 364 primes 7<=p<=2500, covering 210031 distinct legal fibers (352 fixed). The previously published p=31 two-orbit collision remains an explicit witness that the norm-compressed readout loses B information.

This is an algebraic refinement for a typed finite-field BRC observer; the next task is to find an orientation-aware moving-fiber cancellation identity and then connect its signed observation with frozen second-digit Delta_p-R_p, retaining odd branch/fixed provenance. Source role-bound claim/session unavailable; no formal Source checkpoint or independent review.

Antecedent: research_notes/portable_direct/2026-11-11_h40_d25_lucas_orbit_norm_signed_residual_author_portable.md