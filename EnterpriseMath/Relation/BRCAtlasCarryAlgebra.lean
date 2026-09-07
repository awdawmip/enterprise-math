import EnterpriseMath.Relation.BRCAtlasPolynomialEmission
import EnterpriseMath.Relation.BRCCountAtlas
import Mathlib.Tactic

namespace EnterpriseMath.BranchRecoalescence

/-- Uniform common layer: the same nonnegative depth on every atlas axis. -/
def commonLayerAtlas {ι : Type*} (h : ℕ) : CountAtlas ι :=
  fun _ => h

@[simp] theorem commonLayerAtlas_apply {ι : Type*} (h : ℕ) (i : ι) :
    commonLayerAtlas h i = h := rfl

/-- Common depth plus normalized residue reconstructs the original atlas as an
actual pointwise sum. -/
theorem commonLayer_add_normalizeAtlas {ι : Type*}
    [Fintype ι] [Nonempty ι] (n : CountAtlas ι) :
    commonLayerAtlas (commonDepth n) + normalizeAtlas n = n := by
  funext i
  exact commonDepth_add_normalizeAtlas n i

/-- Algebraic common-layer factor.  In raw axis variables this is
`(∏ᵢ Xᵢ)^h`; no independent depth coordinate is postulated. -/
noncomputable def depthMonomial {ι R : Type*}
    [Fintype ι] [CommSemiring R] (h : ℕ) : AtlasPolynomial ι R :=
  atlasMonomial (commonLayerAtlas h) 0 1

/-- Every atlas monomial factors canonically into a common-depth factor and a
min-zero residual monomial.

For the K4 six-axis specialization this is exactly
`X^n = (X_AB X_AC X_AD X_BC X_BD X_CD)^h X^r`
with `h = min(n)` and `min(r)=0`. -/
theorem atlasMonomial_decompose_commonDepth {ι R : Type*}
    [Fintype ι] [Nonempty ι] [CommSemiring R]
    (n : CountAtlas ι) (length : ℕ) (coefficient : R) :
    atlasMonomial n length coefficient =
      depthMonomial (commonDepth n) *
        atlasMonomial (normalizeAtlas n) length coefficient := by
  calc
    atlasMonomial n length coefficient =
        atlasMonomial
          (commonLayerAtlas (commonDepth n) + normalizeAtlas n)
          length coefficient := by
      rw [commonLayer_add_normalizeAtlas]
    _ = depthMonomial (commonDepth n) *
          atlasMonomial (normalizeAtlas n) length coefficient := by
      simpa [depthMonomial] using
        (atlasMonomial_mul
          (commonLayerAtlas (commonDepth n)) (normalizeAtlas n)
          0 length (1 : R) coefficient).symm

/-- Multiplying two atlas monomials and then restoring canonical min-zero form
extracts exactly the newly available common layer.  This is the commutative
algebra shadow of BRC common-depth carry. -/
theorem atlasMonomial_mul_normalForm {ι R : Type*}
    [Fintype ι] [Nonempty ι] [CommSemiring R]
    (n m : CountAtlas ι) (length steps : ℕ) (r s : R) :
    atlasMonomial n length r * atlasMonomial m steps s =
      depthMonomial (commonDepth (n + m)) *
        atlasMonomial (normalizeAtlas (n + m)) (length + steps) (r * s) := by
  rw [atlasMonomial_mul]
  exact atlasMonomial_decompose_commonDepth (n + m) (length + steps) (r * s)

/-- Framed version: the second atlas is first transported by the current frame,
then the product is canonically refactored.  The extracted exponent is therefore
`commonDepth (n + g·m)`, exactly the quantity used by framed common-depth carry. -/
theorem atlasMonomial_framed_mul_normalForm
    {G ι R : Type*}
    [Monoid G] [Fintype ι] [Nonempty ι] [CommSemiring R]
    (ρ : CoordinateAction G (CountAtlas ι))
    (g : G) (n m : CountAtlas ι)
    (length steps : ℕ) (r s : R) :
    atlasMonomial n length r * atlasMonomial (ρ.act g m) steps s =
      depthMonomial (commonDepth (n + ρ.act g m)) *
        atlasMonomial (normalizeAtlas (n + ρ.act g m))
          (length + steps) (r * s) := by
  exact atlasMonomial_mul_normalForm n (ρ.act g m) length steps r s

end EnterpriseMath.BranchRecoalescence
