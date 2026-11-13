# PREFIX-765 / Research 6 — A sharper exact upper bound for the Gamma mixed-curvature phase threshold

Date: 2026-11-14. Status: **AUTHOR_EXACT_RATIONAL_REDUCTION / UNREVIEWED / NOT_ADMITTED**.

**Scientific input remains frozen:** `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. This paper concerns the *external independent two-Gamma-clock auxiliary model* only; it is not an assertion about native X6 dynamics or P000 transfer.

## The exact question and the inherited evidence

For the frozen 189-layer BRC stopping kernel let `C_p,C_z` be independent conditionally Erlang/Gamma stopping clocks, and put

`Y(p,z)=max(C_p,C_z)`, `mu(p,z)=E Y(p,z)`, `W(p,z)=Var Y(p,z)`, and `V_q(p,z)=q^2 W(p,z)-q mu(p,z)` for `q>0`.

PREFIX-763 defines the global nonnegative mixed-curvature threshold `q_c=1/(2 max Theta)`, where its derived mixed-derivative factorization gives global mixed supermodularity for `0<q<=q_c`. PREFIX-764 previously proved `q_c<190006/1000000` from one rational rectangle.

The **unchanged** input for the present finite reduction is `research_notes/portable_direct/PREFIX760_R6_EXACT_GAMMA_VARIANCE_RESULTS.json`, 24,743 bytes, SHA-256 `1a480a9a05c4773f82091037fa8f6b695855ffbb885b21e804d56fdc181d4e76`. That source contains full exact rational numerator/denominator certificates for `delta W(z)=W(1/4,z)-W(0,z)` and `delta V_2(z)=V_2(1/4,z)-V_2(0,z)` at six specified rational `z` values.

The recoverable exact mean difference is
```
delta mu(z) = 2 delta W(z) - delta V_2(z)/2,
```
since `V_2=4W-2mu`. This uses no floating point arithmetic.

## Theorem 765.1 — sharpened rational upper bracket

Let `R=[0,1/4] x [1/16,5/64]`, and write `Delta_R` for the rectangular mixed difference with the orientation `f(p_1,z_1)-f(p_0,z_1)-f(p_1,z_0)+f(p_0,z_0)`. Then the exact frozen input yields

```
Delta_R mu < 0,  Delta_R W < 0,
q_R := (Delta_R mu)/(Delta_R W),
69741060/1000000000 < q_R < 69741061/1000000000.
```

For every `q>q_R`,

```
Delta_R V_q = q Delta_R W (q-q_R) < 0.
```

Therefore the global threshold from PREFIX-763 obeys the **strict rational bound**

```
                 q_c < 69741061/1000000000
                     = 0.069741061.
```

In particular, `q=7/100` is a simple rational strict-negative certificate: `Delta_R V_(7/100)<0` (approximately `-0.0017542395349285534`, for display only). The previous PREFIX-764 upper bound was `0.190006`; the new upper endpoint is smaller by a factor of approximately `2.7244495`.

**Proof.** Parse the four exact Fraction fields of the two rows `z=1/16` and `z=5/64` from the SHA-pinned PREFIX-760 data. Recover the means from `V_2=4W-2mu`. Integer cross-multiplication gives both strict negative differences and both stated rational inequalities for `q_R`. The displayed factorization of `Delta_R V_q` is an algebraic identity. A globally nonnegative continuous mixed derivative implies a nonnegative mixed difference on every rectangle, via double integration. Hence any `q>q_R` cannot be at or below `q_c`, proving `q_c<=q_R<69741061/10^9`. The separate `q=7/100` inequality is checked in exact rational arithmetic. QED.

## Theorem 765.2 — signed curvature occurs for all q >= 7/100

PREFIX-762 provides the *separate* rectangle `R_+=[0,1/4]x[1/4,1/2]` with `Delta_(R_+) W>155` and `Delta_(R_+) mu<0`; therefore `Delta_(R_+) V_q>155q^2>0` for every `q>0`. Combine this with the strict negative `Delta_R V_q` for `q>=7/100`. Consequently **for every real `q>=7/100`**, the frozen auxiliary `V_q` has both positive and negative mixed rectangular differences: it is neither globally supermodular nor globally submodular. This improves the guaranteed signed-curvature interval without claiming the exact `q_c`.

## Finite reproducibility and limits

The companion `PREFIX765_R6_RECTANGLE_PHASE_SCAN_CHECK.py` enumerates all 15 unordered rational-endpoint rectangles formed from the six existing `z` points at fixed `p=[0,1/4]`; 13 have both `Delta_R mu<0` and `Delta_R W<0`. It chooses the smallest **among those 13 exact ratios**, at `z=[1/16,5/64]`, and checks the reported rational bounds and `q=7/100` witness with Python `fractions.Fraction`. Local execution returned `ALL_CHECKS_PASS PREFIX765`. The quoted 24,743-byte original certificate is not reconstructed or newly audited; no new 189-layer scientific input was introduced.

This is an author-level, finite-certificate consequence of the prior frozen calculation. It does not establish that the selected rectangle minimizes the ratio over *all real rectangles*, independently review earlier lemmas, establish native P000/X6 transport, or add any previously uncertified `1/768` exclusion area.

**Next:** use exact rational derivative kernels to shrink the phase threshold further, preferably with a certified continuous-rectangle or Bernstein-box sign oracle; independently evaluate an actual remaining Gamma comparator box before claiming increased area coverage.
