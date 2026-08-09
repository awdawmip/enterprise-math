# P018 — All-Power Quotient-Basin Transport

Status: `ACTIVE RESEARCH NOTE`  
Scope: extension of the square-basin quotient transport theorem to every positive root exponent  
Depends on: integer-root basin semantics, exact floor division, and P018 square-basin transport  
Discipline: the proof is elementary integer order arithmetic. No priority claim is made for the underlying inequalities; the project-specific value is the finite-precision/root-basin packaging and its use as a reusable transport lemma.

## 1. Question

The current P018 quotient-basin theorem is stated for square basins. The same structural question exists for every positive root exponent.

Fix

\[
p\ge1,\qquad k\ge1,\qquad d\ge2,
\]

and the canonical `p`-root basin

\[
B_{p,k}=\{n\in\mathbb N:k^p\le n<(k+1)^p\}.
\]

Put

\[
q_0=\left\lfloor\frac{k^p}{d}\right\rfloor,
\qquad
j=R_p(q_0).
\]

How many `p`-root basins can the quotient image `Q_d(B_{p,k})` meet?

## 2. P018-APQ-T01 — All-power two-basin quotient theorem

Status: `PROVED`.

For every

\[
n\in B_{p,k},
\]

one has

\[
\boxed{
R_p\!\left(\left\lfloor\frac nd\right\rfloor\right)
\in\{j,j+1\}
}
\]

and

\[
\boxed{j<k.}
\]

Thus a nontrivial floor quotient sends one entire `p`-root basin into at most two adjacent `p`-root basins. The square theorem is the specialization `p=2`.

### Proof

Because `d>=2`,

\[
\left\lfloor\frac{k^p}{d}\right\rfloor<k^p,
\]

so

\[
j<k.
\]

The lower bound is immediate from monotonicity:

\[
\left\lfloor\frac{k^p}{d}\right\rfloor
\le
\left\lfloor\frac nd\right\rfloor,
\]

hence

\[
j\le R_p\!\left(\left\lfloor\frac nd\right\rfloor\right).
\]

By the root-basin characterization of `j`,

\[
\left\lfloor\frac{k^p}{d}\right\rfloor<(j+1)^p,
\]

therefore

\[
\boxed{k^p<d(j+1)^p.}
\]

Since `j<k`, integer order gives

\[
j+1\le k.
\]

Hence

\[
(k+1)(j+1)\le k(j+2),
\]

because the right side minus the left side is `k-j-1>=0`. Raising both sides to the positive power `p`,

\[
(k+1)^p(j+1)^p\le k^p(j+2)^p.
\]

Combining this with `k^p<d(j+1)^p` gives

\[
(k+1)^p(j+1)^p
<d(j+1)^p(j+2)^p.
\]

Since `(j+1)^p>0`, cancellation yields

\[
\boxed{(k+1)^p<d(j+2)^p.}
\]

For `n<(k+1)^p`, this implies

\[
\left\lfloor\frac nd\right\rfloor<(j+2)^p,
\]

so its `p`-root index is strictly below `j+2`. Together with the lower bound, it is exactly `j` or `j+1`. ∎

No real root or real ratio is used in the proof.

## 3. P018-APQ-T02 — Exact split criterion

Status: `PROVED`.

Let

\[
q_{\max}
=
\left\lfloor
\frac{(k+1)^p-1}{d}
\right\rfloor.
\]

The upper target root `j+1` is actually realized by the quotient image if and only if

\[
\boxed{
d(j+1)^p\le (k+1)^p-1.}
\]

Equivalently,

\[
\boxed{
R_p(q_{\max})=j+1
\iff
d(j+1)^p\le (k+1)^p-1.
}
\]

### Proof

The upper branch occurs exactly when

\[
q_{\max}\ge(j+1)^p.
\]

For positive integer `d`, this is equivalent to

\[
(k+1)^p-1\ge d(j+1)^p.
\]

The two-basin theorem excludes every larger root index. ∎

So the entire basin transport can be summarized by one exact binary branch bit once `p,k,d` are known.

## 4. Quotient-path flattening remains valid

For any finite sequence of positive divisors

\[
d_1,\ldots,d_h,
\]

ordinary Euclidean division gives

\[
Q_{d_h}\circ\cdots\circ Q_{d_1}=Q_D,
\qquad
D=\prod_i d_i.
\]

Therefore APQ-T01 applies once with divisor `D`:

\[
\boxed{
R_p(Q_D(n))\in\{j_D,j_D+1\},
\qquad
j_D=R_p(Q_D(k^p)).
}
\]

Repeated quotient stages do not create an exponential family of final `p`-root indices. This is the all-power analogue of the existing square-root path-flatness consequence.

Intermediate quotient states can still differ across factorizations or stage orderings when the operations are not merely quotient factors of one product. The statement concerns the exact final quotient represented by the product divisor.

## 5. Finite-precision interpretation

The theorem separates three levels of information:

1. the coarse source root index `k`;
2. the computable base target index `j=R_p(k^p//d)`;
3. at most one additional bit deciding whether the actual target is `j` or `j+1`.

This does **not** say the whole quotient state is recoverable from one bit. It says only that the final `p`-root-basin observation has binary residual ambiguity inside each source root basin.

If the future-compatible quotient machinery of P023 is used, the pair

\[
(k,\,R_p(Q_d(n)))
\]

is the coarsest one-step repair of the source root-basin observation for this specific future root observation. APQ-T01 shows that the extra label is binary; APQ-T02 tells exactly when it is nontrivial.

## 6. Relation to the square result

For `p=2`, APQ-T01 specializes to the existing P018 two-square-basin transport theorem. The general proof reveals that the mechanism is not specifically Pythagorean or quadratic. The essential ingredients are:

- exact perfect-power basin boundaries;
- nontrivial floor division;
- the order relation `j<k`;
- the elementary cross-multiplication inequality
  \[
  (k+1)(j+1)\le k(j+2).
  \]

The square case remains useful because P017 is currently organized around consecutive squares, but the transport law belongs to the general integer-root layer.

## 7. Executable validation

`src/enterprise_math/p018_power_basin.py` implements:

- `power_basin_quotient_window`;
- `power_basin_quotient_transport`;
- `iterated_power_basin_quotient_transport`.

`tests/test_p018_power_basin.py` checks broad bounded grids of exponents, basin indices and divisors, exact split criteria, statewise transport on small basins, and quotient-path flattening. These tests audit the implementation; the proof above is the mathematical justification.

## 8. Next question

The next useful extension is not another copy of the same two-basin statement. Two directions are sharper:

1. classify when the **actual** target `p`-root is guaranteed to be strictly below `k` across the whole source basin, equivalently when
   \[
   (k+1)^p\le d k^p;
   \]
2. combine APQ-T01 with operation-safe precision selection to determine which root-basin distinctions must survive a prescribed family of quotient/collapse operations.

Any further result should remain integer-only and should be demoted if it merely rewrites standard quotient identities without new structural use.
