# Composite membership-or-factor: antecedent match and exact reuse boundary

2026-10-28 (Asia/Shanghai). Researcher `EM-NT-EFC4A8`.

Status: `BOUNDED_DIRECT_TASK_RESEARCH / PRIMARY_SOURCE_MATCH / REUSE_NO_NEW_ALGORITHM`. This is an author-side interface analysis for later nonauthor review, not a formal Task result, Driver decision, or Working Truth update. The live formal Task/owner inventory is UNKNOWN. No formal core was claimed or executed, no old extractor or fixture was rerun, and no new scientific code was run.

## Result that changes the research route

The composite-modulus algorithmic core already has a direct antecedent: Bartosz Źrałek, *A deterministic version of Pollard's p−1 algorithm*, author version [arXiv:0707.4102v5](https://arxiv.org/pdf/0707.4102v5), 12 May 2009, §4, pp. 5–6, Theorem 4.2 and Corollary 4.3. The associated publication is *Mathematics of Computation* **79** (2010), 513–533, [DOI 10.1090/S0025-5718-09-02262-5](https://doi.org/10.1090/S0025-5718-09-02262-5). The publisher PDF request returned HTTP 403; the actual mathematical text read was the pinned author v5, not an asserted byte-identical journal PDF.

In that text, n is odd. Theorem 4.2 treats two units with known prime-power orders and attempts digit recovery using gcd tests. Failure to obtain a proper divisor establishes cyclicity. Corollary 4.3 extends generator-or-divisor extraction to any finite supplied set with factored element orders. The proof's successful branch determines the exponents. Its scope already includes prime-power CRT factors and more than two distinct primes. This is a direct composite antecedent, beyond merely naming ordinary Pohlig–Hellman. The author's [2014 exposition](https://sbn.wat.edu.pl/pdf-135229-63545?filename=A-GENERALIZATION-OF-THE-P.pdf), §3, pp. 179–180, also presents the binary case and general statement; it was used to locate the earlier work.

Consequently, neither a new composite extraction algorithm nor an arbitrary-odd-modulus generalization should be opened from this packet. The useful delivery is the following explicit input reduction and separation of output meanings. It makes no global earliest-priority or exhaustive-literature claim.

## Existing internal source and input typing

The target is `RSA_DYADIC_MEMBERSHIP_DERIVATION.md`, 8,515 bytes, SHA256 `02523e710e3875eafa3e57551bc46111a1937839c345ff5af03fd2450af8d220`, preserved inside `RSA_TOOLS_COMPLETE_ORIGINALS_CAPSULE.json` at commit `56f5938da3f707c1d9db1b39afde124eac4634e3`; exact capsule path is in `primary_sources.json`. Its antecedent return and authorship remain unchanged. The earlier comparison `../rsa_prior_art_boundary.md` established only the ordinary cyclic digit-lifting match; the present note supplies the missing composite antecedent.

Assume public n is odd with n ≥ 3, and a nonempty finite list of public units x_i modulo n with positive integers Δ_i satisfying x_i^Δ_i = 1. These are supplied valid collisions, not data generated from n alone. Validity, positivity, and unit conditions can be checked; a false certificate is rejected. Define

\[
 L=\operatorname{lcm}_i\Delta_i=2^s u,\qquad u\text{ odd},\qquad y_i=x_i^u.
\]

The factorization of n is used only in the proof below, not supplied to the extractor. No factorization of u, L, or Δ_i is assumed. The ordinary arithmetic cost of constructing L, modular exponentiation, and checking inputs remains paid. Polynomial dependence is on the supplied transcript size, log n and log L; nothing here bounds the cost of obtaining that transcript.

## Reduction to the antecedent's known-order input

Let H = ⟨x_i⟩ and let H₂ be its Sylow-2 subgroup. Since the exponent of H divides L, the odd-order component of H is killed by raising to u. On H₂ that same operation is an automorphism because u is odd. Thus ⟨y_i⟩ = H₂ and y_i^(2^s) = 1.

For each y_i, repeated squaring finds its first power equal to 1 and hence its exact order 2^(t_i), with 0 ≤ t_i ≤ s. This supplies a *complete factorization* of the relevant element order without factoring any odd integer. Identity elements have t_i = 0 and can be omitted from a nontrivial instance; if all elements are identities, the trivial membership certificate is immediate.

For the remaining elements, choose a supplied g of maximal order 2^t. To apply Theorem 4.2 use the paper's prime parameter equal to 2, its first base a = g, and its second base b = y_i, with their computed depths. (The paper's prime parameter and this note's exponent s are different variables.) In a cyclic 2-group, a maximum-order supplied element generates the group: the group order is the maximum of the generator orders. Consequently successful pairwise digit computations give y_i = g^(e_i), with 0 ≤ e_i < 2^t. This is a specialization of the cited method, not an additional discrete-log oracle.

The stored exponent list is an explicit public certificate. Recording the digits computed by an algorithm and subsequently checking their exponentiations is an output-format refinement, not evidence for a new extraction algorithm. This match is a mathematical parameter reduction; it does not assert byte-level equivalence, identical stopping order, identical factors, or identical operation counts for the two implementations.

## Cyclicity and the graph barrier are different interfaces

Write n = ∏_(j=1)^k p_j^(a_j), for distinct odd primes, only for proof purposes. Let π_j be reduction to the j-th prime-power unit group. For a 2-subgroup K of the units modulo n, the following are equivalent:

1. Every restriction π_j|K is injective.
2. K is cyclic and either K = {1}, or its unique involution is the global residue −1 modulo n.
3. Either K = {1}, or there is a generator g of order 2^t, t > 0, with g^(2^(t−1)) = −1 modulo n.

**Proof.** Each unit group modulo an odd prime power is cyclic. If every π_j is injective, K embeds in one of these cyclic groups, so K is cyclic. For nontrivial K, its unique involution must project to the unique element of order 2 in every coordinate, namely −1. This proves 1 ⇒ 2, and 2 ⇒ 3 is the elementary description of the involution of a cyclic 2-group. Conversely, in 3 the order of π_j(g) divides 2^t but does not divide 2^(t−1), since its half-power is −1, distinct from 1 at every odd prime power. It is therefore exactly 2^t, so each projection has trivial kernel. The trivial K case is immediate. ∎

For k = 2, condition 1 is precisely that K is a graph of an isomorphism between its two projection images. For arbitrary k it means that K maps isomorphically to each image; these are linked images, not independent CRT coordinates. This elementary equivalence supplies the interpretation of the existing certificate. It is not claimed as a new general theorem family.

Cyclicity alone does not establish condition 1. For example, modulo 15 the cyclic subgroup ⟨4⟩ = {1,4} has trivial projection modulo 3 and order-2 projection modulo 5. Its involution 4 is neither 1 nor −1 modulo 15, and gcd(4−1,15) = 3. Thus a generator-or-factor routine may validly return a generator on an input where the stricter graph-or-factor interface must split. The existing preliminary root check or the same half-order check applied to the returned generator supplies exactly this missing condition. No collision search is supplied by this check.

More explicitly, once a generator g of a nontrivial cyclic K has been certified, set z = g^(2^(t−1)). Then z² = 1. At each odd prime power z is 1 or −1, because p_j cannot divide both z−1 and z+1. If z is not the global −1, and has order 2, both signs occur. Therefore

\[
 d=\gcd(z-1,n)=\prod_{j:\;z\equiv1\pmod{p_j^{a_j}}}p_j^{a_j},\qquad 1<d<n.
\]

This returns a proper divisor formed from whole prime-power CRT blocks. It need not return a prime: modulo 45, z = 19 satisfies z² = 1, is neither 1 nor −1, and gcd(18,45) = 9. If n is a single odd prime power, every 2-subgroup already satisfies the equivalent conditions, so this square-root mechanism cannot split it. For instance the supplied collision (x,Δ) = (2,6) modulo 9 gives u = 3 and y = 8 = −1. A positive membership certificate therefore proves neither primality of n nor impossibility of factoring it by other means.

The original internal output also carries the nontrivial root, which the abstract statement of Corollary 4.3 does not demand. This format can be preserved in the dyadic specialization: check the base half-power first; after it is −1, a digit residual r with r^(2^(t−k)) = 1 gives w = r^(2^(t−k−1)) and w² = 1. A failed ±1 digit comparison records this w together with gcd(w−1,n). Thus the root witness remains public. This observation matches the already-written internal invariant; it is not a claim that every black-box generator-or-factor implementation automatically emits that witness.

## Reusable outcome and remaining obligations

The reusable interface is `supplied valid collision list → known dyadic orders → classical composite PH + global involution check → proper divisor OR explicit all-projection-injective cyclic certificate`. The certificate proves a barrier for this supplied subgroup and observer, not for arbitrary later generators. The dyadic part is retained for the stated square-root splitting mechanism; no equivalence for unrestricted odd-order information is asserted. This is external classical modular arithmetic. It neither supplies a native X6 readout bridge nor changes the fixed no-plane X6 semantics.

No success-probability improvement, new collision-generation method, factoring breakthrough, or correction to the already-fixed PCF7 zero branch follows. The prior paper's deterministic Pollard p−1 applications have separate smoothness hypotheses; they are not imported as an unconditional way to produce these collisions from any n.

The remaining program-level obligations are exact current formal Task/owner verification before formal intake, a nonauthor review of this parameter mapping and certificate interpretation, and any separately specified collision-generation problem. A bounded antecedent match is now established; an exhaustive originality audit and formal acceptance are not asserted. Parent Source publication and exact readback are required before calling this a persisted research checkpoint.

Researcher-ID: EM-NT-EFC4A8 / TASK_RESEARCH
