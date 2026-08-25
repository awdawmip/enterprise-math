import EnterpriseMath.PrimeFusion.PointedQuotient
import EnterpriseMath.PrimeFusion.PhaseReadout

namespace EnterpriseMath.PrimeFusion

/-- Canonical integer lift of the T4 pointed residue. -/
def pointedLift (a b : ℤ) (hab : IsCoprime a b) : ℤ :=
  (pointedResidue a b hab).cast

@[simp] theorem pointedLift_cast (a b : ℤ) (hab : IsCoprime a b) :
    ((pointedLift a b hab : ℤ) : ZMod (Hmodulus a b)) = pointedResidue a b hab := by
  change (((pointedResidue a b hab).cast : ℤ) : ZMod (Hmodulus a b)) =
    pointedResidue a b hab
  exact ZMod.intCast_zmod_cast (pointedResidue a b hab)

/-- The canonical lift satisfies the source defining congruence `b*r+a=0 mod H`. -/
theorem pointedLift_linear_dvd (a b : ℤ) (hab : IsCoprime a b) :
    (Hmodulus a b : ℤ) ∣ b * pointedLift a b hab + a := by
  apply (ZMod.intCast_zmod_eq_zero_iff_dvd
    (b * pointedLift a b hab + a) (Hmodulus a b)).mp
  rw [Int.cast_add, Int.cast_mul, pointedLift_cast]
  have h := pointedResidue_spec a b hab
  linear_combination h

/-- T5 arithmetic core for any integral representative satisfying the pointed linear congruence.
The proof keeps the two channel labels ordered and cancels the primitive coefficient by exact
Bézout identities rather than by sampled modular computation. -/
theorem pointed_factor_divisibilities_of_linear {a b r : ℤ} (hab : IsCoprime a b)
    (hr : (Hmodulus a b : ℤ) ∣ b * r + a) :
    (Nmodulus a b : ℤ) ∣ gaussianEval r ∧
      (Cmodulus a b : ℤ) ∣ eisensteinEval r := by
  have hNH : (Nmodulus a b : ℤ) ∣ (Hmodulus a b : ℤ) := by
    refine ⟨(Cmodulus a b : ℤ), ?_⟩
    rw [Hmodulus_eq_mul]
    push_cast
    rfl
  have hCH : (Cmodulus a b : ℤ) ∣ (Hmodulus a b : ℤ) := by
    refine ⟨(Nmodulus a b : ℤ), ?_⟩
    rw [Hmodulus_eq_mul]
    push_cast
    ring
  have hNlinMod : (Nmodulus a b : ℤ) ∣ b * r + a := dvd_trans hNH hr
  have hClinMod : (Cmodulus a b : ℤ) ∣ b * r + a := dvd_trans hCH hr
  have hNlin : N a b ∣ b * r + a := by simpa using hNlinMod
  have hClin : C a b ∣ b * r + a := by simpa using hClinMod
  have hNscaled : N a b ∣ b ^ 2 * gaussianEval r := by
    rcases hNlin with ⟨k, hk⟩
    refine ⟨k * (b * r - a) + 1, ?_⟩
    calc
      b ^ 2 * gaussianEval r =
          (b * r + a) * (b * r - a) + N a b := by
            simp only [gaussianEval, N]
            ring
      _ = (N a b * k) * (b * r - a) + N a b := by rw [hk]
      _ = N a b * (k * (b * r - a) + 1) := by ring
  have hCscaled : C a b ∣ b ^ 2 * eisensteinEval r := by
    rcases hClin with ⟨k, hk⟩
    refine ⟨k * (b * r + b - a) + 1, ?_⟩
    calc
      b ^ 2 * eisensteinEval r =
          (b * r + a) * (b * r + b - a) + C a b := by
            simp only [eisensteinEval, C]
            ring
      _ = (C a b * k) * (b * r + b - a) + C a b := by rw [hk]
      _ = C a b * (k * (b * r + b - a) + 1) := by ring
  have hNdiv : N a b ∣ gaussianEval r := by
    rcases primitive_b_N_isCoprime hab with ⟨s, t, hst⟩
    rcases hNscaled with ⟨k, hk⟩
    refine ⟨s ^ 2 * k +
      (2 * s * t * b + t ^ 2 * N a b) * gaussianEval r, ?_⟩
    calc
      gaussianEval r = (s * b + t * N a b) ^ 2 * gaussianEval r := by
        rw [hst]
        ring
      _ = s ^ 2 * (b ^ 2 * gaussianEval r) +
          N a b * ((2 * s * t * b + t ^ 2 * N a b) * gaussianEval r) := by ring
      _ = N a b * (s ^ 2 * k +
          (2 * s * t * b + t ^ 2 * N a b) * gaussianEval r) := by
            rw [hk]
            ring
  have hCdiv : C a b ∣ eisensteinEval r := by
    rcases primitive_b_C_isCoprime hab with ⟨s, t, hst⟩
    rcases hCscaled with ⟨k, hk⟩
    refine ⟨s ^ 2 * k +
      (2 * s * t * b + t ^ 2 * C a b) * eisensteinEval r, ?_⟩
    calc
      eisensteinEval r = (s * b + t * C a b) ^ 2 * eisensteinEval r := by
        rw [hst]
        ring
      _ = s ^ 2 * (b ^ 2 * eisensteinEval r) +
          C a b * ((2 * s * t * b + t ^ 2 * C a b) * eisensteinEval r) := by ring
      _ = C a b * (s ^ 2 * k +
          (2 * s * t * b + t ^ 2 * C a b) * eisensteinEval r) := by
            rw [hk]
            ring
  constructor
  · simpa only [coe_Nmodulus] using hNdiv
  · simpa only [coe_Cmodulus] using hCdiv

/-- The T4 pointed lift carries the Gaussian and Eisenstein factors in their designated channels. -/
theorem pointed_factor_divisibilities (a b : ℤ) (hab : IsCoprime a b) :
    (Nmodulus a b : ℤ) ∣ gaussianEval (pointedLift a b hab) ∧
      (Cmodulus a b : ℤ) ∣ eisensteinEval (pointedLift a b hab) :=
  pointed_factor_divisibilities_of_linear hab (pointedLift_linear_dvd a b hab)

/-- T5 pointed channel recovery at exact source strength. -/
theorem pointed_channel_recovery (a b : ℤ) (hab : IsCoprime a b) :
    Int.gcd (Hmodulus a b : ℤ) (gaussianEval (pointedLift a b hab)) = Nmodulus a b ∧
      Int.gcd (Hmodulus a b : ℤ) (eisensteinEval (pointedLift a b hab)) = Cmodulus a b := by
  have h := pointed_factor_divisibilities a b hab
  exact exact_channel_recovery (Hmodulus_eq_mul a b) (pointedLift a b hab) h.1 h.2

/-- Integral polynomial representative of the reciprocal-trace idempotent. -/
def pointedIdempotentInt (r : ℤ) : ℤ := r ^ 3 + r ^ 2 + r + 1

/-- The Gaussian evaluation divides the integral idempotent representative. -/
theorem gaussianEval_dvd_pointedIdempotentInt (r : ℤ) :
    gaussianEval r ∣ pointedIdempotentInt r := by
  refine ⟨r + 1, ?_⟩
  dsimp [gaussianEval, pointedIdempotentInt]
  ring

/-- The Eisenstein evaluation divides `e-1`. -/
theorem eisensteinEval_dvd_pointedIdempotentInt_sub_one (r : ℤ) :
    eisensteinEval r ∣ pointedIdempotentInt r - 1 := by
  refine ⟨r, ?_⟩
  dsimp [eisensteinEval, pointedIdempotentInt]
  ring

/-- Integral lift of the T6 reciprocal-trace idempotent attached to the pointed residue. -/
def pointedIdempotentLift (a b : ℤ) (hab : IsCoprime a b) : ℤ :=
  pointedIdempotentInt (pointedLift a b hab)

/-- Pointed T6 divisibility orientation: `N|e` and `C|(e-1)`. -/
theorem pointed_idempotent_factor_divisibilities (a b : ℤ) (hab : IsCoprime a b) :
    (Nmodulus a b : ℤ) ∣ pointedIdempotentLift a b hab ∧
      (Cmodulus a b : ℤ) ∣ pointedIdempotentLift a b hab - 1 := by
  have h := pointed_factor_divisibilities a b hab
  constructor
  · exact dvd_trans h.1 (by
      simpa [pointedIdempotentLift] using
        gaussianEval_dvd_pointedIdempotentInt (pointedLift a b hab))
  · exact dvd_trans h.2 (by
      simpa [pointedIdempotentLift] using
        eisensteinEval_dvd_pointedIdempotentInt_sub_one (pointedLift a b hab))

/-- The pointed integral representative is idempotent modulo `H`. -/
theorem pointed_idempotent_congruence (a b : ℤ) (hab : IsCoprime a b) :
    (Hmodulus a b : ℤ) ∣
      pointedIdempotentLift a b hab * (pointedIdempotentLift a b hab - 1) := by
  rcases pointed_idempotent_factor_divisibilities a b hab with ⟨hN, hC⟩
  rcases hN with ⟨kN, hkN⟩
  rcases hC with ⟨kC, hkC⟩
  refine ⟨kN * kC, ?_⟩
  calc
    pointedIdempotentLift a b hab * (pointedIdempotentLift a b hab - 1) =
        ((Nmodulus a b : ℤ) * kN) * (pointedIdempotentLift a b hab - 1) := by
          exact congrArg
            (fun x : ℤ => x * (pointedIdempotentLift a b hab - 1)) hkN
    _ = ((Nmodulus a b : ℤ) * kN) * ((Cmodulus a b : ℤ) * kC) := by
          exact congrArg (fun x : ℤ => ((Nmodulus a b : ℤ) * kN) * x) hkC
    _ = (Hmodulus a b : ℤ) * (kN * kC) := by
          rw [Hmodulus_eq_mul]
          push_cast
          ring

/-- Accepted T6 strengthening specialized to the pointed primitive cell. -/
theorem pointed_idempotent_partition (a b : ℤ) (hab : IsCoprime a b) :
    Nat.Coprime
        (Int.gcd (pointedIdempotentLift a b hab) (Hmodulus a b : ℤ))
        (Int.gcd (pointedIdempotentLift a b hab - 1) (Hmodulus a b : ℤ)) ∧
      Int.gcd (pointedIdempotentLift a b hab) (Hmodulus a b : ℤ) *
        Int.gcd (pointedIdempotentLift a b hab - 1) (Hmodulus a b : ℤ) =
          Hmodulus a b :=
  idempotent_gcd_partition (pointed_idempotent_congruence a b hab)

/-- T6 pointed specialization: the two idempotent gcd factors are exactly the ordered channels. -/
theorem pointed_idempotent_channel_recovery (a b : ℤ) (hab : IsCoprime a b) :
    Int.gcd (pointedIdempotentLift a b hab) (Hmodulus a b : ℤ) = Nmodulus a b ∧
      Int.gcd (pointedIdempotentLift a b hab - 1) (Hmodulus a b : ℤ) = Cmodulus a b := by
  have h := pointed_idempotent_factor_divisibilities a b hab
  have hconsec :
      IsCoprime (pointedIdempotentLift a b hab) (pointedIdempotentLift a b hab - 1) := by
    refine ⟨1, -1, ?_⟩
    ring
  constructor
  · simpa [Int.gcd_comm] using
      (gcd_recover_left (Hmodulus_eq_mul a b) h.1 h.2 hconsec)
  · simpa [Int.gcd_comm] using
      (gcd_recover_right (Hmodulus_eq_mul a b) h.1 h.2 hconsec)

/-- The integral T6 representative reduces to the generic reciprocal-trace idempotent. -/
theorem pointedIdempotentLift_cast (a b : ℤ) (hab : IsCoprime a b) :
    ((pointedIdempotentLift a b hab : ℤ) : ZMod (Hmodulus a b)) =
      rootIdempotent (pointedResidue a b hab) := by
  rw [rootIdempotent_eq_polynomial]
  simp [pointedIdempotentLift, pointedIdempotentInt, pointedLift]

/-- The pointed reciprocal-trace idempotent is idempotent in the fused quotient. -/
theorem pointed_rootIdempotent_isIdempotent (a b : ℤ) (hab : IsCoprime a b) :
    rootIdempotent (pointedResidue a b hab) ^ 2 =
      rootIdempotent (pointedResidue a b hab) :=
  rootIdempotent_isIdempotent (pointedResidue_fusion_root a b hab)

#print axioms channel_gcd_exact
#print axioms fusionCRT
#print axioms pointedCRT
#print axioms pointedResidue_fusion_root
#print axioms pointed_channel_recovery
#print axioms pointed_idempotent_channel_recovery
#print axioms mixed_locus_order_twelve
#print axioms mixed_locus_four_orbit
#print axioms mixed_orbit_inverse_only_eleven
#print axioms dualPrime_sixth_gcd_readout
#print axioms mixed_sixth_eq_two_rootIdempotent_sub_one

end EnterpriseMath.PrimeFusion
