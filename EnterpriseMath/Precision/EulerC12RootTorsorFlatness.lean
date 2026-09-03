import Mathlib

namespace EnterpriseMath.Precision.EulerC12RootTorsorFlatness

/-! ## Fixed cyclic carriers -/

abbrev C2 := Fin 2
abbrev C3 := Fin 3
abbrev C4 := Fin 4
abbrev C6 := Fin 6
abbrev C12 := Fin 12

def c2 (n : ℕ) : C2 := ⟨n % 2, by omega⟩
def c3 (n : ℕ) : C3 := ⟨n % 3, by omega⟩
def c4 (n : ℕ) : C4 := ⟨n % 4, by omega⟩
def c6 (n : ℕ) : C6 := ⟨n % 6, by omega⟩
def c12 (n : ℕ) : C12 := ⟨n % 12, by omega⟩

def add6 (x y : C6) : C6 := c6 (x.val + y.val)
def add12 (x y : C12) : C12 := c12 (x.val + y.val)
def neg12 (x : C12) : C12 := c12 (12 - x.val)
def nsmul12 (n : ℕ) (x : C12) : C12 := c12 (n * x.val)

def reduce12To6 (x : C12) : C6 := c6 x.val
def reduce4To2 (x : C4) : C2 := c2 x.val

def crt6 (x : C6) : C3 × C2 := (c3 x.val, c2 x.val)
def crt6Inv (x : C3 × C2) : C6 := c6 (4 * x.1.val + 3 * x.2.val)

def crt12 (x : C12) : C3 × C4 := (c3 x.val, c4 x.val)
def crt12Inv (x : C3 × C4) : C12 := c12 (4 * x.1.val + 9 * x.2.val)

theorem crt6_left_inverse : ∀ x : C6, crt6Inv (crt6 x) = x := by
  native_decide

theorem crt6_right_inverse : ∀ x : C3 × C2, crt6 (crt6Inv x) = x := by
  native_decide

theorem crt12_left_inverse : ∀ x : C12, crt12Inv (crt12 x) = x := by
  native_decide

theorem crt12_right_inverse : ∀ x : C3 × C4, crt12 (crt12Inv x) = x := by
  native_decide

/-- Under CRT, `C12 -> C6` is `id_C3 × (C4 -> C2)`. -/
theorem root_cover_crt_compatibility : ∀ x : C12,
    crt6 (reduce12To6 x) = ((crt12 x).1, reduce4To2 (crt12 x).2) := by
  native_decide

theorem reduce12To6_add : ∀ x y : C12,
    reduce12To6 (add12 x y) = add6 (reduce12To6 x) (reduce12To6 y) := by
  native_decide

theorem root_cover_kernel : ∀ x : C12,
    reduce12To6 x = c6 0 ↔ x = c12 0 ∨ x = c12 6 := by
  native_decide

theorem root_cover_surjective : ∀ x : C6, ∃ y : C12, reduce12To6 y = x := by
  native_decide

/-- A homomorphic section would have to send the generator of `C6` to such a
    point.  No such point exists, which is the generator criterion for the
    non-splitting of `C12 -> C6`. -/
theorem no_generator_section :
    ¬ ∃ q : C12,
      reduce12To6 q = c6 1 ∧ nsmul12 6 q = c12 0 := by
  native_decide

/-! ## The quarter-turn root torsor -/

/-- Bit zero is one quarter-turn root and bit one is its inverse. -/
def quarterRoot (sign : Bool) : C12 :=
  if sign then c12 9 else c12 3

/-- Transport across a sign-changing overlap applies inversion. -/
def transportRoot (edgeSign : Bool) (root : C12) : C12 :=
  if edgeSign then neg12 root else root

theorem quarter_roots_exhaustive : ∀ q : C12,
    add12 q q = c12 6 ↔ q = c12 3 ∨ q = c12 9 := by
  native_decide

theorem quarter_root_reduces_to_half_turn : ∀ sign : Bool,
    reduce12To6 (quarterRoot sign) = c6 3 := by
  native_decide

theorem quarter_root_doubles_to_half_turn : ∀ sign : Bool,
    add12 (quarterRoot sign) (quarterRoot sign) = c12 6 := by
  native_decide

theorem inversion_exchanges_quarter_roots : ∀ sign : Bool,
    neg12 (quarterRoot sign) = quarterRoot (!sign) := by
  native_decide

theorem no_inversion_fixed_quarter_root : ∀ sign : Bool,
    neg12 (quarterRoot sign) ≠ quarterRoot sign := by
  native_decide

theorem root_transport_sign_law : ∀ source target : Bool,
    transportRoot (Bool.xor source target) (quarterRoot source) = quarterRoot target := by
  native_decide

/-- The chirality-even half-turn endpoint is independent of the chosen root. -/
theorem projective_half_turn_endpoint : ∀ edgeSign sign : Bool,
    add12
        (transportRoot edgeSign (quarterRoot sign))
        (transportRoot edgeSign (quarterRoot sign)) = c12 6 := by
  native_decide

/-! ## Four-slice tetrahedral atlas over `F2` -/

@[ext]
structure VertexBits where
  a : Bool
  b : Bool
  c : Bool
  d : Bool
  deriving DecidableEq, Fintype

@[ext]
structure EdgeBits where
  ab : Bool
  ac : Bool
  ad : Bool
  bc : Bool
  bd : Bool
  cd : Bool
  deriving DecidableEq, Fintype

@[ext]
structure HolonomyCode where
  abc : Bool
  abd : Bool
  acd : Bool
  deriving DecidableEq, Fintype

/-- Local frame changes induce overlap signs by endpoint xor. -/
def coboundary (v : VertexBits) : EdgeBits :=
  ⟨Bool.xor v.a v.b,
   Bool.xor v.a v.c,
   Bool.xor v.a v.d,
   Bool.xor v.b v.c,
   Bool.xor v.b v.d,
   Bool.xor v.c v.d⟩

def edgeXor (x y : EdgeBits) : EdgeBits :=
  ⟨Bool.xor x.ab y.ab,
   Bool.xor x.ac y.ac,
   Bool.xor x.ad y.ad,
   Bool.xor x.bc y.bc,
   Bool.xor x.bd y.bd,
   Bool.xor x.cd y.cd⟩

def vertexFlip (v : VertexBits) : VertexBits :=
  ⟨!v.a, !v.b, !v.c, !v.d⟩

def faceABC (e : EdgeBits) : Bool := Bool.xor (Bool.xor e.ab e.ac) e.bc
def faceABD (e : EdgeBits) : Bool := Bool.xor (Bool.xor e.ab e.ad) e.bd
def faceACD (e : EdgeBits) : Bool := Bool.xor (Bool.xor e.ac e.ad) e.cd
def faceBCD (e : EdgeBits) : Bool := Bool.xor (Bool.xor e.bc e.bd) e.cd

def holonomyCode (e : EdgeBits) : HolonomyCode :=
  ⟨faceABC e, faceABD e, faceACD e⟩

def Flat (e : EdgeBits) : Prop :=
  faceABC e = false ∧
  faceABD e = false ∧
  faceACD e = false ∧
  faceBCD e = false

def Globalizable (e : EdgeBits) : Prop :=
  ∃ v : VertexBits, coboundary v = e

def GaugeEquivalent (x y : EdgeBits) : Prop :=
  ∃ v : VertexBits, y = edgeXor x (coboundary v)

/-- Gauge-fix the root on slice `A` and reconstruct the other three signs. -/
def reconstruct (e : EdgeBits) : VertexBits :=
  ⟨false, e.ab, e.ac, e.ad⟩

theorem fourth_face_is_sum_of_first_three : ∀ e : EdgeBits,
    faceBCD e = Bool.xor (Bool.xor (faceABC e) (faceABD e)) (faceACD e) := by
  native_decide

theorem coboundary_is_flat : ∀ v : VertexBits, Flat (coboundary v) := by
  native_decide

theorem reconstructs_every_flat_system : ∀ e : EdgeBits,
    Flat e → coboundary (reconstruct e) = e := by
  native_decide

/-- Flatness on the filled tetrahedral atlas is equivalent to the existence of
    one signed global quarter-turn root. -/
theorem flat_iff_globalizable : ∀ e : EdgeBits,
    Flat e ↔ Globalizable e := by
  native_decide

/-- Two vertex lifts of the same overlap system differ only by overall root
    reversal. -/
theorem global_lift_unique_up_to_reversal : ∀ v w : VertexBits,
    coboundary v = coboundary w ↔ w = v ∨ w = vertexFlip v := by
  native_decide

theorem overall_reversal_preserves_transitions : ∀ v : VertexBits,
    coboundary (vertexFlip v) = coboundary v := by
  native_decide

theorem overall_reversal_is_nontrivial : ∀ v : VertexBits,
    vertexFlip v ≠ v := by
  native_decide

/-- The three faces adjacent to `A` give a complete gauge invariant on the
    one-skeleton `K4`. -/
theorem holonomy_classifies_gauge_orbits : ∀ x y : EdgeBits,
    GaugeEquivalent x y ↔ holonomyCode x = holonomyCode y := by
  native_decide

/-- Every triple of face holonomies occurs; therefore the obstruction space
    has exactly three independent bits. -/
theorem holonomy_code_surjective : ∀ h : HolonomyCode,
    ∃ e : EdgeBits, holonomyCode e = h := by
  native_decide

/-! ## Root transport around faces -/

def transportABC (e : EdgeBits) (root : C12) : C12 :=
  transportRoot e.ac (transportRoot e.bc (transportRoot e.ab root))

def transportABD (e : EdgeBits) (root : C12) : C12 :=
  transportRoot e.ad (transportRoot e.bd (transportRoot e.ab root))

def transportACD (e : EdgeBits) (root : C12) : C12 :=
  transportRoot e.ad (transportRoot e.cd (transportRoot e.ac root))

def transportBCD (e : EdgeBits) (root : C12) : C12 :=
  transportRoot e.bd (transportRoot e.cd (transportRoot e.bc root))

theorem abc_transport_detects_holonomy : ∀ e : EdgeBits, ∀ sign : Bool,
    transportABC e (quarterRoot sign) =
      quarterRoot (Bool.xor sign (faceABC e)) := by
  native_decide

theorem abd_transport_detects_holonomy : ∀ e : EdgeBits, ∀ sign : Bool,
    transportABD e (quarterRoot sign) =
      quarterRoot (Bool.xor sign (faceABD e)) := by
  native_decide

theorem acd_transport_detects_holonomy : ∀ e : EdgeBits, ∀ sign : Bool,
    transportACD e (quarterRoot sign) =
      quarterRoot (Bool.xor sign (faceACD e)) := by
  native_decide

theorem bcd_transport_detects_holonomy : ∀ e : EdgeBits, ∀ sign : Bool,
    transportBCD e (quarterRoot sign) =
      quarterRoot (Bool.xor sign (faceBCD e)) := by
  native_decide

/-- A non-flat face flips the signed root, but the doubled/half-turn endpoint
    remains the same. -/
theorem face_holonomy_cannot_change_projective_endpoint : ∀ e : EdgeBits,
    ∀ sign : Bool,
    add12 (transportABC e (quarterRoot sign))
          (transportABC e (quarterRoot sign)) = c12 6 := by
  native_decide

end EnterpriseMath.Precision.EulerC12RootTorsorFlatness
