# Free Research — Augmented Odd-Simplex Singular Gap and Provenance-Loss Barrier

Status: `FREE_RESEARCH_FRONTIER / AUGMENTED_SINGULAR_GAP_CLOSED / SCALAR_PROVENANCE_TRANSFER_NO_GO / ORDERED_OPERATOR_LIFT_REQUIRED / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Parent: `FREE_RESEARCH_PRIME_WINDING_NILPOTENT_PSEUDOSPECTRAL_NO_GO_20260904.md`

## 1. Correction

The nilpotent no-go shows that the one-step quotient operator `P_N` has a perfect but irrelevant eigenvalue gap and a logarithmically large inverse norm. It does **not** mean that the full quotient 2-complex lacks a singular gap.

Once the one-step, direct product-edge, and transported product-edge channels are retained together, the odd-triangle identity already supplies a uniform lower singular-value estimate.

Thus the geometry gap is closed. The remaining problem is an arithmetic **energy-transfer** theorem.

---

## 2. Augmented differential

Let `S` be a finite action set with weights `u_a>=0`, and write

\[
U=\sum_{a\in S}u_a.
\]

For each state `n`, define the augmented odd-simplex differential by its three families of coordinates:

\[
\mathscr D_S f(n)
:=
\left(
\{\sqrt{Uu_a}\,\delta_a f(n)\}_{a\in S},
\{\sqrt{u_au_b}\,\delta_{ab}f(n)\}_{a,b\in S},
\{\sqrt{u_au_b}\,\delta_bf(q_a(n))\}_{a,b\in S}
\right).
\]

Its squared norm is exactly

\[
\boxed{
\|\mathscr D_Sf(n)\|^2
=UE_1(f;n,S)+E_{\rm dir}(f;n,S)+E_{\rm tr}(f;n,S).
}
\tag{2.1}
\]

---

## ASG-T01 — Uniform pointwise lower singular gap

The weighted odd-triangle inequality gives

\[
\boxed{
\|\mathscr D_Sf(n)\|^2
\ge\frac43U^2|f(n)|^2.
}
\tag{2.2}
\]

Therefore the normalized differential

\[
U^{-1}\mathscr D_S
\]

has pointwise lower singular value at least

\[
\boxed{2/\sqrt3}
\]

whenever `U>0`.

This constant is independent of the cutoff, the number of action labels, and the arithmetic values of the positive weights.

---

## ASG-T02 — Global weighted gap

Because (2.2) is pointwise, it may be multiplied by any nonnegative outer vertex weight `m_n` and summed:

\[
\boxed{
\sum_nm_n\|\mathscr D_Sf(n)\|^2
\ge\frac43U^2\sum_nm_n|f(n)|^2.
}
\tag{2.3}
\]

Hence the full augmented quotient complex already has a uniform singular/Poincare gap in every diagonal positive vertex measure.

The missing theorem is not another geometric gap estimate.

---

## 3. Reconciliation with the nilpotent no-go

The one-step residual sees only

\[
(I+P)f.
\]

Its inverse can amplify by `Theta(log N)` because a single deterministic quotient chain can alternate coherently.

The augmented differential additionally sees

\[
(I+P^2)f
\]

and the transported one-step residuals. These coordinates compare each two-step route with the direct product edge and destroy coherent alternation by odd-triangle parity.

Thus:

\[
\boxed{
\text{one-step operator: logarithmic pseudospectral loss},
}
\]

but

\[
\boxed{
\text{full quotient 2-complex: uniform normalized singular gap}.
}
\]

There is no contradiction; the second operator contains strictly more provenance information.

---

## 4. Arithmetic specialization

For prime-power labels up to `Y`, take

\[
u_a=\Lambda(a)/a,
\qquad U_Y=\log Y+O(1).
\]

Then

\[
\|\mathscr D_Y f(n)\|^2
\ge\frac43U_Y^2|f(n)|^2.
\]

At the natural scale `Y=floor(sqrt n)`, the PNT zero-energy criterion is precisely

\[
\boxed{
\|\mathscr D_Y r(n)\|^2=o(U_Y^2).
}
\]

The real-smoothing proof establishes this asymptotically. A native proof must show that an arithmetic positive provenance packet controls the left side.

---

## 5. Scalar provenance-loss barrier

The scalar convolution coefficient

\[
(\Lambda*\Lambda)(c)
=\sum_{ab=c}\Lambda(a)\Lambda(b)
\]

remembers the recoalesced product label `c` but forgets the ordered intermediate vertex `q_a(n)`.

The direct energy depends only on the product endpoint and can therefore be grouped by `c`. The transported energy cannot.

### Exact counterexample

Take `n=100` and product label

\[
18=2\cdot9=9\cdot2.
\]

Both ordered histories end at

\[
q_{18}(100)=5.
\]

But their intermediate states differ:

\[
q_2(100)=50,
\qquad
q_9(100)=11.
\]

Choose a field with

\[
f(50)=1,
\qquad f(11)=0,
\qquad f(5)=0.
\]

Then

\[
\delta_9f(q_2(100))=1,
\]

while

\[
\delta_2f(q_9(100))=0.
\]

The two histories have the same scalar product label and the same final endpoint, yet different transported energy.

Therefore:

\[
\boxed{
\text{no scalar function of }c=ab
\text{ can reconstruct }E_{\rm tr}
\text{ for arbitrary }f.
}
\tag{5.1}
\]

This is a concrete no-resurrection statement: once the ordered intermediate history has been collapsed into the scalar coefficient at `c`, the transported quotient defect cannot be recovered.

---

## ASG-T03 — Required operator-valued lift

The degree-three object required by the remainder problem cannot be only the scalar sequence

\[
\Lambda_3=D\Lambda_2+\Lambda*\Lambda_2.
\]

It must retain at least the ordered path key

\[
(a,b,q_a(n),q_{ab}(n)).
\]

A minimal operator-valued packet is therefore indexed by ordered action pairs:

\[
\mathbf P_3(n)
=
\bigoplus_{a,b}
\frac{\Lambda(a)\Lambda(b)}{ab}
\,|a,b;n\rangle\langle a,b;n|,
\]

with the evaluation map sending the path key to

\[
\delta_bf(q_a(n)).
\]

The scalar convolution is only the pushforward under

\[
(a,b)\mapsto ab.
\]

That pushforward is sufficient for direct endpoint energy but not for transported energy.

---

## 6. Updated exact frontier

Closed:

1. the one-step eigenvalue route is ruled out by nilpotent pseudospectral growth;
2. the full augmented quotient 2-complex has a uniform normalized singular gap;
3. PNT is equivalent to decay of its arithmetic energy;
4. scalar product-label provenance is proved insufficient for the transported channel.

Open:

1. construct the ordered operator-valued degree-three provenance packet canonically from the existing branch/recoalescence substrate;
2. prove its arithmetic expectation is `o(U_Y^2)` on the centered winding field;
3. derive quantitative remainder information.

---

## 7. Next theorem

The next target is no longer a vague curvature search. It is the explicit factorization

\[
\boxed{
\mathscr D_Y^*\mathscr D_Y
\preccurlyeq
\mathbf P_{3,Y}+\text{controlled boundary operator},
}
\]

where `P_3,Y` retains ordered action-pair provenance and admits an arithmetic asymptotic estimate.

Any construction that first pushes `(a,b)` down to `ab` is disqualified by the counterexample above, because it has already erased the intermediate vertex required by the transported channel.
