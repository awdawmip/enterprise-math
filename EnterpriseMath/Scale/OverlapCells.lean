import EnterpriseMath.Scale.OverlapBoundary
import Mathlib.Tactic

namespace EnterpriseMath.Scale

/-- Positive-length overlap of the half-open uniform cells
`[i/d,(i+1)/d)` and `[j/e,(j+1)/e)`, expressed without rationals. -/
def cellOverlap (d i e j : ℕ) : Prop :=
  i * e < (j + 1) * d ∧ j * d < (i + 1) * e

/-- Multiplying both scale denominators by the same positive factor preserves the
cell-overlap relation. -/
theorem cellOverlap_mul_right_iff {d e g i j : ℕ} (hg : 0 < g) :
    cellOverlap (d * g) i (e * g) j ↔ cellOverlap d i e j := by
  unfold cellOverlap
  constructor
  · rintro ⟨h₁, h₂⟩
    constructor
    · have hs : (i * e) * g < ((j + 1) * d) * g := by
        simpa [Nat.mul_assoc] using h₁
      exact (Nat.mul_lt_mul_right hg).1 hs
    · have hs : (j * d) * g < ((i + 1) * e) * g := by
        simpa [Nat.mul_assoc] using h₂
      exact (Nat.mul_lt_mul_right hg).1 hs
  · rintro ⟨h₁, h₂⟩
    constructor
    · have hs : (i * e) * g < ((j + 1) * d) * g :=
        (Nat.mul_lt_mul_right hg).2 h₁
      simpa [Nat.mul_assoc] using hs
    · have hs : (j * d) * g < ((i + 1) * e) * g :=
        (Nat.mul_lt_mul_right hg).2 h₂
      simpa [Nat.mul_assoc] using hs

/-- After dividing both scales by their gcd, overlap is unchanged at the level of
raw cell indices. The quotient cell indices may span several reduced blocks; those
blocks are classified below. -/
theorem cellOverlap_gcd_reduced_iff {d e i j : ℕ} (hd : 0 < d) :
    cellOverlap d i e j ↔
      cellOverlap (d / d.gcd e) i (e / d.gcd e) j := by
  let g := d.gcd e
  have hg : 0 < g := by
    dsimp [g]
    exact Nat.gcd_pos_of_pos_left e hd
  have hd_decomp : d = (d / g) * g := by
    exact (Nat.div_mul_cancel (by
      dsimp [g]
      exact Nat.gcd_dvd_left d e)).symm
  have he_decomp : e = (e / g) * g := by
    exact (Nat.div_mul_cancel (by
      dsimp [g]
      exact Nat.gcd_dvd_right d e)).symm
  rw [hd_decomp, he_decomp]
  exact cellOverlap_mul_right_iff hg

/-- Gcd-block label of a scale-`d` cell relative to another scale `e`.
For positive `d`, the reduced block width is `d/gcd(d,e)`. -/
def gcdBlockD (d e i : ℕ) : ℕ :=
  i / (d / d.gcd e)

/-- Symmetric gcd-block label on the `e` side. -/
def gcdBlockE (d e j : ℕ) : ℕ :=
  j / (e / d.gcd e)

/-- Every positive-length overlap edge stays inside one common gcd block.

This is the separation half of the theorem that the bipartite overlap graph has
exactly `gcd(d,e)` connected components. -/
theorem cellOverlap_same_gcdBlock {d e i j : ℕ} (hd : 0 < d) (he : 0 < e)
    (hov : cellOverlap d i e j) :
    gcdBlockD d e i = gcdBlockE d e j := by
  let g := d.gcd e
  let d' := d / g
  let e' := e / g
  let a := i / d'
  let b := j / e'
  have hd' : 0 < d' := by
    dsimp [d', g]
    exact Nat.div_gcd_pos_of_pos_left e hd
  have he' : 0 < e' := by
    have hg_symm : e.gcd d = g := by
      dsimp [g]
      rw [Nat.gcd_comm]
    dsimp [e']
    rw [← hg_symm]
    exact Nat.div_gcd_pos_of_pos_left d he
  have hred : cellOverlap d' i e' j := by
    dsimp [d', e', g]
    exact (cellOverlap_gcd_reduced_iff hd).1 hov
  change a = b
  by_contra hne
  rcases lt_or_gt_of_ne hne with hab | hba
  · have hi_upper_raw : i < a * d' + d' := by
      simpa [a] using Nat.lt_div_mul_add i hd'
    have hi_upper : i + 1 ≤ (a + 1) * d' := by
      have : i + 1 ≤ a * d' + d' := by omega
      simpa [Nat.add_mul] using this
    have hj_lower : b * e' ≤ j := by
      simpa [b] using Nat.div_mul_le_self j e'
    have hab' : a + 1 ≤ b := by omega
    have h₁ : (a + 1) * e' ≤ b * e' := Nat.mul_le_mul_right e' hab'
    have h₂ : ((a + 1) * e') * d' ≤ (b * e') * d' :=
      Nat.mul_le_mul_right d' h₁
    have h₃ : (b * e') * d' ≤ j * d' := Nat.mul_le_mul_right d' hj_lower
    have h₄ : (i + 1) * e' ≤ ((a + 1) * d') * e' :=
      Nat.mul_le_mul_right e' hi_upper
    have hcontra : ((a + 1) * d') * e' < ((a + 1) * d') * e' := by
      calc
        ((a + 1) * d') * e' = ((a + 1) * e') * d' := by ac_rfl
        _ ≤ (b * e') * d' := h₂
        _ ≤ j * d' := h₃
        _ < (i + 1) * e' := hred.2
        _ ≤ ((a + 1) * d') * e' := h₄
    exact (Nat.lt_irrefl _) hcontra
  · have hj_upper_raw : j < b * e' + e' := by
      simpa [b] using Nat.lt_div_mul_add j he'
    have hj_upper : j + 1 ≤ (b + 1) * e' := by
      have : j + 1 ≤ b * e' + e' := by omega
      simpa [Nat.add_mul] using this
    have hi_lower : a * d' ≤ i := by
      simpa [a] using Nat.div_mul_le_self i d'
    have hba' : b + 1 ≤ a := by omega
    have h₁ : (b + 1) * d' ≤ a * d' := Nat.mul_le_mul_right d' hba'
    have h₂ : ((b + 1) * d') * e' ≤ (a * d') * e' :=
      Nat.mul_le_mul_right e' h₁
    have h₃ : (a * d') * e' ≤ i * e' := Nat.mul_le_mul_right e' hi_lower
    have h₄ : (j + 1) * d' ≤ ((b + 1) * e') * d' :=
      Nat.mul_le_mul_right d' hj_upper
    have hcontra : ((b + 1) * e') * d' < ((b + 1) * e') * d' := by
      calc
        ((b + 1) * e') * d' = ((b + 1) * d') * e' := by ac_rfl
        _ ≤ (a * d') * e' := h₂
        _ ≤ i * e' := h₃
        _ < (j + 1) * d' := hred.1
        _ ≤ ((b + 1) * e') * d' := h₄
    exact (Nat.lt_irrefl _) hcontra

end EnterpriseMath.Scale
