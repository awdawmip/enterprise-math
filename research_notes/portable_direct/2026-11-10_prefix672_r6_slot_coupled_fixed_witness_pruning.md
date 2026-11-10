# PREFIX-672-SC-R6 — Slot-coupled fixed-witness exclusion with a cubic Bernstein certificate

Date: 2026-11-10 (Asia/Shanghai).
Mode: independent portable TASK_RESEARCH. Researcher-ID: `EM-DIRECT-C11F8D`; activity: `RA-337DF0BCC7D3C8D024F92E2B`.
Frozen science pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Status: `AUTHOR_DERIVED / EXACT_RATIONAL_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED`.

## Mother question, selected unit, and native BRC interface

The mother objective is the full-domain maximum of the frozen 189-layer two-information-direction first-stop **statistical observer** variance on `[0,1]^2`. The observer parameters `p,z` are probability parameters, **not** two native spatial axes or a native X6 plane. This result retains the frozen integer survivor multiplicity carrier, moment observer and q-sampling law. The BRC interface is `COMPOSE_APPLIED` from PREFIX-659, 660, 668, 670, 671-FW. No native X6 process or new 96-port experiment is inferred.

The local question: can the PREFIX-671-FW single rational competitor `Q=(0,19/128)` eliminate more of the previously certified boundary rectangle, by retaining the exact q-dependence and the positive quadratic normal penalty rather than pairing independent q-worst cases?

Write `mu=E[Y]`, `W=Var(Y)`, `V_q=q^2 W-q mu`, `I=[607/4096,609/4096]`, and `R=[0,1/64] x I`. Real `12<=q<=24` is an analytic interpolation; actual sampling schemes are integral. Let `M(q)=max_{z in I}V_q(0,z)` with the unique edge maximizer `z_*(q)` from PREFIX-660.

## New theorem: fourfold narrowing of the unresolved fixed-witness strip

For **every real** `12<=q<=24`, every `z in I`, and every `p in [1/245197,1/64]`,

```
V_q(0,19/128)-V_q(p,z) > 1/300000 > 0.
```

Consequently the fixed rational competitor `(0,19/128)` excludes the entire closed substrip without evaluating `z_*(q)` or changing the model. The excluded area fraction within `R` is exactly

```
1-(1/245197)/(1/64) = 245133/245197 ≈ 0.999738985.
```

Compared with PREFIX-671-FW's cutoff `p>=1/61317`, the unresolved small-p width decreases by the **exact factor `245197/61317`**, about 3.99884.

## Proof — exact q-dependent coupling, no sampling grid

Prior author certificates are invoked at their original statements:

1. PREFIX-659 bounds `g'_12(Q)` strictly between -451 and -449 and `g'_24(Q)` strictly between 11344 and 11347, where `g_q(z)=V_q(0,z)`.
2. PREFIX-660 proves the strict negative curvatures `g''_12<-12800000`, `g''_24<-51500000` throughout `I`, and existence of `z_*(q)`.
3. PREFIX-670 proves throughout `R` that `M(q)-V_q(p,z) >= L(q)p+C(q)p^2+6400000(z-z_*(q))^2` with
   `L(q)=q*(76650/12+76595*(q-12)/144)` and `C(q)=(15000*q^2+221*q)/2`.

Set `t=(q-12)/12 in [0,1]` and define these positive affine rational functions:

```
A(t) = (1-t)*(451/12) + t*(11347/24)
B(t) = (1-t)*(12800000/12) + t*(51500000/24)
ell(t) = (1-t)*(76650/12) + t*(306490/24)
q(t) = 12+12*t
L(q) = q(t)*ell(t).
```

Because `g'_q(Q)/q=qW_z(Q)-mu_z(Q)` and `g''_q(z)/q=qW_zz(z)-mu_zz(z)` are affine in `q`, the predecessor endpoint bounds imply `|g'_q(Q)| <= qA(t)` and `-g''_q(z)>qB(t)`. The one-dimensional strong-concavity comparison yields the **strict** bound

```
0 <= M(q)-g_q(Q) < D(q) := q(t)*A(t)^2/[2B(t)].
```

Therefore throughout `R`,

```
g_q(Q)-V_q(p,z) >
     L(q)*p + C(q)*p^2 + 6400000*(z-z_*(q))^2 - D(q).
```

For `p>=1/N`, `N=245197`, discard the nonnegative z term, use monotonicity in p, and certify the rational function

```
E_N(t) := L(q)/N+C(q)/N^2-D(q)
        = P_N(t)/(2B(t)),
P_N(t) = 2B(t)*[L(q)/N+C(q)/N^2] - q(t)*A(t)^2.
```

`P_N` is a **cubic polynomial in t**. Direct exact rational expansion into the degree-three Bernstein basis `binom(3,j)t^j(1-t)^(3-j)` gives the four coefficients `beta_j`, j=0,...,3:

```
beta_0 = 468934256008280591 / 721458825708
beta_1 = 2560142094994810109 / 2164376477124
beta_2 = 12978210975416362535 / 8657505908496
beta_3 = 7437196790373 / 480972550472.
```

All four are strictly positive, with minimum `beta_3`. Because the Bernstein basis is nonnegative and sums to one, for all real `t in [0,1]`,

```
P_N(t) >= beta_3;  B(t) <= B(1)=51500000/24,
E_N(t) >= beta_3/(2*(51500000/24))
       = 22311590371119/6192521587327000000
       > 1/300000.
```

The strict original `M(q)-g_q(Q)<D(q)` then proves the stated strict gap for every `q,p,z` in the quantified domain, including interval endpoints.

For scope of the certificate: `N=245198` makes `E_N(1)<0`. Thus `245197` is the largest integer denominator attainable **by this specific single-cubic Bernstein sufficient bound**; this is not a claim about the actual variance comparison at smaller p. A different competitor or sharper source bounds may still improve it.

## Verification, model correspondence and evidence scope

Companion `PREFIX672_R6_SLOT_COUPLED_PRUNING_CERTIFICATE.py` uses Python `Fraction` and integers for all expansions, the four Bernstein coefficients, the certified margin, predecessor coefficient reconstruction, and the adjacent-denominator comparison. Companion JSON captures exact outputs. The local checker was executed successfully on 2026-11-10.

The proof of the universal interval statement is the rational Bernstein identity and positivity, **not** extrapolation from samples. This is an author implication certificate relying on the explicit PREFIX-659, 660 and 670 predecessor bounds; it does not rerun 189 survivor rows or independently review those predecessor proofs. The original BRC path-identity and moment observer are preserved by composition.

## Next useful research unit

(1) Replace the globally worst center-slope envelope `A(t)` with a signed center-gradient affine bound, split at its exact zero `q_0`, and separately evaluate the two sides. This should reduce `D(q)` near its zero and may sharpen the fixed-witness cutoff without recalculating any survivor rows.
(2) Incorporate `6400000(z-z_*(q))^2` using strict rational brackets for `z_*(q)` to remove parts of the remaining `0<=p<1/245197` band.
(3) Feed certified exclusions into the global symmetry-reduced triangle `0<=p<=z<=1/2` with signed Bernstein boxes; the full-square mother objective remains open.

Sources: `2026-11-10_prefix659_r6_exact_boundary_competitor_and_slot_transition.md` (commit `65536b12a268b619e0e1e89f685de3fb2162bea3`); `2026-11-10_prefix670_r6_slot_resolved_normal_stability.md` (commit `24c22a1496db5cb5da05ffef104b55b8d52f520e`); `2026-11-10_prefix671_r6_fixed_witness_uniform_pruning.md` (commit `4ff259f7078c40a796a8ffcf9dadef44d35015ee`). PREFIX-660 edge note was read through its quoted, unchanged source bounds, not independently rerun.
