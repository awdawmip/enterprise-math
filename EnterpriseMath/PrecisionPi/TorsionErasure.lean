import Mathlib.Data.ZMod.Basic
import Mathlib.Algebra.Group.Hom.End

namespace EnterpriseMath.PrecisionPi.TorsionErasure

/-- Every element of `ZMod 2` is killed by doubling. -/
theorem zmod_two_add_self (x : ZMod 2) : x + x = 0 := by
  calc
    x + x = (2 : ZMod 2) * x := by ring
    _ = 0 := by norm_num

/-- Any additive observation of a `C₂` torsion bit in the real continuum is zero. -/
theorem addHom_zmod_two_real_eq_zero (f : ZMod 2 →+ ℝ) : f = 0 := by
  ext x
  have hdouble : f x + f x = 0 := by
    calc
      f x + f x = f (x + x) := by simp
      _ = f 0 := by rw [zmod_two_add_self]
      _ = 0 := by simp
  have hx : f x = 0 := by linarith
  simpa using hx

/-- Pointwise form of continuum torsion erasure. -/
theorem addHom_zmod_two_real_apply (f : ZMod 2 →+ ℝ) (x : ZMod 2) :
    f x = 0 := by
  rw [addHom_zmod_two_real_eq_zero f]
  rfl

end EnterpriseMath.PrecisionPi.TorsionErasure
