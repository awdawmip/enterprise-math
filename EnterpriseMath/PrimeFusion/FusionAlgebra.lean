import EnterpriseMath.PrimeFusion.Channels
import Mathlib.Algebra.Ring.Fin
import Mathlib.RingTheory.Ideal.Quotient.Operations

namespace EnterpriseMath.PrimeFusion

open Polynomial
open scoped Function

/-- The Gaussian fusion factor `X² + 1`. -/
noncomputable def gaussianPoly : Polynomial ℤ := X ^ 2 + 1

/-- The Eisenstein fusion factor `X² + X + 1`. -/
noncomputable def eisensteinPoly : Polynomial ℤ := X ^ 2 + X + 1

/-- The Prime Fusion polynomial `F = (X²+1)(X²+X+1)`. -/
noncomputable def fusionPoly : Polynomial ℤ := gaussianPoly * eisensteinPoly

/-- T3's integral Bézout certificate. -/
theorem fusion_bezout :
    (X + 1) * gaussianPoly - X * eisensteinPoly = (1 : Polynomial ℤ) := by
  simp [gaussianPoly, eisensteinPoly]
  ring

/-- Principal Gaussian factor ideal. -/
noncomputable def gaussianIdeal : Ideal (Polynomial ℤ) := Ideal.span {gaussianPoly}

/-- Principal Eisenstein factor ideal. -/
noncomputable def eisensteinIdeal : Ideal (Polynomial ℤ) := Ideal.span {eisensteinPoly}

/-- Principal fusion ideal. -/
noncomputable def fusionIdeal : Ideal (Polynomial ℤ) := Ideal.span {fusionPoly}

/-- The two polynomial factor ideals are comaximal over `ℤ[X]`. -/
theorem fusionFactors_isCoprime : IsCoprime gaussianIdeal eisensteinIdeal := by
  rw [Ideal.isCoprime_iff_exists]
  refine ⟨(X + 1) * gaussianPoly, ?_, (-X) * eisensteinPoly, ?_, ?_⟩
  · exact gaussianIdeal.mul_mem_left _ (Ideal.subset_span (by simp))
  · exact eisensteinIdeal.mul_mem_left _ (Ideal.subset_span (by simp))
  · simpa [sub_eq_add_neg] using fusion_bezout

/-- The fusion principal ideal is the intersection of the two component ideals. -/
theorem fusionIdeal_eq_inf : fusionIdeal = gaussianIdeal ⊓ eisensteinIdeal := by
  calc
    fusionIdeal = gaussianIdeal * eisensteinIdeal := by
      simp [fusionIdeal, gaussianIdeal, eisensteinIdeal, fusionPoly,
        Ideal.span_singleton_mul_span_singleton]
    _ = gaussianIdeal ⊓ eisensteinIdeal :=
      Ideal.mul_eq_inf_of_coprime (Ideal.isCoprime_iff_sup_eq.mp fusionFactors_isCoprime)

/-- The factor-ideal family used by the finite integral CRT. -/
noncomputable def factorIdeal : Fin 2 → Ideal (Polynomial ℤ) :=
  ![gaussianIdeal, eisensteinIdeal]

/-- The two-element factor family is pairwise comaximal. -/
theorem factorIdeal_pairwise : Pairwise (IsCoprime on factorIdeal) := by
  intro i j hij
  fin_cases i <;> fin_cases j
  · exact (hij rfl).elim
  · change IsCoprime gaussianIdeal eisensteinIdeal
    exact fusionFactors_isCoprime
  · change IsCoprime eisensteinIdeal gaussianIdeal
    exact fusionFactors_isCoprime.symm
  · exact (hij rfl).elim

/-- The finite infimum of the two factor ideals is their ordinary intersection. -/
theorem factorIdeal_iInf :
    (⨅ i, factorIdeal i) = gaussianIdeal ⊓ eisensteinIdeal := by
  ext P
  simp [factorIdeal, Fin.forall_fin_two]

/-- The fusion ideal is the finite intersection used by the CRT map. -/
theorem fusionIdeal_eq_iInf : fusionIdeal = ⨅ i, factorIdeal i := by
  rw [factorIdeal_iInf, fusionIdeal_eq_inf]

/-- T3: the integral CRT decomposition, with the two factors kept definitionally visible. -/
noncomputable def fusionCRT :
    (Polynomial ℤ ⧸ fusionIdeal) ≃+*
      (Polynomial ℤ ⧸ factorIdeal 0) × (Polynomial ℤ ⧸ factorIdeal 1) := by
  let e₁ := Ideal.quotEquivOfEq fusionIdeal_eq_iInf
  let e₂ := Ideal.quotientInfRingEquivPiQuotient factorIdeal factorIdeal_pairwise
  let e₃ := RingEquiv.piFinTwo (fun i => Polynomial ℤ ⧸ factorIdeal i)
  exact e₁.trans (e₂.trans e₃)

/-- The first CRT factor is exactly the Gaussian quotient. -/
theorem factorIdeal_zero : factorIdeal 0 = gaussianIdeal := by
  simp [factorIdeal]

/-- The second CRT factor is exactly the Eisenstein quotient. -/
theorem factorIdeal_one : factorIdeal 1 = eisensteinIdeal := by
  simp [factorIdeal]

end EnterpriseMath.PrimeFusion
