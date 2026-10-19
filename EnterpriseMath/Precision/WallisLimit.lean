import EnterpriseMath.Precision.WallisPrecision
import Mathlib.Topology.Instances.Real.Lemmas

namespace EnterpriseMath.Precision

open Filter Set
open scoped Topology

/-- Real-valued view of the exact rational Wallis lower approximants. -/
def wallisPartialReal (n : ℕ) : ℝ := (wallisPartial n : ℝ)

/-- Real-valued view of the exact rational Wallis upper approximants. -/
def wallisUpperReal (n : ℕ) : ℝ := (wallisUpper n : ℝ)

/-- Real-valued view of the target-free upper prefactor. -/
def wallisUpperFactorReal (n : ℕ) : ℝ := (wallisUpperFactor n : ℝ)

/-- The real upper approximant is the lower approximant times its explicit prefactor. -/
theorem wallisUpperReal_eq_mul (n : ℕ) :
    wallisUpperReal n = wallisPartialReal n * wallisUpperFactorReal n := by
  simp [wallisUpperReal, wallisPartialReal, wallisUpperFactorReal, wallisUpper]

/-- The real Wallis lower approximants are strictly increasing. -/
theorem wallisPartialReal_strictMono : StrictMono wallisPartialReal := by
  refine strictMono_nat_of_lt_succ fun n => ?_
  unfold wallisPartialReal
  exact_mod_cast wallisPartial_strictMono_step n

/-- The real Wallis upper approximants are strictly decreasing. -/
theorem wallisUpperReal_strictAnti : StrictAnti wallisUpperReal := by
  refine strictAnti_nat_of_succ_lt fun n => ?_
  unfold wallisUpperReal
  exact_mod_cast wallisUpper_strictAnti_step n

/-- Every real Wallis lower approximant is positive. -/
theorem wallisPartialReal_pos (n : ℕ) : 0 < wallisPartialReal n := by
  unfold wallisPartialReal
  exact_mod_cast wallisPartial_pos n

/-- Pointwise lower/upper separation after embedding the rational certificate in `ℝ`. -/
theorem wallisPartialReal_lt_upperReal (n : ℕ) :
    wallisPartialReal n < wallisUpperReal n := by
  unfold wallisPartialReal wallisUpperReal
  exact_mod_cast wallisPartial_lt_upper n

/-- The lower sequence is bounded above by the initial upper envelope. -/
theorem wallisPartialReal_bddAbove : BddAbove (range wallisPartialReal) := by
  refine ⟨wallisUpperReal 0, ?_⟩
  rintro x ⟨n, rfl⟩
  exact (wallisPartialReal_lt_upperReal n).le.trans
    (wallisUpperReal_strictAnti.antitone (Nat.zero_le n))

/-- The internally defined Wallis completion, with no primitive `pi` input. -/
noncomputable def wallisLimit : ℝ := sSup (range wallisPartialReal)

/-- WSR-L25: the exact Wallis lower products converge to the internal completion. -/
theorem wallisPartialReal_tendsto :
    Tendsto wallisPartialReal atTop (𝓝 wallisLimit) := by
  unfold wallisLimit
  rw [sSup_range]
  exact tendsto_atTop_ciSup wallisPartialReal_strictMono.monotone wallisPartialReal_bddAbove

/-- The explicit upper prefactor is `1 + 1/(4n+1)` over the reals. -/
theorem wallisUpperFactorReal_eq_one_add (n : ℕ) :
    wallisUpperFactorReal n = 1 + 1 / (4 * (n : ℝ) + 1) := by
  unfold wallisUpperFactorReal
  rw [wallisUpperFactor_eq_one_add]
  push_cast
  rfl

/-- The target-free upper prefactor converges to one. -/
theorem wallisUpperFactorReal_tendsto_one :
    Tendsto wallisUpperFactorReal atTop (𝓝 1) := by
  have hden : Tendsto (fun n : ℕ => 4 * (n : ℝ) + 1) atTop atTop := by
    apply tendsto_atTop_add_const_right
    exact tendsto_natCast_atTop_atTop.const_mul_atTop (by norm_num)
  have hinv : Tendsto (fun n : ℕ => (4 * (n : ℝ) + 1)⁻¹) atTop (𝓝 0) :=
    tendsto_inv_atTop_zero.comp hden
  have hadd : Tendsto (fun n : ℕ => 1 + (4 * (n : ℝ) + 1)⁻¹) atTop (𝓝 1) := by
    simpa using tendsto_const_nhds.add hinv
  apply hadd.congr'
  filter_upwards with n
  rw [wallisUpperFactorReal_eq_one_add]
  simp [one_div]

/-- WSR-L26: the rational upper envelopes converge to the same internal completion. -/
theorem wallisUpperReal_tendsto :
    Tendsto wallisUpperReal atTop (𝓝 wallisLimit) := by
  have h :
      Tendsto (fun n => wallisPartialReal n * wallisUpperFactorReal n)
        atTop (𝓝 wallisLimit) := by
    simpa using wallisPartialReal_tendsto.mul wallisUpperFactorReal_tendsto_one
  exact h.congr' <| Filter.Eventually.of_forall fun n => (wallisUpperReal_eq_mul n).symm

/-- Every finite lower approximant lies below the internal completion. -/
theorem wallisPartialReal_le_limit (n : ℕ) :
    wallisPartialReal n ≤ wallisLimit := by
  unfold wallisLimit
  exact le_csSup wallisPartialReal_bddAbove ⟨n, rfl⟩

/-- In fact every finite lower approximant lies strictly below the completion. -/
theorem wallisPartialReal_lt_limit (n : ℕ) :
    wallisPartialReal n < wallisLimit := by
  exact (wallisPartialReal_strictMono (Nat.lt_succ_self n)).trans_le
    (wallisPartialReal_le_limit (n + 1))

/-- Every finite upper envelope bounds the internal completion from above. -/
theorem wallisLimit_le_upperReal (n : ℕ) :
    wallisLimit ≤ wallisUpperReal n := by
  unfold wallisLimit
  refine csSup_le (range_nonempty wallisPartialReal) ?_
  rintro x ⟨m, rfl⟩
  rcases le_total m n with hmn | hnm
  · exact (wallisPartialReal_strictMono.monotone hmn).trans
      (wallisPartialReal_lt_upperReal n).le
  · exact (wallisPartialReal_lt_upperReal m).le.trans
      (wallisUpperReal_strictAnti.antitone hnm)

/-- WSR-L27: exact finite target-free Wallis squeeze relative to the internal completion. -/
theorem wallisLimit_ratio_bounds (n : ℕ) :
    1 < wallisLimit / wallisPartialReal n ∧
      wallisLimit / wallisPartialReal n ≤ wallisUpperFactorReal n := by
  have hp : 0 < wallisPartialReal n := wallisPartialReal_pos n
  constructor
  · exact (one_lt_div₀ hp).2 (wallisPartialReal_lt_limit n)
  · apply (div_le_iff₀ hp).2
    rw [mul_comm, ← wallisUpperReal_eq_mul]
    exact wallisLimit_le_upperReal n

end EnterpriseMath.Precision
