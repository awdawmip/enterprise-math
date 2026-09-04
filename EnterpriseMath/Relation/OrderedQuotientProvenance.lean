import EnterpriseMath.Relation.BranchRecoalescence
import EnterpriseMath.Relation.PrimePowerQuotientTriangle
import Mathlib.Tactic

namespace EnterpriseMath.OrderedQuotientProvenance

open EnterpriseMath.BranchRecoalescence
open EnterpriseMath.PrimePowerQuotientTriangle

/-- A two-step quotient history with its starting state and ordered action labels. -/
structure OrderedHistory where
  start : ℕ
  first : ℕ
  second : ℕ
  deriving DecidableEq

/-- State reached after the first ordered quotient action. -/
def intermediate (h : OrderedHistory) : ℕ :=
  quotient h.first h.start

/-- Common recoalesced endpoint after both quotient actions. -/
def endpoint (h : OrderedHistory) : ℕ :=
  quotient (h.first * h.second) h.start

/-- Minimal ordered runtime key needed by transported endpoint readouts. -/
def transportKey (h : OrderedHistory) : ℕ × ℕ :=
  oneStepKey intermediate endpoint h

/-- Forgetful key retaining only the start and recoalesced product label. -/
def productKey (h : OrderedHistory) : ℕ × ℕ :=
  (h.start, h.first * h.second)

/-- A direct endpoint is recoverable from the start and product label alone. -/
theorem productKey_recovers_endpoint :
    Recovers productKey endpoint := by
  refine ⟨fun key => quotient key.2 key.1, ?_⟩
  intro h
  rfl

/-- The transport key is sufficient and coarsest for recovering both intermediate and endpoint. -/
theorem transportKey_coarsest :
    OneStepSufficient transportKey intermediate endpoint ∧
      ∀ (C : Type*) (classifier : OrderedHistory → C),
        OneStepSufficient classifier intermediate endpoint →
          Recovers classifier transportKey := by
  simpa [transportKey] using oneStepCoarsest intermediate endpoint

/-- Every additive transported readout factors through the ordered transport key. -/
def transportedReadout {R : Type*} [Add R]
    (f : ℕ → R) (h : OrderedHistory) : R :=
  f (intermediate h) + f (endpoint h)

theorem transportKey_recovers_transportedReadout
    {R : Type*} [Add R] (f : ℕ → R) :
    Recovers transportKey (transportedReadout f) := by
  refine ⟨fun key => f key.1 + f key.2, ?_⟩
  intro h
  rfl

/-- The ordered history `2` then `9` from state `100`. -/
def historyTwoNine : OrderedHistory where
  start := 100
  first := 2
  second := 9

/-- The ordered history `9` then `2` from state `100`. -/
def historyNineTwo : OrderedHistory where
  start := 100
  first := 9
  second := 2

/-- The product-label key identifies the two ordered histories. -/
theorem productKey_twoNine_eq_nineTwo :
    productKey historyTwoNine = productKey historyNineTwo := by
  norm_num [productKey, historyTwoNine, historyNineTwo]

/-- Their intermediate-plus-endpoint transport keys are different. -/
theorem transportKey_twoNine_ne_nineTwo :
    transportKey historyTwoNine ≠ transportKey historyNineTwo := by
  norm_num [transportKey, oneStepKey, intermediate, endpoint, quotient,
    historyTwoNine, historyNineTwo]

/-- Product-label recoalescence cannot recover the ordered transport key. -/
theorem productKey_not_recovers_transportKey :
    ¬ Recovers productKey transportKey := by
  intro h
  have hsame : transportKey historyTwoNine = transportKey historyNineTwo :=
    noResurrection h productKey_twoNine_eq_nineTwo
  exact transportKey_twoNine_ne_nineTwo hsame

/-- A concrete observable distinguishing the two intermediate vertices. -/
def witnessObservable (n : ℕ) : ℕ :=
  if n = 50 then 1 else 0

/-- The transported observable distinguishes histories with the same product label. -/
theorem transportedReadout_twoNine_ne_nineTwo :
    transportedReadout witnessObservable historyTwoNine ≠
      transportedReadout witnessObservable historyNineTwo := by
  norm_num [transportedReadout, witnessObservable, intermediate, endpoint, quotient,
    historyTwoNine, historyNineTwo]

/-- Product-label recoalescence cannot recover even this concrete transported readout. -/
theorem productKey_not_recovers_witnessReadout :
    ¬ Recovers productKey (transportedReadout witnessObservable) := by
  intro h
  have hsame :
      transportedReadout witnessObservable historyTwoNine =
        transportedReadout witnessObservable historyNineTwo :=
    noResurrection h productKey_twoNine_eq_nineTwo
  exact transportedReadout_twoNine_ne_nineTwo hsame

end EnterpriseMath.OrderedQuotientProvenance
