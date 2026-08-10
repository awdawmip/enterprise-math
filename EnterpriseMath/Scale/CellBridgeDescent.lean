import EnterpriseMath.Scale.CellGapBridge
import EnterpriseMath.Scale.PrefixCompatibility
import Mathlib.Tactic

namespace EnterpriseMath.Scale

/-- Bridgeability is symmetric in the two old cells. -/
theorem cellsBridgeableAt_comm {d i e j h : ℕ} :
    cellsBridgeableAt d i e j h ↔ cellsBridgeableAt e j d i h := by
  constructor <;> rintro ⟨k, h₁, h₂⟩ <;> exact ⟨k, h₂, h₁⟩

/-- A reduced `N`-fraction in a closed gap whose endpoint denominators are `<N`
is automatically strict with respect to both endpoints. -/
theorem coprime_gridPoint_strict_in_oldGap
    {m N l ln u un : ℕ}
    (hm : 0 < m) (hmN : m < N) (hcop : m.Coprime N)
    (hln : 0 < ln) (hun : 0 < un)
    (hlnN : ln < N) (hunN : un < N)
    (hmem : fracInClosedGap l ln u un m N) :
    fracLt l ln m N ∧ fracLt m N u un := by
  unfold fracInClosedGap fracLe at hmem
  rcases hmem with ⟨hleft, hright⟩
  constructor
  · unfold fracLt
    have hne : l * N ≠ m * ln := by
      intro heq
      have hNdiv : N ∣ m * ln := by
        refine ⟨l, ?_⟩
        simpa [Nat.mul_comm] using heq.symm
      have hNln : N ∣ ln := by
        apply hcop.symm.dvd_of_dvd_mul_right
        simpa [Nat.mul_comm] using hNdiv
      have hle : N ≤ ln := Nat.le_of_dvd hln hNln
      omega
    omega
  · unfold fracLt
    have hne : m * un ≠ u * N := by
      intro heq
      have hNdiv : N ∣ m * un := by
        refine ⟨u, ?_⟩
        simpa [Nat.mul_comm] using heq
      have hNun : N ∣ un := by
        apply hcop.symm.dvd_of_dvd_mul_right
        simpa [Nat.mul_comm] using hNdiv
      have hle : N ≤ un := Nat.le_of_dvd hun hNun
      omega
    omega

/-- Ordered cell bridge descent.

The source pair is bridgeable at scale `N`, while the target pair is not. Both source
and target pairs are supplied in their own left-to-right order; the two orders need
not agree. Then some strictly smaller scale already preserves this distinction. -/
theorem ordered_cell_bridge_descend
    {sd si se sj td ti te tj N : ℕ}
    (hsd : 0 < sd) (hse : 0 < se) (htd : 0 < td) (hte : 0 < te)
    (hN : 0 < N)
    (hsi : si < sd) (hsj : sj < se) (hti : ti < td) (htj : tj < te)
    (hsdN : sd < N) (hseN : se < N) (htdN : td < N) (hteN : te < N)
    (hsourceBefore : cellBefore sd si se sj)
    (htargetBefore : cellBefore td ti te tj)
    (hsourceBridge : cellsBridgeableAt sd si se sj N)
    (htargetNoBridge : ¬ cellsBridgeableAt td ti te tj N) :
    ∃ h,
      0 < h ∧ h < N ∧
        cellsBridgeableAt sd si se sj h ∧
        ¬ cellsBridgeableAt td ti te tj h := by
  have hsourceNoN : ¬ gapHasGridPoint (si + 1) sd sj se N :=
    (cellsBridgeableAt_iff_gapNoGridPoint hsd hse hN hsi hsj hsourceBefore).1
      hsourceBridge
  have htargetHasN : gapHasGridPoint (ti + 1) td tj te N := by
    by_contra hno
    exact htargetNoBridge
      ((cellsBridgeableAt_iff_gapNoGridPoint htd hte hN hti htj htargetBefore).2 hno)
  rcases htargetHasN with ⟨m, hmGap⟩
  unfold fracInClosedGap fracLe at hmGap
  rcases hmGap with ⟨hmLeft, hmRight⟩
  have hm : 0 < m := by
    have hleftPos : 0 < (ti + 1) * N := by positivity
    by_contra hm0
    have : m = 0 := Nat.eq_zero_of_not_pos hm0
    subst m
    simp at hmLeft
  have hmN : m < N := by
    have htjN : tj * N < te * N := (Nat.mul_lt_mul_right hN).2 htj
    have hmte : m * te ≤ tj * N := hmRight
    have hmNte : m * te < N * te := lt_of_le_of_lt hmte (by
      simpa [Nat.mul_comm] using htjN)
    exact (Nat.mul_lt_mul_right hte).1 (by
      simpa [Nat.mul_comm] using hmNte)
  have hmGap' : fracInClosedGap (ti + 1) td tj te m N :=
    ⟨hmLeft, hmRight⟩
  by_cases hcop : m.Coprime N
  · have hstrict := coprime_gridPoint_strict_in_oldGap hm hmN hcop
      htd hte htdN hteN hmGap'
    obtain ⟨h, hh, hhN, htargetHasH, hsourceNoH⟩ :=
      primitive_grid_bridge_descend hm hmN hcop htdN hteN
        hstrict.1 hstrict.2 hsourceNoN
    have hsourceH : cellsBridgeableAt sd si se sj h :=
      (cellsBridgeableAt_iff_gapNoGridPoint hsd hse hh hsi hsj hsourceBefore).2
        hsourceNoH
    have htargetNoH : ¬ cellsBridgeableAt td ti te tj h := by
      intro hbridge
      exact ((cellsBridgeableAt_iff_gapNoGridPoint htd hte hh hti htj htargetBefore).1
        hbridge) htargetHasH
    exact ⟨h, hh, hhN, hsourceH, htargetNoH⟩
  · obtain ⟨h, hh, hhN, htargetHasH, hsourceNoH⟩ :=
      nonprimitive_grid_bridge_descend hm hmN hcop hmGap' hsourceNoN
    have hsourceH : cellsBridgeableAt sd si se sj h :=
      (cellsBridgeableAt_iff_gapNoGridPoint hsd hse hh hsi hsj hsourceBefore).2
        hsourceNoH
    have htargetNoH : ¬ cellsBridgeableAt td ti te tj h := by
      intro hbridge
      exact ((cellsBridgeableAt_iff_gapNoGridPoint htd hte hh hti htj htargetBefore).1
        hbridge) htargetHasH
    exact ⟨h, hh, hhN, hsourceH, htargetNoH⟩

/-- Prefix compatibility forces pairwise feasibility for every new scale `N`.
This is the local-to-global bridge theorem that combines cell-gap descent with the
old-prefix compatibility law. -/
theorem PrefixCompatible.pairwiseNewAllowed
    {N : ℕ} (hN : 2 ≤ N) {ρ : ScaleMapFamily}
    (hcompat : PrefixCompatible N ρ) : PairwiseNewAllowed ρ := by
  intro j A B hAj hBj
  have hNpos : 0 < N := by omega
  have hsourceBridge : cellsBridgeableAt A.scale A.index B.scale B.index N :=
    ⟨j, hAj, hBj⟩
  by_contra hnoTarget
  push_neg at hnoTarget
  have htargetNoBridge :
      ¬ cellsBridgeableAt A.scale (ρ A.scale A.2).1
        B.scale (ρ B.scale B.2).1 N := by
    intro hbridge
    rcases hbridge with ⟨k, hAk, hBk⟩
    exact hnoTarget k hAk hBk
  have hsourceNotOverlap : ¬ cellOverlap A.scale A.index B.scale B.index := by
    intro hov
    have himg := hcompat A B hov
    have hbridge := cellsBridgeableAt_of_overlap A.scale_pos B.scale_pos hNpos
      (ρ A.scale A.2).2 (ρ B.scale B.2).2 himg
    exact htargetNoBridge hbridge
  have htargetNotOverlap :
      ¬ cellOverlap A.scale (ρ A.scale A.2).1 B.scale (ρ B.scale B.2).1 := by
    intro hov
    exact htargetNoBridge
      (cellsBridgeableAt_of_overlap A.scale_pos B.scale_pos hNpos
        (ρ A.scale A.2).2 (ρ B.scale B.2).2 hov)
  rcases cellBefore_or_reverse_of_not_overlap hsourceNotOverlap with hsAB | hsBA
  · rcases cellBefore_or_reverse_of_not_overlap htargetNotOverlap with htAB | htBA
    · obtain ⟨h, hh, hhN, hsBridge, htNo⟩ := ordered_cell_bridge_descend
        A.scale_pos B.scale_pos A.scale_pos B.scale_pos hNpos
        A.2.2 B.2.2 (ρ A.scale A.2).2 (ρ B.scale B.2).2
        A.1.2 B.1.2 A.1.2 B.1.2 hsAB htAB hsourceBridge htargetNoBridge
      have himg := hcompat.preserves_bridge_exists A B hh hhN hsBridge
      exact htNo himg
    · obtain ⟨h, hh, hhN, hsBridge, htNoBA⟩ := ordered_cell_bridge_descend
        A.scale_pos B.scale_pos B.scale_pos A.scale_pos hNpos
        A.2.2 B.2.2 (ρ B.scale B.2).2 (ρ A.scale A.2).2
        A.1.2 B.1.2 B.1.2 A.1.2 hsAB htBA hsourceBridge
        ((cellsBridgeableAt_comm).2 htargetNoBridge)
      have himgAB := hcompat.preserves_bridge_exists A B hh hhN hsBridge
      exact htNoBA ((cellsBridgeableAt_comm).1 himgAB)
  · rcases cellBefore_or_reverse_of_not_overlap htargetNotOverlap with htAB | htBA
    · obtain ⟨h, hh, hhN, hsBridgeBA, htNo⟩ := ordered_cell_bridge_descend
        B.scale_pos A.scale_pos A.scale_pos B.scale_pos hNpos
        B.2.2 A.2.2 (ρ A.scale A.2).2 (ρ B.scale B.2).2
        B.1.2 A.1.2 A.1.2 B.1.2 hsBA htAB
        ((cellsBridgeableAt_comm).2 hsourceBridge) htargetNoBridge
      have hsBridgeAB := (cellsBridgeableAt_comm).1 hsBridgeBA
      have himg := hcompat.preserves_bridge_exists A B hh hhN hsBridgeAB
      exact htNo himg
    · obtain ⟨h, hh, hhN, hsBridgeBA, htNoBA⟩ := ordered_cell_bridge_descend
        B.scale_pos A.scale_pos B.scale_pos A.scale_pos hNpos
        B.2.2 A.2.2 (ρ B.scale B.2).2 (ρ A.scale A.2).2
        B.1.2 A.1.2 B.1.2 A.1.2 hsBA htBA
        ((cellsBridgeableAt_comm).2 hsourceBridge)
        ((cellsBridgeableAt_comm).2 htargetNoBridge)
      have hsBridgeAB := (cellsBridgeableAt_comm).1 hsBridgeBA
      have himgAB := hcompat.preserves_bridge_exists A B hh hhN hsBridgeAB
      exact htNoBA ((cellsBridgeableAt_comm).1 himgAB)

/-- R007 one-step extension theorem: every compatible prefix on scales `<N` extends
to a scale-`N` residue map preserving all old/new overlaps. -/
theorem PrefixCompatible.exists_oneStepExtension
    {N : ℕ} (hN : 2 ≤ N) {ρ : ScaleMapFamily}
    (hcompat : PrefixCompatible N ρ) :
    ∃ fN : Fin N → Fin N,
      ∀ (j : Fin N) (A : PrefixCell N),
        prefixSourceOverlap A j → prefixTargetOverlap ρ A (fN j) := by
  exact exists_oneStepExtension_of_pairwiseAllowed hN ρ (hcompat.pairwiseNewAllowed hN)

end EnterpriseMath.Scale
