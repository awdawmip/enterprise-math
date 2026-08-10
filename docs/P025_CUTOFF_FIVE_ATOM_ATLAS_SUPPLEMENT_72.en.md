# P025 Supplement 72 — Cutoff-Five Prime-Power Atom Atlas and Its Negative Boundary

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-paired-square-tail-stage61`  
Depends on: P025 Supplements 51, 69, 71  
Hard block: `NONE`

## 1. The cutoff-five hard slice has only sixteen ordered exponent types

Stage 71 proves that if a threshold-active cyclic orientation has

\[
H_i<5,
\]

then its two complementary blocks are prime powers

\[
\boxed{p^e,\quad q^f,\qquad e,f\in\{1,2,3,4\}.}
\]

The primes are distinct because the abc components are pairwise coprime.

If the active component is `c`, then

\[
N=p^e+q^f.
\]

If a side component is active, then the two complements contain the other side and `c`, and

\[
N=|p^e-q^f|.
\]

In both cases the exact projective denominator is

\[
\boxed{K=e q+f p.}
\]

Thus threshold activation on this atom is exactly

\[
\boxed{
m(N)\ge T(eq+fp),}
\]

or equivalently

\[
\boxed{
\operatorname{rad}(N)
\le
\frac{N}{T(eq+fp)}.
}
\]

All remaining difficulty now lies in the radical structure of a binomial prime-power sum or difference.

## 2. P025-T141 — the prime-prime shell can never activate

Take

\[
e=f=1.
\]

Then the denominator is

\[
K=p+q.
\]

For the sum orientation,

\[
N=p+q=K,
\]

but every positive integer `N>1` satisfies

\[
m(N)<N.
\]

Hence

\[
m(N)<K.
\]

For a difference orientation,

\[
N=|p-q|<p+q=K,
\]

and

\[
m(N)\le N<K.
\]

Therefore

\[
\boxed{
(e,f)=(1,1)
\Longrightarrow
\text{no threshold-one projective activation}.
}
\]

This is also consistent with Stage 69: two prime complements would leave too much squarefree structure for activation.

## 3. P025-NB15 — every other exponent shell is genuinely populated

The prime-prime shell is the **only** unordered exponent pair that can be removed using exponent data alone.

For every other unordered pair

\[
1\le e\le f\le4,
\qquad(e,f)\ne(1,1),
\]

there exists a primitive threshold-one activated triple in the cutoff-five atlas.

Exact fixtures are:

| exponent shell | primitive activated triple |
|---|---|
| `(1,2)` | `2 + 5^2 = 27` |
| `(1,3)` | `3 + 5^3 = 128` |
| `(1,4)` | `23 + 5^4 = 648` |
| `(2,2)` | `3^2 + 79^2 = 6250` |
| `(2,3)` | `5^3 + 19^2 = 486` |
| `(2,4)` | `7^2 + 576 = 5^4` |
| `(3,3)` | `2^3 + 1323 = 11^3` |
| `(3,4)` | `3^4 + 1250 = 11^3` |
| `(4,4)` | `2^4 + 14625 = 11^4` |

In the difference-mode rows, the two displayed prime powers are the complementary blocks and the middle integer is the active component.

Each fixture satisfies

\[
m(N)\ge eq+fp.
\]

Thus no theorem using only the pair `(e,f)` can eliminate any of these nine shells.

## 4. Same exponent shell can contain both activated and subunit states

Even a surviving exponent shell does not determine activation.

Compare two `(1,2)` sum atoms:

\[
2+5^2=27
\]

and

\[
2+3^2=11.
\]

For the first,

\[
K=2\cdot2+5=9,
\qquad
m(27)=9,
\]

so the c-oriented term reaches threshold one exactly.

For the second,

\[
K=2\cdot2+3=7,
\qquad
m(11)=1,
\]

so it remains subunit.

Therefore

\[
\boxed{
(e,f)+\text{sum/difference mode}
\text{ is still insufficient for the activation query.}
}
\]

Prime-base information, or information capable of determining the radical of `p^e +/- q^f`, must enter next.

## 5. Precision stopping rule

Stage 72 gives a concrete example of **coordinate saturation** in the precision architecture.

Starting from the low-capacity state, adding exponent precision is useful up to

\[
(e,f)\in\{1,2,3,4\}^2.
\]

But once this shell is known:

- `(1,1)` is decided as safe;
- every other shell remains genuinely mixed.

Further refinement of the same exponent coordinate cannot solve the future query, because the exponent coordinate is already exact.

The next useful coordinate must be of a different type: prime bases, congruence class, binomial factorization, or direct radical information.

This is a negative boundary against the idea that every unresolved task should be attacked by simply increasing precision along the coordinate already in use.

## 6. Relation to classical Diophantine families

The hard atom layer consists of equations of the form

\[
p^e+q^f=N
\]

or

\[
|p^e-q^f|=N,
\qquad e,f\le4,
\]

with an unusually small radical for `N` relative to the linear cross-capacity `eq+fp`.

Prime-power Diophantine equations, binomial factorization, Catalan/Pillai-type problems, Zsigmondy phenomena and related tools are established external mathematics. P025 should import those selectively rather than claim the atom families as new.

The project-side contribution is only the route from projective activation to this finite exponent atlas and the explicit proof that exponent-only refinement is exhausted at this point.

## 7. Executable assets

Added:

- `src/enterprise_math/abc_projective_low_capacity_atoms.py`;
- `tests/test_abc_projective_low_capacity_atoms.py`.

The executable atlas verifies the prime-prime impossibility and one exact activated primitive fixture for each of the nine remaining unordered shells.

## 8. Next frontier

No hard block exists. Continue with:

1. classify which prime-base congruence/factorization information is the cheapest next coordinate inside each shell;
2. prioritize shells where classical binomial identities or Zsigmondy-type primitive-divisor results give exact radical lower bounds;
3. preserve the negative result that exponent precision is exhausted rather than repeatedly enumerating larger prime bases without a theorem;
4. feed the `precision coordinate saturation -> switch coordinate family` pattern back to A2/P023.
