import EnterpriseMath.Arithmetic.IntegerRoot
import EnterpriseMath.Relation.BranchRecoalescence
import Mathlib.Data.Finset.Card
import Mathlib.Data.Finset.Union
import Mathlib.Tactic

namespace EnterpriseMath.PowerBRCTrichotomy

open EnterpriseMath.IntegerRoot
open EnterpriseMath.BranchRecoalescence

/-- Refine the exact p-th-power parent state `k^p` by the integer factor `r`. -/
def refinedPowerInput (p r k : ℕ) : ℕ :=
  r * k ^ p

/-- Exact root index after refinement. -/
def rootIndex (p r k : ℕ) : ℕ :=
  EnterpriseMath.IntegerRoot.root p (refinedPowerInput p r k)

/-- The refinement is aligned when it is itself an exact p-th power. -/
def Aligned (p r : ℕ) : Prop :=
  ∃ a : ℕ, r = a ^ p

/-- The sub-threshold interval-funnel regime. -/
def Funnel (p r : ℕ) : Prop :=
  ¬ Aligned p r ∧ r < 2 ^ p

/-- The super-threshold collision-free binary regime. -/
def Binary (p r : ℕ) : Prop :=
  ¬ Aligned p r ∧ 2 ^ p < r

/-- The upper child root index, respecting the exact-power singleton convention. -/
def childUpper (p r k : ℕ) : ℕ :=
  if rootIndex p r k ^ p = refinedPowerInput p r k then
    rootIndex p r k
  else
    rootIndex p r k + 1

/-- Exact finite root-index support produced by one endpoint-BRC step from one parent. -/
def childRootFinset (p r k : ℕ) : Finset ℕ :=
  if rootIndex p r k ^ p = refinedPowerInput p r k then
    {rootIndex p r k}
  else
    {rootIndex p r k, rootIndex p r k + 1}

/-- Union of all one-parent child supports. -/
def childRootFinsetOf (p r : ℕ) (S : Finset ℕ) : Finset ℕ :=
  S.biUnion (childRootFinset p r)

/-- Iterate exact finite root-index BRC support. -/
def iterateRootFinset (p r : ℕ) : ℕ → Finset ℕ → Finset ℕ
  | 0, S => S
  | t + 1, S => childRootFinsetOf p r (iterateRootFinset p r t S)

/-- Root-index relational step, as a direct specialization of canonical Boolean BRC support. -/
def rootChildRel (p r : ℕ) : EnterpriseMath.BranchRecoalescence.Rel ℕ :=
  fun k j => j ∈ childRootFinset p r k

/-- Actual p-th-power support corresponding to a finite root-index support. -/
def powerSupport (p : ℕ) (S : Finset ℕ) : Finset ℕ :=
  S.image (fun k => k ^ p)

/-- Exact p-th-power endpoint relation on actual states. -/
def powerEndpointRel (p r : ℕ) : EnterpriseMath.BranchRecoalescence.Rel ℕ :=
  fun x y => ∃ k j : ℕ,
    x = k ^ p ∧ j ∈ childRootFinset p r k ∧ y = j ^ p

/-- L01: the refined input lies in the exact basin indexed by `rootIndex`. -/
theorem rootIndex_basin {p r k : ℕ} (hp : p ≠ 0) :
    rootIndex p r k ^ p ≤ refinedPowerInput p r k ∧
      refinedPowerInput p r k < (rootIndex p r k + 1) ^ p := by
  exact (EnterpriseMath.IntegerRoot.root_eq_iff hp).1 rfl

/-- Root index is monotone in the parent root index. -/
theorem rootIndex_monotone {p r : ℕ} (hp : p ≠ 0) :
    Monotone (rootIndex p r) := by
  intro k l hkl
  apply EnterpriseMath.IntegerRoot.root_monotone hp
  exact Nat.mul_le_mul_left r (Nat.pow_le_pow_left hkl p)

/-- Zero is always exact and never branches. -/
@[simp] theorem rootIndex_zero {p r : ℕ} (hp : p ≠ 0) :
    rootIndex p r 0 = 0 := by
  simp [rootIndex, refinedPowerInput, EnterpriseMath.IntegerRoot.root, hp]

/-- Zero has singleton root-index child support for every positive exponent. -/
@[simp] theorem childRootFinset_zero {p r : ℕ} (hp : p ≠ 0) :
    childRootFinset p r 0 = {0} := by
  simp [childRootFinset, refinedPowerInput, rootIndex_zero hp, hp]

/-- Every one-parent support is exactly the integer interval from root to `childUpper`. -/
theorem childRootFinset_eq_Icc (p r k : ℕ) :
    childRootFinset p r k = Finset.Icc (rootIndex p r k) (childUpper p r k) := by
  classical
  by_cases h : rootIndex p r k ^ p = refinedPowerInput p r k
  · ext j
    simp [childRootFinset, childUpper, h]
  · ext j
    simp [childRootFinset, childUpper, h]
    omega

/-- Every child is either the lower root or its immediate successor. -/
theorem mem_childRootFinset_cases {p r k j : ℕ}
    (h : j ∈ childRootFinset p r k) :
    j = rootIndex p r k ∨ j = rootIndex p r k + 1 := by
  by_cases hexact : rootIndex p r k ^ p = refinedPowerInput p r k
  · simp [childRootFinset, hexact] at h
    exact Or.inl h
  · simp [childRootFinset, hexact] at h
    exact h

/-- Every child support has cardinality at most two. -/
theorem childRootFinset_card_le_two (p r k : ℕ) :
    (childRootFinset p r k).card ≤ 2 := by
  by_cases h : rootIndex p r k ^ p = refinedPowerInput p r k
  · simp [childRootFinset, h]
  · simp [childRootFinset, h]

/-- The upper endpoint always lies at or above the lower root index. -/
theorem rootIndex_le_childUpper (p r k : ℕ) :
    rootIndex p r k ≤ childUpper p r k := by
  by_cases h : rootIndex p r k ^ p = refinedPowerInput p r k <;>
    simp [childUpper, h]

/-- L02 arithmetic identity for aligned refinement. -/
theorem refinedPowerInput_aligned (p a k : ℕ) :
    refinedPowerInput p (a ^ p) k = (a * k) ^ p := by
  simp [refinedPowerInput, mul_pow]

/-- L02: aligned refinement sends root index `k` exactly to `a*k`. -/
theorem rootIndex_aligned {p : ℕ} (hp : p ≠ 0) (a k : ℕ) :
    rootIndex p (a ^ p) k = a * k := by
  rw [rootIndex, refinedPowerInput_aligned]
  exact EnterpriseMath.IntegerRoot.root_pow hp (a * k)

/-- L02: aligned refinement creates a singleton child. -/
theorem childRootFinset_aligned {p : ℕ} (hp : p ≠ 0) (a k : ℕ) :
    childRootFinset p (a ^ p) k = {a * k} := by
  have hroot := rootIndex_aligned hp a k
  have hinput := refinedPowerInput_aligned p a k
  simp [childRootFinset, hroot, hinput]

/-- Aligned refinements are exactly classified as aligned. -/
theorem aligned_self (p a : ℕ) : Aligned p (a ^ p) :=
  ⟨a, rfl⟩

/-- `r=2^p` is aligned, not binary. -/
theorem threshold_aligned (p : ℕ) : Aligned p (2 ^ p) :=
  ⟨2, rfl⟩

/-- The super-threshold square island `r=9` is aligned. -/
theorem square_nine_aligned : Aligned 2 9 := by
  refine ⟨3, ?_⟩
  norm_num

/-- L02 repeated corollary: aligned refinement never creates fresh branches. -/
theorem aligned_iterate_singleton {p : ℕ} (hp : p ≠ 0) (a k t : ℕ) :
    iterateRootFinset p (a ^ p) t {k} = {a ^ t * k} := by
  induction t with
  | zero => simp [iterateRootFinset]
  | succ t ih =>
      simp [iterateRootFinset, ih, childRootFinsetOf, childRootFinset_aligned hp,
        pow_succ, mul_left_comm, mul_comm]

/-- L03 load-bearing cancellation lemma: a positive parent cannot hide nonalignment. -/
theorem positive_nonaligned_input_not_power {p r k : ℕ}
    (hp : 2 ≤ p) (hk : 0 < k) (hnonaligned : ¬ Aligned p r) :
    ¬ ∃ b : ℕ, b ^ p = refinedPowerInput p r k := by
  intro h
  rcases h with ⟨b, hb⟩
  have hp0 : p ≠ 0 := by omega
  have hpowDvd : k ^ p ∣ b ^ p := by
    rw [hb]
    refine ⟨r, ?_⟩
    simp [refinedPowerInput, Nat.mul_comm]
  have hdiv : k ∣ b := (Nat.pow_dvd_pow_iff hp0).1 hpowDvd
  rcases hdiv with ⟨a, rfl⟩
  apply hnonaligned
  refine ⟨a, ?_⟩
  have hEq : k ^ p * a ^ p = r * k ^ p := by
    simpa [refinedPowerInput, mul_pow] using hb
  have hkpow : 0 < k ^ p := pow_pos hk p
  have haeqr : a ^ p = r := by
    apply Nat.eq_of_mul_eq_mul_left hkpow
    calc
      k ^ p * a ^ p = r * k ^ p := hEq
      _ = k ^ p * r := by ac_rfl
  exact haeqr.symm

/-- Positive nonalignment makes the root-index child genuinely binary. -/
theorem positive_nonaligned_root_not_exact {p r k : ℕ}
    (hp : 2 ≤ p) (hk : 0 < k) (hnonaligned : ¬ Aligned p r) :
    rootIndex p r k ^ p ≠ refinedPowerInput p r k := by
  intro h
  exact positive_nonaligned_input_not_power hp hk hnonaligned ⟨rootIndex p r k, h⟩

/-- L04 sub-threshold root-index bounds. -/
theorem subthreshold_root_bounds {p r k : ℕ}
    (hp : 2 ≤ p) (hk : 0 < k) (hr1 : 1 < r) (hr2 : r < 2 ^ p) :
    k ≤ rootIndex p r k ∧ rootIndex p r k < 2 * k := by
  have hp0 : p ≠ 0 := by omega
  constructor
  · calc
      k = EnterpriseMath.IntegerRoot.root p (k ^ p) :=
        (EnterpriseMath.IntegerRoot.root_pow hp0 k).symm
      _ ≤ EnterpriseMath.IntegerRoot.root p (refinedPowerInput p r k) := by
        apply EnterpriseMath.IntegerRoot.root_monotone hp0
        calc
          k ^ p = 1 * k ^ p := by simp
          _ ≤ r * k ^ p := Nat.mul_le_mul_right (k ^ p) (Nat.le_of_lt hr1)
      _ = rootIndex p r k := rfl
  · have hkpow : 0 < k ^ p := pow_pos hk p
    have hmul : r * k ^ p < 2 ^ p * k ^ p :=
      Nat.mul_lt_mul_of_pos_right hr2 hkpow
    have hinput : refinedPowerInput p r k < (2 * k) ^ p := by
      simpa [refinedPowerInput, mul_pow] using hmul
    exact (Nat.nthRoot_lt_iff hp0).2 hinput

/-- L04 super-threshold lower root bound. -/
theorem superthreshold_root_lower {p r k : ℕ}
    (hp : 2 ≤ p) (hr : 2 ^ p < r) :
    2 * k ≤ rootIndex p r k := by
  have hp0 : p ≠ 0 := by omega
  have hpow : (2 * k) ^ p ≤ refinedPowerInput p r k := by
    have hle : 2 ^ p ≤ r := Nat.le_of_lt hr
    simpa [refinedPowerInput, mul_pow] using Nat.mul_le_mul_right (k ^ p) hle
  exact (Nat.le_nthRoot_iff hp0).2 hpow

/-- In the strict sub-threshold range, alignment is impossible. -/
theorem subthreshold_not_aligned {p r : ℕ}
    (hp : 2 ≤ p) (hr1 : 1 < r) (hr2 : r < 2 ^ p) :
    ¬ Aligned p r := by
  have hp0 : p ≠ 0 := by omega
  rintro ⟨a, rfl⟩
  have ha2 : 2 ≤ a := by
    by_contra h
    have ha01 : a = 0 ∨ a = 1 := by omega
    rcases ha01 with rfl | rfl
    · simp [hp0] at hr1
    · simp at hr1
  have hpows : 2 ^ p ≤ a ^ p := Nat.pow_le_pow_left ha2 p
  omega

/-- The first positive parent has root index one throughout the funnel range. -/
theorem rootIndex_one_of_subthreshold {p r : ℕ}
    (hp : 2 ≤ p) (hr1 : 1 < r) (hr2 : r < 2 ^ p) :
    rootIndex p r 1 = 1 := by
  have hp0 : p ≠ 0 := by omega
  apply (EnterpriseMath.IntegerRoot.root_eq_iff hp0).2
  constructor
  · simpa [refinedPowerInput] using Nat.le_of_lt hr1
  · simpa [refinedPowerInput] using hr2

/-- L05 positive-parent lower half of funnel spacing. -/
private theorem funnel_spacing_lower_pos {p r k : ℕ}
    (hp : 2 ≤ p) (hk : 0 < k) (hr1 : 1 < r) (hr2 : r < 2 ^ p) :
    rootIndex p r k + 1 ≤ rootIndex p r (k + 1) := by
  have hp0 : p ≠ 0 := by omega
  let m := rootIndex p r k
  have hkm : k ≤ m := by
    simpa [m] using (subthreshold_root_bounds hp hk hr1 hr2).1
  have hbasin : m ^ p ≤ refinedPowerInput p r k := by
    simpa [m] using (rootIndex_basin (p := p) (r := r) (k := k) hp0).1
  have hcross : (m + 1) * k ≤ m * (k + 1) := by
    calc
      (m + 1) * k = m * k + k := by ring
      _ ≤ m * k + m := Nat.add_le_add_left hkm (m * k)
      _ = m * (k + 1) := by ring
  have hcrossp : (m + 1) ^ p * k ^ p ≤ m ^ p * (k + 1) ^ p := by
    simpa [mul_pow] using Nat.pow_le_pow_left hcross p
  have hfull : (m + 1) ^ p * k ^ p ≤
      (r * (k + 1) ^ p) * k ^ p := by
    calc
      (m + 1) ^ p * k ^ p ≤ m ^ p * (k + 1) ^ p := hcrossp
      _ ≤ (r * k ^ p) * (k + 1) ^ p :=
        Nat.mul_le_mul_right ((k + 1) ^ p) hbasin
      _ = (r * (k + 1) ^ p) * k ^ p := by ring
  have hkpow : 0 < k ^ p := pow_pos hk p
  have htarget : (m + 1) ^ p ≤ r * (k + 1) ^ p :=
    Nat.le_of_mul_le_mul_right hfull hkpow
  have hroot : m + 1 ≤ rootIndex p r (k + 1) := by
    exact (Nat.le_nthRoot_iff hp0).2 (by simpa [refinedPowerInput] using htarget)
  simpa [m] using hroot

/-- L05 positive-parent upper half of funnel spacing. -/
private theorem funnel_spacing_upper_pos {p r k : ℕ}
    (hp : 2 ≤ p) (hk : 0 < k) (hr1 : 1 < r) (hr2 : r < 2 ^ p) :
    rootIndex p r (k + 1) ≤ rootIndex p r k + 2 := by
  have hp0 : p ≠ 0 := by omega
  let m := rootIndex p r k
  have hm2k : m < 2 * k := by
    simpa [m] using (subthreshold_root_bounds hp hk hr1 hr2).2
  have hbasin : refinedPowerInput p r k < (m + 1) ^ p := by
    simpa [m] using (rootIndex_basin (p := p) (r := r) (k := k) hp0).2
  have hm1 : m + 1 ≤ 2 * k := by omega
  have hcross : (m + 1) * (k + 1) ≤ k * (m + 3) := by
    calc
      (m + 1) * (k + 1) = m * k + (m + 1 + k) := by ring
      _ ≤ m * k + (2 * k + k) := by
        exact Nat.add_le_add_left (Nat.add_le_add_right hm1 k) (m * k)
      _ = k * (m + 3) := by ring
  have hcrossp : (m + 1) ^ p * (k + 1) ^ p ≤ k ^ p * (m + 3) ^ p := by
    simpa [mul_pow] using Nat.pow_le_pow_left hcross p
  have hk1pow : 0 < (k + 1) ^ p := pow_pos (Nat.succ_pos k) p
  have hfirst : (r * k ^ p) * (k + 1) ^ p <
      (m + 1) ^ p * (k + 1) ^ p :=
    Nat.mul_lt_mul_of_pos_right hbasin hk1pow
  have hfull : (r * (k + 1) ^ p) * k ^ p < (m + 3) ^ p * k ^ p := by
    calc
      (r * (k + 1) ^ p) * k ^ p = (r * k ^ p) * (k + 1) ^ p := by ring
      _ < (m + 1) ^ p * (k + 1) ^ p := hfirst
      _ ≤ k ^ p * (m + 3) ^ p := hcrossp
      _ = (m + 3) ^ p * k ^ p := by ring
  have htarget : r * (k + 1) ^ p < (m + 3) ^ p :=
    Nat.lt_of_mul_lt_mul_right hfull
  have hroot : rootIndex p r (k + 1) < m + 3 := by
    exact (Nat.nthRoot_lt_iff hp0).2 (by simpa [refinedPowerInput] using htarget)
  omega

/-- L05 exact local spacing in the funnel: every step is one or two. -/
theorem funnel_spacing {p r k : ℕ}
    (hp : 2 ≤ p) (hr1 : 1 < r) (hr2 : r < 2 ^ p) :
    rootIndex p r k + 1 ≤ rootIndex p r (k + 1) ∧
      rootIndex p r (k + 1) ≤ rootIndex p r k + 2 := by
  by_cases hk0 : k = 0
  · subst k
    have hp0 : p ≠ 0 := by omega
    have h0 := rootIndex_zero (p := p) (r := r) hp0
    have h1 := rootIndex_one_of_subthreshold hp hr1 hr2
    simp [h0, h1]
  · have hk : 0 < k := Nat.pos_of_ne_zero hk0
    exact ⟨funnel_spacing_lower_pos hp hk hr1 hr2,
      funnel_spacing_upper_pos hp hk hr1 hr2⟩

/-- Positive funnel parents are genuinely nonexact and hence have two children. -/
theorem funnel_childRootFinset_pos {p r k : ℕ}
    (hp : 2 ≤ p) (hk : 0 < k) (hr1 : 1 < r) (hr2 : r < 2 ^ p) :
    childRootFinset p r k = {rootIndex p r k, rootIndex p r k + 1} := by
  have hna := subthreshold_not_aligned hp hr1 hr2
  have hne := positive_nonaligned_root_not_exact hp hk hna
  simp [childRootFinset, hne]

/-- Positive funnel upper endpoint is exactly `m_k+1`. -/
theorem funnel_childUpper_pos {p r k : ℕ}
    (hp : 2 ≤ p) (hk : 0 < k) (hr1 : 1 < r) (hr2 : r < 2 ^ p) :
    childUpper p r k = rootIndex p r k + 1 := by
  have hna := subthreshold_not_aligned hp hr1 hr2
  have hne := positive_nonaligned_root_not_exact hp hk hna
  simp [childUpper, hne]

/-- Funnel children of the next parent start at most one after the previous upper endpoint. -/
theorem funnel_next_root_le_childUpper_succ {p r k : ℕ}
    (hp : 2 ≤ p) (hr1 : 1 < r) (hr2 : r < 2 ^ p) :
    rootIndex p r (k + 1) ≤ childUpper p r k + 1 := by
  by_cases hk0 : k = 0
  · subst k
    have hp0 : p ≠ 0 := by omega
    have h0 := rootIndex_zero (p := p) (r := r) hp0
    have h1 := rootIndex_one_of_subthreshold hp hr1 hr2
    simp [childUpper, h0, refinedPowerInput, hp0, h1]
  · have hk : 0 < k := Nat.pos_of_ne_zero hk0
    rw [funnel_childUpper_pos hp hk hr1 hr2]
    exact (funnel_spacing (p := p) (r := r) (k := k) hp hr1 hr2).2

/-- Funnel upper endpoints are monotone from one parent to the next. -/
theorem funnel_childUpper_le_next {p r k : ℕ}
    (hp : 2 ≤ p) (hr1 : 1 < r) (hr2 : r < 2 ^ p) :
    childUpper p r k ≤ childUpper p r (k + 1) := by
  by_cases hk0 : k = 0
  · subst k
    have hp0 : p ≠ 0 := by omega
    have h0 := rootIndex_zero (p := p) (r := r) hp0
    have h1 := rootIndex_one_of_subthreshold hp hr1 hr2
    have hpos1 : 0 < (1 : ℕ) := by decide
    rw [funnel_childUpper_pos hp hpos1 hr1 hr2]
    simp [childUpper, h0, refinedPowerInput, hp0, h1]
  · have hk : 0 < k := Nat.pos_of_ne_zero hk0
    have hk1 : 0 < k + 1 := Nat.succ_pos k
    rw [funnel_childUpper_pos hp hk hr1 hr2,
      funnel_childUpper_pos hp hk1 hr1 hr2]
    have h := (funnel_spacing (p := p) (r := r) (k := k) hp hr1 hr2).1
    omega

/-- L06: one exact BRC step maps a root-index interval to an exact no-hole interval. -/
theorem funnel_interval_finset {p r A B : ℕ}
    (hp : 2 ≤ p) (hr1 : 1 < r) (hr2 : r < 2 ^ p) (hAB : A ≤ B) :
    childRootFinsetOf p r (Finset.Icc A B) =
      Finset.Icc (rootIndex p r A) (childUpper p r B) := by
  classical
  induction B generalizing A with
  | zero =>
      have hA : A = 0 := by omega
      subst A
      simp [childRootFinsetOf, childRootFinset_eq_Icc]
  | succ B ih =>
      by_cases hA_B : A ≤ B
      · have hsplit : Finset.Icc A (B + 1) =
            insert (B + 1) (Finset.Icc A B) := by
          ext x
          simp
          omega
        rw [hsplit]
        simp only [childRootFinsetOf, Finset.biUnion_insert]
        have hih := ih hA_B
        unfold childRootFinsetOf at hih
        rw [hih, childRootFinset_eq_Icc]
        have hLM : rootIndex p r A ≤ rootIndex p r (B + 1) := by
          apply rootIndex_monotone (p := p) (r := r) (by omega)
          omega
        have hUV : childUpper p r B ≤ childUpper p r (B + 1) :=
          funnel_childUpper_le_next hp hr1 hr2
        have htouch : rootIndex p r (B + 1) ≤ childUpper p r B + 1 :=
          funnel_next_root_le_childUpper_succ hp hr1 hr2
        apply Finset.ext
        intro x
        simp only [Finset.mem_union, Finset.mem_Icc]
        omega
      · have hEq : A = B + 1 := by omega
        subst A
        simp [childRootFinsetOf, childRootFinset_eq_Icc]

/-- One BRC step from any finite root support has at most twice as many roots. -/
theorem childRootFinsetOf_card_le_two_mul (p r : ℕ) (S : Finset ℕ) :
    (childRootFinsetOf p r S).card ≤ 2 * S.card := by
  classical
  induction S using Finset.induction_on with
  | empty => simp [childRootFinsetOf]
  | @insert a S ha ih =>
      rw [childRootFinsetOf, Finset.biUnion_insert]
      calc
        (childRootFinset p r a ∪ S.biUnion (childRootFinset p r)).card ≤
            (childRootFinset p r a).card + (S.biUnion (childRootFinset p r)).card :=
          Finset.card_union_le _ _
        _ ≤ 2 + 2 * S.card := Nat.add_le_add (childRootFinset_card_le_two p r a) ih
        _ = 2 * (insert a S).card := by simp [ha]; omega

/-- L07 one-step quantitative funnel statement: interval support cannot exceed binary size. -/
theorem funnel_interval_card_le_two_mul {p r A B : ℕ}
    (_hp : 2 ≤ p) (_hr1 : 1 < r) (_hr2 : r < 2 ^ p) (_hAB : A ≤ B) :
    (childRootFinsetOf p r (Finset.Icc A B)).card ≤
      2 * (Finset.Icc A B).card :=
  childRootFinsetOf_card_le_two_mul p r (Finset.Icc A B)

/-- L07: repeated funnel evolution preserves exact interval representation. -/
theorem repeated_funnel_interval {p r A B : ℕ}
    (hp : 2 ≤ p) (hr1 : 1 < r) (hr2 : r < 2 ^ p) (hAB : A ≤ B) :
    ∀ t : ℕ, ∃ A' B' : ℕ,
      A' ≤ B' ∧ iterateRootFinset p r t (Finset.Icc A B) = Finset.Icc A' B' := by
  intro t
  induction t with
  | zero =>
      exact ⟨A, B, hAB, rfl⟩
  | succ t ih =>
      rcases ih with ⟨A', B', hA'B', hiter⟩
      refine ⟨rootIndex p r A', childUpper p r B', ?_, ?_⟩
      · exact (rootIndex_monotone (p := p) (r := r) (by omega) hA'B').trans
          (rootIndex_le_childUpper p r B')
      · simp only [iterateRootFinset]
        rw [hiter, funnel_interval_finset hp hr1 hr2 hA'B']

/-- L08 super-threshold spacing: consecutive positive parents are separated by at least two roots. -/
theorem superthreshold_spacing {p r k : ℕ}
    (hp : 2 ≤ p) (hk : 0 < k) (hr : 2 ^ p < r) :
    rootIndex p r k + 2 ≤ rootIndex p r (k + 1) := by
  have hp0 : p ≠ 0 := by omega
  let m := rootIndex p r k
  have h2k : 2 * k ≤ m := by
    simpa [m] using superthreshold_root_lower hp hr
  have hbasin : m ^ p ≤ refinedPowerInput p r k := by
    simpa [m] using (rootIndex_basin (p := p) (r := r) (k := k) hp0).1
  have hcross : (m + 2) * k ≤ m * (k + 1) := by
    calc
      (m + 2) * k = m * k + 2 * k := by ring
      _ ≤ m * k + m := Nat.add_le_add_left h2k (m * k)
      _ = m * (k + 1) := by ring
  have hcrossp : (m + 2) ^ p * k ^ p ≤ m ^ p * (k + 1) ^ p := by
    simpa [mul_pow] using Nat.pow_le_pow_left hcross p
  have hfull : (m + 2) ^ p * k ^ p ≤
      (r * (k + 1) ^ p) * k ^ p := by
    calc
      (m + 2) ^ p * k ^ p ≤ m ^ p * (k + 1) ^ p := hcrossp
      _ ≤ (r * k ^ p) * (k + 1) ^ p :=
        Nat.mul_le_mul_right ((k + 1) ^ p) hbasin
      _ = (r * (k + 1) ^ p) * k ^ p := by ring
  have hkpow : 0 < k ^ p := pow_pos hk p
  have htarget : (m + 2) ^ p ≤ r * (k + 1) ^ p :=
    Nat.le_of_mul_le_mul_right hfull hkpow
  have hroot : m + 2 ≤ rootIndex p r (k + 1) := by
    exact (Nat.le_nthRoot_iff hp0).2 (by simpa [refinedPowerInput] using htarget)
  simpa [m] using hroot

/-- Positive binary-regime parents have exactly their two adjacent root children. -/
theorem binary_childRootFinset_pos {p r k : ℕ}
    (hp : 2 ≤ p) (hk : 0 < k) (hnonaligned : ¬ Aligned p r) :
    childRootFinset p r k = {rootIndex p r k, rootIndex p r k + 1} := by
  have hne := positive_nonaligned_root_not_exact hp hk hnonaligned
  simp [childRootFinset, hne]

/-- L09: ordered distinct positive parents have disjoint binary child pairs. -/
theorem binary_child_disjoint_of_lt {p r k l : ℕ}
    (hp : 2 ≤ p) (hk : 0 < k) (hl : 0 < l)
    (hr : 2 ^ p < r) (hnonaligned : ¬ Aligned p r) (hkl : k < l) :
    Disjoint (childRootFinset p r k) (childRootFinset p r l) := by
  have hsep0 := superthreshold_spacing hp hk hr
  have hnextle : rootIndex p r (k + 1) ≤ rootIndex p r l := by
    apply rootIndex_monotone (p := p) (r := r) (by omega)
    omega
  have hsep : rootIndex p r k + 2 ≤ rootIndex p r l := hsep0.trans hnextle
  rw [binary_childRootFinset_pos hp hk hnonaligned,
    binary_childRootFinset_pos hp hl hnonaligned]
  rw [Finset.disjoint_left]
  intro j hjk hjl
  simp at hjk hjl
  omega

/-- Each positive nonaligned parent contributes exactly two roots. -/
theorem binary_childRootFinset_card_two {p r k : ℕ}
    (hp : 2 ≤ p) (hk : 0 < k) (hnonaligned : ¬ Aligned p r) :
    (childRootFinset p r k).card = 2 := by
  rw [binary_childRootFinset_pos hp hk hnonaligned]
  simp

/-- L10: arbitrary finite positive support doubles exactly in the binary regime. -/
theorem binary_childRootFinsetOf_card {p r : ℕ} (S : Finset ℕ)
    (hp : 2 ≤ p) (hr : 2 ^ p < r) (hnonaligned : ¬ Aligned p r)
    (hpositive : ∀ k ∈ S, 0 < k) :
    (childRootFinsetOf p r S).card = 2 * S.card := by
  classical
  unfold childRootFinsetOf
  rw [Finset.card_biUnion]
  · calc
      (∑ k ∈ S, (childRootFinset p r k).card) = ∑ _k ∈ S, 2 := by
        apply Finset.sum_congr rfl
        intro k hk
        exact binary_childRootFinset_card_two hp (hpositive k hk) hnonaligned
      _ = 2 * S.card := by simp [Nat.mul_comm]
  · intro k hk l hl hne
    rcases lt_or_gt_of_ne hne with hkl | hlk
    · exact binary_child_disjoint_of_lt hp (hpositive k hk) (hpositive l hl)
        hr hnonaligned hkl
    · exact (binary_child_disjoint_of_lt hp (hpositive l hl) (hpositive k hk)
        hr hnonaligned hlk).symm

/-- Super-threshold evolution preserves positivity of finite support. -/
theorem superthreshold_child_positive {p r : ℕ} (S : Finset ℕ)
    (hp : 2 ≤ p) (hr : 2 ^ p < r)
    (hpositive : ∀ k ∈ S, 0 < k) :
    ∀ j ∈ childRootFinsetOf p r S, 0 < j := by
  intro j hj
  rcases Finset.mem_biUnion.mp hj with ⟨k, hkS, hjk⟩
  have hk := hpositive k hkS
  have hm := superthreshold_root_lower (k := k) hp hr
  rcases mem_childRootFinset_cases hjk with hj | hj <;> omega

/-- Positivity remains invariant under repeated super-threshold evolution. -/
theorem superthreshold_iterate_positive {p r : ℕ} (S : Finset ℕ)
    (hp : 2 ≤ p) (hr : 2 ^ p < r)
    (hpositive : ∀ k ∈ S, 0 < k) :
    ∀ t j, j ∈ iterateRootFinset p r t S → 0 < j := by
  intro t
  induction t with
  | zero =>
      intro j hj
      exact hpositive j hj
  | succ t ih =>
      intro j hj
      exact superthreshold_child_positive (iterateRootFinset p r t S) hp hr
        (fun k hk => ih k hk) j hj

/-- L10 repeated law: exact binary cardinality grows as `2^t` on positive support. -/
theorem binary_iterate_card {p r : ℕ} (S : Finset ℕ)
    (hp : 2 ≤ p) (hr : 2 ^ p < r) (hnonaligned : ¬ Aligned p r)
    (hpositive : ∀ k ∈ S, 0 < k) :
    ∀ t : ℕ, (iterateRootFinset p r t S).card = 2 ^ t * S.card := by
  intro t
  induction t with
  | zero => simp [iterateRootFinset]
  | succ t ih =>
      simp only [iterateRootFinset]
      rw [binary_childRootFinsetOf_card (iterateRootFinset p r t S) hp hr hnonaligned
        (fun k hk => superthreshold_iterate_positive S hp hr hpositive t k hk)]
      rw [ih, pow_succ]
      ring

/-- Explicit zero-boundary mutation: singleton zero support never doubles. -/
theorem zero_support_not_doubling {p r : ℕ} (hp : p ≠ 0) :
    (childRootFinsetOf p r {0}).card ≠ 2 * ({0} : Finset ℕ).card := by
  simp [childRootFinsetOf, childRootFinset_zero hp]

/-- L11: the three predicates are mutually exclusive. -/
theorem regimes_mutually_exclusive {p r : ℕ} :
    (Aligned p r → ¬ Funnel p r) ∧
      (Aligned p r → ¬ Binary p r) ∧
      (Funnel p r → ¬ Binary p r) := by
  constructor
  · intro ha hf
    exact hf.1 ha
  constructor
  · intro ha hb
    exact hb.1 ha
  · intro hf hb
    exact (Nat.lt_asymm hf.2 hb.2)

/-- L11: for `p>=2, r>=1`, ALIGNED/FUNNEL/BINARY are exhaustive. -/
theorem regimes_exhaustive {p r : ℕ} (_hp : 2 ≤ p) (_hr : 1 ≤ r) :
    Aligned p r ∨ Funnel p r ∨ Binary p r := by
  by_cases ha : Aligned p r
  · exact Or.inl ha
  · by_cases hlt : r < 2 ^ p
    · exact Or.inr (Or.inl ⟨ha, hlt⟩)
    · have hle : 2 ^ p ≤ r := Nat.le_of_not_gt hlt
      have hne : r ≠ 2 ^ p := by
        intro heq
        apply ha
        exact ⟨2, heq⟩
      have hgt : 2 ^ p < r := lt_of_le_of_ne hle (Ne.symm hne)
      exact Or.inr (Or.inr ⟨ha, hgt⟩)

/-- A classifier-level funnel hypothesis implies the strict lower threshold `1<r`. -/
theorem funnel_one_lt {p r : ℕ} (_hp : 2 ≤ p) (hr : 1 ≤ r) (hf : Funnel p r) :
    1 < r := by
  have hrne : r ≠ 1 := by
    intro heq
    apply hf.1
    refine ⟨1, ?_⟩
    simp [heq]
  omega

/-- L12: positive powering preserves finite root-support cardinality exactly. -/
theorem powerSupport_card {p : ℕ} (hp : p ≠ 0) (S : Finset ℕ) :
    (powerSupport p S).card = S.card := by
  unfold powerSupport
  exact Finset.card_image_of_injective S (Nat.pow_left_injective hp)

/-- L12 aligned bridge to actual p-th-power endpoint support. -/
theorem aligned_actual_child_support {p : ℕ} (hp : p ≠ 0) (a k : ℕ) :
    powerSupport p (childRootFinset p (a ^ p) k) = {(a * k) ^ p} := by
  rw [childRootFinset_aligned hp]
  simp [powerSupport]

/-- L12 funnel bridge: actual support is exactly the power image of the no-hole root interval. -/
theorem funnel_actual_interval_support {p r A B : ℕ}
    (hp : 2 ≤ p) (hr1 : 1 < r) (hr2 : r < 2 ^ p) (hAB : A ≤ B) :
    powerSupport p (childRootFinsetOf p r (Finset.Icc A B)) =
      powerSupport p (Finset.Icc (rootIndex p r A) (childUpper p r B)) := by
  rw [funnel_interval_finset hp hr1 hr2 hAB]

/-- L12 binary bridge: actual p-th-power support has the same exact doubled cardinality. -/
theorem binary_actual_support_card {p r : ℕ} (S : Finset ℕ)
    (hp : 2 ≤ p) (hr : 2 ^ p < r) (hnonaligned : ¬ Aligned p r)
    (hpositive : ∀ k ∈ S, 0 < k) :
    (powerSupport p (childRootFinsetOf p r S)).card = 2 * S.card := by
  rw [powerSupport_card (by omega), binary_childRootFinsetOf_card S hp hr hnonaligned hpositive]

/-- L12 repeated bridge: actual p-th-power support grows exactly as `2^t` in binary regime. -/
theorem binary_actual_iterate_card {p r : ℕ} (S : Finset ℕ)
    (hp : 2 ≤ p) (hr : 2 ^ p < r) (hnonaligned : ¬ Aligned p r)
    (hpositive : ∀ k ∈ S, 0 < k) :
    ∀ t : ℕ,
      (powerSupport p (iterateRootFinset p r t S)).card = 2 ^ t * S.card := by
  intro t
  rw [powerSupport_card (by omega), binary_iterate_card S hp hr hnonaligned hpositive t]

/-- L13 narrow connection: canonical BRC relational direct image equals the exact finite root support union. -/
theorem brc_rootSupport_relImage_bridge (p r : ℕ) (S : Finset ℕ) :
    EnterpriseMath.BranchRecoalescence.relImage (rootChildRel p r) (↑S : Set ℕ) =
      (↑(childRootFinsetOf p r S) : Set ℕ) := by
  ext j
  simp [EnterpriseMath.BranchRecoalescence.relImage, rootChildRel, childRootFinsetOf]

/-- L13 actual-state specialization of canonical Boolean BRC direct-image support. -/
theorem brc_powerEndpoint_relImage_bridge {p r : ℕ} (hp : p ≠ 0) (S : Finset ℕ) :
    EnterpriseMath.BranchRecoalescence.relImage (powerEndpointRel p r)
        (↑(powerSupport p S) : Set ℕ) =
      (↑(powerSupport p (childRootFinsetOf p r S)) : Set ℕ) := by
  ext y
  constructor
  · rintro ⟨x, hx, k, j, hxk, hj, rfl⟩
    rcases Finset.mem_image.mp hx with ⟨s, hs, hsx⟩
    have hsk : s = k := Nat.pow_left_injective hp (hsx.trans hxk)
    subst s
    apply Finset.mem_image.mpr
    refine ⟨j, ?_, rfl⟩
    apply Finset.mem_biUnion.mpr
    exact ⟨k, hs, hj⟩
  · intro hy
    rcases Finset.mem_image.mp hy with ⟨j, hj, rfl⟩
    rcases Finset.mem_biUnion.mp hj with ⟨k, hk, hjk⟩
    refine ⟨k ^ p, ?_, ?_⟩
    · apply Finset.mem_image.mpr
      exact ⟨k, hk, rfl⟩
    · exact ⟨k, j, rfl, hjk, rfl⟩

/-- Mutation witness: a funnel layer can have no duplicate collision at all. -/
theorem funnel_no_duplicate_witness :
    childRootFinsetOf 2 3 (Finset.Icc 1 2) = Finset.Icc 1 4 := by
  native_decide

/-- The witness has exact binary-sized cardinality for that one funnel layer. -/
theorem funnel_no_duplicate_witness_card :
    (childRootFinsetOf 2 3 (Finset.Icc 1 2)).card =
      2 * (Finset.Icc 1 2).card := by
  native_decide

#print axioms positive_nonaligned_input_not_power
#print axioms funnel_interval_finset
#print axioms binary_childRootFinsetOf_card
#print axioms binary_iterate_card
#print axioms regimes_exhaustive
#print axioms brc_powerEndpoint_relImage_bridge

end EnterpriseMath.PowerBRCTrichotomy
