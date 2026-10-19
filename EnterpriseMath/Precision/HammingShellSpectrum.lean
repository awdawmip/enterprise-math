import EnterpriseMath.Precision.HammingKrawtchoukKernel
import Mathlib.Algebra.Order.Ring.Nat

namespace EnterpriseMath.Precision

/-- Krawtchouk mode on the natural-number shell coordinate `j`. -/
noncomputable def hammingShellMode (m k j : ℕ) : ℚ :=
  hammingModeCoeff j (m - j) k

/--
Permutation-invariant Hamming-shell adjacency operator, evaluated at shell `j`.
Outside the physical range only values multiplied by a zero boundary coefficient can occur.
-/
def hammingShellAdjacency (m : ℕ) (f : ℕ → ℚ) (j : ℕ) : ℚ :=
  (j : ℚ) * f (j - 1) + ((m - j : ℕ) : ℚ) * f (j + 1)

/-- Normalized shell operator `K_m=(mI-A_m)/2`. -/
def hammingShellK (m : ℕ) (f : ℕ → ℚ) (j : ℕ) : ℚ :=
  ((m : ℚ) * f j - hammingShellAdjacency m f j) / 2

/--
WSR-L46: every physical Krawtchouk shell mode obeys the adjacency eigen-equation
with eigenvalue `m-2k`.
-/
theorem hammingShellAdjacency_mode
    (m k j : ℕ) (hk : k ≤ m) (hj : j ≤ m) :
    hammingShellAdjacency m (hammingShellMode m k) j =
      ((m : ℚ) - 2 * (k : ℚ)) * hammingShellMode m k j := by
  by_cases hm0 : m = 0
  · subst m
    have hk0 : k = 0 := Nat.eq_zero_of_le_zero hk
    have hj0 : j = 0 := Nat.eq_zero_of_le_zero hj
    subst k
    subst j
    simp [hammingShellAdjacency]
  by_cases hj0 : j = 0
  · subst j
    have hm1 : 1 ≤ m := Nat.one_le_iff_ne_zero.mpr hm0
    have hpred : m - 1 + 1 = m := Nat.sub_add_cancel hm1
    have h := hammingModeCoeff_left (m - 1) k
    simpa [hammingShellAdjacency, hammingShellMode, hpred] using h
  by_cases hjm : j = m
  · subst j
    have hm1 : 1 ≤ m := Nat.one_le_iff_ne_zero.mpr hm0
    have hpred : m - 1 + 1 = m := Nat.sub_add_cancel hm1
    have hgap : m - (m - 1) = 1 := by omega
    have h := hammingModeCoeff_right (m - 1) k
    simpa [hammingShellAdjacency, hammingShellMode, hpred, hgap] using h
  · have hjpos : 0 < j := Nat.pos_of_ne_zero hj0
    have hjlt : j < m := lt_of_le_of_ne hj hjm
    have ha1 : j - 1 + 1 = j := by omega
    have ha2 : j - 1 + 2 = j + 1 := by omega
    have hb1 : m - j - 1 + 1 = m - j := by omega
    have hb2 : m - j - 1 + 2 = m - (j - 1) := by omega
    have hright : m - (j + 1) = m - j - 1 := by omega
    have hmab : j - 1 + (m - j - 1) + 2 = m := by omega
    have h := hammingModeCoeff_interior (j - 1) (m - j - 1) k
    simpa [hammingShellAdjacency, hammingShellMode, ha1, ha2, hb1, hb2,
      hright, hmab] using h

/--
WSR-L47: the normalized Hamming-shell operator has the exact integer eigenvalue `k`.
-/
theorem hammingShellK_mode
    (m k j : ℕ) (hk : k ≤ m) (hj : j ≤ m) :
    hammingShellK m (hammingShellMode m k) j =
      (k : ℚ) * hammingShellMode m k j := by
  unfold hammingShellK
  rw [hammingShellAdjacency_mode m k j hk hj]
  ring

/-- The shell-zero value of mode `k` is exactly the binomial coefficient `m choose k`. -/
theorem hammingShellMode_zero (m k : ℕ) :
    hammingShellMode m k 0 = (Nat.choose m k : ℚ) := by
  unfold hammingShellMode hammingModeCoeff hammingBasisPoly
  simp [Polynomial.coeff_one_add_X_pow]

/-- Every mode in the physical range has nonzero shell-zero value. -/
theorem hammingShellMode_zero_ne (m k : ℕ) (hk : k ≤ m) :
    hammingShellMode m k 0 ≠ 0 := by
  rw [hammingShellMode_zero]
  exact_mod_cast (Nat.choose_pos hk).ne'

/-- Hence every physical Krawtchouk shell mode is a genuinely nonzero function. -/
theorem hammingShellMode_ne_zero (m k : ℕ) (hk : k ≤ m) :
    (hammingShellMode m k : ℕ → ℚ) ≠ 0 := by
  intro hzero
  have h0 := congrFun hzero 0
  simp only [Pi.zero_apply] at h0
  exact hammingShellMode_zero_ne m k hk h0

end EnterpriseMath.Precision
