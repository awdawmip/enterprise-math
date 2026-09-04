import Mathlib

namespace EnterpriseMath.Precision.EulerFccChiralityGluing

/-- Six `F₂` transition bits on the edges of the tetrahedral four-slice atlas.
The field order is `01,02,03,12,13,23`. -/
@[ext]
structure EdgeBits where
  e01 : Bool
  e02 : Bool
  e03 : Bool
  e12 : Bool
  e13 : Bool
  e23 : Bool
  deriving DecidableEq, Repr, Fintype

/-- Reversal choices for the four local signed chiral generators. -/
@[ext]
structure GaugeBits where
  g0 : Bool
  g1 : Bool
  g2 : Bool
  g3 : Bool
  deriving DecidableEq, Repr, Fintype

/-- The four triangular face holonomies, ordered `012,013,023,123`. -/
@[ext]
structure FaceBits where
  h012 : Bool
  h013 : Bool
  h023 : Bool
  h123 : Bool
  deriving DecidableEq, Repr, Fintype

/-- Four three-axis slices, represented by `Fin 4` for stable executable
finite enumeration under the pinned Lean toolchain. -/
abbrev Slice := Fin 4

/-- A slice together with one of the two local signs `J` and `-J`. -/
@[ext]
structure SignedSlice where
  slice : Slice
  sheet : Bool
  deriving DecidableEq, Repr, Fintype

/-- Vertices of the three-dimensional Boolean cube. -/
@[ext]
structure CubeBits where
  x : Bool
  y : Bool
  z : Bool
  deriving DecidableEq, Repr, Fintype

/-- Three-fold addition in `F₂`, represented by Boolean xor. -/
def xor3 (a b c : Bool) : Bool :=
  Bool.xor (Bool.xor a b) c

/-- Four-fold addition in `F₂`. -/
def xor4 (a b c d : Bool) : Bool :=
  Bool.xor (Bool.xor a b) (Bool.xor c d)

/-- Vertex-frame gauge action `eᵢⱼ ↦ eᵢⱼ+gᵢ+gⱼ`. -/
def gaugeAction (g : GaugeBits) (e : EdgeBits) : EdgeBits where
  e01 := xor3 e.e01 g.g0 g.g1
  e02 := xor3 e.e02 g.g0 g.g2
  e03 := xor3 e.e03 g.g0 g.g3
  e12 := xor3 e.e12 g.g1 g.g2
  e13 := xor3 e.e13 g.g1 g.g3
  e23 := xor3 e.e23 g.g2 g.g3

/-- Gauge-invariant triangle holonomies. -/
def faceHolonomy (e : EdgeBits) : FaceBits where
  h012 := xor3 e.e01 e.e02 e.e12
  h013 := xor3 e.e01 e.e03 e.e13
  h023 := xor3 e.e02 e.e03 e.e23
  h123 := xor3 e.e12 e.e13 e.e23

/-- Tetrahedral Bianchi parity: xor of all four face bits. -/
def faceParity (h : FaceBits) : Bool :=
  xor4 h.h012 h.h013 h.h023 h.h123

/-- Hamming weight of a face-holonomy vector. -/
def faceWeight (h : FaceBits) : Nat :=
  (if h.h012 then 1 else 0) +
  (if h.h013 then 1 else 0) +
  (if h.h023 then 1 else 0) +
  (if h.h123 then 1 else 0)

/-- Explicit finite list of all local slice-frame gauges. -/
def allGauges : List GaugeBits := [
  ⟨false, false, false, false⟩,
  ⟨false, false, false, true⟩,
  ⟨false, false, true, false⟩,
  ⟨false, false, true, true⟩,
  ⟨false, true, false, false⟩,
  ⟨false, true, false, true⟩,
  ⟨false, true, true, false⟩,
  ⟨false, true, true, true⟩,
  ⟨true, false, false, false⟩,
  ⟨true, false, false, true⟩,
  ⟨true, false, true, false⟩,
  ⟨true, false, true, true⟩,
  ⟨true, true, false, false⟩,
  ⟨true, true, false, true⟩,
  ⟨true, true, true, false⟩,
  ⟨true, true, true, true⟩
]

/-- Explicit finite list of the eight signed slice states. -/
def allSignedSlices : List SignedSlice := [
  ⟨0, false⟩, ⟨0, true⟩,
  ⟨1, false⟩, ⟨1, true⟩,
  ⟨2, false⟩, ⟨2, true⟩,
  ⟨3, false⟩, ⟨3, true⟩
]

/-- Executable finite vertex-gauge equivalence test. -/
def gaugeEquivalentB (e f : EdgeBits) : Bool :=
  allGauges.any (fun g => decide (gaugeAction g e = f))

/-- Two edge systems are equivalent when related by local slice-frame flips. -/
def GaugeEquivalent (e f : EdgeBits) : Prop :=
  gaugeEquivalentB e f = true

instance (e f : EdgeBits) : Decidable (GaugeEquivalent e f) := by
  unfold GaugeEquivalent
  infer_instance

/-- Executable full-face-symmetry test.  Since `S₄` acts transitively on the
four tetrahedral faces, a fixed vector has all four coordinates equal. -/
def fullySymmetricB (h : FaceBits) : Bool :=
  decide (h.h012 = h.h013 ∧ h.h013 = h.h023 ∧ h.h023 = h.h123)

/-- A face vector fixed by the full transitive permutation action on faces. -/
def FullySymmetric (h : FaceBits) : Prop :=
  fullySymmetricB h = true

instance (h : FaceBits) : Decidable (FullySymmetric h) := by
  unfold FullySymmetric
  infer_instance

/-- The trivial edge transition system. -/
def zeroEdges : EdgeBits := ⟨false, false, false, false, false, false⟩

/-- The all-negative/antibalanced edge representative. -/
def antibalancedEdges : EdgeBits := ⟨true, true, true, true, true, true⟩

/-- No local slice-frame reversals. -/
def zeroGauge : GaugeBits := ⟨false, false, false, false⟩

/-- Simultaneous reversal of all four local slice frames. -/
def globalFlip : GaugeBits := ⟨true, true, true, true⟩

/-- Componentwise complement, i.e. composition with the global flip. -/
def complementGauge (g : GaugeBits) : GaugeBits :=
  ⟨!g.g0, !g.g1, !g.g2, !g.g3⟩

/-- Flat face holonomy. -/
def zeroFaces : FaceBits := ⟨false, false, false, false⟩

/-- Odd holonomy on every tetrahedral face. -/
def allOddFaces : FaceBits := ⟨true, true, true, true⟩

/-- Existence of one globally signed chiral generator across all four slices. -/
def Globalizable (e : EdgeBits) : Prop :=
  GaugeEquivalent e zeroEdges

instance (e : EdgeBits) : Decidable (Globalizable e) := by
  unfold Globalizable
  infer_instance

/-- One representative from each antipodal pair of cube vertices. -/
def cubeBase (s : Slice) : CubeBits :=
  match s.val with
  | 0 => ⟨false, false, false⟩
  | 1 => ⟨false, true, true⟩
  | 2 => ⟨true, false, true⟩
  | _ => ⟨true, true, false⟩

/-- Central inversion on the cube. -/
def cubeComplement (p : CubeBits) : CubeBits :=
  ⟨!p.x, !p.y, !p.z⟩

/-- The explicit eight-state cube labeling of the antibalanced orientation
cover. -/
def cubeLabel (s : SignedSlice) : CubeBits :=
  match s.sheet with
  | false => cubeBase s.slice
  | true => cubeComplement (cubeBase s.slice)

/-- The deck transformation reversing the sign of the local generator. -/
def deckFlip (s : SignedSlice) : SignedSlice :=
  ⟨s.slice, !s.sheet⟩

/-- Adjacency in the all-negative signed-slice cover: move to a different
slice and reverse sheet. -/
def coverAdjacentB (a b : SignedSlice) : Bool :=
  decide (a.slice ≠ b.slice ∧ a.sheet ≠ b.sheet)

/-- Propositional cover adjacency. -/
def CoverAdjacent (a b : SignedSlice) : Prop :=
  coverAdjacentB a b = true

instance (a b : SignedSlice) : Decidable (CoverAdjacent a b) := by
  unfold CoverAdjacent
  infer_instance

/-- Convert one Boolean difference to a natural Hamming contribution. -/
def bitNat : Bool → Nat
  | false => 0
  | true => 1

/-- Hamming distance in the Boolean cube. -/
def cubeDistance (a b : CubeBits) : Nat :=
  bitNat (Bool.xor a.x b.x) +
  bitNat (Bool.xor a.y b.y) +
  bitNat (Bool.xor a.z b.z)

/-- Propositional cube-edge adjacency. -/
def CubeAdjacent (a b : CubeBits) : Prop :=
  cubeDistance a b = 1

instance (a b : CubeBits) : Decidable (CubeAdjacent a b) := by
  unfold CubeAdjacent
  infer_instance

/-- All finite tetrahedral chirality holonomies satisfy the even-parity
Bianchi identity because every edge occurs in exactly two faces. -/
theorem faceHolonomy_even :
    ∀ e : EdgeBits, faceParity (faceHolonomy e) = false := by
  native_decide

/-- Face holonomy is unchanged by local reversal of any slice frame. -/
theorem faceHolonomy_gauge_invariant :
    ∀ (e : EdgeBits) (g : GaugeBits),
      faceHolonomy (gaugeAction g e) = faceHolonomy e := by
  native_decide

/-- The four face bits are a complete invariant of the vertex-gauge action. -/
theorem equal_faceHolonomy_iff_gaugeEquivalent :
    ∀ e f : EdgeBits,
      faceHolonomy e = faceHolonomy f ↔ GaugeEquivalent e f := by
  native_decide

/-- Every even face vector is realized by an edge transition system. -/
theorem every_even_face_pattern_is_realized :
    ∀ h : FaceBits,
      faceParity h = false → ∃ e : EdgeBits, faceHolonomy e = h := by
  native_decide

/-- A single globally signed `J` exists exactly in the flat class. -/
theorem globalizable_iff_flat :
    ∀ e : EdgeBits,
      Globalizable e ↔ faceHolonomy e = zeroFaces := by
  native_decide

/-- The gauge action has exactly the two-element kernel generated by the
simultaneous global reversal. -/
theorem gauge_stabilizer_is_global_flip :
    ∀ (e : EdgeBits) (g : GaugeBits),
      gaugeAction g e = e ↔ g = zeroGauge ∨ g = globalFlip := by
  native_decide

/-- Whenever a flat system is trivialized, the trivializing frame is unique
up to simultaneous reversal of all four local generators. -/
theorem trivializing_gauges_unique_up_to_global_flip :
    ∀ (e : EdgeBits) (g h : GaugeBits),
      gaugeAction g e = zeroEdges →
      gaugeAction h e = zeroEdges →
      h = g ∨ h = complementGauge g := by
  native_decide

/-- Even tetrahedral face vectors have only weights zero, two, or four. -/
theorem even_face_weight_trichotomy :
    ∀ h : FaceBits,
      faceParity h = false →
      faceWeight h = 0 ∨ faceWeight h = 2 ∨ faceWeight h = 4 := by
  native_decide

/-- Full tetrahedral symmetry leaves only the flat and all-face-odd vectors. -/
theorem fully_symmetric_face_dichotomy :
    ∀ h : FaceBits,
      FullySymmetric h → h = zeroFaces ∨ h = allOddFaces := by
  native_decide

/-- The all-face-odd vector is the unique nonzero fully symmetric vector. -/
theorem fully_symmetric_nonflat_is_allOdd :
    ∀ h : FaceBits,
      FullySymmetric h → h ≠ zeroFaces → h = allOddFaces := by
  native_decide

/-- At the level of gauge classes, a fully symmetric transition system is
therefore either flat or the unique antibalanced class. -/
theorem fully_symmetric_edge_class_dichotomy :
    ∀ e : EdgeBits,
      FullySymmetric (faceHolonomy e) →
      GaugeEquivalent e zeroEdges ∨ GaugeEquivalent e antibalancedEdges := by
  native_decide

/-- The accepted all-negative overlap representative has odd holonomy on all
four faces. -/
theorem antibalanced_has_all_odd_face_holonomy :
    faceHolonomy antibalancedEdges = allOddFaces := by
  native_decide

/-- The all-face-odd class cannot carry one globally signed chiral generator. -/
theorem antibalanced_is_not_globalizable :
    ¬ Globalizable antibalancedEdges := by
  native_decide

/-- The eight signed slice states are exactly the eight cube vertices. -/
theorem cubeLabel_bijective : Function.Bijective cubeLabel := by
  native_decide

/-- The explicit labeling identifies the antibalanced orientation-cover graph
with the three-dimensional cube graph. -/
theorem cubeLabel_preserves_adjacency :
    ∀ a b : SignedSlice,
      CoverAdjacent a b ↔ CubeAdjacent (cubeLabel a) (cubeLabel b) := by
  native_decide

/-- Reversal of the signed generator is central inversion of the cube. -/
theorem deckFlip_is_cube_antipode :
    ∀ s : SignedSlice,
      cubeLabel (deckFlip s) = cubeComplement (cubeLabel s) := by
  native_decide

/-- The deck transformation has no fixed signed slice state. -/
theorem deckFlip_fixed_point_free :
    ∀ s : SignedSlice, deckFlip s ≠ s := by
  native_decide

/-- The orientation cover and cube both have eight vertices. -/
theorem signedSlice_card : Fintype.card SignedSlice = 8 := by
  native_decide

theorem cubeBits_card : Fintype.card CubeBits = 8 := by
  native_decide

/-- The gauge quotient has eight classes, represented by the eight even face
vectors. -/
def evenFacePatterns : Finset FaceBits :=
  Finset.univ.filter (fun h => faceParity h = false)

theorem evenFacePatterns_card : evenFacePatterns.card = 8 := by
  native_decide

/-- Exactly eight of the 64 edge assignments are flat. -/
def flatEdgeAssignments : Finset EdgeBits :=
  Finset.univ.filter (fun e => faceHolonomy e = zeroFaces)

theorem flatEdgeAssignments_card : flatEdgeAssignments.card = 8 := by
  native_decide

/-- Exactly eight edge assignments represent the all-face-odd class. -/
def allOddEdgeAssignments : Finset EdgeBits :=
  Finset.univ.filter (fun e => faceHolonomy e = allOddFaces)

theorem allOddEdgeAssignments_card : allOddEdgeAssignments.card = 8 := by
  native_decide

/-- The six intermediate face classes contain the remaining 48 edge
assignments. -/
def weightTwoEdgeAssignments : Finset EdgeBits :=
  Finset.univ.filter (fun e => faceWeight (faceHolonomy e) = 2)

theorem weightTwoEdgeAssignments_card : weightTwoEdgeAssignments.card = 48 := by
  native_decide

end EnterpriseMath.Precision.EulerFccChiralityGluing
