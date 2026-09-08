import EnterpriseMath.Relation.FramedBranchRecoalescence
import Mathlib.Algebra.MonoidAlgebra.Support
import Mathlib.Algebra.Group.Pointwise.Set.Basic
import Mathlib.Data.Finsupp.Order
import Mathlib.Tactic

namespace EnterpriseMath.BranchRecoalescence

open scoped Pointwise

/-- For positive multiplicity BRC, Boolean support is multiplicative as well as
additive: serial convolution has exactly the pointwise product of the two live
support sets.  The reverse inclusion uses the no-cancellation property of `ℕ`;
it would fail for signed coefficients. -/
theorem booleanShadow_mul {W G C : Type*}
    [Monoid W] [Monoid G] [AddMonoid C] {ρ : CoordinateAction G C}
    (f g : FramedNBRC W G C ρ) :
    booleanShadow (f * g) = booleanShadow f * booleanShadow g := by
  classical
  ext z
  constructor
  · intro hz
    change (f * g).coeff z ≠ 0 at hz
    have hzSupport : z ∈ (f * g).coeff.support :=
      Finsupp.mem_support_iff.mpr hz
    have hprod : z ∈ f.coeff.support * g.coeff.support :=
      MonoidAlgebra.support_coeff_mul_subset f g hzSupport
    rcases Finset.mem_mul.mp hprod with ⟨x, hx, y, hy, hxy⟩
    rw [Set.mem_mul]
    refine ⟨x, ?_, y, ?_, hxy⟩
    · change f.coeff x ≠ 0
      exact Finsupp.mem_support_iff.mp hx
    · change g.coeff y ≠ 0
      exact Finsupp.mem_support_iff.mp hy
  · rw [Set.mem_mul]
    rintro ⟨x, hx, y, hy, rfl⟩
    change (f * g).coeff (x * y) ≠ 0
    change f.coeff x ≠ 0 at hx
    change g.coeff y ≠ 0 at hy
    have hxSupport : x ∈ f.coeff.support :=
      Finsupp.mem_support_iff.mpr hx
    have hySupport : y ∈ g.coeff.support :=
      Finsupp.mem_support_iff.mpr hy
    have hxPos : 0 < f.coeff x := Nat.pos_of_ne_zero hx
    have hyPos : 0 < g.coeff y := Nat.pos_of_ne_zero hy
    rw [MonoidAlgebra.coeff_mul]
    apply ne_of_gt
    refine Finsupp.sum_pos' (fun _ _ => Nat.zero_le _) ?_
    refine ⟨x, hxSupport, ?_⟩
    refine Finsupp.sum_pos' (fun _ _ => Nat.zero_le _) ?_
    refine ⟨y, hySupport, ?_⟩
    rw [if_pos rfl]
    exact Nat.mul_pos hxPos hyPos

/-- The positive N-BRC Boolean shadow therefore preserves both alternative
recoalescence and serial composition. -/
theorem booleanShadow_semiring_bridge {W G C : Type*}
    [Monoid W] [Monoid G] [AddMonoid C] {ρ : CoordinateAction G C}
    (f g : FramedNBRC W G C ρ) :
    booleanShadow (f + g) = booleanShadow f ∪ booleanShadow g ∧
      booleanShadow (f * g) = booleanShadow f * booleanShadow g := by
  exact ⟨booleanShadow_add f g, booleanShadow_mul f g⟩

end EnterpriseMath.BranchRecoalescence
