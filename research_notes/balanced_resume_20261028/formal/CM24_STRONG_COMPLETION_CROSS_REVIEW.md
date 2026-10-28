# Distinct-reader cross-check of the CM24 strong-completion result

Reviewer: EM-DIRECT-099801. Activity: RA-BALANCE-FORMAL-20261028-099801.
Date: 2026-10-28 (Asia/Shanghai).

Disposition: LOCAL_NONAUTHOR_PAPER_CHECK_NO_MUSTFIX_FOUND, at the exact stated
inherited Frobenius interface. This is a research review contribution, not a
Driver review, formal acceptance, Task closure, or theorem promotion.

## Exact object and actual reading

I read the entire frozen author paper
`cm/CM24_STRONG_COMPLETION_NONCLOSED_RANGE.md`, 13,584 UTF-8 bytes,
SHA256 b19248580b174c7ce6aaacc453ab777f7c81f8ec820a5c153c4acd1cc2dca1e0,
Git blob dad756a3bfaa7e8edb7f0fd58a5c367743447d98.

I also read all 328 lines of the actual prior integral-weak source, restored
from the author's saved actual connector response:
`cm/strong_torsion_source.md`, 15,655 bytes,
SHA256 087bfc6a67f95912050fdef992cde596a5d905e8e23095172ba4e284415b0fdd,
Git blob 58ec6ce156797557758cd868d21bcaf2c4b4776c.
Its immutable locator is commit
56f5938da3f707c1d9db1b39afde124eac4634e3,
`research_notes/owner_goal_20261017/cm24_integral_weak_primitive_denominators_cf1677/ACTUAL_INTEGRAL_WEAK_COKERNEL_UNBOUNDED_P_TORSION_AUTHOR_COMPOSE_V1.md`.

The matched earlier nonauthor review and the original canonical Frobenius
paper are cited premises of the present author paper. I did not independently
reconstruct the full Frobenius construction or re-adjudicate its old review.
My assessment explicitly uses the literal inherited identities
L(u_n)=p^n b_n, integral u_n and b_n, and the exact unit leading coefficient of
the second infinity component for every n. The original source actually
states and proves those interfaces in sections 3--5; they were not inferred
from a determinant or a six-dimensional quotient summary.

## Independence and semantics

I did not participate in the CM author's construction, suggest its proof, or
review an intermediate version. The request arrived after the indicated byte
freeze. I inherited the owner's common monthly/control context and the task
title, and subsequently received the complete frozen proof and its dependency.
Thus this is a distinct-author, source-exposed review with shared control
context, not clean-blind review. Root supplies no mathematical vote.

The P000/Heartbeat signed-six-axis/no-native-plane rules remain fixed. This is
an external nonarchimedean module model; no physical or native geometric law
is inferred. The strong completion is not silently identified with an annular
analytic ring or a formal Laurent ring.

## 1. Laurent ambient field and actual-completion injection

For E0 the negative coefficient tail tends p-adically to zero while all
coefficients lie in O. At each p^n reduction only finitely many negative
coefficients remain; positive coefficients are unrestricted formal power
series. This is exactly lim_n (O/p^n)((z)), including the compatibility of the
inverse-system coefficients. Product coefficients converge because for each
fixed sum index, at either infinite end one factor is in its negative tail.

Reduction gives k((z)). If an E0 element has nonzero reduction, lift the inverse
Laurent series from k((z)); the product is 1 plus an element in pE0. The
p-adically convergent geometric correction is an inverse. Every nonzero
element has a finite minimal coefficient valuation and is a power of p times
a unit. This verifies the complete DVR and fraction-field claims. It does not
require a finite residue field.

The finite-level evaluation of A/p^n is injective: a polynomial in z^-1 has
unique coefficients even over the ring O/p^n, and the two localized
denominators evaluate to units. Hence a localized element can map to zero only
if its numerator did. Passing to the inverse limit is injective. The standard
identification Ahat/p^n Ahat=A/p^n A applies here because A is a localization
of a finite-type algebra over the noetherian DVR O; equivalently it follows
from the compatible p-adic presentation. This also pays the exact lattice
valuation, not merely an injective map after inverting p.

The old weak presentation is p-adically convergent on these generators.
Reducing modulo any p^n leaves finitely many terms, so its E0 coefficients
agree with its inherited annular coefficients. The proof makes no unsupported
analytic-annulus claim for arbitrary strong elements.

## 2. Constants and finite strong horizontal space

Termwise d/dr=-z^2 d/dz preserves the negative-tail condition and is bounded:
integer multipliers have p-adic absolute value at most one. In characteristic
zero its kernel on E consists exactly of the exponent-zero coefficients K.
There is no extra constant-field ambiguity in the field extension used here.

For a homogeneous rank-two differential system over this differential field,
K-independent solutions are E-independent. I checked the minimal-dependence
argument: normalize one coefficient, differentiate, cancel the common matrix
term, and use minimality to force each remaining coefficient derivative to
vanish. Thus the coefficient relation is already over K. Consequently
dim_K H<=2 is justified. Crucially, the proof does not reuse weak kernel-zero
as if completion preserved it.

## 3. Approximate-horizontal rows are independent modulo p

The inherited second component has smallest exponent 1-p^n and a unit
coefficient beta^n; the remainder has no smaller exponent. In a finite linear
relation among the reductions, the greatest n with nonzero scalar coefficient
has an exponent below every earlier row's smallest exponent. It cannot cancel.
Thus the entire family, and every tail of it, is k-linearly independent.

The finite-level injectivity above transfers that independence to X0/pX0.
It also gives ||u_n||=1, while integrality of b_n gives
||L(u_n)||<=|p|^n. No assertion that ||b_n||=1 is needed.

## 4. Closed-range contradiction survives the kernel ambiguity

X=Ahat[1/p]^2 is Banach in the lattice norm: a Cauchy sequence is bounded and
one p-power scales its tail into the complete lattice. D is integral and
d/dr preserves the lattice, so L is bounded. If the range were closed,
the induced bijection X/H -> L(X) would be a bounded map of Banach spaces,
and the nonarchimedean open-mapping theorem gives
dist(x,H)<=C||Lx||. This theorem applies over the complete nontrivially valued
field K; compactness of the unit ball is not used.

For large n, choose h_n in H at distance strictly below 1 from u_n. The
discrete lattice norm makes u_n-h_n an element of pX0, and ultrametricity puts
h_n in H0=H intersect X0. The image of H0 modulo p has dimension dim_K H:
finite-dimensional norm equivalence traps H0 between scaled free lattices;
the DVR is noetherian, so H0 is finite free of the same rank; and saturation
H0 intersect pX0=pH0 follows by dividing an element of H by p.

This puts an infinite independent residue tail inside a space of dimension at
most two, which is impossible. The argument does remove the entire possible
strong horizontal kernel, rather than assuming it is zero or using individual
p-primitivity as a substitute for independence.

## 5. Infinite algebraic cokernel is not inferred from topology alone

A nonclosed subspace can in general have finite algebraic codimension, so the
separate bounded-operator lemma is essential. I independently checked it as
used here. If range L has finite codimension d, add representatives y_1,...,y_d
and form the bounded surjection T:X direct-sum K^d -> X. Open mapping gives
preimages whose product norm is bounded by a fixed multiple of the target
norm. The K^d coefficient of a preimage is unique, since the y_i are independent
modulo range L. That uniquely defined linear coordinate map is therefore
bounded, and its kernel range L is closed. This contradicts section 4.

Thus algebraic codimension is infinite. Non-Hausdorffness follows from
nonclosedness. A map from the inherited six-dimensional weak cokernel cannot
surject onto this strong cokernel. The proof correctly withholds conclusions
about the separated quotient, kernel of the comparison, and an explicit input
outside the strong image. In particular the old b_n are already weak-exact,
so presenting one of them as an explicit nonexact witness would be wrong;
the author explicitly avoids that mistake.

## Outcome and evidence limits

No must-fix mathematical gap was found in the exact composition at the stated
Frobenius inputs. The proof supports the four stated bounded conclusions.
This assessment is a paper check: no Lean kernel was run, no scientific
enumeration or numerical computation was used, and no new external-source
novelty audit was performed. The byte/hash calculations bind the reviewed
object and its literal source; they are not mathematical validation by
themselves.

Recommended harvest: RESULT_ONLY_STANDARD_COMPOSE with the exact ring, rank-two
connection, finite-dimensional kernel proof, and infinite independent residue
family retained as load-bearing assumptions. It must not be advertised as a
general assertion that every strong completion has infinite-dimensional
cohomology. The remaining kernel, separated quotient, comparison kernel and
explicit-cokernel-source questions stay open.

Researcher-ID: EM-DIRECT-099801 / TASK_RESEARCH
