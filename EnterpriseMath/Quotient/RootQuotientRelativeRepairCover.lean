import EnterpriseMath.Quotient.RootQuotientMultiSpareReachability
import EnterpriseMath.Quotient.RootQuotientCompositeMacroStorage
import Mathlib.Data.Set.Card
import Mathlib.Order.Lattice.Nat
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- A candidate-restricted divisor hitting set for a finite family of targets.

The candidate set is explicit so that trivial divisors such as `1`, or primitive
instructions that are not allowed as optional macros, do not collapse the cover
problem. -/
def RootQuotientRepairDivisorCover
    (T : Finset ℕ) (C S : Set ℕ) : Prop :=
  S ⊆ C ∧
  ∀ t ∈ T, ∃ g : ℕ, g ∈ S ∧ g ∣ t

/-- Feasible cardinalities of finite candidate-restricted divisor covers. -/
def RootQuotientRepairDivisorCoverCardinalities
    (T : Finset ℕ) (C : Set ℕ) : Set ℕ :=
  {m : ℕ | ∃ S : Set ℕ,
    S.Finite ∧
    RootQuotientRepairDivisorCover T C S ∧
    S.ncard = m}

/-- Minimum candidate-restricted divisor-cover size.

This is a first-order repair lower bound.  It records only the necessity that
some stored spare divisor hit every base-hard target; it does not by itself
assert that the selected divisors meet the execution-depth budget. -/
noncomputable def rootQuotientRepairDivisorCoverNumber
    (T : Finset ℕ) (C : Set ℕ) : ℕ :=
  sInf (RootQuotientRepairDivisorCoverCardinalities T C)

/-- The repair divisor-cover number is no larger than any finite admissible
cover. -/
theorem rootQuotientRepairDivisorCoverNumber_le
    {T : Finset ℕ} {C S : Set ℕ}
    (hSFinite : S.Finite)
    (hCover : RootQuotientRepairDivisorCover T C S) :
    rootQuotientRepairDivisorCoverNumber T C ≤ S.ncard := by
  apply Nat.sInf_le
  exact ⟨S, hSFinite, hCover, rfl⟩

/-- **Relative repair-cover storage lower bound.**

If a finite spare dictionary `S` lies in the allowed candidate set `C` and
repairs every target in a finite family that is horizon-hard for the base ISA
`G`, then the candidate-restricted divisor-cover number is a lower bound on the
number of stored spare types. -/
theorem repairDivisorCoverNumber_le_spare_storage
    {G C S : Set ℕ} {h : ℕ} {T : Finset ℕ}
    (hSFinite : S.Finite)
    (hSC : S ⊆ C)
    (hReach : ∀ t ∈ T,
      RootQuotientProductReachableWithin h (G ∪ S) t)
    (hNoBase : ∀ t ∈ T,
      ¬RootQuotientProductReachableWithin h G t) :
    rootQuotientRepairDivisorCoverNumber T C ≤ S.ncard := by
  apply rootQuotientRepairDivisorCoverNumber_le hSFinite
  refine ⟨hSC, ?_⟩
  exact spare_family_divisor_covers_base_hard_targets hReach hNoBase

/-- Ambient candidate set for normalized optional composite macros. -/
def RootQuotientSemanticCompositeCandidates
    (r N : ℕ) : Set ℕ :=
  RootQuotientNontrivialPowerFreeBasis r N \ RootQuotientPrimeBasis N

/-- The existing composite-macro-family predicate is exactly containment in the
semantic composite candidate set. -/
theorem compositeMacroFamily_iff_subset_semanticCompositeCandidates
    {r N : ℕ} {S : Set ℕ} :
    RootQuotientCompositeMacroFamily r N S ↔
      S ⊆ RootQuotientSemanticCompositeCandidates r N := by
  rfl

/-- Any feasible normalized macro presentation yields the corresponding
candidate-restricted divisor-cover lower bound for every finite family of
semantic targets that is hard for the prime base. -/
theorem semanticRepairDivisorCoverNumber_le_macroPresentation
    {r N h : ℕ} {S : Set ℕ} {T : Finset ℕ}
    (hr : 2 ≤ r)
    (hS : RootQuotientCompositeMacroPresentation r N h S)
    (hSemantic : ∀ t ∈ T,
      t ∈ RootQuotientNontrivialPowerFreeBasis r N)
    (hNoPrime : ∀ t ∈ T,
      ¬RootQuotientProductReachableWithin h (RootQuotientPrimeBasis N) t) :
    rootQuotientRepairDivisorCoverNumber
        T (RootQuotientSemanticCompositeCandidates r N) ≤ S.ncard := by
  have hPos : PositiveRootQuotientGenerators
      (RootQuotientPrimeBasis N ∪ S) := by
    intro g hg
    rcases hg with hgPrime | hgS
    · exact hgPrime.1.one_le
    · have hgSemantic := (hS.2.1 hgS).1
      omega
  have hReach : ∀ t ∈ T,
      RootQuotientProductReachableWithin h
        (RootQuotientPrimeBasis N ∪ S) t := by
    intro t ht
    have htSemantic := hSemantic t ht
    exact
      (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
        (r := r) (N := N) (h := h)
        (G := RootQuotientPrimeBasis N ∪ S)
        (by omega) hPos).1 hS.2.2
        t (by omega) htSemantic.2.1 htSemantic.2.2
  exact repairDivisorCoverNumber_le_spare_storage
    hS.1 hS.2.1 hReach hNoPrime

end EnterpriseMath.Quotient
