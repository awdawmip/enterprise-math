import Mathlib

namespace EnterpriseMath.EulerRotation.FccO2ChiralityGlobalization

/-- Sign conventions on the four FCC carrier slices. -/
@[ext]
structure VertexGauge where
  a : Bool
  b : Bool
  c : Bool
  d : Bool
  deriving DecidableEq, Fintype

/-- Chirality-preserving/reversing handoff bits on AB, AC, AD, BC, BD, CD. -/
@[ext]
structure EdgeCochain where
  ab : Bool
  ac : Bool
  ad : Bool
  bc : Bool
  bd : Bool
  cd : Bool
  deriving DecidableEq, Fintype

/-- Three independent triangle holonomies. -/
@[ext]
structure HolonomyCode where
  abc : Bool
  abd : Bool
  acd : Bool
  deriving DecidableEq, Fintype

/-- The vertex-gauge coboundary on the six shared line families. -/
def coboundary (s : VertexGauge) : EdgeCochain :=
  ⟨s.a ^^ s.b, s.a ^^ s.c, s.a ^^ s.d,
   s.b ^^ s.c, s.b ^^ s.d, s.c ^^ s.d⟩

/-- Pointwise addition in the F₂ edge-cochain space. -/
def edgeAdd (x y : EdgeCochain) : EdgeCochain :=
  ⟨x.ab ^^ y.ab, x.ac ^^ y.ac, x.ad ^^ y.ad,
   x.bc ^^ y.bc, x.bd ^^ y.bd, x.cd ^^ y.cd⟩

/-- Change local signs in the four slice charts. -/
def gaugeTransform (e : EdgeCochain) (s : VertexGauge) : EdgeCochain :=
  edgeAdd e (coboundary s)

/-- The three independent K₄ triangle holonomies. -/
def holonomyCode (e : EdgeCochain) : HolonomyCode :=
  ⟨e.ab ^^ e.ac ^^ e.bc,
   e.ab ^^ e.ad ^^ e.bd,
   e.ac ^^ e.ad ^^ e.cd⟩

/-- The fourth triangle holonomy. -/
def bcdHolonomy (e : EdgeCochain) : Bool :=
  e.bc ^^ e.bd ^^ e.cd

/-- Gauge equivalence of chirality handoff systems. -/
def GaugeEquivalent (left right : EdgeCochain) : Prop :=
  ∃ s : VertexGauge, gaugeTransform left s = right

instance (left right : EdgeCochain) : Decidable (GaugeEquivalent left right) :=
  inferInstance

/-- All local sign choices that trivialize one edge-sign system. -/
def trivializations (e : EdgeCochain) : Finset VertexGauge :=
  Finset.univ.filter fun s => coboundary s = e

/-- The fourth triangle value is the sum of the chosen three. -/
theorem fourth_triangle_dependency :
    ∀ e : EdgeCochain,
      bcdHolonomy e =
        (holonomyCode e).abc ^^ (holonomyCode e).abd ^^ (holonomyCode e).acd := by
  native_decide

/-- Triangle holonomies are unchanged by every vertex sign gauge. -/
theorem holonomy_gauge_invariant :
    ∀ (e : EdgeCochain) (s : VertexGauge),
      holonomyCode (gaugeTransform e s) = holonomyCode e := by
  native_decide

/-- The three triangle values completely classify the 64 edge systems modulo gauge. -/
theorem holonomy_complete_invariant :
    ∀ left right : EdgeCochain,
      GaugeEquivalent left right ↔ holonomyCode left = holonomyCode right := by
  native_decide

/-- A global signed generator exists exactly in the zero-holonomy class. -/
theorem global_signed_generator_iff :
    ∀ e : EdgeCochain,
      (∃ s : VertexGauge, coboundary s = e) ↔
        holonomyCode e = ⟨false, false, false⟩ := by
  native_decide

/-- A trivial chirality class has exactly two global sign choices; every other class has none. -/
theorem global_chirality_is_two_element_torsor :
    ∀ e : EdgeCochain,
      (trivializations e).card =
        if holonomyCode e = ⟨false, false, false⟩ then 2 else 0 := by
  native_decide

/-- Every vertex-gauge orbit contains eight of the 64 edge systems. -/
theorem gauge_orbit_card :
    ∀ e : EdgeCochain,
      (Finset.univ.image fun s : VertexGauge => gaugeTransform e s).card = 8 := by
  native_decide

section AbstractO2

variable {G : Type*} [CommGroup G]

/-- A chirality-preserving handoff fixes a phase; a reversing handoff inverts it. -/
def chiralityTransport (flip : Bool) (z : G) : G :=
  if flip then z⁻¹ else z

/-- Finite/abstract O(2) multiplication on `G ⋊ C₂`. -/
def o2Mul (left right : G × Bool) : G × Bool :=
  (left.1 * chiralityTransport left.2 right.1, left.2 ^^ right.2)

/-- Every order-two phase is fixed by chirality reversal. -/
theorem involutive_phase_fixed_by_chirality
    (h : G) (hh : h * h = 1) :
    ∀ flip : Bool, chiralityTransport flip h = h := by
  have hinv : h⁻¹ = h := by
    calc
      h⁻¹ = h⁻¹ * 1 := by simp
      _ = h⁻¹ * (h * h) := by rw [hh]
      _ = h := by group
  intro flip
  cases flip <;> simp [chiralityTransport, hinv]

/-- Identity is fixed by every chirality handoff. -/
theorem identity_fixed_by_chirality :
    ∀ flip : Bool, chiralityTransport flip (1 : G) = 1 := by
  intro flip
  cases flip <;> simp [chiralityTransport]

/-- The orientation-reversal phase is central in the semidirect O(2) completion. -/
theorem involutive_rotation_central
    (h : G) (hh : h * h = 1) :
    ∀ state : G × Bool,
      o2Mul (h, false) state = o2Mul state (h, false) := by
  have hfixed := involutive_phase_fixed_by_chirality h hh
  rintro ⟨z, flip⟩
  cases flip <;> simp [o2Mul, chiralityTransport, hfixed, mul_comm]

end AbstractO2

/-- In the complex character circle, the Euler half-turn `-1` is fixed by every
chirality-preserving or chirality-reversing slice handoff. -/
theorem complex_euler_halfTurn_descends :
    ∀ flip : Bool,
      chiralityTransport flip (-1 : ℂ) = -1 := by
  apply involutive_phase_fixed_by_chirality
  norm_num

/-- The same half-turn is central in the full rotation/reflection semidirect product. -/
theorem complex_euler_halfTurn_central :
    ∀ state : ℂ × Bool,
      o2Mul ((-1 : ℂ), false) state = o2Mul state ((-1 : ℂ), false) := by
  apply involutive_rotation_central
  norm_num

end EnterpriseMath.EulerRotation.FccO2ChiralityGlobalization
