# P025 Supplement 77 — Root-of-Unity Congruence Precision for Repeated Cube Factors

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-cyclotomic-stage76`  
Depends on: P025 Supplement 76  
Hard block: `NONE`

## 1. Repeated cyclotomic multiplicity is a prime-base congruence condition

Stage 76 proves that every repeated prime factor of

\[
\Phi_3(p,q)=p^2+pq+q^2
\]

or

\[
\Phi_6(p,q)=p^2-pq+q^2
\]

is congruent to one modulo six.

Suppose now that for such a prime `r` and integer `e>=2`,

\[
r^e\mid\Phi_3(p,q)
\]

or

\[
r^e\mid\Phi_6(p,q).
\]

Since `r` is coprime to `pq`, the labelled prime ratio

\[
\boxed{x=pq^{-1}\pmod{r^e}}
\]

is defined.

The multiplicity condition can be expressed entirely as a root-of-unity congruence for this ratio.

## 2. P025-T149 — repeated `Phi_3` factors are order-three congruences

If

\[
r^e\mid p^2+pq+q^2,
\]

then

\[
x^2+x+1\equiv0\pmod{r^e}.
\]

Therefore

\[
\boxed{x^3\equiv1\pmod{r^e}.}
\]

Modulo `r`, Stage 76 already shows `x!=1` because `r!=3`. Thus the order modulo `r` is exactly three. The order modulo `r^e` divides three and reduces to order three modulo `r`, so it is also exactly three.

Hence

\[
\boxed{
\operatorname{ord}_{r^e}(pq^{-1})=3.
}
\]

## 3. P025-T150 — repeated `Phi_6` factors are order-six congruences

If

\[
r^e\mid p^2-pq+q^2,
\]

then

\[
x^2-x+1\equiv0\pmod{r^e}.
\]

Multiplication by `x+1` gives

\[
x^3\equiv-1\pmod{r^e},
\]

so

\[
x^6\equiv1\pmod{r^e}.
\]

Modulo `r`, `x` has exact order six by Stage 76. Therefore the prime-power order is also exactly six:

\[
\boxed{
\operatorname{ord}_{r^e}(pq^{-1})=6.
}
\]

## 4. P025-T151 — exactly two local root classes at every prime-power level

For the polynomial

\[
f_3(X)=X^2+X+1
\]

or

\[
f_6(X)=X^2-X+1,
\]

the discriminant is

\[
-3.
\]

At every repeated cyclotomic prime `r`, one has `r!=3`, so the derivative cannot vanish at a root modulo `r`. Therefore every root modulo `r` has a unique Hensel lift to a root modulo every `r^e`.

Since there are exactly two primitive order-three or order-six roots modulo `r`, there are exactly two roots modulo `r^e`.

They are inverse to one another because both polynomials have constant term one. Thus the local allowed ratio state is

\[
\boxed{
\{\zeta_r,\zeta_r^{-1}\}
\subset
(\mathbb Z/r^e\mathbb Z)^\times.
}
\]

So a repeated prime-power factor does not merely say "some prime repeats". It restricts the prime ratio to **two labelled residue classes modulo the full repeated prime power**.

## 5. P025-C22 — multiple repeated primes give only `2^k` CRT ratio classes

Suppose the repeated cyclotomic part is supported on distinct primes

\[
r_1,\dots,r_k
\]

with full exponents

\[
e_1,\dots,e_k\ge2.
\]

Set

\[
\boxed{M=\prod_{i=1}^k r_i^{e_i}.}
\]

At each prime-power modulus there are exactly two local root choices. The moduli are pairwise coprime, so the Chinese remainder theorem gives exactly

\[
\boxed{2^k}
\]

allowed ratio classes modulo `M`.

Therefore the repeated cyclotomic factor state compiles to the finite congruence signature

\[
\boxed{
(M,\text{ one of }2^{\omega(M)}\text{ root-of-unity classes}).
}
\]

The full prime bases `p,q` are not needed for any future query that asks only for the repeated cyclotomic divisibility pattern.

## 6. Exact examples

### Cube sum `(q,p)=(5,59)`

\[
\Phi_6(59,5)=3211=13^2\cdot19.
\]

The repeated modulus is

\[
M=13^2=169.
\]

The ratio `59/5` modulo `169` is one of exactly two primitive order-six roots.

Thus the repeated multiplicity state has only two labelled ratio classes modulo 169.

### Cube difference `(q,p)=(5,101)`

\[
\Phi_3(101,5)=3\cdot7^2\cdot73.
\]

The prime three is simple and contributes no residual. The repeated modulus is

\[
M=7^2=49,
\]

and `101/5` is one of the two exact order-three roots modulo 49.

### Simultaneous but disjoint sum/difference multiplicity

For

\[
(q,p)=(13,109),
\]

\[
\Phi_6=7^3\cdot31,
\qquad
\Phi_3=3\cdot67^2.
\]

The sum signature lives modulo `7^3`; the difference signature lives modulo `67^2`. Stage 76 proves the two support sets are disjoint.

## 7. Precision interpretation

Stage 72 showed that exponent coordinates eventually saturate and prime-base information must enter. Stages 76–77 identify a much smaller prime-base coordinate than `(p,q)` itself:

\[
\boxed{
\text{repeated cyclotomic support}
\to
\text{root-of-unity residue signature of }p/q.
}
\]

The precision cost is controlled by the repeated modulus and only one binary root choice per repeated prime.

This is a concrete example of **congruence precision replacing value precision**: the future task needs a labelled residue class, not the exact primes.

## 8. Prior-art / novelty discipline

Cyclotomic roots of unity, Hensel lifting, multiplicative order and the Chinese remainder theorem are classical mathematics. P025 claims none of those results.

The project-specific result is the exact use of this congruence signature as the next theorem-native coordinate after exponent precision saturates in the Stage-75 cube atoms. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 9. Executable assets

Added:

- `src/enterprise_math/abc_prime_cube_cyclotomic_congruence.py`;
- `tests/test_abc_prime_cube_cyclotomic_congruence.py`.

The implementation records full repeated prime-power moduli, observed root ratios, inverse root pairs, exact orders, and the CRT root-choice count.

## 10. Next frontier

No hard block exists. Continue with:

1. convert the congruence signature into an exact finite incidence/cost bound for prime-base pairs before using any distribution theorem for primes in progressions;
2. compare this labelled residue precision with Stage-40 certificate congruence kernels — the algebraic mechanism is different but the finite-quotient semantics may share an A2 home;
3. keep `sum` and `difference` cyclotomic signatures separate because Stage 76 proves their supports are disjoint;
4. import prime-distribution or primitive-divisor theorems only if they materially improve the finite-state bound.
