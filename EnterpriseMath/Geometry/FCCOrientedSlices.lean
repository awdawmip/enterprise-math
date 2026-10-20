import EnterpriseMath.Geometry.FCCSliceIncidence

namespace EnterpriseMath.FCCOrientedSlices

open EnterpriseMath.FCCSliceIncidence

/-- Integral three-coordinate carrier vectors.  These are carrier readouts,
not identifications of the six native P000 axes. -/
abbrev Vec3 := Fin 3 → ℤ

/-- Dot product in the integral FCC carrier chart. -/
def dot (u v : Vec3) : ℤ :=
  u 0 * v 0 + u 1 * v 1 + u 2 * v 2

/-- Squared carrier length. -/
def normSq (v : Vec3) : ℤ := dot v v

/-- Representatives of the six unoriented FCC line families
`L₁,...,L₆`. -/
def lineVector : Line → Vec3 :=
  ![![1, 1, 0],
    ![1, -1, 0],
    ![1, 0, 1],
    ![1, 0, -1],
    ![0, 1, 1],
    ![0, 1, -1]]

/-- An ordered listing of the three line labels in each slice. -/
def sliceLineOrder : Slice → Fin 3 → Line :=
  ![![0, 2, 5],
    ![0, 3, 4],
    ![1, 2, 4],
    ![1, 3, 5]]

/-- Local orientation signs chosen so the three representatives in each
slice sum to zero. -/
def orientationSign : Slice → Fin 3 → ℤ :=
  ![![1, -1, -1],
    ![1, -1, -1],
    ![1, -1, 1],
    ![1, -1, 1]]

/-- The oriented carrier vector seen in a local three-axis slice chart. -/
def orientedVector (s : Slice) (j : Fin 3) : Vec3 :=
  fun c => orientationSign s j * lineVector (sliceLineOrder s j) c

/-- The ordered line table agrees with the incidence atlas. -/
theorem sliceLineOrder_mem (s : Slice) (j : Fin 3) :
    sliceLineOrder s j ∈ sliceLines s := by
  fin_cases s <;> fin_cases j <;> native_decide

/-- Every oriented local representative has the same squared carrier length. -/
theorem orientedVector_normSq (s : Slice) (j : Fin 3) :
    normSq (orientedVector s j) = 2 := by
  fin_cases s <;> fin_cases j <;> native_decide

/-- The three oriented vectors in every slice close exactly. -/
theorem orientedSlice_sum_zero (s : Slice) :
    (fun c => orientedVector s 0 c + orientedVector s 1 c +
      orientedVector s 2 c) = 0 := by
  funext c
  fin_cases s <;> fin_cases c <;> native_decide

/-- Distinct local axes have dot product `-1`; together with squared length
`2`, this is the exact algebraic `120°` certificate. -/
theorem orientedVector_dot_of_ne (s : Slice) (i j : Fin 3) (h : i ≠ j) :
    dot (orientedVector s i) (orientedVector s j) = -1 := by
  fin_cases s <;> fin_cases i <;> fin_cases j <;> simp_all <;> native_decide

/-- The local chart has no repeated line label. -/
theorem sliceLineOrder_injective (s : Slice) :
    Function.Injective (sliceLineOrder s) := by
  intro i j h
  fin_cases s <;> fin_cases i <;> fin_cases j <;>
    simp_all [sliceLineOrder]

end EnterpriseMath.FCCOrientedSlices
