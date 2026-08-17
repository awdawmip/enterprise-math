import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Data.Finset.Card

namespace EnterpriseMath.Scale

/-- Cross-multiplication equality for boundaries `i/d = j/e` without introducing rationals. -/
def boundaryEq (d i e j : ℕ) : Prop :=
  i * e = j * d

/-- Multiplying both scale denominators by the same positive factor does not change
boundary coincidence. -/
theorem boundaryEq_mul_right_iff {d e g i j : ℕ} (hg : 0 < g) :
    boundaryEq (d * g) i (e * g) j ↔ boundaryEq d i e j := by
  unfold boundaryEq
  constructor
  · intro h
    apply Nat.mul_right_cancel hg
    simpa [Nat.mul_assoc] using h
  · intro h
    simpa [Nat.mul_assoc] using congrArg (fun x : ℕ => x * g) h

/-- For coprime positive scales, coincident grid boundaries occur exactly at a common
integer index: `i/d = j/e` iff `i=d*k` and `j=e*k` for some `k`.

This is the arithmetic core of the R007 overlap-component decomposition. -/
theorem boundaryEq_coprime_iff {d e i j : ℕ} (hcop : d.Coprime e) (hd : 0 < d) :
    boundaryEq d i e j ↔ ∃ k, i = d * k ∧ j = e * k := by
  constructor
  · intro h
    have hdi : d ∣ i := by
      apply hcop.dvd_of_dvd_mul_right
      rw [h]
      exact Nat.dvd_mul_left d j
    rcases hdi with ⟨k, hk⟩
    refine ⟨k, hk, ?_⟩
    apply Nat.mul_right_cancel hd
    calc
      j * d = i * e := h.symm
      _ = (d * k) * e := by rw [hk]
      _ = (e * k) * d := by
        simp [Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
  · rintro ⟨k, rfl, rfl⟩
    simp [boundaryEq, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]

/-- Two arbitrary positive uniform grids share boundaries exactly at multiples of their
reduced coprime step sizes `d/gcd(d,e)` and `e/gcd(d,e)`.

Equivalently, the common boundary grid is the `gcd(d,e)` grid. -/
theorem boundaryEq_gcd_iff {d e i j : ℕ} (hd : 0 < d) :
    boundaryEq d i e j ↔
      ∃ k, i = (d / d.gcd e) * k ∧ j = (e / d.gcd e) * k := by
  let g := d.gcd e
  change boundaryEq d i e j ↔
    ∃ k, i = (d / g) * k ∧ j = (e / g) * k
  have hg : 0 < g := by
    dsimp [g]
    exact Nat.gcd_pos_of_pos_left e hd
  have hcop : (d / g).Coprime (e / g) := by
    dsimp [g]
    exact Nat.coprime_div_gcd_div_gcd (Nat.gcd_pos_of_pos_left e hd)
  have hd' : 0 < d / g := by
    dsimp [g]
    exact Nat.div_gcd_pos_of_pos_left e hd
  have hd_decomp : d = (d / g) * g := by
    exact (Nat.div_mul_cancel (by
      dsimp [g]
      exact Nat.gcd_dvd_left d e)).symm
  have he_decomp : e = (e / g) * g := by
    exact (Nat.div_mul_cancel (by
      dsimp [g]
      exact Nat.gcd_dvd_right d e)).symm
  have hscale : boundaryEq d i e j ↔ boundaryEq (d / g) i (e / g) j := by
    rw [hd_decomp, he_decomp]
    exact boundaryEq_mul_right_iff hg
  calc
    boundaryEq d i e j ↔ boundaryEq (d / g) i (e / g) j := hscale
    _ ↔ ∃ k, i = (d / g) * k ∧ j = (e / g) * k :=
      boundaryEq_coprime_iff hcop hd'

/-- Inside the closed unit interval, every common boundary has a unique reduced index
`k ≤ gcd(d,e)`. This is the finite form needed to count the common boundaries. -/
theorem boundaryEq_gcd_existsUnique_index {d e i j : ℕ} (hd : 0 < d)
    (hi : i ≤ d) (h : boundaryEq d i e j) :
    ∃! k,
      k ≤ d.gcd e ∧
        i = (d / d.gcd e) * k ∧
        j = (e / d.gcd e) * k := by
  let g := d.gcd e
  change ∃! k,
    k ≤ g ∧
      i = (d / g) * k ∧
      j = (e / g) * k
  have hd' : 0 < d / g := by
    dsimp [g]
    exact Nat.div_gcd_pos_of_pos_left e hd
  have hd_decomp : d = (d / g) * g := by
    exact (Nat.div_mul_cancel (by
      dsimp [g]
      exact Nat.gcd_dvd_left d e)).symm
  have hrepr := (boundaryEq_gcd_iff hd).1 h
  change ∃ k, i = (d / g) * k ∧ j = (e / g) * k at hrepr
  rcases hrepr with ⟨k, hik, hjk⟩
  have hk_le : k ≤ g := by
    apply Nat.le_of_mul_le_mul_left ?_ hd'
    calc
      (d / g) * k = i := hik.symm
      _ ≤ d := hi
      _ = (d / g) * g := hd_decomp
  refine ⟨k, ⟨hk_le, hik, hjk⟩, ?_⟩
  intro l hl
  rcases hl with ⟨_, hil, _⟩
  apply Nat.mul_left_cancel hd'
  calc
    (d / g) * l = i := hil.symm
    _ = (d / g) * k := hik

/-- Canonical pair of boundary indices corresponding to reduced common-grid index `k`. -/
def gcdBoundaryPair (d e k : ℕ) : ℕ × ℕ :=
  ((d / d.gcd e) * k, (e / d.gcd e) * k)

/-- All common boundary-index pairs in the closed unit interval, represented by their
canonical reduced indices `0, ..., gcd(d,e)`. -/
def gcdBoundaryPairs (d e : ℕ) : Finset (ℕ × ℕ) :=
  (Finset.range (d.gcd e + 1)).image (gcdBoundaryPair d e)

/-- Positive scales make the canonical reduced-index representation injective. -/
theorem gcdBoundaryPair_injective {d e : ℕ} (hd : 0 < d) :
    Function.Injective (gcdBoundaryPair d e) := by
  intro a b hab
  have hd' : 0 < d / d.gcd e := Nat.div_gcd_pos_of_pos_left e hd
  have hfst := congrArg Prod.fst hab
  exact Nat.mul_left_cancel hd' hfst

/-- There are exactly `gcd(d,e)+1` common grid boundaries in the closed unit interval. -/
theorem gcdBoundaryPairs_card {d e : ℕ} (hd : 0 < d) :
    (gcdBoundaryPairs d e).card = d.gcd e + 1 := by
  unfold gcdBoundaryPairs
  rw [Finset.card_image_of_injective _ (gcdBoundaryPair_injective hd)]
  simp

/-- The canonical finite image is exactly the set of boundary-index pairs in `[0,1]`
that represent the same geometric boundary. -/
theorem mem_gcdBoundaryPairs_iff {d e i j : ℕ} (hd : 0 < d) :
    (i, j) ∈ gcdBoundaryPairs d e ↔
      i ≤ d ∧ j ≤ e ∧ boundaryEq d i e j := by
  let g := d.gcd e
  have hd_decomp : d = (d / g) * g := by
    exact (Nat.div_mul_cancel (by
      dsimp [g]
      exact Nat.gcd_dvd_left d e)).symm
  have he_decomp : e = (e / g) * g := by
    exact (Nat.div_mul_cancel (by
      dsimp [g]
      exact Nat.gcd_dvd_right d e)).symm
  constructor
  · intro hmem
    unfold gcdBoundaryPairs at hmem
    rcases Finset.mem_image.mp hmem with ⟨k, hk, hpair⟩
    have hk_le : k ≤ g := by
      exact Nat.le_of_lt_succ (Finset.mem_range.mp hk)
    have hik : i = (d / g) * k := by
      have := congrArg Prod.fst hpair
      simpa [gcdBoundaryPair, g] using this.symm
    have hjk : j = (e / g) * k := by
      have := congrArg Prod.snd hpair
      simpa [gcdBoundaryPair, g] using this.symm
    refine ⟨?_, ?_, ?_⟩
    · rw [hik, hd_decomp]
      exact Nat.mul_le_mul_left (d / g) hk_le
    · rw [hjk, he_decomp]
      exact Nat.mul_le_mul_left (e / g) hk_le
    · apply (boundaryEq_gcd_iff hd).2
      exact ⟨k, by simpa [g] using hik, by simpa [g] using hjk⟩
  · rintro ⟨hi, _hj, hboundary⟩
    obtain ⟨k, hk, _huniq⟩ := boundaryEq_gcd_existsUnique_index hd hi hboundary
    rcases hk with ⟨hk_le, hik, hjk⟩
    unfold gcdBoundaryPairs
    apply Finset.mem_image.mpr
    refine ⟨k, ?_, ?_⟩
    · exact Finset.mem_range.mpr (Nat.lt_succ_of_le hk_le)
    · apply Prod.ext
      · simpa [gcdBoundaryPair] using hik.symm
      · simpa [gcdBoundaryPair] using hjk.symm

end EnterpriseMath.Scale
