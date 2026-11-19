# R284AZ — Probabilistic low-height one-scalar directed Port observer

Date: 2026-11-19. Status: AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED.
Lineage: R284AT → R284AX (simultaneous-star formal-identifiability and deterministic coefficient packing) → R284AY (necessary actuator-height bound). Frozen inherited scientific input: R284AT Git blob \`43ec6098b1330ae86d0a7863be336c5d97f6ef34\`. This is an auxiliary named-Port determinant observer, not a new native X6 or Heartbeat dynamic.

## R284AZ.1 — Existence of a one-read instrument with substantially shorter settings

Let n≥2 and integer H≥2 be known. The unknown matrix C has entries in {1,...,H}, and the observer may choose integer diagonal D=diag(d_0,...,d_{n−1}) and independent simultaneous star strengths z_1,...,z_{n−1}. A single exact scalar reading is

    Y_C(d,z)=det(diag(d)−C−Σ_{v=1}^{n−1} z_v E_{0v}).

Write N=H^(n²), L=binom(N,2), K=4(n−1)L. Independently sample all 2n−1 setting coordinates uniformly from the integer alphabet {0,...,K}. Then

    Pr[ C ↦ Y_C(d,z) is injective on {1,...,H}^{n×n} ]
        ≥ 1 − (n−1)L/(K+1) > 3/4.                        (AZ1)

Consequently a fixed integer instrument with 0≤d_i,z_v≤K exists for every n,H. Each setting is specified in O(n² log(H+1)+log n) bits. Its exact output magnitude is at most n!(H+K)^n; thus the maximum scalar output needs O(n³ log(H+1)+n log n) bits. Random settings are a **nonuniform / probabilistic existence construction**; identifying a successful setting by exhaustive finite-alphabet verification and then decoding by table lookup may require exponential time and memory. No polynomial-time setting search or decoding theorem is asserted.

## Complete algebraic proof

Write F_C(d)=det(diag(d)−C) and G_{C,v}(d)=F_C(d) evaluated with an additional −E_{0v} in row zero, minus F_C(d). Row-zero multilinearity gives the exact polynomial identity

    Y_C(d,z)=F_C(d)+Σ_{v=1}^{n−1} z_v G_{C,v}(d).       (AZ2)

The formal coefficient of ∏_{i∉T}d_i in F_C is (−1)^|T| det C[T,T]. Let a_i=c_ii. Coefficients for |T|=1 and |T|=2 recover a_i and p_ij=c_ij c_ji. The coefficient of ∏_{i∉{0,v}}d_i in G_{C,v} is −c_{v0}; hence c_{v0} is recovered. Using p_{0v} recovers c_{0v}=p_{0v}/c_{v0}. For i,j distinct and positive, the coefficient of ∏_{t∉{0,i,j}}d_t in G_{C,i} equals

    g_{i,{0,i,j}}=a_j c_{i0}−c_{ij}c_{j0}.

It therefore recovers c_ij=(a_j c_{i0}−g_{i,{0,i,j}})/c_{j0}. Every divisor is nonzero because C is strictly positive. For n=2 there are no internal i,j pairs. Thus equality of the complete polynomials Y_C=Y_C' forces C=C'.

For distinct matrices C≠C', the polynomial P=Y_C−Y_C' over Q is nonzero. Every monomial in F_C has degree ≤n; its only degree-n term is ∏_i d_i, independent of C, and cancels from F_C−F_C'. Each G_{C,v} is a cofactor at an off-diagonal entry, with degree ≤n−2 in d, so z_v G_{C,v} has total degree ≤n−1. Hence

    deg(Y_C−Y_C') ≤ n−1.                               (AZ3)

The Schwartz–Zippel zero bound over the finite integer subset S={0,...,K} of Q gives Pr[P(d,z)=0] ≤(n−1)/(K+1). There are exactly L unordered pairs of possible C. The union bound gives (AZ1). This proves both existence and the claimed probabilistic success bound.

The bit bounds follow from log₂(K+1)=O(n² log(H+1)+log n) and the Leibniz estimate |det(diag(d)−C−Z)|≤n!(H+K)^n. Distinct exact outputs are distinct integers, so absolute output measurement error strictly less than 1/2 can be corrected by rounding. Relative error, input miscalibration, and arbitrary later Port operations are outside this statement.

## R284AZ.2 — Explicit cost comparison with the inherited frontier

- R284AX constructs one exact read with polynomial-time coefficient recovery, but a conservative O(n^10(log n+log(H+1))) total input/output bit upper bound using explicit high-radix packing.
- This result gives randomized settings with only O(n² log H+log n) *per-setting* bits and O(n³ log H+n log n) response bits, together with an existential deterministic choice via finite enumeration. The computational decoder may require Θ(H^(n²)) precomputed examples and storage; this is an existence/precision improvement, not a faster end-to-end algorithm.
- R284AY supplies the necessary actuator-size inequality 2n!(H+K)^n+1≥H^(n²), which for fixed H≥2 implies K≥(e+o(1))H^n/n−H. The present sufficient K scales as n H^(2n²), so the sharp dynamic-range Pareto boundary remains open.
- The recoverable object is the full named matrix under this specific star-intervention observer. No quotient or compression of arbitrary signed BRC, branch/path provenance, native six-axis spatial relations or future Heartbeat operations is inferred.

## Reproduction and exact coverage

Companion script: R284AZ_probabilistic_port_height_checker.py (Python standard library only). Companion finite record: R284AZ_probabilistic_port_height_verification.json. It enumerates the *complete* positive-integer matrix alphabet for six fixed seeded instruments: (n,H)=(2,2) once, (3,2) three times, (3,3) once, (4,2) once. There are 86,771 candidate/output checks total; each instrument has no collisions. An independent row-linearity check passes 84 exact integer comparisons at n=2,3,4. Exact max observed output widths are 16,55,59,57,90,134 bits respectively. The finite computations test concrete instruments; the general statement is proved algebraically above. This work has not received independent mathematical review.

## Next research targets

1. Close the gap between the sufficient O(n² log H) actuator-setting bits and the necessary Ω(n log H) bits for fixed H, ideally with a polynomial-time explicit decoder.
2. Test conditional-expectation or bounded-degree hitting-set derandomization without exponential full-alphabet verification.
3. Derive the achievable number-of-readings / precision / number-of-active-Port-edges frontier when each actuator is restricted to a fixed K.
4. Resolve the H=2,3 adaptive single-entry lower-bound cases of R284AW separately.

Provenance: independent portable scientific research; no new CLAIM, native PROGRESS, Result, Review, P000 amendment or formal acceptance asserted.
