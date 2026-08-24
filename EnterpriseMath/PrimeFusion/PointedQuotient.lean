import EnterpriseMath.PrimeFusion.MixedLocus

namespace EnterpriseMath.PrimeFusion

/-- `N` is always nonnegative. -/
theorem N_nonneg (a b : ℤ) : 0 ≤ N a b := by
  simp [N]
  positivity

/-- `C` is always nonnegative, using the exact diagonal identity from T1. -/
theorem C_nonneg (a b : ℤ) : 0 ≤ C a b := by
  have h := four_mul_C_eq_u_sq_add_three_v_sq a b
  nlinarith [sq_nonneg (u a b), sq_nonneg (v a b)]

/-- Natural modulus carried by the Gaussian channel. -/
def Nmodulus (a b : ℤ) : ℕ := (N a b).natAbs

/-- Natural modulus carried by the Eisenstein channel. -/
def Cmodulus (a b : ℤ) : ℕ := (C a b).natAbs

/-- Natural fused modulus. -/
def Hmodulus (a b : ℤ) : ℕ := (N a b * C a b).natAbs

@[simp] theorem coe_Nmodulus (a b : ℤ) : (Nmodulus a b : ℤ) = N a b := by
  simp [Nmodulus, Int.natAbs_of_nonneg (N_nonneg a b)]

@[simp] theorem coe_Cmodulus (a b : ℤ) : (Cmodulus a b : ℤ) = C a b := by
  simp [Cmodulus, Int.natAbs_of_nonneg (C_nonneg a b)]

@[simp] theorem coe_Hmodulus (a b : ℤ) : (Hmodulus a b : ℤ) = N a b * C a b := by
  have hnonneg : 0 ≤ N a b * C a b := mul_nonneg (N_nonneg a b) (C_nonneg a b)
  simp [Hmodulus, Int.natAbs_of_nonneg hnonneg]

/-- A primitive pair has positive Gaussian channel size. -/
theorem N_pos_of_isCoprime {a b : ℤ} (hab : IsCoprime a b) : 0 < N a b := by
  rcases hab with ⟨s, t, hst⟩
  by_contra hpos
  have hzero : N a b = 0 := le_antisymm (le_of_not_gt hpos) (N_nonneg a b)
  have ha2 : a ^ 2 = 0 := by
    simp [N] at hzero
    nlinarith [sq_nonneg a, sq_nonneg b]
  have hb2 : b ^ 2 = 0 := by
    simp [N] at hzero
    nlinarith [sq_nonneg a, sq_nonneg b]
  have ha : a = 0 := by simpa using ha2
  have hb : b = 0 := by simpa using hb2
  subst a
  subst b
  norm_num at hst

/-- A primitive pair has positive Eisenstein channel size. -/
theorem C_pos_of_isCoprime {a b : ℤ} (hab : IsCoprime a b) : 0 < C a b := by
  rcases hab with ⟨s, t, hst⟩
  by_contra hpos
  have hzero : C a b = 0 := le_antisymm (le_of_not_gt hpos) (C_nonneg a b)
  have hdiag := four_mul_C_eq_u_sq_add_three_v_sq a b
  have hu2 : u a b ^ 2 = 0 := by
    rw [hzero] at hdiag
    nlinarith [sq_nonneg (u a b), sq_nonneg (v a b)]
  have hv2 : v a b ^ 2 = 0 := by
    rw [hzero] at hdiag
    nlinarith [sq_nonneg (u a b), sq_nonneg (v a b)]
  have hu : u a b = 0 := by simpa using hu2
  have hv : v a b = 0 := by simpa using hv2
  have ha : a = 0 := by
    simp [u, v] at hu hv
    linarith
  have hb : b = 0 := by
    simp [u, v] at hu hv
    linarith
  subst a
  subst b
  norm_num at hst

/-- The common primitive linear residue map used by both component quotients. -/
def channelResidueMap (n : ℕ) (a b : ℤ) : (ℤ × ℤ) →+ ZMod n where
  toFun z := (b : ZMod n) * (z.1 : ZMod n) - (a : ZMod n) * (z.2 : ZMod n)
  map_zero' := by simp
  map_add' x y := by
    push_cast
    ring

/-- Exact kernel criterion for the component residue map. -/
theorem mem_ker_channelResidueMap_iff (n : ℕ) (a b : ℤ) (z : ℤ × ℤ) :
    z ∈ (channelResidueMap n a b).ker ↔ (n : ℤ) ∣ b * z.1 - a * z.2 := by
  rw [AddMonoidHom.mem_ker]
  change ((b * z.1 - a * z.2 : ℤ) : ZMod n) = 0 ↔ (n : ℤ) ∣ b * z.1 - a * z.2
  exact ZMod.intCast_zmod_eq_zero_iff_dvd _ _

/-- Primitive input makes the linear residue map surjective for every nonzero modulus. -/
theorem channelResidueMap_surjective {n : ℕ} [NeZero n] {a b : ℤ}
    (hab : IsCoprime a b) : Function.Surjective (channelResidueMap n a b) := by
  rintro z
  rcases hab with ⟨s, t, hst⟩
  have hbez := congrArg (fun k : ℤ => (k : ZMod n)) hst
  push_cast at hbez
  refine ⟨(t * (z.val : ℤ), -s * (z.val : ℤ)), ?_⟩
  change (b : ZMod n) * (t * (z.val : ℤ) : ℤ) -
      (a : ZMod n) * (-s * (z.val : ℤ) : ℤ) = z
  push_cast
  rw [← ZMod.natCast_zmod_val z]
  push_cast
  linear_combination (z.val : ZMod n) * hbez

/-- Gaussian cyclic quotient map from the primitive lattice coordinates. -/
def gaussianQuotientMap (a b : ℤ) : (ℤ × ℤ) →+ ZMod (Nmodulus a b) :=
  channelResidueMap (Nmodulus a b) a b

/-- Eisenstein cyclic quotient map from the primitive lattice coordinates. -/
def eisensteinQuotientMap (a b : ℤ) : (ℤ × ℤ) →+ ZMod (Cmodulus a b) :=
  channelResidueMap (Cmodulus a b) a b

/-- T4 exact Gaussian kernel. -/
theorem gaussianQuotientMap_kernel (a b : ℤ) (z : ℤ × ℤ) :
    z ∈ (gaussianQuotientMap a b).ker ↔ N a b ∣ b * z.1 - a * z.2 := by
  simpa [gaussianQuotientMap] using mem_ker_channelResidueMap_iff (Nmodulus a b) a b z

/-- T4 exact Eisenstein kernel. -/
theorem eisensteinQuotientMap_kernel (a b : ℤ) (z : ℤ × ℤ) :
    z ∈ (eisensteinQuotientMap a b).ker ↔ C a b ∣ b * z.1 - a * z.2 := by
  simpa [eisensteinQuotientMap] using mem_ker_channelResidueMap_iff (Cmodulus a b) a b z

/-- T4 Gaussian component quotient is onto its cyclic carrier. -/
theorem gaussianQuotientMap_surjective {a b : ℤ} (hab : IsCoprime a b) :
    Function.Surjective (gaussianQuotientMap a b) := by
  letI : NeZero (Nmodulus a b) := by
    constructor
    intro hz
    have hcast : (Nmodulus a b : ℤ) = 0 := by simp [hz]
    rw [coe_Nmodulus] at hcast
    exact (N_pos_of_isCoprime hab).ne' hcast
  exact channelResidueMap_surjective hab

/-- T4 Eisenstein component quotient is onto its cyclic carrier. -/
theorem eisensteinQuotientMap_surjective {a b : ℤ} (hab : IsCoprime a b) :
    Function.Surjective (eisensteinQuotientMap a b) := by
  letI : NeZero (Cmodulus a b) := by
    constructor
    intro hz
    have hcast : (Cmodulus a b : ℤ) = 0 := by simp [hz]
    rw [coe_Cmodulus] at hcast
    exact (C_pos_of_isCoprime hab).ne' hcast
  exact channelResidueMap_surjective hab

/-- T4 exact Gaussian cyclic carrier size. -/
theorem gaussianCarrier_card (a b : ℤ) :
    Nat.card (ZMod (Nmodulus a b)) = Nmodulus a b := Nat.card_zmod _

/-- T4 exact Eisenstein cyclic carrier size. -/
theorem eisensteinCarrier_card (a b : ℤ) :
    Nat.card (ZMod (Cmodulus a b)) = Cmodulus a b := Nat.card_zmod _

/-- T4 product carrier has the fused size `N*C`. -/
theorem fusedCarrier_card (a b : ℤ) :
    Nat.card (ZMod (Nmodulus a b) × ZMod (Cmodulus a b)) =
      Nmodulus a b * Cmodulus a b := by
  simp [Nat.card_zmod]

/-- Primitive `b` is coprime to the Gaussian channel. -/
theorem primitive_b_N_isCoprime {a b : ℤ} (hab : IsCoprime a b) : IsCoprime b (N a b) := by
  have hba2 : IsCoprime b (a ^ 2) := hab.symm.pow_right
  rcases hba2 with ⟨s, t, hst⟩
  refine ⟨s - t * b, t, ?_⟩
  dsimp [N]
  linear_combination hst

/-- Primitive `b` is coprime to the Eisenstein channel. -/
theorem primitive_b_C_isCoprime {a b : ℤ} (hab : IsCoprime a b) : IsCoprime b (C a b) := by
  have hba2 : IsCoprime b (a ^ 2) := hab.symm.pow_right
  rcases hba2 with ⟨s, t, hst⟩
  refine ⟨s - t * (b - a), t, ?_⟩
  dsimp [C]
  linear_combination hst

/-- Primitive `b` is therefore a unit modulo the fused modulus. -/
theorem primitive_b_H_isCoprime {a b : ℤ} (hab : IsCoprime a b) :
    IsCoprime b (Hmodulus a b : ℤ) := by
  rw [coe_Hmodulus]
  exact (primitive_b_N_isCoprime hab).mul_right (primitive_b_C_isCoprime hab)

/-- Turn an integral Bézout certificate with the modulus into an actual `ZMod` unit. -/
def zmodUnitOfIntCoprime {H : ℕ} (b : ℤ) (hb : IsCoprime b (H : ℤ)) : (ZMod H)ˣ := by
  rcases hb with ⟨s, t, hst⟩
  have hcast := congrArg (fun k : ℤ => (k : ZMod H)) hst
  push_cast at hcast
  have hsb : (s : ZMod H) * (b : ZMod H) = 1 := by
    simpa using hcast
  exact {
    val := (b : ZMod H)
    inv := (s : ZMod H)
    val_inv := by simpa [mul_comm] using hsb
    inv_val := hsb
  }

/-- The primitive coefficient `b` as a unit modulo `H=N*C`. -/
def pointedBUnit (a b : ℤ) (hab : IsCoprime a b) : (ZMod (Hmodulus a b))ˣ :=
  zmodUnitOfIntCoprime b (primitive_b_H_isCoprime hab)

/-- T4 pointed residue `r = -a b⁻¹` in the fused quotient. -/
def pointedResidue (a b : ℤ) (hab : IsCoprime a b) : ZMod (Hmodulus a b) :=
  -(a : ZMod (Hmodulus a b)) *
    (↑((pointedBUnit a b hab)⁻¹) : ZMod (Hmodulus a b))

/-- The pointed residue satisfies the defining linear equation `b r = -a`. -/
theorem pointedResidue_spec (a b : ℤ) (hab : IsCoprime a b) :
    (b : ZMod (Hmodulus a b)) * pointedResidue a b hab = -a := by
  let bu := pointedBUnit a b hab
  have hbu : (bu : ZMod (Hmodulus a b)) = (b : ZMod (Hmodulus a b)) := rfl
  have hinv : (↑(bu⁻¹) : ZMod (Hmodulus a b)) * (bu : ZMod (Hmodulus a b)) = 1 := by
    simp
  simp only [pointedResidue]
  rw [← hbu]
  calc
    (bu : ZMod (Hmodulus a b)) *
        (-(a : ZMod (Hmodulus a b)) * (↑(bu⁻¹) : ZMod (Hmodulus a b))) =
        -(a : ZMod (Hmodulus a b)) *
          ((↑(bu⁻¹) : ZMod (Hmodulus a b)) * (bu : ZMod (Hmodulus a b))) := by ring
    _ = -a := by rw [hinv]; ring

/-- T4 pointed residue is a fused root modulo `H=N*C`. -/
theorem pointedResidue_fusion_root (a b : ℤ) (hab : IsCoprime a b) :
    fusionEval (pointedResidue a b hab) = 0 := by
  let H := Hmodulus a b
  let r : ZMod H := pointedResidue a b hab
  let bu : (ZMod H)ˣ := pointedBUnit a b hab
  have hbr : (b : ZMod H) * r = -a := by
    simpa [H, r] using pointedResidue_spec a b hab
  have hbr2 : (b : ZMod H) ^ 2 * r ^ 2 = (a : ZMod H) ^ 2 := by
    calc
      (b : ZMod H) ^ 2 * r ^ 2 = ((b : ZMod H) * r) ^ 2 := by ring
      _ = (-(a : ZMod H)) ^ 2 := by rw [hbr]
      _ = (a : ZMod H) ^ 2 := by ring
  have hbr1 : (b : ZMod H) ^ 2 * r = -(a : ZMod H) * (b : ZMod H) := by
    calc
      (b : ZMod H) ^ 2 * r = (b : ZMod H) * ((b : ZMod H) * r) := by ring
      _ = (b : ZMod H) * (-(a : ZMod H)) := by rw [hbr]
      _ = -(a : ZMod H) * (b : ZMod H) := by ring
  have hNscaled :
      (b : ZMod H) ^ 2 * (r ^ 2 + 1) = (N a b : ZMod H) := by
    calc
      (b : ZMod H) ^ 2 * (r ^ 2 + 1) =
          (b : ZMod H) ^ 2 * r ^ 2 + (b : ZMod H) ^ 2 := by ring
      _ = (a : ZMod H) ^ 2 + (b : ZMod H) ^ 2 := by rw [hbr2]
      _ = (N a b : ZMod H) := by simp [N]; ring
  have hCscaled :
      (b : ZMod H) ^ 2 * (r ^ 2 + r + 1) = (C a b : ZMod H) := by
    calc
      (b : ZMod H) ^ 2 * (r ^ 2 + r + 1) =
          (b : ZMod H) ^ 2 * r ^ 2 + (b : ZMod H) ^ 2 * r +
            (b : ZMod H) ^ 2 := by ring
      _ = (a : ZMod H) ^ 2 - (a : ZMod H) * (b : ZMod H) +
            (b : ZMod H) ^ 2 := by rw [hbr2, hbr1]; ring
      _ = (C a b : ZMod H) := by simp [C]; ring
  have hprod0 : ((N a b * C a b : ℤ) : ZMod H) = 0 := by
    have hcoe : (H : ℤ) = N a b * C a b := by simpa [H] using coe_Hmodulus a b
    have hcast := congrArg (fun k : ℤ => (k : ZMod H)) hcoe
    push_cast at hcast
    simpa using hcast.symm
  have hscaled :
      (b : ZMod H) ^ 4 * fusionEval r = 0 := by
    calc
      (b : ZMod H) ^ 4 * fusionEval r =
          ((b : ZMod H) ^ 2 * (r ^ 2 + 1)) *
            ((b : ZMod H) ^ 2 * (r ^ 2 + r + 1)) := by
              simp [fusionEval]
              ring
      _ = (N a b : ZMod H) * (C a b : ZMod H) := by rw [hNscaled, hCscaled]
      _ = ((N a b * C a b : ℤ) : ZMod H) := by push_cast; rfl
      _ = 0 := hprod0
  have hbu : (bu : ZMod H) = (b : ZMod H) := rfl
  have hinv : (↑(bu⁻¹) : ZMod H) * (b : ZMod H) = 1 := by
    rw [← hbu]
    simp
  calc
    fusionEval r = 1 ^ 4 * fusionEval r := by ring
    _ = (((↑(bu⁻¹) : ZMod H) * (b : ZMod H)) ^ 4) * fusionEval r := by rw [hinv]
    _ = (↑(bu⁻¹) : ZMod H) ^ 4 * ((b : ZMod H) ^ 4 * fusionEval r) := by ring
    _ = 0 := by rw [hscaled]; ring

end EnterpriseMath.PrimeFusion
