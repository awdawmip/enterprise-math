import Mathlib.Analysis.SpecialFunctions.Pow.NthRootLemmas
import Mathlib.Order.Interval.Finset.Nat

namespace EnterpriseMath.IntegerRoot

/-- Enterprise Math's natural-state root is mathlib's integer `Nat.nthRoot`. -/
abbrev root : ℕ → ℕ → ℕ := Nat.nthRoot

/-- Perfect-power collapse specialized to natural-number nth roots. -/
def collapse (p n : ℕ) : ℕ :=
  root p n ^ p

/-- Positive powering is left adjoint to the integer nth root. -/
theorem galoisConnection_pow_root {p : ℕ} (hp : p ≠ 0) :
    GaloisConnection (fun a : ℕ => a ^ p) (root p) := by
  intro a b
  exact (Nat.le_nthRoot_iff (n := p) (a := a) (b := b) hp).symm

/-- T003: the positive-exponent integer root is monotone in its state argument. -/
theorem root_monotone {p : ℕ} (hp : p ≠ 0) : Monotone (root p) :=
  (galoisConnection_pow_root hp).monotone_u

/-- Exact basin characterization of the integer root. -/
theorem root_eq_iff {p n k : ℕ} (hp : p ≠ 0) :
    root p n = k ↔ k ^ p ≤ n ∧ n < (k + 1) ^ p := by
  constructor
  · rintro rfl
    exact ⟨Nat.pow_nthRoot_le (.inl hp), Nat.lt_pow_nthRoot_add_one hp n⟩
  · rintro ⟨h₁, h₂⟩
    exact Nat.nthRoot_eq_of_le_of_lt h₁ h₂

/-- T007: a collapse basin is exactly the half-open interval between consecutive p-th powers. -/
theorem collapse_eq_pow_iff {p n k : ℕ} (hp : p ≠ 0) :
    collapse p n = k ^ p ↔ k ^ p ≤ n ∧ n < (k + 1) ^ p := by
  constructor
  · intro h
    have hpow : root p n ^ p = k ^ p := by
      simpa [collapse] using h
    have hroot : root p n = k := Nat.pow_left_injective hp hpow
    exact (root_eq_iff hp).1 hroot
  · intro h
    have hroot : root p n = k := (root_eq_iff hp).2 h
    simp [collapse, hroot]

/-- Finite state set of the basin with root index `k` at exponent `p`. -/
def basin (p k : ℕ) : Finset ℕ :=
  Finset.Ico (k ^ p) ((k + 1) ^ p)

/-- Positive-exponent collapse membership agrees exactly with the finite basin interval. -/
theorem mem_basin_iff {p n k : ℕ} (hp : p ≠ 0) :
    n ∈ basin p k ↔ collapse p n = k ^ p := by
  rw [collapse_eq_pow_iff hp]
  simp [basin]

/-- T008: the exact number of states in a perfect-power collapse basin. -/
theorem basin_card (p k : ℕ) :
    (basin p k).card = (k + 1) ^ p - k ^ p := by
  simp [basin]

/-- T008 square specialization: the k-th square basin contains exactly `2k+1` states. -/
theorem basin_card_square (k : ℕ) :
    (basin 2 k).card = 2 * k + 1 := by
  rw [basin_card, Nat.sq_sub_sq]
  simp
  omega

/-- T008 identity specialization: every p=1 basin is a singleton. -/
theorem basin_card_one (k : ℕ) :
    (basin 1 k).card = 1 := by
  simp [basin]

/-- T009: positive-exponent perfect-power collapse is monotone. -/
theorem collapse_monotone {p : ℕ} (hp : p ≠ 0) : Monotone (collapse p) := by
  intro a b hab
  simpa [collapse] using Nat.pow_le_pow_left (root_monotone hp hab) p

/-- Enterprise Math collapse is reductive. -/
theorem collapse_le {p : ℕ} (hp : p ≠ 0) (n : ℕ) : collapse p n ≤ n := by
  exact Nat.pow_nthRoot_le (n := p) (a := n) (.inl hp)

/-- Perfect powers are recovered exactly by the integer root. -/
theorem root_pow {p : ℕ} (hp : p ≠ 0) (n : ℕ) : root p (n ^ p) = n := by
  exact Nat.nthRoot_pow hp n

/-- T011 positive half: integer root is a left inverse of positive powering. -/
theorem root_leftInverse_pow {p : ℕ} (hp : p ≠ 0) :
    Function.LeftInverse (root p) (fun n : ℕ => n ^ p) := by
  intro n
  exact root_pow hp n

/-- Every nontrivial exponent sends state 2 to the first perfect-power state. -/
theorem collapse_two_eq_one {p : ℕ} (hp : 2 ≤ p) : collapse p 2 = 1 := by
  have hp0 : p ≠ 0 := by omega
  have hpow : 2 < 2 ^ p := by
    calc
      2 < 2 ^ 2 := by decide
      _ ≤ 2 ^ p := Nat.pow_le_pow_right (by decide) hp
  have hcollapse : collapse p 2 = 1 ^ p :=
    (collapse_eq_pow_iff (p := p) (n := 2) (k := 1) hp0).2 ⟨by simp, hpow⟩
  simpa using hcollapse

/-- T011 negative half: state 2 is a uniform counterexample to two-sided inversion for every p>=2. -/
theorem collapse_two_ne_self {p : ℕ} (hp : 2 ≤ p) : collapse p 2 ≠ 2 := by
  rw [collapse_two_eq_one hp]
  decide

/-- T011: for every nontrivial exponent, power-after-root is not the identity on all states. -/
theorem root_pow_not_two_sided {p : ℕ} (hp : 2 ≤ p) :
    ¬ ∀ n : ℕ, root p n ^ p = n := by
  intro h
  have h2 : collapse p 2 = 2 := by
    simpa [collapse] using h 2
  exact collapse_two_ne_self hp h2

/-- The algebraic p=1 member is exactly the identity root. -/
theorem root_one (n : ℕ) : root 1 n = n := rfl

/-- The algebraic p=1 collapse member is exactly the identity. -/
theorem collapse_one (n : ℕ) : collapse 1 n = n := by
  simp [collapse, root]

/-- Perfect-power collapse is idempotent. -/
theorem collapse_idempotent {p : ℕ} (hp : p ≠ 0) (n : ℕ) :
    collapse p (collapse p n) = collapse p n := by
  simp [collapse, root, Nat.nthRoot_pow hp]

/-- Collapse fixed points are exactly perfect p-th powers. -/
theorem collapse_eq_self_iff {p : ℕ} (hp : p ≠ 0) (n : ℕ) :
    collapse p n = n ↔ ∃ k : ℕ, k ^ p = n := by
  simpa [collapse, root] using (Nat.exists_pow_eq_iff' (n := p) (a := n) hp).symm

/-- Positive iterated integer roots compose by multiplying exponents. -/
theorem root_mul {p q : ℕ} (hp : p ≠ 0) (hq : q ≠ 0) (n : ℕ) :
    root (p * q) n = root p (root q n) := by
  have hpq : p * q ≠ 0 := Nat.mul_ne_zero hp hq
  have gcPQ := galoisConnection_pow_root hpq
  have gcComp := (galoisConnection_pow_root hp).compose (galoisConnection_pow_root hq)
  exact gcPQ.u_unique gcComp (fun a => by simp [pow_mul])

/-- Positive iterated integer roots commute. -/
theorem root_mul_comm {p q : ℕ} (hp : p ≠ 0) (hq : q ≠ 0) (n : ℕ) :
    root p (root q n) = root q (root p n) := by
  calc
    root p (root q n) = root (p * q) n := (root_mul hp hq n).symm
    _ = root (q * p) n := by rw [Nat.mul_comm]
    _ = root q (root p n) := root_mul hq hp n

end EnterpriseMath.IntegerRoot
