import EnterpriseMath.Scale.CellBridgeDescent
import Mathlib.Tactic

namespace EnterpriseMath.Scale

/-- Cell overlap is symmetric. -/
theorem cellOverlap_comm {d i e j : ℕ} :
    cellOverlap d i e j ↔ cellOverlap e j d i := by
  unfold cellOverlap
  tauto

/-- At one positive scale, two half-open cells overlap in positive length exactly when
they are the same cell. -/
theorem cellOverlap_same_scale_iff {d i j : ℕ} (hd : 0 < d) :
    cellOverlap d i d j ↔ i = j := by
  constructor
  · rintro ⟨h₁, h₂⟩
    have hij : i < j + 1 := by
      have : i * d < (j + 1) * d := h₁
      exact (Nat.mul_lt_mul_right hd).1 this
    have hji : j < i + 1 := by
      have : j * d < (i + 1) * d := h₂
      exact (Nat.mul_lt_mul_right hd).1 this
    omega
  · rintro rfl
    unfold cellOverlap
    constructor <;> exact (Nat.mul_lt_mul_right hd).2 (Nat.lt_succ_self _)

/-- Update exactly one scale map in a total scale-map family. -/
def setScaleMap (ρ : ScaleMapFamily) (N : ℕ) (fN : Fin N → Fin N) :
    ScaleMapFamily :=
  Function.update ρ N fN

@[simp]
theorem setScaleMap_same (ρ : ScaleMapFamily) (N : ℕ) (fN : Fin N → Fin N) :
    setScaleMap ρ N fN N = fN := by
  simp [setScaleMap]

@[simp]
theorem setScaleMap_of_ne (ρ : ScaleMapFamily) (N d : ℕ)
    (fN : Fin N → Fin N) (h : d ≠ N) :
    setScaleMap ρ N fN d = ρ d := by
  simp [setScaleMap, h]

/-- Writing a valid one-step extension map into scale `N` upgrades a compatible prefix
`<N` to a compatible prefix `<N+1`. -/
theorem PrefixCompatible.setScaleMap_succ
    {N : ℕ} (hN : 2 ≤ N) {ρ : ScaleMapFamily}
    (hcompat : PrefixCompatible N ρ)
    {fN : Fin N → Fin N}
    (hExt : ∀ (j : Fin N) (A : PrefixCell N),
      prefixSourceOverlap A j → prefixTargetOverlap ρ A (fN j)) :
    PrefixCompatible (N + 1) (setScaleMap ρ N fN) := by
  intro A B hAB
  have hNpos : 0 < N := by omega
  by_cases hA : A.scale = N
  · by_cases hB : B.scale = N
    · have hidx : A.index = B.index := by
        have hs : cellOverlap N A.index N B.index := by simpa [hA, hB] using hAB
        exact (cellOverlap_same_scale_iff hNpos).1 hs
      have hAmap : (setScaleMap ρ N fN A.scale A.2).1 = (fN ⟨A.index, by simpa [hA] using A.2.2⟩).1 := by
        subst hA
        simp [setScaleMap]
      have hBmap : (setScaleMap ρ N fN B.scale B.2).1 = (fN ⟨B.index, by simpa [hB] using B.2.2⟩).1 := by
        subst hB
        simp [setScaleMap]
      have heqMap : (setScaleMap ρ N fN A.scale A.2).1 =
          (setScaleMap ρ N fN B.scale B.2).1 := by
        rw [hAmap, hBmap, hidx]
      subst hA
      subst hB
      apply (cellOverlap_same_scale_iff hNpos).2
      exact heqMap
    · have hBlt : B.scale < N := by omega
      let Bold : PrefixCell N := ⟨⟨B.scale, hBlt⟩, B.2⟩
      let j : Fin N := ⟨A.index, by simpa [hA] using A.2.2⟩
      have hsource : prefixSourceOverlap Bold j := by
        unfold prefixSourceOverlap
        apply (cellOverlap_comm).1
        simpa [Bold, j, hA] using hAB
      have htarget := hExt j Bold hsource
      unfold prefixTargetOverlap at htarget
      have htargetSymm := (cellOverlap_comm).2 htarget
      subst hA
      simpa [setScaleMap, Bold, j, hB] using htargetSymm
  · have hAlt : A.scale < N := by omega
    let Aold : PrefixCell N := ⟨⟨A.scale, hAlt⟩, A.2⟩
    by_cases hB : B.scale = N
    · let j : Fin N := ⟨B.index, by simpa [hB] using B.2.2⟩
      have hsource : prefixSourceOverlap Aold j := by
        unfold prefixSourceOverlap
        simpa [Aold, j, hB] using hAB
      have htarget := hExt j Aold hsource
      unfold prefixTargetOverlap at htarget
      subst hB
      simpa [setScaleMap, Aold, j, hA] using htarget
    · have hBlt : B.scale < N := by omega
      let Bold : PrefixCell N := ⟨⟨B.scale, hBlt⟩, B.2⟩
      have hold : cellOverlap Aold.scale Aold.index Bold.scale Bold.index := by
        simpa [Aold, Bold] using hAB
      have himg := hcompat Aold Bold hold
      simpa [setScaleMap, Aold, Bold, hA, hB] using himg

/-- Every compatible prefix through scales `<N` admits a compatible successor prefix
through scales `<N+1`. -/
theorem PrefixCompatible.exists_successor_family
    {N : ℕ} (hN : 2 ≤ N) {ρ : ScaleMapFamily}
    (hcompat : PrefixCompatible N ρ) :
    ∃ ρ' : ScaleMapFamily,
      PrefixCompatible (N + 1) ρ' ∧
      (∀ d, d < N → ρ' d = ρ d) := by
  obtain ⟨fN, hExt⟩ := hcompat.exists_oneStepExtension hN
  refine ⟨setScaleMap ρ N fN, hcompat.setScaleMap_succ hN hExt, ?_⟩
  intro d hdN
  exact setScaleMap_of_ne ρ N d fN (by omega)

end EnterpriseMath.Scale
