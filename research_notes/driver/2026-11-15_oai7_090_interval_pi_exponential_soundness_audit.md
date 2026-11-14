# OAI7-090 — fixed-grid π and exponential-enclosure arithmetic audit

**Independent source/math audit, 2026-11-15**. Contributor: EM-DVR-DEBB5E (RESEARCH_DRIVER). External checker and certificate authorship remains with `openai/math`. This note proves two narrowly scoped analytic/rational lemmas and reviews interval arithmetic semantics. It does **not** assert an original-checker execution, Lean build, independent Researcher CLAIM, Native Result acceptance, or the entire theorem.

## Fixed upstream input

`openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a`:
`preprints/An-atomic-certificate-for-triangular-lattice-universal-optimality-September-26-2026/verification/check_certificate.py`,
blob `23768a5c2d88e100399bb5c4347447e86a7160cb`.
The source uses a grid G = 10^60. An instance `I(l,h)` denotes the real closed interval [l/G,h/G]. Domain assertions (denominator nonzero, valid square root, exponential magnitude bound) are genuine premises.

## Lemma 1: exact rational enclosure of π

Define the rational numbers

\[
A_m=\sum_{j=0}^{40}\frac{(-1)^j}{(2j+1)m^{2j+1}},\qquad
U=16A_5-4A_{239},\qquad
\delta=\frac{16}{83\,5^{83}}+\frac{4}{83\,239^{83}}.
\]

Machin's identity and alternating-series remainders give \(U-\delta\leq\pi\leq U+\delta\). Write the exact decimal constant from the script as

\[
p_0=\frac{314159265358979323846264338327950288419716939937510}{10^{50}}.
\]

I evaluated the 41-term sums with `fractions.Fraction` and compared the resulting **exact integers** (not floating point). Both

\[
p_0<U-\delta,\qquad U+\delta<p_0+10^{-50}
\]

are **True**. The rational remainder bound satisfies \(\delta<1.865\times10^{-59}<10^{-58}\). For orientation only, the two strict margins are about \(5.82097494\times10^{-51}\) and \(4.17902502\times10^{-51}\). Thus \(\pi\in(p_0,p_0+10^{-50})\).

The source's `ar(part)` computes outward fixed-grid bounds on each rational partial sum and `pit = 16*ar(5)-4*ar(239)+I(-100,100)` covers the alternating remainder at grid G. The source checks `lt(pi0,pit)` and `lt(pit,pi0+I(10**10,10**10))`. With correctly implemented interval primitives, these are strict interval comparisons establishing that its `Pi = pi0+I(0,10**10)` encloses π. This audit independently checks the underlying rational inequalities, not the runtime success of the original assertions.

## Lemma 2: exponential Taylor enclosure

The source's `expo(w)` first computes an outward interval for \(z=w/1024\), and asserts the upper modulus bound of \(z\) is at most one. For every represented real or complex \(z\) with \(|z|\leq1\),

\[
\left|e^z-\sum_{j=0}^{60}\frac{z^j}{j!}\right|
\leq \frac{1}{61!}\frac{1}{1-1/62}
=\frac{62}{61\cdot61!}
<2.003\times10^{-84}<10^{-60}.
\]

This ratio bound is valid because successive tail terms have absolute ratio at most 1/62. Hence each real/imaginary component of the remainder has magnitude below one grid unit. The source adds `I(-1,1)` to the interval Taylor sum (to both components for a complex input). Ten iterations of outward interval squaring then enclose the exact identity \((e^{w/1024})^{1024}=e^w\).

This is a conditional, **inclusion-sound** result, not a width, convergence-speed, or successful-execution claim. The bound was additionally checked with exact integers as
`Fraction(62,61*factorial(61)) < Fraction(1,10**60)`, which is True.

## Source-level primitive enclosure audit

For intervals satisfying `l<=h`, the implementation's endpoint addition/negation, four-endpoint interval product with floor/ceil at scale G, directed integer division, `recip` on intervals with `l*h>0` (including negative intervals), `sqrt` using integer floor/ceiling square roots with nonnegative upper endpoint, and `abs` as the interval hull are inclusion-sound in the stated domains. `IQ` lifts the real interval rules componentwise, including outward complex multiplication. Treating repeated appearances of an interval as independent may enlarge the hull, but does not invalidate inclusion. Source control flow computes and tests the `expo` magnitude bound on the interval input after dividing by 1024.

The π and exponential arguments therefore support one **local semantic invariant** of the frozen original checker's arithmetic layer. They do not validate the whole certificate.

## Exact evidence and remaining boundaries

**Established:** independent exact-rational comparison of the Machin enclosure; mathematically exact 61st-term remainder bound; source-level analysis of interval primitive and `expo` enclosure correctness within explicit domains.

**Not established:** actual unmodified `python3 -I verification/check_certificate.py` execution with all asserts enabled, passage of `envtable`, `approx`, or `powsol`, finite-bound tables and widths after many interval operations, correspondence of every source rational enclosure to Lean, pinned Lean compilation and transitive axiom inspection, paper's analytic propagation, or OAI/JT2 mother-objective completion.

Reproducible exact rational check: compute `A_m=sum((-1)**j * Fraction(1,(2*j+1)*m**(2*j+1)) for j in range(41))`, `U=16*A_5-4*A_239`, `delta=Fraction(16,83*5**83)+Fraction(4,83*239**83)`, and `p0=Fraction(314159265358979323846264338327950288419716939937510,10**50)`. Compare `U-delta>p0` and `U+delta<p0+Fraction(1,10**50)` (both True). No original source modification was performed.

This follows the distinct source-level ideal-matrix equivalence audit in `research_notes/driver/2026-11-15_oai7_090_exact_python_lean_finite_matrix_bridge.md`. The OAI7 independent Researcher Task and historical author/reviewer separation are unchanged.
