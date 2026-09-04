import Mathlib

namespace EnterpriseMath.EulerRotation.NativeAtlasOrientationObstruction

abbrev F2 := ZMod 2

/-- The six overlap-orientation bits in edge order 01, 02, 03, 12, 13, 23. -/
@[ext]
structure EdgeBits where
  e01 : F2
  e02 : F2
  e03 : F2
  e12 : F2
  e13 : F2
  e23 : F2
  deriving DecidableEq

/-- Parities of four local chart-frame changes. -/
@[ext]
structure VertexBits where
  a0 : F2
  a1 : F2
  a2 : F2
  a3 : F2
  deriving DecidableEq

/-- Change overlap parity by the endpoint frame parities. -/
def gauge (e : EdgeBits) (a : VertexBits) : EdgeBits :=
  ⟨e.e01 + a.a0 + a.a1,
   e.e02 + a.a0 + a.a2,
   e.e03 + a.a0 + a.a3,
   e.e12 + a.a1 + a.a2,
   e.e13 + a.a1 + a.a3,
   e.e23 + a.a2 + a.a3⟩

/-- The zero overlap-orientation field. -/
def zeroEdge : EdgeBits := ⟨0, 0, 0, 0, 0, 0⟩

/-- Independent triangle orientation holonomies. -/
def triangle012 (e : EdgeBits) : F2 := e.e01 + e.e12 + e.e02
def triangle013 (e : EdgeBits) : F2 := e.e01 + e.e13 + e.e03
def triangle023 (e : EdgeBits) : F2 := e.e02 + e.e23 + e.e03

def triangle123 (e : EdgeBits) : F2 := e.e12 + e.e23 + e.e13

/-- A constructive frame gauge based at vertex zero. -/
def reductionGauge (e : EdgeBits) : VertexBits :=
  ⟨0, e.e01, e.e02, e.e03⟩

/-- Triangle orientation parity is invariant under vertex-frame changes. -/
theorem triangle012_gauge (e : EdgeBits) (a : VertexBits) :
    triangle012 (gauge e a) = triangle012 e := by
  simp [triangle012, gauge]
  ring

theorem triangle013_gauge (e : EdgeBits) (a : VertexBits) :
    triangle013 (gauge e a) = triangle013 e := by
  simp [triangle013, gauge]
  ring

theorem triangle023_gauge (e : EdgeBits) (a : VertexBits) :
    triangle023 (gauge e a) = triangle023 e := by
  simp [triangle023, gauge]
  ring

/-- The fourth triangle is the sum of the chosen three independent cycles. -/
theorem triangle123_dependency (e : EdgeBits) :
    triangle123 e = triangle012 e + triangle013 e + triangle023 e := by
  simp [triangle123, triangle012, triangle013, triangle023]
  ring

/-- Vanishing independent triangle holonomies give an explicit gauge in which
all overlap transitions are orientation preserving. -/
theorem reductionGauge_clears
    (e : EdgeBits)
    (h012 : triangle012 e = 0)
    (h013 : triangle013 e = 0)
    (h023 : triangle023 e = 0) :
    gauge e (reductionGauge e) = zeroEdge := by
  apply EdgeBits.ext
  · simp [gauge, reductionGauge, zeroEdge]
    ring
  · simp [gauge, reductionGauge, zeroEdge]
    ring
  · simp [gauge, reductionGauge, zeroEdge]
    ring
  · simp [gauge, reductionGauge, zeroEdge]
    linear_combination h012
  · simp [gauge, reductionGauge, zeroEdge]
    linear_combination h013
  · simp [gauge, reductionGauge, zeroEdge]
    linear_combination h023

/-- The three triangle tests are exactly the obstruction to reducing the
four-chart transition parities to the all-even field. -/
theorem flat_iff_exists_clearing_gauge (e : EdgeBits) :
    (triangle012 e = 0 ∧ triangle013 e = 0 ∧ triangle023 e = 0) ↔
      ∃ a : VertexBits, gauge e a = zeroEdge := by
  constructor
  · rintro ⟨h012, h013, h023⟩
    exact ⟨reductionGauge e, reductionGauge_clears e h012 h013 h023⟩
  · rintro ⟨a, ha⟩
    constructor
    · rw [← triangle012_gauge e a, ha]
      rfl
    constructor
    · rw [← triangle013_gauge e a, ha]
      rfl
    · rw [← triangle023_gauge e a, ha]
      rfl

/-- Two clearing gauges differ by one global frame-reversal bit. -/
theorem clearing_gauges_differ_globally
    (e : EdgeBits)
    (a b : VertexBits)
    (ha : gauge e a = zeroEdge)
    (hb : gauge e b = zeroEdge) :
    b.a1 - a.a1 = b.a0 - a.a0 ∧
    b.a2 - a.a2 = b.a0 - a.a0 ∧
    b.a3 - a.a3 = b.a0 - a.a0 := by
  have h01a := congrArg EdgeBits.e01 ha
  have h01b := congrArg EdgeBits.e01 hb
  have h02a := congrArg EdgeBits.e02 ha
  have h02b := congrArg EdgeBits.e02 hb
  have h03a := congrArg EdgeBits.e03 ha
  have h03b := congrArg EdgeBits.e03 hb
  simp [gauge, zeroEdge] at h01a h01b h02a h02b h03a h03b
  constructor
  · linear_combination h01b - h01a
  constructor
  · linear_combination h02b - h02a
  · linear_combination h03b - h03a

end EnterpriseMath.EulerRotation.NativeAtlasOrientationObstruction
