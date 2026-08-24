import EnterpriseMath.PrimeFusion.Channels

namespace EnterpriseMath.PrimeFusion

/-- Evaluation of the Gaussian factor at an integer. -/
def gaussianEval (r : ℤ) : ℤ := r ^ 2 + 1

/-- Evaluation of the Eisenstein factor at an integer. -/
def eisensteinEval (r : ℤ) : ℤ := r ^ 2 + r + 1

/-- Evaluation of the fused polynomial at an integer. -/
def fusionEvalInt (r : ℤ) : ℤ := gaussianEval r * eisensteinEval r

/-- T5's signed Bézout identity at an integer residue. -/
theorem eval_bezout (r : ℤ) :
    (r + 1) * gaussianEval r - r * eisensteinEval r = 1 := by
  simp [gaussianEval, eisensteinEval]
  ring

/-- The two evaluated factors are coprime over `ℤ`, uniformly in `r`. -/
theorem eval_isCoprime (r : ℤ) : IsCoprime (gaussianEval r) (eisensteinEval r) := by
  refine ⟨r + 1, -r, ?_⟩
  simpa [sub_eq_add_neg] using eval_bezout r

/-- A no-leakage lemma: if `h = n*c`, `n | f`, `c | g`, and `f,g` are coprime,
then the first gcd recovers exactly `n`. -/
theorem gcd_recover_left {n c h : ℕ} {f g : ℤ}
    (hH : h = n * c) (hnf : (n : ℤ) ∣ f) (hcg : (c : ℤ) ∣ g)
    (hfg : IsCoprime f g) : Int.gcd (h : ℤ) f = n := by
  have hHInt : (h : ℤ) = (n : ℤ) * (c : ℤ) := by
    exact_mod_cast hH
  have hnH : (n : ℤ) ∣ (h : ℤ) := ⟨c, hHInt⟩
  have hndInt : (n : ℤ) ∣ (Int.gcd (h : ℤ) f : ℤ) :=
    Int.dvd_coe_gcd hnH hnf
  have hdf : (Int.gcd (h : ℤ) f : ℤ) ∣ f := Int.gcd_dvd_right _ _
  have hfc : IsCoprime f (c : ℤ) := hfg.of_isCoprime_of_dvd_right hcg
  have hdc : IsCoprime (Int.gcd (h : ℤ) f : ℤ) (c : ℤ) :=
    hfc.of_isCoprime_of_dvd_left hdf
  have hdh : (Int.gcd (h : ℤ) f : ℤ) ∣ (h : ℤ) := Int.gcd_dvd_left _ _
  have hdnInt : (Int.gcd (h : ℤ) f : ℤ) ∣ (n : ℤ) := by
    rw [hHInt] at hdh
    exact hdc.dvd_of_dvd_mul_right hdh
  have hnd : n ∣ Int.gcd (h : ℤ) f := by exact_mod_cast hndInt
  have hdn : Int.gcd (h : ℤ) f ∣ n := by exact_mod_cast hdnInt
  exact Nat.dvd_antisymm hdn hnd

/-- Symmetric no-leakage lemma for the second factor. -/
theorem gcd_recover_right {n c h : ℕ} {f g : ℤ}
    (hH : h = n * c) (hnf : (n : ℤ) ∣ f) (hcg : (c : ℤ) ∣ g)
    (hfg : IsCoprime f g) : Int.gcd (h : ℤ) g = c := by
  have hHInt : (h : ℤ) = (n : ℤ) * (c : ℤ) := by
    exact_mod_cast hH
  have hcH : (c : ℤ) ∣ (h : ℤ) := ⟨n, by rw [hHInt]; ring⟩
  have hcdInt : (c : ℤ) ∣ (Int.gcd (h : ℤ) g : ℤ) :=
    Int.dvd_coe_gcd hcH hcg
  have hdg : (Int.gcd (h : ℤ) g : ℤ) ∣ g := Int.gcd_dvd_right _ _
  have hgn : IsCoprime g (n : ℤ) :=
    hfg.symm.of_isCoprime_of_dvd_right hnf
  have hdn : IsCoprime (Int.gcd (h : ℤ) g : ℤ) (n : ℤ) :=
    hgn.of_isCoprime_of_dvd_left hdg
  have hdh : (Int.gcd (h : ℤ) g : ℤ) ∣ (h : ℤ) := Int.gcd_dvd_left _ _
  have hdcInt : (Int.gcd (h : ℤ) g : ℤ) ∣ (c : ℤ) := by
    rw [hHInt, mul_comm] at hdh
    exact hdn.dvd_of_dvd_mul_right hdh
  have hcd : c ∣ Int.gcd (h : ℤ) g := by exact_mod_cast hcdInt
  have hdc : Int.gcd (h : ℤ) g ∣ c := by exact_mod_cast hdcInt
  exact Nat.dvd_antisymm hdc hcd

/-- T5: exact channel recovery, with the Gaussian factor carrying `n` and the
Eisenstein factor carrying `c`. The signed Bézout identity rules out leakage. -/
theorem exact_channel_recovery {n c h : ℕ} (hH : h = n * c) (r : ℤ)
    (hrN : (n : ℤ) ∣ gaussianEval r)
    (hrC : (c : ℤ) ∣ eisensteinEval r) :
    Int.gcd (h : ℤ) (gaussianEval r) = n ∧
      Int.gcd (h : ℤ) (eisensteinEval r) = c :=
  ⟨gcd_recover_left hH hrN hrC (eval_isCoprime r),
    gcd_recover_right hH hrN hrC (eval_isCoprime r)⟩

section RootUnit

variable {R : Type*} [CommRing R]

/-- The fused polynomial evaluated in an arbitrary commutative ring. -/
def fusionEval (r : R) : R := (r ^ 2 + 1) * (r ^ 2 + r + 1)

/-- Explicit reciprocal forced by the fused-root equation. -/
def reciprocalCandidate (r : R) : R := -(r ^ 3 + r ^ 2 + 2 * r + 1)

/-- T6: every fused root has the displayed automatic reciprocal. -/
theorem fusion_root_mul_reciprocal {r : R} (hF : fusionEval r = 0) :
    r * reciprocalCandidate r = 1 := by
  calc
    r * reciprocalCandidate r = 1 - fusionEval r := by
      simp [reciprocalCandidate, fusionEval]
      ring
    _ = 1 := by rw [hF]; ring

/-- The reciprocal works on the other side as well. -/
theorem fusion_root_reciprocal_mul {r : R} (hF : fusionEval r = 0) :
    reciprocalCandidate r * r = 1 := by
  rw [mul_comm]
  exact fusion_root_mul_reciprocal hF

/-- The unit structure canonically forced by a fused root. -/
def fusionRootUnit (r : R) (hF : fusionEval r = 0) : Rˣ where
  val := r
  inv := reciprocalCandidate r
  val_inv := fusion_root_mul_reciprocal hF
  inv_val := fusion_root_reciprocal_mul hF

/-- `e = -(r+r⁻¹)` written without any ambient division operation. -/
def rootIdempotent (r : R) : R := -(r + reciprocalCandidate r)

/-- The explicit reciprocal is literally the inverse of the forced unit. -/
theorem rootIdempotent_eq_unit_trace (r : R) (hF : fusionEval r = 0) :
    rootIdempotent r =
      -((fusionRootUnit r hF : R) + ((↑((fusionRootUnit r hF)⁻¹) : R))) := by
  rfl

/-- T6: `e = -(r+r⁻¹)` is idempotent at every fused root. -/
theorem rootIdempotent_isIdempotent {r : R} (hF : fusionEval r = 0) :
    rootIdempotent r ^ 2 = rootIdempotent r := by
  have hid : rootIdempotent r ^ 2 - rootIdempotent r =
      r * (r + 1) * fusionEval r := by
    simp [rootIdempotent, reciprocalCandidate, fusionEval]
    ring
  rw [hid, hF]
  ring

end RootUnit

/-- T6 arithmetic split: an integral idempotence congruence modulo `H` produces
coprime gcd factors whose product is exactly `H`. -/
theorem idempotent_gcd_partition {H : ℕ} {e : ℤ}
    (hidem : (H : ℤ) ∣ e * (e - 1)) :
    Nat.Coprime (Int.gcd e (H : ℤ)) (Int.gcd (e - 1) (H : ℤ)) ∧
      Int.gcd e (H : ℤ) * Int.gcd (e - 1) (H : ℤ) = H := by
  have hconsec : IsCoprime e (e - 1) := by
    refine ⟨1, -1, ?_⟩
    ring
  have habs : Nat.Coprime e.natAbs (e - 1).natAbs :=
    Int.isCoprime_iff_nat_coprime.mp hconsec
  have hdivNat : H ∣ e.natAbs * (e - 1).natAbs := by
    rcases hidem with ⟨k, hk⟩
    refine ⟨k.natAbs, ?_⟩
    have hkabs := congrArg Int.natAbs hk
    simpa [Int.natAbs_mul] using hkabs
  constructor
  · simpa [Int.gcd_def, Nat.gcd_comm] using habs.gcd_both H H
  · have hprod :=
      (Nat.gcd_mul_gcd_eq_iff_dvd_mul_of_coprime habs).2 hdivNat
    simpa [Int.gcd_def, Nat.gcd_comm] using hprod

end EnterpriseMath.PrimeFusion
