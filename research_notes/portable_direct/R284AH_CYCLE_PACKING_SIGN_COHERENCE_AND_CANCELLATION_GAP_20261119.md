# R284AH — Cycle packing, signed cancellation, and exact Port activation degree

**Date:** 2026-11-19. **Status:** AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED.  
**Source:** R284AG principal-minor/SCC result, R284Y complementary minors, R284AB/AG Port Schur transfer.  
**Frozen scientific input:** 43ec6098b1330ae86d0a7863be336c5d97f6ef34.  
**Research mode:** independent portable continuation, no Task CLAIM, Result or Review authority. The matrix vertices below are typed *auxiliary Port channels*, not independent native X6 spatial axes. Named edits, signed path terms, provenance and possible future observation remain preserved.

## 1. Structural support bound and efficient cycle packing

Fix a characteristic-zero field K, an integer q≥1 and a zero-diagonal matrix N∈K^(q×q). Let t₁,…,t_q be independent commuting named edit variables, and define

    P_N(t) = det(N + diag(t₁,…,t_q)).
    ν(N) = least total degree of a nonzero monomial of P_N.

Give the directed support graph G one edge i→j for each nonzero N_ij. Define p(G) as the maximum number of distinct vertices covered by vertex-disjoint directed cycles of length at least two; the empty packing covers zero vertices.

**Theorem AH1.** For every exact assignment of nonzero rational, real or complex edge weights,

    q − p(G) ≤ ν(N) ≤ q.                                           (1)

**Proof.** The principal-minor expansion from R284AG is

    P_N(t) = Σ_{T⊆[q]} det N[T,T] ⋅ ∏_{i∉T} t_i.                   (2)

Every nonzero term in det N[T,T] comes from a permutation of T with no fixed points because N_ii=0. Its cycles are directed cycles of G, pairwise vertex-disjoint, so |T|≤p(G). Hence coefficients below degree q−p(G) vanish. The term for T=∅ equals ∏t_i and has coefficient one. This proves both inequalities. QED.

**Theorem AH2 (assignment reduction).** Adjoin an *artificial* loop of weight zero at every vertex. Give each actual nonzero off-diagonal edge weight one and forbid absent off-diagonal edges. A maximum-weight perfect row-to-column assignment has optimum exactly p(G): a selected edge permutation consists of genuine disjoint directed cycles and artificial fixed points; the objective counts vertices in genuine cycles. Thus p(G) admits O(q³) weighted-assignment computation (arithmetic/comparison model), and the support graph can first be decomposed into SCCs in O(q+|E|) graph operations. The implementation uses a subset DP rather than a cubic Hungarian implementation; the two independent small-instance packing methods are checked against one another.

## 2. Sharpness and cancellation-free conditions

**Theorem AH3 (generic sharpness).** Assign to every support edge its own algebraically independent indeterminate x_e. Then over Q(x_e),

    ν(N(x)) = q − p(G).                                            (3)

The same equality holds outside a proper algebraic subset of fixed-support numeric weight choices, including almost all strictly positive real choices.

**Proof.** Choose a maximum directed cycle packing on a vertex subset T of size p(G). Its corresponding permutation contributes a nonzero product of distinct x_e to det N[T,T]. Different permutations use different sets of directed edges and hence have distinct monomials. Their symbolic sum is nonzero. By (2) the degree q−p(G) coefficient therefore exists. The determinant polynomial is not identically zero on the positive orthant, which establishes the generic positive-weight assertion. QED.

An **exact one-sided certificate** for the actual weights is a subset T with |T|=p(G) and a verified det N[T,T]≠0: this certifies equality in (1) using one determinant after the support calculation. If weights are drawn independently and uniformly from {1,…,M}, the polynomial-zero bound applied to this fixed nonzero degree-p minor gives failure probability at most min(1,p/M). The probabilistic bound is an experiment-design aid, never a replacement for the exact nonzero certificate.

**Theorem AH4 (sign-coherent packing).** Equality ν=q−p holds when some maximum-packing subset T has all its supported determinant-permutation summands of the same strict sign. In particular:

- For positive weights, if the graph contains no **even-length directed cycle**, every supported cycle-cover summand has positive sign and equality holds.
- For arbitrary nonzero signed weights, a maximum T possessing a **unique supported cycle-cover permutation** also certifies equality.

**Proof.** A permutation that decomposes into cycles of lengths ℓ₁,…,ℓ_s has sign ∏(-1)^(ℓ_j−1). If every directed cycle is odd and weights are positive, each supported summand is positive. More generally, any sum of nonzero same-sign summands cannot vanish. For a unique supported permutation, cancellation is impossible regardless of signs. Apply AH3's exact-certificate argument. QED.

The graph criterion certifies the first nonzero **degree** only; it does not certify deletion of any named Port direction or future-operation observer equivalence.

**Theorem AH5 (SCC additivity).** For strongly connected vertex components B₁,…,B_h,

    ν(N) = Σ ν(N[B_j,B_j]),
    p(G) = Σ p(G[B_j]),
    Δ(N) := ν(N) − (q−p(G)) = Σ Δ(N[B_j,B_j]).                    (4)

**Proof.** Ordering SCCs makes N+diag(t) block upper-triangular. Its determinant is the product of nonzero polynomials in disjoint named variable families, whose minimum degrees add. Directed cycles cannot cross SCC boundaries, so packing sizes add. QED.

Equation (4) gives a cancellation-aware adaptive workflow: on each SCC compute p; search for one exact nonzero maximum-size principal minor; if found, finish the degree certificate. If not, only that SCC requires lower-cardinality signed-minor analysis. Proving that a whole degree layer vanishes requires checking all its candidate minors or a valid equivalent identity—failure of one candidate is insufficient.

## 3. Exact strong-SCC counterexample and unbounded gap

Consider the entirely nonnegative four-channel matrix

    N₀ = [ [0,1,0,0],
           [1,0,1,0],
           [0,0,0,1],
           [1,0,1,0] ].

Its support is **strongly connected** and admits a cycle packing covering all four vertices: either the two disjoint 2-cycles or one 4-cycle. Hence p(G)=4 and the graph-only bound is zero. Yet an exact Leibniz expansion gives

    det(N₀+diag(t₁,t₂,t₃,t₄))
      = t₁t₂t₃t₄ − t₁t₂ − t₃t₄,                                (5)

so ν(N₀)=2 and the constant coefficient is cancelled by opposite-parity full cycle covers. Replacing only entry N₂₁=1 with N₂₁=2 leaves support and SCC unchanged but gives det N=1, hence ν=0.

The block diagonal sum of b copies of N₀ has q=4b, p=4b and ν=2b, so Δ=2b grows without bound. Each block is strongly connected; the direct sum is not globally strongly connected.

### Strictly positive core and stable Port realization

Let k=5, c=1/80, g=1/16 and δ=1/(256k). Define, for 0≤t_i≤c,

    C(t) = c J₅ + c blockdiag(N₀,0) + diag(t₁,t₂,t₃,t₄,0).

Every entry is strictly positive and each core row sum is below one. Subtract the fifth row from the first four and expand at its fifth-column pivot to obtain

    det C(t)
      = c det(c N₀ + diag(t))
      = c [ t₁t₂t₃t₄ − c²(t₁t₂+t₃t₄) ].                         (6)

For the R284AB/AG gated bidirectional-feedback Port complement

    A_Port(t) = [ [I−δJ, −C(t), 0],
                  [−δJ,  I−δJ, −gI],
                  [−gI,     0,    0] ],

Schur elimination proves det A_Port(t)=(-1)^5 g^10 det C(t). The associated nonnegative feedback weights are strictly row-substochastic and its internal A/B feedback graph is strongly connected. Thus the cancellation gap survives as an exact, positive-core, stable auxiliary Port observer. The claim is algebraic and does not introduce a new native heartbeat evolution or an actual BRC–Shor arithmetic result.

## 4. Reproducible finite verification

Program: R284AH_cycle_packing_cancellation_checker.py (Python 3 standard library, Fraction and exact Bareiss). Execute it with Python 3; it emits JSON on stdout. Evidence: R284AH_exact_verification.json.

Actual author-run checks, 2026-11-19:

- **4,096/4,096** labeled simple directed graphs on four vertices: exact graph bound, SCC degree additivity, and equality of independent exhaustive and assignment-DP cycle packing implementations.
- **675/675** graphs with no even directed cycle: equality ν=q−p.
- **327/4,096** graphs exhibit strict cancellation gaps under 0/1 weights; maximum observed gap is 2. Degree histogram: 0→1104, 1→1452, 2→997, 4→543.
- **108** seeded 5–7-vertex signed integer matrices satisfy graph bound and SCC factorization. **324** exact minors match an independent permutation determinant implementation.
- **243** four-vertex rational pencil evaluations match the closed formula. **4** positive five-channel cores and complete 15×15 Port complements satisfy the exact determinant identity.
- Direct-sum gap for b=1,…,8 follows from the proved block-product formula; those runs are **not** an exhaustive enumeration of all high-dimensional minors.

These computations corroborate the finite claims and the implementation; AH1–AH5 rely on the proofs above. Independent mathematical review is pending.

## 5. Remaining problem

Develop a *compact exact signed cycle-cover pairing certificate* inside a nontrivial SCC, identifying an involution or weighted symmetry that forces all maximum-cardinality principal minors to cancel without enumerating all subsets. Compare precision/bit cost against R284Y minor enumeration and R284AE graded Schur recursion. Preserve the separately named edits, signs, path identities, and future-observer scope.

**Source and status:** Frozen P000 and ACTIVE X6 Heartbeat worldview are used as project premises. This matrix observer remains a separately typed auxiliary model. Portable-source publication is distinct from Task ownership, Activity linkage, formal Result and Review; no reviewer independence is asserted.
