# EC49FVF — a 5-adic residual certificate beyond seven old prime coordinates

2026-11-21 (Asia/Shanghai). **AUTHOR_PROVED / EXACT_FRACTION_CROSSCHECKED / PARENT_DEPENDENT / NOT_REVIEWED / NOT_ADMITTED.**

## Model, pins and claim boundary

Independent portable continuation of EC49FVE (PR #2876, exact scientific commit 17a7555e92f35ce0bcb1cd7ae7704ccf50363b04); frozen BRC16943 scientific pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Current P000/ACTIVE worldview and present control policies are distinct from the frozen scientific input. This is the **derived Bernoulli hit observer**, not native signed X6 dynamics, a native time-phase theorem, or a physical claim. Full composite-minimax transfer is conditional on the unreviewed FUQ/FUR endpoint-reduction author results.

The exact rational model is
\[
\beta=\frac3{637},\quad \gamma=\frac{141024}{1653649},\quad
u=\frac{4822040484}{8132285009},
\]
\[
T_0=(1-x)(1-\beta x),\quad T_E=(1-x)(1+\gamma x),\quad
a=1-T_0=\frac{x(640-3x)}{637},\quad b=1-uT_E,
\]
\[
R=\frac{T_0}{uT_E},\qquad S=\frac{bR}{a},\qquad
t(x)=\frac{\log R}{\log S},\quad 0<x<1.
\]
The frozen strict probabilities imply \(1<R<S\). For any reduced rational \(x=m/d\), if \(t=h/k\) is rational in lowest terms, \(0<h<k\), then \(R^k=S^h\). Thus **every prime p** must satisfy
\[
k\,v_p(R)=h\,v_p(S). \tag{1}
\]
Finite prime compatibility is necessary, not sufficient, for a rational phase.

## Theorem: two infinite 5-adic obstruction families

For any reduced \(0<m<d\), \(5\nmid d\), the following are sufficient for \(t(m/d)\notin\mathbb Q\):

**(A)** If \(j=v_5(m)\ge2\), then
\[
(v_5(R),v_5(S))=(0,1-j).
\]

**(B)** If \(v_5(m)=1\) and the 5-adic unit \(y=m/(5d)\equiv-1\bmod5\), then
\[
v_5(R)=0,\qquad v_5(S)\ge1.
\]

Equivalently, **either of the two 5-unit denominator classes** \(m d^{-1}\equiv0,20\bmod25\) has irrational phase. This is a sufficient two-class sieve, not a classification of all 5-adic obstructions. The certified rational widths are dense in the real interval \((0,1)\): take arbitrarily large \(d\equiv1\bmod25\) and choose \(0<m<d\) in either prescribed residue close to any chosen fraction of \(d\), discarding non-coprime choices or choosing a prime denominator.

### Analytic proof

Exact constants yield \(v_5(u)=v_5(\beta)=v_5(\gamma)=0\), \(v_5(1-u)=2\), \(v_5(\gamma-1)=3\), \(v_5(1+\beta)=1\). If \(5\mid m,5\nmid d\), then \(u,T_0,T_E\) are 5-units, hence \(v_5(R)=0\).

For (A), \(j=v_5(x)\ge2\), and
\[
T_E-1=(\gamma-1)x-\gamma x^2,\quad
v_5(T_E-1)\ge \min(j+3,2j)\ge4.
\]
Therefore \(b=(1-u)-u(T_E-1)\) has \(v_5(b)=2\). Since \(v_5(640)=1\), \(v_5(3x)\ge2\), \(637\) is a unit,
\(v_5(a)=j+1\); consequently \(v_5(S)=1-j\).

For (B), write \(x=5y\), where \(y\equiv-1\bmod5\). Then
\[
a=\frac{25y(128-3y)}{637},\qquad v_5(a)=2,
\]
since \(128-3y\equiv1\bmod5\). An exact identity gives
\[
b=\frac{411225984x^2+4410814500x+3310244525}{8132285009}
 =\frac{25H(y)}{8132285009},
\quad H(y)=411225984y^2+882162900y+132409781.
\]
Modulo 5, \(H(y)\equiv4y^2+1\equiv0\), so \(v_5(b)\ge3\), hence \(v_5(S)\ge1\). Both (A) and (B) contradict (1) because \(v_5(R)=0\), \(v_5(S)\ne0\) and \(h>0\). QED.

## Strict new eight-coordinate witness

Let
\[
\boxed{x_*=\frac{471955466252550476437545415817070}
{534065128161609717579116674491301}}. \tag{2}
\]
This reduced rational lies in \((0,1)\). It is the CRT numerator \(m\) satisfying the eight residue constraints below; the denominator is \(d=N+1\), where \(N\) is their pairwise-coprime modulus product.

| modulus | residue of m |
|---|---:|
| \(4\) | 2 |
| \(3^7\) | 729 |
| \(7^5\) | 1814 |
| \(13^3\) | 157 |
| 25 | 20 |
| \(29^2\) | 23 |
| \(673^2\) | 295 |
| \(416677^2\) | 168371 |

Exact rational valuations for (2):

| p | \(v_p(R)\) | \(v_p(S)\) | conclusion |
|---:|---:|---:|---|
| 2 | -2 | -4 | compatible with \(t=1/2\) |
| 3 | -6 | -12 | compatible with \(t=1/2\) |
| 7 | -2 | -4 | compatible with \(t=1/2\) |
| 13 | -1 | -2 | compatible with \(t=1/2\) |
| 29 | 0 | 0 | no condition |
| 673 | 0 | 0 | no condition |
| 416677 | 0 | 0 | no condition |
| **5** | **0** | **1** | **strict contradiction** |

Every one of the **seven specified old primewise coordinates** is compatible with \(t=1/2\) (the large three are zero/zero), but the new 5-adic coordinate strictly excludes it. We do not assert that every other prime or all non-valuation methods are inconclusive. This demonstrates a strict additional residual distinguishing power for this **specific** seven-coordinate observer. It does not establish phase rationality for any width.

## Reproduction and limits

Run the companion Python 3 standard-library script EC49FVF_FIVE_ADIC_RESIDUAL_VERIFY.py. It uses exact Fraction arithmetic to check the constant valuations; exhausts **all reduced rational** \(0<m<d\le400\) satisfying the two families; reconstructs the CRT witness and its coprimality, and computes the eight prime valuation pairs. Observed results: **1,609** examples in family A, **1,622** in family B; the strict eight-coordinate witness passes; **ALL PASS**. These are finite arithmetic regression checks; the infinite statements are proved above.

Novelty comparison: EC49FVB already covered primes 29, 673, 416677, 2, 3; EC49FVC/FVD/FVE added primes 7, 13 and coupled 2/3/7/13 constraints. The new ingredient is **prime 5** and a witness where all seven listed old prime valuations leave the same possible ratio.

**Next:** lift the \(v_5(x)=1,\ y\equiv1\bmod5\) branch, where both \(H(y)\) and \(128-3y\) may have positive 5-adic valuations. Classify their valuation difference and combine the resulting residual with existing simultaneous prime constraints. Keep the upstream minimax transfer conditional, P000 unchanged, formal CLAIM/Review separate, and avoid claiming exhaustive irrationality from this sieve.
