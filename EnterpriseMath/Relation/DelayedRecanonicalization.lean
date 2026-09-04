import Mathlib.Tactic

namespace EnterpriseMath.DelayedRecanonicalization

noncomputable section

/-- Root/mean energy after one stopped/core scattering step. -/
def rootOut (s root : ℝ) : ℝ := (1 - 2 * s) ^ 2 * root

/-- Retained standard energy after one step with mixer survival `gamma`. -/
def standardOut (gamma s root standard : ℝ) : ℝ :=
  4 * gamma * s * (1 - s) * root + s * standard

/-- A general positive two-channel energy. -/
def coneEnergy (lambda root standard : ℝ) : ℝ :=
  root + lambda * standard

/-- Terminally canonical two-channel energy. -/
def terminalEnergy (gamma root standard : ℝ) : ℝ :=
  root + standard / gamma

/-- Exact orthogonal stopped/core partition. -/
theorem stoppedCore_partition (s : ℝ) :
    (1 - 2 * s) ^ 2 + 4 * s * (1 - s) = 1 := by
  ring

/-- One step is exactly nonexpansive in the terminal energy. -/
theorem terminalEnergy_step
    {gamma : ℝ} (hgamma : gamma ≠ 0)
    (s root standard : ℝ) :
    terminalEnergy gamma (rootOut s root)
        (standardOut gamma s root standard) =
      root + s * (standard / gamma) := by
  unfold terminalEnergy rootOut standardOut
  field_simp [hgamma]
  ring

/-- The one-step energy defect is precisely the stopped part of the old standard channel. -/
theorem terminalEnergy_step_defect
    {gamma : ℝ} (hgamma : gamma ≠ 0)
    (s root standard : ℝ) :
    terminalEnergy gamma root standard -
        terminalEnergy gamma (rootOut s root)
          (standardOut gamma s root standard) =
      (1 - s) * (standard / gamma) := by
  rw [terminalEnergy_step hgamma]
  unfold terminalEnergy
  ring

/-- Exact two-step hypocoercive terminal-energy formula. -/
theorem terminalEnergy_twoStep
    {gamma : ℝ} (hgamma : gamma ≠ 0)
    (s₁ s₂ root standard : ℝ) :
    terminalEnergy gamma
        (rootOut s₂ (rootOut s₁ root))
        (standardOut gamma s₂ (rootOut s₁ root)
          (standardOut gamma s₁ root standard)) =
      (1 - 4 * (1 - s₂) * s₁ * (1 - s₁)) * root +
        s₁ * s₂ * (standard / gamma) := by
  unfold terminalEnergy rootOut standardOut
  field_simp [hgamma]
  ring

/-- Exact positive two-step dissipation identity. -/
theorem terminalEnergy_twoStep_defect
    {gamma : ℝ} (hgamma : gamma ≠ 0)
    (s₁ s₂ root standard : ℝ) :
    terminalEnergy gamma root standard -
        terminalEnergy gamma
          (rootOut s₂ (rootOut s₁ root))
          (standardOut gamma s₂ (rootOut s₁ root)
            (standardOut gamma s₁ root standard)) =
      4 * (1 - s₂) * s₁ * (1 - s₁) * root +
        (1 - s₁ * s₂) * (standard / gamma) := by
  rw [terminalEnergy_twoStep hgamma]
  unfold terminalEnergy
  ring

/-- The balanced row forces the inverse mixer weight in every positive root recovery. -/
theorem balanced_recovery_forces_inverse
    {gamma lambda : ℝ}
    (hrecover :
      coneEnergy lambda (rootOut (1 / 2 : ℝ) 1)
          (standardOut gamma (1 / 2 : ℝ) 1 0) ≥ 1) :
    1 ≤ lambda * gamma := by
  norm_num [coneEnergy, rootOut, standardOut] at hrecover ⊢
  nlinarith

/--
Conditional odd-triangle energy equals twice the parent root energy, twice the
child root-plus-variance energy, and one explicit signless-residual correction.
-/
theorem oddTriangle_childTerminal_identity
    (x y conditionalMean variance : ℝ) :
    (x + y) ^ 2 + ((x + conditionalMean) ^ 2 + variance) +
        ((y + conditionalMean) ^ 2 + variance) =
      2 * x ^ 2 + 2 * (y ^ 2 + variance) +
        2 * (y + conditionalMean) *
          ((y + conditionalMean) + x - y) := by
  ring

/-- With zero conditional signless residual, the terminal identity is exact. -/
theorem oddTriangle_childTerminal_residualFree
    (x y conditionalMean variance : ℝ)
    (hresidual : y + conditionalMean = 0) :
    (x + y) ^ 2 + ((x + conditionalMean) ^ 2 + variance) +
        ((y + conditionalMean) ^ 2 + variance) =
      2 * x ^ 2 + 2 * (y ^ 2 + variance) := by
  rw [oddTriangle_childTerminal_identity]
  rw [hresidual]
  ring

/-- In the residual-free case, child terminal energy is at most half the odd simplex. -/
theorem childTerminal_le_half_oddTriangle
    (x y conditionalMean variance : ℝ)
    (hresidual : y + conditionalMean = 0) :
    y ^ 2 + variance ≤
      ((x + y) ^ 2 + ((x + conditionalMean) ^ 2 + variance) +
        ((y + conditionalMean) ^ 2 + variance)) / 2 := by
  have hidentity :=
    oddTriangle_childTerminal_residualFree
      x y conditionalMean variance hresidual
  nlinarith [sq_nonneg x]

/-- Root Mellin coefficient. -/
def mellinA (beta : ℝ) : ℝ :=
  1 / (1 - beta) - 4 / (2 - beta) + 4 / (3 - beta)

/-- Standard diagonal Mellin coefficient. -/
def mellinB (beta : ℝ) : ℝ := 1 / (2 - beta)

/-- Unmixed stopped/core contrast Mellin coefficient. -/
def mellinD (beta : ℝ) : ℝ :=
  4 * (1 / (2 - beta) - 1 / (3 - beta))

/-- Recanonicalizing the complete local split recovers the critical Hardy coefficient. -/
theorem mellinA_add_mellinD
    {beta : ℝ}
    (h₁ : 1 - beta ≠ 0)
    (h₂ : 2 - beta ≠ 0)
    (h₃ : 3 - beta ≠ 0) :
    mellinA beta + mellinD beta = 1 / (1 - beta) := by
  unfold mellinA mellinD
  field_simp [h₁, h₂, h₃]
  ring

/-- Two-step terminal root coefficient. -/
def twoStepRootCoefficient (beta : ℝ) : ℝ :=
  mellinA beta ^ 2 +
    mellinD beta * (mellinA beta + mellinB beta)

/-- Exact rational Mellin data at the safe exponent `1/6`. -/
theorem beta_oneSixth_mellinA :
    mellinA (1 / 6 : ℝ) = 402 / 935 := by
  norm_num [mellinA]

theorem beta_oneSixth_mellinB :
    mellinB (1 / 6 : ℝ) = 6 / 11 := by
  norm_num [mellinB]

theorem beta_oneSixth_mellinD :
    mellinD (1 / 6 : ℝ) = 144 / 187 := by
  norm_num [mellinD]

/-- Exact two-step contraction coefficient at exponent `1/6`. -/
theorem beta_oneSixth_twoStep :
    twoStepRootCoefficient (1 / 6 : ℝ) = 48132 / 51425 := by
  norm_num [twoStepRootCoefficient, mellinA, mellinB, mellinD]

theorem beta_oneSixth_twoStep_lt_one :
    twoStepRootCoefficient (1 / 6 : ℝ) < 1 := by
  rw [beta_oneSixth_twoStep]
  norm_num

end

end EnterpriseMath.DelayedRecanonicalization
