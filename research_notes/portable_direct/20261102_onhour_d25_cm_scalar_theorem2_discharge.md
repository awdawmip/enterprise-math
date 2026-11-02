# D25: CM Theorem-2 discharge of original scalar port; explicit Fermat quotient target

2026-11-02. AUTHOR-SIDE SCIENCE / PUBLISHED-THEOREM SPECIALIZATION + EXACT ALGEBRAIC CONSEQUENCE / FINITE EXACT CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.
Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7; frozen science c47e13e4aba0e006366f989d6334d443f6333ae3; historical Research lane chatgpt-research-onhour-enterprise-math-20260923 (NOT a current authenticated session). Previous author front e6f675caf4a340766d117d16c859c1f9c06b2512. This is not a Source checkpoint/Result.

## Theorem A: a previously conditional p^2 scalar lemma is discharged by an exact source

For any prime p ≡ 13 or 19 (mod 24), p>3, and a_k=(1/2)_k(1/3)_k(2/3)_k/(k!)^3, define F_p(z)=Σ_{k=0}^{p−1}a_k z^k, W_p=[(1+6θ)F_p](1/2), θ=z(d/dz). Then

    F_p(1/2) ≡ 0 (mod p²).                                      (A)

Proof and provenance: S. Chisholm, A. Deines, L. Long, G. Nebe, H. Swisher, “p-Adic Analogues of Ramanujan Type Formulas for 1/π,” Mathematics 1 (2013), 9–31, DOI 10.3390/math1010009, Theorem 2. PDF: https://www.math.rwth-aachen.de/~Gabriele.Nebe/papers/Ramanujan.pdf . For CM elliptic curves the theorem gives vanishing of the *unweighted* truncated 3F2 modulo p² when the reduction is supersingular. This is a specialization of published prior art, not a new universal theorem.

For d=3 its family is E_3(t): y²+xy+(t/27)y=x³, λ=−4t(t−1). At the exact original λ=1/2, take t=(1−1/√2)/2 with t(1−t)=1/8. Its invariants are c4=1−8t/9, Δ=t³(1−t)/27³ and
    j=27(9−8t)³/[t³(1−t)]=5832000−6829056t=2417472+1707264√2.
This is the CM j-value for discriminant −24, the CM field being Q(√−6); independently listed in Imin Chen, “On the equations a²−2b⁶=c^p and a²−2=c^p,” LMS J. Comput. Math. 15 (2012), doi:10.1112/S146115701200006X. The Hilbert class polynomial is H_{−24}(X)=X²−4834944 X+14670139392.

For both selected residue classes, (−6/p)=−1. Deuring's CM reduction criterion therefore gives supersingular reduction in the unramified residue extension. The 2013 theorem's other hypotheses hold: p>3, Q(√2) unramified, t and 1−t p-units so Δ is a p-unit, λ=1/2 and the original Ramanujan weight parameter a=6 are p-units. Apply the cited Theorem 2 to get (A). Its Theorem 1 also independently confirms the known first-digit weighted W_p≡p mod p² (its sign and (2/p) both −1), but NOT the unproved p³ mother goal. Remark 1 explicitly attributes a p³ conjecture to Zudilin.

## Theorem B: the source-preserving scalar port vanishes at the *required* operation

Reuse the exact Cauchy-value transport already proved at
research_notes/portable_direct/20261102_onhour_d25_original_w_cauchy_value_p3_boundary_transport.md .
Keep ALL its original ordered-index definitions: C=[E F]_{<p}, P=(1−z)^{3m}F, H=P−[P]_{<p}, D=C−[P]_{<p}, m=(p−1)/6, L=[(3θ−1)C](1/2), U=[(3θ−1)H](1/2), T=[(3θ−1)D](1/2), e0=2^(−3m). The exact earlier identity is

    W_p = 2e0^(−1)(L+U−T) + 3p F_p(1/2).

By (A), its scalar correction is divisible by p³ for this prime class. Therefore the frozen D25 weighted supercongruence is equivalent to

    W_p ≡ p (mod p³)  iff  L+U−T ≡ p e0/2 (mod p³).              (B)

This discharges an explicit condition in the prior author note, without silently replacing any original coefficient, weight, cut-off or sign. It is NOT a proof of the right-hand p³ congruence.

## Theorem C: express the exact remaining target in one ordinary integer coordinate

Let q_p(2)=(2^(p−1)−1)/p ∈ Z. Since p≡13 or19 (mod24), (2/p)=−1. With 3m=(p−1)/2, Euler's criterion fixes the negative p-adic square-root branch:
    e0=2^(-(p−1)/2)=−(1+p q_p(2))^(−1/2)
      ≡ −1 + p q_p(2)/2 (mod p²).
Hence (B) is exactly equivalent to the **unresolved** explicit signed target

    L+U−T ≡ −p/2 + p² q_p(2)/4 (mod p³).                        (C)

All rational denominators are p-units. This is an exact algebraic simplification for the chosen class, not an approximate numeric formula.

## Exact check and typed observer scope

The attached executed standalone standard-library checker computes modular Pochhammer coefficients, the original weighted W, *independent* ordered E*F and (1−z)^(3m)*F convolutions, retained high boundary U and signed defect T, and Fermat quotient target. The tested p=13,19,37,43,109,373,1171 all satisfy source lemma (A) and the transport; their W≡p mod p³ is finite diagnostic ONLY. At p=373:
    F=9,878,159 = 71*(373²) (mod 373³),
    L=8,487,242; U=19,060,673; T=46,400,081 (mod 51,895,117),
    (L+U−T) mod 51,895,117 = 33,042,951,
    q_373(2) mod 373 = 204; RHS (C) = 33,042,951.
U/373²=137 mod373: the high boundary must NOT be dropped.

BRC carrier: original ordered-index (i,j), prime valuations, signed and provenance-labeled U/T/L, scalar F and precision. Future operation: W mod p³ for this CM family. (A) certifies only that 3pF is zero under this observer; it does NOT erase F/p² at higher precision, nor imply full-state/joint equivalence, nor extend to p=7. Resolution: REUSE_APPLIED (2013 CM theorem), COMPOSE_APPLIED (previous exact source transport).

## Frontier and control

Mother goal stays OPEN for all p≡13,19 (mod24): prove W_p≡p (mod p³), now reduce proof construction to (C) with BOTH valuation-2 U and order-p,p² log T preserved. Next exact step: finite WZ/creative telescoping for signed L+U−T with right-hand Fermat quotient boundary, test 13,19,373 and one non-CM witness, and confirm any candidate's source/normalization/precision. Fixed p373 native H0/B0 divided-power benchmark ([X]U mod139129, module rank, semilinear Frobenius, Green/Hesse and independent reproduction) remains NOT_EXECUTED/PENDING_OWNER; issue https://github.com/awdawmip/enterprise-math/issues/1559 .

Current native client has Site research_authority_granted=false; exact continuation CONTROL_QUOTA; own checkpoint ACCESS_DENIED; original request research-onhour-20261031-0205-dispatch-r15 reads CONTROL_REQUEST_NOT_FOUND. No mutation replay, new session, CLAIM, Source checkpoint or admission is asserted; author evidence remains UNREVIEWED/NOT_ADMITTED. No scheduler/notification change.
