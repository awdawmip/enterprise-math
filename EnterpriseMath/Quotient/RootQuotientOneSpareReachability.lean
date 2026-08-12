import EnterpriseMath.Quotient.RootQuotientInstructionMetric
import Mathlib.Data.List.Count
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- Removing all occurrences of one distinguished instruction splits list
length into the residual length plus its occurrence count. -/
theorem length_filter_ne_add_count
    (g : ℕ) (l : List ℕ) :
    (l.filter (fun a : ℕ => a != g)).length + l.count g = l.length := by
  induction l with
  | nil => simp
  | cons a l ih =>
      by_cases hag : a = g
      · subst a
        simp [List.count_cons, ih]
      · simp [List.count_cons, hag, ih]

/-- Multiplicative counterpart: all occurrences of one instruction factor out
of the word product. -/
theorem pow_count_mul_filter_ne_prod
    (g : ℕ) (l : List ℕ) :
    g ^ l.count g * (l.filter (fun a : ℕ => a != g)).prod = l.prod := by
  induction l with
  | nil => simp
  | cons a l ih =>
      by_cases hag : a = g
      · subst a
        simp [List.count_cons, ih, pow_succ,
          Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
      · simp [List.count_cons, hag, ih,
          Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]

/-- **Exact one-spare reachability decomposition.**

A target is reachable within `h` after adjoining one instruction `g` to a base
ISA `G` iff it can be factored as `g^j * b`, where `j<=h` and the residual `b`
is reachable from `G` within the remaining `h-j` steps.

This is the word-level theorem behind the executable identity

`ell_{G+g}(t) = min_j (j + ell_G(t/g^j))`

over admissible powers dividing the target. -/
theorem rootQuotientProductReachableWithin_insert_iff_exists_spare_factorization
    {G : Set ℕ} {g t h : ℕ} :
    RootQuotientProductReachableWithin h (insert g G) t ↔
      ∃ j b : ℕ,
        j ≤ h ∧
        g ^ j * b = t ∧
        RootQuotientProductReachableWithin (h - j) G b := by
  constructor
  · rintro ⟨w, hwLen, hwFull, hProd⟩
    let j := w.count g
    let u := w.filter (fun a : ℕ => a != g)
    let b := rootQuotientWordProduct u
    have hLenSplit : u.length + j = w.length := by
      dsimp [u, j]
      exact length_filter_ne_add_count g w
    have hj : j ≤ h := by omega
    have huLen : u.length ≤ h - j := by omega
    have huG : RootQuotientWordOver G u := by
      intro a haU
      have haFilter := List.mem_filter.1 haU
      have haWord : a ∈ w := haFilter.1
      have haNe : a ≠ g := by
        have := haFilter.2
        simp at this
        exact this
      have haFull := hwFull a haWord
      simp only [Set.mem_insert_iff] at haFull
      rcases haFull with haEq | haG
      · exact (haNe haEq).elim
      · exact haG
    have hSplit : g ^ j * b = rootQuotientWordProduct w := by
      dsimp [j, u, b]
      rw [rootQuotientWordProduct_eq_prod]
      rw [rootQuotientWordProduct_eq_prod]
      exact pow_count_mul_filter_ne_prod g w
    refine ⟨j, b, hj, ?_, ?_⟩
    · exact hSplit.trans hProd.symm
    · exact ⟨u, huLen, huG, rfl⟩
  · rintro ⟨j, b, hj, hFactor, u, huLen, huG, hbProd⟩
    let w := List.replicate j g ++ u
    refine ⟨w, ?_, ?_, ?_⟩
    · dsimp [w]
      simp only [List.length_append, List.length_replicate]
      omega
    · intro a haW
      dsimp [w] at haW
      simp only [List.mem_append, List.mem_replicate] at haW
      rcases haW with haRep | haU
      · subst a
        exact Set.mem_insert g G
      · exact Set.mem_insert_of_mem g (huG a haU)
    · calc
        t = g ^ j * b := hFactor.symm
        _ = g ^ j * rootQuotientWordProduct u := by rw [hbProd]
        _ = rootQuotientWordProduct w := by
          dsimp [w]
          rw [rootQuotientWordProduct_eq_prod]
          simp [List.prod_append, List.prod_replicate,
            rootQuotientWordProduct_eq_prod]

/-- Metric-radius form of the one-spare factorization theorem. -/
theorem rootQuotientInstructionLength_insert_le_natCast_iff_exists_spare_factorization
    {G : Set ℕ} {g t h : ℕ} :
    rootQuotientInstructionLength (insert g G) t ≤ (h : ℕ∞) ↔
      ∃ j b : ℕ,
        j ≤ h ∧
        g ^ j * b = t ∧
        rootQuotientInstructionLength G b ≤ ((h - j : ℕ) : ℕ∞) := by
  rw [rootQuotientInstructionLength_le_natCast_iff]
  rw [rootQuotientProductReachableWithin_insert_iff_exists_spare_factorization]
  constructor
  · rintro ⟨j, b, hj, hFactor, hReach⟩
    exact ⟨j, b, hj, hFactor,
      (rootQuotientInstructionLength_le_natCast_iff).2 hReach⟩
  · rintro ⟨j, b, hj, hFactor, hMetric⟩
    exact ⟨j, b, hj, hFactor,
      (rootQuotientInstructionLength_le_natCast_iff).1 hMetric⟩

end EnterpriseMath.Quotient
