import EnterpriseMath.Relation.BRCCountAtlas
import Mathlib.Tactic

namespace EnterpriseMath.BranchRecoalescence

/-- Reindexing a restored depth/residual atlas keeps the scalar common layer
fixed and acts only on the residual coordinates. -/
theorem act_restoreAtlas {G ι : Type*}
    [Monoid G] [Fintype ι] [Nonempty ι]
    (ρ : CoordinateAction G (CountAtlas ι))
    (hρ : CoordinateReindexing ρ)
    (g : G) (h : ℕ) (r : CountAtlas ι) :
    ρ.act g (restoreAtlas (h, r)) = restoreAtlas (h, ρ.act g r) := by
  rcases hρ g with ⟨e, he⟩
  funext i
  rw [he (restoreAtlas (h, r)) i, he r i]
  rfl

/-- Adding two decoded depth/residual pairs simply adds their scalar depths and
residual atlases before the next canonical normalization. -/
theorem restoreAtlas_add {ι : Type*}
    (h k : ℕ) (r s : CountAtlas ι) :
    restoreAtlas (h, r) + restoreAtlas (k, s) =
      restoreAtlas (h + k, r + s) := by
  funext i
  change (h + r i) + (k + s i) = (h + k) + (r i + s i)
  omega

/-- Uniformly restoring any scalar depth does not change the normalized residual. -/
theorem normalizeAtlas_restoreAtlas {ι : Type*}
    [Fintype ι] [Nonempty ι]
    (h : ℕ) (r : CountAtlas ι) :
    normalizeAtlas (restoreAtlas (h, r)) = normalizeAtlas r := by
  funext i
  rw [normalizeAtlas_apply, commonDepth_restoreAtlas, normalizeAtlas_apply]
  change (h + r i) - (h + commonDepth r) = r i - commonDepth r
  omega

/-- Canonical decomposition of an arbitrary decoded pair first absorbs every
additional common layer hidden inside the residual. -/
theorem decomposeAtlas_restoreAtlas {ι : Type*}
    [Fintype ι] [Nonempty ι]
    (h : ℕ) (r : CountAtlas ι) :
    decomposeAtlas (restoreAtlas (h, r)) =
      (h + commonDepth r, normalizeAtlas r) := by
  apply Prod.ext
  · exact commonDepth_restoreAtlas h r
  · exact normalizeAtlas_restoreAtlas h r

/-- New common layer created when two already-normalized residuals are composed
in a declared current frame. -/
def normalFormCarry {G ι : Type*}
    [Monoid G] [Fintype ι] [Nonempty ι]
    (ρ : CoordinateAction G (CountAtlas ι))
    (g : G) (r s : CountAtlas ι) : ℕ :=
  commonDepth (r + ρ.act g s)

/-- Direct coordinate-normal-form composition.  It is defined through the exact
normal-form equivalence so that no coordinate information is lost; the next
theorem exposes the executable carry formula. -/
def composeAtlasNormalForm {G ι : Type*}
    [Monoid G] [Fintype ι] [Nonempty ι]
    (ρ : CoordinateAction G (CountAtlas ι))
    (g : G)
    (x y : CountAtlasNormalForm ι) : CountAtlasNormalForm ι :=
  countAtlasNormalFormEquiv ι
    (restoreAtlas x.1 + ρ.act g (restoreAtlas y.1))

/-- The direct normal-form algorithm has the explicit coordinate formula

`(h,r) ⋆_g (k,s) =
 (h+k+carry_g(r,s), normalize(r + g·s))`.

This is the finite-atlas BRC carry as an intrinsic multiplication rule rather
than a post-processing statistic. -/
theorem composeAtlasNormalForm_val {G ι : Type*}
    [Monoid G] [Fintype ι] [Nonempty ι]
    (ρ : CoordinateAction G (CountAtlas ι))
    (hρ : CoordinateReindexing ρ)
    (g : G)
    (x y : CountAtlasNormalForm ι) :
    (composeAtlasNormalForm ρ g x y).1 =
      (x.1.1 + y.1.1 + normalFormCarry ρ g x.1.2 y.1.2,
        normalizeAtlas (x.1.2 + ρ.act g y.1.2)) := by
  rcases x with ⟨⟨h, r⟩, hr⟩
  rcases y with ⟨⟨k, s⟩, hs⟩
  change decomposeAtlas
      (restoreAtlas (h, r) + ρ.act g (restoreAtlas (k, s))) = _
  rw [act_restoreAtlas ρ hρ]
  rw [restoreAtlas_add]
  rw [decomposeAtlas_restoreAtlas]
  rfl

/-- Decoding direct normal-form composition recovers the exact original framed
coordinate sum.  Thus the compressed operation is lossless for the declared
count-atlas/frame observer. -/
@[simp] theorem restore_composeAtlasNormalForm {G ι : Type*}
    [Monoid G] [Fintype ι] [Nonempty ι]
    (ρ : CoordinateAction G (CountAtlas ι))
    (g : G)
    (x y : CountAtlasNormalForm ι) :
    restoreAtlas (composeAtlasNormalForm ρ g x y).1 =
      restoreAtlas x.1 + ρ.act g (restoreAtlas y.1) := by
  change restoreAtlas
      (decomposeAtlas (restoreAtlas x.1 + ρ.act g (restoreAtlas y.1))) = _
  exact restoreAtlas_decomposeAtlas _

end EnterpriseMath.BranchRecoalescence
