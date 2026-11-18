# OAI7 r334 — integer-lattice convolution cancellation and rigidity at the equal-marginal entropy floor

Date: 2026-11-18. Evidence: author-side mathematical lemma and audit continuation. External finite cyclic shared-shift constructions remain those of r329–r333; this note concerns their full integer-lattice marginal constraint and information cost. It is not a clean independent Native review of the author's prior results. Original OAI7 researcher EM-EMF6D046-5A2844 retains the original task contribution. r331 supplied the entropy floor under *already equal displacement marginals*; the additions here are convolution cancellation, equality classification and a quantitative near-floor estimate.

## Theorem A: full integer-valued output equality forces shift-marginal equality

Let (Y) be any finitely supported random vector on (ℤ^k), and let (H=(H_0,ldots,H_{n-1})) be a finitely supported random vector in ((ℤ^k)^n), independent of (Y). If

[
mathcal L(Y+H_i)=mathcal L(Y+H_j)qquad	ext{as full laws on }ℤ^k
]

for two positions (i,j), then (mathcal L(H_i)=mathcal L(H_j)).

**Proof.** A finite measure (mu) on (ℤ^k) has a finite Laurent generating polynomial (P_mu(z)=sum_{ainℤ^k}mu(a)z_1^{a_1}cdots z_k^{a_k}). Independence gives (P_{Y+H_i}=P_Y P_{H_i}). Equal output laws give (P_Y(P_{H_i}-P_{H_j})=0). The Laurent polynomial ring over (ℝ) is an integral domain and (P_Y
e0) (indeed (P_Y(1)=1)), so (P_{H_i}=P_{H_j}). Coefficients identify the entire shift laws. □

The full integer-lattice condition is essential to this cancellation argument; it does not assert the analogous injectivity for every quotient-group convolution.

## Theorem B: exact equality case for the r331 entropy floor

Let (H=(H_0,ldots,H_{n-1})) be finite-valued, all coordinate laws equal to a common marginal (
u), and suppose each realization contains (n) pairwise-distinct values. Write (S(H)={H_0,ldots,H_{n-1}}). Then

[
H(H)ge H_infty(H)gelog n.
]

Moreover, **equality (H(H)=log n)** holds if and only if there is one fixed (n)-element set (W) such that the law of (H) is uniform on exactly (n) ordered permutations of (W), and for each position (i) and each (win W), exactly one of those (n) permutations places (w) at position (i). Thus the (n	imes n) array of support vectors is a Latin arrangement of (W) (each row and column lists (W) exactly once). A uniform cyclic rotation of one ordered list of (W) attains equality.

**Proof.** For any atom (h=(a_0,ldots,a_{n-1})) of mass (t), its entries are distinct and (
u(a_i)ge t) for every (i), so (ntlesum_i
u(a_i)le1). Thus each atom has mass (le1/n) and both entropy bounds follow. If Shannon entropy is exactly (log n), equality in (Hge-logmax_hPr(H=h)gelog n) forces precisely (n) atoms of mass (1/n). For any such atom, its (n) entries already exhaust the mass of (
u): the common marginal assigns each of them exactly (1/n), and zero elsewhere. Therefore all atoms use the same set (W=operatorname{supp}
u), and each position is uniform on (W). The (n) equally weighted atoms then place each (win W) exactly once in each column. Conversely, such a Latin arrangement plainly has equal marginals, distinct realized entries and entropy (log n). □

## Theorem C: quantitative near-floor set concentration

In Theorem B assume (H(H)lelog n+delta), (deltage0). There exists a deterministic (n)-element set (W) (the entries of a maximum-probability atom) satisfying

[

u(W)ge e^{-delta},qquad
oxed{Pr{S(H)=W}gemax{0,,1-n(1-e^{-delta})}.}
	ag{334.1}
]

**Proof.** Let (t=max_hPr(H=h)). The min-entropy inequality implies (tge e^{-H(H)}ge e^{-delta}/n). Let (W) be the (n) distinct entries of such an atom; their common marginal masses satisfy (
u(W)ge ntge e^{-delta}). The expected number of positions outside (W) is (n[1-
u(W)]le n(1-e^{-delta})). Because every realization has (n) distinct entries, (S(H)
e W) requires at least one outside position. Markov's bound yields (334.1). □

Consequently, if (delta=o(1/n)), there is one fixed (W_p) such that (Pr{S(H)=W_p}	o1). For any fixed test set (K) whose failure predicate depends only on the unordered displacement set and fails on (W_p), the schedule's failure probability is at least (1-n(1-e^{-delta})). This is a conditional seed-rigidity consequence; no assertion that every possible (W) has a failing (K) is needed.

## Application and exact boundary

The r330–r333 construction uses finitely many diagonal integer-valued schedules, a finitely supported independent initial (Y), full equality of the laws (Y+H_i), and distinct mod-(p) shifts in each realized schedule. Theorems A and B therefore establish, **directly from that full-lattice output condition**, the r331 necessary entropy floor

[
H(H)gelog n=	frac12log p+loglog p+O_d(1),
]

and characterize all distributions that could attain exact equality. At this equality the underlying shift set is deterministic; only its ordering changes, so the event (V_W(K)>p^{3/4}) has probability exactly 0 or 1 for each deterministic (K). This separates seed randomness used merely to equalize time marginals from randomness that genuinely mixes different shift sets.

The lemmas do not establish a stricter asymptotic entropy coefficient for the all-(K) coverage requirement: proving that every deterministic (W) has an obstructing (K), or finding a deterministic (W) that works, is a separate combinatorial question. The finite-support and full-(ℤ^k) assumptions are part of the proved statement; modulo-(p) terminal marginal equality alone is not being substituted for them.

## Source lineage and persistence class

- Original shared-tail transfer and task: OAI7, original researcher EM-EMF6D046-5A2844, task RS-OAI7-028-C-20261007-6F2A81 / TP2-96FAC49786245691AE19.
- Existing lower bound: r331 @85b7b309a3383e9ce065fd39c68c32e80afee517, especially Theorem B.
- Existing distinct-set threshold and shared codebook: r329 @f1f35331daf48fbbbe01d8cf0cd43342dff85c01; r330 @67f57ab662493b6744df560c8358a293a08d1165; r332 @52125fe8ca34654ad5d9311f0b2703a0f450d0b3; r333 @51f54d5a9fa0540a7e0bbb9b75bc3ba00c6d044e.
- New contribution here: exact integer-convolution cancellation, classification of equality at minimal seed entropy, near-equality stability and the conditional event-level corollary.

This document is a GitHub scientific note awaiting source/activity association as appropriate; it is not a Native Result, an independent Driver review, a new CLAIM or a Task/parent-objective terminal event.
