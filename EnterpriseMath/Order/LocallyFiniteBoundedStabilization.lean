import Mathlib.Data.Fintype.Card
import Mathlib.Order.Interval.Finset.Basic
import EnterpriseMath.Order.AdjointReductiveDuality

namespace EnterpriseMath.LocallyFiniteBoundedStabilization

open EnterpriseMath.AdjointReductiveDuality

variable {α : Type*} [PartialOrder α] [LocallyFiniteOrder α]

/--
Restrict an extensive monotone map to a finite closed interval `[x,y]` when `y`
is a fixed upper bound.  The lifted map is still monotone and extensive.
-/
def intervalMap (L : α → α) (hmono : Monotone L) (hext : ∀ z, z ≤ L z)
    {x y : α} (hxy : x ≤ y) (hyfix : L y = y) :
    {z : α // z ∈ Finset.Icc x y} → {z : α // z ∈ Finset.Icc x y} := fun z => by
  refine ⟨L z.1, ?_⟩
  have hz := Finset.mem_Icc.mp z.2
  exact Finset.mem_Icc.mpr ⟨hz.1.trans (hext z.1), by
    calc
      L z.1 ≤ L y := hmono hz.2
      _ = y := hyfix⟩

@[simp]
theorem intervalMap_val (L : α → α) (hmono : Monotone L) (hext : ∀ z, z ≤ L z)
    {x y : α} (hxy : x ≤ y) (hyfix : L y = y)
    (z : {z : α // z ∈ Finset.Icc x y}) :
    (intervalMap L hmono hext hxy hyfix z).1 = L z.1 := rfl

theorem intervalMap_mono (L : α → α) (hmono : Monotone L) (hext : ∀ z, z ≤ L z)
    {x y : α} (hxy : x ≤ y) (hyfix : L y = y) :
    Monotone (intervalMap L hmono hext hxy hyfix) := by
  intro a b hab
  exact hmono hab

theorem intervalMap_extensive (L : α → α) (hmono : Monotone L) (hext : ∀ z, z ≤ L z)
    {x y : α} (hxy : x ≤ y) (hyfix : L y = y) :
    ∀ z, z ≤ intervalMap L hmono hext hxy hyfix z := by
  intro z
  exact hext z.1

/-- Iterating the interval lift and then forgetting the subtype is ordinary iteration of `L`. -/
theorem intervalMap_iterate_val (L : α → α) (hmono : Monotone L) (hext : ∀ z, z ≤ L z)
    {x y : α} (hxy : x ≤ y) (hyfix : L y = y)
    (z : {z : α // z ∈ Finset.Icc x y}) :
    ∀ n : ℕ,
      (((intervalMap L hmono hext hxy hyfix)^[n]) z).1 = (L^[n]) z.1 := by
  intro n
  induction n with
  | zero => rfl
  | succ n ih =>
      rw [Function.iterate_succ_apply]
      rw [Function.iterate_succ_apply]
      change L ((((intervalMap L hmono hext hxy hyfix)^[n]) z).1) = L ((L^[n]) z.1)
      rw [ih]

/--
Local bounded stabilization: a monotone extensive map needs no global
`WellFoundedGT` assumption if the orbit starts below an explicit fixed upper
bound inside a locally finite interval.

Ordinary iteration reaches, after finitely many steps, the least fixed point of
`L` lying between `x` and `y` and above `x`.
-/
theorem exists_iterate_isLeast_of_fixed_upper_bound
    (L : α → α) (hmono : Monotone L) (hext : ∀ z, z ≤ L z)
    {x y : α} (hxy : x ≤ y) (hyfix : L y = y) :
    ∃ n : ℕ,
      IsLeast {z : α | L z = z ∧ x ≤ z ∧ z ≤ y} ((L^[n]) x) := by
  let β := {z : α // z ∈ Finset.Icc x y}
  let xβ : β := ⟨x, Finset.mem_Icc.mpr ⟨le_rfl, hxy⟩⟩
  let Lβ : β → β := intervalMap L hmono hext hxy hyfix
  have hmonoβ : Monotone Lβ := intervalMap_mono L hmono hext hxy hyfix
  have hextβ : ∀ z, z ≤ Lβ z := intervalMap_extensive L hmono hext hxy hyfix
  obtain ⟨n, hn⟩ := exists_iterate_isLeast Lβ hmonoβ hextβ xβ
  refine ⟨n, ?_⟩
  have hval : ((Lβ^[n]) xβ).1 = (L^[n]) x := by
    exact intervalMap_iterate_val L hmono hext hxy hyfix xβ n
  have hcandIcc := Finset.mem_Icc.mp ((Lβ^[n]) xβ).2
  constructor
  · constructor
    · have hfixval := congrArg Subtype.val hn.1.1
      change L ((Lβ^[n]) xβ).1 = ((Lβ^[n]) xβ).1 at hfixval
      rw [hval] at hfixval
      exact hfixval
    · constructor
      · have hxle : xβ ≤ (Lβ^[n]) xβ := hn.1.2
        change x ≤ ((Lβ^[n]) xβ).1 at hxle
        rw [hval] at hxle
        exact hxle
      · rw [hval] at hcandIcc
        exact hcandIcc.2
  · intro z hz
    let zβ : β := ⟨z, Finset.mem_Icc.mpr ⟨hz.2.1, hz.2.2⟩⟩
    have hzfixβ : Lβ zβ = zβ := by
      apply Subtype.ext
      exact hz.1
    have hxzβ : xβ ≤ zβ := hz.2.1
    have hleastβ : (Lβ^[n]) xβ ≤ zβ := hn.2 ⟨hzfixβ, hxzβ⟩
    change ((Lβ^[n]) xβ).1 ≤ z at hleastβ
    rw [hval] at hleastβ
    exact hleastβ

end EnterpriseMath.LocallyFiniteBoundedStabilization
