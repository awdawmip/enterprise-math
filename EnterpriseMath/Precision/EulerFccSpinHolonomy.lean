import Mathlib

namespace EnterpriseMath.Precision.EulerFccSpinHolonomy

/-- The four close-packed FCC slice charts. -/
inductive Slice
  | A | B | C | D
  deriving DecidableEq, Repr

/-- Exact carrier three-vector. -/
@[ext]
structure Vec3 where
  x : ℚ
  y : ℚ
  z : ℚ
  deriving DecidableEq, Repr

def vadd (a b : Vec3) : Vec3 :=
  ⟨a.x + b.x, a.y + b.y, a.z + b.z⟩

def vneg (a : Vec3) : Vec3 :=
  ⟨-a.x, -a.y, -a.z⟩

def vsub (a b : Vec3) : Vec3 :=
  vadd a (vneg b)

def vscale (c : ℚ) (a : Vec3) : Vec3 :=
  ⟨c * a.x, c * a.y, c * a.z⟩

def dot (a b : Vec3) : ℚ :=
  a.x * b.x + a.y * b.y + a.z * b.z

def cross (a b : Vec3) : Vec3 :=
  ⟨a.y * b.z - a.z * b.y,
   a.z * b.x - a.x * b.z,
   a.x * b.y - a.y * b.x⟩

def det3 (a b c : Vec3) : ℚ :=
  dot a (cross b c)

/-- The oriented tetrahedral normal frame of the four FCC slices. -/
def normal : Slice → Vec3
  | .A => ⟨-1, 1, 1⟩
  | .B => ⟨1, -1, 1⟩
  | .C => ⟨1, 1, -1⟩
  | .D => ⟨-1, -1, -1⟩

/-- The oriented shared FCC line from `source` to `target`. -/
def sharedLine (source target : Slice) : Vec3 :=
  vscale (1 / 2) (cross (normal source) (normal target))

theorem normal_norm_sq (s : Slice) :
    dot (normal s) (normal s) = 3 := by
  cases s <;> norm_num [normal, dot]

theorem normal_pair_dot
    (source target : Slice)
    (h : source ≠ target) :
    dot (normal source) (normal target) = -1 := by
  cases source <;> cases target <;> simp_all [normal, dot]

theorem normals_sum_zero :
    vadd (vadd (normal .A) (normal .B))
      (vadd (normal .C) (normal .D)) = ⟨0, 0, 0⟩ := by
  ext <;> norm_num [normal, vadd]

theorem sharedLine_reverse (source target : Slice) :
    sharedLine target source = vneg (sharedLine source target) := by
  cases source <;> cases target <;>
    ext <;> norm_num [sharedLine, normal, cross, vscale, vneg]

theorem sharedLine_norm_sq
    (source target : Slice)
    (h : source ≠ target) :
    dot (sharedLine source target) (sharedLine source target) = 2 := by
  cases source <;> cases target <;>
    simp_all [sharedLine, normal, cross, vscale, dot]

/-- The three outgoing shared-line representatives from each slice sum to zero. -/
theorem outgoing_sum_A :
    vadd (vadd (sharedLine .A .B) (sharedLine .A .C))
      (sharedLine .A .D) = ⟨0, 0, 0⟩ := by
  ext <;> norm_num [sharedLine, normal, cross, vscale, vadd]

theorem outgoing_sum_B :
    vadd (vadd (sharedLine .B .A) (sharedLine .B .C))
      (sharedLine .B .D) = ⟨0, 0, 0⟩ := by
  ext <;> norm_num [sharedLine, normal, cross, vscale, vadd]

theorem outgoing_sum_C :
    vadd (vadd (sharedLine .C .A) (sharedLine .C .B))
      (sharedLine .C .D) = ⟨0, 0, 0⟩ := by
  ext <;> norm_num [sharedLine, normal, cross, vscale, vadd]

theorem outgoing_sum_D :
    vadd (vadd (sharedLine .D .A) (sharedLine .D .B))
      (sharedLine .D .C) = ⟨0, 0, 0⟩ := by
  ext <;> norm_num [sharedLine, normal, cross, vscale, vadd]

/-- At one slice, any two distinct outgoing shared lines have dot product `-1`. -/
theorem outgoing_pair_dot
    (source target₁ target₂ : Slice)
    (h₁ : source ≠ target₁)
    (h₂ : source ≠ target₂)
    (h₁₂ : target₁ ≠ target₂) :
    dot (sharedLine source target₁) (sharedLine source target₂) = -1 := by
  cases source <;> cases target₁ <;> cases target₂ <;>
    simp_all [sharedLine, normal, cross, vscale, dot]

/-- Exact proper rotation across one shared FCC line. -/
def transition (source target : Slice) (v : Vec3) : Vec3 :=
  let ell := sharedLine source target
  vscale (1 / 3)
    (vadd
      (vadd (vneg v) (vscale (2 * dot ell v) ell))
      (vscale 2 (cross ell v)))

theorem transition_normal
    (source target : Slice)
    (h : source ≠ target) :
    transition source target (normal source) = normal target := by
  cases source <;> cases target <;>
    simp_all [transition, sharedLine, normal, cross, dot, vscale, vadd, vneg] <;>
    ext <;> norm_num

theorem transition_sharedLine
    (source target : Slice)
    (h : source ≠ target) :
    transition source target (sharedLine source target) =
      sharedLine source target := by
  cases source <;> cases target <;>
    simp_all [transition, sharedLine, normal, cross, dot, vscale, vadd, vneg] <;>
    ext <;> norm_num

theorem transition_inverse
    (source target : Slice)
    (h : source ≠ target)
    (v : Vec3) :
    transition target source (transition source target v) = v := by
  cases source <;> cases target <;>
    simp_all [transition, sharedLine, normal, cross, dot, vscale, vadd, vneg] <;>
    ext <;> ring

theorem transition_preserves_dot
    (source target : Slice)
    (h : source ≠ target)
    (v w : Vec3) :
    dot (transition source target v) (transition source target w) = dot v w := by
  cases source <;> cases target <;>
    simp_all [transition, sharedLine, normal, cross, dot, vscale, vadd, vneg] <;>
    ring

/-- The local cross-product complex structures are transported by conjugation. -/
theorem transition_intertwines_chirality
    (source target : Slice)
    (h : source ≠ target)
    (v : Vec3) :
    transition source target (cross (normal source) v) =
      cross (normal target) (transition source target v) := by
  cases source <;> cases target <;>
    simp_all [transition, sharedLine, normal, cross, dot, vscale, vadd, vneg] <;>
    ext <;> ring

/-- Half-turn around one slice normal. -/
def halfTurn (source : Slice) (v : Vec3) : Vec3 :=
  vsub (vscale ((2 / 3) * dot (normal source) v) (normal source)) v

/-- Transport around one ordered triangular slice loop. -/
def faceTransport (source middle target : Slice) (v : Vec3) : Vec3 :=
  transition target source
    (transition middle target (transition source middle v))

theorem face_transport_eq_halfTurn
    (source middle target : Slice)
    (h₁ : source ≠ middle)
    (h₂ : middle ≠ target)
    (h₃ : target ≠ source)
    (v : Vec3) :
    faceTransport source middle target v = halfTurn source v := by
  cases source <;> cases middle <;> cases target <;>
    simp_all [faceTransport, halfTurn, transition, sharedLine, normal,
      cross, dot, vscale, vadd, vneg, vsub] <;>
    ext <;> ring

theorem halfTurn_negates_slice
    (source : Slice)
    (v : Vec3)
    (hv : dot (normal source) v = 0) :
    halfTurn source v = vneg v := by
  ext <;> simp [halfTurn, vsub, vadd, vscale, vneg, hv]

theorem face_transport_negates_slice
    (source middle target : Slice)
    (h₁ : source ≠ middle)
    (h₂ : middle ≠ target)
    (h₃ : target ≠ source)
    (v : Vec3)
    (hv : dot (normal source) v = 0) :
    faceTransport source middle target v = vneg v := by
  rw [face_transport_eq_halfTurn source middle target h₁ h₂ h₃ v]
  exact halfTurn_negates_slice source v hv

/-- Exact quaternion coordinates used only for the spin lift. -/
@[ext]
structure Quat where
  w : ℚ
  x : ℚ
  y : ℚ
  z : ℚ
  deriving DecidableEq, Repr

def qmul (a b : Quat) : Quat :=
  ⟨a.w * b.w - a.x * b.x - a.y * b.y - a.z * b.z,
   a.w * b.x + a.x * b.w + a.y * b.z - a.z * b.y,
   a.w * b.y - a.x * b.z + a.y * b.w + a.z * b.x,
   a.w * b.z + a.x * b.y - a.y * b.x + a.z * b.w⟩

def qconj (a : Quat) : Quat :=
  ⟨a.w, -a.x, -a.y, -a.z⟩

def qscale (c : ℚ) (a : Quat) : Quat :=
  ⟨c * a.w, c * a.x, c * a.y, c * a.z⟩

def qpure (v : Vec3) : Quat :=
  ⟨0, v.x, v.y, v.z⟩

def qscalar (a : ℚ) : Quat :=
  ⟨a, 0, 0, 0⟩

def qnormSq (a : Quat) : ℚ :=
  a.w ^ 2 + a.x ^ 2 + a.y ^ 2 + a.z ^ 2

/-- Numerator `1 + ell_ST` of the unit transition spinor. -/
def transitionSpinNumerator (source target : Slice) : Quat :=
  let ell := sharedLine source target
  ⟨1, ell.x, ell.y, ell.z⟩

theorem transition_spin_norm_sq
    (source target : Slice)
    (h : source ≠ target) :
    qnormSq (transitionSpinNumerator source target) = 3 := by
  cases source <;> cases target <;>
    simp_all [qnormSq, transitionSpinNumerator, sharedLine, normal,
      cross, vscale] <;> norm_num

theorem transition_spin_transports_normal
    (source target : Slice)
    (h : source ≠ target) :
    qmul (transitionSpinNumerator source target)
      (qmul (qpure (normal source))
        (qconj (transitionSpinNumerator source target))) =
      qscale 3 (qpure (normal target)) := by
  cases source <;> cases target <;>
    simp_all [qmul, qconj, qscale, qpure, transitionSpinNumerator,
      sharedLine, normal, cross, vscale] <;>
    ext <;> norm_num

def orientedFaceSign (source middle target : Slice) : ℚ :=
  det3 (normal source) (normal middle) (normal target) / 4

def faceSpinNumerator (source middle target : Slice) : Quat :=
  qmul (transitionSpinNumerator target source)
    (qmul (transitionSpinNumerator middle target)
      (transitionSpinNumerator source middle))

theorem oriented_face_sign_sq
    (source middle target : Slice)
    (h₁ : source ≠ middle)
    (h₂ : middle ≠ target)
    (h₃ : target ≠ source) :
    orientedFaceSign source middle target ^ 2 = 1 := by
  cases source <;> cases middle <;> cases target <;>
    simp_all [orientedFaceSign, det3, normal, cross, dot] <;> norm_num

/-- The three-transition spin numerator is `3 * sign * n_source`. -/
theorem face_spin_numerator_formula
    (source middle target : Slice)
    (h₁ : source ≠ middle)
    (h₂ : middle ≠ target)
    (h₃ : target ≠ source) :
    faceSpinNumerator source middle target =
      qscale (3 * orientedFaceSign source middle target)
        (qpure (normal source)) := by
  cases source <;> cases middle <;> cases target <;>
    simp_all [faceSpinNumerator, orientedFaceSign, det3, qmul, qscale,
      qpure, transitionSpinNumerator, sharedLine, normal, cross, dot,
      vscale] <;>
    ext <;> norm_num

/-- Before dividing by `(sqrt 3)^3`, every face spin numerator squares to `-27`. -/
theorem face_spin_numerator_sq
    (source middle target : Slice)
    (h₁ : source ≠ middle)
    (h₂ : middle ≠ target)
    (h₃ : target ≠ source) :
    qmul (faceSpinNumerator source middle target)
      (faceSpinNumerator source middle target) = qscalar (-27) := by
  cases source <;> cases middle <;> cases target <;>
    simp_all [faceSpinNumerator, qscalar, qmul, transitionSpinNumerator,
      sharedLine, normal, cross, vscale] <;>
    ext <;> norm_num

/-- Agreeing scalar orientations on all three edges of a triangle is impossible. -/
theorem no_triangle_scalar_orientation_flattening :
    ¬ ∃ gA gB gC : ℤ,
      gA ^ 2 = 1 ∧ gB ^ 2 = 1 ∧ gC ^ 2 = 1 ∧
      gA = -gB ∧ gB = -gC ∧ gC = -gA := by
  rintro ⟨gA, gB, gC, hA, hB, hC, hAB, hBC, hCA⟩
  nlinarith

end EnterpriseMath.Precision.EulerFccSpinHolonomy
