# HODGE H0O — Non-Split Weil Sixfold Intermediate-Support Fourier–Mukai Exceptional `ch_3` Gate — Research Return

Researcher-ID: `EM-HODGEH0O-D39219`  
Task-ID: `RS-HODGE-H0O-NONSPLIT-WEIL-INTERMEDIATE-SUPPORT-FM-EXCEPTIONAL-CH3`  
Publication: `TP2-A314F727276CFF8CE168`  
Claim: `chatgpt-hodge-h0o-20260903-1101`  
Execution record: `ER-12DEE3E77A08D5F29FB1`  
Execution branch: `research/hodge-h0o-intermediate-support-fm-exceptional-ch3-em-hodgeh0o-d39219`  
Execution base: `1fce8294c6116bdd9fd97828a232657fc7ee892c`  
Date: `2026-09-03`

## Verdict

Terminal classification:

`POINCARE_POLARIZATION_PURE_MIDDLE_SUPPORT_FM_IS_EXCEPTIONAL_SEED_CONSERVING__NO_FIRST_SEED_GENERATION`.

Terminal verdict:

`NEGATIVE_BOUNDARY / EXACT POSITIVE-INSTANTIATION OBSTRUCTION`.

The hard target

`NONSPLIT_WEIL_INTERMEDIATE_SUPPORT_FM_EXCEPTIONAL_CH3_SEED_OR_EXACT_NO_GO_CLASSIFIED`

is satisfied for the single family frozen before calculation: **Poincaré–polarization endo-Fourier–Mukai transforms of pure codimension-three coherent sheaves on the fixed very-general non-split `[-3]` Weil sixfold**.

No nonzero exceptional seed is constructed. Instead, the family is classified exactly:

\[
\boxed{\Pi_W\bigl(\operatorname{ch}_3(\Psi_Q(F))\bigr)
      =T_\lambda\!\left(\Pi_W(\operatorname{ch}_3(F))\right)}
\]

and for pure codimension-three `F`,

\[
\boxed{\Pi_W\bigl(\operatorname{ch}_3(\Psi_Q(F))\bigr)\neq0
\iff
\Pi_W([F]_{\rm cyc})\neq0.}
\]

Thus this Fourier–Mukai route is **exceptional-seed conserving**: it can transport an exceptional codimension-three algebraic support class already present on the same non-split target, but it cannot manufacture the first one from non-exceptional source data.

The exact missing datum is therefore named:

`AN_EXPLICIT_ALGEBRAIC_CODIMENSION3_SUPPORT_CYCLE_GAMMA_ON_A_GEN_WITH_PI_W(GAMMA)_NONZERO`.

No H1 promotion, non-algebraicity statement, all-Fourier–Mukai theorem, or Hodge-conjecture claim is made.

## 1. Frozen target and inherited separator

Use only the H0N target data already accepted by Driver:

- `A=A_gen` is a very-general polarized abelian sixfold of Weil type for `K=Q(i)`;
- the Hermitian discriminant class is `[-3]`, not the split `[-1]` class;
- after complexification
  \[
  H^1(A,\mathbf C)=V_\sigma\oplus V_{\bar\sigma},
  \qquad \dim V_\sigma=\dim V_{\bar\sigma}=6;
  \]
- in middle degree
  \[
  B_p=\Lambda^pV_\sigma\otimes\Lambda^{6-p}V_{\bar\sigma},
  \qquad p=0,\dots,6;
  \]
- the exceptional Weil space is
  \[
  W_{K,\mathbf C}=B_0\oplus B_6;
  \]
- H0N supplies an algebraic rational projector `Pi_W=P(u^*)` whose action is exactly `1` on `B_0,B_6` and `0` on `B_1,...,B_5`.

This projector is used only as a separator. Nothing below assumes that a nonzero rational class in `W_K` is algebraic.

## 2. Family frozen before calculation

Let
\[
\lambda:A\longrightarrow\widehat A
\]
be the fixed `K`-compatible polarization isogeny. Its Rosati involution restricts to complex conjugation on `K`.

Let `P` be the normalized Poincaré line bundle on `A x Ahat`. Put
\[
Q=(\operatorname{id}_A\times\lambda)^*P
\quad\text{on }A\times A.
\]

Define the endo-Fourier–Mukai functor
\[
\Psi_Q(F)
=Rp_{2*}\bigl(p_1^*F\otimes^L Q\bigr).
\]

Since `lambda` is a finite flat isogeny, flat base change identifies this functor with
\[
\Psi_Q\simeq L\lambda^*\circ\Phi_P,
\]
where
\[
\Phi_P:D^b(A)\longrightarrow D^b(\widehat A)
\]
is the standard Poincaré Fourier–Mukai equivalence.

The declared source family is:

> all coherent sheaves `F` on `A` that are pure of codimension `3` (equivalently, pure of dimension `3`).

No WIT hypothesis is imposed. No assumption is made that `Psi_Q(F)` is a sheaf, a bundle, or semihomogeneous. The output is allowed to be an arbitrary object of `D^b(A)`.

This is the crucial separation from H0N: the argument below is not obtained by first proving the output semihomogeneous and then applying the divisor-line formula.

## 3. Exact GRR degree calculation

For an abelian variety the tangent bundle is trivial, so
\[
\operatorname{td}(A)=\operatorname{td}(\widehat A)=1.
\]

Write
\[
\ell=c_1(P)\in H^1(A)\otimes H^1(\widehat A).
\]

Grothendieck–Riemann–Roch gives the cohomological Poincaré transform
\[
\mathcal F_P(\alpha)
=
p_{\widehat A*}\bigl(p_A^*\alpha\,e^\ell\bigr).
\]

If `alpha` has cohomological degree `n`, then to survive integration over the six-dimensional `A` factor the exponential contributes precisely `ell^(12-n)/(12-n)!`. That term has target degree `12-n`. Hence
\[
\boxed{
\mathcal F_P:H^n(A)\longrightarrow H^{12-n}(\widehat A).
}
\]

For even degree `n=2j` this is
\[
\operatorname{ch}_j
\longmapsto
\operatorname{ch}_{6-j}.
\]

Consequently the codimension-three component of the output has **one and only one** source:
\[
\boxed{
\operatorname{ch}_3(\Psi_Q(F))
=
T_\lambda\bigl(\operatorname{ch}_3(F)\bigr),
}
\]
where
\[
T_\lambda
=
\lambda^*\circ\mathcal F_P
\big|_{H^6(A)}.
\]

No `ch_0,ch_1,ch_2,ch_4,ch_5,ch_6` term can leak into target `ch_3`. This remains true without WIT because Chern character is defined on `K_0(D^b(A))`.

## 4. Exact `B_p` block calculation

Let
\[
\widehat V_\sigma\oplus\widehat V_{\bar\sigma}
=H^1(\widehat A,\mathbf C)
\]
be the dual `K`-eigenspace decomposition and set
\[
\widehat B_q
=
\Lambda^q\widehat V_\sigma
\otimes
\Lambda^{6-q}\widehat V_{\bar\sigma}.
\]

The Poincaré class is the universal pairing. With the standard dual `K` labels, a class in `B_p` already uses `p` sigma directions and `6-p` conjugate directions on the source. The only term of `ell^6` that completes the source volume uses the complementary `6-p` sigma directions and `p` conjugate directions. The target factors carried by those six Poincaré terms therefore lie in
\[
\widehat B_{6-p}.
\]
Thus
\[
\boxed{
\mathcal F_P(B_p)=\widehat B_{6-p}.
}
\]

Now use the Weil polarization. Rosati conjugation gives, for `a in K`,
\[
\widehat a\circ\lambda
=
\lambda\circ\bar a.
\]
Hence pullback by `lambda` exchanges the two embedding labels:
\[
\lambda^*(\widehat V_\sigma)=V_{\bar\sigma},
\qquad
\lambda^*(\widehat V_{\bar\sigma})=V_\sigma.
\]
Therefore
\[
\boxed{
\lambda^*(\widehat B_q)=B_{6-q},
}
\]
and the endo middle transform satisfies
\[
\boxed{
T_\lambda(B_p)=B_p
\qquad(p=0,\ldots,6).
}
\]

In particular it preserves both
\[
W_{K,\mathbf C}=B_0\oplus B_6
\]
and the complementary sum
\[
B_1\oplus\cdots\oplus B_5.
\]

Since `Pi_W` is exactly the scalar selector `1` on the first space and `0` on the second,
\[
\boxed{
\Pi_WT_\lambda=T_\lambda\Pi_W
\quad\text{on }H^6(A,\mathbf Q).
}
\]

The Poincaré cohomological transform is an isomorphism, and `lambda^*` is a rational cohomology isomorphism because `lambda` is an isogeny. Thus `T_lambda|W_K` is invertible.

The conclusion is independent of a harmless reversal of the naming convention for the dual `K` eigenspaces: such a reversal replaces the displayed intermediate labels simultaneously, while the set of extreme blocks `{0,6}` remains invariant.

## 5. Pure middle support identifies the source datum

Let `F` be a coherent sheaf pure of codimension `3`.

Its lower Chern-character components vanish:
\[
\operatorname{ch}_0(F)
=
\operatorname{ch}_1(F)
=
\operatorname{ch}_2(F)
=0.
\]

The first nonzero Chern-character component is the fundamental support cycle with generic multiplicities:
\[
\boxed{
\operatorname{ch}_3(F)=[F]_{\rm cyc}.
}
\]

Equivalently, the standard leading-term identity for a pure codimension-`p` sheaf says `ch_p(F)=[F]_cyc`. For `p=3`, one may see this from
\[
c_3(F)=2![F]_{\rm cyc}
\]
together with the Newton identity `ch_3=c_3/2` when `c_1=c_2=0`.

Combining this with the previous sections gives the central theorem.

### Theorem — Poincaré–polarization middle-support seed conservation

For every pure codimension-three coherent sheaf `F` on the fixed non-split `[-3]` Weil sixfold `A_gen`,
\[
\boxed{
\Pi_W\bigl(\operatorname{ch}_3(\Psi_Q(F))\bigr)
=
T_\lambda\bigl(\Pi_W([F]_{\rm cyc})\bigr).
}
\]

Since `T_lambda|W_K` is invertible,
\[
\boxed{
\Pi_W\bigl(\operatorname{ch}_3(\Psi_Q(F))\bigr)\neq0
\iff
\Pi_W([F]_{\rm cyc})\neq0.
}
\]

So a positive output in this entire declared family exists **if and only if** the source support already supplies a nonzero exceptional algebraic codimension-three class on the same target.

The Fourier–Mukai construction contributes no new first-seed mechanism.

## 6. Exact terminal obstruction

The H0O route asked whether intermediate support could let GRR mix source geometry into degree six in a way that escapes H0N.

For this declared family, the answer is exact:

1. intermediate support does matter, because its leading codimension-three support cycle is precisely the datum transported into target `ch_3`;
2. dimension six makes the Poincaré transform anti-diagonal in cohomological degree, so no other source Chern component can contaminate target codimension three;
3. the `K`-compatible polarization closes the transform back on `A` without mixing the exceptional extreme blocks with `B_1,...,B_5`;
4. therefore a nonzero exceptional target component is equivalent to a nonzero exceptional source support cycle.

The positive route is consequently blocked by one named datum:
\[
\boxed{
\exists\ \gamma\in CH^3(A)_\mathbf Q
\text{ algebraic with }
\Pi_W(\gamma)\neq0.
}
\]

But such a `gamma` is already the missing exceptional algebraic seed. Producing it as the support class of `F` would solve the seed problem before applying Fourier–Mukai.

This is an **instantiation obstruction for first-seed generation**, not a proof that every algebraic codimension-three cycle has zero exceptional projection.

## 7. Why this is not the H0N no-go repeated

H0N killed families whose target `ch_3` was forced into `Q theta^3`, notably semihomogeneous bundles and outputs independently verified to remain semihomogeneous.

The present theorem uses none of those hypotheses.

The source support cycle `[F]_cyc` may be any algebraic codimension-three cycle carried by a pure sheaf. Higher Chern data are unrestricted. The Fourier–Mukai output may have arbitrary cohomological amplitude and need not be a sheaf. The conclusion is instead a **conservation law for the exceptional middle block**.

It therefore extends the negative boundary in a genuinely different direction while stopping exactly where the underlying Hodge-algebraicity question begins.

## 8. Adversarial audit

### Hidden semihomogeneity

No semihomogeneity assumption is made or needed. If a special member happens to transform to a semihomogeneous object, H0N gives a second proof of zero whenever applicable; the H0O theorem does not depend on that classification.

### Hidden WIT assumption

None. The output is treated in `D^b(A)` and all formulas are `K_0`/Chern-character identities.

### Divisor-algebra collapse

No assumption `ch_3(F) in Q theta^3` is made. The theorem applies to arbitrary pure codimension-three support cycles. If `[F]` happens to be divisor-generated, H0N is recovered as a special case.

### Imported split data

No split secant sheaf, discriminant `-1` cycle, or deformation from the split component is used. The kernel `Q` is built from the Poincaré bundle and the actual polarization of the fixed `[-3]` target.

Markman's current sixfold theorem proves algebraicity for discriminant `-1`, and his secant-sheaf framework is explicitly presented for split Weil type. Those results are retained only as negative controls; they are not relabeled onto the present target.

### Unsupported support/output assumptions

The only source hypothesis is purity of codimension three. No smooth support is required in the theorem statement; generic multiplicities enter `[F]_cyc`. No claim is made about the geometric support of the derived output.

### Forbidden overreach

The theorem does **not** imply
`Pi_W(CH^3(A)_Q)=0`.

That would be a non-algebraicity statement far beyond the task. If a pure sheaf with exceptional support cycle exists, the theorem predicts a positive Fourier–Mukai output; it correctly identifies that input as a pre-existing seed rather than deriving a contradiction.

## 9. Exact finite certificate

Task-local checker:

`research_checks/HODGE_H0O_NONSPLIT_WEIL_INTERMEDIATE_SUPPORT_FM_EXCEPTIONAL_CH3_CHECK_20260903.py`

Frozen local run:

```text
HODGE_H0O_CHECKS=46
HODGE_H0O_FAILURES=0
DEGREE_REVERSAL_CH3_SOURCE_ONLY=PASS
POINCARE_BLOCK_MAP=B_p->Bhat_(6-p)
POLARIZATION_BLOCK_MAP=Bhat_q->B_(6-q)
ENDO_MIDDLE_BLOCK_MAP=B_p->B_p
PI_W_COMMUTATION_SELECTOR=PASS
H0N_PROJECTOR_RECHECK=PASS
HODGE_H0O_NONSPLIT_WEIL_INTERMEDIATE_SUPPORT_FM_EXCEPTIONAL_CH3_CHECK: PASS
```

The checker independently re-evaluates all seven Gaussian eigenvalues of the frozen H0N projector and its exact rational polynomial values, verifies the degree involution `j -> 6-j`, and verifies the finite block-label composition.

It is only a certificate of the finite reduction. It does not replace GRR, Poincaré duality, the Rosati calculation, or the leading-cycle theorem for coherent sheaves.

## 10. Literature/frontier control

The proof above is internal and does not import a split construction.

Current primary-source routing remains consistent with the frozen boundary:

- Eyal Markman, arXiv:2502.03415, proves algebraicity of Weil classes for abelian sixfolds of discriminant `-1`;
- Markman's arXiv:2509.23403 describes the secant-sheaf strategy for polarized abelian varieties of **split** Weil type;
- Amir Mostaed, arXiv:2603.20268, records current sixfold situations where lack of a suitable secant structure and uncontrolled discriminant remain genuine obstructions.

These sources motivate the negative-control boundary only. No absence-of-literature statement is promoted to a mathematical no-go.

## 11. Unresolved residue

This task closes only the declared Poincaré–polarization pure-middle-support route.

Still open are, among other separately typed possibilities:

- a genuinely different Fourier–Mukai kernel whose middle cohomological action does not preserve the exceptional/complement decomposition;
- a direct construction of an algebraic codimension-three support cycle with nonzero `Pi_W`;
- another algebraic correspondence with an explicit algebraic source class that maps nontrivially into `W_K`;
- other source families whose degree-six contribution contains new geometric data not reduced to a pre-existing middle support cycle.

No statement is made about arbitrary Fourier–Mukai kernels, all derived objects, or all correspondences.

## 12. Recommendation

Driver-review this return as a terminal negative boundary for H0O at the strength:

`POINCARE_POLARIZATION_PURE_MIDDLE_SUPPORT_FM_IS_EXCEPTIONAL_SEED_CONSERVING__NO_FIRST_SEED_GENERATION`.

If accepted, preserve the reusable identity
\[
\Pi_W\operatorname{ch}_3(\Psi_Q(F))
=
T_\lambda\Pi_W([F]_{\rm cyc})
\]
and route any successor only to a genuinely different kernel/action capable of mixing the H0N exceptional/complement blocks, or directly to construction of the named exceptional support cycle.

Do not broaden this result to non-algebraicity or H1.

Freeze boundary reached.
