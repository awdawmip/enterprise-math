import Mathlib

namespace EnterpriseMath.EulerRotation.TetrahedralTransportHolonomy

/-- Exact rational three-vector used for the tetrahedral transport certificate. -/
@[ext]
structure Vec3 where
  x : ℚ
  y : ℚ
  z : ℚ
  deriving DecidableEq, Repr

/-- Exact rational three-by-three matrix. -/
@[ext]
structure Mat3 where
  a11 : ℚ
  a12 : ℚ
  a13 : ℚ
  a21 : ℚ
  a22 : ℚ
  a23 : ℚ
  a31 : ℚ
  a32 : ℚ
  a33 : ℚ
  deriving DecidableEq, Repr

/-- Matrix-vector multiplication. -/
def mulVec (A : Mat3) (v : Vec3) : Vec3 :=
  ⟨A.a11 * v.x + A.a12 * v.y + A.a13 * v.z,
   A.a21 * v.x + A.a22 * v.y + A.a23 * v.z,
   A.a31 * v.x + A.a32 * v.y + A.a33 * v.z⟩

/-- Matrix multiplication. -/
def mul (A B : Mat3) : Mat3 :=
  ⟨A.a11 * B.a11 + A.a12 * B.a21 + A.a13 * B.a31,
   A.a11 * B.a12 + A.a12 * B.a22 + A.a13 * B.a32,
   A.a11 * B.a13 + A.a12 * B.a23 + A.a13 * B.a33,
   A.a21 * B.a11 + A.a22 * B.a21 + A.a23 * B.a31,
   A.a21 * B.a12 + A.a22 * B.a22 + A.a23 * B.a32,
   A.a21 * B.a13 + A.a22 * B.a23 + A.a23 * B.a33,
   A.a31 * B.a11 + A.a32 * B.a21 + A.a33 * B.a31,
   A.a31 * B.a12 + A.a32 * B.a22 + A.a33 * B.a32,
   A.a31 * B.a13 + A.a32 * B.a23 + A.a33 * B.a33⟩

/-- Matrix transpose. -/
def transpose (A : Mat3) : Mat3 :=
  ⟨A.a11, A.a21, A.a31,
   A.a12, A.a22, A.a32,
   A.a13, A.a23, A.a33⟩

/-- Matrix negation. -/
def neg (A : Mat3) : Mat3 :=
  ⟨-A.a11, -A.a12, -A.a13,
   -A.a21, -A.a22, -A.a23,
   -A.a31, -A.a32, -A.a33⟩

/-- Vector negation. -/
def vneg (v : Vec3) : Vec3 := ⟨-v.x, -v.y, -v.z⟩

/-- Exact determinant. -/
def det (A : Mat3) : ℚ :=
  A.a11 * (A.a22 * A.a33 - A.a23 * A.a32)
  - A.a12 * (A.a21 * A.a33 - A.a23 * A.a31)
  + A.a13 * (A.a21 * A.a32 - A.a22 * A.a31)

/-- Identity matrix. -/
def I3 : Mat3 :=
  ⟨1, 0, 0,
   0, 1, 0,
   0, 0, 1⟩

/-- Three vertices of one oriented face of the tetrahedral normal set. -/
def n0 : Vec3 := ⟨1, 1, 1⟩
def n1 : Vec3 := ⟨1, -1, -1⟩
def n2 : Vec3 := ⟨-1, 1, -1⟩

/-- Shared-line vectors based at the first normal. -/
def c01 : Vec3 := ⟨0, 2, -2⟩
def c02 : Vec3 := ⟨-2, 0, 2⟩
def c03 : Vec3 := ⟨2, -2, 0⟩

/-- Proper shortest transports along the base oriented normal face. -/
def A01 : Mat3 :=
  ⟨-(1/3 : ℚ), 2/3, 2/3,
   -2/3, 1/3, -2/3,
   -2/3, -2/3, 1/3⟩

def A12 : Mat3 :=
  ⟨1/3, 2/3, 2/3,
   2/3, 1/3, -2/3,
   -2/3, 2/3, -(1/3 : ℚ)⟩

def A20 : Mat3 :=
  ⟨1/3, 2/3, -2/3,
   -2/3, -(1/3 : ℚ), -2/3,
   -2/3, 2/3, 1/3⟩

/-- Inverses of the three proper transports. -/
def A10 : Mat3 := transpose A01
def A21 : Mat3 := transpose A12
def A02 : Mat3 := transpose A20

/-- Half-turn about the first tetrahedral normal. -/
def Q0 : Mat3 :=
  ⟨-(1/3 : ℚ), 2/3, 2/3,
   2/3, -(1/3 : ℚ), 2/3,
   2/3, 2/3, -(1/3 : ℚ)⟩

/-- Unnormalized chiral cross-product matrix for `n0`. -/
def D0 : Mat3 :=
  ⟨0, -1, 1,
   1, 0, -1,
   -1, 1, 0⟩

/-- Mirror bridges along the same face. -/
def H01 : Mat3 :=
  ⟨1, 0, 0,
   0, 0, -1,
   0, -1, 0⟩

def H12 : Mat3 :=
  ⟨0, 1, 0,
   1, 0, 0,
   0, 0, 1⟩

def H20 : Mat3 :=
  ⟨0, 0, -1,
   0, 1, 0,
   -1, 0, 0⟩

/-- The mirror triangle composite at the first normal. -/
def K0 : Mat3 := H12

/-- The first proper bridge maps the first normal to the second. -/
theorem A01_maps_normal : mulVec A01 n0 = n1 := by
  native_decide

/-- The second proper bridge maps the second normal to the third. -/
theorem A12_maps_normal : mulVec A12 n1 = n2 := by
  native_decide

/-- The third proper bridge closes the face. -/
theorem A20_maps_normal : mulVec A20 n2 = n0 := by
  native_decide

/-- The first proper bridge fixes the shared line pointwise. -/
theorem A01_fixes_shared_axis : mulVec A01 c01 = c01 := by
  native_decide

/-- Proper bridges are exactly orthogonal in this certificate. -/
theorem A01_orthogonal : mul (transpose A01) A01 = I3 := by
  native_decide

theorem A12_orthogonal : mul (transpose A12) A12 = I3 := by
  native_decide

theorem A20_orthogonal : mul (transpose A20) A20 = I3 := by
  native_decide

/-- Proper bridges have determinant one. -/
theorem A01_det : det A01 = 1 := by
  native_decide

theorem A12_det : det A12 = 1 := by
  native_decide

theorem A20_det : det A20 = 1 := by
  native_decide

/-- The first two proper transports simplify to an exact coordinate half-turn. -/
theorem first_two_transport_product :
    mul A12 A01 =
      ⟨-1, 0, 0,
       0, 1, 0,
       0, 0, -1⟩ := by
  native_decide

/-- Exact tetrahedral face holonomy: a half-turn about `n0`. -/
theorem base_face_holonomy : mul A20 (mul A12 A01) = Q0 := by
  native_decide

/-- The face holonomy is an involution. -/
theorem Q0_sq : mul Q0 Q0 = I3 := by
  native_decide

/-- The face holonomy is a proper rotation. -/
theorem Q0_det : det Q0 = 1 := by
  native_decide

/-- The based face normal is fixed. -/
theorem Q0_fixes_normal : mulVec Q0 n0 = n0 := by
  native_decide

/-- Every shared oriented line in the starting slice is reversed. -/
theorem Q0_reverses_c01 : mulVec Q0 c01 = vneg c01 := by
  native_decide

theorem Q0_reverses_c02 : mulVec Q0 c02 = vneg c02 := by
  native_decide

theorem Q0_reverses_c03 : mulVec Q0 c03 = vneg c03 := by
  native_decide

/-- The unnormalized chiral operator squares to `-3` on the slice directions. -/
theorem D0_sq_c01 : mulVec (mul D0 D0) c01 =
    ⟨-3 * c01.x, -3 * c01.y, -3 * c01.z⟩ := by
  native_decide

theorem D0_sq_c02 : mulVec (mul D0 D0) c02 =
    ⟨-3 * c02.x, -3 * c02.y, -3 * c02.z⟩ := by
  native_decide

theorem D0_sq_c03 : mulVec (mul D0 D0) c03 =
    ⟨-3 * c03.x, -3 * c03.y, -3 * c03.z⟩ := by
  native_decide

/-- Proper face holonomy is complex-linear: it commutes with the chiral skew. -/
theorem Q0_commutes_D0 : mul Q0 D0 = mul D0 Q0 := by
  native_decide

/-- The three mirror bridges have determinant minus one. -/
theorem H01_det : det H01 = -1 := by
  native_decide

theorem H12_det : det H12 = -1 := by
  native_decide

theorem H20_det : det H20 = -1 := by
  native_decide

/-- The mirror face composite is a tangent reflection, not a phase rotation. -/
theorem mirror_face_holonomy : mul H20 (mul H12 H01) = K0 := by
  native_decide

/-- The mirror loop reverses the local chiral operator. -/
theorem mirror_face_anticommutes_D0 :
    mul K0 (mul D0 K0) = neg D0 := by
  native_decide

/-- Exact rational part of the spherical cosine-law certificate. -/
theorem spherical_vertex_cosine :
    (((-(1/3 : ℚ)) - (-(1/3 : ℚ)) ^ 2) /
      (1 - (-(1/3 : ℚ)) ^ 2)) = -(1/2 : ℚ) := by
  norm_num

end EnterpriseMath.EulerRotation.TetrahedralTransportHolonomy
