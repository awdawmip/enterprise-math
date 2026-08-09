import EnterpriseMath.Precision.BinaryRootAtlasBoundary
import Mathlib.Data.Finset.Card
import Mathlib.Tactic

namespace EnterpriseMath.Precision

open EnterpriseMath.IntegerRoot

/-- Positive quotient-root states seen by denominators `1,...,n`, encoded by
zero-based indices `i=0,...,n-1` with denominator `i+1`. -/
def quotientRootStates (s n : ℕ) : Finset ℕ :=
  (Finset.range n).image (fun i => root (s + 1) (n / (i + 1)))

/-- High-branch root states, again using zero-based denominator indices. -/
def highQuotientRootStates (s n : ℕ) : Finset ℕ :=
  let H := root (s + 2) ((s + 1) * n - 1)
  let D := n / (H + 1) ^ (s + 1)
  (Finset.range D).image (fun i => root (s + 1) (n / (i + 1)))

/-- Guaranteed low roots `1,...,H-1`, represented as a shifted range so their
cardinality is definitionally tied to `H-1`. -/
def guaranteedLowRootStates (H : ℕ) : Finset ℕ :=
  (Finset.range (H - 1)).image (fun i => i + 1)

/-- The guaranteed low-root set has exactly `H-1` elements. -/
theorem guaranteedLowRootStates_card (H : ℕ) :
    (guaranteedLowRootStates H).card = H - 1 := by
  unfold guaranteedLowRootStates
  exact Finset.card_image_of_injective _ (fun _ _ h => by omega)

/-- Membership in the guaranteed low-root set is exactly the positive interval
strictly below `H`. -/
theorem mem_guaranteedLowRootStates_iff
    {H t : ℕ} :
    t ∈ guaranteedLowRootStates H ↔ 1 ≤ t ∧ t < H := by
  constructor
  · intro ht
    rcases Finset.mem_image.mp ht with ⟨i, hi, rfl⟩
    have hiRange : i < H - 1 := Finset.mem_range.mp hi
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

/-- The high quotient-root branch contributes exactly one state per high
positive denominator label, hence exactly `D` states. -/
theorem highQuotientRootStates_card
    {s n : ℕ}
    (hn : 0 < n) :
    let H := root (s + 2) ((s + 1) * n - 1)
    let D := n / (H + 1) ^ (s + 1)
    (highQuotientRootStates s n).card = D := by
  let H := root (s + 2) ((s + 1) * n - 1)
  let D := n / (H + 1) ^ (s + 1)
  change (highQuotientRootStates s n).card = D
  unfold highQuotientRootStates
  dsimp only
  apply Finset.card_image_of_injOn
  intro i hi j hj hEq
  have hiD : i < D := Finset.mem_range.mp hi
  have hjD : j < D := Finset.mem_range.mp hj
  have hDenEq := high_denominator_root_injective
    (s := s) (n := n) (d := i + 1) (e := j + 1)
    hn (by omega) (by omega)
    (by omega) (by omega) hEq
  omega

end EnterpriseMath.Precision
