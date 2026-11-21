# R762IA — Port/BRC signed displacement: exact cosets and uniform off-zero local limit

Date: 2026-11-21. Model: the frozen six-axis *composite Port candidate* of RS-X6-TRIADIC-CLOSURE-DYNAMICS, scientific pin awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. This continues R762HX@13feed6f521a5d221700a918d86db4b903e1630c, R762HY and R762HZ. Research status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. The primitive P000 TRIADIC_CLOSURE_E remains a separate open lift.

## IA1 — Exact lattice and length-dependent coset

Let X={0,1,2,3,4,5} and P be its fifteen unordered two-axis Ports. A directed Port transition p→q is legal when |p∩q|=1. It retains support S=p∪q, occurrence identity, original order, and an independent sign ε∈{−1,+1}. The signed six-axis displacement is ε h_S, where h_S=Σ(i∈S)e_i∈Z⁶. Let W_m(p,q;x) count all m-step signed histories from p to q with total displacement x.

**Theorem IA1.** The integer span of the twenty triple-incidence vectors is exactly

    L = {x∈Z⁶ : Σ_i x_i ≡ 0 (mod 3)},       [Z⁶:L]=3.

At every finite length, for every p,q,x,

    W_m(p,q;x)=0 unless Σ_i x_i ≡ 3m (mod 6).

**Proof.** Every h_S has coordinate sum 3. For any i≠j, choose different a,b outside {i,j}; then h_{abi}−h_{abj}=e_i−e_j. Hence the span contains all zero-sum integer vectors and a vector of sum 3, so it equals L. For an m-step path, Σ_i x_i=3Σ_t ε_t, while Σ_t ε_t≡m (mod 2). The stated fixed-length congruence follows without any quotient of paths or histograms.

## IA2 — Uniform six-dimensional local limit for nonzero targets and arbitrary endpoints

Put

    Σ=(3/10)I₆+(1/5)11ᵀ,
    Σ⁻¹=(10/3)I₆−(4/9)11ᵀ,
    det Σ=729/200000.

**Theorem IA2.** For each fixed R>0, uniformly for all fifteen start Ports p, all fifteen end Ports q, and every integer target x with ||x||≤R√m and Σ_i x_i≡3m (mod 6), as m→∞ through positive integers,

    W_m(p,q;x)
      = [10√5/(27π³)] · [16^m/m³]
        · exp(−xᵀΣ⁻¹x/(2m)) · [1+O_R(m⁻¹)].

The count is exactly zero on all nonadmissible cosets. As a consequence, for each R the declared congruence is **eventually sufficient** for positive reachability between every pair of Ports throughout the stated diffusive window. In particular, each fixed target x is reached from every p to every q for all sufficiently large m of its admissible parity. No explicit minimal length is asserted.

### Exact positive BRC extraction

Let A be the adjacency matrix of the line graph of K₆, 15 vertices and degree eight. Define the real symmetric 15×15 derived characteristic observer

    B(θ)_{pq} = cos(Σ_{i∈p∪q} θ_i)/8   if |p∩q|=1,
               0                       otherwise.

There are eight allowed next Ports and two sign choices, so the positive ordered source count has the exact Fourier coefficient representation

    W_m(p,q;x) =
       16^m/(2π)^6 ∫_[0,2π]^6 e^(−iθ·x) (B(θ)^m)_{pq} dθ.          (1)

This is an exact character projection of a nonnegative source count, not a signed-weight primitive or an additional physical axis.

### Independent verification of the complete six-peak classification

For every θ, |B(θ)|≤A/8 entrywise, so ||B(θ)||₂≤1. Suppose equality holds. Because B is real symmetric, it has a real eigenvector v with eigenvalue η∈{−1,+1}. The absolute-value inequality and the connected regular graph maximum principle force all |v_p| to be equal and nonzero and every legal edge to attain |B_{pq}|=1/8. Writing s_p=sign(v_p), each edge sign is η s_p s_q.

For each triple S={a,b,c}, the Ports ab,ac,bc form a triangle. Its three edge phases have one common real sign σ_S=cos(Σ_{i∈S}θ_i)=±1. Multiplying those three signs gives σ_S, whereas the eigenvector gauge gives η³=η. Thus σ_S=η **for every triple**. All triple phase sums are congruent to 0 (if η=+1) or π (if η=−1) modulo 2π. Subtraction of triples sharing two axes gives θ_i≡θ_j (mod 2π) for all i,j. Hence θ_i=a for all i and 3a∈πZ, leaving precisely six peaks

    θ^(j)=(jπ/3)1,    j=0,...,5.

Conversely B(θ^(j))=(−1)^j A/8, so all six are achieved. Compactness gives a uniform spectral gap outside their neighborhoods. The exact spectrum of A is 8 (simple), 2 (multiplicity five), −2 (multiplicity nine), so in each neighborhood the dominant branch is analytic and separated from the remaining eigenvalues. This independently rederives the load-bearing six-saddle condition invoked by R762HX.

### Gaussian scale, periodic character sum, and uniform error

Near θ=0, B(u) is an even analytic real symmetric matrix. The normalized top eigenvector is f=1/√15·1. Each triple support occurs six times in the 120 ordered Port edges, giving

    λ(u)=1−(1/2)uᵀΣu+O(||u||⁴),
    Π(u)_{pq}=1/15+O(||u||²).

Indeed Σ is the exact uniform three-subset second moment: Σ_ii=P(i∈S)=1/2 and Σ_ij=P(i,j∈S)=1/5 for i≠j. Its eigenvalues are 3/2 once and 3/10 five times, so detΣ=729/200000.

For every j and sufficiently small u, B(θ^(j)+u)=(−1)^j B(u) **exactly**. The six peaks contribute the character sum

    ∑_{j=0}^5 (−1)^(jm) exp(−i jπ Σ_i x_i/3),

which is precisely 6 for Σ_i x_i≡3m (mod 6) and 0 otherwise. On an admissible coset, all saddle contributions agree.

Set u=v/√m and y=x/√m, with ||y||≤R. Even analytic expansions imply the central integrand differs by relative integrated O(m⁻¹) from

    (1/15) exp(−vᵀΣv/2) exp(−i v·y).

The quadratic positive-definite maximum controls the tails of each peak, and the strict global gap controls the remaining torus; the error is uniform because |exp(−i v·y)|=1. Gaussian Fourier inversion gives

    ∫_R⁶ exp(−vᵀΣv/2−i v·y) dv
      = (2π)³/sqrt(detΣ) · exp(−yᵀΣ⁻¹y/2).

The Gaussian factor is uniformly bounded below for ||y||≤R, so the integrated absolute O(m⁻¹) error becomes relative O_R(m⁻¹). The constant is

    6/[15(2π)³sqrt(detΣ)] = 10√5/(27π³).

Equation (1), the exact character sum and this integral prove IA2. Positivity of its uniform leading term proves eventual full-coset reachability in each fixed diffusive window.

## Reproducibility, scope, and retained questions

The accompanying Python-standard-library exact checker enumerates all 15 Ports, 120 directed transitions and 20 supports, checks 30 ordered axis-difference lattice witnesses, verifies Σ over all supports with rational arithmetic, and computes all reachable (endpoint, six-axis displacement) states from Port 01 for m=0,...,6. Every state satisfies Σ_i x_i≡3m (mod 6), every layer has exactly 16^m signed paths, and root zero counts at m=0,2,4,6 are 1,16,624,34688. Actual execution returned PASS R762IA; this finite check verifies the stated finite range, not a continuous-torus theorem by itself.

R762HX/HY/HZ higher zero-return corrections keep their existing author-proved/unreviewed strength. The new result gives the **leading** off-zero coefficient and arbitrary endpoint behavior. Higher corrections for x≠0 or p≠q are separate questions.

The next main question remains **single-histogram** feasibility: can N_p(n)>0 and coordinate-even H(n) coexist with C(n)=0? This theorem is an aggregate over all histograms and does not establish that every eligible individual histogram can be sign-balanced. Retain full order, sign, multiplicity and provenance for such a test. Native P000 Cell/Link/Port/time/rotation/triadic force admission remains separate from this composite candidate.
