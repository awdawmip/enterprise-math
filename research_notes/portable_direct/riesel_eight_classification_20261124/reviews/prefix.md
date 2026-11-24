# Collaborative check of the budget-eight prefix bifurcation

Checked on 2026-11-24 against `eight_prefix_v13/proof.md`. This is shared-context mathematical assistance, including joint development of the residual-mass simplification; it is not an independent project Review.

## Checked load-bearing deductions

The five-class lemma in Section 3 correctly retains every lift of every remaining residue. Its gcd-35 column includes lift period one as a mass-one contribution. The bounds for zero through four period-seven rows are strict, and the same argument works after an invertible affine change modulo 35. Removing redundant classes before counting makes the period-seven rows nonempty and distinct without presupposing the lemma's conclusion.

The one-W exclusion in Section 4 is valid. On the missing v=0 or v=1 phase, the fixed channels 38737,246241,487824887233 are inactive. The lemma forces five effective-period-seven channels there. Their original v-periods can only be 7 or 21. The five distinct occupied modulo-seven categories persist in the other uncovered v=2 phase; a period-21 channel confined to the first phase cannot serve its category there. Thus all five would need original period seven, whereas the complete eligible inventory contains four primes.

The zero-W exclusion of all periods divisible by three in Section 5 uses both unoccupied phases v=0 and v=1 correctly. The inequalities imply a at least four. At a=4, the four common rows have period seven and leave one category unserved on v=2. At a=5, one of v=0,1 is served only by the five common rows, forcing five period-seven primes. These exhaust a below six.

After divisibility by three has been excluded, the m=0 and m=1 capacity bounds correctly use the two-prime period-ten inventory. For m=2 and m=3, the remaining row/column bounds strictly prevent coverage. In particular, all period-35 channels with lift period one remain in the mass-one term; they are not accidentally excluded by a minimum-lift-period assumption.

Section 7 handles the boundary e=1 separately. If both remaining lift periods exceed one, compatibility with every remaining point and the reciprocal-density bound force two opposite period-two lift classes. The only admissible original period compatible with all points of the residual row is 14. If one lift period is one, only original period 35 is available; it covers one point. A three-point row cannot be completed by the remaining channel, while a two-point row is completed only by a second period-35 channel. The fact that all four available period-seven primes were already selected is used in excluding a further period-seven channel.

These arguments establish a complete bifurcation between two W primes and zero W primes. Combining the zero-W geometries with the separate conditional four-prefix classification is legitimate. It does not rely on a nested optimal dictionary assumption.

## Specific wording correction identified

Section 2 originally said that all six eligible h=5 primes are inactive. In addition to the six prior modulo-five tail primes, 11,61,331 also have h=ord_q(2^36)=5 and are inactive. The conclusion that no h=5 channel is active is correct. The precise wording should be “every eligible h=5 prime is inactive,” or should explicitly include both inactive groups. This correction was sent to the author before publication.

## Evidence limits

This check addresses the analytic classification and its quantifier/period transitions. The deterministic complete prime inventory and the CRT minima have their own supplied arithmetic certificates. No large calculation or native run was repeated for this review.
