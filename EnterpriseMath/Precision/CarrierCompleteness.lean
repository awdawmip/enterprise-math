import Mathlib
import EnterpriseMath.Arithmetic.IntegerRoot
import EnterpriseMath.Precision.BranchDeferral

namespace EnterpriseMath.CarrierCompleteness

open Set
open EnterpriseMath.IntegerRoot
open EnterpriseMath.BranchDeferral

universe u v w z t

variable {X : Type u} {A : Type v} {B : Type w} {Q : Type z} {C : Type t}

/-! ## R018-L01: joint observation and its kernel -/

/-- The joint observation retaining both endpoint observations. -/
def jointObservation (f : X → A) (g : X → B) (x : X) : A × B :=
  (f x, g x)

/-- R018-L01: equality of joint observations is exactly intersection of the two kernels. -/
theorem jointObservation_eq_iff (f : X → A) (g : X → B) (x y : X) :
    jointObservation f g x = jointObservation f g y ↔
      f x = f y ∧ g x = g y := by
  simp [jointObservation]

/-- R018-L01: any observation through which both components factor also carries
an explicit factorization of the joint observation. Thus the joint observation
is the coarsest observation retaining both components. -/
theorem jointObservation_coarsest_factorization
    (f : X → A) (g : X → B) (h : X → C) (f' : C → A) (g' : C → B)
    (hf : ∀ x, f x = f' (h x)) (hg : ∀ x, g x = g' (h x)) :
    ∃ k : C → A × B, ∀ x, jointObservation f g x = k (h x) := by
  refine ⟨fun c => (f' c, g' c), ?_⟩
  intro x
  simp [jointObservation, hf x, hg x]

/-! ## R018-L02: p-th-power lower/upper bracket -/

/-- Lower p-th-power anchor. -/
def lowerAnchor (p n : ℕ) : ℕ :=
  collapse p n

/-- Upper p-th-power anchor. Exact powers keep the same lower/upper anchor;
non-powers use the next p-th power above the integer root. -/
def upperAnchor (p n : ℕ) : ℕ :=
  if lowerAnchor p n = n then n else (root p n + 1) ^ p

/-- Ordered lower/upper p-th-power bracket. This is a cell label, not a literal
set of endpoint alternatives. -/
def powerBracket (p n : ℕ) : ℕ × ℕ :=
  (lowerAnchor p n, upperAnchor p n)

/-- R018-L02.1: the lower anchor is below the fine state. -/
theorem lowerAnchor_le {p : ℕ} (hp : 2 ≤ p) (n : ℕ) :
    lowerAnchor p n ≤ n := by
  exact collapse_le (by omega) n

/-- R018-L02.1: the fine state is below the upper anchor. -/
theorem le_upperAnchor {p : ℕ} (hp : 2 ≤ p) (n : ℕ) :
    n ≤ upperAnchor p n := by
  have hp0 : p ≠ 0 := by omega
  by_cases hfix : lowerAnchor p n = n
  · simp [upperAnchor, hfix]
  · simp [upperAnchor, hfix]
    exact Nat.le_of_lt (Nat.lt_pow_nthRoot_add_one hp0 n)

/-- R018-L02.2: lower and upper anchors coincide exactly at perfect p-th powers. -/
theorem lowerAnchor_eq_upperAnchor_iff {p : ℕ} (hp : 2 ≤ p) (n : ℕ) :
    lowerAnchor p n = upperAnchor p n ↔ ∃ k : ℕ, k ^ p = n := by
  have hp0 : p ≠ 0 := by omega
  constructor
  · intro hEq
    have hLower : lowerAnchor p n ≤ n := lowerAnchor_le hp n
    have hUpper : n ≤ upperAnchor p n := le_upperAnchor hp n
    have hUpper' : n ≤ lowerAnchor p n := by
      rw [hEq]
      exact hUpper
    have hFix : lowerAnchor p n = n := Nat.le_antisymm hLower hUpper'
    exact (collapse_eq_self_iff hp0 n).1 (by simpa [lowerAnchor] using hFix)
  · rintro ⟨k, rfl⟩
    have hFix : lowerAnchor p (k ^ p) = k ^ p := by
      exact (by
        simpa [lowerAnchor] using
          (collapse_eq_self_iff hp0 (k ^ p)).2 ⟨k, rfl⟩)
    simp [upperAnchor, hFix]

/-- R018-L02.3: every interior point in one open gap has the same ordered bracket. -/
theorem powerBracket_eq_of_mem_openGap {p k n : ℕ} (hp : 2 ≤ p)
    (hLower : k ^ p < n) (hUpper : n < (k + 1) ^ p) :
    powerBracket p n = (k ^ p, (k + 1) ^ p) := by
  have hp0 : p ≠ 0 := by omega
  have hRoot : root p n = k :=
    (root_eq_iff hp0).2 ⟨Nat.le_of_lt hLower, hUpper⟩
  have hL : lowerAnchor p n = k ^ p := by
    simp [lowerAnchor, collapse, hRoot]
  have hNotFix : lowerAnchor p n ≠ n := by
    intro hFix
    rw [hL] at hFix
    omega
  have hU : upperAnchor p n = (k + 1) ^ p := by
    simp [upperAnchor, hNotFix, hRoot]
  change (lowerAnchor p n, upperAnchor p n) = (k ^ p, (k + 1) ^ p)
  rw [hL, hU]

/-- The bracket of an exact p-th power is the repeated exact endpoint. -/
theorem powerBracket_at_power {p : ℕ} (hp : 2 ≤ p) (k : ℕ) :
    powerBracket p (k ^ p) = (k ^ p, k ^ p) := by
  have hp0 : p ≠ 0 := by omega
  have hFix : lowerAnchor p (k ^ p) = k ^ p := by
    simpa [lowerAnchor] using
      (collapse_eq_self_iff hp0 (k ^ p)).2 ⟨k, rfl⟩
  simp [powerBracket, upperAnchor, hFix]

/-- R018-L02.4: every exact p-th power has a singleton bracket fibre. -/
theorem powerBracket_power_fibre_singleton {p : ℕ} (hp : 2 ≤ p) (k : ℕ) :
    {n : ℕ | powerBracket p n = powerBracket p (k ^ p)} =
      ({k ^ p} : Set ℕ) := by
  ext n
  constructor
  · intro hn
    have hPair : powerBracket p n = (k ^ p, k ^ p) :=
      hn.trans (powerBracket_at_power hp k)
    have hL : lowerAnchor p n = k ^ p := congrArg Prod.fst hPair
    have hU : upperAnchor p n = k ^ p := congrArg Prod.snd hPair
    have hLower := lowerAnchor_le hp n
    have hUpper := le_upperAnchor hp n
    rw [hL] at hLower
    rw [hU] at hUpper
    have hnk : n = k ^ p := by omega
    simp [hnk]
  · intro hn
    have hnk : n = k ^ p := by simpa using hn
    subst n
    rfl

/-- R018-L02.4: the fibre carrying the non-exact bracket `(k^p,(k+1)^p)` is
exactly the open gap between those consecutive powers. -/
theorem powerBracket_openGap_fibre {p k : ℕ} (hp : 2 ≤ p) :
    {n : ℕ | powerBracket p n = (k ^ p, (k + 1) ^ p)} =
      Set.Ioo (k ^ p) ((k + 1) ^ p) := by
  have hp0 : p ≠ 0 := by omega
  ext n
  constructor
  · intro hn
    have hL : lowerAnchor p n = k ^ p := congrArg Prod.fst hn
    have hCollapse : collapse p n = k ^ p := by simpa [lowerAnchor] using hL
    have hInterval := (collapse_eq_pow_iff hp0).1 hCollapse
    refine ⟨?_, hInterval.2⟩
    have hNe : n ≠ k ^ p := by
      intro hnk
      subst n
      have hPairs : (k ^ p, k ^ p) = (k ^ p, (k + 1) ^ p) :=
        (powerBracket_at_power hp k).symm.trans hn
      have hPow : k ^ p = (k + 1) ^ p := congrArg Prod.snd hPairs
      have hk : k = k + 1 := Nat.pow_left_injective hp0 hPow
      omega
    omega
  · rintro ⟨hLower, hUpper⟩
    exact powerBracket_eq_of_mem_openGap hp hLower hUpper

/-- Consecutive p-th powers with `p ≥ 2` and positive lower root leave room for
at least two distinct interior natural states. -/
theorem two_points_in_power_gap {p k : ℕ} (hp : 2 ≤ p) (hk : 1 ≤ k) :
    k ^ p + 2 < (k + 1) ^ p := by
  obtain ⟨r, rfl⟩ := Nat.exists_eq_add_of_le hp
  clear hp
  induction r with
  | zero =>
      simp [pow_two]
      nlinarith
  | succ r ih =>
      have hk0 : 0 < k := by omega
      calc
        k ^ (2 + (r + 1)) + 2
            = k ^ (2 + r) * k + 2 := by
                rw [show 2 + (r + 1) = (2 + r) + 1 by omega, pow_succ]
        _ ≤ k ^ (2 + r) * k + 2 * k := by omega
        _ = (k ^ (2 + r) + 2) * k := by ring
        _ < (k + 1) ^ (2 + r) * k := by
              exact Nat.mul_lt_mul_of_pos_right ih hk0
        _ < (k + 1) ^ (2 + r) * (k + 1) := by
              exact Nat.mul_lt_mul_of_pos_left
                (Nat.lt_succ_self k) (by positivity)
        _ = (k + 1) ^ (2 + (r + 1)) := by
              rw [show 2 + (r + 1) = (2 + r) + 1 by omega, pow_succ]

/-- R018-L02.4 nontriviality: every positive-root open gap is a non-singleton
bracket fibre; the two displayed fine states share the same cell label. -/
theorem powerBracket_openGap_nontrivial {p k : ℕ} (hp : 2 ≤ p) (hk : 1 ≤ k) :
    ∃ n₁ n₂ : ℕ,
      n₁ ≠ n₂ ∧
      powerBracket p n₁ = (k ^ p, (k + 1) ^ p) ∧
      powerBracket p n₂ = (k ^ p, (k + 1) ^ p) := by
  have hGap : k ^ p + 2 < (k + 1) ^ p := two_points_in_power_gap hp hk
  refine ⟨k ^ p + 1, k ^ p + 2, by omega, ?_, ?_⟩
  · apply powerBracket_eq_of_mem_openGap hp <;> omega
  · apply powerBracket_eq_of_mem_openGap hp <;> omega

/-! ## R018-L03: deferred lower/upper endpoint selection -/

/-- Result-only future support after selecting the first endpoint. -/
def lowerSelectedSupport (R : A → C → Prop) (f : X → A) (x : X) : Set C :=
  RelSupport R {f x}

/-- Result-only future support after selecting the second endpoint. -/
def upperSelectedSupport (R : B → C → Prop) (g : X → B) (x : X) : Set C :=
  RelSupport R {g x}

/-- R018-L03 sufficiency: equality of the joint endpoint observation suffices for
all later result-only relational futures after either deferred endpoint selection.
This theorem makes no claim about arbitrary fine-state operations before selection. -/
theorem jointObservation_sufficient_for_deferred_selection
    (f : X → A) (g : X → B) (Rlower : A → C → Prop) (Rupper : B → C → Prop)
    {x y : X} (hxy : jointObservation f g x = jointObservation f g y) :
    lowerSelectedSupport Rlower f x = lowerSelectedSupport Rlower f y ∧
      upperSelectedSupport Rupper g x = upperSelectedSupport Rupper g y := by
  have h := (jointObservation_eq_iff f g x y).1 hxy
  constructor
  · simp [lowerSelectedSupport, h.1]
  · simp [upperSelectedSupport, h.2]

/-- R018-L03 minimality in the declared deferred-selection interface: any
observation that itself supports deterministic lower and upper selection factors
the joint endpoint observation. No fine-state dynamics are assumed. -/
theorem jointObservation_minimal_for_deferred_selection
    (f : X → A) (g : X → B) (h : X → C)
    (selectLower : C → A) (selectUpper : C → B)
    (hLower : ∀ x, f x = selectLower (h x))
    (hUpper : ∀ x, g x = selectUpper (h x)) :
    ∃ k : C → A × B, ∀ x, jointObservation f g x = k (h x) :=
  jointObservation_coarsest_factorization f g h selectLower selectUpper hLower hUpper

/-! ## R018-L04: quotient saturation -/

/-- Saturation of a fine support by the fibres of `q`. -/
def Sat (q : X → Q) (S : Set X) : Set X :=
  {x | ∃ y ∈ S, q x = q y}

/-- R018-L04: saturation is extensive. -/
theorem subset_sat (q : X → Q) (S : Set X) : S ⊆ Sat q S := by
  intro x hx
  exact ⟨x, hx, rfl⟩

/-- R018-L04: saturation is monotone. -/
theorem sat_mono (q : X → Q) : Monotone (Sat q) := by
  intro S T hST x hx
  rcases hx with ⟨y, hy, hxy⟩
  exact ⟨y, hST hy, hxy⟩

/-- R018-L04: saturation is idempotent. -/
theorem sat_idempotent (q : X → Q) (S : Set X) :
    Sat q (Sat q S) = Sat q S := by
  ext x
  constructor
  · rintro ⟨y, ⟨z, hz, hyz⟩, hxy⟩
    exact ⟨z, hz, hxy.trans hyz⟩
  · intro hx
    exact subset_sat q (Sat q S) hx

/-- Saturation preserves the quotient image. -/
theorem image_sat (q : X → Q) (S : Set X) :
    q '' Sat q S = q '' S := by
  ext c
  constructor
  · rintro ⟨x, ⟨y, hy, hxy⟩, rfl⟩
    exact ⟨y, hy, hxy.symm⟩
  · rintro ⟨x, hx, rfl⟩
    exact ⟨x, subset_sat q S hx, rfl⟩

/-- R018-L04: two fine supports have the same quotient image iff their
saturations agree. -/
theorem image_eq_iff_sat_eq (q : X → Q) (S T : Set X) :
    q '' S = q '' T ↔ Sat q S = Sat q T := by
  constructor
  · intro hImage
    ext x
    constructor
    · rintro ⟨y, hy, hxy⟩
      have hyImage : q y ∈ q '' S := ⟨y, hy, rfl⟩
      rw [hImage] at hyImage
      rcases hyImage with ⟨z, hz, hyz⟩
      exact ⟨z, hz, hxy.trans hyz.symm⟩
    · rintro ⟨y, hy, hxy⟩
      have hyImage : q y ∈ q '' T := ⟨y, hy, rfl⟩
      rw [← hImage] at hyImage
      rcases hyImage with ⟨z, hz, hyz⟩
      exact ⟨z, hz, hxy.trans hyz.symm⟩
  · intro hSat
    calc
      q '' S = q '' Sat q S := (image_sat q S).symm
      _ = q '' Sat q T := by rw [hSat]
      _ = q '' T := image_sat q T

/-! ## R018-L05: one-step existential quotient lifting -/

/-- Existential quotient lift of a fine relation. -/
def QuotRel (q : X → Q) (R : X → X → Prop) : Q → Q → Prop :=
  fun a b => ∃ x y, q x = a ∧ q y = b ∧ R x y

/-- R018-L05: one quotient step is exact when the fine input denotes the full
fibre closure of the coarse input. This is deliberately only a one-step theorem. -/
theorem quotientRel_one_step_exact (q : X → Q) (R : X → X → Prop) (S : Set X) :
    q '' RelSupport R (Sat q S) = RelSupport (QuotRel q R) (q '' S) := by
  ext b
  constructor
  · rintro ⟨y, ⟨x, hxSat, hRxy⟩, rfl⟩
    rcases hxSat with ⟨x₀, hx₀, hqx⟩
    refine ⟨q x₀, ⟨x₀, hx₀, rfl⟩, ?_⟩
    exact ⟨x, y, hqx, rfl, hRxy⟩
  · rintro ⟨a, ⟨x₀, hx₀, rfl⟩, ⟨x, y, hqx, hqy, hRxy⟩⟩
    refine ⟨y, ?_, hqy⟩
    refine ⟨x, ?_, hRxy⟩
    exact ⟨x₀, hx₀, hqx⟩

/-! ## R018-L06: strong completeness and fibre successor signatures -/

/-- Coarse successor-support signature of one fine source state. -/
def coarseSuccessorSupport (q : X → Q) (R : X → X → Prop) (x : X) : Set Q :=
  {c | ∃ y, R x y ∧ q y = c}

/-- Fine states in one quotient fibre have the same coarse successor-support signature. -/
def FibreSuccessorConstant (q : X → Q) (R : X → X → Prop) : Prop :=
  ∀ ⦃x y : X⦄, q x = q y → coarseSuccessorSupport q R x = coarseSuccessorSupport q R y

/-- Strong one-generator saturation completeness from R017. -/
def StrongComplete (q : X → Q) (R : X → X → Prop) : Prop :=
  ∀ S : Set X,
    Sat q (RelSupport R (Sat q S)) = Sat q (RelSupport R S)

/-- R018-L06: the strong saturation identity for every support is equivalent to
constancy of coarse successor support on each `q`-fibre. -/
theorem strongComplete_iff_fibreSuccessorConstant
    (q : X → Q) (R : X → X → Prop) :
    StrongComplete q R ↔ FibreSuccessorConstant q R := by
  constructor
  · intro hComplete x y hxy
    ext c
    constructor
    · rintro ⟨z, hxz, hzc⟩
      have hzLeft : z ∈ Sat q (RelSupport R (Sat q ({y} : Set X))) := by
        refine ⟨z, ?_, rfl⟩
        refine ⟨x, ?_, hxz⟩
        exact ⟨y, by simp, hxy⟩
      have hzRight : z ∈ Sat q (RelSupport R ({y} : Set X)) := by
        rw [← hComplete ({y} : Set X)]
        exact hzLeft
      rcases hzRight with ⟨w, ⟨y', hy', hyw⟩, hzw⟩
      have hy'y : y' = y := by simpa using hy'
      subst y'
      exact ⟨w, hyw, hzw.symm.trans hzc⟩
    · rintro ⟨z, hyz, hzc⟩
      have hzLeft : z ∈ Sat q (RelSupport R (Sat q ({x} : Set X))) := by
        refine ⟨z, ?_, rfl⟩
        refine ⟨y, ?_, hyz⟩
        exact ⟨x, by simp, hxy.symm⟩
      have hzRight : z ∈ Sat q (RelSupport R ({x} : Set X)) := by
        rw [← hComplete ({x} : Set X)]
        exact hzLeft
      rcases hzRight with ⟨w, ⟨x', hx', hxw⟩, hzw⟩
      have hx'x : x' = x := by simpa using hx'
      subst x'
      exact ⟨w, hxw, hzw.symm.trans hzc⟩
  · intro hConst S
    ext z
    constructor
    · rintro ⟨y, ⟨x', hx'Sat, hRxy⟩, hzy⟩
      rcases hx'Sat with ⟨x, hxS, hx'x⟩
      have hSig := hConst hx'x
      have hySig : q y ∈ coarseSuccessorSupport q R x' :=
        ⟨y, hRxy, rfl⟩
      rw [hSig] at hySig
      rcases hySig with ⟨w, hRxw, hqwy⟩
      exact ⟨w, ⟨x, hxS, hRxw⟩, hzy.trans hqwy.symm⟩
    · rintro ⟨y, ⟨x, hxS, hRxy⟩, hzy⟩
      exact ⟨y, ⟨x, subset_sat q S hxS, hRxy⟩, hzy⟩

/-! ## R018-L07: finite words and repeated saturation -/

/-- Quotient-style finite-word execution: each generator is fed the current full
fibre closure and its result is re-saturated before the next generator. -/
def RepeatedSatExec (q : X → Q) : List (X → X → Prop) → Set X → Set X
  | [], S => Sat q S
  | R :: Rs, S => RepeatedSatExec q Rs (Sat q (RelSupport R (Sat q S)))

/-- Auxiliary invariant: a finite word of generatorwise-complete relations has
the same final saturated support whether its input is pre-saturated or not. -/
theorem propagateList_sat_input_exact
    (q : X → Q) (Rs : List (X → X → Prop))
    (hComplete : ∀ R ∈ Rs, StrongComplete q R) (S : Set X) :
    Sat q (PropagateList Rs (Sat q S)) = Sat q (PropagateList Rs S) := by
  induction Rs generalizing S with
  | nil =>
      simp [PropagateList, sat_idempotent]
  | cons R Rs ih =>
      have hR : StrongComplete q R := hComplete R (by simp)
      have hRs : ∀ T ∈ Rs, StrongComplete q T := by
        intro T hT
        exact hComplete T (by simp [hT])
      simp only [PropagateList]
      calc
        Sat q (PropagateList Rs (RelSupport R (Sat q S))) =
            Sat q (PropagateList Rs (Sat q (RelSupport R (Sat q S)))) :=
          (ih (hComplete := hRs) (S := RelSupport R (Sat q S))).symm
        _ = Sat q (PropagateList Rs (Sat q (RelSupport R S))) := by
          rw [hR S]
        _ = Sat q (PropagateList Rs (RelSupport R S)) :=
          ih (hComplete := hRs) (S := RelSupport R S)

/-- R018-L07: generatorwise L06 completeness implies arbitrary finite-word
repeated-saturation exactness at the level of final result support. Path
multiplicity and branch identity are intentionally outside the theorem. -/
theorem repeatedSatExec_exact
    (q : X → Q) (Rs : List (X → X → Prop))
    (hComplete : ∀ R ∈ Rs, StrongComplete q R) (S : Set X) :
    RepeatedSatExec q Rs S = Sat q (PropagateList Rs S) := by
  induction Rs generalizing S with
  | nil => rfl
  | cons R Rs ih =>
      have hR : StrongComplete q R := hComplete R (by simp)
      have hRs : ∀ T ∈ Rs, StrongComplete q T := by
        intro T hT
        exact hComplete T (by simp [hT])
      simp only [RepeatedSatExec, PropagateList]
      calc
        RepeatedSatExec q Rs (Sat q (RelSupport R (Sat q S))) =
            Sat q (PropagateList Rs (Sat q (RelSupport R (Sat q S)))) :=
          ih (hComplete := hRs) (S := Sat q (RelSupport R (Sat q S)))
        _ = Sat q (PropagateList Rs (Sat q (RelSupport R S))) := by
          rw [hR S]
        _ = Sat q (PropagateList Rs (RelSupport R S)) :=
          propagateList_sat_input_exact q Rs hRs (RelSupport R S)

/-! ## R018-L08: finite composition counterexample -/

/-- Four fine states: start `0`, merged middle representatives `1,2`, final `3`. -/
def counterQ (x : Fin 4) : Fin 3 :=
  if x = 0 then 0 else if x = 3 then 2 else 1

/-- First fine step reaches only middle representative `1`. -/
def counterR (x y : Fin 4) : Prop :=
  x = 0 ∧ y = 1

/-- Second fine step leaves only from the other merged middle representative `2`. -/
def counterS (x y : Fin 4) : Prop :=
  x = 2 ∧ y = 3

/-- R018-L08: composing the separately lifted quotient relations manufactures a
coarse final transition `0 → 2`. -/
theorem coarse_composition_has_spurious_final :
    RelComp (QuotRel counterQ counterR) (QuotRel counterQ counterS)
      (0 : Fin 3) (2 : Fin 3) := by
  refine ⟨(1 : Fin 3), ?_, ?_⟩
  · refine ⟨(0 : Fin 4), (1 : Fin 4), ?_, ?_, ?_⟩
    · simp [counterQ]
    · simp [counterQ]
    · exact ⟨rfl, rfl⟩
  · refine ⟨(2 : Fin 4), (3 : Fin 4), ?_, ?_, ?_⟩
    · simp [counterQ]
    · simp [counterQ]
    · exact ⟨rfl, rfl⟩

/-- The fine two-step relation has no trajectory from the start fibre to the
final fibre; direct quotient lifting of the composed fine relation therefore
does not contain the spurious coarse result. -/
theorem direct_lift_composed_relation_excludes_spurious_final :
    ¬ QuotRel counterQ (RelComp counterR counterS) (0 : Fin 3) (2 : Fin 3) := by
  rintro ⟨x, z, hqx, hqz, y, hRxy, hSyz⟩
  rcases hRxy with ⟨hx0, hy1⟩
  rcases hSyz with ⟨hy2, hz3⟩
  subst x
  subst z
  exact (by decide : ¬ ((1 : Fin 4) = 2)) (hy1.symm.trans hy2)

/-! ## R018-L09: square 4--9 / +1 sanity boundary -/

/-- R018-L09: 5 and 8 carry the same square bracket `(4,9)`. -/
theorem squareBracket_five_eq_eight :
    powerBracket 2 5 = powerBracket 2 8 := by
  have h5 : powerBracket 2 5 = (4, 9) := by
    apply powerBracket_eq_of_mem_openGap (p := 2) (k := 2) (n := 5) (by decide) <;> norm_num
  have h8 : powerBracket 2 8 = (4, 9) := by
    apply powerBracket_eq_of_mem_openGap (p := 2) (k := 2) (n := 8) (by decide) <;> norm_num
  exact h5.trans h8.symm

/-- R018-L09: after adding one, 6 remains in `(4,9)` while 9 is the exact
square bracket `(9,9)`, so the brackets differ. -/
theorem squareBracket_six_ne_nine :
    powerBracket 2 6 ≠ powerBracket 2 9 := by
  have h6 : powerBracket 2 6 = (4, 9) := by
    apply powerBracket_eq_of_mem_openGap (p := 2) (k := 2) (n := 6) (by decide) <;> norm_num
  have h9 : powerBracket 2 9 = (9, 9) := by
    simpa using powerBracket_at_power (p := 2) (by decide) 3
  rw [h6, h9]
  decide

/-- R018-L09: `n ↦ n+1` does not descend to a deterministic operation on the
square-bracket cell label. -/
theorem addOne_not_deterministic_through_squareBracket :
    ¬ ∃ F : (ℕ × ℕ) → (ℕ × ℕ),
      ∀ n : ℕ, F (powerBracket 2 n) = powerBracket 2 (n + 1) := by
  rintro ⟨F, hF⟩
  have hEq : powerBracket 2 6 = powerBracket 2 9 := by
    calc
      powerBracket 2 6 = F (powerBracket 2 5) := by simpa using (hF 5).symm
      _ = F (powerBracket 2 8) := congrArg F squareBracket_five_eq_eight
      _ = powerBracket 2 9 := by simpa using hF 8
  exact squareBracket_six_ne_nine hEq

#print axioms jointObservation_eq_iff
#print axioms jointObservation_coarsest_factorization
#print axioms lowerAnchor_le
#print axioms le_upperAnchor
#print axioms lowerAnchor_eq_upperAnchor_iff
#print axioms powerBracket_eq_of_mem_openGap
#print axioms powerBracket_power_fibre_singleton
#print axioms powerBracket_openGap_fibre
#print axioms powerBracket_openGap_nontrivial
#print axioms jointObservation_sufficient_for_deferred_selection
#print axioms jointObservation_minimal_for_deferred_selection
#print axioms subset_sat
#print axioms sat_mono
#print axioms sat_idempotent
#print axioms image_eq_iff_sat_eq
#print axioms quotientRel_one_step_exact
#print axioms strongComplete_iff_fibreSuccessorConstant
#print axioms propagateList_sat_input_exact
#print axioms repeatedSatExec_exact
#print axioms coarse_composition_has_spurious_final
#print axioms direct_lift_composed_relation_excludes_spurious_final
#print axioms squareBracket_five_eq_eight
#print axioms squareBracket_six_ne_nine
#print axioms addOne_not_deterministic_through_squareBracket

end EnterpriseMath.CarrierCompleteness