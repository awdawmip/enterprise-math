import EnterpriseMath.Precision.BinaryRootAtlasBoundary
import Mathlib.Data.Finset.Card
import Mathlib.Tactic

namespace EnterpriseMath.Precision

open EnterpriseMath.IntegerRoot

/-- Positive quotient-root states seen by denominators `1,...,n`, encoded by
zero-based indices `i=0,...,n-1` with denominator `i+1`. -/
def quotientRootStates (s n : ℕ) : Finset ℕ :=
  (Finset.range n).image (fun i : ℕ => root (s + 1) (n / (i + 1)))

/-- Guaranteed low roots `1,...,H-1`. -/
def guaranteedLowRootStates (H : ℕ) : Finset ℕ :=
  (Finset.range (H - 1)).image (fun i : ℕ => i + 1)

/-- Low-root chart with the exact horizon bit made explicit in the parameters.
Using explicit `H,D` avoids repeatedly unfolding the root and quotient scales
inside finite-set proofs. -/
def lowRootStatesAt (r H D n : ℕ) : Finset ℕ :=
  if H = 0 then ∅
  else if (D + 1) * H ^ r ≤ n then
    insert H (guaranteedLowRootStates H)
  else
    guaranteedLowRootStates H

/-- The guaranteed low-root set has exactly `H-1` elements. -/
theorem guaranteedLowRootStates_card (H : ℕ) :
    (guaranteedLowRootStates H).card = H - 1 := by
  unfold guaranteedLowRootStates
  calc
    ((Finset.range (H - 1)).image (fun i : ℕ => i + 1)).card =
        (Finset.range (H - 1)).card :=
      Finset.card_image_of_injective (Finset.range (H - 1)) (by
        intro i j hij
        omega)
    _ = H - 1 := Finset.card_range (H - 1)

/-- Membership in the guaranteed low-root set is exactly the positive interval
strictly below `H`. -/
theorem mem_guaranteedLowRootStates_iff
    {H t : ℕ} :
    t ∈ guaranteedLowRootStates H ↔ 1 ≤ t ∧ t < H := by
  constructor
  · intro ht
    rcases Finset.mem_image.mp ht with ⟨i, hi, hEq⟩
    have hiRange : i < H - 1 := Finset.mem_range.mp hi
    rw [← hEq]
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

/-- Explicit membership description of the low chart for positive horizon. -/
theorem mem_lowRootStatesAt_iff
    {r H D n y : ℕ}
    (hH : 0 < H) :
    y ∈ lowRootStatesAt r H D n ↔
      y ∈ guaranteedLowRootStates H ∨
        ((D + 1) * H ^ r ≤ n ∧ y = H) := by
  have hHne : H ≠ 0 := by omega
  by_cases hThreshold : (D + 1) * H ^ r ≤ n
  · simp [lowRootStatesAt, hHne, hThreshold, or_comm]
  · simp [lowRootStatesAt, hHne, hThreshold]

/-- For positive horizon, the explicit low chart has `H-1` guaranteed states
plus exactly one horizon state when the boundary threshold is present. -/
theorem lowRootStatesAt_card
    {r H D n : ℕ}
    (hH : 0 < H) :
    (lowRootStatesAt r H D n).card =
      H - 1 + (if (D + 1) * H ^ r ≤ n then 1 else 0) := by
  have hHne : H ≠ 0 := by omega
  have hHnotBase : H ∉ guaranteedLowRootStates H := by
    rw [mem_guaranteedLowRootStates_iff]
    omega
  by_cases hThreshold : (D + 1) * H ^ r ≤ n
  · simp [lowRootStatesAt, hHne, hThreshold, hHnotBase,
      guaranteedLowRootStates_card]
  · simp [lowRootStatesAt, hHne, hThreshold,
      guaranteedLowRootStates_card]

/-- The exact high-denominator image has cardinality `D`. -/
theorem highRootStates_card
    {s n : ℕ}
    (hn : 0 < n) :
    let H := root (s + 2) ((s + 1) * n - 1)
    let D := n / (H + 1) ^ (s + 1)
    ((Finset.range D).image
      (fun i : ℕ => root (s + 1) (n / (i + 1)))).card = D := by
  let H := root (s + 2) ((s + 1) * n - 1)
  let D := n / (H + 1) ^ (s + 1)
  let f : ℕ → ℕ := fun i => root (s + 1) (n / (i + 1))
  change ((Finset.range D).image f).card = D
  have hInj : Set.InjOn f (↑(Finset.range D) : Set ℕ) := by
    intro i hi j hj hij
    have hiD : i < D := Finset.mem_range.mp hi
    have hjD : j < D := Finset.mem_range.mp hj
    have hiDenLe : i + 1 ≤ D := Nat.succ_le_of_lt hiD
    have hjDenLe : j + 1 ≤ D := Nat.succ_le_of_lt hjD
    have hDenEq : i + 1 = j + 1 := by
      apply high_denominator_root_injective
        (s := s) (n := n) (d := i + 1) (e := j + 1)
        hn (by omega) (by omega)
      · simpa [D, H] using hiDenLe
      · simpa [D, H] using hjDenLe
      · simpa [f] using hij
    omega
  calc
    ((Finset.range D).image f).card = (Finset.range D).card :=
      Finset.card_image_of_injOn hInj
    _ = D := Finset.card_range D

/-- A positive realized quotient-root witness belongs to the physical state
finset automatically. -/
theorem mem_quotientRootStates_of_positive_witness
    {s n t d : ℕ}
    (ht : 1 ≤ t)
    (hd : 1 ≤ d)
    (hRoot : root (s + 1) (n / d) = t) :
    t ∈ quotientRootStates s n := by
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

/-- Positive-horizon atlas decomposition: the full state image is the disjoint
union of the injective high-denominator chart and the explicit low-root chart. -/
theorem quotientRootStates_eq_high_union_low_of_horizon_pos
    {s n : ℕ}
    (hn : 0 < n) :
    let H := root (s + 2) ((s + 1) * n - 1)
    let D := n / (H + 1) ^ (s + 1)
    0 < H →
      quotientRootStates s n =
        (Finset.range D).image
          (fun i : ℕ => root (s + 1) (n / (i + 1))) ∪
        lowRootStatesAt (s + 1) H D n := by
  let H := root (s + 2) ((s + 1) * n - 1)
  let D := n / (H + 1) ^ (s + 1)
  let f : ℕ → ℕ := fun i => root (s + 1) (n / (i + 1))
  change 0 < H →
    quotientRootStates s n =
      (Finset.range D).image f ∪ lowRootStatesAt (s + 1) H D n
  intro hH
  have hDLeN : D ≤ n := Nat.div_le_self _ _
  apply Finset.ext
  intro y
  constructor
  · intro hy
    unfold quotientRootStates at hy
    rcases Finset.mem_image.mp hy with ⟨i, hi, hiy⟩
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
      apply Finset.mem_image.mpr
      refine ⟨i, Finset.mem_range.mpr ?_, ?_⟩
      · dsimp [d] at hdHigh
        omega
      · simpa [f] using hiy
    · apply Finset.mem_union.mpr
      right
      have hDd : D < d := by omega
      have hRootLe0 : root (s + 1) (n / d) ≤ H :=
        denominator_after_cutoff_root_at_most_horizon hd hDd
      have hOneQuot : 1 ≤ n / d := by
        apply (Nat.le_div_iff_mul_le (by omega)).2
        simpa using hdN
      have hRootPos0 : 1 ≤ root (s + 1) (n / d) :=
        (Nat.le_nthRoot_iff (n := s + 1) (by omega)).2 (by simpa using hOneQuot)
      have hyLe : y ≤ H := by
        rw [← hiy]
        simpa [f, d] using hRootLe0
      have hyPos : 1 ≤ y := by
        rw [← hiy]
        simpa [f, d] using hRootPos0
      by_cases hyH : y = H
      · have hRootH : root (s + 1) (n / d) = H := by
          simpa [f, d, hyH] using hiy
        have hThreshold : (D + 1) * H ^ (s + 1) ≤ n :=
          (horizon_root_fiber_nonempty_iff (s := s) (n := n) hH).1
            ⟨d, hd, hRootH⟩
        exact (mem_lowRootStatesAt_iff hH).2 (Or.inr ⟨hThreshold, hyH⟩)
      · have hyLt : y < H := by omega
        have hBase : y ∈ guaranteedLowRootStates H :=
          mem_guaranteedLowRootStates_iff.mpr ⟨hyPos, hyLt⟩
        exact (mem_lowRootStatesAt_iff hH).2 (Or.inl hBase)
  · intro hyUnion
    rcases Finset.mem_union.mp hyUnion with hyHigh | hyLow
    · rcases Finset.mem_image.mp hyHigh with ⟨i, hi, hiy⟩
      have hiD : i < D := Finset.mem_range.mp hi
      have hiN : i < n := lt_of_lt_of_le hiD hDLeN
      unfold quotientRootStates
      apply Finset.mem_image.mpr
      exact ⟨i, Finset.mem_range.mpr hiN, by simpa [f] using hiy⟩
    · rcases (mem_lowRootStatesAt_iff hH).1 hyLow with hyBase | ⟨hThreshold, hyH⟩
      · obtain ⟨hyPos, hyHlt⟩ := mem_guaranteedLowRootStates_iff.mp hyBase
        obtain ⟨d, hd, hRoot⟩ :=
          low_root_fiber_nonempty (s := s) (n := n) (t := y) hn hyPos hyHlt
        exact mem_quotientRootStates_of_positive_witness hyPos hd hRoot
      · subst y
        obtain ⟨d, hd, hRoot⟩ :=
          (horizon_root_fiber_nonempty_iff (s := s) (n := n) hH).2 hThreshold
        exact mem_quotientRootStates_of_positive_witness (by omega) hd hRoot

/-- The explicit high and low charts are disjoint for positive horizon. -/
theorem high_low_root_states_disjoint_of_horizon_pos
    {s n : ℕ}
    (hn : 0 < n) :
    let H := root (s + 2) ((s + 1) * n - 1)
    let D := n / (H + 1) ^ (s + 1)
    0 < H →
      Disjoint
        ((Finset.range D).image
          (fun i : ℕ => root (s + 1) (n / (i + 1))))
        (lowRootStatesAt (s + 1) H D n) := by
  let H := root (s + 2) ((s + 1) * n - 1)
  let D := n / (H + 1) ^ (s + 1)
  let f : ℕ → ℕ := fun i => root (s + 1) (n / (i + 1))
  change 0 < H →
    Disjoint ((Finset.range D).image f) (lowRootStatesAt (s + 1) H D n)
  intro hH
  apply Finset.disjoint_left.mpr
  intro y hyHigh hyLow
  rcases Finset.mem_image.mp hyHigh with ⟨i, hi, hiy⟩
  have hiD : i < D := Finset.mem_range.mp hi
  have hiDenLe : i + 1 ≤ D := Nat.succ_le_of_lt hiD
  have hAbove0 : H < root (s + 1) (n / (i + 1)) := by
    apply high_denominator_root_above_horizon (s := s) (n := n) (d := i + 1)
      (by omega)
    simpa [D, H] using hiDenLe
  have hyAbove : H < y := by
    rw [← hiy]
    simpa [f] using hAbove0
  rcases (mem_lowRootStatesAt_iff hH).1 hyLow with hyBase | ⟨_, hyH⟩
  · have hyLt := (mem_guaranteedLowRootStates_iff.mp hyBase).2
    omega
  · omega

/-- Complete binary quotient-root atlas cardinality.

All positive quotient-root states satisfy the exact subtraction-free count

`N+1 = D+H+kappa`,

where `kappa` is the single horizon-fiber indicator.  This is the geometric
input consumed by the already-formalized ternary carry reduction. -/
theorem quotientRootStates_binary_cardinality
    {s n : ℕ}
    (hn : 0 < n) :
    let H := root (s + 2) ((s + 1) * n - 1)
    let D := n / (H + 1) ^ (s + 1)
    (quotientRootStates s n).card + 1 =
      D + H + (if (D + 1) * H ^ (s + 1) ≤ n then 1 else 0) := by
  let H := root (s + 2) ((s + 1) * n - 1)
  let D := n / (H + 1) ^ (s + 1)
  let High : Finset ℕ :=
    (Finset.range D).image (fun i : ℕ => root (s + 1) (n / (i + 1)))
  let Low : Finset ℕ := lowRootStatesAt (s + 1) H D n
  change (quotientRootStates s n).card + 1 =
    D + H + (if (D + 1) * H ^ (s + 1) ≤ n then 1 else 0)
  by_cases hH0 : H = 0
  · have hD : D = n := by
      dsimp [D]
      rw [hH0]
      simp
    have hSet : quotientRootStates s n = High := by
      unfold quotientRootStates
      dsimp [High]
      rw [hD]
    have hHighCard : High.card = D := by
      dsimp [High]
      simpa [H, D] using highRootStates_card (s := s) (n := n) hn
    rw [hSet, hHighCard]
    simp [hH0, hD]
  · have hH : 0 < H := Nat.pos_of_ne_zero hH0
    have hSet0 := quotientRootStates_eq_high_union_low_of_horizon_pos
      (s := s) (n := n) hn hH
    have hSet : quotientRootStates s n = High ∪ Low := by
      simpa [High, Low, H, D] using hSet0
    have hDisj0 := high_low_root_states_disjoint_of_horizon_pos
      (s := s) (n := n) hn hH
    have hDisj : Disjoint High Low := by
      simpa [High, Low, H, D] using hDisj0
    have hHighCard : High.card = D := by
      dsimp [High]
      simpa [H, D] using highRootStates_card (s := s) (n := n) hn
    have hLowCard : Low.card =
        H - 1 + (if (D + 1) * H ^ (s + 1) ≤ n then 1 else 0) := by
      dsimp [Low]
      exact lowRootStatesAt_card hH
    rw [hSet, Finset.card_union_of_disjoint hDisj, hHighCard, hLowCard]
    omega

end EnterpriseMath.Precision
