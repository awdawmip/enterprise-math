import EnterpriseMath.Geometry.FCCSliceIncidence

namespace EnterpriseMath.PrecisionPi.FCCSliceAngles

open FCCSliceIncidence

abbrev CarrierVec := Fin 3 → ℤ

def canonicalLine : Line → CarrierVec :=
  ![![1, 1, 0],
    ![1, -1, 0],
    ![1, 0, 1],
    ![1, 0, -1],
    ![0, 1, 1],
    ![0, 1, -1]]

def sliceLineOrder : Slice → Fin 3 → Line :=
  ![![0, 2, 5],
    ![0, 3, 4],
    ![1, 2, 4],
    ![1, 3, 5]]

def sliceSign : Slice → Fin 3 → ℤ :=
  ![![1, -1, -1],
    ![1, -1, -1],
    ![1, -1, 1],
    ![1, -1, 1]]

def orientedSliceVector (s : Slice) (i : Fin 3) : CarrierVec :=
  fun c => sliceSign s i * canonicalLine (sliceLineOrder s i) c

theorem line_mem_slice_iff_exists_local_index :
    ∀ s : Slice, ∀ l : Line,
      l ∈ sliceLines s ↔ ∃ i : Fin 3, sliceLineOrder s i = l := by
  native_decide

def dot (x y : CarrierVec) : ℤ :=
  x 0 * y 0 + x 1 * y 1 + x 2 * y 2

def normSq (x : CarrierVec) : ℤ := dot x x

theorem oriented_normSq_two :
    ∀ s : Slice, ∀ i : Fin 3,
      normSq (orientedSliceVector s i) = 2 := by
  native_decide

theorem oriented_pairwise_dot_neg_one :
    ∀ s : Slice, ∀ i j : Fin 3, i ≠ j →
      dot (orientedSliceVector s i) (orientedSliceVector s j) = -1 := by
  native_decide

theorem oriented_slice_sum_zero :
    ∀ s : Slice, ∀ c : Fin 3,
      orientedSliceVector s 0 c +
        orientedSliceVector s 1 c +
        orientedSliceVector s 2 c = 0 := by
  native_decide

/-- Equal norm and dot product `-1` give the normalized cosine `-1/2`. -/
theorem oriented_120_certificate
    (s : Slice) (i j : Fin 3) (hij : i ≠ j) :
    normSq (orientedSliceVector s i) = 2 ∧
      normSq (orientedSliceVector s j) = 2 ∧
      2 * dot (orientedSliceVector s i) (orientedSliceVector s j) = -2 := by
  refine ⟨oriented_normSq_two s i, oriented_normSq_two s j, ?_⟩
  rw [oriented_pairwise_dot_neg_one s i j hij]
  norm_num

end EnterpriseMath.PrecisionPi.FCCSliceAngles
