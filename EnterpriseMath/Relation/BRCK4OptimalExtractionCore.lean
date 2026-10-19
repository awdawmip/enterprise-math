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

 theorem k4SevenBound_le_ab_cd (n : K4Capacity) :
    k4SevenBound n ≤ n.ab + n.cd := by simp [k4SevenBound]
 theorem k4SevenBound_le_ac_bd (n : K4Capacity) :
    k4SevenBound n ≤ n.ac + n.bd := by simp [k4SevenBound]
 theorem k4SevenBound_le_ad_bc (n : K4Capacity) :
    k4SevenBound n ≤ n.ad + n.bc := by simp [k4SevenBound]
 theorem k4SevenBound_le_starA (n : K4Capacity) :
    k4SevenBound n ≤ n.ab + n.ac + n.ad := by simp [k4SevenBound]
 theorem k4SevenBound_le_starB (n : K4Capacity) :
    k4SevenBound n ≤ n.ab + n.bc + n.bd := by simp [k4SevenBound]
 theorem k4SevenBound_le_starC (n : K4Capacity) :
    k4SevenBound n ≤ n.ac + n.bc + n.cd := by simp [k4SevenBound]
 theorem k4SevenBound_le_starD (n : K4Capacity) :
    k4SevenBound n ≤ n.ad + n.bd + n.cd := by simp [k4SevenBound]

/-- Every feasible extraction is bounded by all seven declared bounds. -/
theorem k4Feasible_value_le_sevenBound (n : K4Capacity)
    (a b c d : ℕ) (h : k4Feasible n a b c d) :
    k4ExtractionValue a b c d ≤ k4SevenBound n := by
  rcases h with ⟨hab, hac, had, hbc, hbd, hcd⟩
  unfold k4ExtractionValue
  apply le_k4SevenBound <;> omega

private theorem k4PairSplit {x y m : ℕ} (h : m ≤ x + y) :
    ∃ x' y' : ℕ, x' ≤ x ∧ y' ≤ y ∧ x' + y' = m := by
  by_cases hx : m ≤ x
  · exact ⟨m, 0, hx, Nat.zero_le _, by omega⟩
  · refine ⟨x, m - x, le_rfl, ?_, ?_⟩ <;> omega

/-- Any feasible extraction can be shrunk to every lower integer total. -/
theorem k4Feasible_shrink (n : K4Capacity)
    (a b c d m : ℕ) (hfeas : k4Feasible n a b c d)
    (hm : m ≤ k4ExtractionValue a b c d) :
    ∃ a' b' c' d' : ℕ,
      k4Feasible n a' b' c' d' ∧ k4ExtractionValue a' b' c' d' = m := by
  have hm' : m ≤ (a + b) + (c + d) := by
    unfold k4ExtractionValue at hm
    omega
  rcases k4PairSplit (x := a + b) (y := c + d) (m := m) hm' with
    ⟨p, q, hp, hq, hpq⟩
  rcases k4PairSplit (x := a) (y := b) (m := p) hp with
    ⟨a', b', ha, hb, hab⟩
  rcases k4PairSplit (x := c) (y := d) (m := q) hq with
    ⟨c', d', hc, hd, hcd⟩
  refine ⟨a', b', c', d', ?_, ?_⟩
  · unfold k4Feasible at hfeas ⊢
    omega
  · unfold k4ExtractionValue
    omega

/-- The nested minimum is one of its seven explicit linear bounds. -/
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

/-- Four integral star faces have immediate witnesses. -/
theorem k4Realizable_starA_of_min (n : K4Capacity)
    (h0 : n.ab + n.ac + n.ad ≤ n.ab + n.cd)
    (h1 : n.ab + n.ac + n.ad ≤ n.ac + n.bd)
    (h2 : n.ab + n.ac + n.ad ≤ n.ad + n.bc) :
    ∃ a b c d : ℕ, k4Feasible n a b c d ∧
      k4ExtractionValue a b c d = n.ab + n.ac + n.ad := by
  refine ⟨0, n.ab, n.ac, n.ad, ?_, ?_⟩
  · unfold k4Feasible; omega
  · unfold k4ExtractionValue; omega

theorem k4Realizable_starB_of_min (n : K4Capacity)
    (h0 : n.ab + n.bc + n.bd ≤ n.ab + n.cd)
    (h1 : n.ab + n.bc + n.bd ≤ n.ac + n.bd)
    (h2 : n.ab + n.bc + n.bd ≤ n.ad + n.bc) :
    ∃ a b c d : ℕ, k4Feasible n a b c d ∧
      k4ExtractionValue a b c d = n.ab + n.bc + n.bd := by
  refine ⟨n.ab, 0, n.bc, n.bd, ?_, ?_⟩
  · unfold k4Feasible; omega
  · unfold k4ExtractionValue; omega

theorem k4Realizable_starC_of_min (n : K4Capacity)
    (h0 : n.ac + n.bc + n.cd ≤ n.ab + n.cd)
    (h1 : n.ac + n.bc + n.cd ≤ n.ac + n.bd)
    (h2 : n.ac + n.bc + n.cd ≤ n.ad + n.bc) :
    ∃ a b c d : ℕ, k4Feasible n a b c d ∧
      k4ExtractionValue a b c d = n.ac + n.bc + n.cd := by
  refine ⟨n.ac, n.bc, 0, n.cd, ?_, ?_⟩
  · unfold k4Feasible; omega
  · unfold k4ExtractionValue; omega

theorem k4Realizable_starD_of_min (n : K4Capacity)
    (h0 : n.ad + n.bd + n.cd ≤ n.ab + n.cd)
    (h1 : n.ad + n.bd + n.cd ≤ n.ac + n.bd)
    (h2 : n.ad + n.bd + n.cd ≤ n.ad + n.bc) :
    ∃ a b c d : ℕ, k4Feasible n a b c d ∧
      k4ExtractionValue a b c d = n.ad + n.bd + n.cd := by
  refine ⟨n.ad, n.bd, n.cd, 0, ?_, ?_⟩
  · unfold k4Feasible; omega
  · unfold k4ExtractionValue; omega

end EnterpriseMath.BranchRecoalescence
