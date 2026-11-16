# PREFIX-841 — Optimal one-scalar provenance coding, sharp modular alias criterion, and conditional label entropy

Date: 2026-11-16. Status: AUTHOR_PROVED / EXACT_BIGINT_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

## Provenance and declared model

Frozen input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d (unchanged). Immediate predecessor: PREFIX-840, research_notes/portable_direct/2026-11-16_r6_prefix840_one_frame_tagged_BRC_provenance_reconstruction.md at commit 248eebd980734de4241e5f3d8c4f9192e0c18554.

Use its auxiliary positive-weight, named-source BRC Q-only model. Fix p=q>=1 initially present distinct original names, removal weights w_1,...,w_p positive integers, and one initially absent marked source whose addition/removal weights are a,b>0. One step Q=R+A sums every legal weighted removal and addition of that marked source, within capacity. Time t>=1 counts formal Q steps, not physical heartbeat time. Let D_i(t) be the total positive terminal history mass with exactly original name i removed, all other original names retained, and the marked bit absent at odd t/present at even t.

As proven in PREFIX-840, there is a unique valid history in this one-deletion channel for each missing name, so

$$
D_i(t)=c_t w_i,\qquad c_t=a^{\lfloor t/2\rfloor}b^{\lfloor(t-1)/2\rfloor}>0.
$$

Assume a known a priori bound 1<=w_i<=W, a fixed public order of original names, and a provenance-sensitive readout that can return a prescribed nonnegative integer linear combination of the tagged terminal masses D_i. This observer is stronger than untagged Q occupancy totals and stronger than an interface that permits only single-name survival queries.

## Theorem 841.1 — One tagged integer, information-optimal normalized encoding

For W>=1 set S=sum_{i=1}^p W^{i-1} and read one positive integer

$$
Z_W(t)=\sum_{i=1}^p W^{i-1}D_i(t)
      =c_t\sum_{i=1}^p w_iW^{i-1}.
$$

Then

$$
U_W=Z_W(t)/c_t-S=\sum_{i=1}^p(w_i-1)W^{i-1}
\quad\in\{0,\ldots,W^p-1\}.
$$

The consecutive base-W digits of U_W are exactly w_i-1, and every ordered tuple in {1,...,W}^p occurs once. For W=1 the assignment is already determined and U_W=0.

**Proof.** Substitute D_i=c_tw_i, divide by the nonzero c_t, and subtract S. Each digit lies between 0 and W-1. Uniqueness and surjectivity follow from finite radix representation. QED.

For W>=2, a fixed-width binary representation of U_W uses exactly L=ceil(log_2(W^p)) bits, attaining the universal fixed-width lower bound from the W^p distinct assignments. The observer's raw positive mass instead has

$$
c_t S\le Z_W(t)\le c_t W S,\qquad
S=\frac{W^p-1}{W-1}.
$$

Thus the maximal raw integer requires floor(log_2(c_t W S))+1 bits; known exact quotient and offset normalization can transmit U_W using L bits. Computing Z directly still requires the named readout itself; using p separate D_i values also incurs their acquisition cost. Explicitly listing all coefficients W^{i-1} costs Theta(p^2 log W) bits for W>=2, whereas a recurrence generates them with a largest coefficient of O(p log W) bits. No time-complexity acceleration of the underlying Q evolution is asserted.

## Theorem 841.2 — Exact modular provenance-fidelity criterion

Let N=W^p, m>=1 be an integer modulus, and g=gcd(m,c_t). The residue Z_W(t) modulo m distinguishes **all** W^p labeled assignments if and only if

$$
\boxed{\frac{m}{\gcd(m,c_t)}\ge W^p.}
$$

**Proof.** From Theorem 841.1, Z_W=c_t(S+U), with U running through every integer 0,...,N-1. Two such residues coincide iff m divides c_t(U-U'), equivalently (m/g) divides U-U'. If m/g>=N, the only divisible difference in [-(N-1),N-1] is zero. If m/g<N, choose U=0 and U'=m/g, which are both valid but collide. QED.

In particular, m=W^p is a minimum-cardinality lossless modular observer exactly when gcd(c_t,W)=1. If gcd(c_t,W)>1, that modulus aliases some names. For p=2, W=2, a=2, b=1, t=2: c_t=2, m=4, and m/g=2<4. The assignments (1,1) and (1,2) have raw readings 6 and 10 and identical residue 2 modulo 4. At m=5, gcd(2,5)=1, hence m/g=5>=4 and all four assignments are separated.

A second consequence concerns finite observation precision. For W>=2 the raw codewords are c_t(S+U), so their minimum spacing is exactly c_t. If the observed real scalar has absolute error strictly less than c_t/2, nearest-codeword decoding uniquely recovers U; for adversarial real errors the threshold is sharp because neighboring error intervals meet at radius c_t/2.

## Theorem 841.3 — Exact number of conditional identity-residual bits

Suppose the unordered multiset M of p weights is already known, and each distinct value v occurs m_v times. The number of labeled assignments compatible with M is

$$
F(M)=\frac{p!}{\prod_v m_v!}.
$$

The optimal fixed-width identity side-information code needs exactly ceil(log_2 F(M)) bits. A constructive bijection is the lexicographic rank among multiset permutations.

**Proof.** With r names remaining and multiplicities m_v, let P=r!/(product m_v!). The number of admissible suffixes starting with a currently available value v is the integer P*m_v/r. At each position, sum these counts over available values smaller than the actual weight and append that sum to the running rank. Then select the actual weight, decrement m_v, and replace P by P*m_v/r. Reverse greedy selection un-ranks each integer from 0 to F(M)-1 exactly once. The pigeonhole principle gives the matching lower bound. QED.

If all weights agree then F(M)=1 and identity residual is zero bits; if all p weights differ then F(M)=p!. PREFIX-839 recovers the unordered multiset from two late untagged occupancy frames; PREFIX-840 supplies a tagged name-sensitive observer. This theorem measures the additional information content of their name assignment fiber; ranking still requires access to provenance.

## Independent exact tests

An accompanying JavaScript BigInt checker independently enumerates named-original-subset / marked-bit legal Q transitions. It extracts D_i from its complete state map and compares it with c_tw_i rather than implementing only the closed formula.

Full positional and labeled test domain: p=1..5, W=1..4, every ordered tuple in [1,W]^p, a,b=1..2, t=1..6. The program checks 7,176 configurations, 43,056 time frames, 198,864 named-channel equalities, 43,056 coded-scalar identities and 198,864 individual digit recoveries, plus 1,794 multiset rank/unrank instances. Additional sharp-modulus tests enumerate all residues for p=1..4, W in {2,3}, a,b=1..3, t=1..5, every modulus m=1..W^p+7, yielding 9,270 modular cases and 187,865 candidate residue comparisons. Result: ALL_EXACT_ASSERTIONS_PASSED. All counting arithmetic is exact BigInt.

Example: p=3, W=4, weights (1,2,4), a=b=2 and t=6 give c_t=32, S=21, U=52, Z=2336. The unconditional 4^3=64 possible assignments need 6 fixed bits, while knowing the multiset {1,2,4} leaves 3 bits (six named permutations).

## Observer boundary and next discriminating work

This paper establishes an exact **auxiliary** tagged BRC source observer, not an admissible native X6 Cell/Link/Port measurement. Raw positive history mass remains distinct from signed/phase amplitude. Name ordering, the bound W, the tagged terminal measurement and its input/output arithmetic all belong to the resource accounting. A Q-only untagged occupancy projection cannot construct Z_W: permutations of distinct original names preserve all those occupancy counts while changing Z_W.

Next investigate whether a licensed provenance-sensitive native event can realize the modular readout with m/gcd(m,c_t)>=W^p, and the least-cost fixed modulus for given a,b and an observation horizon. Retain separate open topics: q>=5,b>0 nonnegative minimal Q carrier; and a uniform O(sqrt(T)) even-time recollision resource upper bound.

Provenance status: independent auxiliary research; no shared Task CLAIM, formal Result, independent Review or Foundation admission.
