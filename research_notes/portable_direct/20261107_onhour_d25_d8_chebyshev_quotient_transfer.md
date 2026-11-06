# D25 / SECOND-DIGIT-LIFT — Chebyshev quotient of the D8 source observer

Date: 2026-11-07 (Asia/Hong_Kong). Author-side portable research. Logical lane: \`chatgpt-research-onhour-enterprise-math-20260923\` (not maintenance \`chatgpt-hourly-enterprise-math-20260921\`). Task publication \`TP2-B6F4FC938FF94941C1B7\`; frozen scientific pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\`. Previous author-side frontier \`731eb24885993ab70e9b64c855048293409f85b5\`. Proof status: AUTHOR_SIDE_PROVED / FINITE_VERIFIED / UNREVIEWED / NOT_ADMITTED. The native p=373 H0/B0/Frobenius experiment (#1559) is not performed here.

## Reused exact definitions

Let p=6m+1 be a prime, p≡13 or 19 (mod 24); then χ(2)=-1. Let X=F_p\{0,1,-1}, y=2x+1, and v(y)=(x^5(x+1)^2y)^m. The existing source-preserving D8 generators are s(y)=-y, q(y)=1/y, T(y)=(y-1)/(y+1). For a D8 orbit O write A(O)=sum_{y∈O}v(y) mod p. The previously proven Pfaff bridge is S_m≡-sum_O A(O) mod p, where S_m=sum_{k=0}^m binom(m,k)binom(2m+k,k). In the 13-branch the existing D8 criterion says A(O)≠0 only if a(y)=χ(y²-1)=1 and b(y)=χ(y)=1 on the full eight-element orbit. Source (y), residual phase v, a,b, group orbit, and sign are kept distinct.

## Theorem A: D8 field of invariants and Chebyshev semiconjugacy (PROVED)

On y²+1≠0 define

    r(y)=(y²-1)/(y²+1),  w(y)=2y/(y²+1),
    r²+w²=1,  J(y)=r²w²=4y²(y²-1)²/(y²+1)^4,
    ξ(y)=1-8J(y).

The transformations s,q,T act on the pair (r,w) as signed coordinate permutations. Explicitly, s:(r,w)→(r,-w), q:(r,w)→(-r,w), T:(r,w)→(-w,r); hence J is invariant. As a rational map of projective lines, J has degree 8. Since D8 is a subgroup of PGL_2(F_p) of order 8, and p>3, it follows that F_p(y)^D8=F_p(J). Two rational finite points with the same finite J differ by an actual D8 transformation: their unordered squared coordinate pairs agree; choosing signs and swap recovers the D8 action. If p≡13 (mod24), the two points y²=-1 make a single exceptional D8 orbit and are assigned J=∞.

Introduce the degree-two rational operation

    R(y)=2y/(1-y²).

R maps X to itself: its poles ±1 were excluded, it sends no point of X to 0, and R(y)=±1 would require a root of a quadratic of discriminant 8, impossible since χ(2)=-1. Direct substitution yields

    J(R(y))=P(J(y)),  P(j)=4j(1-4j),
    ξ(R(y))=2ξ(y)^2-1.

For y²=-1, R(y)=y and P fixes the assigned point J=∞. Thus this is the exact Chebyshev T_2 map induced on the D8 orbit quotient, not just a numerical pattern.

## Theorem B: P permutes the F_p-rational D8 orbit set (PROVED)

For two finite orbit labels j1,j2, P(j1)=P(j2) implies either j1=j2 or j1+j2=1/4. Suppose j1=J(y), j2=J(z)=1/4-j1 with y,z∈X and finite J. Put r=r(y),w=w(y). Then the two values r(z)^2,w(z)^2 must be (r+w)^2/2 and (r-w)^2/2 (up to order), because they sum to 1 and their product is 1/4-r²w². Since χ(2)=-1, either expression is a nonsquare whenever its numerator is nonzero. Both r+w and r-w are nonzero: if either vanished, r²=w²=1/2 would itself be a square, contrary to χ(2)=-1. Contradiction. Hence j2=j1, which means the original points are in the same D8 orbit. P is injective on the finite rational-orbit labels and therefore a permutation; the exceptional ∞, if present, is fixed.

This is an all-primes theorem about the concrete quotient, not an assumption about the unsolved S_m=0 statement.

## Theorem C: the 13-branch nonzero-to-zero transfer (PROVED)

Suppose p≡13 (mod24), so χ(-1)=1. For y∈X,

    b(R(y))=χ(R(y))=χ(2)χ(y)χ(1-y²)=-a(y)b(y).

If A(O)≠0, existing D8 parity reduction forces a=b=1 for every y∈O. Consequently b(R(y))=-1. In the 13-branch the Klein-four suborbit contribution is v(1+a)(1+b), and T swaps a,b. Every Klein quartet in the target D8 orbit therefore has vanishing sum. Thus

    A(O)≠0  =>  A(P(O))=0  (p≡13 mod24).

Since P is a permutation of orbit labels, the number of nonzero source orbits cannot exceed the number of zero orbits. More sharply, each P-cycle of length L contains at most floor(L/2) nonzero orbits. In particular N_+ + N_- ≤ N_0 for the established D8 signed observers. This is an exact integer bound for all such primes, independent of the open global balance N_+=N_-.

## A decisive counterexample to cycle-local cancellation

Although P is a genuine cross-orbit permutation, it does not in general reverse nonzero orbit signs, nor force cancellation inside each P-cycle.

At p=19, labels j=4 and j=7 are interchanged, and their actual signed D8 sums are 12 and 7 (mod19); this is a *special-case* cross-orbit cancellation.

At p=61, two distinct P-cycles of finite labels are

    C1=(34,1,49,27), signed source sums (0,0,60,0) mod61,
    C2=(41,47),       signed source sums (1,0)       mod61.

Thus each individual cycle has nonzero total, while 60+1=0 (mod61) globally. For p=373, all ten previously identified nonzero D8 orbits map to zero orbits under P. The mother first-digit balance must therefore use a cross-cycle relation or another global trace mechanism; merely requiring zero sum on each doubling cycle is disproved at p=61. This is a scoped counterexample, not a disproof of the mother target.

## Execution and sources

The companion exact finite-field checker independently enumerates D8 orbits, reconstructs S_m modulo p using multiplicative binomial recurrences, verifies J and R, the orbit permutation, and the 13-branch transfer. Process-exit-verified execution: all 77 target primes p≤1999 (40 in class 13, 37 in class 19), zero failures, with explicit p19/p61/p373 cycle evidence. The existing prior D8 checker covered 312 primes through 10000; this new run is separately scoped and does not claim a native p373 benchmark.

BRC use: composed source-aware D8 residual phase (original y,v,a,b), one quotient readout J and exact future operation R. Retain raw y and full signed orbit A(O); J alone loses information needed for the sum, so it is used only as an exact orbit locator with A stored as an independent observation. No novel universal BRC operation is claimed.

Current Source read attempt: \`em_status\` and the original receipt ID \`onhour11-20261106-1400-exact-research-lane-continuation\` each returned BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false; Site gateway phase CONFIGURED_NOT_LIVE_VERIFIED, research_authority_granted=false. No new session, claim, run, Result or native checkpoint claimed. Activity REGISTER_PENDING / SYNC_DEBT. Issue #1559 remains OPEN, native benchmark pending owner.

Next exact science: exploit the permutation P as a dynamical operator, but test a *cross-cycle* trace/sign correspondence (not a per-cycle cancellation assertion) against p=61 and p=373; then consume existing Gauss second-jet/Clausen signed boundary toward W_p≡p (mod p³) for p≡13,19 (mod24).