import EnterpriseMath.Precision.HammingReflection
import Mathlib.LinearAlgebra.Eigenspace.Basic
import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas
import Mathlib.LinearAlgebra.Pi

namespace EnterpriseMath.Precision

/-- Finite-dimensional permutation-invariant Hamming shell space. -/
abbrev HammingShellFinSpace (m : ℕ) := Fin (m + 1) → ℚ

/-- Coordinate immediately to the left, with natural-number truncation at zero. -/
def hammingPrevProjection (m : ℕ) (j : Fin (m + 1)) :
    HammingShellFinSpace m →ₗ[ℚ] ℚ :=
  LinearMap.proj ⟨j.val - 1, by omega⟩

/-- Coordinate immediately to the right; at the top shell the coefficient multiplying it is zero. -/
def hammingNextProjection (m : ℕ) (j : Fin (m + 1)) :
    HammingShellFinSpace m →ₗ[ℚ] ℚ :=
  if h : j.val < m then
    LinearMap.proj ⟨j.val + 1, by omega⟩
  else
    LinearMap.proj j

/-- Genuine finite-dimensional Hamming-shell adjacency endomorphism. -/
noncomputable def hammingShellAdjacencyFin (m : ℕ) :
    Module.End ℚ (HammingShellFinSpace m) :=
  LinearMap.pi fun j =>
    (j.val : ℚ) • hammingPrevProjection m j +
      ((m - j.val : ℕ) : ℚ) • hammingNextProjection m j

/-- Genuine finite-dimensional normalized shell operator `K_m=(mI-A_m)/2`. -/
noncomputable def hammingShellKFin (m : ℕ) :
    Module.End ℚ (HammingShellFinSpace m) :=
  (2 : ℚ)⁻¹ •
    ((m : ℚ) • LinearMap.id - hammingShellAdjacencyFin m)

/-- Restriction of the natural Krawtchouk shell mode to the physical shell coordinates. -/
noncomputable def hammingShellModeFin (m k : ℕ) : HammingShellFinSpace m :=
  fun j => hammingShellMode m k j.val

/-- Pointwise formula for the finite Hamming adjacency operator. -/
theorem hammingShellAdjacencyFin_apply
    (m : ℕ) (f : HammingShellFinSpace m) (j : Fin (m + 1)) :
    hammingShellAdjacencyFin m f j =
      (j.val : ℚ) * f ⟨j.val - 1, by omega⟩ +
        ((m - j.val : ℕ) : ℚ) *
          (if h : j.val < m then f ⟨j.val + 1, by omega⟩ else f j) := by
  simp [hammingShellAdjacencyFin, hammingPrevProjection, hammingNextProjection,
    LinearMap.pi_apply, LinearMap.proj_apply, LinearMap.smul_apply, smul_eq_mul]

/-- Pointwise formula for the normalized finite Hamming operator. -/
theorem hammingShellKFin_apply
    (m : ℕ) (f : HammingShellFinSpace m) (j : Fin (m + 1)) :
    hammingShellKFin m f j =
      ((m : ℚ) * f j - hammingShellAdjacencyFin m f j) / 2 := by
  simp [hammingShellKFin, LinearMap.smul_apply, LinearMap.sub_apply,
    LinearMap.id_apply, smul_eq_mul, div_eq_mul_inv]
  ring

/-- The finite adjacency operator carries the restricted mode with eigenvalue `m-2k`. -/
theorem hammingShellAdjacencyFin_mode
    (m k : ℕ) (hk : k ≤ m) :
    hammingShellAdjacencyFin m (hammingShellModeFin m k) =
      ((m : ℚ) - 2 * (k : ℚ)) • hammingShellModeFin m k := by
  ext j
  have hj : j.val ≤ m := by omega
  have hnat := hammingShellAdjacency_mode m k j.val hk hj
  rw [hammingShellAdjacencyFin_apply]
  by_cases hlt : j.val < m
  · simpa [hammingShellModeFin, hammingShellAdjacency, hlt, Pi.smul_apply,
      smul_eq_mul] using hnat
  · have heq : j.val = m := by omega
    simpa [hammingShellModeFin, hammingShellAdjacency, hlt, heq, Pi.smul_apply,
      smul_eq_mul] using hnat

/-- The genuine finite-dimensional operator has exact eigenvalue `k` on mode `k`. -/
theorem hammingShellKFin_mode
    (m k : ℕ) (hk : k ≤ m) :
    hammingShellKFin m (hammingShellModeFin m k) =
      (k : ℚ) • hammingShellModeFin m k := by
  ext j
  rw [hammingShellKFin_apply]
  have hA := congrFun (hammingShellAdjacencyFin_mode m k hk) j
  simp only [Pi.smul_apply, smul_eq_mul] at hA ⊢
  rw [hA]
  ring

/-- Every physical finite Krawtchouk mode is nonzero. -/
theorem hammingShellModeFin_ne_zero
    (m k : ℕ) (hk : k ≤ m) :
    hammingShellModeFin m k ≠ 0 := by
  intro hzero
  have h0 := congrFun hzero ⟨0, by omega⟩
  simp only [Pi.zero_apply] at h0
  exact hammingShellMode_zero_ne m k hk (by simpa [hammingShellModeFin] using h0)

/-- Each physical finite mode is a genuine eigenvector of the finite shell endomorphism. -/
theorem hammingShellKFin_hasEigenvector
    (m k : ℕ) (hk : k ≤ m) :
    (hammingShellKFin m).HasEigenvector (k : ℚ) (hammingShellModeFin m k) := by
  exact ⟨Module.End.mem_eigenspace_iff.mpr (hammingShellKFin_mode m k hk),
    hammingShellModeFin_ne_zero m k hk⟩

/-- Distinct integer eigenvalues make the full finite Krawtchouk family linearly independent. -/
theorem hammingShellModeFin_linearIndependent (m : ℕ) :
    LinearIndependent ℚ (fun k : Fin (m + 1) => hammingShellModeFin m k.val) := by
  apply (hammingShellKFin m).eigenvectors_linearIndependent'
    (fun k : Fin (m + 1) => (k.val : ℚ))
  · intro a b hab
    norm_cast at hab
    exact Fin.ext hab
  · intro k
    exact hammingShellKFin_hasEigenvector m k.val (by omega)

/-- The Krawtchouk modes form a basis of the full finite Hamming shell space. -/
noncomputable def hammingKrawtchoukBasis (m : ℕ) :
    Basis (Fin (m + 1)) ℚ (HammingShellFinSpace m) :=
  basisOfPiSpaceOfLinearIndependent (hammingShellModeFin_linearIndependent m)

@[simp]
theorem hammingKrawtchoukBasis_apply (m : ℕ) (k : Fin (m + 1)) :
    hammingKrawtchoukBasis m k = hammingShellModeFin m k.val := by
  simp [hammingKrawtchoukBasis, coe_basisOfPiSpaceOfLinearIndependent]

end EnterpriseMath.Precision
