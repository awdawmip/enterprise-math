import EnterpriseMath.Quotient.RootQuotientSpareMacroDivisibility
import Mathlib.Algebra.GCDMonoid.Finset
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- GCD kernel of a finite target family that a single spare instruction is
asked to repair. -/
def rootQuotientRepairDivisorKernel (T : Finset ℕ) : ℕ :=
  T.gcd id

/-- **Finite spare-slot repair-kernel theorem.**

If every target in a finite family is outside the horizon-`h` reachability ball
of a base ISA `G`, but adjoining one generator `g` makes every target reachable,
then `g` must divide the gcd of the whole target family.

Thus single-slot dictionary completion reduces from an unbounded search over
candidate instructions to the divisor lattice of one integer. -/
theorem spare_generator_dvd_repairDivisorKernel
    {G : Set ℕ} {g h : ℕ} {T : Finset ℕ}
    (hReach : ∀ t ∈ T,
      RootQuotientProductReachableWithin h (insert g G) t)
    (hNoBase : ∀ t ∈ T,
      ¬RootQuotientProductReachableWithin h G t) :
    g ∣ rootQuotientRepairDivisorKernel T := by
  dsimp [rootQuotientRepairDivisorKernel]
  apply Finset.dvd_gcd
  intro t ht
  exact spare_generator_dvd_target_of_reachable_not_reachable_without
    (hReach t ht) (hNoBase t ht)

/-- If the repair kernel is one, no nontrivial single spare generator can repair
the entire finite hard-target family. -/
theorem no_nontrivial_spare_generator_repairs_family_of_kernel_eq_one
    {G : Set ℕ} {g h : ℕ} {T : Finset ℕ}
    (hgTwo : 2 ≤ g)
    (hKernel : rootQuotientRepairDivisorKernel T = 1)
    (hReach : ∀ t ∈ T,
      RootQuotientProductReachableWithin h (insert g G) t)
    (hNoBase : ∀ t ∈ T,
      ¬RootQuotientProductReachableWithin h G t) :
    False := by
  have hgDvd := spare_generator_dvd_repairDivisorKernel hReach hNoBase
  rw [hKernel] at hgDvd
  have hgLe : g ≤ 1 := Nat.le_of_dvd (by omega) hgDvd
  omega

/-- Kernel monotonicity under adding more base-hard targets: a larger target
certificate can only shrink the repair-divisor kernel in the divisibility
order. -/
theorem repairDivisorKernel_union_dvd_left
    (T U : Finset ℕ) :
    rootQuotientRepairDivisorKernel (T ∪ U) ∣
      rootQuotientRepairDivisorKernel T := by
  dsimp [rootQuotientRepairDivisorKernel]
  exact Finset.gcd_mono (Finset.subset_union_left)

/-- Symmetric kernel monotonicity toward the right certificate family. -/
theorem repairDivisorKernel_union_dvd_right
    (T U : Finset ℕ) :
    rootQuotientRepairDivisorKernel (T ∪ U) ∣
      rootQuotientRepairDivisorKernel U := by
  dsimp [rootQuotientRepairDivisorKernel]
  exact Finset.gcd_mono (Finset.subset_union_right)

end EnterpriseMath.Quotient
