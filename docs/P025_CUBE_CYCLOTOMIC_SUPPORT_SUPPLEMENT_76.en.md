# P025 Supplement 76 — Cyclotomic Support Rigidity of the Centered Prime-Cube Factors

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-cyclotomic-stage76`  
Base: frozen Stage-75 head `a4a3cc935210ef06be1ab09af1d322481ab07cfe`  
Depends on: P025 Supplement 75  
Hard block: `NONE`

## 1. The centered quadratic factors are homogeneous cyclotomic factors

For distinct odd primes

\[
p>q
\]

Stage 75 introduced

\[
E=p^2-pq+q^2
\]

and

\[
D=p^2+pq+q^2.
\]

These are the homogeneous cyclotomic factors

\[
\boxed{E=\Phi_6(p,q),\qquad D=\Phi_3(p,q).}
\]

They arise from

\[
p^3+q^3=(p+q)E
\]

and

\[
p^3-q^3=(p-q)D.
\]

The projective formulas from Stage 75 depend on multiplicity inside `E` and `D`. Their prime support is highly restricted.

## 2. P025-T146 — `E` and `D` are coprime

First,

\[
\gcd(E,pq)=\gcd(D,pq)=1.
\]

Indeed modulo `p` or `q`, each quadratic factor reduces to the square of the other prime.

Also

\[
D-E=2pq.
\]

Any common divisor of `D,E` therefore divides `2pq`. But both `D,E` are odd because `p,q` are odd, and neither shares a prime with `pq`. Hence

\[
\boxed{\gcd(E,D)=1.}
\]

So the two centered cube quadratic factors have disjoint prime supports.

## 3. P025-T147 — every non-3 prime divisor is `1 mod 6`

### Divisors of `D=p^2+pq+q^2`

Let a prime `r` divide `D`. Since `r` does not divide `q`, the residue

\[
x=pq^{-1}\pmod r
\]

is defined and satisfies

\[
x^2+x+1\equiv0\pmod r.
\]

Thus

\[
x^3\equiv1\pmod r.
\]

If `x=1`, then `3=0 mod r`, so `r=3`. For `r!=3`, `x` has exact multiplicative order three. Therefore

\[
3\mid r-1.
\]

Since `r` is odd,

\[
\boxed{r\equiv1\pmod6.}
\]

### Divisors of `E=p^2-pq+q^2`

Now

\[
x^2-x+1\equiv0\pmod r.
\]

Multiplying by `x+1` gives

\[
x^3+1\equiv0\pmod r.
\]

If `x=-1`, then again `r=3`. Otherwise `x^3=-1` and `x` has exact order six. Thus for `r!=3`,

\[
6\mid r-1,
\]

so again

\[
\boxed{r\equiv1\pmod6.}
\]

Consequently every prime divisor of either quadratic factor lies in

\[
\boxed{\{3\}\cup\{r:r\equiv1\pmod6\}.}
\]

## 4. P025-T148 — the prime `3` never repeats

If `3|D`, then `p,q` are both nonzero modulo three and

\[
p\equiv q\pmod3.
\]

Using

\[
D=\frac{p^3-q^3}{p-q}
\]

and the ordinary LTE identity for the prime three,

\[
v_3(p^3-q^3)=v_3(p-q)+v_3(3),
\]

one gets

\[
\boxed{v_3(D)=1.}
\]

Similarly, if `3|E`, then `p≡-q mod 3`, and from

\[
E=\frac{p^3+q^3}{p+q}
\]

LTE gives

\[
\boxed{v_3(E)=1.}
\]

If one of `p,q` is itself three, neither quadratic factor is divisible by three.

Thus

\[
\boxed{v_3(E),v_3(D)\in\{0,1\}.}
\]

## 5. P025-C21 — every repeated cyclotomic prime is `1 mod 6`

Combining P025-T147–T148:

\[
\boxed{
r^2\mid E\text{ or }r^2\mid D
\Longrightarrow
r\equiv1\pmod6.}
\]

The exceptional cyclotomic prime `3` is allowed in the support but can never contribute multiplicity residual.

Therefore all multiplicity information coming from the centered quadratic factors is supported on primes `1 mod 6`.

## 6. Consequences for Stage-75 activation

### Cube sum

Stage 75 proves

\[
\rho_{(3,3),+}
=
\frac{\varepsilon_B g_B m(E)}{6\operatorname{rad}(B)}.
\]

If this reaches one, then `m(E)>1`, so `E` is nonsquarefree. P025-C21 gives

\[
\boxed{
\rho_{(3,3),+}\ge1
\Longrightarrow
\exists r\equiv1\pmod6:\ r^2\mid E.
}
\]

Thus the cube-sum hard state must contain a repeated primitive cyclotomic prime.

### Cube difference

Stage 75 gives

\[
\rho_{(3,3),-}
=
\frac{\varepsilon_A g_A m(A)m(D)}{6B}.
\]

If the quadratic factor contributes nontrivial residual, then every repeated prime in that contribution is again `1 mod 6`.

The radius `A` may carry unrelated multiplicity, so the difference shell has two distinct sources of hidden information:

1. ordinary repeated-prime structure in `A`;
2. cyclotomic repeated-prime structure in `D`, supported only on `1 mod 6` primes.

## 7. Exact examples

### Activated cube sum

For

\[
(q,p)=(5,59),
\]

\[
E=3211=13^2\cdot19.
\]

The repeated prime is

\[
13\equiv1\pmod6.
\]

### Activated cube difference

For

\[
(q,p)=(5,101),
\]

\[
D=10731=3\cdot7^2\cdot73.
\]

The prime three occurs only once; the repeated prime is

\[
7\equiv1\pmod6.
\]

### Both quadratic factors nonsquarefree

For

\[
(q,p)=(13,109),
\]

\[
E=7^3\cdot31,
\qquad
D=3\cdot67^2.
\]

The two repeated supports are disjoint and both are `1 mod 6`, as predicted.

## 8. Precision interpretation

Stage 75 changed coordinates from prime bases to centered quadratic forms. Stage 76 compresses their multiplicity-support language further:

\[
\text{factorization of }E,D
\to
\text{support class }\{3\}\cup(1\bmod6)
\to
\text{repeated support only in }1\bmod6.
\]

For the future query

> "can the quadratic factor supply any projective multiplicity residual?"

prime three can be discarded immediately, and only the `1 mod 6` support can matter.

This is another theorem-native coordinate switch: the next useful information is cyclotomic congruence support, not a larger exponent table.

## 9. Prior-art / novelty discipline

Cyclotomic factorizations, multiplicative orders modulo primes, LTE, and the congruence restrictions on prime divisors of `Phi_3/Phi_6` are classical mathematics. P025 claims none of them as new.

The project-specific result is their exact use as the minimal-looking multiplicity-support interface for Stage-75 projective cube atoms. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 10. Executable assets

Added:

- `src/enterprise_math/abc_prime_cube_cyclotomic_support.py`;
- `tests/test_abc_prime_cube_cyclotomic_support.py`.

The executable layer factors exact working examples and asserts the prime-support restrictions independently of the closed Stage-75 projective formulas.

## 11. Next frontier

No hard block exists. Continue with:

1. lift repeated factors `r^2|Phi_3/Phi_6` to explicit root-of-unity congruence classes modulo `r^2`;
2. quantify the cost of those congruence classes before attempting another global tail;
3. separate radius multiplicity from cyclotomic multiplicity in the cube-difference shell;
4. import deeper cyclotomic/primitive-divisor theorems only if they give a real radical or access gain beyond this elementary support classification.
