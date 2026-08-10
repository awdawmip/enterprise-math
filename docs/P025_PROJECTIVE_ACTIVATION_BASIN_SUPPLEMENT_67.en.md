# P025 Supplement 67 — Sparse Activation Basin of the Projective Capacity State

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-paired-square-tail-stage61`  
Depends on: P025 Supplements 47, 64  
Hard block: `NONE`

## 1. A much coarser future query than the projective value

The full projective observable is

\[
\sigma_{\rm proj}=\max\{\rho_a,\rho_b,\rho_c\}.
\]

For many future tasks one first needs only the Boolean question

\[
\boxed{
A_{\rm proj}=\mathbf 1_{\{\sigma_{\rm proj}\ge1\}}.
}
\]

Call `A_proj=1` the **activated projective state** and `A_proj=0` the **subunit basin**.

This bit is a strict quotient of the projective scalar. For example,

\[
1+2=3
\]

and

\[
1+3=4
\]

are both activated, while their exact projective values are `1` and `2`.

## 2. P025-T134 — exact subunit-basin criterion

Because `sigma_proj` is the maximum of the three cyclic terms,

\[
\boxed{
\sigma_{\rm proj}<1
\iff
\rho_a<1,\ \rho_b<1,\ \rho_c<1.
}
\]

Equivalently, in the residual/capacity coordinates from Stage 47,

\[
\boxed{
\begin{aligned}
m(a)&<K_{bc},\\
m(b)&<K_{ac},\\
m(c)&<K_{ab}.
\end{aligned}}
}
\]

Thus the activation bit is exact and requires no witness search.

## 3. P025-T135 — activated states are de Bruijn-sparse

Stage 64 proves, after importing the classical de Bruijn radical-counting theorem, that on a dyadic height interval

\[
X/2<c\le X
\]

one has

\[
N_X(\sigma_{\rm proj}\ge T)
\ll_\varepsilon
\frac{X^{1+\varepsilon}}T
\qquad(1\le T\le X).
\]

Set `T=1`. Then

\[
\boxed{
N_X(A_{\rm proj}=1)
\ll_\varepsilon X^{1+\varepsilon}.
}
\]

The ambient number of positive additive triples on the same dyadic interval is `Theta(X^2)`. Hence

\[
\boxed{
\frac{N_X(A_{\rm proj}=1)}{X^2}
\ll_\varepsilon X^{-1+\varepsilon}.
}
\]

So the activated projective state has density zero with a nearly full factor `X^-1` saving at the level supplied by the imported de Bruijn theorem.

Equivalently, almost all additive states lie in the exact subunit basin

\[
\boxed{\sigma_{\rm proj}<1.}
\]

This is a theorem about the project-defined observable, not a pointwise abc theorem.

## 4. Why this is stronger than merely saying PCC failures are sparse

For every fixed positive exponent `eta`, `PCC_eta` only asks whether

\[
\sigma_{\rm proj}<c^\eta,
\]

whose threshold grows with height.

P025-T135 fixes the threshold at the absolute integer scale `1` and still obtains a sparse exceptional layer.

Thus the projective observable is not merely usually below every positive power of `c`; it is usually already below the first nontrivial integer threshold.

This gives a natural precision basin:

\[
\boxed{
\text{subunit bulk }(\sigma<1)
\quad\cup\quad
\text{sparse activated layer }(\sigma\ge1).
}
\]

## 5. Precision interpretation

The full projective value contains much more information than the activation bit, but for the future language

> "has the projective resource crossed the first integer threshold?"

all values below one are exactly equivalent.

The external counting theorem then shows that this coarse quotient is extremely unbalanced: one fiber contains almost the entire finite universe at large scale.

This is a useful distinction between:

- **state complexity:** the quotient has only two labels;
- **incidence complexity:** one label is sparse by a power law;
- **exact value precision:** needed only after entering the activated layer.

## 6. Prior-art boundary

The de Bruijn theorem and its radical-counting consequences are external prior mathematics. P025-T135 is only the `T=1` specialization of Stage 64's projective compiler plus that prior theorem.

The project-side value is the identification of a sparse activation basin in the explicit projective precision state. No priority claim is made for the counting theorem.

## 7. Executable assets

Added:

- `src/enterprise_math/abc_projective_activation.py`;
- `tests/test_abc_projective_activation.py`.

The code stores only the exact finite activation classification. It does not implement the external asymptotic count.

## 8. Next frontier

No hard block exists. Continue with:

1. study the conditional distribution of `sigma_proj` *inside* the sparse activated layer;
2. separate c-oriented and side-oriented activated states using Stage 65;
3. test whether the activated layer admits a smaller exact state than the whole weighted-radical tuple for useful downstream queries;
4. relay the distinction `state cardinality vs incidence sparsity vs value precision` to A2/P023.
