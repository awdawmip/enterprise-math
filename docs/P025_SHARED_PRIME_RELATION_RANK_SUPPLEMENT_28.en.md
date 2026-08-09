# P025 Supplement 28 — Shared-Prime Coupling Before Relation Rank

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-access-tail-stage18`  
Depends on: P025 Supplements 26–27  
Hard block: `NONE`

## 1. Why pairwise coprimality mattered

Supplement 26 assumes pairwise-coprime blocks. Under that assumption distinct blocks have disjoint prime-coordinate supports, so each block derivative value can be chosen independently before the declared relation rows are imposed.

If blocks share primes, this product structure fails **before** any declared relation is applied. The same prime-coordinate variable contributes simultaneously to several block derivative values.

The correct general state is therefore controlled by a block-by-prime coefficient matrix.

## 2. P025-D16 — derivative coefficient matrix

Let positive integer blocks be

\[
n_1,\ldots,n_m,
\]

with no coprimality assumption. Let

\[
p_1,\ldots,p_s
\]

be the union of all prime supports.

Define

\[
\boxed{
B_{i,p}
=
\begin{cases}
\dfrac{n_i v_p(n_i)}p,&p\mid n_i,\\
0,&p\nmid n_i.
\end{cases}}
\]

For a fine prime-coordinate vector

\[
x\in\mathbb Z^s,
\]

the block derivative-value vector is exactly

\[
\boxed{t=Bx.}
\]

Thus even before relation constraints, the exact joint block-value image is

\[
\boxed{
\Gamma_B=\operatorname{im}_{\mathbb Z}B,
}
\]

not generally the Cartesian product of the separate row ideals.

## 3. P025-T80 — exact shared-prime relation state

Let declared integer block relations be

\[
Ln=0.
\]

Linearity of the derivative requires

\[
Lt=LBx=0.
\]

Therefore the relation-adapted fine coordinates are

\[
\ker_{\mathbb Z}(LB),
\]

and their exact compressed derivative-value image is

\[
\boxed{
\Lambda_{B,L}
=
B(\ker_{\mathbb Z}(LB)).
}
\]

Equivalently,

\[
\boxed{
\Lambda_{B,L}
=
\operatorname{im}_{\mathbb Z}B
\cap
\ker_{\mathbb Z}L.
}
\]

### Proof of the intersection identity

Every vector `Bx` with `LBx=0` is visibly in both sets.

Conversely, if `t` lies in `im_Z B` and `Lt=0`, choose integer `x` with `Bx=t`. Then

\[
LBx=Lt=0,
\]

so `x` is relation-adapted and `t` lies in `B(ker_Z LB)`. ∎

## 4. P025-T81 — general rational rank formula

Consider the restriction

\[
B:\ker_{\mathbb Q}(LB)\to\mathbb Q^m.
\]

Its kernel is exactly

\[
\ker_{\mathbb Q}B,
\]

because `ker B` is automatically contained in `ker LB`.

Hence rank-nullity gives

\[
\begin{aligned}
\operatorname{rank}_{\mathbb Q}\Lambda_{B,L}
&=
\dim\ker(LB)-\dim\ker B\\
&=
(s-\operatorname{rank}LB)-(s-\operatorname{rank}B).
\end{aligned}
\]

Therefore

\[
\boxed{
\operatorname{rank}_{\mathbb Q}\Lambda_{B,L}
=
\operatorname{rank}_{\mathbb Q}B
-
\operatorname{rank}_{\mathbb Q}(LB).
}
\]

This is the shared-prime replacement for Supplement 26's

\[
\text{active block count}-\text{relation rank}.
\]

## 5. Recovery of the pairwise-coprime law

If the non-unit blocks are pairwise coprime, their nonzero rows in `B` have disjoint prime-coordinate supports. Therefore those rows are rationally independent and

\[
\operatorname{rank}B=s_{\rm blocks},
\]

the active block count.

Moreover the disjoint-support matrix has a rational right inverse on its active rows, so multiplication by `B` does not change the row rank of the restricted relation matrix:

\[
\operatorname{rank}(LB)
=
\operatorname{rank}L_I.
\]

Thus P025-T81 reduces exactly to

\[
\boxed{
\operatorname{rank}\Lambda
=s_{\rm blocks}-\operatorname{rank}L_I,
}
\]

recovering Supplement 26.

## 6. P025-N10 — separate block image ideals can create false states

Consider

\[
\boxed{2+4=6.}
\]

The union prime coordinates are `(2,3)`, and the derivative matrix is

\[
\boxed{
B=
\begin{pmatrix}
1&0\\
4&0\\
3&2
\end{pmatrix}.
}
\]

The declared relation row is

\[
L=(1,1,-1),
\]

so

\[
\boxed{LB=(2,-2).}
\]

Hence the fine relation condition is

\[
x_2=x_3,
\]

and the compressed states are

\[
\boxed{
(t_2,t_4,t_6)=t(1,4,5).
}
\]

The ranks are

\[
\operatorname{rank}B=2,
\qquad
\operatorname{rank}(LB)=1,
\]

so the compressed relation state has rank one.

Now inspect the separate block ideals:

\[
A(2)=1,
\qquad
A(4)=4,
\qquad
A(6)=1.
\]

The vector

\[
\boxed{(0,4,4)}
\]

passes the naive tests:

- each component lies in its separate block image ideal;
- it satisfies `0+4=4`.

But it is impossible jointly. The first derivative value is `x_2`, so `t_2=0` forces `x_2=0`; then `t_4=4x_2=0`, contradicting `t_4=4`.

Therefore

\[
\boxed{
\left(\prod_i A_i\mathbb Z\right)\cap\ker L
\supsetneq
\operatorname{im}_{\mathbb Z}B\cap\ker L
}
\]

can hold when blocks share primes.

This is an exact negative boundary for any attempt to apply the independent-block access calculus outside its coprime scope.

## 7. Coupling can reduce rank even with no declared relation

Take blocks

\[
(4,8).
\]

There is only one prime coordinate `2`, and

\[
B=
\begin{pmatrix}4\\12\end{pmatrix}.
\]

Thus

\[
\boxed{
\operatorname{rank}B=1
}
\]

although there are two non-unit blocks.

So shared-prime coupling itself acts like a hidden relation among block values before any external relation language is declared.

## 8. Architecture consequence

The general dimension pipeline is now

\[
\boxed{
\text{fine prime coordinates }x
\xrightarrow{B}
\operatorname{im}B
\xrightarrow{L}
\operatorname{im}B\cap\ker L.
}
\]

The two independent sources of collapse are:

1. **shared-coordinate coupling:** `rank B` can already be smaller than block count;
2. **declared relations:** `rank(LB)` removes additional directions.

Hence the exact global relation-state rank is

\[
\boxed{
\text{prime-to-block image rank}
-
\text{relation rank visible on that image}.
}
\]

This is more general than Supplement 26 and clarifies precisely where its pairwise-coprime product assumption enters.

## 9. Access-cost boundary

When supports are disjoint, a fixed block-value state has exact fine cost

\[
\max_i\kappa_{n_i}(t_i)
\]

because optimal block preimages can be chosen independently.

With shared primes this generally fails: separate optimal preimages may assign incompatible values to the same prime coordinate. The correct preimage-cost problem is now joint:

\[
\boxed{
\min\{\|x\|_\infty:Bx=t\}.
}
\]

Thus Supplements 20–24 remain exact on their declared pairwise-coprime abc scope; Stage 28 identifies the correct replacement object beyond that scope rather than silently extending the old formula.

## 10. Prior-art boundary

Integer matrix images, rank of restricted linear maps, kernel/image intersection identities, and coupled linear preimage problems are standard linear algebra/module theory.

P025 does not claim them as new. The project-side result is the explicit correction of the relation-conditioned precision architecture when block supports overlap.

This is a natural A3/P023 bridge candidate and should be relayed rather than silently promoted into P025-only language.

## 11. Executable assets

Added:

- `src/enterprise_math/relation_shared_prime_rank.py`
  - union-prime derivative coefficient matrix;
  - relation-derivative matrix `LB`;
  - exact rank formula;
  - fine coordinate evaluation/relation check;
  - naive separate-ideal test and explicit false-state counterexample.
- `tests/test_relation_shared_prime_rank.py`
  - `2+4=6` rank-one shared-prime state;
  - pairwise-coprime recovery of Stage 26;
  - no-relation shared-prime rank loss;
  - false separate-ideal state `(0,4,4)`;
  - mixed-exponent calibration.

## 12. Next frontier

No hard block exists. Continue with:

1. define the exact joint access function `kappa_B(t)=min{||x||∞:Bx=t}` for shared-prime systems;
2. seek finite precision summaries of that matrix-preimage cost analogous to the Apéry/capacity profiles in the disjoint-block case;
3. extend certificate rank-gain from `L` to the general image-restricted form on `im B`;
4. test whether Smith/HNF normal forms give practical exact shared-prime access solvers;
5. relay the corrected rank law and false-product counterexample to A3/P023.
