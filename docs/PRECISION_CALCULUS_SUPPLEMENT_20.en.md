# Precision Calculus — Supplement 20

Status: `ACTIVE RESEARCH NOTE`  
Scope: exact transport of one square-collapse basin through integer floor division  
Depends on: T007 integer roots, P007 discrete division, and the canonical P018 response/transport layer through T109  
Discipline: this note is finite and integer-only. `Nat.nthRoot` and floor division are established formal tools; the project question is the exact compatibility forced by combining them on a square basin.

> **Concurrent-numbering resolution.** This note entered `main` from a concurrent P018 route under the provisional labels `Supplement 12 / T110`. PR #68 already had a previously developed and validated continuous sequence `T110–T181`. To preserve both routes without duplicate theorem identifiers, only this later concurrent note is relabelled here as **Supplement 20 / T182**. Its mathematics is unchanged.

## 1. Motivation

The Legendre pressure test exposed a recurring operation:

1. start with a state in one square-collapse basin;
2. extract or divide by an integer factor;
3. ask which square-root scale the quotient can occupy.

At first this appeared to be a P017-specific fact about prime cofactors. The prime assumption is unnecessary. The phenomenon belongs in the precision calculus itself.

Let

\[
B_k=[k^2,(k+1)^2)\cap\mathbb N.
\]

For an integer divisor `d>=2`, consider the floor-quotient projection

\[
Q_d(n)=\left\lfloor\frac nd\right\rfloor.
\]

The question is: how many square-collapse basins can `Q_d(B_k)` meet?

---

## 2. Base quotient root

Set

\[
m=\left\lfloor\frac{k^2}{d}\right\rfloor,
\qquad
j=R_2(m).
\]

Thus

\[
j^2\le m<(j+1)^2.
\]

Because `d>=2` and `k>0`,

\[
m<k^2,
\]

so immediately

\[
\boxed{j<k.}
\]

Integer division therefore strictly lowers the base square-root scale.

---

## 3. A quotient helper inequality

Let

\[
a=\left\lfloor\frac kd\right\rfloor.
\]

Then

\[
a^2\le\left\lfloor\frac{k^2}{d}\right\rfloor=m.
\]

Indeed,

\[
ad\le k,
\]

so

\[
a^2d
\le a k
\le k^2,
\]

and the defining adjunction of floor division gives `a^2<=k^2/d`.

Consequently

\[
a\le j.
\]

This small inequality is the key finite coupling between Euclidean quotient scale and square-root scale.

---

## 4. P018-T182 — Two-basin quotient transport

Status: `PROVED` and Lean-formalized.

Let

\[
k\ge1,
\qquad d\ge2,
\qquad k^2\le n<(k+1)^2.
\]

Set

\[
j=R_2\!\left(\left\lfloor\frac{k^2}{d}\right\rfloor\right).
\]

Then

\[
\boxed{
R_2\!\left(\left\lfloor\frac nd\right\rfloor\right)
\in\{j,j+1\}
}
\]

and

\[
\boxed{j<k.}
\]

Equivalently, floor division maps one complete square-collapse basin into at most two adjacent square-root-index basins at a strictly smaller root scale.

### Proof

The lower bound is immediate from monotonicity of integer division:

\[
\left\lfloor\frac{k^2}{d}\right\rfloor
\le
\left\lfloor\frac nd\right\rfloor.
\]

Since

\[
j^2\le\left\lfloor\frac{k^2}{d}\right\rfloor,
\]

we obtain

\[
j
\le
R_2\!\left(\left\lfloor\frac nd\right\rfloor\right).
\]

For the upper bound, from the definition of `j`,

\[
\left\lfloor\frac{k^2}{d}\right\rfloor<(j+1)^2,
\]

hence

\[
k^2<d(j+1)^2.
\]

From Section 3,

\[
\left\lfloor\frac kd\right\rfloor\le j.
\]

Euclidean division also gives

\[
k<d\left(\left\lfloor\frac kd\right\rfloor+1\right)
\le d(j+1).
\]

Therefore

\[
2k<d(2j+3).
\]

Combining the last inequality with `k^2<d(j+1)^2` yields

\[
(k+1)^2\le d(j+2)^2.
\]

Since `n<(k+1)^2`,

\[
n<d(j+2)^2,
\]

and hence

\[
\left\lfloor\frac nd\right\rfloor<(j+2)^2.
\]

Thus its integer square root is strictly below `j+2`. Together with the lower bound it must equal `j` or `j+1`.

Finally, `d>=2` gives

\[
\left\lfloor\frac{k^2}{d}\right\rfloor<k^2,
\]

so `j<k`. ∎

---

## 5. Window form

The complete quotient image of the basin is the integer interval

\[
Q_d(B_k)
=
\left[
\left\lfloor\frac{k^2}{d}\right\rfloor,
\left\lfloor\frac{(k+1)^2-1}{d}\right\rfloor
\right].
\]

T182 says every element of this interval has square-root index `j` or `j+1`.

For divisible states strictly inside the square basin, the quotient/cofactor window becomes

\[
\left[
\left\lfloor\frac{k^2}{d}\right\rfloor+1,
\left\lfloor\frac{(k+1)^2-1}{d}\right\rfloor
\right].
\]

Every element `q` in a nonempty such window satisfies

\[
\boxed{j^2<q<(j+2)^2.}
\]

This is exactly the form needed by P017 after extracting a least prime factor, but the theorem itself is not prime-specific.

---

## 6. Why this is stronger than a size estimate

A coarse estimate such as

\[
Q_d(n)\approx n/d
\]

only says that division reduces magnitude. T182 says more:

- the square-root **index** strictly descends;
- the entire original basin has only **two possible target indices**;
- no continuum approximation or real square root is used;
- the result is stable under arbitrary integer `d>=2`, not just prime factors.

So division does not scatter one square basin across many lower square scales. It produces a tightly controlled two-basin image.

---

## 7. Formalization and executable checks

The Python reference layer provides:

- `square_basin_quotient_transport(k,d,n)`;
- `square_basin_quotient_window(k,d)`;
- `open_divisible_cofactor_window(k,d)`.

The regression suite exhaustively checks bounded families of `k`, `d`, and basin states, including cases that actually reach the upper target index `j+1`.

The Lean module `EnterpriseMath.Precision.QuotientBasin` formalizes the statewise theorem using only:

- `Nat.nthRoot` order characterizations;
- exact natural-number floor division;
- finite arithmetic inequalities.

No hidden real-root semantics is required by the proof.

---

## 8. Consequence for the research architecture

T182 changes the status of the lower-band problem discovered in P017.

The lower-band least prime may be small, so a direct sieve count remains difficult. But after dividing by that least factor, the quotient is not an arbitrary smaller integer interval: it is confined to two adjacent square-collapse basins whose base root index is strictly less than `k`.

This gives a genuine root-scale descent mechanism:

\[
\boxed{
\text{one square basin}
\xrightarrow{\;\lfloor /d\rfloor\;}
\text{at most two adjacent lower square basins}.
\]

The next P017 step should therefore test recursive lower-band transport through T182 rather than introduce another flat sieve encoding. The key question becomes whether repeated factor extraction plus two-basin transport can force a well-founded finite descent strong enough to control the remaining lower-band composite mass.
