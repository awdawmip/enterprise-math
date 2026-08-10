import EnterpriseMath.Quotient.RootQuotientPrimeBasis
import Mathlib.Data.Nat.Factors
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- `k`-factor instruction capacity: every declared primitive quotient
denominator carries at most `k` prime factors, counted with multiplicity. -/
def RootQuotientFactorCapacity (k : ℕ) (G : Set ℕ) : Prop :=
  ∀ g : ℕ, g ∈ G → rootQuotientPrimeFactorCount g ≤ k

/-- Prime-factor count is additive on products of positive denominators. -/
theorem rootQuotientPrimeFactorCount_mul
    {a b : ℕ}
    (ha : 1 ≤ a)
    (hb : 1 ≤ b) :
    rootQuotientPrimeFactorCount (a * b) =
      rootQuotientPrimeFactorCount a + rootQuotientPrimeFactorCount b := by
  have hPerm := Nat.perm_primeFactorsList_mul (by omega : a ≠ 0) (by omega : b ≠ 0)
  have hLen := hPerm.length_eq
  simpa [rootQuotientPrimeFactorCount, List.length_append] using hLen

/-- A word over a `k`-factor primitive alphabet can compile at most `k` prime
factors per executed instruction. -/
theorem rootQuotientPrimeFactorCount_wordProduct_le
    {k : ℕ} {G : Set ℕ} {w : List ℕ}
    (hG : PositiveRootQuotientGenerators G)
    (hCap : RootQuotientFactorCapacity k G)
    (hw : RootQuotientWordOver G w) :
    rootQuotientPrimeFactorCount (rootQuotientWordProduct w) ≤
      k * w.length := by
  induction w with
  | nil =>
      simp [rootQuotientWordProduct, rootQuotientPrimeFactorCount]
  | cons a w ih =>
      have haG : a ∈ G := hw a (by simp)
      have haPos : 1 ≤ a := hG a haG
      have hTail : RootQuotientWordOver G w := by
        intro b hb
        exact hw b (by simp [hb])
      have hTailPos : 1 ≤ rootQuotientWordProduct w :=
        rootQuotientWordProduct_pos hG hTail
      have haCap : rootQuotientPrimeFactorCount a ≤ k := hCap a haG
      have hTailCap := ih hTail
      rw [rootQuotientWordProduct,
        rootQuotientPrimeFactorCount_mul haPos hTailPos]
      simp only [List.length_cons]
      omega

/-- Pointwise capacity lower bound for one compiled target denominator. -/
theorem rootQuotientPrimeFactorCount_le_capacity_mul_horizon_of_reachable
    {k h b : ℕ} {G : Set ℕ}
    (hG : PositiveRootQuotientGenerators G)
    (hCap : RootQuotientFactorCapacity k G)
    (hReach : RootQuotientProductReachableWithin h G b) :
    rootQuotientPrimeFactorCount b ≤ k * h := by
  obtain ⟨w, hwLen, hwG, hProd⟩ := hReach
  rw [hProd]
  exact (rootQuotientPrimeFactorCount_wordProduct_le hG hCap hwG).trans
    (Nat.mul_le_mul_left k hwLen)

/-- Universal instruction-capacity × execution-depth lower bound.

Any positive primitive quotient language with per-instruction prime-factor
capacity at most `k` that separates all exact states by words of length at most
`h` must satisfy

`rootQuotientPrimeHorizon r N ≤ k * h`.

This is a presentation-resource theorem, not a storage-cardinality theorem. -/
theorem rootQuotientPrimeHorizon_le_capacity_mul_horizon
    {r N h k : ℕ} {G : Set ℕ}
    (hr : 1 ≤ r)
    (hG : PositiveRootQuotientGenerators G)
    (hCap : RootQuotientFactorCapacity k G)
    (hSep : SeparatesRootQuotientWordsUpTo r N h G) :
    rootQuotientPrimeHorizon r N ≤ k * h := by
  apply (rootQuotientPrimeHorizon_le_iff
    (r := r) (N := N) (h := k * h)).2
  intro b hbPos hbN hbFree
  have hReach :=
    (separatesRootQuotientWordsUpTo_iff_powerFree_reachable
      (r := r) (N := N) (h := h) (G := G) hr hG).1 hSep
      b hbPos hbN hbFree
  exact
    rootQuotientPrimeFactorCount_le_capacity_mul_horizon_of_reachable
      hG hCap hReach

/-- The bounded prime alphabet has exact factor capacity one. -/
theorem rootQuotientPrimeBasis_factorCapacity_one
    {N : ℕ} :
    RootQuotientFactorCapacity 1 (RootQuotientPrimeBasis N) := by
  intro p hp
  rw [rootQuotientPrimeFactorCount, Nat.primeFactorsList_prime hp.1]
  simp

end EnterpriseMath.Quotient
