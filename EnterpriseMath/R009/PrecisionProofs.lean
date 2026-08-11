import Mathlib
import EnterpriseMath.R009.PrecisionTargets

namespace EnterpriseMath.R009

private theorem r009_dvd_of_mod_eq_zero {r n : ℕ} (h : n % r = 0) : r ∣ n := by
  refine ⟨n / r, ?_⟩
  have hdecomp := Nat.mod_add_div n r
  omega

/-- R009-T27: a monotone map is quotient-safe exactly when every attained
coarse-output threshold first occurs on an input block boundary. -/
theorem r009_t27 : T27Statement := by
  unfold T27Statement
  intro r hr F
  have hr0 : 0 < r := by omega
  constructor
  · intro hSafe t τ hCross
    rcases hCross with ⟨hReach, hFirst⟩
    by_contra hNotDvd
    have hMod : τ % r ≠ 0 := by
      intro hz
      exact hNotDvd (r009_dvd_of_mod_eq_zero hz)
    let b : ℕ := (τ / r) * r
    have hDecomp := Nat.mod_add_div τ r
    have hb_lt : b < τ := by
      dsimp [b]
      omega
    have hb_div : b / r = τ / r := by
      dsimp [b]
      rw [Nat.mul_div_right _ hr0]
    have hOutEq : F b / r = F τ / r := hSafe b τ hb_div
    have hBefore : F b < t * r := hFirst b hb_lt
    have hBeforeDiv : F b / r < t := by
      exact (Nat.div_lt_iff_lt_mul hr0).2 hBefore
    have hReachDiv : t ≤ F τ / r := by
      exact (Nat.le_div_iff_mul_le hr0).2 hReach
    rw [hOutEq] at hBeforeDiv
    omega
  · intro hAligned n m hSame
    have hOrdered : ∀ {x y : ℕ}, x ≤ y → x / r = y / r → F x / r = F y / r := by
      intro x y hxy hBlock
      have hFxy : F x ≤ F y := F.monotone hxy
      have hDivLe : F x / r ≤ F y / r := Nat.div_le_div_right hFxy
      by_contra hNe
      have hStrict : F x / r < F y / r := lt_of_le_of_ne hDivLe hNe
      let t : ℕ := F x / r + 1
      have hxBefore : F x < t * r := by
        have hxlt := Nat.lt_div_mul_add hr0 (F x)
        dsimp [t]
        omega
      have htLe : t ≤ F y / r := by
        dsimp [t]
        omega
      have hyReach : t * r ≤ F y := by
        exact (Nat.le_div_iff_mul_le hr0).1 htLe
      let hExists : ∃ z : ℕ, t * r ≤ F z := ⟨y, hyReach⟩
      let τ : ℕ := Nat.find hExists
      have hτReach : t * r ≤ F τ := Nat.find_spec hExists
      have hτFirst : ∀ z < τ, F z < t * r := by
        intro z hz
        have hn := Nat.find_min hExists hz
        omega
      have hτle : τ ≤ y := Nat.find_min' hExists hyReach
      have hxltτ : x < τ := by
        by_contra hNot
        have hτx : τ ≤ x := by omega
        have hmono : F τ ≤ F x := F.monotone hτx
        omega
      have hτDvd : r ∣ τ := hAligned t τ ⟨hτReach, hτFirst⟩
      obtain ⟨k, hk⟩ := hτDvd
      have hxk : x / r < k := by
        apply (Nat.div_lt_iff_lt_mul hr0).2
        simpa [hk, Nat.mul_comm] using hxltτ
      have hky : k ≤ y / r := by
        apply (Nat.le_div_iff_mul_le hr0).2
        simpa [hk, Nat.mul_comm] using hτle
      omega
    rcases le_total n m with hnm | hmn
    · exact hOrdered hnm hSame
    · exact (hOrdered hmn hSame.symm).symm

/-- R009-T28: the repaired predecessor right adjoint exists as a mathlib `OrderHom`,
forms a `GaloisConnection` with `A`, and is r-safe exactly at the divisibility-aligned
thresholds `A (t*r)`. -/
theorem r009_t28 : T28Statement := by
  unfold T28Statement
  intro A hA0 hStrict hUnbounded
  have hIdLe : ∀ k : ℕ, k ≤ A k := by
    intro k
    induction k with
    | zero => simp [hA0]
    | succ k ih =>
        have hstep : A k < A (k + 1) := hStrict (Nat.lt_succ_self k)
        omega
  let Rfun : ℕ → ℕ := fun n => Nat.findGreatest (fun k => A k ≤ n) n
  have hRmono : Monotone Rfun := by
    intro n m hnm
    exact Nat.findGreatest_mono (fun _ hk => hk.trans hnm) hnm
  let R : ℕ →o ℕ :=
    { toFun := Rfun
      monotone' := hRmono }
  have hRspec : ∀ n : ℕ, A (R n) ≤ n := by
    intro n
    change A (Nat.findGreatest (fun k => A k ≤ n) n) ≤ n
    apply Nat.findGreatest_spec (m := 0) (n := n)
    · exact Nat.zero_le _
    · simp [hA0]
  have hGC : GaloisConnection A R := by
    intro j n
    constructor
    · intro hAj
      change j ≤ Nat.findGreatest (fun k => A k ≤ n) n
      exact Nat.le_findGreatest ((hIdLe j).trans hAj) hAj
    · intro hj
      exact (hStrict.monotone hj).trans (hRspec n)
  refine ⟨R, hGC, ?_⟩
  intro r hr
  have hT27 : SafeAt r R ↔
      ∀ t τ : ℕ, IsFirstCrossing r t R τ → r ∣ τ :=
    r009_t27 r hr R
  constructor
  · intro hSafe t
    apply (hT27.mp hSafe) t (A (t * r))
    constructor
    · exact (hGC (t * r) (A (t * r))).2 le_rfl
    · intro n hn
      have hNot : ¬ t * r ≤ R n := by
        intro hle
        have hAn : A (t * r) ≤ n := (hGC (t * r) n).2 hle
        omega
      omega
  · intro hDiv
    apply hT27.mpr
    intro t τ hCross
    rcases hCross with ⟨hReach, hFirst⟩
    have hAle : A (t * r) ≤ τ := (hGC (t * r) τ).2 hReach
    have hτle : τ ≤ A (t * r) := by
      by_contra hNot
      have hlt : A (t * r) < τ := by omega
      have hBefore := hFirst (A (t * r)) hlt
      have hAt : t * r ≤ R (A (t * r)) :=
        (hGC (t * r) (A (t * r))).2 le_rfl
      omega
    have hEq : τ = A (t * r) := le_antisymm hτle hAle
    rw [hEq]
    exact hDiv t

end EnterpriseMath.R009
