import Mathlib

namespace EnterpriseMath.EulerRotation.FccChiralTransportObstruction

abbrev VertexBits := Fin 4 → Bool
abbrev EdgeBits := Fin 6 → Bool
abbrev FaceBits := Fin 4 → Bool
abbrev RootDefect := Fin 3 → Bool

def xor3 (a b c : Bool) : Bool :=
  Bool.xor (Bool.xor a b) c

def xor4 (a b c d : Bool) : Bool :=
  Bool.xor (Bool.xor a b) (Bool.xor c d)

def edgeU : Fin 6 → Fin 4 :=
  ![0, 0, 0, 1, 1, 2]

def edgeV : Fin 6 → Fin 4 :=
  ![1, 2, 3, 2, 3, 3]

def coboundary (g : VertexBits) : EdgeBits :=
  fun e => Bool.xor (g (edgeU e)) (g (edgeV e))

def gaugeTransform (e : EdgeBits) (g : VertexBits) : EdgeBits :=
  fun k => Bool.xor (e k) (coboundary g k)

def holonomy (e : EdgeBits) : FaceBits :=
  ![
    xor3 (e 0) (e 1) (e 3),
    xor3 (e 0) (e 2) (e 4),
    xor3 (e 1) (e 2) (e 5),
    xor3 (e 3) (e 4) (e 5)
  ]

def evenFacePattern (h : FaceBits) : Prop :=
  xor4 (h 0) (h 1) (h 2) (h 3) = false

def IsFlat (e : EdgeBits) : Prop :=
  holonomy e = fun _ => false

def AllFacesFrustrated (e : EdgeBits) : Prop :=
  holonomy e = fun _ => true

def rootDefect (e : EdgeBits) : RootDefect :=
  ![holonomy e 0, holonomy e 1, holonomy e 2]

def xorEdges (e r : EdgeBits) : EdgeBits :=
  fun k => Bool.xor (e k) (r k)

def treeFlat (a b c : Bool) : EdgeBits :=
  ![
    a,
    b,
    c,
    Bool.xor a b,
    Bool.xor a c,
    Bool.xor b c
  ]

def flatPart (e : EdgeBits) : EdgeBits :=
  treeFlat (e 0) (e 1) (e 2)

def rootNormalForm (e : EdgeBits) : EdgeBits :=
  xorEdges e (flatPart e)

def complementVertices (g : VertexBits) : VertexBits :=
  fun i => !(g i)

def edgeWeight (e : EdgeBits) : Nat :=
  ((Finset.univ : Finset (Fin 6)).filter fun i => e i = true).card

def faceWeight (h : FaceBits) : Nat :=
  ((Finset.univ : Finset (Fin 4)).filter fun i => h i = true).card

def repairs (e : EdgeBits) : Finset EdgeBits :=
  (Finset.univ : Finset EdgeBits).filter fun r => IsFlat (xorEdges e r)

def conjugatePhase (z : Int × Int) : Int × Int :=
  (z.1, -z.2)

def transportPhase (b : Bool) (z : Int × Int) : Int × Int :=
  if b then conjugatePhase z else z

def transportWinding (b : Bool) (w : Int) : Int :=
  if b then -w else w

def facePhaseMonodromy (e : EdgeBits) (f : Fin 4) (z : Int × Int) : Int × Int :=
  transportPhase (holonomy e f) z

def faceWindingMonodromy (e : EdgeBits) (f : Fin 4) (w : Int) : Int :=
  transportWinding (holonomy e f) w

def SignedWindingGlobalizes (e : EdgeBits) : Prop :=
  ∀ f : Fin 4, faceWindingMonodromy e f 1 = 1

def QuarterTurnGlobalizes (e : EdgeBits) : Prop :=
  ∀ f : Fin 4, facePhaseMonodromy e f (0, 1) = (0, 1)

def HalfTurnEndpointGlobalizes (e : EdgeBits) : Prop :=
  ∀ f : Fin 4, facePhaseMonodromy e f (-1, 0) = (-1, 0)

/-- The four triangular chirality defects always have even parity. -/
theorem curvature_even :
    ∀ e : EdgeBits, evenFacePattern (holonomy e) := by
  native_decide

/-- Independent local sign changes do not alter triangle holonomy. -/
theorem holonomy_gauge_invariant :
    ∀ e : EdgeBits, ∀ g : VertexBits,
      holonomy (gaugeTransform e g) = holonomy e := by
  native_decide

/-- Every even face-frustration pattern occurs. -/
theorem curvature_surjective_onto_even_patterns :
    ∀ h : FaceBits,
      evenFacePattern h ↔ ∃ e : EdgeBits, holonomy e = h := by
  native_decide

/-- Every curvature class contains exactly eight raw edge connections. -/
theorem curvature_fiber_cardinality :
    ∀ h : FaceBits,
      evenFacePattern h →
      ((Finset.univ : Finset EdgeBits).filter fun e => holonomy e = h).card = 8 := by
  native_decide

/-- Exactly eight of the sixty-four edge connections are flat. -/
theorem flat_connection_cardinality :
    ((Finset.univ : Finset EdgeBits).filter IsFlat).card = 8 := by
  native_decide

/-- Flatness is exactly the existence of a vertex-potential trivialization. -/
theorem flat_iff_exact :
    ∀ e : EdgeBits,
      IsFlat e ↔ ∃ g : VertexBits, e = coboundary g := by
  native_decide

/-- A flat potential is unique modulo one simultaneous global sign reversal. -/
theorem flat_potential_unique_up_to_global_flip :
    ∀ g h : VertexBits,
      coboundary g = coboundary h →
      g = h ∨ g = complementVertices h := by
  native_decide

/-- Three rooted tree signs have one and only one flat extension. -/
theorem tree_flat_is_flat :
    ∀ a b c : Bool, IsFlat (treeFlat a b c) := by
  native_decide

theorem flat_reconstructed_from_root_tree :
    ∀ e : EdgeBits,
      IsFlat e →
      e = treeFlat (e 0) (e 1) (e 2) := by
  native_decide

/-- Every gauge class has a unique representative on the three non-tree chords. -/
theorem root_normal_form_formula :
    ∀ e : EdgeBits,
      rootNormalForm e =
      ![
        false,
        false,
        false,
        holonomy e 0,
        holonomy e 1,
        holonomy e 2
      ] := by
  native_decide

/-- The three rooted triangle defects completely classify gauge orbits. -/
theorem root_defect_complete :
    ∀ e f : EdgeBits,
      rootDefect e = rootDefect f ↔
      ∃ g : VertexBits, gaugeTransform e g = f := by
  native_decide

/-- The effective eight-element gauge group acts transitively on flat connections. -/
theorem flat_connections_form_one_gauge_orbit :
    ∀ e f : EdgeBits,
      IsFlat e → IsFlat f →
      ∃ g : VertexBits, gaugeTransform e g = f := by
  native_decide

/-- No flat connection is fixed by every independent local-frame change. -/
theorem no_flat_connection_is_gauge_canonical :
    ∀ e : EdgeBits,
      IsFlat e →
      ∃ g : VertexBits, gaugeTransform e g ≠ e := by
  native_decide

/-- A two-face defect has one unique one-edge correction. -/
theorem two_face_defect_unique_one_edge_repair :
    ∀ e : EdgeBits,
      faceWeight (holonomy e) = 2 →
      ∃! r : EdgeBits,
        edgeWeight r = 1 ∧ IsFlat (xorEdges e r) := by
  native_decide

/-- A fully frustrated connection cannot be repaired by zero or one edge flip. -/
theorem fully_frustrated_requires_two_edge_flips :
    ∀ e r : EdgeBits,
      AllFacesFrustrated e →
      edgeWeight r ≤ 1 →
      ¬ IsFlat (xorEdges e r) := by
  native_decide

/-- A fully frustrated connection has exactly three minimum two-edge repairs. -/
theorem fully_frustrated_has_three_two_edge_repairs :
    ∀ e : EdgeBits,
      AllFacesFrustrated e →
      ((Finset.univ : Finset EdgeBits).filter fun r =>
        edgeWeight r = 2 ∧ IsFlat (xorEdges e r)).card = 3 := by
  native_decide

/-- The real/even Euler coordinate is insensitive to chirality transport. -/
theorem transportPhase_real_fixed (b : Bool) (z : Int × Int) :
    (transportPhase b z).1 = z.1 := by
  cases b <;> rfl

/-- The half-turn endpoint is fixed even under complex conjugation. -/
theorem half_turn_fixed_by_any_transport (b : Bool) :
    transportPhase b (-1, 0) = (-1, 0) := by
  cases b <;> rfl

/-- A quarter-turn detects the chirality sign exactly. -/
theorem quarter_turn_fixed_iff_sign_trivial (b : Bool) :
    transportPhase b (0, 1) = (0, 1) ↔ b = false := by
  cases b <;> decide

/-- Every edge connection globally preserves the Euler half-turn endpoint. -/
theorem half_turn_endpoint_always_globalizes :
    ∀ e : EdgeBits, HalfTurnEndpointGlobalizes e := by
  native_decide

/-- A signed quarter-turn globalizes exactly for a flat chirality connection. -/
theorem quarter_turn_globalizes_iff_flat :
    ∀ e : EdgeBits, QuarterTurnGlobalizes e ↔ IsFlat e := by
  native_decide

/-- Nonzero signed winding has precisely the same flatness obstruction. -/
theorem signed_winding_globalizes_iff_flat :
    ∀ e : EdgeBits, SignedWindingGlobalizes e ↔ IsFlat e := by
  native_decide

end EnterpriseMath.EulerRotation.FccChiralTransportObstruction
