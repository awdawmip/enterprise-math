import Mathlib

namespace EnterpriseMath.EulerRotation.TetrahedralOrientationLocalSystem

/-- Three-coordinate carrier vector used only for the exact tetrahedral
orientation calculation. -/
@[ext]
structure Vec3 (R : Type*) where
  x : R
  y : R
  z : R
  deriving DecidableEq

namespace Vec3

variable {R : Type*} [CommRing R]

/-- Scalar multiplication in carrier coordinates. -/
def scale (a : R) (v : Vec3 R) : Vec3 R :=
  ⟨a * v.x, a * v.y, a * v.z⟩

/-- Additive reversal. -/
def neg (v : Vec3 R) : Vec3 R :=
  ⟨-v.x, -v.y, -v.z⟩

/-- Carrier dot product. -/
def dot (u v : Vec3 R) : R :=
  u.x * v.x + u.y * v.y + u.z * v.z

/-- Carrier cross product. -/
def cross (u v : Vec3 R) : Vec3 R :=
  ⟨u.y * v.z - u.z * v.y,
   u.z * v.x - u.x * v.z,
   u.x * v.y - u.y * v.x⟩

/-- An orientation-preserving cyclic coordinate permutation. -/
def cyclic (v : Vec3 R) : Vec3 R :=
  ⟨v.z, v.x, v.y⟩

/-- The determinant-positive half turn about the first coordinate axis. -/
def halfTurnX (v : Vec3 R) : Vec3 R :=
  ⟨v.x, -v.y, -v.z⟩

/-- The determinant-negative reflection interchanging the first two coordinates. -/
def swapXY (v : Vec3 R) : Vec3 R :=
  ⟨v.y, v.x, v.z⟩

@[simp]
theorem scale_scale (a b : R) (v : Vec3 R) :
    scale a (scale b v) = scale (a * b) v := by
  ext <;> simp [scale] <;> ring

@[simp]
theorem cross_scale_right (u v : Vec3 R) (a : R) :
    cross u (scale a v) = scale a (cross u v) := by
  ext <;> simp [cross, scale] <;> ring

@[simp]
theorem cross_antisymm (u v : Vec3 R) :
    cross v u = neg (cross u v) := by
  ext <;> simp [cross, neg] <;> ring

/-- Coordinate form of `n × (n × v) = n(n·v) - (n·n)v`. -/
theorem cross_cross (n v : Vec3 R) :
    cross n (cross n v) =
      ⟨n.x * dot n v - dot n n * v.x,
       n.y * dot n v - dot n n * v.y,
       n.z * dot n v - dot n n * v.z⟩ := by
  ext <;> simp [cross, dot] <;> ring

/-- For a normal of squared norm three, the cross operator squares to `-3`
on its perpendicular slice plane. -/
theorem cross_cross_on_slice
    (n v : Vec3 R)
    (hperp : dot n v = 0)
    (hnorm : dot n n = 3) :
    cross n (cross n v) = scale (-3) v := by
  rw [cross_cross]
  ext <;> simp [scale, hperp, hnorm]

/-- Positive cyclic coordinate transport preserves the cross product. -/
theorem cyclic_cross (u v : Vec3 R) :
    cyclic (cross u v) = cross (cyclic u) (cyclic v) := by
  ext <;> simp [cyclic, cross] <;> ring

/-- The determinant-positive half turn preserves the cross product. -/
theorem halfTurnX_cross (u v : Vec3 R) :
    halfTurnX (cross u v) = cross (halfTurnX u) (halfTurnX v) := by
  ext <;> simp [halfTurnX, cross] <;> ring

/-- The determinant-negative coordinate reflection reverses the cross product. -/
theorem swapXY_cross (u v : Vec3 R) :
    swapXY (cross u v) = neg (cross (swapXY u) (swapXY v)) := by
  ext <;> simp [swapXY, cross, neg] <;> ring

end Vec3

open Vec3

/-- The four regular-tetrahedral slice normals. -/
def nA : Vec3 ℤ := ⟨1, 1, 1⟩
def nB : Vec3 ℤ := ⟨1, -1, -1⟩
def nC : Vec3 ℤ := ⟨-1, 1, -1⟩
def nD : Vec3 ℤ := ⟨-1, -1, 1⟩

@[simp] theorem cyclic_nA : cyclic nA = nA := by rfl
@[simp] theorem cyclic_nB : cyclic nB = nC := by rfl
@[simp] theorem cyclic_nC : cyclic nC = nD := by rfl
@[simp] theorem cyclic_nD : cyclic nD = nB := by rfl

@[simp] theorem halfTurnX_nA : halfTurnX nA = nB := by rfl
@[simp] theorem halfTurnX_nB : halfTurnX nB = nA := by rfl
@[simp] theorem halfTurnX_nC : halfTurnX nC = nD := by rfl
@[simp] theorem halfTurnX_nD : halfTurnX nD = nC := by rfl

@[simp] theorem swapXY_nA : swapXY nA = nA := by rfl
@[simp] theorem swapXY_nB : swapXY nB = nC := by rfl
@[simp] theorem swapXY_nC : swapXY nC = nB := by rfl
@[simp] theorem swapXY_nD : swapXY nD = nD := by rfl

@[simp] theorem dot_nA_nA : dot nA nA = 3 := by norm_num [dot, nA]
@[simp] theorem dot_nB_nB : dot nB nB = 3 := by norm_num [dot, nB]
@[simp] theorem dot_nC_nC : dot nC nC = 3 := by norm_num [dot, nC]
@[simp] theorem dot_nD_nD : dot nD nD = 3 := by norm_num [dot, nD]

@[simp] theorem dot_nA_nB : dot nA nB = -1 := by norm_num [dot, nA, nB]
@[simp] theorem dot_nA_nC : dot nA nC = -1 := by norm_num [dot, nA, nC]
@[simp] theorem dot_nA_nD : dot nA nD = -1 := by norm_num [dot, nA, nD]
@[simp] theorem dot_nB_nC : dot nB nC = -1 := by norm_num [dot, nB, nC]
@[simp] theorem dot_nB_nD : dot nB nD = -1 := by norm_num [dot, nB, nD]
@[simp] theorem dot_nC_nD : dot nC nD = -1 := by norm_num [dot, nC, nD]

/-- Normalized chiral cross operator. The scale parameter is kept explicit so
that the finite algebra is independent of a particular square-root API. -/
def normalizedCross (s : ℝ) (n v : Vec3 ℝ) : Vec3 ℝ :=
  scale (1 / s) (cross n v)

/-- Squared-norm-three slice normals yield a complex structure after the
unique square-root normalization. -/
theorem normalizedCross_sq_on_slice
    (s : ℝ)
    (n v : Vec3 ℝ)
    (hs0 : s ≠ 0)
    (hs : s ^ 2 = 3)
    (hperp : dot n v = 0)
    (hnorm : dot n n = 3) :
    normalizedCross s n (normalizedCross s n v) = neg v := by
  have hcross : cross n (cross n v) = scale (-3) v :=
    cross_cross_on_slice n v hperp hnorm
  unfold normalizedCross
  rw [cross_scale_right, scale_scale, hcross, scale_scale]
  have hcoef : (1 / s) * (1 / s) * (-3 : ℝ) = -1 := by
    field_simp [hs0]
    nlinarith [hs]
  rw [hcoef]
  ext <;> simp [scale, neg]

/-- Orientation-preserving cyclic transport intertwines the normalized local
Euler generators. -/
theorem cyclic_normalizedCross
    (s : ℝ) (n v : Vec3 ℝ) :
    cyclic (normalizedCross s n v) =
      normalizedCross s (cyclic n) (cyclic v) := by
  ext <;> simp [normalizedCross, scale, cyclic, cross] <;> ring

/-- The determinant-positive tetrahedral half turn also intertwines the local
Euler generators. -/
theorem halfTurnX_normalizedCross
    (s : ℝ) (n v : Vec3 ℝ) :
    halfTurnX (normalizedCross s n v) =
      normalizedCross s (halfTurnX n) (halfTurnX v) := by
  ext <;> simp [normalizedCross, scale, halfTurnX, cross] <;> ring

/-- The determinant-negative tetrahedral reflection anti-intertwines the
local Euler generators. -/
theorem swapXY_normalizedCross
    (s : ℝ) (n v : Vec3 ℝ) :
    swapXY (normalizedCross s n v) =
      neg (normalizedCross s (swapXY n) (swapXY v)) := by
  ext <;> simp [normalizedCross, scale, swapXY, cross, neg] <;> ring

/-- At the actual Cell normalization, every squared-norm-three slice normal
carries a genuine complex structure. -/
theorem cellNormalizedCross_sq_on_slice
    (n v : Vec3 ℝ)
    (hperp : dot n v = 0)
    (hnorm : dot n n = 3) :
    normalizedCross (Real.sqrt 3) n
        (normalizedCross (Real.sqrt 3) n v) = neg v := by
  apply normalizedCross_sq_on_slice (Real.sqrt 3) n v
  · positivity
  · simpa using Real.sq_sqrt (show (0 : ℝ) ≤ 3 by norm_num)
  · exact hperp
  · exact hnorm

end EnterpriseMath.EulerRotation.TetrahedralOrientationLocalSystem
