import EnterpriseMath.Relation.BRCAtlasNormalFormComposition
import EnterpriseMath.Relation.FramedBranchRecoalescence
import Mathlib.Algebra.Group.TransferInstance
import Mathlib.Tactic

namespace EnterpriseMath.BranchRecoalescence

/-- Framed BRC path written directly in canonical count-atlas normal form.

The coordinate field is no longer a raw atlas: it is a certified
`(commonDepth, min-zero residual)` pair.  Weight, resulting frame, and raw
operation length are retained exactly. -/
@[ext]
structure AtlasNormalFramedPath
    (W G ι : Type*) [Monoid W] [Monoid G]
    [Fintype ι] [Nonempty ι]
    (ρ : CoordinateAction G (CountAtlas ι)) where
  weight : W
  atlas : CountAtlasNormalForm ι
  frame : G
  length : ℕ

namespace AtlasNormalFramedPath

variable {W G ι : Type*}
variable [Monoid W] [Monoid G] [Fintype ι] [Nonempty ι]
variable (ρ : CoordinateAction G (CountAtlas ι))

/-- Decode a canonical normal-form path back to the exact raw-atlas
`FramedPath`. -/
def decode (p : AtlasNormalFramedPath W G ι ρ) :
    FramedPath W G (CountAtlas ι) ρ where
  weight := p.weight
  coord := restoreAtlas p.atlas.1
  frame := p.frame
  length := p.length

/-- Encode an exact raw-atlas framed path into canonical depth/residual form. -/
def encode (p : FramedPath W G (CountAtlas ι) ρ) :
    AtlasNormalFramedPath W G ι ρ where
  weight := p.weight
  atlas := countAtlasNormalFormEquiv ι p.coord
  frame := p.frame
  length := p.length

/-- Exact equivalence between raw framed paths and carry-ready canonical framed
paths.  This is a coordinate representation change, not an observer quotient. -/
def normalFormEquiv :
    AtlasNormalFramedPath W G ι ρ ≃ FramedPath W G (CountAtlas ι) ρ where
  toFun := decode ρ
  invFun := encode ρ
  left_inv p := by
    apply AtlasNormalFramedPath.ext
    · rfl
    · change countAtlasNormalFormEquiv ι
        (restoreAtlas p.atlas.1) = p.atlas
      exact (countAtlasNormalFormEquiv ι).apply_symm_apply p.atlas
    · rfl
    · rfl
  right_inv p := by
    apply FramedPath.ext
    · rfl
    · change restoreAtlas (countAtlasNormalFormEquiv ι p.coord).1 = p.coord
      exact (countAtlasNormalFormEquiv ι).symm_apply_apply p.coord
    · rfl
    · rfl

/-- Transport the already-proved framed-path monoid structure across the exact
normal-form equivalence.  Associativity therefore follows from the original BRC
semidirect product rather than being re-proved by ad hoc carry algebra. -/
noncomputable instance instMonoid : Monoid (AtlasNormalFramedPath W G ι ρ) :=
  (normalFormEquiv ρ).monoid

/-- The normal-form equivalence is multiplicative by construction. -/
noncomputable def normalFormMulEquiv :
    AtlasNormalFramedPath W G ι ρ ≃* FramedPath W G (CountAtlas ι) ρ :=
  Equiv.mulEquiv (normalFormEquiv ρ)

@[simp] theorem decode_one :
    decode ρ (1 : AtlasNormalFramedPath W G ι ρ) = 1 := by
  change (normalFormEquiv ρ)
      ((normalFormEquiv ρ).symm (1 : FramedPath W G (CountAtlas ι) ρ)) = 1
  exact (normalFormEquiv ρ).apply_symm_apply _

@[simp] theorem decode_mul
    (a b : AtlasNormalFramedPath W G ι ρ) :
    decode ρ (a * b) = decode ρ a * decode ρ b := by
  exact (normalFormMulEquiv ρ).map_mul a b

@[simp] theorem weight_mul
    (a b : AtlasNormalFramedPath W G ι ρ) :
    (a * b).weight = a.weight * b.weight := by
  change (decode ρ (a * b)).weight = _
  rw [decode_mul]
  rfl

@[simp] theorem frame_mul
    (a b : AtlasNormalFramedPath W G ι ρ) :
    (a * b).frame = a.frame * b.frame := by
  change (decode ρ (a * b)).frame = _
  rw [decode_mul]
  rfl

@[simp] theorem length_mul
    (a b : AtlasNormalFramedPath W G ι ρ) :
    (a * b).length = a.length + b.length := by
  change (decode ρ (a * b)).length = _
  rw [decode_mul]
  rfl

/-- The transported monoid multiplication uses exactly the direct atlas
normal-form composition algorithm. -/
theorem atlas_mul
    (a b : AtlasNormalFramedPath W G ι ρ) :
    (a * b).atlas = composeAtlasNormalForm ρ a.frame a.atlas b.atlas := by
  apply Subtype.ext
  change decomposeAtlas (restoreAtlas (a * b).atlas.1) =
    decomposeAtlas
      (restoreAtlas a.atlas.1 + ρ.act a.frame (restoreAtlas b.atlas.1))
  rw [restoreAtlas_decomposeAtlas]
  have hcoord := congrArg FramedPath.coord (decode_mul ρ a b)
  exact congrArg decomposeAtlas hcoord

/-- With a pure coordinate-reindexing frame action, the actual multiplication
on canonical framed paths is the explicit BRC carry formula

`depth' = h + k + min(r + g·s)`
`residual' = normalize(r + g·s)`.

Thus carry is part of the monoid law itself. -/
theorem atlas_mul_val
    (hρ : CoordinateReindexing ρ)
    (a b : AtlasNormalFramedPath W G ι ρ) :
    (a * b).atlas.1 =
      (a.atlas.1.1 + b.atlas.1.1 +
          normalFormCarry ρ a.frame a.atlas.1.2 b.atlas.1.2,
        normalizeAtlas (a.atlas.1.2 + ρ.act a.frame b.atlas.1.2)) := by
  rw [atlas_mul]
  exact composeAtlasNormalForm_val ρ hρ a.frame a.atlas b.atlas

end AtlasNormalFramedPath

end EnterpriseMath.BranchRecoalescence
