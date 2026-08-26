# P017×P018 square diagonal — G3C Matomäki–Radziwiłł terminal endpoint

Status: `EXACT SPECIALIZATION / PRIOR-ART NEAR-MISS / ANALYTIC TARGET OPEN`

No Legendre proof is claimed.

## C1. Half-rough Liouville is exactly a prime indicator on the MR factor range

Put

\[
y=\lfloor k/2\rfloor,
\qquad
f_k(n)=\lambda(n)1_{(n,P_y)=1}.
\]

The function `f_k` is completely multiplicative.  For `k>=9`, every `y`-rough
integer in `[k,2k]` is prime: a composite would have at least two factors
strictly exceeding `k/2`, whose product already exceeds `2k`.  Therefore

\[
\boxed{
f_k(n)=-1_{\mathbb P}(n)
\qquad(k\le n\le2k).
}
\]

Now consider the exact consecutive-square bilinear strip

\[
k^2\le n_1n_2\le k^2+2k,
\qquad
k\le n_1\le2k.
\]

If `f_k(n_1)f_k(n_2)` is nonzero, then both factors are prime.  Thus the left
side of the Matomäki--Radziwiłł bilinear geometry becomes a positive count of
prime-prime terminal pairs.

## C2. Exact relation to the Generation-1 half-cutoff semiprime tail

Let `T_central(k)` count half-cutoff terminal semiprimes `pq` in the open square
shell with

\[
k/2<p\le k<q\le2k.
\]

Then the finite `h=2` MR-shaped sum is exactly

\[
\boxed{
\sum_{\substack{k^2\le n_1n_2\le k^2+2k\\k\le n_1\le2k}}
 f_k(n_1)f_k(n_2)
=
T_{\rm central}(k)
+1_{\mathbb P}(k)
+1_{\{k,k+2\text{ twin primes}\}}.
}
\]

The first correction is the included lower square endpoint `k^2`; the second
is the doubled orientation of `k(k+2)` when both factors lie in `[k,2k]`.

The rest of the Generation-1 half-cutoff semiprime tail has `q>2k`.  Since
`p>k/2`, one has `q<2k+4`, so the only possible prime boundary values are

\[
q=2k+1,\qquad q=2k+3.
\]

Hence

\[
\boxed{
H_{1/2}(k)
\le T_{\rm central}(k)+2.
}
\]

This makes the 2016 bilinear geometry an exact mother object for the terminal
semiprime microscope developed internally.

## C3. What Matomäki--Radziwiłł actually prove

Their Theorem 2 concerns

\[
x\le n_1n_2\le x+h\sqrt x,
\qquad
\sqrt x\le n_1\le2\sqrt x,
\]

and, uniformly for multiplicative `f`, compares the normalized bilinear average
with the square of the long average of `f` on `[sqrt(x),2sqrt(x)]`.  The theorem
is stated for `h>=10` and has normalized error

\[
O\!\left(
\frac{\log\log h}{\log h}
+
(\log x)^{-1/100}
\right).
\]

The consecutive-square interval has `x=k^2` and normalized width

\[
\boxed{h=2.}
\]

Thus the published theorem does not cover the required constant-width endpoint.
Moreover, a fixed-`h` error of constant size would only give an `O(k)` terminal
bound, whereas the useful target is

\[
\boxed{
T_{\rm central}(k)\ll k/\log^2 k.
}
\]

To obtain that order through the MR identity, the special-function endpoint
would need a normalized error of order `O(1/log^2 k)` (or better), because

\[
\frac1k\sum_{k\le n\le2k}f_k(n)
=-\frac{\pi(2k)-\pi(k^-)}{k}
\asymp-\frac1{\log k}.
\]

## C4. Relation to floor-prime prior art

Runbo Li's 2023 floor-prime theorem gives asymptotics for the number of
integers `n<=X^theta` for which `floor(X/n)` is prime whenever
`theta>435/923`; in particular the range contains `theta=1/2`.

That controls one primality condition in the reciprocal floor geometry.  It
does **not** in the result consumed here also require the outer variable `n`
to be prime.  The terminal staircase requires exactly this second prime
condition.

Thus the missing object can equally be described as

`prime-on-floor-prime correlation at the X^(1/2) outer scale`,

or as the special-`f_k`, `h=2` endpoint of the MR bilinear geometry.

## C5. Current role in the proof hierarchy

This route attacks only the **terminal semiprime tail**.  Even a proof of

\[
H_{1/2}(k)\ll k/\log^2 k
\]

would still require a pointwise lower bound for the corresponding half-rough
survivor mass in order to deduce a prime.  Therefore G3C is not a standalone
Legendre route.

Its value is sharper:

1. it identifies a known bilinear mother theorem for the internal reciprocal
   staircase;
2. it isolates the exact prior-art boundary `h>=10` versus required `h=2`;
3. it replaces a generic "reciprocal prime correlation" request by a precise
   special-function error target.

## Sources

- K. Matomäki and M. Radziwiłł, *Multiplicative functions in short intervals*,
  Ann. of Math. 183 (2016), 1015--1056, especially Theorem 2.
- R. Li, *On some problems of primes with the floor function*, arXiv:2308.16301
  (2023), especially Theorems 1.1 and 1.2.
