import EnterpriseMath.Geometry.FCCSliceIncidence

namespace EnterpriseMath.PrecisionPi.FCCSliceRotation

open FCCSliceIncidence

def rotate3Slice : Slice → Slice := ![1, 2, 0, 3]
def rotate3SliceInv : Slice → Slice := ![2, 0, 1, 3]
def rotate3Line : Line → Line := ![4, 5, 0, 1, 2, 3]
def rotate3LineInv : Line → Line := ![2, 3, 4, 5, 0, 1]

def rotate4Slice : Slice → Slice := ![1, 2, 3, 0]
def rotate4SliceInv : Slice → Slice := ![3, 0, 1, 2]
def rotate4Line : Line → Line := ![4, 5, 3, 2, 1, 0]
def rotate4LineInv : Line → Line := ![5, 4, 3, 2, 0, 1]

theorem rotate3Slice_inverse_left : ∀ s : Slice,
    rotate3SliceInv (rotate3Slice s) = s := by native_decide

theorem rotate3Slice_inverse_right : ∀ s : Slice,
    rotate3Slice (rotate3SliceInv s) = s := by native_decide

theorem rotate4Slice_inverse_left : ∀ s : Slice,
    rotate4SliceInv (rotate4Slice s) = s := by native_decide

theorem rotate4Slice_inverse_right : ∀ s : Slice,
    rotate4Slice (rotate4SliceInv s) = s := by native_decide

theorem rotate3Line_inverse_left : ∀ l : Line,
    rotate3LineInv (rotate3Line l) = l := by native_decide

theorem rotate3Line_inverse_right : ∀ l : Line,
    rotate3Line (rotate3LineInv l) = l := by native_decide

theorem rotate4Line_inverse_left : ∀ l : Line,
    rotate4LineInv (rotate4Line l) = l := by native_decide

theorem rotate4Line_inverse_right : ∀ l : Line,
    rotate4Line (rotate4LineInv l) = l := by native_decide

theorem rotate3_incidence_equivariant :
    ∀ s : Slice, ∀ l : Line,
      l ∈ sliceLines s ↔ rotate3Line l ∈ sliceLines (rotate3Slice s) := by
  native_decide

theorem rotate4_incidence_equivariant :
    ∀ s : Slice, ∀ l : Line,
      l ∈ sliceLines s ↔ rotate4Line l ∈ sliceLines (rotate4Slice s) := by
  native_decide

theorem rotate3_incidentSlices :
    ∀ l : Line, ∀ s : Slice,
      s ∈ incidentSlices l ↔
        rotate3Slice s ∈ incidentSlices (rotate3Line l) := by
  native_decide

theorem rotate4_incidentSlices :
    ∀ l : Line, ∀ s : Slice,
      s ∈ incidentSlices l ↔
        rotate4Slice s ∈ incidentSlices (rotate4Line l) := by
  native_decide

theorem rotate3_commonLines :
    ∀ s t : Slice, ∀ l : Line,
      l ∈ commonLines s t ↔
        rotate3Line l ∈ commonLines (rotate3Slice s) (rotate3Slice t) := by
  native_decide

theorem rotate4_commonLines :
    ∀ s t : Slice, ∀ l : Line,
      l ∈ commonLines s t ↔
        rotate4Line l ∈ commonLines (rotate4Slice s) (rotate4Slice t) := by
  native_decide

end EnterpriseMath.PrecisionPi.FCCSliceRotation
