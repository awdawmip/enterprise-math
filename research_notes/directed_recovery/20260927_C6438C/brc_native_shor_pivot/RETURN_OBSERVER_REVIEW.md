# Marked-return observer: shared-context symbolic review

Verdict: the proposed rank obstruction is correct in its stated fixed linear
scope. This is a shared-context mathematical review, not formal independent
admission. No scientific module, numerical example, host scientific
calculation or external query was run. The reviewed object is the
coordinator's statement in this task; no separate source-proof file was
available at the time of review.

## Assumptions and the observed sequence

Let N>=2 and gcd(a,N)=1. On a work carrier containing the modular residues,
let T send the basis vector e_y to e_(ay mod N); padding may be fixed if
specified by the native permutation contract. The orbit of the marked
label 1 has length r=ord_N(a)>=1. For m>=0,

    c_m=e_1^T T^m e_1=1 if r divides m, and 0 otherwise.

The unit assumption matters: without it, modular multiplication is not
the stated permutation and this order/return argument is not the same
claim. Any padding outside the orbit does not change the marked sequence.

Because every permutation column sums to one,

    1^T T^m e_1=1

for all m. Thus this particular total-mass scalar alone distinguishes no
orders. It does not say that the full propagated state, marked ports,
correlations, phases or other native observables lose their order
information. In particular one must not replace a marked-port contract
by total mass and then infer equivalent information preservation.

In the ring of formal power series over any field K,

    sum_(m>=0) c_m z^m = sum_(k>=0) z^(kr) = 1/(1-z^r).

The denominator has constant term one, so the formal inverse is defined
without analytic convergence or spectral diagonalization. This identity
describes the unknown order; it is not a way to supply r to a compiler or
evaluate the right-hand side at zero computational cost. An explicit
degree-r denominator or exact specialized rational value may also carry
output/representation costs that must be counted.

## Fixed linear realization lower bound

Suppose a fixed A in K^(d x d), fixed u,v in K^d reproduce the sequence:

    c_m=u^T A^m v.

The entries of A,u,v may depend on the declared N,a; the argument does
not require that they were computed efficiently, or that their entries
are nonnegative. Form H with H_(i,j)=c_(i+j), 0<=i,j<r. There is exactly
one nonzero entry in every row and column:

    j=0 for i=0, and j=r-i for 1<=i<r.

All these entries are one. H is the permutation matrix for negation
modulo r, so H is invertible and rank_K(H)=r. No distinct-root or
characteristic-zero hypothesis is needed: its determinant is +1 or -1,
which remains nonzero in every field, including characteristic two and
characteristics dividing r. The possible failure of a roots-of-unity
diagonalization in such fields is irrelevant to this proof.

On the other hand define O_(i,:)=u^T A^i and C_(:,j)=A^j v. Then

    H=OC,     rank_K(H)<=d,

and therefore d>=r. For r=1, H=[1], so the same argument gives d>=1;
there is no empty or exceptional rank-zero realization.

In fact only agreement for 0<=m<=2r-2 is needed to fill this particular
Hankel block. The infinite-sequence contract implies that finite-prefix
agreement, but the proof does not impose d>=r on every shorter or
otherwise restricted set of observation times. If a finite observation
horizon includes 0..2r-2 with the same fixed A,u,v, the lower bound does
apply. Heterogeneous time-dependent transitions are a different model.

The statement applies over Q, R or C and to a positive-real linear BRC
realization as a special case. Signs or complex amplitudes cannot defeat
this fixed-realization rank bound. It is not a general rank theorem for
an arbitrary semiring without field linear algebra. A finite-field
algebraic statement does not itself give the field a physical probability
interpretation.

## What this does and does not rule out

This rules out an exact fixed low-dimensional linear state and fixed
linear readout representing the complete marked-return sequence when
r exceeds that dimension. It does not rule out a succinct description of
an exponentially large linear operator, a nonlinear or adaptive encoding,
time-dependent circuits, a more limited finite-horizon contract, controlled
approximation, or a direct factor-producing algorithm. Such alternatives
still need their own construction and resource proof.

In particular an n-bit work-label register can describe 2^n distinct
basis states. A compact native description of modular multiplication is
not a d=n linear realization of its marked-return sequence. Equating
description length with unfolded linear dimension would misapply this
obstruction. The proof is neither an impossibility result for BRC itself
nor a lower bound for every Shor-relevant observable or sampling task.

## Native continuation

The next target should be a sufficient native instrument, not reconstruction
of every c_m. Specify the output that is sufficient for the decoder—such
as a complete measured phase bitstring with a stated distribution-error
or factor-success contract—and retain the work/port information necessary
for that contract. Total mass alone is inadequate; the full return-series
oracle is stronger than the requested output and has the obstruction above.

A concrete next interface is compositional: source-certified native modular
permutations for the required powers, chronological controlled native phase
words, and a measured-output instrument with exact or certified-error
composition. Modular powers must come from declared actual arithmetic;
order r, its odd part, factors, and discrete-log addresses must not be
silently supplied. Compact operators may represent a large carrier without
materializing it, but applying, composing and observing them must each have
explicit counted costs.

For a candidate compressed observable, first state which joint output
probabilities it preserves and how it composes after an earlier measurement.
Then prove that its retained representation suffices for the decoder,
including correlations and residual ports. If approximation is used, the
error must reach the complete output or success event rather than only a
normalized selected history. This suggests a native research direction;
it does not assert that a cheap closed interface has already been found.

Global-Knowledge-Sync: main@8c6557d / GLOBAL_KNOWLEDGE_V1. The shipped helper
returned PASS / LEASE_REUSED at this review; earlier frozen science was not
modified and no new scientific execution or admission is claimed.
