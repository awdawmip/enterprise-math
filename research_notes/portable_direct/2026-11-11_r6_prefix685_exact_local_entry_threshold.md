# PREFIX-685-R6 — Exact 12-decimal entry threshold for the frozen BRC diagonal–edge variance crossing

Date: 2026-11-11 (Asia/Shanghai). Mode: author-side independent BRC observer research, no shared Task CLAIM or Result/Review admission. Researcher-ID: `EM-DIRECT-281535`; Research-Activity-ID: `RA-2CF2C17BBE1EC85D88270ACC`.

**Frozen scientific input:** `f42f2906d77f24085c123f3ccfe9667d41caa96d`. This is the 189-level finite Poissonized stopping-time *observer model*; the scalar `p,z` are observation probabilities, not Heartbeat World's native spatial axes. P000 and its X6 typing remain unchanged.

## Certified new theorem

For the same model, write `μ(p,z)=E[Y(p,z)]`, `W(p,z)=Var(Y(p,z))`, and `V_q(p,z)=q²W(p,z)-qμ(p,z)`. Set

```text
A(z)=W(z,z)-W(0,z)
B(z)=μ(z,z)-μ(0,z)
F_q(z)=q A(z)-B(z)
I=[0.0532600,0.0532610]; L=2663/50000=0.0532600
q_c=B(L)/A(L)
```

Then `A(L)>0`, `B(L)>0`, and **exact rational arithmetic** proves the strict 12-decimal bracket

```text
9872.453419496357 < q_c < 9872.453419496358 .
```

Combining this endpoint certificate with the already certified `F'_q(z)<0` on `I` for all real `q>=0` (PREFIX-682/684) gives the **exact complete local entry classification**:

For every real `q>=0`, `V_q(z,z)=V_q(0,z)` has a solution `z∈I` if and only if `q>=q_c`; this solution is unique. It is `L` at `q=q_c`, and lies strictly inside `I` for `q>q_c`. For **integer** `q>=0`, a solution exists in `I` if and only if `q>=9873`. The smooth increasing/concave branch conclusions of PREFIX-684 therefore begin at the exact newly evaluated threshold.

The previous `9816<q_c<9929` width of 113 is replaced by an interval of width `10^-12`. This precise entry threshold is a local observer-model theorem; it does not assert uniqueness of all crossings on `0.052<z<0.054` or complete the two-variable maximum.

## Exact computation and proof kernel

Use the original unmodified frozen survivor classifier in `PREFIX680_R6_EXACT_THIRD_ORDER_CROSSOVER_CERTIFICATE.py` (source commit `2c91711f60aa74d93880780929f532da24140ec0`). Its deterministic recurrence enumerates 189 survivor rows `R_n={k:count}`, with exactly 9,529 occupied `(n,k)` cells, and a final empty row. At rational `L`, compute the exact fractions

```text
s_n = Σ_{k∈R_n} R_n[k] L^k(1-L)^(n-k),     t_n=R_n.get(0,0)
K_ij = binom(i+j,i) / 2^(i+j+1)
J_ij = (i+j+1) K_ij / 2
< u,v >_K = Σ_ij u_i v_j K_ij,     < u,v >_J = Σ_ij u_i v_j J_ij .
```

The finite survivor-to-Poisson Gamma integration identity gives

```text
μ_d = 2Σs_n - <s,s>_K
μ_e = Σ(t_n+s_n) - <t,s>_K
H_d = 2Σ(n+1)s_n - <s,s>_J
H_e = Σ(n+1)(t_n+s_n) - <t,s>_J
B(L)=μ_d-μ_e
A(L)=2(H_d-H_e)-μ_d²+μ_e².
```

Here `H=E[Y²]/2`; the subscripts `d,e` mean diagonal and edge parameterizations. The formulas follow by integrating the exact finite survival series for the maximum of two independent Poisson first-stop clocks, so all sums have declared finite domains.

The exact computed fractions satisfy:

```text
803334881118283114227 / 10^24 < A(L) < 803334881118283114228 / 10^24
7930886194096894324395803 / 10^24 < B(L) < 7930886194096894324395804 / 10^24 .
```

Let `a0,a1,b0,b1` denote these respective integer interval endpoints and set `Q0=9872453419496357`, `M=10^12`. Two **strict integer cross-products** are independently checked:

```text
b0*M > Q0*a1
b1*M < (Q0+1)*a0 .
```

All endpoint numerators share the denominator `10^24`. Consequently

```text
Q0/M < B(L)/A(L) < (Q0+1)/M.
```

This small-integer certificate is a compact verifier for the displayed decimal bracket; the attached exact recurrence program additionally certifies that those enclosure integers really contain the frozen-model moments, using Python `int` and `Fraction` with no floating-point sign decisions.

## Execution and scope

Local reproduction with the fetched frozen acceptance/survivor and Gamma-kernel functions returned `ALL_CHECKS_PASS PREFIX685-R6`. The full exact 189-row survivor count was reconstructed; the derived `A(L)`, `B(L)`, `q_c` have large rational numerator/denominator lengths recorded in the JSON. The published verifier imports the existing source module from the same directory; it does not republish the predecessor kernel or alter its scientific input.

Dependency: the local **iff/uniqueness** consequence uses PREFIX-684's proved `F'_q<0` and endpoint signs. This run independently recomputes the exact endpoint moments and the 12-decimal threshold enclosure. Status: `AUTHOR_DERIVED / EXACT_INTEGER_FRACTION_RECOMPUTED / UNREVIEWED / NOT_ADMITTED`.

**Next scientific unit:** use the new sharp `q_c` for numerical/certified branch continuation near the left boundary, then build signed Bernstein derivative patches over `0.052≤z≤0.054` to count other crossings. In parallel, keep the PREFIX-675 exact edge maximum as the benchmark for two-dimensional variance exclusion.
