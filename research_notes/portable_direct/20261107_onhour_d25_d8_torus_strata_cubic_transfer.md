# D25 / SECOND-DIGIT-LIFT — Cyclic torus strata behind D8 Chebyshev dynamics

2026-11-07 (Asia/Hong_Kong), author-side portable research, logical lane \`chatgpt-research-onhour-enterprise-math-20260923\`, not maintenance \`chatgpt-hourly-enterprise-math-20260921\`. Publication: \`TP2-B6F4FC938FF94941C1B7\`; frozen scientific pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\`. Previous new result: \`e44e3c7e551a0fe524b8bed856797ab40157b79a\`. Status: AUTHOR_SIDE_PROVED / FINITE_VERIFIED / UNREVIEWED / NOT_ADMITTED.

## Mother objective and reused observer

For primes p≡13,19 (mod 24), mother objective remains original216 W_p≡p (mod p³); the first-digit Pfaff identity S_m≡-∑_O A(O) (mod p) reduces its first layer to signed D8 orbit masses A(O). The prior theorem proves D8 quotient

    r=(y²-1)/(y²+1),  w=2y/(y²+1),  r²+w²=1,
    J=r²w²,  ξ=1−8J,

and R(y)=2y/(1−y²), with J(Ry)=4J(1−4J), ξ(Ry)=2ξ²−1. This work identifies the *arithmetic source* of that permutation and introduces a genuine order-changing transfer that crosses the p61 obstruction.

## Theorem 1: cyclic torus model (PROVED, all target primes)

Let δ=χ_p(−1) and work in the quadratic F_p algebra A=F_p[i]/(i²+1), with conjugation i↦−i. Its norm-one group

    G={z∈A× : z z̄=1}

is cyclic of order p−δ: when δ=−1 it is the norm-one subgroup of F_{p²}× (order p+1), while for δ=1 the algebra splits and G≅F_p× (order p−1). Let μ4={±1,±i}⊂G. Thus H=G/μ4 is cyclic of odd order

    M=(p−δ)/4.

For y∈X=F_p\{0,±1} with y²+1≠0, put z(y)=r(y)+i w(y). This gives a bijection from these rational source points to G\μ4; its rational inverse is y=w/(1−r). Under the existing D8 generators:

    s: z↦z^{-1},  q: z↦−z^{-1},  T: z↦i z.

Therefore the regular D8 rational orbits are precisely (H\{1})/{h∼h^{-1}}. When p≡13 (mod24), the two excluded y²=−1 points form one additional exceptional size-two orbit, labeled J=∞. When p≡19 (mod24), there is no exceptional orbit.

For R(y)=2y/(1−y²), direct substitution gives

    z(R(y))=−z(y)².

The −1 is killed in H, so R acts by the group squaring map h↦h², and by j↦4j(1−4j) on the D8 quotient. Since M is odd, squaring is an automorphism of H; this gives a second, group-theoretic proof that the orbit quotient action is a permutation.

## Theorem 2: exact cycle-length and population formula (PROVED)

For each divisor d>1 of M, define

    L_d=min{ℓ≥1 : 2^ℓ≡+1 or −1 (mod d)}.

There are exactly φ(d)/2 regular D8 orbits whose H-class has multiplicative order d. Each cycle under R has length L_d; consequently the number of cycles of length L_d in the exact-order-d stratum is

    C_d=φ(d)/(2 L_d).

The reason: the squaring map acts on a cyclic group H as exponent doubling; inverting a group element identifies exponent t with −t. Exact order d is preserved, and every orbit on that stratum has the same return condition 2^ℓ≡±1 mod d. Add one fixed exceptional ∞-orbit only in the 13-branch. No analytic approximation or numerical extrapolation is used in this theorem.

Exact sample predictions verified by direct D8 orbit construction:

    p=19:  M=5;  d=5 has one cycle of length 2.
    p=43:  M=11; d=11 has one cycle of length 5.
    p=61:  M=15; d=3 has one length-1 cycle,
                      d=5 has one length-2 cycle,
                      d=15 has one length-4 cycle,
                      plus one exceptional fixed orbit.
    p=373: M=93; d=3 has one length-1 cycle,
                      d=31 has three length-5 cycles,
                      d=93 has three length-10 cycles,
                      plus one exceptional fixed orbit.

## Theorem 3: cubing is an exact cross-stratum transfer (PROVED)

On the same norm-one algebra, define the source operation z↦z³ and retain the original z and signed orbit observation separately. Since

    ξ=(z⁴+z^{-4})/2,

the induced quotient satisfies

    ξ↦T_3(ξ)=4ξ³−3ξ,
    J↦Q_3(J)=J(16J−3)².

For a source H-class of exact order d, cubing changes its order to d/gcd(d,3). In particular, unlike R, this valid algebraic operator can bridge *different* torsion strata.

A discriminating exact source example is p=61: the D8 orbit labeled J=49 has order d=15 and source signed mass A=60 (mod61). Cubing takes J=49 to J=41, whose H-class has order d=5 and source signed mass A=1. Their opposite signed masses match modulo 61, providing one actual cross-stratum transfer example. At p=19, cubing takes J=4 (A=12) to J=7 (A=7). This is a constructive candidate operation, *not* a theorem that cubing pairs all nonzero masses: p=373 contains source orbits whose cubed image has zero mass.

The p61 example also establishes a precise limitation of *group automorphisms of H*: automorphisms preserve element order, whereas p61's only nonzero opposite masses lie in strata d=15 and d=5. Hence an all-orbit pairing restricted to H automorphisms cannot account for this p61 certificate. An order-changing operation such as cubing is a meaningful alternative.

## Executed verification, preservation and next exact action

The independent stdlib checker enumerates actual F_p D8 source orbits and signed masses; it builds the norm-one pairs (r,w) using exact F_p arithmetic, computes order of z⁴∈H, and independently compares every predicted divisor-stratum cycle count to the observed cycle multiset. It also checks Q_3(J) by cubing (r,w). Full process-exit-verified coverage: 77 target primes p≤1999 (40 of residue 13 and 37 of residue 19), zero failures. The p61 and p373 exact stratum tables are printed. This is an auxiliary exact finite-field certificate, not the native H0/B0, divided-power, Frobenius or independent reproduction benchmark.

BRC/source retention: z(y), original y, sixth-root residual phase v, D8 mass A(O), branch symbols and order d are distinct typed observations. The quotient J and torsion order reduce the orbit directory but do not replace the signed mass. The threefold operator includes its original z and image z³, so future source operations can be reconstructed. P000/ACTIVE worldview remain unchanged.

Native Source still reports \`BACKEND_IDENTITY_OR_VERSION_MISMATCH\`, \`operation_sent=false\`, and Site \`CONFIGURED_NOT_LIVE_VERIFIED\`, \`research_authority_granted=false\`. Existing request \`onhour11-20261106-1400-exact-research-lane-continuation\` remains UNKNOWN; not resent. No new session, claim, open, run, Result, Source checkpoint or admission. Native benchmark #1559 is OPEN, PENDING_OWNER/NOT_EXECUTED; activity REGISTER_PENDING / SYNC_DEBT.

Next smallest scientific question: derive a signed trace/transfer identity across H-order strata using order-changing odd-power or more general correspondences, first distinguishing p61 and p373 (where cubic images are often zero), and then connect this to the already completed Gauss/Clausen p²/p³ transfer. A uniform p³ proof remains the frozen target.