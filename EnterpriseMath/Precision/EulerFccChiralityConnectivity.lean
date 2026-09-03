import EnterpriseMath.Precision.EulerFccChiralityGluing

namespace EnterpriseMath.Precision.EulerFccChiralityGluing

/-- Read one unordered tetrahedral edge bit.  Diagonal pairs are assigned
`false` because they are not overlap edges. -/
def edgeBit (e : EdgeBits) : Slice → Slice → Bool
  | .s0, .s1 => e.e01
  | .s1, .s0 => e.e01
  | .s0, .s2 => e.e02
  | .s2, .s0 => e.e02
  | .s0, .s3 => e.e03
  | .s3, .s0 => e.e03
  | .s1, .s2 => e.e12
  | .s2, .s1 => e.e12
  | .s1, .s3 => e.e13
  | .s3, .s1 => e.e13
  | .s2, .s3 => e.e23
  | .s3, .s2 => e.e23
  | _, _ => false

/-- Executable adjacency in the two-sheeted orientation cover determined by
an arbitrary transition cochain. -/
def transitionCoverAdjacentB
    (e : EdgeBits) (a b : SignedSlice) : Bool :=
  decide
    (a.slice ≠ b.slice ∧
      b.sheet = Bool.xor a.sheet (edgeBit e a.slice b.slice))

/-- Propositional orientation-cover adjacency. -/
def TransitionCoverAdjacent
    (e : EdgeBits) (a b : SignedSlice) : Prop :=
  transitionCoverAdjacentB e a b = true

/-- Reachability by at most `n` cover edges. -/
def coverReachableWithin
    (e : EdgeBits) : Nat → SignedSlice → SignedSlice → Bool
  | 0, a, b => decide (a = b)
  | n + 1, a, b =>
      decide (a = b) ||
        (Finset.univ : Finset SignedSlice).any
          (fun c =>
            transitionCoverAdjacentB e a c &&
              coverReachableWithin e n c b)

/-- Every connected non-flat eight-state cover in this finite family has
diameter three, so radius-three reachability is a complete connectedness test. -/
def coverConnectedB (e : EdgeBits) : Bool :=
  decide
    (∀ a b : SignedSlice,
      coverReachableWithin e 3 a b = true)

/-- Connectedness of the signed orientation cover. -/
def CoverConnected (e : EdgeBits) : Prop :=
  coverConnectedB e = true

/-- For the all-one edge system, generic cover adjacency agrees with the
specialized opposite-sheet relation used in the cube isomorphism. -/
theorem antibalanced_generic_adjacency_eq_cube_cover :
    ∀ a b : SignedSlice,
      TransitionCoverAdjacent antibalancedEdges a b ↔ CoverAdjacent a b := by
  native_decide

/-- The trivial transition system preserves sheet and therefore produces two
disjoint copies of the tetrahedral overlap graph. -/
theorem flat_cover_adjacency_preserves_sheet :
    ∀ a b : SignedSlice,
      TransitionCoverAdjacent zeroEdges a b ↔
        a.slice ≠ b.slice ∧ a.sheet = b.sheet := by
  native_decide

/-- The orientation cover is connected exactly when the face-holonomy class is
non-flat. -/
theorem cover_connected_iff_nonflat :
    ∀ e : EdgeBits,
      CoverConnected e ↔ faceHolonomy e ≠ zeroFaces := by
  native_decide

/-- Equivalently, all 56 non-flat assignments have diameter at most three,
whereas the eight flat assignments remain disconnected. -/
theorem nonflat_reachable_within_three :
    ∀ e : EdgeBits,
      faceHolonomy e ≠ zeroFaces →
      ∀ a b : SignedSlice, coverReachableWithin e 3 a b = true := by
  native_decide

/-- The flat fully symmetric class is disconnected. -/
theorem flat_cover_not_connected :
    ¬ CoverConnected zeroEdges := by
  native_decide

/-- The all-face-odd fully symmetric class is connected. -/
theorem antibalanced_cover_connected :
    CoverConnected antibalancedEdges := by
  native_decide

/-- Full tetrahedral symmetry together with connected signed transport selects
the unique all-face-odd holonomy vector. -/
theorem full_symmetry_and_connectedness_select_allOdd :
    ∀ e : EdgeBits,
      FullySymmetric (faceHolonomy e) →
      CoverConnected e →
      faceHolonomy e = allOddFaces := by
  native_decide

/-- At gauge-class level, connectedness distinguishes the antibalanced class
from the flat class among the two fully symmetric possibilities. -/
theorem fully_symmetric_connected_iff_antibalanced :
    ∀ e : EdgeBits,
      FullySymmetric (faceHolonomy e) →
      (CoverConnected e ↔ GaugeEquivalent e antibalancedEdges) := by
  native_decide

end EnterpriseMath.Precision.EulerFccChiralityGluing
