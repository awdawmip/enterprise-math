# Legendre Pressure Test — Supplement 22

Status: `PROVED REDUCTION + OPEN FRONTIER`  
Scope: exact prime-pair normal form for square-of-square diagonal realized high-band root repair  
Depends on: P017 L060–L062, P007 dual factor windows, P023-S9 realized repair counting  
Discipline: this is a reduction theorem. It does not assert that the resulting restricted Goldbach multiplicity is unbounded.

## 1. Setup

Fix

\[
K=t^2,
\qquad
t\ge6,
\]

and retain cofactor root `t` in the outer square basin

\[
(K^2,K(K+2)].
\]

By L060, every raw prime shell label reaching root `t` lies in

\[
\boxed{(t-1)^2+3\le p\le K.}
\]

Write

\[
p=K-a,
\qquad
0\le a\le2t-4.
\]

A quotient in root bucket `t` has the form

\[
q=K+b,
\qquad
0\le b\le2t.
\]

## 2. L063-A — Diagonal p-rough realizability is primality

Status: `PROVED`.

For every raw diagonal prime label `p` and every `q` in root bucket `t`,

\[
\boxed{q\text{ is }p\text{-rough}\iff q\text{ is prime}.}
\]

### Proof

From the raw factor window,

\[
p\ge(t-1)^2+3.
\]

For `t>=6` this is strictly larger than `t+1`. But

\[
q<(t+1)^2,
\]

so

\[
\sqrt q<t+1<p.
\]

If `q` were composite, it would have a prime divisor at most `sqrt(q)`, hence a prime divisor strictly below `p`, contradicting `p`-roughness.

Conversely, a prime `q` has no prime divisor below `p` except itself; here `q>=K>=p`, so it is `p`-rough. ∎

Thus the diagonal realizability filter converts the rough-shell problem into an exact prime-pair problem.

## 3. L063-B — Only two center offsets are possible

Status: `PROVED`.

Suppose `p=K-a` and `q=K+b` are the two prime factors of a realized diagonal state. Define

\[
c=b-a.
\]

Then

\[
\boxed{c\in\{2,4\}.}
\]

### Parity and positivity

For `t>=6`, both `p,q` are odd primes. Since `a=K-p` and `b=q-K`, `a` and `b` have the same parity. Hence `c` is even.

Also

\[
pq-K^2
=K(b-a)-ab
=Kc-ab.
\]

Because the state lies strictly above `K^2`, this quantity is positive, so `c>0`. Therefore `c>=2`.

### Excluding c>=6

The root bucket gives `b<=2t`, so if `c=b-a` then

\[
a\le2t-c.
\]

Hence

\[
ab=a(a+c)\le(2t-c)(2t)=4K-2ct.
\]

The basin upper bound `pq<=K(K+2)` gives

\[
Kc-ab\le2K,
\]

or

\[
(c-2)K\le ab.
\]

If `c>=6`, however,

\[
(c-2)K-(4K-2ct)
=(c-6)K+2ct>0,
\]

contradicting the two inequalities. Thus `c` cannot be `6` or larger. Since it is a positive even integer, only `2` and `4` remain. ∎

## 4. L063-C — Exact two-slice Goldbach classification

Status: `PROVED`.

Let `K=t^2` and `p=K-a` be prime with `0<=a<=2t-4`.

The label `p` is realized in root `t` if and only if at least one of the following holds.

### Slice 2

\[
\boxed{
q=K+a+2\text{ is prime},
\qquad
a(a+2)<2K.
}
\]

Equivalently,

\[
\boxed{p+q=2K+2.}
\]

Indeed

\[
pq-K^2
=2K-a(a+2),
\]

whose upper bound by `2K` is automatic; strict positivity is exactly the displayed inequality.

### Slice 4

\[
\boxed{
q=K+a+4\text{ is prime},
\qquad
2K\le a(a+4)<4K.
}
\]

Equivalently,

\[
\boxed{p+q=2K+4.}
\]

Here

\[
pq-K^2
=4K-a(a+4),
\]

and requiring it to lie in `(0,2K]` is exactly the displayed double inequality.

By L063-B no other offset exists, and by L063-A prime `q` is exactly the realizability condition. Hence the two slices are jointly necessary and sufficient. ∎

## 5. Exact repair multiplicity as a union, not a sum

Define the two left-prime label sets

\[
\mathcal P_2(t)
=
\{K-a:\ K-a,K+a+2\text{ prime},\ a(a+2)<2K\},
\]

and

\[
\mathcal P_4(t)
=
\{K-a:\ K-a,K+a+4\text{ prime},\ 2K\le a(a+4)<4K\}.
\]

Then

\[
\boxed{
P^{\rm sh}_{t^2,t}
=
\mathcal P_2(t)\cup\mathcal P_4(t)
}
\]

and therefore

\[
\boxed{
R^{\rm sh}_{t^2,t}
=
|\mathcal P_2(t)\cup\mathcal P_4(t)|.
}
\]

The union is essential. At `t=11`, `K=121`, the same shell label

\[
p=107
\]

has both witnesses

\[
107+137=244=2K+2
\]

and

\[
107+139=246=2K+4.
\]

So adding the two Goldbach representation counts would double-count one repair class.

This is another exact instance of the project-wide rule:

\[
\boxed{
\text{count realized state labels, not formal witness tuples}.}
\]

## 6. Consequence for the unboundedness frontier

The raw diagonal burden is already proved unbounded by L061. The realized diagonal burden is now reduced exactly to

\[
\boxed{
|\mathcal P_2(t)\cup\mathcal P_4(t)|.
}
\]

Therefore proving

\[
\sup_t R^{\rm sh}_{t^2,t}=\infty
\]

is equivalent to proving that these two restricted, near-central Goldbach slices produce arbitrarily many distinct left primes along the square sequence `K=t^2`.

This is much sharper than the previous statement that realizability is merely "related to prime pairs". It identifies the exact missing number-theoretic object.

No unboundedness claim is made here.

## 7. Tool feedback

This reduction illustrates the complete research-tool chain:

1. P007 dual window removes irrelevant factor labels;
2. the p-rough admissibility filter turns the envelope into actual shell states;
3. parity and basin inequalities collapse the surviving prime-pair geometry to two exact slices;
4. P023-S9 says the repair cost is the number of **distinct realized shell labels**, hence the union rather than witness count.

The final hard object is now a prime-pair counting problem, not an ambiguity about state semantics.

## 8. Executable specification

`diagonal_goldbach_slices(t)` in

- `src/enterprise_math/p017_high_band_root_precision.py`

constructs both slices and asserts that their label union equals the independently compiled realized p-rough shell labels. Regression covers `6<=t<=100` and includes the `t=11,p=107` double-witness example.
