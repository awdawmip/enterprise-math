# Prime-BRC Floor-Quotient Branch Birth Multiplicity

Status: `L3 OWNER-LOCAL / PROVED ELEMENTARY THEOREM / NOT LEGENDRE`
Date: `2026-08-23`
Researcher-ID: `EM-PRIMEBRC-7F3A21`
Owner branch: `research/prime-brc-stage-a`

## 1. Full floor-quotient support

For `n>=1`, define

\[
\mathcal F(n)=
\left\{
\left\lfloor\frac{n}{j}\right\rfloor:1\le j\le n
\right\}.
\]

For a label `m>=1`, define

\[
J_n(m)=
\left\lfloor\frac nm\right\rfloor-
\left\lfloor\frac n{m+1}\right\rfloor.
\]

Then

\[
m\in\mathcal F(n)\iff J_n(m)>0.
\]

As in the signed-jump supplement,

\[
J_n(m)-J_{n-1}(m)
=
\mathbf1_{m\mid n}-\mathbf1_{m+1\mid n}.
\]

## 2. Exact branch-birth set

### Theorem

For every `n>=2`,

\[
\boxed{
\mathcal F(n)\setminus\mathcal F(n-1)
=
\{d:d\mid n,\ d^2\ge n\}.
}
\]

### Proof

A label `d` can enter only when `d|n`. Write

\[
n=ad.
\]

Then

\[
J_{n-1}(d)
=a-1-
\left\lfloor\frac{ad-1}{d+1}\right\rfloor.
\]

Since `(ad-1)/(d+1)<a`, this vanishes iff

\[
(a-1)(d+1)\le ad-1,
\]

which reduces exactly to

\[
a\le d.
\]

Since `n=ad`, this is equivalent to

\[
d^2\ge n.
\]

In that case `d+1` cannot simultaneously create a cancelling loss, so `d` is genuinely new. ∎

## 3. Birth multiplicity and the divisor function

Let `tau(n)` be the number of positive divisors of `n`.

If `n` is not a square, divisors pair strictly as

\[
d\longleftrightarrow n/d
\]

across `sqrt(n)`, so exactly half lie above the square-root frontier. Hence

\[
\boxed{
|\mathcal F(n)\setminus\mathcal F(n-1)|
=\frac{\tau(n)}2
\qquad(n\text{ nonsquare}).
}
\]

If `n=s^2`, the central divisor `s` is unpaired and

\[
\boxed{
|\mathcal F(n)\setminus\mathcal F(n-1)|
=\frac{\tau(n)+1}{2}.
}
\]

## 4. Consecutive-square prime criterion

Every integer strictly between consecutive squares is nonsquare. Therefore for

\[
K^2<n<(K+1)^2,
\]

\[
\boxed{
|\mathcal F(n)\setminus\mathcal F(n-1)|
=\frac{\tau(n)}2.
}
\]

Since `tau(n)=2` iff `n` is prime,

\[
\boxed{
K^2<n<(K+1)^2:
\quad
n\text{ prime}
\iff
|\mathcal F(n)\setminus\mathcal F(n-1)|=1.
}
\]

Thus primality in the open square basin is exactly **one-branch birth** in the full floor-quotient support dynamics.

## 5. Relation to P2 and the repeat-event repair

For a nonsquare distinct semiprime `n=pq`, `tau(n)=4`, so the birth multiplicity is `2`.

A prime cube `p^3` is also nonsquare and has `tau(p^3)=4`, hence also birth multiplicity `2`, despite `Omega(p^3)=3`.

Therefore the coarse classifier

\[
\text{birth multiplicity}\le2
\]

is not P2-sound by itself. The ambiguity is exactly a repeated factor branch.

This matches the owner-local adaptive P2 detector:

- pair interaction detects multiple distinct visible branches;
- repeat-event credit detects branch depth `v_p(n)>=2`;
- together they repair the birth-multiplicity ambiguity without penalizing genuine semiprimes.

## 6. Capacity no-go

Let

\[
B_K=
\sum_{K^2<n<(K+1)^2}
|\mathcal F(n)\setminus\mathcal F(n-1)|.
\]

If the basin were prime-free then trivially `B_K>=4K`, because all `2K` nonsquare states would have birth multiplicity at least `2`.

However direct exact evaluation shows the actual birth mass grows much larger than `4K`; e.g. at `K=2000`,

\[
B_K=32692>4K=8000.
\]

Hence a raw total-birth capacity argument cannot prove Legendre. The value of the theorem is state classification / future-signature structure, not a global branch-count shortage.

## 7. BRC interpretation

The floor-quotient set is a finite current-support object. Moving from `n-1` to `n` creates a finite birth fiber. The theorem identifies that fiber exactly with the upper half of the divisor lattice.

Freeze:

`FLOOR_QUOTIENT_NEW_BRANCHES_EQUAL_UPPER_DIVISOR_FRONTIER = true`.

`OPEN_SQUARE_BASIN_PRIME_IFF_ONE_BRANCH_BIRTH = true`.

`BIRTH_MULTIPLICITY_TWO_REQUIRES_REPEAT_EVENT_TO_SEPARATE_P2_FROM_PRIME_POWERS = true`.

`RAW_TOTAL_BIRTH_CAPACITY_DOES_NOT_PROVE_LEGENDRE = true`.
