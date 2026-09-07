# #1162 — q-chain Schur elimination, alias Markov gauge, and finite-time provenance stabilization

Status: RESEARCH_NOTE / DURABLE FRONTIER / NOT PROMOTED
Researcher-ID: EM-DIRECT-B62D
Research-Mode: TASK_RESEARCH
Progress-Event-ID: 1162-q-chain-markov-gauge-stabilization-20260908
At: 2026-09-08T00:30:00+08:00
Parents:
- `research_notes/1162_alias_fiber_resolvent_brc_20260907.md`
- `research_notes/1162_alias_boundary_renyi_observer_lattice_20260907.md`
- `research_notes/1162_physical_schur_pi_free_determinant_20260908.md`

## 1. q>2 physical elimination: Chebyshev as a continuant output

Let g=(qN)^2 and y=1+u/(2g). Divide A_(qN)+uI by g and retain every q-th vertex. Each interval between retained ports contains q-1 hidden vertices with tridiagonal block

T_r(y)=tridiag(-1,2y,-1), r=q-1.

Its determinant D_r satisfies

D_0=1,
D_1=2y,
D_r=2y D_(r-1)-D_(r-2).

Thus `D_r=U_r(y)` by the standard Chebyshev name, but the recurrence/continuant is the primitive finite object.

The hidden-block inverse endpoint entries are

(T_(q-1)^(-1))_(1,q-1)=1/U_(q-1)(y),
(T_(q-1)^(-1))_(1,1)=U_(q-2)(y)/U_(q-1)(y).

Therefore the physical Schur complement is

Schur(A_(qN)+uI)
=
[q^2/U_(q-1)(y)]
[A_N+2N^2(T_q(y)-1)I],

where the second continuant combination is

T_q(y)=yU_(q-1)(y)-U_(q-2)(y).

This proves the earlier Chebyshev resolvent map entirely by finite path elimination; no Fourier diagonalization or microscopic derivative is needed.

## 2. Root-of-unity finite branch probabilities

For the normalized finite cycle spectrum write

x_(N,k)=1/[N^2 |1-omega_N^k|^2],
omega_N=exp(2pi i/N).

A q-refinement child is

z_r=omega_(qN)^(k+rN),

so z_r^q=omega_N^k. Its mass ratio is

p_r=x_(qN,k+rN)/x_(N,k)
=|1-z_r^q|^2/[q^2 |1-z_r|^2].

Using the finite geometric sum,

p_r=|(1/q) sum_(j=0)^(q-1) z_r^j|^2.

The q values z_r differ by q-th roots of unity, so finite DFT Parseval gives sum_r p_r=1. This is a purely finite root-of-unity proof of alias mass conservation. Complex phase is used only to prove the positive weights; after squaring, phase-sensitive information is not claimed to survive in the positive BRC carrier.

The same probabilities are normalized samples of the Fejer/Dirichlet leakage kernel. The DFT/Parseval mechanism itself is classical prior mathematics.

## 3. Gauge / Doob form

For theta in (0,1) define

g(theta)=csc^2(pi theta).

The finite multiplication identity is

(1/q^2) sum_(r=0)^(q-1) g((theta+r)/q)=g(theta).

Thus the raw equal branch weight 1/q^2 (total raw mass 1/q) becomes a probability by the positive gauge

p_r(theta)=(1/q^2) g((theta+r)/q)/g(theta).

Along depth m, Q=q^m,

p_(Q,a)=Q^(-2) g((theta+a)/Q)/g(theta),

so the gauge telescopes. In probability terminology this is the Doob-h transform of the uniform substochastic preimage kernel, with g as the harmonic gauge. In project BRC terminology this is a positive gauge normalization pattern. The weights are generally cyclotomic/algebraic, not positive rationals, so the current finite-rational gauge implementation is not claimed to execute this Fourier carrier directly.

## 4. Markov eigenfunctions and genuine martingales

Let P_q be the positive Markov operator

(P_q f)(theta)=sum_r p_r(theta) f((theta+r)/q).

For s>1 and orientation parity a in {0,1}, define the alias-boundary observable

H_(s,a)(theta)
=
E_theta[sgn(L+theta)^a |L+theta|^(2-s)]

where L is the integer alias boundary variable. Classical compatibility gives

H_(s,a)(theta)
=
[sin^2(pi theta)/pi^2]
[zeta(s,theta)+(-1)^a zeta(s,1-theta)].

The discrete boundary scaling alone gives

P_q H_(s,a)=q^(s-2) H_(s,a).

Hence along the actual refinement chain theta_m,

q^(m(2-s)) H_(s,a)(theta_m)

is a genuine martingale with an explicit common probability space and nested filtration.

At s=2 no scale normalization is required. H_(2,0)=1 identically, so the Basel channel is the constant harmonic observable of the alias probability tree.

## 5. Ordinary boundary vs blow-up alias boundary

If one observes theta_m only in the compact interval [0,1], refinement mass concentrates at endpoints 0 and 1. Their probabilities are

P(0)=sin^2(pi theta)/pi^2 * zeta(2,theta),
P(1)=sin^2(pi theta)/pi^2 * zeta(2,1-theta).

The arithmetic alias is not destroyed in the full carrier. It survives in the endpoint blow-up coordinates:

left: Q theta_m-theta -> ell>=0,
right: Q(1-theta_m)-(1-theta) -> ell>=0.

Thus collapsing to the geometric endpoint without the blow-up coordinate discards the integer alias provenance. This is the finite-resolution reason not to replace the lost label by unstable microscopic differentiation.

## 6. Almost-sure finite-time provenance stabilization

At depth m the exact branch history is the integer

a_m=r_0+r_1 q+...+r_(m-1) q^(m-1).

A nonnegative boundary alias ell has a finite base-q expansion and thereafter all new digits are 0. A negative alias uses the complementary representation and thereafter all new digits are q-1.

Since the boundary measure is supported entirely on integer aliases, the refinement path almost surely becomes endpoint-only after a finite random depth T.

The alias tail p_ell(theta)=sin^2(pi theta)/[pi^2(ell+theta)^2] gives

P(T>m)=O(q^(-m)),

and in particular E[T]<infinity. Hence arithmetic provenance is revealed by finite integer digits and almost surely stabilizes; it is not encoded in an infinitesimal derivative.

## 7. Dirichlet L readout without holonomy differentiation

Let chi mod d be a real Dirichlet character with chi(-1)=(-1)^a. Start the positive alias tree from each coarse residue phase theta_b=b/d, b=1,...,d-1. Then for s>1,

L(s,chi)
=
pi^2/(2d^s)
sum_(b=1)^(d-1)
chi(b)/sin^2(pi b/d) * H_(s,a)(b/d).

This is a boundary expectation of integer residue/orientation/magnitude labels. The Hurwitz expression is merely the classical name of the same boundary sum. No high-order holonomy differentiation is required.

This further downgrades the previous claim that parity-mismatch L-values require A^(-1/2) as a native carrier. A^(-1/2) remains a valid conditional analytic/readout construction after provenance collapse, but if integer alias labels are retained then the common positive A^(-1) mass carrier suffices for all s>1; the character observer itself can be signed and remains typed separately.

## 8. Antiperiodic zeta label moment

For theta=1/2 let K=|2L+1| be the positive odd boundary alias magnitude. Its probability distribution is

P(K=2n+1)=8/[pi^2(2n+1)^2].

Therefore for every s>1,

zeta(s)=pi^2/[8(1-2^(-s))] E[K^(2-s)].

At s=2 the random label disappears from the observable because K^0=1, giving Basel directly from probability normalization. This is the shortest observer-factorization statement of the special role of s=2.

## 9. Status / prior-art boundary

Classical components: finite DFT Parseval, Fejer/Dirichlet kernels, Doob transforms, Hurwitz multiplication formulas, Chebyshev/continuant recurrences. No novelty is claimed for those ingredients.

Candidate project synthesis: the exact alias-refinement probability carrier, rough-observer blow-up labeling, finite-time provenance stabilization, and the statement that Basel is the unique total-only member of the zeta/Hurwitz label-moment family under this carrier.

## 10. Next

1. derive explicit finite-depth character estimators and robust error bounds from centered alias labels;
2. quantify observer sensitivity when alias provenance is deliberately discarded;
3. investigate the Shannon/Renyi information revealed per refinement and its relation to zeta derivatives, keeping LOG as a derived readout only.
