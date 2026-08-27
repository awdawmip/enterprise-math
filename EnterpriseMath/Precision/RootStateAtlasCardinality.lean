import EnterpriseMath.Precision.PowerQuotientCoalescenceGap
import EnterpriseMath.Precision.QuotientRootFiber
import EnterpriseMath.Precision.RootStateCountCarryUpper
import EnterpriseMath.Precision.TernaryBandCarryCount
import Mathlib.Data.Finset.Card
import Mathlib.Data.Finset.Interval
import Mathlib.Tactic

namespace EnterpriseMath.Precision

open EnterpriseMath.IntegerRoot

/-- A quantitative gap between two positive denominator scales forces their
floor quotients to be strictly separated. -/
theorem strict_floor_quotient_of_gap
    {n a b : ℕ}
    (ha : 0 < a)
    (hab : a < b)
    (hgap : a * b < n * (b - a)) :
    n / b < n / a := by
  let q := n / b
  have hb : 0 < b := lt_trans ha hab
  have hqMul : q * b ≤ n := by
    dsimp [q]
    exact Nat.div_mul_le_self n b
  have hqSuccLe : q + 1 ≤ n / a := by
    apply (Nat.le_div_iff_mul_le ha).2
    by_contra hnot
    have hnLt : n < (q + 1) * a := by omega
    have hqCross : q * b < (q + 1) * a := lt_of_le_of_lt hqMul hnLt
    let g := b - a
    have hg : 0 < g := by
      dsimp [g]
      omega
    have hbDecomp : b = a + g := by
      dsimp [g]
      omega
    have hqGap : q * g < a := by
      rw [hbDecomp] at hqCross
      nlinarith
    have hSuccGap : (q + 1) * g < b := by
      rw [hbDecomp]
      nlinarith
    have hnScaled : n * g < ((q + 1) * a) * g :=
      Nat.mul_lt_mul_of_pos_right hnLt hg
    have hReverse : n * (b - a) < a * b := by
      calc
        n * (b - a) = n * g := by rfl
        _ < ((q + 1) * a) * g := hnScaled
        _ = a * ((q + 1) * g) := by ring
        _ < a * b := Nat.mul_lt_mul_of_pos_left hSuccGap ha
    omega
  dsimp [q] at hqSuccLe
  omega

/-- Denominators up through `D=floor(n/(H+1)^r)` always produce roots strictly
above the coalescence horizon `H`. -/
theorem root_state_high_denominator_above_horizon
    {s n d : ℕ} :
    let H := root (s + 2) ((s + 1) * n - 1)
    let D := n / (H + 1) ^ (s + 1)
    1 ≤ d → d ≤ D → H < root (s + 1) (n / d) := by
  let H := root (s + 2) ((s + 1) * n - 1)
  let D := n / (H + 1) ^ (s + 1)
  change 1 ≤ d → d ≤ D → H < root (s + 1) (n / d)
  intro hdPos hdD
  have hXPos : 0 < (H + 1) ^ (s + 1) := pow_pos (by omega) (s + 1)
  have hDMul : D * (H + 1) ^ (s + 1) ≤ n := by
    dsimp [D]
    exact Nat.div_mul_le_self n ((H + 1) ^ (s + 1))
  have hdMul : d * (H + 1) ^ (s + 1) ≤ n := by
    exact le_trans
      (Nat.mul_le_mul_right ((H + 1) ^ (s + 1)) hdD)
      hDMul
  have hPow : (H + 1) ^ (s + 1) ≤ n / d := by
    apply (Nat.le_div_iff_mul_le (by omega)).2
    simpa [Nat.mul_comm] using hdMul
  have hRoot : H + 1 ≤ root (s + 1) (n / d) :=
    (Nat.le_nthRoot_iff (n := s + 1) (by omega)).2 hPow
  omega

/-- Denominators strictly past the high threshold can only produce roots at or
below the horizon. -/
theorem root_state_low_denominator_at_most_horizon
    {s n d : ℕ} :
    let H := root (s + 2) ((s + 1) * n - 1)
    let D := n / (H + 1) ^ (s + 1)
    1 ≤ d → D < d → root (s + 1) (n / d) ≤ H := by
  let H := root (s + 2) ((s + 1) * n - 1)
  let D := n / (H + 1) ^ (s + 1)
  change 1 ≤ d → D < d → root (s + 1) (n / d) ≤ H
  intro hdPos hDd
  have hXPos : 0 < (H + 1) ^ (s + 1) := pow_pos (by omega) (s + 1)
  have hDivLt : n / (H + 1) ^ (s + 1) < d := by
    simpa [D] using hDd
  have hnLt0 : n < d * (H + 1) ^ (s + 1) :=
    (Nat.div_lt_iff_lt_mul hXPos).1 hDivLt
  have hnLt : n < (H + 1) ^ (s + 1) * d := by
    simpa [Nat.mul_comm] using hnLt0
  have hQuotLt : n / d < (H + 1) ^ (s + 1) := by
    apply (Nat.div_lt_iff_lt_mul (by omega)).2
    simpa [Nat.mul_comm] using hnLt
  have hRootLt : root (s + 1) (n / d) < H + 1 :=
    (Nat.nthRoot_lt_iff (n := s + 1) (by omega)).2 hQuotLt
  omega

/-- The high-denominator branch is injective. -/
theorem root_state_high_denominator_injective
    {s n d e : ℕ}
    (hn : 0 < n)
    (hdPos : 1 ≤ d)
    (hde : d < e) :
    let H := root (s + 2) ((s + 1) * n - 1)
    let D := n / (H + 1) ^ (s + 1)
    e ≤ D →
      root (s + 1) (n / d) ≠ root (s + 1) (n / e) := by
  let H := root (s + 2) ((s + 1) * n - 1)
  let D := n / (H + 1) ^ (s + 1)
  change e ≤ D → root (s + 1) (n / d) ≠ root (s + 1) (n / e)
  intro heD hEq
  have hdD : d ≤ D := le_trans (Nat.le_of_lt hde) heD
  have hHigh0 := root_state_high_denominator_above_horizon
    (s := s) (n := n) (d := d)
  have hHigh : H < root (s + 1) (n / d) := by
    simpa [H, D] using hHigh0 hdPos hdD
  have hCollision := state_distinct_divisor_root_collision_gap
    (n := n) (d := d) (e := e) (s := s)
    hn (by omega) hde hEq
  have hGapPos : 1 ≤ e - d := by omega
  have hPowerWeighted :
      (root (s + 1) (n / d)) ^ (s + 2) ≤
        (e - d) * (root (s + 1) (n / d)) ^ (s + 2) := by
    calc
      (root (s + 1) (n / d)) ^ (s + 2)
          = 1 * (root (s + 1) (n / d)) ^ (s + 2) := by simp
      _ ≤ (e - d) * (root (s + 1) (n / d)) ^ (s + 2) :=
        Nat.mul_le_mul_right _ hGapPos
  have hParentOrder : s + 2 ≠ 0 := by omega
  have hHUpper0 : (s + 1) * n - 1 < (H + 1) ^ (s + 2) := by
    dsimp [H]
    exact Nat.lt_pow_nthRoot_add_one hParentOrder ((s + 1) * n - 1)
  have hParentUpper : (s + 1) * n ≤ (H + 1) ^ (s + 2) := by
    omega
  have hRootPower :
      (H + 1) ^ (s + 2) ≤ (root (s + 1) (n / d)) ^ (s + 2) :=
    Nat.pow_le_pow_left (by omega) (s + 2)
  omega

/-- Pure natural-number floor-gap kernel harvested from the independent P018
binary-atlas route. -/
theorem floor_quotient_strict_gap_of_tangent
    {n A B t r u : ℕ}
    (ht : 0 < t)
    (hr : 0 < r)
    (hu : 0 < u)
    (hA : A = t * u)
    (hTangent : A + r * u ≤ B)
    (hHorizon : t * B < r * n) :
    n / B < n / A := by
  have hApos : 0 < A := by
    rw [hA]
    exact Nat.mul_pos ht hu
  have hAB : A ≤ B := by omega
  have hMon : n / B ≤ n / A := Nat.div_le_div_left hAB hApos
  by_contra hnot
  have hEq : n / B = n / A := by omega
  let q := n / B
  have hQB : q * B ≤ n := by
    dsimp [q]
    exact Nat.div_mul_le_self n B
  have hDivSucc : n / A < n / A + 1 := Nat.lt_succ_self _
  have hNltA0 : n < (n / A + 1) * A :=
    (Nat.div_lt_iff_lt_mul hApos).1 hDivSucc
  have hNltA : n < (q + 1) * A := by
    dsimp [q]
    rw [hEq]
    exact hNltA0
  have hQBern : q * (A + r * u) ≤ q * B :=
    Nat.mul_le_mul_left q hTangent
  have hQStrict : q * (A + r * u) < (q + 1) * A :=
    hQBern.trans_lt (hQB.trans_lt hNltA)
  have hQRU : q * r * u < A := by
    nlinarith [hQStrict]
  have hQRUFactored : (q * r) * u < t * u := by
    simpa [hA, Nat.mul_assoc] using hQRU
  have hQRLt : q * r < t :=
    (Nat.mul_lt_mul_right hu).mp hQRUFactored
  have hTBern : t * (A + r * u) ≤ t * B :=
    Nat.mul_le_mul_left t hTangent
  have hCoeffLower : (t + r) * A ≤ t * B := by
    calc
      (t + r) * A = t * (A + r * u) := by
        rw [hA]
        ring
      _ ≤ t * B := hTBern
  have hRNUpper : r * n < r * ((q + 1) * A) :=
    Nat.mul_lt_mul_of_pos_left hNltA hr
  have hCoeffMul : (t + r) * A < (r * (q + 1)) * A := by
    calc
      (t + r) * A ≤ t * B := hCoeffLower
      _ < r * n := hHorizon
      _ < r * ((q + 1) * A) := hRNUpper
      _ = (r * (q + 1)) * A := by ring
  have hCoeff : t + r < r * (q + 1) :=
    (Nat.mul_lt_mul_right hApos).mp hCoeffMul
  have hTLtRQ : t < r * q := by
    nlinarith [hCoeff]
  nlinarith [hQRLt, hTLtRQ]

/-- Every positive root strictly below the horizon is realized by a positive
denominator `d≤n`. -/
theorem root_state_low_root_realized
    {s n t : ℕ}
    (hn : 0 < n)
    (htPos : 0 < t) :
    let H := root (s + 2) ((s + 1) * n - 1)
    t < H →
      ∃ d : ℕ, 1 ≤ d ∧ d ≤ n ∧ root (s + 1) (n / d) = t := by
  let H := root (s + 2) ((s + 1) * n - 1)
  change t < H → ∃ d : ℕ, 1 ≤ d ∧ d ≤ n ∧ root (s + 1) (n / d) = t
  intro htH
  let A := t ^ (s + 1)
  let B := (t + 1) ^ (s + 1)
  let u := t ^ s
  have hu : 0 < u := by
    dsimp [u]
    exact pow_pos htPos s
  have hA : A = t * u := by
    dsimp [A, u]
    rw [pow_succ']
  have hBernRaw :=
    pow_add_mul_le_add_pow (R := ℕ) (a := t) (b := 1)
      (by omega) (by omega) (s + 1)
  have hTangent : A + (s + 1) * u ≤ B := by
    simpa [A, B, u] using hBernRaw
  have hHPos : 0 < H := by omega
  have hBLe : B ≤ H ^ (s + 1) := by
    dsimp [B]
    exact Nat.pow_le_pow_left (by omega) (s + 1)
  have hTBltHPow : t * B < H ^ (s + 2) := by
    calc
      t * B ≤ t * H ^ (s + 1) := Nat.mul_le_mul_left t hBLe
      _ < H * H ^ (s + 1) :=
        Nat.mul_lt_mul_of_pos_right htH (pow_pos hHPos (s + 1))
      _ = H ^ (s + 2) := by
        conv_rhs =>
          rw [show s + 2 = (s + 1) + 1 by omega, pow_succ']
  have hHLower : H ^ (s + 2) ≤ (s + 1) * n - 1 := by
    dsimp [H]
    exact Nat.pow_nthRoot_le (Or.inl (by omega))
  have hHorizon : t * B < (s + 1) * n := by
    calc
      t * B < H ^ (s + 2) := hTBltHPow
      _ ≤ (s + 1) * n - 1 := hHLower
      _ < (s + 1) * n := by
        have hProdPos : 0 < (s + 1) * n := Nat.mul_pos (by omega) hn
        omega
  have hDivGap : n / B < n / A :=
    floor_quotient_strict_gap_of_tangent
      (n := n) (A := A) (B := B) (t := t) (r := s + 1) (u := u)
      htPos (by omega) hu hA hTangent hHorizon
  let d := n / B + 1
  have hdPos : 1 ≤ d := by
    dsimp [d]
    exact Nat.succ_pos _
  have hLower : n / B < d := by
    dsimp [d]
    exact Nat.lt_succ_self _
  have hUpper : d ≤ n / A := by
    dsimp [d]
    exact Nat.succ_le_of_lt hDivGap
  have hdLeN : d ≤ n :=
    le_trans hUpper (Nat.div_le_self n A)
  have hRoot : root (s + 1) (n / d) = t := by
    apply (quotient_root_fiber_iff
      (r := s + 1) (n := n) (d := d) (t := t)
      (by omega) (by omega) htPos).2
    simpa [A, B] using And.intro hLower hUpper
  exact ⟨d, hdPos, hdLeN, hRoot⟩

/-- The horizon root is the unique optional low state. -/
theorem root_state_horizon_realized_iff
    {s n : ℕ}
    (hn : 0 < n) :
    let H := root (s + 2) ((s + 1) * n - 1)
    let D := n / (H + 1) ^ (s + 1)
    (∃ d : ℕ, 1 ≤ d ∧ d ≤ n ∧ root (s + 1) (n / d) = H) ↔
      0 < H ∧ (D + 1) * H ^ (s + 1) ≤ n := by
  let H := root (s + 2) ((s + 1) * n - 1)
  let D := n / (H + 1) ^ (s + 1)
  change
    (∃ d : ℕ, 1 ≤ d ∧ d ≤ n ∧ root (s + 1) (n / d) = H) ↔
      0 < H ∧ (D + 1) * H ^ (s + 1) ≤ n
  constructor
  · rintro ⟨d, hdPos, hdN, hRoot⟩
    have hQuotOne : 1 ≤ n / d := by
      apply (Nat.le_div_iff_mul_le (by omega)).2
      simpa using hdN
    have hRootOne : 1 ≤ root (s + 1) (n / d) :=
      (Nat.le_nthRoot_iff (n := s + 1) (by omega)).2 (by simpa using hQuotOne)
    have hHPos : 0 < H := by
      rw [hRoot] at hRootOne
      omega
    have hFiber := (quotient_root_fiber_iff
      (r := s + 1) (n := n) (d := d) (t := H)
      (by omega) (by omega) hHPos).1 hRoot
    have hLower : D < d := by
      simpa [D] using hFiber.1
    have hUpper : d ≤ n / H ^ (s + 1) := hFiber.2
    have hCarryDiv : D + 1 ≤ n / H ^ (s + 1) := by omega
    have hHPowPos : 0 < H ^ (s + 1) := pow_pos hHPos (s + 1)
    have hCarry : (D + 1) * H ^ (s + 1) ≤ n :=
      (Nat.le_div_iff_mul_le hHPowPos).1 hCarryDiv
    exact ⟨hHPos, hCarry⟩
  · rintro ⟨hHPos, hCarry⟩
    let d := D + 1
    have hHPowPos : 0 < H ^ (s + 1) := pow_pos hHPos (s + 1)
    have hdUpper : d ≤ n / H ^ (s + 1) := by
      apply (Nat.le_div_iff_mul_le hHPowPos).2
      simpa [d] using hCarry
    have hdPos : 1 ≤ d := by
      dsimp [d]
      exact Nat.succ_pos _
    have hdLeN : d ≤ n :=
      le_trans hdUpper (Nat.div_le_self n (H ^ (s + 1)))
    have hRoot : root (s + 1) (n / d) = H := by
      apply (quotient_root_fiber_iff
        (r := s + 1) (n := n) (d := d) (t := H)
        (by omega) (by omega) hHPos).2
      constructor
      · dsimp [d]
        change D < D + 1
        exact Nat.lt_succ_self D
      · exact hdUpper
    exact ⟨d, hdPos, hdLeN, hRoot⟩

/-- Positive quotient-root states seen by denominators `1,...,n`. -/
def quotientRootStates (s n : ℕ) : Finset ℕ :=
  (Finset.range n).image (fun i : ℕ => root (s + 1) (n / (i + 1)))

/-- Guaranteed low root states `1,...,H-1`. -/
def guaranteedLowRootStates (H : ℕ) : Finset ℕ :=
  (Finset.range (H - 1)).image (fun i : ℕ => i + 1)

/-- Low-root chart with the horizon carry bit explicit. -/
def lowRootStatesAt (r H D n : ℕ) : Finset ℕ :=
  if H = 0 then ∅
  else if (D + 1) * H ^ r ≤ n then
    insert H (guaranteedLowRootStates H)
  else
    guaranteedLowRootStates H

/-- The guaranteed low-root interval has `H-1` states. -/
theorem guaranteedLowRootStates_card (H : ℕ) :
    (guaranteedLowRootStates H).card = H - 1 := by
  unfold guaranteedLowRootStates
  calc
    ((Finset.range (H - 1)).image (fun i : ℕ => i + 1)).card =
        (Finset.range (H - 1)).card :=
      Finset.card_image_of_injective (Finset.range (H - 1)) (by
        intro i j hij
        exact Nat.add_right_cancel hij)
    _ = H - 1 := Finset.card_range (H - 1)

/-- Membership in the guaranteed low-root set is exactly `1 ≤ t < H`. -/
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

/-- Explicit low-chart membership for a positive horizon. -/
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

/-- The low chart has `H-1` forced states plus the optional horizon state. -/
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

/-- The high-denominator image has exactly `D` distinct states. -/
theorem root_state_high_states_card
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
    by_contra hne
    by_cases hijlt : i < j
    · have hNo0 := root_state_high_denominator_injective
        (s := s) (n := n) (d := i + 1) (e := j + 1)
        hn (by omega) (by omega)
      have hNo : f i ≠ f j := by
        simpa [f, H, D] using hNo0 (Nat.succ_le_of_lt hjD)
      exact hNo hij
    · have hjilt : j < i := by omega
      have hNo0 := root_state_high_denominator_injective
        (s := s) (n := n) (d := j + 1) (e := i + 1)
        hn (by omega) (by omega)
      have hNo : f j ≠ f i := by
        simpa [f, H, D] using hNo0 (Nat.succ_le_of_lt hiD)
      exact hNo hij.symm
  calc
    ((Finset.range D).image f).card = (Finset.range D).card :=
      Finset.card_image_of_injOn hInj
    _ = D := Finset.card_range D

/-- Any positive witness with `d≤n` lies in the finite atlas. -/
theorem mem_quotientRootStates_of_witness
    {s n t d : ℕ}
    (hd : 1 ≤ d)
    (hdN : d ≤ n)
    (hRoot : root (s + 1) (n / d) = t) :
    t ∈ quotientRootStates s n := by
  let i := d - 1
  have hiN : i < n := by
    dsimp [i]
    omega
  have hid : i + 1 = d := by
    dsimp [i]
    omega
  unfold quotientRootStates
  apply Finset.mem_image.mpr
  exact ⟨i, Finset.mem_range.mpr hiN, by simpa [hid] using hRoot⟩

/-- For positive horizon the atlas is exactly the high image plus the low chart. -/
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
    have hd : 1 ≤ d := by dsimp [d]; omega
    have hdN : d ≤ n := by dsimp [d]; omega
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
      have hRootLe0 := root_state_low_denominator_at_most_horizon
        (s := s) (n := n) (d := d)
      have hRootLe : root (s + 1) (n / d) ≤ H := by
        simpa [H, D] using hRootLe0 hd hDd
      have hOneQuot : 1 ≤ n / d := by
        apply (Nat.le_div_iff_mul_le (by omega)).2
        simpa using hdN
      have hRootPos : 1 ≤ root (s + 1) (n / d) :=
        (Nat.le_nthRoot_iff (n := s + 1) (by omega)).2 (by simpa using hOneQuot)
      have hyLe : y ≤ H := by
        rw [← hiy]
        simpa [f, d] using hRootLe
      have hyPos : 1 ≤ y := by
        rw [← hiy]
        simpa [f, d] using hRootPos
      by_cases hyH : y = H
      · have hRootH : root (s + 1) (n / d) = H := by
          simpa [f, d, hyH] using hiy
        have hIff :
            (∃ e : ℕ, 1 ≤ e ∧ e ≤ n ∧ root (s + 1) (n / e) = H) ↔
              0 < H ∧ (D + 1) * H ^ (s + 1) ≤ n := by
          simpa [H, D] using root_state_horizon_realized_iff (s := s) (n := n) hn
        have hPair := hIff.mp ⟨d, hd, hdN, hRootH⟩
        exact (mem_lowRootStatesAt_iff hH).2 (Or.inr ⟨hPair.2, hyH⟩)
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
        have hReal0 := root_state_low_root_realized
          (s := s) (n := n) (t := y) hn (by omega)
        obtain ⟨d, hd, hdN, hRoot⟩ := by
          simpa [H] using hReal0 hyHlt
        exact mem_quotientRootStates_of_witness hd hdN hRoot
      · subst y
        have hIff :
            (∃ e : ℕ, 1 ≤ e ∧ e ≤ n ∧ root (s + 1) (n / e) = H) ↔
              0 < H ∧ (D + 1) * H ^ (s + 1) ≤ n := by
          simpa [H, D] using root_state_horizon_realized_iff (s := s) (n := n) hn
        obtain ⟨d, hd, hdN, hRoot⟩ := hIff.mpr ⟨hH, hThreshold⟩
        exact mem_quotientRootStates_of_witness hd hdN hRoot

/-- The high and low charts are disjoint for positive horizon. -/
theorem root_state_high_low_disjoint_of_horizon_pos
    {s n : ℕ}
    (_hn : 0 < n) :
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
  change 0 < H → Disjoint ((Finset.range D).image f) (lowRootStatesAt (s + 1) H D n)
  intro hH
  apply Finset.disjoint_left.mpr
  intro y hyHigh hyLow
  rcases Finset.mem_image.mp hyHigh with ⟨i, hi, hiy⟩
  have hiD : i < D := Finset.mem_range.mp hi
  have hAbove0 := root_state_high_denominator_above_horizon
    (s := s) (n := n) (d := i + 1)
  have hAbove : H < root (s + 1) (n / (i + 1)) := by
    simpa [H, D] using hAbove0 (by omega) (Nat.succ_le_of_lt hiD)
  have hyAbove : H < y := by
    rw [← hiy]
    simpa [f] using hAbove
  rcases (mem_lowRootStatesAt_iff hH).1 hyLow with hyBase | ⟨_, hyH⟩
  · have hyLt := (mem_guaranteedLowRootStates_iff.mp hyBase).2
    omega
  · omega

/-- Exact binary quotient-root atlas cardinality. -/
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
      simpa [H, D] using root_state_high_states_card (s := s) (n := n) hn
    rw [hSet, hHighCard]
    simp [hH0, hD]
  · have hH : 0 < H := Nat.pos_of_ne_zero hH0
    have hSet0 := quotientRootStates_eq_high_union_low_of_horizon_pos
      (s := s) (n := n) hn hH
    have hSet : quotientRootStates s n = High ∪ Low := by
      simpa [High, Low, H, D] using hSet0
    have hDisj0 := root_state_high_low_disjoint_of_horizon_pos
      (s := s) (n := n) hn hH
    have hDisj : Disjoint High Low := by
      simpa [High, Low, H, D] using hDisj0
    have hHighCard : High.card = D := by
      dsimp [High]
      simpa [H, D] using root_state_high_states_card (s := s) (n := n) hn
    have hLowCard : Low.card =
        H - 1 + (if (D + 1) * H ^ (s + 1) ≤ n then 1 else 0) := by
      dsimp [Low]
      exact lowRootStatesAt_card hH
    rw [hSet, Finset.card_union_of_disjoint hDisj, hHighCard, hLowCard]
    omega

/-- Final exact ternary threshold-to-cardinality theorem. -/
theorem quotientRootStates_ternary_cardinality
    {s n : ℕ}
    (hn : 0 < n) :
    let H := root (s + 2) ((s + 1) * n - 1)
    let q := H / (s + 1)
    let X := (H + 1) ^ (s + 1)
    let Y := H ^ (s + 1)
    let A := max (q * X) ((q + 1) * Y)
    let B := (q + 1) * X
    let tau := if n < A then 0 else if n < B then 1 else 2
    (quotientRootStates s n).card + 1 = H + q + tau := by
  let H := root (s + 2) ((s + 1) * n - 1)
  let D := n / (H + 1) ^ (s + 1)
  let q := H / (s + 1)
  let X := (H + 1) ^ (s + 1)
  let Y := H ^ (s + 1)
  change (quotientRootStates s n).card + 1 =
    H + q + (if n < max (q * X) ((q + 1) * Y) then 0
      else if n < (q + 1) * X then 1 else 2)
  have hBand0 := root_state_denominator_three_point_band (s := s) (n := n) hn
  have hBand : q - 1 ≤ D ∧ D ≤ q + 1 := by
    simpa [H, D, q] using hBand0
  have hXPos : 0 < X := by
    dsimp [X]
    exact pow_pos (by omega) (s + 1)
  have hCellLower : D * X ≤ n := by
    dsimp [D, X]
    exact Nat.div_mul_le_self n ((H + 1) ^ (s + 1))
  have hCellUpper : n < (D + 1) * X := by
    have hDivSucc : n / X < n / X + 1 := Nat.lt_succ_self _
    have hMul := (Nat.div_lt_iff_lt_mul hXPos).1 hDivSucc
    simpa [D, X] using hMul
  have hLowerForced : 1 ≤ q → D = q - 1 → (D + 1) * Y ≤ n := by
    intro hq hD
    have h0 := root_state_lower_band_forces_horizon_threshold
      (s := s) (n := n) hn
    simpa [H, D, q, Y] using h0 hq hD
  have hUpperForced : D = q + 1 → (D + 1) * Y ≤ n := by
    intro hD
    have h0 := root_state_upper_band_forces_horizon_threshold
      (s := s) (n := n) hn
    simpa [H, D, q, Y] using h0 hD
  have hCount0 := quotientRootStates_binary_cardinality (s := s) (n := n) hn
  have hCount : (quotientRootStates s n).card + 1 =
      D + H + (if (D + 1) * Y ≤ n then 1 else 0) := by
    simpa [H, D, Y] using hCount0
  have hFinal := ternary_count_from_binary_carry
    (n := n) (D := D) (q := q) (X := X) (Y := Y) (H := H)
    (N := (quotientRootStates s n).card)
    hBand.1 hBand.2 hCellLower hCellUpper hLowerForced hUpperForced hCount
  simpa using hFinal

end EnterpriseMath.Precision
