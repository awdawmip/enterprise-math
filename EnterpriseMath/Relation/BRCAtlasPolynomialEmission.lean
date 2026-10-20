import EnterpriseMath.Relation.BRCFiniteFrameLift
import EnterpriseMath.Relation.BRCCountAtlas
import Mathlib.Algebra.MvPolynomial.Basic
import Mathlib.Data.Finsupp.Fintype
import Mathlib.Tactic

namespace EnterpriseMath.BranchRecoalescence

/-- Polynomial-variable convention for a finite count atlas: `some i` records
axis `i`, while `none` records the raw operation length.  Weight information is
kept in the coefficient ring through a separate multiplicative character. -/
abbrev AtlasPolynomial (ι R : Type*) [CommSemiring R] := MvPolynomial (Option ι) R

/-- Exponent vector carrying all finite atlas counts together with raw length. -/
noncomputable def atlasExponent {ι : Type*} [Fintype ι]
    (n : CountAtlas ι) (length : ℕ) : Option ι →₀ ℕ :=
  Finsupp.equivFunOnFinite.symm fun x =>
    match x with
    | none => length
    | some i => n i

@[simp] theorem atlasExponent_none {ι : Type*} [Fintype ι]
    (n : CountAtlas ι) (length : ℕ) :
    atlasExponent n length none = length := by
  simp [atlasExponent]

@[simp] theorem atlasExponent_some {ι : Type*} [Fintype ι]
    (n : CountAtlas ι) (length : ℕ) (i : ι) :
    atlasExponent n length (some i) = n i := by
  simp [atlasExponent]

/-- Atlas counts and length add componentwise at the exponent level. -/
@[simp] theorem atlasExponent_add {ι : Type*} [Fintype ι]
    (n m : CountAtlas ι) (length steps : ℕ) :
    atlasExponent (n + m) (length + steps) =
      atlasExponent n length + atlasExponent m steps := by
  ext x
  cases x <;> simp [atlasExponent]

/-- One exact atlas/length/weight-character contribution as a single
multivariate monomial. -/
noncomputable def atlasMonomial {ι R : Type*}
    [Fintype ι] [CommSemiring R]
    (n : CountAtlas ι) (length : ℕ) (coefficient : R) : AtlasPolynomial ι R :=
  MvPolynomial.monomial (atlasExponent n length) coefficient

/-- Multiplying two atlas monomials adds every axis count and raw length while
multiplying their exact coefficient readouts. -/
@[simp] theorem atlasMonomial_mul {ι R : Type*}
    [Fintype ι] [CommSemiring R]
    (n m : CountAtlas ι) (length steps : ℕ) (r s : R) :
    atlasMonomial n length r * atlasMonomial m steps s =
      atlasMonomial (n + m) (length + steps) (r * s) := by
  simp [atlasMonomial]

/-- Canonical polynomial emission for finite count-atlas framed BRC.

At current frame `g`, the coordinate exponent is `g · p.coord`; the coefficient
is the chosen exact multiplicative weight character, and `none` carries the raw
operation length.  The twisted emission law is forced by the coordinate-action
identity

`g · (n + p.frame · m) = g · n + (g * p.frame) · m`.

Thus all frame noncommutativity remains in the finite frame-state matrix, while
weight/count/length information enters an ordinary commutative polynomial ring. -/
noncomputable def atlasPolynomialEmission
    {W G ι R : Type*}
    [Monoid W] [Monoid G] [Fintype ι] [CommSemiring R]
    (ρ : CoordinateAction G (CountAtlas ι))
    (χ : W →* R) :
    FrameEmission W G (CountAtlas ι) (AtlasPolynomial ι R) ρ where
  emit g p := atlasMonomial (ρ.act g p.coord) p.length (χ p.weight)
  emit_one g := by
    have hExp : atlasExponent (0 : CountAtlas ι) 0 = 0 := by
      ext x
      cases x <;> simp [atlasExponent]
    simp [atlasMonomial, ρ.act_zero, hExp]
  emit_mul g a b := by
    change
      atlasMonomial
          (ρ.act g (a.coord + ρ.act a.frame b.coord))
          (a.length + b.length)
          (χ (a.weight * b.weight)) =
        atlasMonomial (ρ.act g a.coord) a.length (χ a.weight) *
          atlasMonomial (ρ.act (g * a.frame) b.coord) b.length (χ b.weight)
    rw [ρ.act_add, ← ρ.mul_act, χ.map_mul]
    exact (atlasMonomial_mul
      (ρ.act g a.coord) (ρ.act (g * a.frame) b.coord)
      a.length b.length (χ a.weight) (χ b.weight)).symm

@[simp] theorem atlasPolynomialEmission_emit
    {W G ι R : Type*}
    [Monoid W] [Monoid G] [Fintype ι] [CommSemiring R]
    (ρ : CoordinateAction G (CountAtlas ι))
    (χ : W →* R) (g : G)
    (p : FramedPath W G (CountAtlas ι) ρ) :
    (atlasPolynomialEmission ρ χ).emit g p =
      atlasMonomial (ρ.act g p.coord) p.length (χ p.weight) := rfl

/-- The resulting whole-BRC finite frame lift is an ordinary matrix whose
entries lie in a commutative multivariate polynomial ring. -/
noncomputable def atlasPolynomialFrameLiftNBRC
    {W G ι R : Type*}
    [Monoid W] [Monoid G] [Fintype G] [DecidableEq G]
    [Fintype ι] [CommSemiring R]
    (ρ : CoordinateAction G (CountAtlas ι))
    (χ : W →* R) :
    FramedNBRC W G (CountAtlas ι) ρ →ₐ[ℕ]
      Matrix G G (AtlasPolynomial ι R) :=
  (atlasPolynomialEmission ρ χ).frameLiftNBRCAlgHom

end EnterpriseMath.BranchRecoalescence
