# #1162 — character certificate phase hierarchy

Status: `RESEARCH_NOTE / DURABLE FRONTIER / NOT PROMOTED`
Researcher-ID: `EM-DIRECT-B62D`
At: `2026-09-06T19:05:00+08:00`
Source journal: `awdawmip/chatgpt-global-knowledge:journal/enterprise-math/2026-09-06/20260906T190500+0800-character-certificate-phase-hierarchy.md`
Progress-Event-ID: `character-certificate-phase-hierarchy-20260906`

## Three certificate phases

Let χ be a real nonprincipal Dirichlet character with parity a, and use

`F_χ(t)=Σ_{n>=1}χ(n)e^(-nt)`

and weighted theta

`Θ_{χ,a}(s)=Σ_{n>=1}n^aχ(n)e^(-n^2/(4s))`.

The normalized germ `g_χ(z)=F_χ(sqrt(z))/z^((1-a)/2)` is completely monotone iff `Θ_{χ,a}(s)>=0` for every s>0.

This yields:

### CM phase

Weighted theta is nonnegative. The normalized germ is completely monotone, so all-order finite-rotation correction truncations have strict alternating one-sided remainders, scaled errors form positive moment sequences, and Hankel positivity holds.

Example D=5, with theta positivity proved by self-reciprocity and positive residue blocks.

### Monotone-only phase

`F_χ(t)>0` for every t>0 but weighted theta changes sign. The Fermi error remains positive and the finite-rotation flow is monotone from one side, but complete-monotone/all-order alternating compression is invalid.

Exact example D=53:

`A_53(x)=x(1-x)^2(1+x)P_48(x)`

`P_48(x)=(1-x^4+x^8)+x^9Q_30(x)+x^40(1-x^4+x^8)`

with all coefficients of `Q_30` positive. Hence `A_53(x)>0` on `(0,1)` and `F_{χ53}(t)>0`.

At theta t=1, interval evaluation of the first ten positive-n terms is near `-0.1113564680`; a geometric Gaussian tail bound is below `0.001032`, hence the full half theta is <`-0.1103`. Therefore the normalized germ is not completely monotone.

### Signed phase

`F_χ` itself changes sign, so no universal monotone one-sided Fermi flow follows; signed/provenance-aware BRC sectors are necessary (absolute error bounds remain available).

Exact example D=173: the character polynomial satisfies `A_173(3/4)<0`, so `F_{χ173}` is negative at the corresponding positive t.

## Strict nesting

CM implies positivity of F after undoing the positive parity normalization. D=53 shows positivity of F does not imply CM. D=173 shows F positivity is not universal. Hence the phases are genuinely distinct.

## BRC implication

The phase hierarchy is an exact admissibility hierarchy for future measure-valued BRC:
- CM: positive measure carrier is valid;
- monotone-only: positive total error observer is valid, but not positive Taylor/measure compression;
- signed: retain signed branch/sector provenance.

Do not infer measure positivity from a few alternating coefficients or from a positive real-axis generating kernel alone.

## Next

1. Classify fundamental discriminants by the three phases.
2. Develop signed-sector rigorous bounds for monotone-only and signed characters.
3. Investigate theta nodal count as a signed-carrier complexity invariant.
