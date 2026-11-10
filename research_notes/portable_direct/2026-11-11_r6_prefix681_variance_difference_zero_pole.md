# PREFIX-681-R6 — Certified variance-difference zero and pole obstruction in BRC diagonal–edge crossover

Date: 2026-11-11 (Asia/Shanghai). Scope: independent BRC observer research unit, no shared Task claim.
**Mathematical status:** AUTHOR_DERIVED / EXACT_RATIONAL_REPLAY_CHECKED / UNREVIEWED / NOT_ADMITTED.

Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Predecessor: PREFIX-680 (`2c91711f60aa74d93880780929f532da24140ec0`), with frozen 189-row survivor recurrence, center jets and third-derivative certificate. Model probabilities are scalar observer parameters; they are **not** new primitive spatial coordinates. P000 and ACTIVE world view are unchanged.

## Research question and discovery

The prior proposed route attempted to certify `A(z)>0` and monotone `q₀(z)` across the entire bracket `0.052<z<0.054`. Here `A(z)=W(z,z)-W(0,z)`, `B(z)=μ(z,z)-μ(0,z)`, and `q₀(z)=B(z)/A(z)`, where `μ=E[Y]`, `W=Var[Y]`, and `Y(p,z)=max(Y_p,Y_z)` for independent frozen Poissonized first-stop clocks.

**New exact result:** The variance difference `A` changes sign **inside**
$
  \frac{2663}{50000}<z<\frac{5327}{100000}
  \qquad (0.05326<z<0.05327).
$
Moreover throughout the entire larger interval `53/1000≤z≤107/2000`, the mean difference obeys **`B(z)>6`**.

It follows that there exists at least one `z_A` inside the displayed width-`10^{-5}` rational interval with `A(z_A)=0`, `B(z_A)>6`. For every real `q>0`,
$
 D_q(z_A):=V_q(z_A,z_A)-V_q(0,z_A)
 =q^2A(z_A)-qB(z_A)=-qB(z_A)<-6q,
 \quad V_q=q^2W-qμ.
$
Because `B(z_A)≠0`, the quotient `q₀=B/A` is **undefined and has a genuine pole at every such zero**. At least one of those zeros is sign-changing (analyticity and strict endpoint signs), so there the quotient diverges with opposite signs on the two sides. Therefore no proof of `A(z)>0` or a finite continuous `q₀` over the complete `0.052≤z≤0.054` bracket is possible for the frozen model. This is an exact obstruction to that proposed extension **and a constructive change of research variable**, not a negative conclusion about the mother objective.

## Exact finite-model certificate

The attached `PREFIX681_R6_VARIANCE_ZERO_CERTIFICATE.py` reuses the checked frozen recurrence and Poissonized moments from `PREFIX676_R6_STOCHASTIC_ORDER_AND_DIAGONAL_CROSSING.py` (same repository directory). The recurrence has 189 nonempty rows, zero survivors at row 189, and 9,529 occupied survivor-count cells. The exact acceptance comparison is
$
40(n+1)\binom nk a^k(2^{18}-a)^{n-k}>2^{18n},
$
with the same frozen interval decision as PREFIX-676/680. The finite moment kernels are
$
K_{nm}=\frac{\binom{n+m}{n}}{2^{n+m+1}},\quad
J_{nm}=\frac{n+m+1}{2}K_{nm},
$
$
\mu(p,z)=\sum_n(s_n(p)+s_n(z))-\sum_{n,m}K_{nm}s_n(p)s_m(z),
$
$
H(p,z)=\frac{\mathbb E[Y(p,z)^2]}2=
\sum_n(n+1)(s_n(p)+s_n(z))-\sum_{n,m}J_{nm}s_n(p)s_m(z),
\quad W=2H-\mu^2.
$

Python integer and `Fraction` evaluation (no floats in sign decisions) gives:

| `z` | `sgn A(z)` | `⌊10^6 A(z)⌋` | `sgn B(z)` | `⌊10^6 B(z)⌋` |
|---|---:|---:|---:|---:|
| `2663/50000` | + | 803 | + | 7,930,886 |
| `5327/100000` | − | −16,179 | + | 7,932,168 |

These are exact integer-floor comparisons from full rational values; no floating sign interpolation is used. Polynomiality of the finite moment expressions gives continuity; the intermediate value theorem supplies the zero.

For the global `B` bound, reuse the previously checked exact PREFIX-680 center jet and third-derivative certificate at `b=53/1000`:

$
 B(b)>\frac{789}{100},\quad B'(b)>0,\quad
 |B''(b)|<1000,\quad
 sup_{0le zle 1/2}|B'''(z)|le 69527880576.
$

Write `h=z-b`, `0≤h≤1/2000`. Taylor's theorem and the positive first derivative imply
$
 B(b+h)>\frac{789}{100}
 -\frac{1000}{2}\left(\frac1{2000}\right)^2
 -\frac{69527880576}{6}\left(\frac1{2000}\right)^3
 =\frac{402586093}{62500000}>6.
$
This works on **every real point**, not merely endpoints. The new checker verifies the exact rational bound; the center jets and uniform third-derivative estimate remain explicitly attributed to PREFIX-680 rather than claimed as newly independent evidence.

## Consequences for the search

The quotient `q₀(z)` remains useful **only on subdomains with certified nonzero A**. For crossing analysis over `0.052..0.054`, use instead the division-free residual
$
 F_q(z)=qA(z)-B(z),\qquad D_q(z)=qF_q(z),
$
whose derivatives are polynomials, with no quotient singularity. In any point of `[53/1000,107/2000]` where `A(z)≤0`, `F_q(z)<-6` for all `q>0`. A future direct signed-Bernstein certificate for `F_q'(z)=qA'(z)-B'(z)` may establish uniqueness of the crossovers without requiring `A>0` throughout the interval.

**Precisely not proved:** uniqueness of the zero of `A`; negativity of `A` at every point right of the bracket; uniqueness of every variance crossover over the whole `0.052..0.054` interval; the two-parameter global variance maximum. The endpoint signs and bound prove the stated existence and obstruction only.

## Reproduction and follow-up

Run `python3 research_notes/portable_direct/PREFIX681_R6_VARIANCE_ZERO_CERTIFICATE.py` from the repository root. It imports the unchanged PREFIX-676 exact model, checks both full-rational signs, the inherited PREFIX-680 exact Taylor inequality, and emits `ALL_CHECKS_PASS PREFIX681-R6`. The companion `PREFIX681_R6_RESULTS.json` records the actual evaluated endpoints and analytic scope.

Next independently executable unit: certify `F_q'(z)<0` (or exact sign structure) on rational Bernstein boxes covering `[0.052,0.054]×[12,24]`, separately from pole-free `q₀` subintervals. Then apply the complete `p=0` boundary maximum from PREFIX-675 as the competing benchmark for true two-dimensional parameter pruning.

Provenance: author calculation, frozen model; neither formal Task Result nor independent review has occurred.


## Additional theorem: crossovers for every large real slot parameter

Let `z_A` be the **smallest** zero of `A` in `(53/1000,5327/100000)`. Such a zero exists because PREFIX-680 gives `A(53/1000)>0` and the new exact endpoint calculation gives `A(5327/100000)<0`. By the choice of smallest zero and continuity, `A(z)>0` throughout `[53/1000,z_A)`.

The certified center ratio from PREFIX-680 obeys `q₀(53/1000)<18`. Therefore for **every real q≥18**, the division-free residual `F_q(z)=qA(z)-B(z)` satisfies
$
F_q(53/1000)=A(53/1000)(q-q₀(53/1000))>0,\qquad
F_q(z_A)=-B(z_A)<-6.
$
Consequently **every real `q≥18` has at least one diagonal–edge variance crossover `z_q∈(53/1000,z_A)`**. This extends crossover *existence* beyond the prior sampled slot interval `[12,24]`; it uses the same finite frozen observer and is not a claim of unique roots.

There is also a certified large-slot limiting law. For each `q≥18`, choose any root `z_q∈(b,z_A)`, where `b=53/1000`. On the compact interval `[b,z_A]`, `B` is bounded, while `A` is continuous and strictly positive on every `[b,z_A-ε]` for `ε>0`. The root identity `qA(z_q)=B(z_q)` therefore forces `z_q→z_A` as real `q→+∞`. This conclusion does **not** require an assumed global monotonicity of `q₀`.

This constructive endpoint/limit result suggests separating the crossover study into the finite-`q` pole-free chart and the `q^{-1}` near-zero chart: the second has the regular equation `A(z)-q^{-1}B(z)=0`, which remains well defined across `A=0`.
