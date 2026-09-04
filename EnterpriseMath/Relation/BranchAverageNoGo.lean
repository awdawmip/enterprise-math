import EnterpriseMath.Relation.BranchRecoalescence
import Mathlib.Data.List.Finset
import Mathlib.Tactic

namespace EnterpriseMath.BranchAverageNoGo

open EnterpriseMath.BranchRecoalescence

/-- Encode a list of point histories as singleton exact branches. -/
def singletonConfig (xs : List Bool) : BranchConfig Bool :=
  xs.map fun x => ({x} : Set Bool)

/-- The exact Boolean support of singleton branches is just the set of listed points. -/
theorem configSupport_singletonConfig (xs : List Bool) :
    configSupport (singletonConfig xs) = (xs.toFinset : Set Bool) := by
  induction xs with
  | nil => simp [singletonConfig, configSupport]
  | cons x xs ih =>
      simp [singletonConfig, configSupport, ih]

/-- A support-only runtime key after exact Boolean denotation. -/
def supportKey (xs : List Bool) : Set Bool :=
  configSupport (singletonConfig xs)

/-- Even retaining the original branch count still forgets branch multiplicities. -/
def supportLengthKey (xs : List Bool) : Set Bool × ℕ :=
  (supportKey xs, xs.length)

/-- Multiplicity-sensitive numerator of the uniform Boolean branch average. -/
def trueMultiplicity (xs : List Bool) : ℕ :=
  xs.count true

/-- Six branches with balanced Boolean multiplicity. -/
def balancedSix : List Bool :=
  [false, false, false, true, true, true]

/-- Six branches with the same support but a skewed Boolean multiplicity. -/
def skewedSix : List Bool :=
  [false, false, false, false, false, true]

/-- The two histories have exactly the same Boolean support. -/
theorem supportKey_balanced_eq_skewed :
    supportKey balancedSix = supportKey skewedSix := by
  rw [supportKey, supportKey, configSupport_singletonConfig,
    configSupport_singletonConfig]
  congr
  native_decide

/-- They also have the same total branch count. -/
theorem supportLengthKey_balanced_eq_skewed :
    supportLengthKey balancedSix = supportLengthKey skewedSix := by
  apply Prod.ext
  · exact supportKey_balanced_eq_skewed
  · native_decide

/-- Their multiplicity-sensitive uniform-average numerators are different. -/
theorem trueMultiplicity_balanced_ne_skewed :
    trueMultiplicity balancedSix ≠ trueMultiplicity skewedSix := by
  native_decide

/-- Boolean support alone cannot recover a uniform branch average numerator. -/
theorem supportKey_not_recovers_trueMultiplicity :
    ¬ Recovers supportKey trueMultiplicity := by
  intro h
  have hsame : trueMultiplicity balancedSix = trueMultiplicity skewedSix :=
    noResurrection h supportKey_balanced_eq_skewed
  exact trueMultiplicity_balanced_ne_skewed hsame

/-- Even Boolean support together with the original branch count is insufficient. -/
theorem supportLengthKey_not_recovers_trueMultiplicity :
    ¬ Recovers supportLengthKey trueMultiplicity := by
  intro h
  have hsame : trueMultiplicity balancedSix = trueMultiplicity skewedSix :=
    noResurrection h supportLengthKey_balanced_eq_skewed
  exact trueMultiplicity_balanced_ne_skewed hsame

/-- Exact recoalescence literally identifies the two six-branch configurations. -/
theorem exactRecoalesce_balanced_eq_skewed :
    exactRecoalesce (singletonConfig balancedSix) =
      exactRecoalesce (singletonConfig skewedSix) := by
  unfold exactRecoalesce
  rw [configSupport_singletonConfig, configSupport_singletonConfig]
  congr
  native_decide

/-- No decoder from the exactly recoalesced token can recover branch multiplicity. -/
theorem exactRecoalescedConfig_not_recovers_trueMultiplicity :
    ¬ Recovers
      (fun xs => exactRecoalesce (singletonConfig xs))
      trueMultiplicity := by
  intro h
  have hsame : trueMultiplicity balancedSix = trueMultiplicity skewedSix :=
    noResurrection h exactRecoalesce_balanced_eq_skewed
  exact trueMultiplicity_balanced_ne_skewed hsame

end EnterpriseMath.BranchAverageNoGo
