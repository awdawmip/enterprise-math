# P025 Supplement 75 — Centered Factorization of the `(3,3)` Prime-Cube Shells

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-paired-square-tail-stage61`  
Depends on: P025 Supplements 72–73  
Hard block: `NONE`

## 1. The centered coordinate switch also works for cube shells

Let

\[
p>q
\]

be distinct odd primes and set

\[
\boxed{
B=\frac{p+q}{2},
\qquad
A=\frac{p-q}{2}.
}
\]

As before,

\[
\gcd(A,B)=1
\]

and `A,B` have opposite parity.

For the cutoff-five `(3,3)` shell there are two natural active forms:

\[
p^3+q^3
\]

and

\[
p^3-q^3.
\]

Both admit exact centered factorizations into one centered coordinate and one odd quadratic form.

## 2. P025-T144 — cube-sum projective formula

One has

\[
\boxed{
p^3+q^3=2B(B^2+3A^2).}
\]

Define

\[
E=B^2+3A^2.
\]

Because `A,B` have opposite parity, `E` is odd. Moreover

\[
\gcd(B,E)
=
\gcd(B,3A^2)
=
\boxed{\gcd(B,3)}
=:g_B
\in\{1,3\}.
\]

Let

\[
\varepsilon_B=
\begin{cases}
2,&2\mid B,\\
1,&2\nmid B.
\end{cases}
\]

Tracking the possible shared factor `3` and whether the leading factor `2` is already present in `B` gives

\[
\boxed{
m(p^3+q^3)=\varepsilon_B g_B m(B)m(E).}
\]

The cross-capacity of the two prime cubes is

\[
3p+3q=6B.
\]

Therefore the c-oriented projective term is

\[
\boxed{
\rho_{(3,3),+}
=
\frac{\varepsilon_Bg_Bm(E)}{6\operatorname{rad}(B)}.
}
\]

This replaces factorization of the full cube sum by one center radical and the residual of the quadratic form `E`.

## 3. P025-C19 — a squarefree quadratic factor certifies the cube-sum subunit basin

If `E` is squarefree, then

\[
m(E)=1.
\]

Also

\[
\varepsilon_Bg_B\le6,
\]

while `rad(B)>=2`. Hence

\[
\rho_{(3,3),+}
\le
\frac6{12}<1.
\]

Thus

\[
\boxed{
B^2+3A^2\text{ squarefree}
\Longrightarrow
\rho_{(3,3),+}<1.
}
\]

So cube-sum activation forces repeated-prime structure in the centered quadratic factor.

## 4. P025-T145 — cube-difference projective formula

Similarly,

\[
\boxed{
p^3-q^3=2A(3B^2+A^2).}
\]

Define

\[
D=3B^2+A^2.
\]

Again `D` is odd and

\[
\gcd(A,D)
=
\gcd(A,3B^2)
=
\boxed{\gcd(A,3)}
=:g_A
\in\{1,3\}.
\]

Let

\[
\varepsilon_A=
\begin{cases}
2,&2\mid A,\\
1,&2\nmid A.
\end{cases}
\]

Then

\[
\boxed{
m(p^3-q^3)=\varepsilon_A g_A m(A)m(D).}
\]

The prime-cube complement cross-capacity is still `6B`, so the active side term is

\[
\boxed{
\rho_{(3,3),-}
=
\frac{\varepsilon_Ag_A m(A)m(D)}{6B}.
}
\]

## 5. P025-C20 — double squarefreeness certifies the cube-difference subunit basin

If both

\[
A
\quad\text{and}\quad
D=3B^2+A^2
\]

are squarefree, then

\[
m(A)=m(D)=1.
\]

Since

\[
\varepsilon_Ag_A\le6
\]

and `B>1`,

\[
\rho_{(3,3),-}<1.
\]

Therefore

\[
\boxed{
A,\ 3B^2+A^2\text{ both squarefree}
\Longrightarrow
\rho_{(3,3),-}<1.
}
\]

This is the cube-difference analogue of the centered squarefree guard from Stage 74.

## 6. Exact examples

### Activated cube sum

Take

\[
(q,p)=(5,59),
\qquad
(B,A)=(32,27).
\]

Then

\[
E=32^2+3\cdot27^2=3211=13^2\cdot19.
\]

Here

\[
\varepsilon_B=2,
\qquad
g_B=1,
\qquad
m(E)=13,
\qquad
\operatorname{rad}(B)=2.
\]

Thus

\[
\boxed{
\rho_{(3,3),+}=\frac{13}{6}>1.
}
\]

### Safe cube sum

For

\[
(q,p)=(3,5),
\qquad(B,A)=(4,1),
\]

one has

\[
E=19
\]

squarefree, and

\[
\rho_{(3,3),+}=1/6.
\]

### Activated cube difference

Take

\[
(q,p)=(5,101),
\qquad(B,A)=(53,48).
\]

The formula gives

\[
\boxed{
\rho_{(3,3),-}=56/53>1.
}
\]

### Safe cube difference

For

\[
(q,p)=(3,7),
\qquad(B,A)=(5,2),
\]

one has

\[
D=79,
\]

and both `A=2` and `D=79` are squarefree. Hence

\[
\rho_{(3,3),-}=1/15.
\]

## 7. Why the coordinate switch matters

Stage 72 showed that exact exponent data cannot decide activation inside the surviving low-capacity shells. Stage 75 replaces the full prime-base binomial factorization by smaller centered observables:

### Cube sum

\[
(p,q)
\to
(B,A)
\to
\bigl(\operatorname{rad}(B),\ m(B^2+3A^2)\bigr).
\]

### Cube difference

\[
(p,q)
\to
(B,A)
\to
\bigl(B,\ m(A),\ m(3B^2+A^2)\bigr).
\]

The next precision coordinate is therefore not “more exponent detail” but the multiplicity structure of a classical quadratic form.

## 8. Classical algebra boundary

The sum/difference-of-cubes factorizations and the quadratic forms above are classical mathematics. Their relation to Eisenstein/cyclotomic arithmetic belongs to established number theory and must be imported rather than claimed by P025.

P025 owns only the exact projective-value reductions and the resulting task-relative safe guards. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 9. Executable assets

Added:

- `src/enterprise_math/abc_prime_cube_centered.py`;
- `tests/test_abc_prime_cube_centered.py`.

The module cross-checks both closed formulas against independently computed projective cyclic values.

## 10. Next frontier

No hard block exists. Continue with:

1. use classical primitive-divisor/cyclotomic results to lower-bound the radicals of `B^2+3A^2` and `3B^2+A^2` where possible;
2. seek a P018/P005 existing coordinate home before introducing new quadratic-form terminology;
3. repeat the coordinate-switch audit for quartic shells only if it produces a genuinely smaller theorem-native state;
4. freeze exponent-only refinement as exhausted and focus literature search on the new quadratic-form coordinates.
