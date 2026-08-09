import EnterpriseMath.Precision.BinaryRootAtlasBoundary
import Mathlib.Data.Finset.Card
import Mathlib.Tactic

namespace EnterpriseMath.Precision

open EnterpriseMath.IntegerRoot

/-- Positive quotient-root states seen by denominators `1,...,n`, encoded by
zero-based indices `i=0,...,n-1` with denominator `i+1`. -/
def quotientRootStates (s n : ℕ) : Finset ℕ :=
  (Finset.range n).image (fun i => root (s + 1) (n / (i + 1)))

/-- High-branch root states, again using zero-based denominator indices. -/
def highQuotientRootStates (s n : ℕ) : Finset ℕ :=
  let H := root (s + 2) ((s + 1) * n - 1)
  let D := n / (H + 1) ^ (s + 1)
  (Finset.range D).image (fun i => root (s + 1) (n / (i + 1)))

/-- Guaranteed low roots `1,...,H-1`, represented as a shifted range so their
cardinality is definitionally tied to `H-1`. -/
def guaranteedLowRootStates (H : ℕ) : Finset ℕ :=
  (Finset.range (H - 1)).image (fun i => i + 1)

/-- Actual low-root set.  `H=0` is separated explicitly because zero is not a
positive quotient-root state; for `H>0`, only the final root `H` is optional. -/
def lowQuotientRootStates (s n : ℕ) : Finset ℕ :=
  let H := root (s + 2) ((s + 1) * n - 1)
  let D := n / (H + 1) ^ (s + 1)
  if H = 0 then ∅
  else if (D + 1) * H ^ (s + 1) ≤ n then
    insert H (guaranteedLowRootStates H)
  else
    guaranteedLowRootStates H

/-- The guaranteed low-root set has exactly `H-1` elements. -/
theorem guaranteedLowRootStates_card (H : ℕ) :
    (guaranteedLowRootStates H).card = H - 1 := by
  unfold guaranteedLowRootStates
  exact Finset.card_image_of_injective _ (fun _ _ h => by omega)

/-- Membership in the guaranteed low-root set is exactly the positive interval
strictly below `H`. -/
theorem mem_guaranteedLowRootStates_iff
    {H t : ℕ} :
    t ∈ guaranteedLowRootStates H ↔ 1 ≤ t ∧ t < H := by
  constructor
  · intro ht
    rcases Finset.mem_image.mp ht with ⟨i, hi, rfl⟩
    have hiRange : i < H - 1 := Finset.mem_range.mp hi
    omega
  · rintro ⟨htPos, htH⟩
    let i := t - 1
    have hiRange : i < H - 1 := by
      dsimp [i]
      omega
    have hit : i + 1 = t := by
      dsimp [i]
      omega
    apply Finset.mem_image.mpr
    exact ⟨i, Finset.mem_range.mpr hiRange, hit⟩

/-- The exact high-denominator cutoff never exceeds the physical denominator
range `1,...,n`. -/
theorem root_atlas_cutoff_le_state
    {s n : ℕ} :
    let H := root (s + 2) ((s + 1) * n - 1)
    let D := n / (H + 1) ^ (s + 1)
    D ≤ n := by
  dsimp
  exact Nat.div_le_self _ _

/-- The high quotient-root branch contributes exactly one state per high
positive denominator label, hence exactly `D` states. -/
theorem highQuotientRootStates_card
    {s n : ℕ}
    (hn : 0 < n) :
    let H := root (s + 2) ((s + 1) * n - 1)
    let D := n / (H + 1) ^ (s + 1)
    (highQuotientRootStates s n).card = D := by
  let H := root (s + 2) ((s + 1) * n - 1)
  let D := n / (H + 1) ^ (s + 1)
  change (highQuotientRootStates s n).card = D
  unfold highQuotientRootStates
  dsimp only
  apply Finset.card_image_of_injOn
  intro i hi j hj hEq
  have hiD : i < D := Finset.mem_range.mp hi
  have hjD : j < D := Finset.mem_range.mp hj
  have hDenEq := high_denominator_root_injective
    (s := s) (n := n) (d := i + 1) (e := j + 1)
    hn (by omega) (by omega)
    (by omega) (by omega) hEq
  omega

/-- For a positive horizon, the actual low-root set has exactly the guaranteed
`H-1` roots plus the one horizon indicator bit. -/
theorem lowQuotientRootStates_card_of_horizon_pos
    {s n : ℕ} :
    let H := root (s + 2) ((s + 1) * n - 1)
    let D := n / (H + 1) ^ (s + 1)
    0 < H →
      (lowQuotientRootStates s n).card =
        H - 1 + (if (D + 1) * H ^ (s + 1) ≤ n then 1 else 0) := by
  let H := root (s + 2) ((s + 1) * n - 1)
  let D := n / (H + 1) ^ (s + 1)
  change 0 < H →
    (lowQuotientRootStates s n).card =
      H - 1 + (if (D + 1) * H ^ (s + 1) ≤ n then 1 else 0)
  intro hH
  have hHne : H ≠ 0 := by omega
  have hHnotBase : H ∉ guaranteedLowRootStates H := by
    rw [mem_guaranteedLowRootStates_iff]
    omega
  by_cases hThreshold : (D + 1) * H ^ (s + 1) ≤ n
  · change
      (if H = 0 then ∅
       else if (D + 1) * H ^ (s + 1) ≤ n then
         insert H (guaranteedLowRootStates H)
       else guaranteedLowRootStates H).card = _
    simp [hHne, hThreshold, hHnotBase, guaranteedLowRootStates_card]
  · change
      (if H = 0 then ∅
       else if (D + 1) * H ^ (s + 1) ≤ n then
         insert H (guaranteedLowRootStates H)
       else guaranteedLowRootStates H).card = _
    simp [hHne, hThreshold, guaranteedLowRootStates_card]

/-- The high and actual low root sets are disjoint whenever the horizon is
positive. -/
theorem high_low_root_states_disjoint_of_horizon_pos
    {s n : ℕ}
    (hn : 0 < n) :
    let H := root (s + 2) ((s + 1) * n - 1)
    let D := n / (H + 1) ^ (s + 1)
    0 < H → Disjoint (highQuotientRootStates s n) (lowQuotientRootStates s n) := by
  let H := root (s + 2) ((s + 1) * n - 1)
  let D := n / (H + 1) ^ (s + 1)
  change 0 < H → Disjoint (highQuotientRootStates s n) (lowQuotientRootStates s n)
  intro hH
  apply Finset.disjoint_left.mpr
  intro y hyHigh hyLow

  rcases Finset.mem_image.mp hyHigh with ⟨i, hi, hiy⟩
  have hiD : i < D := Finset.mem_range.mp hi
  have hAbove : H < root (s + 1) (n / (i + 1)) :=
    high_denominator_root_above_horizon (by omega) (by omega)
  have hyAbove : H < y := by
    rw [hiy] at hAbove
    exact hAbove

  have hHne : H ≠ 0 := by omega
  have hyLe : y ≤ H := by
    by_cases hThreshold : (D + 1) * H ^ (s + 1) ≤ n
    · have hLowInsert : y ∈ insert H (guaranteedLowRootStates H) := by
        simpa [lowQuotientRootStates, hHne, hThreshold] using hyLow
      rcases Finset.mem_insert.mp hLowInsert with hyH | hyBase
      · omega
      · have hyRange := (mem_guaranteedLowRootStates_iff.mp hyBase).2
        omega
    · have hyBase : y ∈ guaranteedLowRootStates H := by
        simpa [lowQuotientRootStates, hHne, hThreshold] using hyLow
      have hyRange := (mem_guaranteedLowRootStates_iff.mp hyBase).2
      omega
  omega

/-- For positive horizon, the full quotient-root state set splits exactly into
its injective high branch and its contiguous low branch. -/
theorem quotientRootStates_eq_high_union_low_of_horizon_pos
    {s n : ℕ}
    (hn : 0 < n) :
    let H := root (s + 2) ((s + 1) * n - 1)
    let D := n / (H + 1) ^ (s + 1)
    0 < H →
      quotientRootStates s n =
        highQuotientRootStates s n ∪ lowQuotientRootStates s n := by
  let H := root (s + 2) ((s + 1) * n - 1)
  let D := n / (H + 1) ^ (s + 1)
  change 0 < H →
    quotientRootStates s n =
      highQuotientRootStates s n ∪ lowQuotientRootStates s n
  intro hH
  have hHne : H ≠ 0 := by omega
  have hDLeN : D ≤ n := by
    exact root_atlas_cutoff_le_state (s := s) (n := n)

  have hWitnessMem :
      ∀ {t d : ℕ},
        1 ≤ t → 1 ≤ d → root (s + 1) (n / d) = t →
        t ∈ quotientRootStates s n := by
    intro t d ht hd hRoot
    have hdN : d ≤ n :=
      denominator_le_state_of_positive_root
        (r := s + 1) (n := n) (d := d) (t := t)
        (by omega) hd ht hRoot
    let i := d - 1
    have hiN : i < n := by
      dsimp [i]
      omega
    have hid : i + 1 = d := by
      dsimp [i]
      omega
    unfold quotientRootStates
    apply Finset.mem_image.mpr
    refine ⟨i, Finset.mem_range.mpr hiN, ?_⟩
    rw [hid]
    exact hRoot

  apply Finset.ext
  intro y
  constructor
  · intro hy
    unfold quotientRootStates at hy
    rcases Finset.mem_image.mp hy with ⟨i, hi, rfl⟩
    have hiN : i < n := Finset.mem_range.mp hi
    let d := i + 1
    have hd : 1 ≤ d := by
      dsimp [d]
      omega
    have hdN : d ≤ n := by
      dsimp [d]
      omega
    by_cases hdHigh : d ≤ D
    · apply Finset.mem_union.mpr
      left
      unfold highQuotientRootStates
      dsimp only
      apply Finset.mem_image.mpr
      refine ⟨i, Finset.mem_range.mpr ?_, rfl⟩
      dsimp [d] at hdHigh
      omega
    · apply Finset.mem_union.mpr
      right
      have hDd : D < d := by omega
      have hRootLe : root (s + 1) (n / d) ≤ H :=
        denominator_after_cutoff_root_at_most_horizon hd hDd
      have hOneQuot : 1 ≤ n / d := by
        apply (Nat.le_div_iff_mul_le (by omega)).2
        simpa using hdN
      have hRootPos : 1 ≤ root (s + 1) (n / d) :=
        (Nat.le_nthRoot_iff (n := s + 1) (by omega)).2 (by simpa using hOneQuot)
      by_cases hRootH : root (s + 1) (n / d) = H
      · have hThreshold : (D + 1) * H ^ (s + 1) ≤ n :=
          (horizon_root_fiber_nonempty_iff (s := s) (n := n) hH).1
            ⟨d, hd, hRootH⟩
        have : H ∈ insert H (guaranteedLowRootStates H) := by simp
        simpa [lowQuotientRootStates, hHne, hThreshold, hRootH] using this
      · have hRootLt : root (s + 1) (n / d) < H := by omega
        have hBase : root (s + 1) (n / d) ∈ guaranteedLowRootStates H :=
          mem_guaranteedLowRootStates_iff.mpr ⟨hRootPos, hRootLt⟩
        by_cases hThreshold : (D + 1) * H ^ (s + 1) ≤ n
        · simpa [lowQuotientRootStates, hHne, hThreshold] using
            (Finset.mem_insert_of_mem hBase :
              root (s + 1) (n / d) ∈ insert H (guaranteedLowRootStates H))
        · simpa [lowQuotientRootStates, hHne, hThreshold] using hBase
  · intro hyUnion
    rcases Finset.mem_union.mp hyUnion with hyHigh | hyLow
    · rcases Finset.mem_image.mp hyHigh with ⟨i, hi, hiy⟩
      have hiD : i < D := Finset.mem_range.mp hi
      have hiN : i < n := lt_of_lt_of_le hiD hDLeN
      unfold quotientRootStates
      apply Finset.mem_image.mpr
      exact ⟨i, Finset.mem_range.mpr hiN, hiy⟩
    · by_cases hThreshold : (D + 1) * H ^ (s + 1) ≤ n
      · have hLowInsert : y ∈ insert H (guaranteedLowRootStates H) := by
          simpa [lowQuotientRootStates, hHne, hThreshold] using hyLow
        rcases Finset.mem_insert.mp hLowInsert with hyH | hyBase
        · subst y
          obtain ⟨d, hd, hRoot⟩ :=
            (horizon_root_fiber_nonempty_iff (s := s) (n := n) hH).2 hThreshold
          exact hWitnessMem (by omega) hd hRoot
        · obtain ⟨hyPos, hyHlt⟩ := mem_guaranteedLowRootStates_iff.mp hyBase
          obtain ⟨d, hd, hRoot⟩ :=
            low_root_fiber_nonempty (s := s) (n := n) (t := y) hn hyPos hyHlt
          exact hWitnessMem hyPos hd hRoot
      · have hyBase : y ∈ guaranteedLowRootStates H := by
          simpa [lowQuotientRootStates, hHne, hThreshold] using hyLow
        obtain ⟨hyPos, hyHlt⟩ := mem_guaranteedLowRootStates_iff.mp hyBase
        obtain ⟨d, hd, hRoot⟩ :=
          low_root_fiber_nonempty (s := s) (n := n) (t := y) hn hyPos hyHlt
        exact hWitnessMem hyPos hd hRoot

/-- Positive-horizon binary atlas cardinality in subtraction-free form. -/
theorem quotientRootStates_binary_cardinality_of_horizon_pos
    {s n : ℕ}
    (hn : 0 < n) :
    let H := root (s + 2) ((s + 1) * n - 1)
    let D := n / (H + 1) ^ (s + 1)
    0 < H →
      (quotientRootStates s n).card + 1 =
        D + H + (if (D + 1) * H ^ (s + 1) ≤ n then 1 else 0) := by
  let H := root (s + 2) ((s + 1) * n - 1)
  let D := n / (H + 1) ^ (s + 1)
  change 0 < H →
    (quotientRootStates s n).card + 1 =
      D + H + (if (D + 1) * H ^ (s + 1) ≤ n then 1 else 0)
  intro hH
  have hSet := quotientRootStates_eq_high_union_low_of_horizon_pos
    (s := s) (n := n) hn hH
  have hDisj := high_low_root_states_disjoint_of_horizon_pos
    (s := s) (n := n) hn hH
  have hHighCard := highQuotientRootStates_card (s := s) (n := n) hn
  have hLowCard := lowQuotientRootStates_card_of_horizon_pos
    (s := s) (n := n) hH
  rw [hSet, Finset.card_union_of_disjoint hDisj, hHighCard, hLowCard]
  omega

/-- Zero-horizon case: every physical denominator belongs to the high branch,
so the state count is exactly `D=n`; the binary carry indicator is
arithmetically `1` because `H^r=0`. -/
theorem quotientRootStates_binary_cardinality_of_horizon_zero
    {s n : ℕ}
    (hn : 0 < n) :
    let H := root (s + 2) ((s + 1) * n - 1)
    let D := n / (H + 1) ^ (s + 1)
    H = 0 →
      (quotientRootStates s n).card + 1 =
        D + H + (if (D + 1) * H ^ (s + 1) ≤ n then 1 else 0) := by
  let H := root (s + 2) ((s + 1) * n - 1)
  let D := n / (H + 1) ^ (s + 1)
  change H = 0 →
    (quotientRootStates s n).card + 1 =
      D + H + (if (D + 1) * H ^ (s + 1) ≤ n then 1 else 0)
  intro hH
  have hD : D = n := by
    dsimp [D]
    rw [hH]
    simp
  have hSet : quotientRootStates s n = highQuotientRootStates s n := by
    unfold quotientRootStates highQuotientRootStates
    dsimp only
    rw [hH]
    simp
  have hHighCard := highQuotientRootStates_card (s := s) (n := n) hn
  rw [hSet, hHighCard]
  simp [hH, hD]

/-- Complete binary quotient-root atlas cardinality.

This is the only geometric/cardinality input required by the already formalized
ternary carry reduction: all positive quotient-root states have exact count

`N+1 = D+H+kappa`,

where `kappa` is the single horizon-fiber indicator. -/
theorem quotientRootStates_binary_cardinality
    {s n : ℕ}
    (hn : 0 < n) :
    let H := root (s + 2) ((s + 1) * n - 1)
    let D := n / (H + 1) ^ (s + 1)
    (quotientRootStates s n).card + 1 =
      D + H + (if (D + 1) * H ^ (s + 1) ≤ n then 1 else 0) := by
  let H := root (s + 2) ((s + 1) * n - 1)
  let D := n / (H + 1) ^ (s + 1)
  change (quotientRootStates s n).card + 1 =
    D + H + (if (D + 1) * H ^ (s + 1) ≤ n then 1 else 0)
  by_cases hH : H = 0
  · exact quotientRootStates_binary_cardinality_of_horizon_zero
      (s := s) (n := n) hn hH
  · exact quotientRootStates_binary_cardinality_of_horizon_pos
      (s := s) (n := n) hn (Nat.pos_of_ne_zero hH)

end EnterpriseMath.Precision
