# R762HX — Exact six-saddle local limit for signed Port/BRC return

Date: 2026-11-21. Scientific status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. Research scope: six-axis **composite Port candidate** of RS-X6-TRIADIC-CLOSURE-DYNAMICS. Frozen science: enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Predecessors: R762HU@0e5a7b56c7a3c00907b6cdd0c844c6f85e4de02c (Gram counts), R762HV@30d6ed3e00f11ad5de23424a4fc1d7749f26e16e (parity spectrum), R762HW@5ac0525e4a7661b16a55fc4ea1c3e164a8d246ba (strict parity surplus). No primitive TRIADIC_CLOSURE_E, Foundation, Result, Review or native PROGRESS assertion.

## HX1: exact local limit constant

Let X={0,1,2,3,4,5}, P be its fifteen two-element subsets, and p→q be a legal Port transition when |p∩q|=1. Each transition carries its ordered provenance, triple support S=p∪q, and an independently selected sign ε∈{−1,+1}, giving displacement εh_S where h_S=Σ(i∈S)e_i in Z^6. Denote by K_m(p) the positive integer number of these labeled m-step sources from p back to p with zero total signed six-axis displacement. Each Port has eight adjacent successor Ports and two signing choices per transition.

**Theorem.** For every root p and every odd m, K_m(p)=0. Along even m→∞,

\[
\boxed{K_m(p)=\frac{10\sqrt5}{27\pi^3}\frac{16^m}{m^3}\left(1+O(m^{-1})\right).}
\]

The asymptotic leading constant is universal over all fifteen roots.

### Proof: exact BRC generating operator

Set B(θ)_{pq}=cos(〈θ,h_{p∪q}〉)/8 for adjacent distinct Ports, and zero otherwise, with θ∈(R/2πZ)^6. This is the characteristic-function transfer matrix of the positive signed-path count after normalization by 16 per step: each of the two ± source branches contributes exp(±i〈θ,h〉)/16. Therefore the following is an *exact* extraction identity:

\[
K_m(p)=\frac{16^m}{(2\pi)^6}\int_{[0,2\pi]^6}(B(\theta)^m)_{pp}\,d\theta. \tag{1}
\]

This signed Fourier integrand is a derived projection only; the BRC source mass itself is a nonnegative integer. Each event changes the sum of all six coordinates by ±3, so odd m cannot return to zero.

### Proof: all unit-modulus points

Let A be the adjacency matrix of the line graph of K_6 on P. It is connected and 8-regular. Since |B(θ)_{pq}|≤A_{pq}/8, an eigenvalue of modulus 1 can occur only if every edge has |cos〈θ,h_S〉|=1, and its edge sign is a vertex gauge ±1 times a global sign λ=±1. The equality case follows by propagating the equality in the triangle inequality through the connected regular graph. In particular the phases must satisfy 〈θ,h_S〉∈πZ for **every** one of the twenty triples S.

Taking differences of two triples with two axes in common shows θ_i−θ_j∈πZ for all axes i,j. Consequently θ_i=α+πb_i (mod 2π), with b_i∈{0,1} and 3α∈πZ. For every triple S, its three edges form a triangle of Port vertices, all with the common edge sign σ_S=cos〈θ,h_S〉. The product of those three edge signs is σ_S; for a gauged global-λ adjacency matrix it must be λ. Thus σ_S is identical for all triples. Comparison of triples differing in one axis forces all b_i equal modulo 2. Hence all six θ_i are equal modulo 2π. There are exactly six possibilities:

\[
\boxed{\theta^{(j)}=(j\pi/3)\mathbf 1,\quad j=0,\ldots,5.} \tag{2}
\]

Conversely each is an actual unit-modulus point, with B(θ^(j))=(-1)^j A/8. No other point is dominant. The exact spectrum of A is 8 (simple), 2 (multiplicity five), and −2 (multiplicity nine), so a unique simple dominant eigenvalue is isolated near each point and a uniform spectral gap holds off their neighborhoods.

### Proof: six Gaussian contributions

Write θ=θ^(j)+u. Cosine is even about each dominant point. Analytic symmetric-matrix perturbation about the normalized constant Perron vector gives the unique dominant eigenvalue and its root diagonal spectral projection:

\[
\lambda_j(u)=(-1)^j\bigl[1-\tfrac12u^T\Sigma u+O(\|u\|^4)\bigr],
\qquad \Pi_j(u)_{pp}=\tfrac1{15}+O(\|u\|^2). \tag{3}
\]

Each of the twenty triple supports occurs precisely six times among the 120 ordered Port edges. Thus Σ is the covariance per step with independent mean-zero sign, or equivalently E(h_Sh_S^T) for uniformly distributed three-subsets S. The diagonal is P(i∈S)=1/2; the off-diagonal is P(i,j∈S)=1/5. Therefore

\[
\Sigma=\tfrac3{10}I_6+\tfrac15\mathbf1\mathbf1^T,\quad
\det\Sigma=(\tfrac3{10})^5\tfrac32=\tfrac{729}{200000},\quad
\sqrt{\det\Sigma}=\tfrac{27}{200\sqrt5}. \tag{4}
\]

It is positive definite. For even m, (-1)^(jm)=1 at all six points. Six-dimensional stationary-phase/Gaussian integration in (1), using the even Taylor remainders in (3), gives

\[
K_m(p)=16^m\frac6{15}\frac1{(2\pi m)^3\sqrt{\det\Sigma}}
\bigl[1+O(m^{-1})\bigr]
=\frac{10\sqrt5}{27\pi^3}\frac{16^m}{m^3}
\bigl[1+O(m^{-1})\bigr].
\]

The 6-dimensional Fourier torus and Gaussian are exact/asymptotic mathematical *observers* of the discrete count, not additional physical axes or a continuum ontology. Full Port history, ordered source identity and six-axis displacement are retained before applying the zero-return observer.

## HX2/HX3: conditional populations

R762HV gives the exact unsigned rooted Port count P_m(p)=(8^m+14·2^m)/15 for even m. Since every unsigned walk has 2^m signing sources, the conditional zero-displacement probability among signings of rooted Port loops is

\[
\boxed{\frac{K_m(p)}{2^mP_m(p)}=\frac{50\sqrt5}{9\pi^3}m^{-3}(1+O(m^{-1})).} \tag{HX2}
\]

Let E_m(p) be the number of these rooted Port loops with all six support occurrences even. R762HV/HW established E_m/P_m→1/32 exponentially. Zero signed displacement requires every support occurrence total to be even, so the conditional signed-return probability among parity-eligible walks is

\[
\boxed{\frac{K_m(p)}{2^m E_m(p)}=\frac{1600\sqrt5}{9\pi^3}m^{-3}(1+O(m^{-1})).} \tag{HX3}
\]

HX2 and HX3 count pairs (walk,sign assignment) with uniform signs, not the fraction of individual walks possessing at least one signing. Neither formula resolves the histogram-level existence question.

## Exact finite verification

The accompanying independently implemented R762HX_CHECK.py re-evaluates the positive integer BRC half-path Gram kernel at m=0,2,4,6,8,10 and obtains K_m=1,16,624,34688,2413424,200986368; corresponding half-path endpoint/displacement fiber counts 1,16,193,1980,15909,92556. Every half-path layer sums to 16^r. It also checks the directed Port support frequencies and evaluates all 6^6=46,656 assignments of sixth-root coordinate phases: 192 have |cos|=1 on every triple, exactly six have the triangle-gauge-compatible constant sign, and all six have equal coordinates.

The discrete sixth-root census confirms the finite candidates only; the proof above establishes there are no other torus peaks. Finite BRC counts validate specific integers, while the all-length asymptotic and O(m^-1) depend on the analytic proof. Independent math review remains NOT_REVIEWED.

## Next precise scientific question

Determine whether some all-even six-axis support histogram n has a **connected rooted Port-Euler realization** N_p(n)>0 but no zero-displacement signing C(n)=0. The exact histogram factorization J_p(n)=N_p(n)C(n) and local-limit density must be retained as distinct observations: a large total K_m does not prove signability of every individual eligible histogram. Explore minimum length and structural obstructions with an order/provenance-preserving BRC carrier; maintain native TRIADIC_CLOSURE_E lift as the mother question.
