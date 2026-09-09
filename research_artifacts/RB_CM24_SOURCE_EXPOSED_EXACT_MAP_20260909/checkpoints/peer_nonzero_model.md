# Peer paper review: RB CM24 nonzero and target model

Date: 2026-09-09. Scope: source-exposed paper review only. No mathematics was executed, no control surface was read, and no research-workspace file was changed.

Reviewed note: `D:/em/TEMP/rb-cm24-source-exposed-owner-review-20260909/review-nonzero-model.md`, SHA256 `8a78e4add2692ec903a995623f05344343979ad6691c09c809469d041ca4b504`.

Frozen formulas: source publication `341f36bb53c25d97c3ae533a71c92ad273a7b904`, source_freeze.json SHA256 `85946a8cb4e736021cef6cd311c8cfffbde1cce34fe728255db4b6703f5887f2`.

## Conclusion

**PASS for the stated partial paper obligations.** I found no logical gap in the coefficient-field degree, function-field nonzero arguments, O-point orders, monic target change, or symbolic j formula. These deductions may be incorporated into the researcher's source-bound proof. They are not a complete eight-gate certificate or a formal acceptance.

## Checks

1. **Coefficient field.** Eisenstein gives \([\mathbb Q(\alpha):\mathbb Q]=4\); reality excludes \(i\), hence \(K_0=\mathbb Q(\alpha,i)\) has degree eight. Its generators \(r(\alpha)=i\alpha,\ r(i)=i\) and complex conjugation satisfy the stated dihedral relations. The commutator is \(\langle r^2\rangle\), so every quadratic subfield lies in its degree-four fixed field \(\mathbb Q(\sqrt3,i)\). Its three quadratic subfields exclude \(\mathbb Q(\sqrt2)\). Adjoining \(\beta\) therefore doubles the degree to sixteen. The sixteen listed monomials span and are a basis. This supplies the missing faithfulness justification for reduced coefficient vectors under the selected embedding.

2. **Curve and function-field nonzero facts.** The simple zero of \(R^3-3R\) at \(R=0\) rules out a square in \(L(R)\), giving the basis \(1,t\). At the smooth point \((0,0)\), \(t\) is a local parameter and \(R+2\) is a unit, so \((R+2)t\) has odd valuation and defines a connected quadratic cover. Passing to the smooth projective normalization is correctly retained for global statements. The nonzero constant vectors and
   \[
   k^2=-\alpha^2(\alpha^2\beta-2)^2=12\beta-10\alpha^2
   \]
   have the claimed signs and basis support. Thus \(\lambda\ne0,1\), \(u_N\ne0\), \(C_4\ne0\), and \(k^2\notin\{0,2,-2\}\).

3. **Orders at O.** The unique lowest-order term in \(N\) is \(i\alpha u_N R^3\), of order \(-6\); the remaining terms have larger orders, including \(Rt\) of order \(-5\). In \(D_0\), the unique lowest-order term is \(R^2t\), of order \(-7\), while the cubic-in-R term has order \(-6\). Hence
   \[
   \operatorname{ord}_O(N)=-6,\quad \operatorname{ord}_O(D_0)=-7,\quad
   \operatorname{ord}_O(X)=1.
   \]
   Both functions have no finite poles and lie in \(L(7O)\); their section orders at O are respectively 1 and 0. This proves nonconstancy and that **O alone is not a common base point**. It gives no count or cancellation multiplicity of finite common base points and no degree-six conclusion. Characteristic zero then gives \(dX\ne0\), and the stated relation \(W=2D_0^2\delta X\) implies \(W\ne0\). Nonzero denominators as rational functions do not mean pointwise nonvanishing or regularity everywhere.

4. **Target change and invariant.** With \(C=C_4/4\ne0\), \(x=CX,\ y=CY\) is invertible and yields
   \[
   y^2=x^3-C(1+\lambda)x^2+C^2\lambda x.
   \]
   Substitution in the standard Weierstrass definitions gives exactly the listed \(b_2,b_4,b_6,b_8,c_4\) and
   \[
   \Delta=16C^6\lambda^2(1-\lambda)^2,\qquad
   j=256(1-\lambda+\lambda^2)^3/[\lambda^2(1-\lambda)^2].
   \]
   There is no missing scaling factor or sign. The discriminant proves that this projective target is elliptic. The symbolic j relation does not identify a CM period, choose a simplified radical branch, or prove a homology/image index.

## Gate scope

The note can support coefficient-presentation faithfulness and the declared nonzero embedding facts; nondegenerate function-field interpretation of the already recorded cleared ODE; the O-point part of the section/basepoint analysis; and the monic nonsingular target plus its symbolic j invariant.

Still required are all finite special-fiber valuations, every common-basepoint cancellation and multiplicity, degree six, square-class/half-point placement and descent, the complete unsquared differential and exceptional-point proof, source-bound checks, and the final certificate/return. The period/homology and exhaustive 1980-family frontier remains open. No stronger conclusion is inferred from this review.
