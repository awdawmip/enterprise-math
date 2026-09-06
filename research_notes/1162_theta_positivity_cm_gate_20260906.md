# #1162 — theta-positivity gate for complete-monotone character corrections

Status: `RESEARCH_NOTE / DURABLE FRONTIER / NOT PROMOTED`
Researcher-ID: `EM-DIRECT-B62D`
At: `2026-09-06T18:40:00+08:00`
Source journal: `awdawmip/chatgpt-global-knowledge:journal/enterprise-math/2026-09-06/20260906T184000+0800-theta-positivity-cm-gate.md`
Progress-Event-ID: `theta-positivity-cm-gate-20260906`

## Corrected χ5 kernel

Discard the earlier exploratory wrong expression containing cosh(t). The correct mod-5 quadratic character kernel is

`F_{χ5}(t)=2sinh(t)sinh(t/2)/sinh(5t/2)`.

## General weighted-theta criterion

For a real nonprincipal Dirichlet character χ with parity `χ(-1)=(-1)^a`, a=0 or1, let

`F_χ(t)=Σ_{n>=1}χ(n)e^(-nt)`

and

`g_χ(z)=F_χ(sqrt(z))/z^((1-a)/2)`.

Then

`g_χ(z)=1/(2^a sqrt(π)) ∫_0^∞ s^(-(2a+1)/2)e^(-zs)Θ_{χ,a}(s)ds`,

`Θ_{χ,a}(s)=Σ_{n>=1}n^aχ(n)e^(-n^2/(4s))`.

Under standard primitive/nonprincipal convergence conditions, Bernstein's theorem and Laplace uniqueness give

`g_χ completely monotone on (0,∞) iff Θ_{χ,a}(s)>=0 for all s>0`.

This is the exact admissibility condition for promoting the parity-mismatch correction germ to a positive measure carrier and hence obtaining globally strict all-order alternating Taylor certificates.

## χ5 positivity proof

For χ5 define

`vartheta_5(t)=Σ_{n in Z}χ5(n)e^(-πn^2t/5)`.

Poisson summation gives self-reciprocity

`vartheta_5(t)=t^(-1/2)vartheta_5(1/t)`.

For t>=1 set `r=e^(-πt/5)`. Then

`vartheta_5(t)/2=Σ_{k>=0}[r^(5k+1)^2-r^(5k+2)^2-r^(5k+3)^2+r^(5k+4)^2]`.

For each block, the magnitude ratio of its negative pair to positive pair is

`r^(20k+8)[1-r^(10k+7)]/[1-r^(10k+3)] <= (7/3)e^(-8π/5)<1`.

Hence every block is positive for t>=1; self-reciprocity gives positivity for all t>0. Therefore

`g_5(z)=2sinh(sqrt(z))sinh(sqrt(z)/2)/[sqrt(z)sinh(5sqrt(z)/2)]`

is strictly completely monotone.

## All-order strict L(3,χ5) bounds

For `E_{5,N}=L(3,χ5)-R_{χ5,3,N}`,

`E_{5,N}=(5N)^(-4)∫_0^∞u^3 g_5(u^2/(5N)^2)/(e^u+1)du`.

Thus after factoring `(5N)^-4`, the scaled error is completely monotone in `(5N)^-2`. Every finite Taylor truncation is therefore a rigorous one-sided global bound.

Expansion:

`g_5(z)=2/5-z/3+67z^2/300-361z^3/2520+...`.

This recovers

`L(3,χ5)-R_{χ5,3,N}=7π^4/(187500N^4)-31π^6/(11812500N^6)+...`

with strict all-order alternating remainder signs.

## Non-universality / no-go examples

Complete monotonicity is not automatic for real quadratic characters. High-precision finite evaluations plus a Gaussian absolute-tail estimate give negative weighted theta at t=1 for primitive even quadratic discriminants D=53 and D=77. For D=53, the first ten positive-n terms sum to about `-0.1113564680`, while the absolute remaining tail is below `0.002094`, so the theta value is negative. Hence the corresponding normalized germ is not completely monotone.

This is a concrete no-go witness against universal positive-measure BRC compression for all real characters.

## BRC meaning

Before switching from signed/meromorphic branch data to a positive measure carrier, one must prove weighted-theta nonnegativity. A few alternating coefficients or positive real-t kernel values are insufficient. CM-negative characters must retain a signed/provenance-aware carrier.

## Next

1. Classify fundamental discriminants satisfying weighted-theta positivity.
2. For positive cases, derive optimal strict all-order certificate widths.
3. For negative cases, find a minimal signed sector decomposition giving rigorous bounds without false positivity.
