import EnterpriseMath.Relation.BRCK4OptimalExtractionMatching

namespace EnterpriseMath.BranchRecoalescence

/-- Outside the half-integral obstruction, the top seven-bound value itself is
attained. -/
theorem k4SevenBound_realizable_of_not_exceptional
    (n : K4Capacity) (hne : ¬ k4Exceptional n) :
    ∃ a b c d : ℕ,
      k4Feasible n a b c d ∧
        k4ExtractionValue a b c d = k4SevenBound n := by
  rcases k4SevenBound_choice n with h | h | h | h | h | h | h
  · have h1 : n.ab + n.cd ≤ n.ac + n.bd := by
      rw [← h]; exact k4SevenBound_le_ac_bd n
    have h2 : n.ab + n.cd ≤ n.ad + n.bc := by
      rw [← h]; exact k4SevenBound_le_ad_bc n
    have h3 : n.ab + n.cd ≤ n.ab + n.ac + n.ad := by
      rw [← h]; exact k4SevenBound_le_starA n
    have h4 : n.ab + n.cd ≤ n.ab + n.bc + n.bd := by
      rw [← h]; exact k4SevenBound_le_starB n
    have h5 : n.ab + n.cd ≤ n.ac + n.bc + n.cd := by
      rw [← h]; exact k4SevenBound_le_starC n
    have h6 : n.ab + n.cd ≤ n.ad + n.bd + n.cd := by
      rw [← h]; exact k4SevenBound_le_starD n
    simpa [h] using
      k4Realizable_ab_cd_of_min_of_not_exceptional n h1 h2 h3 h4 h5 h6 hne
  · have h0 : n.ac + n.bd ≤ n.ab + n.cd := by
      rw [← h]; exact k4SevenBound_le_ab_cd n
    have h2 : n.ac + n.bd ≤ n.ad + n.bc := by
      rw [← h]; exact k4SevenBound_le_ad_bc n
    have h3 : n.ac + n.bd ≤ n.ab + n.ac + n.ad := by
      rw [← h]; exact k4SevenBound_le_starA n
    have h4 : n.ac + n.bd ≤ n.ab + n.bc + n.bd := by
      rw [← h]; exact k4SevenBound_le_starB n
    have h5 : n.ac + n.bd ≤ n.ac + n.bc + n.cd := by
      rw [← h]; exact k4SevenBound_le_starC n
    have h6 : n.ac + n.bd ≤ n.ad + n.bd + n.cd := by
      rw [← h]; exact k4SevenBound_le_starD n
    simpa [h] using
      k4Realizable_ac_bd_of_min_of_not_exceptional n h0 h2 h3 h4 h5 h6 hne
  · have h0 : n.ad + n.bc ≤ n.ab + n.cd := by
      rw [← h]; exact k4SevenBound_le_ab_cd n
    have h1 : n.ad + n.bc ≤ n.ac + n.bd := by
      rw [← h]; exact k4SevenBound_le_ac_bd n
    have h3 : n.ad + n.bc ≤ n.ab + n.ac + n.ad := by
      rw [← h]; exact k4SevenBound_le_starA n
    have h4 : n.ad + n.bc ≤ n.ab + n.bc + n.bd := by
      rw [← h]; exact k4SevenBound_le_starB n
    have h5 : n.ad + n.bc ≤ n.ac + n.bc + n.cd := by
      rw [← h]; exact k4SevenBound_le_starC n
    have h6 : n.ad + n.bc ≤ n.ad + n.bd + n.cd := by
      rw [← h]; exact k4SevenBound_le_starD n
    simpa [h] using
      k4Realizable_ad_bc_of_min_of_not_exceptional n h0 h1 h3 h4 h5 h6 hne
  · have h0 : n.ab + n.ac + n.ad ≤ n.ab + n.cd := by
      rw [← h]; exact k4SevenBound_le_ab_cd n
    have h1 : n.ab + n.ac + n.ad ≤ n.ac + n.bd := by
      rw [← h]; exact k4SevenBound_le_ac_bd n
    have h2 : n.ab + n.ac + n.ad ≤ n.ad + n.bc := by
      rw [← h]; exact k4SevenBound_le_ad_bc n
    simpa [h] using k4Realizable_starA_of_min n h0 h1 h2
  · have h0 : n.ab + n.bc + n.bd ≤ n.ab + n.cd := by
      rw [← h]; exact k4SevenBound_le_ab_cd n
    have h1 : n.ab + n.bc + n.bd ≤ n.ac + n.bd := by
      rw [← h]; exact k4SevenBound_le_ac_bd n
    have h2 : n.ab + n.bc + n.bd ≤ n.ad + n.bc := by
      rw [← h]; exact k4SevenBound_le_ad_bc n
    simpa [h] using k4Realizable_starB_of_min n h0 h1 h2
  · have h0 : n.ac + n.bc + n.cd ≤ n.ab + n.cd := by
      rw [← h]; exact k4SevenBound_le_ab_cd n
    have h1 : n.ac + n.bc + n.cd ≤ n.ac + n.bd := by
      rw [← h]; exact k4SevenBound_le_ac_bd n
    have h2 : n.ac + n.bc + n.cd ≤ n.ad + n.bc := by
      rw [← h]; exact k4SevenBound_le_ad_bc n
    simpa [h] using k4Realizable_starC_of_min n h0 h1 h2
  · have h0 : n.ad + n.bd + n.cd ≤ n.ab + n.cd := by
      rw [← h]; exact k4SevenBound_le_ab_cd n
    have h1 : n.ad + n.bd + n.cd ≤ n.ac + n.bd := by
      rw [← h]; exact k4SevenBound_le_ac_bd n
    have h2 : n.ad + n.bd + n.cd ≤ n.ad + n.bc := by
      rw [← h]; exact k4SevenBound_le_ad_bc n
    simpa [h] using k4Realizable_starD_of_min n h0 h1 h2

/-- If a requested integer lies below all seven bounds and the exceptional
half-integral pattern is absent, that exact integer total is realizable. -/
theorem k4Realizable_of_bounds_of_not_exceptional
    (n : K4Capacity) (m : ℕ)
    (h0 : m ≤ n.ab + n.cd)
    (h1 : m ≤ n.ac + n.bd)
    (h2 : m ≤ n.ad + n.bc)
    (h3 : m ≤ n.ab + n.ac + n.ad)
    (h4 : m ≤ n.ab + n.bc + n.bd)
    (h5 : m ≤ n.ac + n.bc + n.cd)
    (h6 : m ≤ n.ad + n.bd + n.cd)
    (hne : ¬ k4Exceptional n) :
    ∃ a b c d : ℕ,
      k4Feasible n a b c d ∧ k4ExtractionValue a b c d = m := by
  have hm : m ≤ k4SevenBound n :=
    le_k4SevenBound h0 h1 h2 h3 h4 h5 h6
  rcases k4SevenBound_realizable_of_not_exceptional n hne with
    ⟨a, b, c, d, hfeas, hvalue⟩
  have hm' : m ≤ k4ExtractionValue a b c d := by
    rw [hvalue]
    exact hm
  exact k4Feasible_shrink n a b c d m hfeas hm'

/-- For an explicit exceptional witness, the seven-bound minimum is the common
opposite-edge value `a+b+c+d+2`. -/
theorem k4SevenBound_eq_of_exceptional_witness
    (n : K4Capacity) {a b c d : ℕ}
    (hab : n.ab = a + b + 1)
    (hac : n.ac = a + c + 1)
    (had : n.ad = a + d + 1)
    (hbc : n.bc = b + c + 1)
    (hbd : n.bd = b + d + 1)
    (hcd : n.cd = c + d + 1) :
    k4SevenBound n = a + b + c + d + 2 := by
  apply le_antisymm
  · have hle := k4SevenBound_le_ab_cd n
    omega
  · apply le_k4SevenBound <;> omega

/-- Exceptional capacities have exactly a one-unit integer deficit below the
seven-bound minimum. -/
theorem k4Exceptional_optimal (n : K4Capacity) (h : k4Exceptional n) :
    K4OptimalValue n (k4SevenBound n - 1) := by
  rcases h with ⟨p, q, r, s, hab, hac, had, hbc, hbd, hcd⟩
  have hseven : k4SevenBound n = p + q + r + s + 2 :=
    k4SevenBound_eq_of_exceptional_witness n hab hac had hbc hbd hcd
  constructor
  · refine ⟨p + 1, q, r, s, ?_, ?_⟩
    · unfold k4Feasible
      omega
    · unfold k4ExtractionValue
      rw [hseven]
      omega
  · intro a b c d hfeas
    unfold k4Feasible at hfeas
    unfold k4ExtractionValue
    rw [hseven]
    omega

/-- Outside the exceptional pattern, the seven-bound minimum is exact. -/
theorem k4Nonexceptional_optimal (n : K4Capacity)
    (hne : ¬ k4Exceptional n) :
    K4OptimalValue n (k4SevenBound n) := by
  constructor
  · exact k4Realizable_of_bounds_of_not_exceptional n (k4SevenBound n)
      (k4SevenBound_le_ab_cd n)
      (k4SevenBound_le_ac_bd n)
      (k4SevenBound_le_ad_bc n)
      (k4SevenBound_le_starA n)
      (k4SevenBound_le_starB n)
      (k4SevenBound_le_starC n)
      (k4SevenBound_le_starD n)
      hne
  · intro a b c d hfeas
    exact k4Feasible_value_le_sevenBound n a b c d hfeas

/-- Closed-form integer optimum used by the executable K4 atlas compiler. -/
noncomputable def k4ClosedValue (n : K4Capacity) : ℕ := by
  classical
  exact if k4Exceptional n then k4SevenBound n - 1 else k4SevenBound n

/-- Formal closure of the executable formula:
`optimum = min(seven_bounds) - exceptional_bit`. -/
theorem k4ClosedValue_optimal (n : K4Capacity) :
    K4OptimalValue n (k4ClosedValue n) := by
  classical
  by_cases h : k4Exceptional n
  · simpa [k4ClosedValue, h] using k4Exceptional_optimal n h
  · simpa [k4ClosedValue, h] using k4Nonexceptional_optimal n h

end EnterpriseMath.BranchRecoalescence
