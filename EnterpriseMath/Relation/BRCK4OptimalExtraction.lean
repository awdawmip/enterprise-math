import EnterpriseMath.Relation.BRCSixAxisS4
import Mathlib.Tactic

namespace EnterpriseMath.BranchRecoalescence

/-- Six K4 edge capacities in the executable atlas source order
`AB, AC, AD, BC, BD, CD`.  This is an optimization carrier, not a claim that
these six naturals are the native Cell address object. -/
structure K4Capacity where
  ab : ℕ
  ac : ℕ
  ad : ℕ
  bc : ℕ
  bd : ℕ
  cd : ℕ

/-- Four nonnegative extraction multiplicities are feasible when every K4 edge
has enough capacity for the two incident vertex extractions. -/
def k4Feasible (n : K4Capacity) (a b c d : ℕ) : Prop :=
  a + b ≤ n.ab ∧
  a + c ≤ n.ac ∧
  a + d ≤ n.ad ∧
  b + c ≤ n.bc ∧
  b + d ≤ n.bd ∧
  c + d ≤ n.cd

/-- Extraction objective. -/
def k4ExtractionValue (a b c d : ℕ) : ℕ := a + b + c + d

/-- The seven elementary upper bounds from the executable K4 atlas compiler:
three opposite-edge pairings followed by four vertex-star sums. -/
def k4SevenBound (n : K4Capacity) : ℕ :=
  min (n.ab + n.cd)
    (min (n.ac + n.bd)
      (min (n.ad + n.bc)
        (min (n.ab + n.ac + n.ad)
          (min (n.ab + n.bc + n.bd)
            (min (n.ac + n.bc + n.cd)
              (n.ad + n.bd + n.cd))))))

/-- The unique half-integral obstruction pattern used by the executable source:
every edge capacity is one more than the sum of two nonnegative vertex bases. -/
def k4Exceptional (n : K4Capacity) : Prop :=
  ∃ a b c d : ℕ,
    n.ab = a + b + 1 ∧
    n.ac = a + c + 1 ∧
    n.ad = a + d + 1 ∧
    n.bc = b + c + 1 ∧
    n.bd = b + d + 1 ∧
    n.cd = c + d + 1

/-- `m` is the exact integer optimum if it is attained and dominates every
feasible extraction value. -/
def K4OptimalValue (n : K4Capacity) (m : ℕ) : Prop :=
  (∃ a b c d : ℕ,
      k4Feasible n a b c d ∧ k4ExtractionValue a b c d = m) ∧
    ∀ a b c d : ℕ,
      k4Feasible n a b c d → k4ExtractionValue a b c d ≤ m

/-- Any number below all seven declared bounds is below their nested minimum. -/
theorem le_k4SevenBound {n : K4Capacity} {m : ℕ}
    (h0 : m ≤ n.ab + n.cd)
    (h1 : m ≤ n.ac + n.bd)
    (h2 : m ≤ n.ad + n.bc)
    (h3 : m ≤ n.ab + n.ac + n.ad)
    (h4 : m ≤ n.ab + n.bc + n.bd)
    (h5 : m ≤ n.ac + n.bc + n.cd)
    (h6 : m ≤ n.ad + n.bd + n.cd) :
    m ≤ k4SevenBound n := by
  unfold k4SevenBound
  exact le_min h0 (le_min h1 (le_min h2
    (le_min h3 (le_min h4 (le_min h5 h6)))))

/-- The seven-bound minimum is below the first opposite-edge pairing. -/
theorem k4SevenBound_le_ab_cd (n : K4Capacity) :
    k4SevenBound n ≤ n.ab + n.cd := by
  simp [k4SevenBound]

/-- The seven-bound minimum is below the second opposite-edge pairing. -/
theorem k4SevenBound_le_ac_bd (n : K4Capacity) :
    k4SevenBound n ≤ n.ac + n.bd := by
  simp [k4SevenBound]

/-- The seven-bound minimum is below the third opposite-edge pairing. -/
theorem k4SevenBound_le_ad_bc (n : K4Capacity) :
    k4SevenBound n ≤ n.ad + n.bc := by
  simp [k4SevenBound]

/-- The seven-bound minimum is below the A-star sum. -/
theorem k4SevenBound_le_starA (n : K4Capacity) :
    k4SevenBound n ≤ n.ab + n.ac + n.ad := by
  simp [k4SevenBound]

/-- The seven-bound minimum is below the B-star sum. -/
theorem k4SevenBound_le_starB (n : K4Capacity) :
    k4SevenBound n ≤ n.ab + n.bc + n.bd := by
  simp [k4SevenBound]

/-- The seven-bound minimum is below the C-star sum. -/
theorem k4SevenBound_le_starC (n : K4Capacity) :
    k4SevenBound n ≤ n.ac + n.bc + n.cd := by
  simp [k4SevenBound]

/-- The seven-bound minimum is below the D-star sum. -/
theorem k4SevenBound_le_starD (n : K4Capacity) :
    k4SevenBound n ≤ n.ad + n.bd + n.cd := by
  simp [k4SevenBound]

/-- Every feasible extraction is bounded by all three opposite-edge pairings and
all four star sums, hence by `k4SevenBound`. -/
theorem k4Feasible_value_le_sevenBound (n : K4Capacity)
    (a b c d : ℕ) (h : k4Feasible n a b c d) :
    k4ExtractionValue a b c d ≤ k4SevenBound n := by
  rcases h with ⟨hab, hac, had, hbc, hbd, hcd⟩
  unfold k4ExtractionValue
  apply le_k4SevenBound <;> omega

/-- Any feasible four-vertex extraction can be monotonically reduced to any
smaller requested total.  Feasibility is preserved because every vertex
multiplicity only decreases. -/
theorem k4Feasible_shrink (n : K4Capacity)
    (a b c d m : ℕ) (hfeas : k4Feasible n a b c d)
    (hm : m ≤ k4ExtractionValue a b c d) :
    ∃ a' b' c' d' : ℕ,
      k4Feasible n a' b' c' d' ∧ k4ExtractionValue a' b' c' d' = m := by
  have hsplit : ∃ a' b' c' d' : ℕ,
      a' ≤ a ∧ b' ≤ b ∧ c' ≤ c ∧ d' ≤ d ∧ a' + b' + c' + d' = m := by
    unfold k4ExtractionValue at hm
    omega
  rcases hsplit with ⟨a', b', c', d', ha, hb, hc, hd, hsum⟩
  refine ⟨a', b', c', d', ?_, ?_⟩
  · unfold k4Feasible at hfeas ⊢
    omega
  · exact hsum

/-- The nested seven-bound minimum is attained by at least one of its seven
explicit linear bounds. -/
theorem k4SevenBound_choice (n : K4Capacity) :
    k4SevenBound n = n.ab + n.cd ∨
    k4SevenBound n = n.ac + n.bd ∨
    k4SevenBound n = n.ad + n.bc ∨
    k4SevenBound n = n.ab + n.ac + n.ad ∨
    k4SevenBound n = n.ab + n.bc + n.bd ∨
    k4SevenBound n = n.ac + n.bc + n.cd ∨
    k4SevenBound n = n.ad + n.bd + n.cd := by
  unfold k4SevenBound
  rcases min_choice (n.ab + n.cd)
      (min (n.ac + n.bd)
        (min (n.ad + n.bc)
          (min (n.ab + n.ac + n.ad)
            (min (n.ab + n.bc + n.bd)
              (min (n.ac + n.bc + n.cd) (n.ad + n.bd + n.cd)))))) with h | h
  · exact Or.inl h
  · rw [h]
    rcases min_choice (n.ac + n.bd)
        (min (n.ad + n.bc)
          (min (n.ab + n.ac + n.ad)
            (min (n.ab + n.bc + n.bd)
              (min (n.ac + n.bc + n.cd) (n.ad + n.bd + n.cd))))) with h | h
    · exact Or.inr (Or.inl h)
    · rw [h]
      rcases min_choice (n.ad + n.bc)
          (min (n.ab + n.ac + n.ad)
            (min (n.ab + n.bc + n.bd)
              (min (n.ac + n.bc + n.cd) (n.ad + n.bd + n.cd)))) with h | h
      · exact Or.inr (Or.inr (Or.inl h))
      · rw [h]
        rcases min_choice (n.ab + n.ac + n.ad)
            (min (n.ab + n.bc + n.bd)
              (min (n.ac + n.bc + n.cd) (n.ad + n.bd + n.cd))) with h | h
        · exact Or.inr (Or.inr (Or.inr (Or.inl h)))
        · rw [h]
          rcases min_choice (n.ab + n.bc + n.bd)
              (min (n.ac + n.bc + n.cd) (n.ad + n.bd + n.cd)) with h | h
          · exact Or.inr (Or.inr (Or.inr (Or.inr (Or.inl h))))
          · rw [h]
            rcases min_choice (n.ac + n.bc + n.cd) (n.ad + n.bd + n.cd) with h | h
            · exact Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl h)))))
            · exact Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr h)))))

/-- If the first opposite-edge pairing is the active minimum and the exceptional
half-integral pattern is absent, the top bound has an integer witness. -/
theorem k4Realizable_ab_cd_of_min_of_not_exceptional
    (n : K4Capacity)
    (h1 : n.ab + n.cd ≤ n.ac + n.bd)
    (h2 : n.ab + n.cd ≤ n.ad + n.bc)
    (h3 : n.ab + n.cd ≤ n.ab + n.ac + n.ad)
    (h4 : n.ab + n.cd ≤ n.ab + n.bc + n.bd)
    (h5 : n.ab + n.cd ≤ n.ac + n.bc + n.cd)
    (h6 : n.ab + n.cd ≤ n.ad + n.bd + n.cd)
    (hne : ¬ k4Exceptional n) :
    ∃ a b c d : ℕ,
      k4Feasible n a b c d ∧
        k4ExtractionValue a b c d = n.ab + n.cd := by
  rcases n with ⟨ab, ac, ad, bc, bd, cd⟩
  unfold k4Exceptional at hne
  unfold k4Feasible k4ExtractionValue
  dsimp at hne ⊢
  omega

/-- Second opposite-edge active-minimum case. -/
theorem k4Realizable_ac_bd_of_min_of_not_exceptional
    (n : K4Capacity)
    (h0 : n.ac + n.bd ≤ n.ab + n.cd)
    (h2 : n.ac + n.bd ≤ n.ad + n.bc)
    (h3 : n.ac + n.bd ≤ n.ab + n.ac + n.ad)
    (h4 : n.ac + n.bd ≤ n.ab + n.bc + n.bd)
    (h5 : n.ac + n.bd ≤ n.ac + n.bc + n.cd)
    (h6 : n.ac + n.bd ≤ n.ad + n.bd + n.cd)
    (hne : ¬ k4Exceptional n) :
    ∃ a b c d : ℕ,
      k4Feasible n a b c d ∧
        k4ExtractionValue a b c d = n.ac + n.bd := by
  rcases n with ⟨ab, ac, ad, bc, bd, cd⟩
  unfold k4Exceptional at hne
  unfold k4Feasible k4ExtractionValue
  dsimp at hne ⊢
  omega

/-- Third opposite-edge active-minimum case. -/
theorem k4Realizable_ad_bc_of_min_of_not_exceptional
    (n : K4Capacity)
    (h0 : n.ad + n.bc ≤ n.ab + n.cd)
    (h1 : n.ad + n.bc ≤ n.ac + n.bd)
    (h3 : n.ad + n.bc ≤ n.ab + n.ac + n.ad)
    (h4 : n.ad + n.bc ≤ n.ab + n.bc + n.bd)
    (h5 : n.ad + n.bc ≤ n.ac + n.bc + n.cd)
    (h6 : n.ad + n.bc ≤ n.ad + n.bd + n.cd)
    (hne : ¬ k4Exceptional n) :
    ∃ a b c d : ℕ,
      k4Feasible n a b c d ∧
        k4ExtractionValue a b c d = n.ad + n.bc := by
  rcases n with ⟨ab, ac, ad, bc, bd, cd⟩
  unfold k4Exceptional at hne
  unfold k4Feasible k4ExtractionValue
  dsimp at hne ⊢
  omega

/-- If the A-star bound is active, setting the A extraction to zero and taking
the three incident capacities gives an explicit optimum witness. -/
theorem k4Realizable_starA_of_min (n : K4Capacity)
    (h0 : n.ab + n.ac + n.ad ≤ n.ab + n.cd)
    (h1 : n.ab + n.ac + n.ad ≤ n.ac + n.bd)
    (h2 : n.ab + n.ac + n.ad ≤ n.ad + n.bc) :
    ∃ a b c d : ℕ,
      k4Feasible n a b c d ∧
        k4ExtractionValue a b c d = n.ab + n.ac + n.ad := by
  refine ⟨0, n.ab, n.ac, n.ad, ?_, ?_⟩
  · unfold k4Feasible
    omega
  · unfold k4ExtractionValue
    omega

/-- B-star active-minimum witness. -/
theorem k4Realizable_starB_of_min (n : K4Capacity)
    (h0 : n.ab + n.bc + n.bd ≤ n.ab + n.cd)
    (h1 : n.ab + n.bc + n.bd ≤ n.ac + n.bd)
    (h2 : n.ab + n.bc + n.bd ≤ n.ad + n.bc) :
    ∃ a b c d : ℕ,
      k4Feasible n a b c d ∧
        k4ExtractionValue a b c d = n.ab + n.bc + n.bd := by
  refine ⟨n.ab, 0, n.bc, n.bd, ?_, ?_⟩
  · unfold k4Feasible
    omega
  · unfold k4ExtractionValue
    omega

/-- C-star active-minimum witness. -/
theorem k4Realizable_starC_of_min (n : K4Capacity)
    (h0 : n.ac + n.bc + n.cd ≤ n.ab + n.cd)
    (h1 : n.ac + n.bc + n.cd ≤ n.ac + n.bd)
    (h2 : n.ac + n.bc + n.cd ≤ n.ad + n.bc) :
    ∃ a b c d : ℕ,
      k4Feasible n a b c d ∧
        k4ExtractionValue a b c d = n.ac + n.bc + n.cd := by
  refine ⟨n.ac, n.bc, 0, n.cd, ?_, ?_⟩
  · unfold k4Feasible
    omega
  · unfold k4ExtractionValue
    omega

/-- D-star active-minimum witness. -/
theorem k4Realizable_starD_of_min (n : K4Capacity)
    (h0 : n.ad + n.bd + n.cd ≤ n.ab + n.cd)
    (h1 : n.ad + n.bd + n.cd ≤ n.ac + n.bd)
    (h2 : n.ad + n.bd + n.cd ≤ n.ad + n.bc) :
    ∃ a b c d : ℕ,
      k4Feasible n a b c d ∧
        k4ExtractionValue a b c d = n.ad + n.bd + n.cd := by
  refine ⟨n.ad, n.bd, n.cd, 0, ?_, ?_⟩
  · unfold k4Feasible
    omega
  · unfold k4ExtractionValue
    omega

/-- Outside the half-integral obstruction, the top seven-bound value itself is
attained.  The proof separates the three matching minima from the four integral
star minima. -/
theorem k4SevenBound_realizable_of_not_exceptional
    (n : K4Capacity) (hne : ¬ k4Exceptional n) :
    ∃ a b c d : ℕ,
      k4Feasible n a b c d ∧
        k4ExtractionValue a b c d = k4SevenBound n := by
  rcases k4SevenBound_choice n with h | h | h | h | h | h | h
  · have h1 : n.ab + n.cd ≤ n.ac + n.bd := by
      rw [← h]
      exact k4SevenBound_le_ac_bd n
    have h2 : n.ab + n.cd ≤ n.ad + n.bc := by
      rw [← h]
      exact k4SevenBound_le_ad_bc n
    have h3 : n.ab + n.cd ≤ n.ab + n.ac + n.ad := by
      rw [← h]
      exact k4SevenBound_le_starA n
    have h4 : n.ab + n.cd ≤ n.ab + n.bc + n.bd := by
      rw [← h]
      exact k4SevenBound_le_starB n
    have h5 : n.ab + n.cd ≤ n.ac + n.bc + n.cd := by
      rw [← h]
      exact k4SevenBound_le_starC n
    have h6 : n.ab + n.cd ≤ n.ad + n.bd + n.cd := by
      rw [← h]
      exact k4SevenBound_le_starD n
    simpa [h] using k4Realizable_ab_cd_of_min_of_not_exceptional n h1 h2 h3 h4 h5 h6 hne
  · have h0 : n.ac + n.bd ≤ n.ab + n.cd := by
      rw [← h]
      exact k4SevenBound_le_ab_cd n
    have h2 : n.ac + n.bd ≤ n.ad + n.bc := by
      rw [← h]
      exact k4SevenBound_le_ad_bc n
    have h3 : n.ac + n.bd ≤ n.ab + n.ac + n.ad := by
      rw [← h]
      exact k4SevenBound_le_starA n
    have h4 : n.ac + n.bd ≤ n.ab + n.bc + n.bd := by
      rw [← h]
      exact k4SevenBound_le_starB n
    have h5 : n.ac + n.bd ≤ n.ac + n.bc + n.cd := by
      rw [← h]
      exact k4SevenBound_le_starC n
    have h6 : n.ac + n.bd ≤ n.ad + n.bd + n.cd := by
      rw [← h]
      exact k4SevenBound_le_starD n
    simpa [h] using k4Realizable_ac_bd_of_min_of_not_exceptional n h0 h2 h3 h4 h5 h6 hne
  · have h0 : n.ad + n.bc ≤ n.ab + n.cd := by
      rw [← h]
      exact k4SevenBound_le_ab_cd n
    have h1 : n.ad + n.bc ≤ n.ac + n.bd := by
      rw [← h]
      exact k4SevenBound_le_ac_bd n
    have h3 : n.ad + n.bc ≤ n.ab + n.ac + n.ad := by
      rw [← h]
      exact k4SevenBound_le_starA n
    have h4 : n.ad + n.bc ≤ n.ab + n.bc + n.bd := by
      rw [← h]
      exact k4SevenBound_le_starB n
    have h5 : n.ad + n.bc ≤ n.ac + n.bc + n.cd := by
      rw [← h]
      exact k4SevenBound_le_starC n
    have h6 : n.ad + n.bc ≤ n.ad + n.bd + n.cd := by
      rw [← h]
      exact k4SevenBound_le_starD n
    simpa [h] using k4Realizable_ad_bc_of_min_of_not_exceptional n h0 h1 h3 h4 h5 h6 hne
  · have h0 : n.ab + n.ac + n.ad ≤ n.ab + n.cd := by
      rw [← h]
      exact k4SevenBound_le_ab_cd n
    have h1 : n.ab + n.ac + n.ad ≤ n.ac + n.bd := by
      rw [← h]
      exact k4SevenBound_le_ac_bd n
    have h2 : n.ab + n.ac + n.ad ≤ n.ad + n.bc := by
      rw [← h]
      exact k4SevenBound_le_ad_bc n
    simpa [h] using k4Realizable_starA_of_min n h0 h1 h2
  · have h0 : n.ab + n.bc + n.bd ≤ n.ab + n.cd := by
      rw [← h]
      exact k4SevenBound_le_ab_cd n
    have h1 : n.ab + n.bc + n.bd ≤ n.ac + n.bd := by
      rw [← h]
      exact k4SevenBound_le_ac_bd n
    have h2 : n.ab + n.bc + n.bd ≤ n.ad + n.bc := by
      rw [← h]
      exact k4SevenBound_le_ad_bc n
    simpa [h] using k4Realizable_starB_of_min n h0 h1 h2
  · have h0 : n.ac + n.bc + n.cd ≤ n.ab + n.cd := by
      rw [← h]
      exact k4SevenBound_le_ab_cd n
    have h1 : n.ac + n.bc + n.cd ≤ n.ac + n.bd := by
      rw [← h]
      exact k4SevenBound_le_ac_bd n
    have h2 : n.ac + n.bc + n.cd ≤ n.ad + n.bc := by
      rw [← h]
      exact k4SevenBound_le_ad_bc n
    simpa [h] using k4Realizable_starC_of_min n h0 h1 h2
  · have h0 : n.ad + n.bd + n.cd ≤ n.ab + n.cd := by
      rw [← h]
      exact k4SevenBound_le_ab_cd n
    have h1 : n.ad + n.bd + n.cd ≤ n.ac + n.bd := by
      rw [← h]
      exact k4SevenBound_le_ac_bd n
    have h2 : n.ad + n.bd + n.cd ≤ n.ad + n.bc := by
      rw [← h]
      exact k4SevenBound_le_ad_bc n
    simpa [h] using k4Realizable_starD_of_min n h0 h1 h2

/-- Presburger completeness of the non-exceptional K4 extraction polytope.
If a requested integer value lies below every one of the seven elementary
bounds and the half-integral exceptional pattern is absent, then that value is
attained by an integer feasible extraction. -/
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
seven-bound minimum.  The lower witness raises any one base vertex by one; the
upper statement is the half-integral parity obstruction, discharged here as a
Presburger theorem. -/
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

/-- Outside the half-integral exceptional pattern, the seven-bound minimum is
attained exactly. -/
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
