import EnterpriseMath.Relation.BRCK4OptimalExtractionCore

namespace EnterpriseMath.BranchRecoalescence

/-- Doubled lower endpoint for the A-coordinate in the AB/CD matching face. -/
private def k4ABCDLower (n : K4Capacity) : ℕ :=
  max (2 * (n.ab - n.bd))
    (max (2 * (n.ab - n.bc))
      (2 * n.ab + n.cd - n.bd - n.bc))

/-- Doubled upper endpoint for the same matching-face interval. -/
private def k4ABCDUpper (n : K4Capacity) : ℕ :=
  min (2 * n.ab)
    (min (2 * n.ac)
      (min (2 * n.ad) (n.ac + n.ad - n.cd)))

/-- Smallest integer A-coordinate whose double reaches the lower endpoint. -/
private def k4ABCDA (n : K4Capacity) : ℕ := (k4ABCDLower n + 1) / 2

private theorem k4CeilHalf_bounds (x : ℕ) :
    x ≤ 2 * ((x + 1) / 2) ∧ 2 * ((x + 1) / 2) ≤ x + 1 := by
  omega

private theorem k4ABCDLower_le_upper (n : K4Capacity)
    (h1 : n.ab + n.cd ≤ n.ac + n.bd)
    (h2 : n.ab + n.cd ≤ n.ad + n.bc)
    (h3 : n.ab + n.cd ≤ n.ab + n.ac + n.ad)
    (h4 : n.ab + n.cd ≤ n.ab + n.bc + n.bd)
    (h5 : n.ab + n.cd ≤ n.ac + n.bc + n.cd)
    (h6 : n.ab + n.cd ≤ n.ad + n.bd + n.cd) :
    k4ABCDLower n ≤ k4ABCDUpper n := by
  unfold k4ABCDLower k4ABCDUpper
  apply le_min
  · apply max_le
    · omega
    · apply max_le <;> omega
  · apply le_min
    · apply max_le
      · omega
      · apply max_le <;> omega
    · apply le_min
      · apply max_le
        · omega
        · apply max_le <;> omega
      · apply max_le
        · omega
        · apply max_le <;> omega

private theorem k4ABCDLower_first_le (n : K4Capacity) :
    2 * (n.ab - n.bd) ≤ k4ABCDLower n := by
  unfold k4ABCDLower
  exact le_max_left _ _

private theorem k4ABCDLower_second_le (n : K4Capacity) :
    2 * (n.ab - n.bc) ≤ k4ABCDLower n := by
  unfold k4ABCDLower
  exact le_trans (le_max_left _ _) (le_max_right _ _)

private theorem k4ABCDLower_key_le (n : K4Capacity) :
    2 * n.ab + n.cd - n.bd - n.bc ≤ k4ABCDLower n := by
  unfold k4ABCDLower
  exact le_trans (le_max_right _ _) (le_max_right _ _)

private theorem k4ABCDUpper_le_ab (n : K4Capacity) :
    k4ABCDUpper n ≤ 2 * n.ab := by
  unfold k4ABCDUpper
  exact min_le_left _ _

private theorem k4ABCDUpper_le_ac (n : K4Capacity) :
    k4ABCDUpper n ≤ 2 * n.ac := by
  unfold k4ABCDUpper
  exact le_trans (min_le_right _ _) (min_le_left _ _)

private theorem k4ABCDUpper_le_ad (n : K4Capacity) :
    k4ABCDUpper n ≤ 2 * n.ad := by
  unfold k4ABCDUpper
  exact le_trans (le_trans (min_le_right _ _) (min_le_right _ _)) (min_le_left _ _)

private theorem k4ABCDUpper_le_key (n : K4Capacity) :
    k4ABCDUpper n ≤ n.ac + n.ad - n.cd := by
  unfold k4ABCDUpper
  exact le_trans (le_trans (min_le_right _ _) (min_le_right _ _)) (min_le_right _ _)

private theorem k4ABCDLower_cases (n : K4Capacity) :
    k4ABCDLower n = 2 * (n.ab - n.bd) ∨
    k4ABCDLower n = 2 * (n.ab - n.bc) ∨
    k4ABCDLower n = 2 * n.ab + n.cd - n.bd - n.bc := by
  unfold k4ABCDLower
  rcases max_choice (2 * (n.ab - n.bd))
      (max (2 * (n.ab - n.bc))
        (2 * n.ab + n.cd - n.bd - n.bc)) with h | h
  · exact Or.inl h
  · rcases max_choice (2 * (n.ab - n.bc))
        (2 * n.ab + n.cd - n.bd - n.bc) with h' | h'
    · exact Or.inr (Or.inl (h.trans h'))
    · exact Or.inr (Or.inr (h.trans h'))

private theorem k4ABCDUpper_cases (n : K4Capacity) :
    k4ABCDUpper n = 2 * n.ab ∨
    k4ABCDUpper n = 2 * n.ac ∨
    k4ABCDUpper n = 2 * n.ad ∨
    k4ABCDUpper n = n.ac + n.ad - n.cd := by
  unfold k4ABCDUpper
  rcases min_choice (2 * n.ab)
      (min (2 * n.ac) (min (2 * n.ad) (n.ac + n.ad - n.cd))) with h | h
  · exact Or.inl h
  · rcases min_choice (2 * n.ac)
        (min (2 * n.ad) (n.ac + n.ad - n.cd)) with h' | h'
    · exact Or.inr (Or.inl (h.trans h'))
    · rcases min_choice (2 * n.ad) (n.ac + n.ad - n.cd) with h'' | h''
      · exact Or.inr (Or.inr (Or.inl ((h.trans h').trans h'')))
      · exact Or.inr (Or.inr (Or.inr ((h.trans h').trans h'')))

/-- Explicit integral witness on the AB/CD matching face once the rounded lower
endpoint remains inside the doubled feasible interval. -/
private theorem k4ABCD_good_witness (n : K4Capacity)
    (h1 : n.ab + n.cd ≤ n.ac + n.bd)
    (h2 : n.ab + n.cd ≤ n.ad + n.bc)
    (h3 : n.ab + n.cd ≤ n.ab + n.ac + n.ad)
    (h4 : n.ab + n.cd ≤ n.ab + n.bc + n.bd)
    (h5 : n.ab + n.cd ≤ n.ac + n.bc + n.cd)
    (h6 : n.ab + n.cd ≤ n.ad + n.bd + n.cd)
    (hgood : 2 * k4ABCDA n ≤ k4ABCDUpper n) :
    ∃ a b c d : ℕ,
      k4Feasible n a b c d ∧
        k4ExtractionValue a b c d = n.ab + n.cd := by
  let a := k4ABCDA n
  let c₁ := n.cd + a - n.ad
  let c₂ := n.ab + n.cd - n.bd - a
  let c := max c₁ c₂
  change 2 * a ≤ k4ABCDUpper n at hgood
  have hceilLower : k4ABCDLower n ≤ 2 * a := by
    change k4ABCDLower n ≤ 2 * ((k4ABCDLower n + 1) / 2)
    exact (k4CeilHalf_bounds (k4ABCDLower n)).1
  have hL1 := k4ABCDLower_first_le n
  have hL2 := k4ABCDLower_second_le n
  have hL3 := k4ABCDLower_key_le n
  have hUab := k4ABCDUpper_le_ab n
  have hUac := k4ABCDUpper_le_ac n
  have hUad := k4ABCDUpper_le_ad n
  have hUkey := k4ABCDUpper_le_key n
  have ha_ab : a ≤ n.ab := by omega
  have ha_ac : a ≤ n.ac := by omega
  have ha_ad : a ≤ n.ad := by omega
  have hab_bd_le_a : n.ab - n.bd ≤ a := by omega
  have hab_bc_le_a : n.ab - n.bc ≤ a := by omega
  have hc1_cd : c₁ ≤ n.cd := by
    dsimp [c₁]
    rw [Nat.sub_le_iff_le_add]
    omega
  have hc2_cd : c₂ ≤ n.cd := by
    dsimp [c₂]
    rw [Nat.sub_le_iff_le_add]
    have hab_le : n.ab ≤ a + n.bd :=
      Nat.sub_le_iff_le_add.mp hab_bd_le_a
    omega
  have hac1 : a + c₁ ≤ n.ac := by
    dsimp [c₁]
    omega
  have hTop_ac : n.ab + n.cd - n.bd ≤ n.ac := by
    rw [Nat.sub_le_iff_le_add]
    omega
  have hac2 : a + c₂ ≤ n.ac := by
    dsimp [c₂]
    by_cases haTop : a ≤ n.ab + n.cd - n.bd
    · calc
        a + (n.ab + n.cd - n.bd - a) = n.ab + n.cd - n.bd :=
          Nat.add_sub_of_le haTop
        _ ≤ n.ac := hTop_ac
    · have hTopA : n.ab + n.cd - n.bd ≤ a := by omega
      have hz : n.ab + n.cd - n.bd - a = 0 := Nat.sub_eq_zero_of_le hTopA
      rw [hz, add_zero]
      exact ha_ac
  have hab_sub_a_le_bc : n.ab - a ≤ n.bc := by
    rw [Nat.sub_le_iff_le_add]
    have hab_le : n.ab ≤ a + n.bc :=
      Nat.sub_le_iff_le_add.mp hab_bc_le_a
    omega
  have hbc1 : (n.ab - a) + c₁ ≤ n.bc := by
    dsimp [c₁]
    by_cases hzero : n.cd + a ≤ n.ad
    · rw [Nat.sub_eq_zero_of_le hzero, add_zero]
      exact hab_sub_a_le_bc
    · have had_le : n.ad ≤ n.cd + a := by omega
      have hab_eq : n.ab - a + a = n.ab := Nat.sub_add_cancel ha_ab
      have hca_eq : n.cd + a - n.ad + n.ad = n.cd + a :=
        Nat.sub_add_cancel had_le
      omega
  have hbc2 : (n.ab - a) + c₂ ≤ n.bc := by
    dsimp [c₂]
    omega
  have hc_cd : c ≤ n.cd := by
    dsimp [c]
    exact max_le hc1_cd hc2_cd
  have hac : a + c ≤ n.ac := by
    rcases max_choice c₁ c₂ with hc | hc
    · change a + max c₁ c₂ ≤ n.ac
      rw [hc]
      exact hac1
    · change a + max c₁ c₂ ≤ n.ac
      rw [hc]
      exact hac2
  have hbc : (n.ab - a) + c ≤ n.bc := by
    rcases max_choice c₁ c₂ with hc | hc
    · change (n.ab - a) + max c₁ c₂ ≤ n.bc
      rw [hc]
      exact hbc1
    · change (n.ab - a) + max c₁ c₂ ≤ n.bc
      rw [hc]
      exact hbc2
  refine ⟨a, n.ab - a, c, n.cd - c, ?_, ?_⟩
  · unfold k4Feasible
    dsimp [c₁, c₂] at *
    omega
  · unfold k4ExtractionValue
    omega

/-- If the rounded lower endpoint lies outside the doubled feasible interval,
the capacities themselves carry the unique all-edges-odd exceptional witness. -/
private theorem k4ABCD_bad_exceptional (n : K4Capacity)
    (h1 : n.ab + n.cd ≤ n.ac + n.bd)
    (h2 : n.ab + n.cd ≤ n.ad + n.bc)
    (h3 : n.ab + n.cd ≤ n.ab + n.ac + n.ad)
    (h4 : n.ab + n.cd ≤ n.ab + n.bc + n.bd)
    (h5 : n.ab + n.cd ≤ n.ac + n.bc + n.cd)
    (h6 : n.ab + n.cd ≤ n.ad + n.bd + n.cd)
    (hbad : ¬ 2 * k4ABCDA n ≤ k4ABCDUpper n) :
    k4Exceptional n := by
  have hLU := k4ABCDLower_le_upper n h1 h2 h3 h4 h5 h6
  have hceil := k4CeilHalf_bounds (k4ABCDLower n)
  have hEqLU : k4ABCDLower n = k4ABCDUpper n := by
    unfold k4ABCDA at hbad
    omega
  have hRound : 2 * k4ABCDA n = k4ABCDLower n + 1 := by
    unfold k4ABCDA at hbad ⊢
    omega
  have hLkey : k4ABCDLower n =
      2 * n.ab + n.cd - n.bd - n.bc := by
    rcases k4ABCDLower_cases n with h | h | h
    · exfalso; omega
    · exfalso; omega
    · exact h
  have hUkey : k4ABCDUpper n = n.ac + n.ad - n.cd := by
    rcases k4ABCDUpper_cases n with h | h | h | h
    · exfalso; omega
    · exfalso; omega
    · exfalso; omega
    · exact h
  have hmatch1 : n.ab + n.cd = n.ac + n.bd := by omega
  have hmatch2 : n.ab + n.cd = n.ad + n.bc := by omega
  have hUab := k4ABCDUpper_le_ab n
  have hUac := k4ABCDUpper_le_ac n
  have hUad := k4ABCDUpper_le_ad n
  have ha_pos : 0 < k4ABCDA n := by omega
  have ha_ab : k4ABCDA n ≤ n.ab := by omega
  have ha_ac : k4ABCDA n ≤ n.ac := by omega
  have ha_ad : k4ABCDA n ≤ n.ad := by omega
  unfold k4Exceptional
  refine ⟨k4ABCDA n - 1, n.ab - k4ABCDA n,
    n.ac - k4ABCDA n, n.ad - k4ABCDA n, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;> omega

/-- First matching face: nonexceptional active minimum has an integer witness. -/
theorem k4Realizable_ab_cd_of_min_of_not_exceptional
    (n : K4Capacity)
    (h1 : n.ab + n.cd ≤ n.ac + n.bd)
    (h2 : n.ab + n.cd ≤ n.ad + n.bc)
    (h3 : n.ab + n.cd ≤ n.ab + n.ac + n.ad)
    (h4 : n.ab + n.cd ≤ n.ab + n.bc + n.bd)
    (h5 : n.ab + n.cd ≤ n.ac + n.bc + n.cd)
    (h6 : n.ab + n.cd ≤ n.ad + n.bd + n.cd)
    (hne : ¬ k4Exceptional n) :
    ∃ a b c d : ℕ, k4Feasible n a b c d ∧
      k4ExtractionValue a b c d = n.ab + n.cd := by
  by_cases hgood : 2 * k4ABCDA n ≤ k4ABCDUpper n
  · exact k4ABCD_good_witness n h1 h2 h3 h4 h5 h6 hgood
  · exact (hne (k4ABCD_bad_exceptional n h1 h2 h3 h4 h5 h6 hgood)).elim

private def k4SwapBC (n : K4Capacity) : K4Capacity where
  ab := n.ac
  ac := n.ab
  ad := n.ad
  bc := n.bc
  bd := n.cd
  cd := n.bd

private theorem k4Exceptional_swapBC (n : K4Capacity) :
    k4Exceptional (k4SwapBC n) ↔ k4Exceptional n := by
  unfold k4Exceptional
  constructor
  · rintro ⟨a, b, c, d, hab, hac, had, hbc, hbd, hcd⟩
    dsimp [k4SwapBC] at hab hac had hbc hbd hcd
    refine ⟨a, c, b, d, hac, hab, had, ?_, hcd, hbd⟩
    omega
  · rintro ⟨a, b, c, d, hab, hac, had, hbc, hbd, hcd⟩
    dsimp [k4SwapBC]
    refine ⟨a, c, b, d, hac, hab, had, ?_, hcd, hbd⟩
    omega

/-- Second matching face, by B↔C relabeling. -/
theorem k4Realizable_ac_bd_of_min_of_not_exceptional
    (n : K4Capacity)
    (h0 : n.ac + n.bd ≤ n.ab + n.cd)
    (h2 : n.ac + n.bd ≤ n.ad + n.bc)
    (h3 : n.ac + n.bd ≤ n.ab + n.ac + n.ad)
    (h4 : n.ac + n.bd ≤ n.ab + n.bc + n.bd)
    (h5 : n.ac + n.bd ≤ n.ac + n.bc + n.cd)
    (h6 : n.ac + n.bd ≤ n.ad + n.bd + n.cd)
    (hne : ¬ k4Exceptional n) :
    ∃ a b c d : ℕ, k4Feasible n a b c d ∧
      k4ExtractionValue a b c d = n.ac + n.bd := by
  let n' := k4SwapBC n
  have h1' : n'.ab + n'.cd ≤ n'.ac + n'.bd := by
    dsimp [n', k4SwapBC]; exact h0
  have h2' : n'.ab + n'.cd ≤ n'.ad + n'.bc := by
    dsimp [n', k4SwapBC]; exact h2
  have h3' : n'.ab + n'.cd ≤ n'.ab + n'.ac + n'.ad := by
    dsimp [n', k4SwapBC]; omega
  have h4' : n'.ab + n'.cd ≤ n'.ab + n'.bc + n'.bd := by
    dsimp [n', k4SwapBC]; exact h5
  have h5' : n'.ab + n'.cd ≤ n'.ac + n'.bc + n'.cd := by
    dsimp [n', k4SwapBC]; exact h4
  have h6' : n'.ab + n'.cd ≤ n'.ad + n'.bd + n'.cd := by
    dsimp [n', k4SwapBC]; omega
  have hne' : ¬ k4Exceptional n' := by
    intro hex
    exact hne ((k4Exceptional_swapBC n).mp hex)
  rcases k4Realizable_ab_cd_of_min_of_not_exceptional n'
      h1' h2' h3' h4' h5' h6' hne' with ⟨a, b, c, d, hfeas, hvalue⟩
  refine ⟨a, c, b, d, ?_, ?_⟩
  · unfold k4Feasible at hfeas ⊢
    dsimp [n', k4SwapBC] at hfeas
    omega
  · unfold k4ExtractionValue at hvalue ⊢
    dsimp [n', k4SwapBC] at hvalue
    omega

private def k4SwapBD (n : K4Capacity) : K4Capacity where
  ab := n.ad
  ac := n.ac
  ad := n.ab
  bc := n.cd
  bd := n.bd
  cd := n.bc

private theorem k4Exceptional_swapBD (n : K4Capacity) :
    k4Exceptional (k4SwapBD n) ↔ k4Exceptional n := by
  unfold k4Exceptional
  constructor
  · rintro ⟨a, b, c, d, hab, hac, had, hbc, hbd, hcd⟩
    dsimp [k4SwapBD] at hab hac had hbc hbd hcd
    refine ⟨a, d, c, b, had, hac, hab, ?_, ?_, ?_⟩ <;> omega
  · rintro ⟨a, b, c, d, hab, hac, had, hbc, hbd, hcd⟩
    dsimp [k4SwapBD]
    refine ⟨a, d, c, b, had, hac, hab, ?_, ?_, ?_⟩ <;> omega

/-- Third matching face, by B↔D relabeling. -/
theorem k4Realizable_ad_bc_of_min_of_not_exceptional
    (n : K4Capacity)
    (h0 : n.ad + n.bc ≤ n.ab + n.cd)
    (h1 : n.ad + n.bc ≤ n.ac + n.bd)
    (h3 : n.ad + n.bc ≤ n.ab + n.ac + n.ad)
    (h4 : n.ad + n.bc ≤ n.ab + n.bc + n.bd)
    (h5 : n.ad + n.bc ≤ n.ac + n.bc + n.cd)
    (h6 : n.ad + n.bc ≤ n.ad + n.bd + n.cd)
    (hne : ¬ k4Exceptional n) :
    ∃ a b c d : ℕ, k4Feasible n a b c d ∧
      k4ExtractionValue a b c d = n.ad + n.bc := by
  let n' := k4SwapBD n
  have h1' : n'.ab + n'.cd ≤ n'.ac + n'.bd := by
    dsimp [n', k4SwapBD]; exact h1
  have h2' : n'.ab + n'.cd ≤ n'.ad + n'.bc := by
    dsimp [n', k4SwapBD]; exact h0
  have h3' : n'.ab + n'.cd ≤ n'.ab + n'.ac + n'.ad := by
    dsimp [n', k4SwapBD]; omega
  have h4' : n'.ab + n'.cd ≤ n'.ab + n'.bc + n'.bd := by
    dsimp [n', k4SwapBD]; omega
  have h5' : n'.ab + n'.cd ≤ n'.ac + n'.bc + n'.cd := by
    dsimp [n', k4SwapBD]; omega
  have h6' : n'.ab + n'.cd ≤ n'.ad + n'.bd + n'.cd := by
    dsimp [n', k4SwapBD]; omega
  have hne' : ¬ k4Exceptional n' := by
    intro hex
    exact hne ((k4Exceptional_swapBD n).mp hex)
  rcases k4Realizable_ab_cd_of_min_of_not_exceptional n'
      h1' h2' h3' h4' h5' h6' hne' with ⟨a, b, c, d, hfeas, hvalue⟩
  refine ⟨a, d, c, b, ?_, ?_⟩
  · unfold k4Feasible at hfeas ⊢
    dsimp [n', k4SwapBD] at hfeas
    omega
  · unfold k4ExtractionValue at hvalue ⊢
    dsimp [n', k4SwapBD] at hvalue
    omega

end EnterpriseMath.BranchRecoalescence
