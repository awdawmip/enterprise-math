# PREFIX-543 — Boundary-bit repair, exact gate moments and preservation of 26 rooted fibers

Date: 2026-11-07. Project: Enterprise Math / RS-X6-NATIVE-ROTATION-DYNAMICS (independent author-side scientific note). Frozen scientific input: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Predecessors: PREFIX-533 (26 rooted full-length classes), PREFIX-539 (first-axis BRC cocycle), PREFIX-542 (phase-only disjoint-pair binomial transform).

## Precise carrier and question

Frozen four-STAR triples: (1,3,6), (1,4,5), (2,3,5), (2,4,6). There are 48 signed directed phase states, 144 legal edges, three successors per phase, and independently chosen INNER/OUTER bits b_t∈{1,0} per transition. The target is T=(A,+L1,-L3), with no self-edge. First-axis BRC count p is determined by the phase path and its endpoint, equivalently by the PREFIX-539 edge cocycle τ_r(i,j)∈{0,1}, with root sign r=σ(s).

For a legal phase path i_0=s,i_1,...,i_d, define K=#{t:2≤t≤d, i_t=T}, E=1_{d≥1 and i_1=T}. Hold the predecessor bit b_0=β∈{0,1} fixed. Let H_β=#{t:1≤t≤d, i_t=T, b_(t-1)=b_t=1}. The refined phase-only polynomial is

    C_s(d;q,x,y) = Σ_(phase paths) q^p x^K y^E = C_s^0(d;q,x) + y C_s^1(d;q,x).

At depth zero, K=E=0, C_s=1. Exactly 3^d unlabeled and 6^d labeled histories exist per root.

Question: extend the potential-arrival transform to a previous INNER bit, derive gate factorial moments and test whether rooted equivalence classes remain invariant.

## Theorem 1 — exact initial-bit transform at every depth

For each root s, integer d≥1 and formal q,z, set x=(3+z)/4. The two full joint BRC–gate polynomials satisfy

    P_s^(0)(d;q,z)=2^d [ C_s^0(d;q,x)+C_s^1(d;q,x) ],
    P_s^(1)(d;q,z)=2^d [ C_s^0(d;q,x)+(1+z)/2 C_s^1(d;q,x) ].

In particular,

    P_s^(1)-P_s^(0)=2^(d-1)(z-1) C_s^1(d;q,(3+z)/4).

For d=0, P_s^(0)=P_s^(1)=1. The pair of labeled distributions recovers the complete refined phase-only polynomial. At z=4x-3,

    C_s^1(d;q,x) = [P_s^(1)(d;q,4x-3)-P_s^(0)(d;q,4x-3)] / [2^(d+1)(x-1)],
    C_s^0(d;q,x) = 2^(-d) P_s^(0)(d;q,4x-3)-C_s^1(d;q,x).

The polynomial quotient is exact over Q[q,x] (one does polynomial division, not numerical division at x=1).

Proof. T has no self-edge, hence distinct potential arrivals after t=1 occupy disjoint adjacent branch-bit pairs. Each pair contributes 3+z: three bit combinations do not trigger a gate, and one does. When E=1, the first target arrival uses b_1 only, which is disjoint from all later gate pairs; with β=0 it contributes 2, with β=1 it contributes 1+z. Other free bits each contribute 2. For a fixed phase path with statistics (p,k,e) the bit-polynomial is 2^(d-2k)(3+z)^k for β=0, and 2^(d-2k-e)(1+z)^e(3+z)^k for β=1. The exponents are nonnegative by disjointness. Summing paths proves both formulas; substitution proves the inverse. QED.

## Theorem 2 — all factorial moments and conditional correlations

Uniformly sample one of 3^d phase paths from a fixed root and d independent fair branch bits, holding β fixed. At an attainable p, define μ_K=E[K|p], μ_E=E[E|p], V_K=Var(K|p), V_E=Var(E|p) and C_KE=Cov(K,E|p). These are exact rational functions of coefficients of C_s(d;q,x,y).

Conditionally on the phase path,

    H_0 ~ Binomial(K,1/4),
    H_1 ~ Binomial(K,1/4) + Bernoulli(E/2),

with independent summands. For falling factorial (X)_j and each j≥1,

    E[(H_0)_j|p]=4^(-j) E[(K)_j|p],
    E[(H_1)_j|p]=4^(-j) E[(K)_j|p]
        + j 4^(-(j-1))/2 E[E (K)_(j-1)|p].

Therefore

    E[H_0|p]=μ_K/4,
    Var(H_0|p)=3μ_K/16+V_K/16,
    Cov(H_0,K|p)=V_K/4,
    E[H_1|p]=μ_K/4+μ_E/2,
    Var(H_1|p)=3μ_K/16+μ_E/4+V_K/16+V_E/4+C_KE/4.

Proof. Given (K,E), the factorial generating functions at 1+u are (1+u/4)^K and (1+u/4)^K(1+Eu/2). Differentiate at u=0, condition on p, and use the law of total variance and conditional expectation. QED. The mixed term retains joint K–E association, rather than replacing it by marginal means.

## Theorem 3 — only three exceptional roots; 26 all-depth classes survive

The exact target predecessor set is

    Pred(T)={(A,-L6,+L1),(B,-L4,+L1),(B,-L5,+L1)}.

Every predecessor has first-axis root sign r=+1 and τ_r(s,T)=0. Let U_n^+1(i;q,x) be PREFIX-542's phase-only three-seed recurrence counting all subsequent potential target arrivals. For d≥1,

    P_s^(1)-P_s^(0)
      = 1_{s∈Pred(T)} 2^(d-1)(z-1) U_(d-1)^+1(T;q,(3+z)/4).

Proof. E=1 exactly when the first successor is T. For each such root its first-step BRC increment is zero, and the remaining phase-path generating function is the same U_(d-1)^+1(T;q,x). For every other root E=0. Apply Theorem 1. QED.

PREFIX-533 established exactly 26 all-length rooted equivalence classes for β=0. Among the three target predecessors, (A,-L6,+L1) and (B,-L5,+L1) belong to one equivalence class while (B,-L4,+L1) forms a singleton; the remaining classes contain no target predecessors. The above correction is constant within every β=0 equivalence class, so none splits. Exhaustive exact enumeration at depths 0..5 yields 26 classes for β=1 and the same partition as β=0, so no distinct class merges. Consequently β=1 has exactly **26 full-length classes with the same partition**, conditional only on the pre-existing PREFIX-533 all-length theorem.

## Exact executed certificate

Run

    python3 PREFIX543_boundary_moment_certificate.py 24

A self-contained Python integer-and-Fraction certificate constructs the frozen model's 48 phases and 144 edges. It compares the refined 3-seed phase-only recurrence plus binomial boundary transforms to independently coded forward INNER/OUTER branch dynamics using the original first-axis BRC endpoint formula for every root, both boundary bits and each depth 0..24.

Actual result: ALL_CHECKS_PASS. Exactly 2,400 complete joint-histogram equalities, 11,552 conditional-moment fiber checks (each compares three rational identities), 72 altered root/depth pairs (three special roots at each positive depth), and the same 26 rooted classes through depth 24 for either initial bit. Depth-five class partitions are identical. At depth one, a target predecessor has P^(0)=6, P^(1)=5+z, an exact witness that initial-bit information changes the gate observer.

The all-length mathematical claims rely on disjoint-pair and finite-state arguments and the PREFIX-533 classification; the bounded computations test the precise frozen model at the stated depths. Independent mathematical review remains open.

## Observer scope and next step

Input: native phase paths with BRC cocycle and labeled branch bits. Retained for this observer: (p,K,E) histogram and fixed predecessor bit β. From these one can recover both gate-count distributions and factorial moments. For future operations inspecting ordered branch identities, Cell addresses, provenance, or cross-segment gate interactions, retain the native carrier.

Next PREFIX-544: determine the minimal exact compositional boundary interface for concatenation of two independently generated path segments. Test whether the terminal phase and last bit (together with the first-axis root information) suffice in addition to phase-potential histograms, or exhibit a small explicit counterexample when replacing paths by only (p,K,E). Compare the BRC fiber distinctions before trying to reduce state.

Source status: independent author mathematical result and exact integer tests; native session/owner unresolved. Native control read returned BACKEND_IDENTITY_OR_VERSION_MISMATCH with operation_sent=false. No native CLAIM, Result, Review or Foundation admission is asserted.
