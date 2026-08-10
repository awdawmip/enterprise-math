import EnterpriseMath.Scale.FareyGridBridge
import Mathlib.Tactic

namespace EnterpriseMath.Scale

/-- Scaling the numerator and denominator of the candidate grid point by the same
positive factor does not change membership in a fixed closed gap. -/
theorem fracInClosedGap_mul_right_iff {l ln u un x h g : ℕ} (hg : 0 < g) :
    fracInClosedGap l ln u un (x * g) (h * g) ↔
      fracInClosedGap l ln u un x h := by
  unfold fracInClosedGap fracLe
  constructor
  · rintro ⟨h₁, h₂⟩
    constructor
    · have hs : (l * h) * g ≤ (x * ln) * g := by
        simpa [Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using h₁
      exact (Nat.mul_le_mul_right g).1 hs
    · have hs : (x * un) * g ≤ (u * h) * g := by
        simpa [Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using h₂
      exact (Nat.mul_le_mul_right g).1 hs
  · rintro ⟨h₁, h₂⟩
    constructor
    · have hs : (l * h) * g ≤ (x * ln) * g :=
        (Nat.mul_le_mul_right g).2 h₁
      simpa [Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using hs
    · have hs : (x * un) * g ≤ (u * h) * g :=
        (Nat.mul_le_mul_right g).2 h₂
      simpa [Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm] using hs

/-- A gap grid point at scale `h` induces one at every positive multiple `h*g`. -/
theorem gapHasGridPoint_mul_right {l ln u un h g : ℕ} (hg : 0 < g)
    (hh : gapHasGridPoint l ln u un h) :
    gapHasGridPoint l ln u un (h * g) := by
  rcases hh with ⟨x, hx⟩
  exact ⟨x * g, (fracInClosedGap_mul_right_iff hg).2 hx⟩

/-- If a source gap has no point at the multiple scale `h*g`, then it has no point at
scale `h`. -/
theorem gapNoGridPoint_of_no_mul_right {l ln u un h g : ℕ} (hg : 0 < g)
    (hno : ¬ gapHasGridPoint l ln u un (h * g)) :
    ¬ gapHasGridPoint l ln u un h := by
  intro hh
  exact hno (gapHasGridPoint_mul_right hg hh)

/-- Nonprimitive bridge descent: a proper `N`-grid point with nontrivial gcd immediately
reduces to the smaller denominator `N/gcd(m,N)`. -/
theorem nonprimitive_grid_bridge_descend
    {m N sl sln su sun tl tln tu tun : ℕ}
    (hm : 0 < m) (hmN : m < N)
    (hnotcop : ¬ m.Coprime N)
    (htarget : fracInClosedGap tl tln tu tun m N)
    (hsourceNoN : ¬ gapHasGridPoint sl sln su sun N) :
    ∃ h,
      0 < h ∧ h < N ∧
        gapHasGridPoint tl tln tu tun h ∧
        ¬ gapHasGridPoint sl sln su sun h := by
  let g := m.gcd N
  let m' := m / g
  let h := N / g
  have hN : 0 < N := by omega
  have hg : 0 < g := Nat.gcd_pos_of_pos_left N hm
  have hg_ne_one : g ≠ 1 := by
    intro hg1
    apply hnotcop
    exact (Nat.coprime_iff_gcd_eq_one).2 (by simpa [g] using hg1)
  have hg_one_lt : 1 < g := by omega
  have hm_decomp : m = m' * g := by
    dsimp [m', g]
    exact (Nat.div_mul_cancel (Nat.gcd_dvd_left m N)).symm
  have hN_decomp : N = h * g := by
    dsimp [h, g]
    exact (Nat.div_mul_cancel (Nat.gcd_dvd_right m N)).symm
  have hh : 0 < h := by
    have : 0 < h * g := by simpa [hN_decomp] using hN
    exact Nat.pos_of_mul_pos_left this
  have hhN : h < N := by
    rw [hN_decomp]
    have hmul : h * 1 < h * g := (Nat.mul_lt_mul_left hh).2 hg_one_lt
    simpa using hmul
  have htarget' : fracInClosedGap tl tln tu tun m' h := by
    have hscaled : fracInClosedGap tl tln tu tun (m' * g) (h * g) := by
      simpa [hm_decomp, hN_decomp] using htarget
    exact (fracInClosedGap_mul_right_iff hg).1 hscaled
  have hsourceNoH : ¬ gapHasGridPoint sl sln su sun h := by
    apply gapNoGridPoint_of_no_mul_right hg
    simpa [hN_decomp] using hsourceNoN
  exact ⟨h, hh, hhN, ⟨m', htarget'⟩, hsourceNoH⟩

/-- Full R007 grid-bridge descent.

A proper `N`-grid point lies strictly inside the target gap, while the source gap has
no `N`-grid point. If the point is nonprimitive, reduce it. If primitive, descend to
one of its two determinant-one Farey parents. In both cases a strictly smaller scale
already separates target from source. -/
theorem grid_bridge_descend
    {m N sl sln su sun tl tln tu tun : ℕ}
    (hm : 0 < m) (hmN : m < N)
    (htln : tln < N) (htun : tun < N)
    (htargetLeft : fracLt tl tln m N)
    (htargetRight : fracLt m N tu tun)
    (hsourceNoN : ¬ gapHasGridPoint sl sln su sun N) :
    ∃ h,
      0 < h ∧ h < N ∧
        gapHasGridPoint tl tln tu tun h ∧
        ¬ gapHasGridPoint sl sln su sun h := by
  by_cases hcop : m.Coprime N
  · exact primitive_grid_bridge_descend hm hmN hcop htln htun
      htargetLeft htargetRight hsourceNoN
  · have htarget : fracInClosedGap tl tln tu tun m N := by
      unfold fracInClosedGap fracLe
      unfold fracLt at htargetLeft htargetRight
      exact ⟨Nat.le_of_lt htargetLeft, Nat.le_of_lt htargetRight⟩
    exact nonprimitive_grid_bridge_descend hm hmN hcop htarget hsourceNoN

end EnterpriseMath.Scale
