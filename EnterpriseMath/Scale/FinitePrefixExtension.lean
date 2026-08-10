import EnterpriseMath.Scale.PrefixExtensionStep
import Mathlib.Tactic

namespace EnterpriseMath.Scale

/-- Compatibility is monotone under restricting the prefix horizon. -/
theorem PrefixCompatible.mono {N M : ℕ} {ρ : ScaleMapFamily}
    (hNM : N ≤ M) (hcompat : PrefixCompatible M ρ) :
    PrefixCompatible N ρ := by
  intro A B hAB
  let liftCell : PrefixCell N → PrefixCell M := fun C =>
    ⟨⟨C.scale, lt_of_lt_of_le C.1.2 hNM⟩, C.2⟩
  have h := hcompat (liftCell A) (liftCell B) (by simpa [liftCell] using hAB)
  simpa [liftCell] using h

/-- Iterating the one-step theorem extends any compatible prefix to every larger finite
horizon while leaving the original prefix maps unchanged. -/
theorem PrefixCompatible.exists_extension_to
    {N M : ℕ} (hN : 2 ≤ N) (hNM : N ≤ M)
    {ρ : ScaleMapFamily} (hcompat : PrefixCompatible N ρ) :
    ∃ ρ' : ScaleMapFamily,
      PrefixCompatible M ρ' ∧
      (∀ d, d < N → ρ' d = ρ d) := by
  induction M, hNM using Nat.le_induction with
  | base =>
      exact ⟨ρ, hcompat, fun _ _ => rfl⟩
  | succ M hNM ih =>
      obtain ⟨ρM, hcompatM, hpresM⟩ := ih
      have hM : 2 ≤ M := le_trans hN hNM
      obtain ⟨ρS, hcompatS, hpresStep⟩ :=
        hcompatM.exists_successor_family hM
      refine ⟨ρS, hcompatS, ?_⟩
      intro d hdN
      calc
        ρS d = ρM d := hpresStep d (lt_of_lt_of_le hdN hNM)
        _ = ρ d := hpresM d hdN

/-- In particular, a prefix compatible through scales `≤r` (horizon `r+1`) extends
consistently to every later finite horizon. This is the finite-horizon form of the
R007 exact cutoff `N_r=r`. -/
theorem compatible_through_r_extends_to_every_finite_horizon
    {r M : ℕ} (hr : 1 ≤ r) (hM : r + 1 ≤ M)
    {ρ : ScaleMapFamily} (hcompat : PrefixCompatible (r + 1) ρ) :
    ∃ ρ' : ScaleMapFamily,
      PrefixCompatible M ρ' ∧
      (∀ d, d ≤ r → ρ' d = ρ d) := by
  obtain ⟨ρ', hρ', hpres⟩ :=
    hcompat.exists_extension_to (N := r + 1) (M := M) (by omega) hM
  refine ⟨ρ', hρ', ?_⟩
  intro d hdr
  exact hpres d (by omega)

end EnterpriseMath.Scale
