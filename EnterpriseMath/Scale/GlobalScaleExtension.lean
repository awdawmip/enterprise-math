import EnterpriseMath.Scale.FinitePrefixExtension
import Mathlib.Tactic

namespace EnterpriseMath.Scale

/-- A compatible scale-map state through all scales `<N`. -/
def CompatibleState (N : ℕ) :=
  {ρ : ScaleMapFamily // PrefixCompatible N ρ}

/-- Choose one compatible successor state. The choice is noncomputable, but the
one-step theorem guarantees existence and exact preservation of every old scale. -/
noncomputable def nextCompatibleState {N : ℕ} (hN : 2 ≤ N)
    (S : CompatibleState N) : CompatibleState (N + 1) := by
  obtain ⟨ρ', hρ', _hpres⟩ := S.2.exists_successor_family hN
  exact ⟨ρ', hρ'⟩

/-- The chosen successor state agrees with its predecessor on every old scale. -/
theorem nextCompatibleState_preserves {N : ℕ} (hN : 2 ≤ N)
    (S : CompatibleState N) {d : ℕ} (hd : d < N) :
    (nextCompatibleState hN S).1 d = S.1 d := by
  unfold nextCompatibleState
  split
  next h =>
    exact h.2 d hd

/-- Coherent recursively chosen compatible prefixes. State `t` is compatible through
horizon `N+t`. -/
noncomputable def compatibleStateSeq {N : ℕ} (hN : 2 ≤ N)
    (S₀ : CompatibleState N) : ∀ t : ℕ, CompatibleState (N + t)
  | 0 => by simpa using S₀
  | t + 1 => by
      have hNt : 2 ≤ N + t := by omega
      simpa [Nat.add_assoc] using
        nextCompatibleState hNt (compatibleStateSeq hN S₀ t)

/-- One recursion step preserves every scale already present in the prefix. -/
theorem compatibleStateSeq_succ_preserves {N : ℕ} (hN : 2 ≤ N)
    (S₀ : CompatibleState N) {t d : ℕ} (hd : d < N + t) :
    (compatibleStateSeq hN S₀ (t + 1)).1 d =
      (compatibleStateSeq hN S₀ t).1 d := by
  have hNt : 2 ≤ N + t := by omega
  simpa [compatibleStateSeq, Nat.add_assoc] using
    nextCompatibleState_preserves hNt (compatibleStateSeq hN S₀ t) hd

/-- Once a scale has entered the prefix, its map is stable at every later state. -/
theorem compatibleStateSeq_stable {N : ℕ} (hN : 2 ≤ N)
    (S₀ : CompatibleState N) {t u d : ℕ}
    (htu : t ≤ u) (hd : d < N + t) :
    (compatibleStateSeq hN S₀ u).1 d =
      (compatibleStateSeq hN S₀ t).1 d := by
  induction u, htu using Nat.le_induction with
  | base => rfl
  | succ u htu ih =>
      have hdu : d < N + u := by omega
      calc
        (compatibleStateSeq hN S₀ (u + 1)).1 d =
            (compatibleStateSeq hN S₀ u).1 d :=
          compatibleStateSeq_succ_preserves hN S₀ hdu
        _ = (compatibleStateSeq hN S₀ t).1 d := ih

/-- First recursion stage whose horizon contains scale `d`. For old scales this is
zero; for new scales it is `d+1-N`. -/
def firstContainingStage (N d : ℕ) : ℕ :=
  d + 1 - N

/-- The first containing stage really contains scale `d`. -/
theorem lt_horizon_firstContainingStage {N d : ℕ} (hN : 1 ≤ N) :
    d < N + firstContainingStage N d := by
  unfold firstContainingStage
  by_cases hd : d < N
  · have hz : d + 1 - N = 0 := by omega
    simp [hz, hd]
  · omega

/-- A global scale family obtained by reading each scale at the first compatible state
that contains it. Coherence makes this equal to every later reading. -/
noncomputable def globalScaleExtension {N : ℕ} (hN : 2 ≤ N)
    (S₀ : CompatibleState N) : ScaleMapFamily := fun d =>
  (compatibleStateSeq hN S₀ (firstContainingStage N d)).1 d

/-- Global readings agree with every later compatible state that already contains the
scale. -/
theorem globalScaleExtension_eq_state {N : ℕ} (hN : 2 ≤ N)
    (S₀ : CompatibleState N) {t d : ℕ} (hd : d < N + t) :
    globalScaleExtension hN S₀ d = (compatibleStateSeq hN S₀ t).1 d := by
  let s := firstContainingStage N d
  have hds : d < N + s := lt_horizon_firstContainingStage (by omega) 
  have hst : s ≤ t := by
    unfold s firstContainingStage
    omega
  unfold globalScaleExtension
  exact (compatibleStateSeq_stable hN S₀ hst hds).symm

/-- The global extension preserves every map from the original compatible prefix. -/
theorem globalScaleExtension_preserves_initial {N : ℕ} (hN : 2 ≤ N)
    (S₀ : CompatibleState N) {d : ℕ} (hd : d < N) :
    globalScaleExtension hN S₀ d = S₀.1 d := by
  have hstage : firstContainingStage N d = 0 := by
    unfold firstContainingStage
    omega
  simp [globalScaleExtension, hstage, compatibleStateSeq]

/-- Full all-scale overlap compatibility. -/
def AllScalesCompatible (ρ : ScaleMapFamily) : Prop :=
  ∀ d e : ℕ, ∀ i : Fin d, ∀ j : Fin e,
    cellOverlap d i.1 e j.1 →
      cellOverlap d (ρ d i).1 e (ρ e j).1

/-- The coherent recursive limit is compatible on all finite scales simultaneously. -/
theorem globalScaleExtension_allCompatible {N : ℕ} (hN : 2 ≤ N)
    (S₀ : CompatibleState N) :
    AllScalesCompatible (globalScaleExtension hN S₀) := by
  intro d e i j hij
  let t := d + e + 1
  have hdH : d < N + t := by dsimp [t]; omega
  have heH : e < N + t := by dsimp [t]; omega
  let A : PrefixCell (N + t) := ⟨⟨d, hdH⟩, i⟩
  let B : PrefixCell (N + t) := ⟨⟨e, heH⟩, j⟩
  have hprefix : PrefixCompatible (N + t) (compatibleStateSeq hN S₀ t).1 :=
    (compatibleStateSeq hN S₀ t).2
  have himg := hprefix A B (by simpa [A, B] using hij)
  have hdEq := globalScaleExtension_eq_state hN S₀ hdH
  have heEq := globalScaleExtension_eq_state hN S₀ heH
  simpa [A, B, hdEq, heEq] using himg

/-- Global extension theorem: every compatible finite prefix of horizon `N>=2` extends
to one single all-scale compatible family, without changing any old scale. -/
theorem PrefixCompatible.exists_global_extension
    {N : ℕ} (hN : 2 ≤ N) {ρ : ScaleMapFamily}
    (hcompat : PrefixCompatible N ρ) :
    ∃ ρ∞ : ScaleMapFamily,
      AllScalesCompatible ρ∞ ∧
      (∀ d, d < N → ρ∞ d = ρ d) := by
  let S₀ : CompatibleState N := ⟨ρ, hcompat⟩
  refine ⟨globalScaleExtension hN S₀,
    globalScaleExtension_allCompatible hN S₀, ?_⟩
  intro d hd
  exact globalScaleExtension_preserves_initial hN S₀ hd

/-- R007 exact finite obstruction cutoff: compatibility through scales `≤r` is already
sufficient for a single global natural residue family. No scale above `r` can create a
new obstruction. -/
theorem compatible_through_r_iff_global_extension
    {r : ℕ} (hr : 1 ≤ r) {ρ : ScaleMapFamily} :
    PrefixCompatible (r + 1) ρ ↔
      ∃ ρ∞ : ScaleMapFamily,
        AllScalesCompatible ρ∞ ∧
        (∀ d, d ≤ r → ρ∞ d = ρ d) := by
  constructor
  · intro hcompat
    obtain ⟨ρ∞, hall, hpres⟩ :=
      hcompat.exists_global_extension (N := r + 1) (by omega)
    exact ⟨ρ∞, hall, fun d hdr => hpres d (by omega)⟩
  · rintro ⟨ρ∞, hall, hpres⟩
    intro A B hAB
    have himg := hall A.scale B.scale A.2 B.2 hAB
    have hAeq : ρ∞ A.scale = ρ A.scale := hpres A.scale (by omega)
    have hBeq : ρ∞ B.scale = ρ B.scale := hpres B.scale (by omega)
    simpa [hAeq, hBeq] using himg

end EnterpriseMath.Scale
