import EnterpriseMath.Precision.RootStateAtlasCardinality

namespace EnterpriseMath.Precision

open EnterpriseMath.IntegerRoot

/-- The positive quotient-root atlas over all positive denominator labels. -/
def rootStateAtlas (s n : ℕ) : Finset ℕ :=
  (Finset.Icc 1 n).image fun d => root (s + 1) (n / d)

/-- Every denominator label in `1..n` produces a positive quotient-root state. -/
theorem root_state_denominator_root_positive
    {s n d : ℕ}
    (_hn : 0 < n)
    (hdPos : 1 ≤ d)
    (hdN : d ≤ n) :
    1 ≤ root (s + 1) (n / d) := by
  have hQuotOne : 1 ≤ n / d := by
    apply (Nat.le_div_iff_mul_le (by omega)).2
    simpa using hdN
  exact (Nat.le_nthRoot_iff (n := s + 1) (by omega)).2 (by simpa using hQuotOne)

/-- Exact binary atlas cardinality.

Let

`H = R_(s+2)((s+1)n-1)` and `D = floor(n/(H+1)^(s+1))`.

The high branch contributes exactly `D` states; every state `1,...,H-1`
occurs; and `H` itself occurs exactly at the one-bit horizon threshold.  The
subtraction-free form also covers the exceptional `H=0` boundary uniformly. -/
theorem root_state_atlas_card_binary
    {s n : ℕ}
    (hn : 0 < n) :
    let H := root (s + 2) ((s + 1) * n - 1)
    let D := n / (H + 1) ^ (s + 1)
    (rootStateAtlas s n).card + 1 =
      D + H + (if (D + 1) * H ^ (s + 1) ≤ n then 1 else 0) := by
  let H := root (s + 2) ((s + 1) * n - 1)
  let D := n / (H + 1) ^ (s + 1)
  let f : ℕ → ℕ := fun d => root (s + 1) (n / d)
  let high : Finset ℕ := (Finset.Icc 1 D).image f
  change ((Finset.Icc 1 n).image f).card + 1 =
    D + H + (if (D + 1) * H ^ (s + 1) ≤ n then 1 else 0)

  have hDLeN : D ≤ n := by
    change n / (H + 1) ^ (s + 1) ≤ n
    exact Nat.div_le_self n ((H + 1) ^ (s + 1))

  have hAbove {d : ℕ} (hdPos : 1 ≤ d) (hdD : d ≤ D) : H < f d := by
    have h := root_state_high_denominator_above_horizon
      (s := s) (n := n) (d := d) hdPos hdD
    simpa [H, D, f] using h

  have hAtMost {d : ℕ} (hdPos : 1 ≤ d) (hDd : D < d) : f d ≤ H := by
    have h := root_state_low_denominator_at_most_horizon
      (s := s) (n := n) (d := d) hdPos hDd
    simpa [H, D, f] using h

  have hPositive {d : ℕ} (hdPos : 1 ≤ d) (hdN : d ≤ n) : 1 ≤ f d := by
    simpa [f] using
      (root_state_denominator_root_positive
        (s := s) (n := n) (d := d) hn hdPos hdN)

  have hLowExists {t : ℕ} (htPos : 0 < t) (htH : t < H) :
      ∃ d : ℕ, 1 ≤ d ∧ d ≤ n ∧ f d = t := by
    have h := root_state_low_root_realized
      (s := s) (n := n) (t := t) hn htPos
    have hex := h (by simpa [H] using htH)
    simpa [f] using hex

  have hHorizonIff :
      (∃ d : ℕ, 1 ≤ d ∧ d ≤ n ∧ f d = H) ↔
        0 < H ∧ (D + 1) * H ^ (s + 1) ≤ n := by
    simpa [H, D, f] using
      (root_state_horizon_realized_iff (s := s) (n := n) hn)

  have hHighInj : Set.InjOn f (↑(Finset.Icc 1 D) : Set ℕ) := by
    intro d hd e he hEq
    have hd' : d ∈ Finset.Icc 1 D := by simpa using hd
    have he' : e ∈ Finset.Icc 1 D := by simpa using he
    have hdB := Finset.mem_Icc.mp hd'
    have heB := Finset.mem_Icc.mp he'
    dsimp [f] at hEq
    by_contra hne
    rcases lt_or_gt_of_ne hne with hde | hed
    · exact
        (root_state_high_denominator_injective
          (s := s) (n := n) (d := d) (e := e)
          hn hdB.1 hde heB.2) hEq
    · exact
        (root_state_high_denominator_injective
          (s := s) (n := n) (d := e) (e := d)
          hn heB.1 hed hdB.2) hEq.symm

  have hHighCard : high.card = D := by
    dsimp [high]
    rw [Finset.card_image_of_injOn hHighInj]
    simp

  have hHighAboveMem {t : ℕ} (ht : t ∈ high) : H < t := by
    rcases Finset.mem_image.mp ht with ⟨d, hd, rfl⟩
    have hdB := Finset.mem_Icc.mp hd
    exact hAbove hdB.1 hdB.2

  by_cases hH0 : H = 0
  · have hD : D = n := by
      change n / (H + 1) ^ (s + 1) = n
      rw [hH0]
      simp
    have hAtlasHigh : (Finset.Icc 1 n).image f = high := by
      dsimp [high]
      rw [hD]
    rw [hAtlasHigh, hHighCard]
    simp [hH0] <;> omega

  · have hHPos : 0 < H := Nat.pos_of_ne_zero hH0
    by_cases hCarry : (D + 1) * H ^ (s + 1) ≤ n
    · have hAtlasIcc :
          (Finset.Icc 1 n).image f = high ∪ Finset.Icc 1 H := by
        ext t
        constructor
        · intro ht
          rcases Finset.mem_image.mp ht with ⟨d, hd, rfl⟩
          have hdB := Finset.mem_Icc.mp hd
          by_cases hdD : d ≤ D
          · exact Finset.mem_union.mpr <| Or.inl <| Finset.mem_image.mpr
              ⟨d, Finset.mem_Icc.mpr ⟨hdB.1, hdD⟩, rfl⟩
          · exact Finset.mem_union.mpr <| Or.inr <| Finset.mem_Icc.mpr
              ⟨hPositive hdB.1 hdB.2, hAtMost hdB.1 (by omega)⟩
        · intro ht
          rcases Finset.mem_union.mp ht with htHigh | htLow
          · rcases Finset.mem_image.mp htHigh with ⟨d, hd, rfl⟩
            have hdB := Finset.mem_Icc.mp hd
            exact Finset.mem_image.mpr
              ⟨d, Finset.mem_Icc.mpr ⟨hdB.1, le_trans hdB.2 hDLeN⟩, rfl⟩
          · have htB := Finset.mem_Icc.mp htLow
            by_cases htEq : t = H
            · subst t
              rcases hHorizonIff.2 ⟨hHPos, hCarry⟩ with ⟨d, hdPos, hdN, hRoot⟩
              exact Finset.mem_image.mpr
                ⟨d, Finset.mem_Icc.mpr ⟨hdPos, hdN⟩, hRoot⟩
            · have htPos : 0 < t := by omega
              have htH : t < H := by omega
              rcases hLowExists htPos htH with ⟨d, hdPos, hdN, hRoot⟩
              exact Finset.mem_image.mpr
                ⟨d, Finset.mem_Icc.mpr ⟨hdPos, hdN⟩, hRoot⟩

      have hDisjoint : Disjoint high (Finset.Icc 1 H) := by
        refine Finset.disjoint_left.mpr ?_
        intro t htHigh htLow
        have hAboveT := hHighAboveMem htHigh
        have hLowB := Finset.mem_Icc.mp htLow
        omega

      rw [hAtlasIcc, Finset.card_union_of_disjoint hDisjoint, hHighCard]
      simp [hCarry] <;> omega

    · have hAtlasIco :
          (Finset.Icc 1 n).image f = high ∪ Finset.Ico 1 H := by
        ext t
        constructor
        · intro ht
          rcases Finset.mem_image.mp ht with ⟨d, hd, rfl⟩
          have hdB := Finset.mem_Icc.mp hd
          by_cases hdD : d ≤ D
          · exact Finset.mem_union.mpr <| Or.inl <| Finset.mem_image.mpr
              ⟨d, Finset.mem_Icc.mpr ⟨hdB.1, hdD⟩, rfl⟩
          · have hLe : f d ≤ H := hAtMost hdB.1 (by omega)
            have hNe : f d ≠ H := by
              intro hEq
              have hExists : ∃ e : ℕ, 1 ≤ e ∧ e ≤ n ∧ f e = H :=
                ⟨d, hdB.1, hdB.2, hEq⟩
              exact hCarry (hHorizonIff.1 hExists).2
            exact Finset.mem_union.mpr <| Or.inr <| Finset.mem_Ico.mpr
              ⟨hPositive hdB.1 hdB.2, by omega⟩
        · intro ht
          rcases Finset.mem_union.mp ht with htHigh | htLow
          · rcases Finset.mem_image.mp htHigh with ⟨d, hd, rfl⟩
            have hdB := Finset.mem_Icc.mp hd
            exact Finset.mem_image.mpr
              ⟨d, Finset.mem_Icc.mpr ⟨hdB.1, le_trans hdB.2 hDLeN⟩, rfl⟩
          · have htB := Finset.mem_Ico.mp htLow
            have htPos : 0 < t := by omega
            rcases hLowExists htPos htB.2 with ⟨d, hdPos, hdN, hRoot⟩
            exact Finset.mem_image.mpr
              ⟨d, Finset.mem_Icc.mpr ⟨hdPos, hdN⟩, hRoot⟩

      have hDisjoint : Disjoint high (Finset.Ico 1 H) := by
        refine Finset.disjoint_left.mpr ?_
        intro t htHigh htLow
        have hAboveT := hHighAboveMem htHigh
        have hLowB := Finset.mem_Ico.mp htLow
        omega

      rw [hAtlasIco, Finset.card_union_of_disjoint hDisjoint, hHighCard]
      simp [hCarry] <;> omega

/-- Exact ternary threshold-to-cardinality theorem for the positive quotient-root atlas. -/
theorem root_state_atlas_card_ternary
    {s n : ℕ}
    (hn : 0 < n) :
    let H := root (s + 2) ((s + 1) * n - 1)
    let q := H / (s + 1)
    let X := (H + 1) ^ (s + 1)
    let Y := H ^ (s + 1)
    let A := max (q * X) ((q + 1) * Y)
    let B := (q + 1) * X
    let tau := if n < A then 0 else if n < B then 1 else 2
    (rootStateAtlas s n).card + 1 = H + q + tau := by
  let H := root (s + 2) ((s + 1) * n - 1)
  let D := n / (H + 1) ^ (s + 1)
  let q := H / (s + 1)
  let X := (H + 1) ^ (s + 1)
  let Y := H ^ (s + 1)
  change (rootStateAtlas s n).card + 1 =
    H + q + (if n < max (q * X) ((q + 1) * Y) then 0
      else if n < (q + 1) * X then 1 else 2)

  have hBand0 := root_state_denominator_three_point_band (s := s) (n := n) hn
  have hBand : q - 1 ≤ D ∧ D ≤ q + 1 := by
    simpa [H, D, q] using hBand0

  have hXPos : 0 < X := by
    dsimp [X]
    exact pow_pos (by omega) (s + 1)
  have hDDef : D = n / X := by rfl
  have hCellLower : D * X ≤ n := by
    rw [hDDef]
    exact Nat.div_mul_le_self n X
  have hCellUpper : n < (D + 1) * X := by
    have hDivSucc : n / X < n / X + 1 := Nat.lt_succ_self _
    have hMul := (Nat.div_lt_iff_lt_mul hXPos).1 hDivSucc
    simpa [hDDef, Nat.mul_comm] using hMul

  have hLower0 := root_state_lower_band_forces_horizon_threshold (s := s) (n := n) hn
  have hLowerForced : 1 ≤ q → D = q - 1 → (D + 1) * Y ≤ n := by
    simpa [H, D, q, Y] using hLower0

  have hUpper0 := root_state_upper_band_forces_horizon_threshold (s := s) (n := n) hn
  have hUpperForced : D = q + 1 → (D + 1) * Y ≤ n := by
    simpa [H, D, q, Y] using hUpper0

  have hCount0 := root_state_atlas_card_binary (s := s) (n := n) hn
  have hCount :
      (rootStateAtlas s n).card + 1 =
        D + H + (if (D + 1) * Y ≤ n then 1 else 0) := by
    simpa [H, D, Y] using hCount0

  have hTernary := ternary_count_from_binary_carry
    (n := n) (D := D) (q := q) (X := X) (Y := Y)
    (H := H) (N := (rootStateAtlas s n).card)
    hBand.1 hBand.2 hCellLower hCellUpper hLowerForced hUpperForced hCount
  simpa using hTernary

end EnterpriseMath.Precision
