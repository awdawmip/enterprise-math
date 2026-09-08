# #1195 research handoff — critical-tail, selector, CM, and finite identification frontier

Status: `ACTIVE HANDOFF / CONSUME BEFORE SUCCESSOR EXECUTION`
Researcher: `EM-FREE-8C31A2`
Parent objective: `EM-PI-POWER-SPECTRAL-SELECTOR`
Source issue: `#1195` — Universal critical-tail law for rational Ramanujan `1/pi^c` series
Predecessor issue: `#1163` — Cross-family Ramanujan-type precision-pi comparison (`COMPLETED`)

## 1. What is already proved and must not be replayed

### A. #1163 cross-family spectral precision

The predecessor route established the representation-invariant spectral contraction datum

`rho = Lambda |z|`, `kappa = -log rho`,

with finite tail theorems, orientation/phase separation, Apéry–Sato and Chudnovsky controls, Weber Type-D/E hyperbolic coordinates, Pell-shell refinements, embedding-resolved precision, and finite pi interval certificates. Its reusable account-level record is:

- `projects/enterprise-math/ENTERPRISE_PRECISION_PI_CROSS_FAMILY_SPECTRAL_MECHANISM_20260903.md` in `awdawmip/chatgpt-global-knowledge`.

Do not reinterpret that work as an independent proof of any classical Ramanujan/CM identity; the analytic/modular completion remains external.

### B. #1195 CP1 — universal `1/pi^c` critical-tail theorem

Comment `5533544516` proves for a complement-symmetric hypergeometric kernel of degree `2c+1` and nonnegative `deg P <= c`:

`|T_(n+1)/T_n| <= rho F_c(n)` and `F_c(n)<1` for `n>=ceil(c/2)`.

The abstract worst-case threshold `ceil(c/2)` is sharp. Nevertheless every one of the 13 known convergent Cohen–Guillera `c=2,3,4` formulas has the stronger true threshold `N_* in {0,1}`. The universal critical exponent is

`T_n ~ C rho^n n^(-1/2)`.

### C. CP2–CP4 — normalization boundary and rank spine

- `5533565468`: outside the canonical reduced-residue gauge, a proved 2026 `1/pi^2` family can approach `rho` from above; the correct asymptotic state is two-scale, `log|T_n|=-kappa n+sigma log n+O(1)`.
- `5533600396`: for rank `r=2c+1`, bilateral negative modes activate first at shifted order `x^r`; the first nonzero negative-mode jet is the upside-down companion. The same rank controls the hypergeometric degree, negative-mode activation, upside-down denominator power, and finite Fourier bandwidth. A causal bridge to `p^(2c+1)` supercongruence depth is not proved.
- `5533621206`: the first `c` odd Taylor vanishings are equivalent, after finite-bandwidth completion, to a global extremal odd Fourier mode.

### D. CP5–CP11 — pi-free selector section

- `5533660662`: the `c` odd-jet equations act homogeneously on `c+1` coefficients of `P`; generically they determine a projective selector ray.
- `5533680882`, corrected by `5533727036`: nilpotent-matrix parity is valid only after the fixed gamma/base normalization is restored. Do not reuse the earlier unnormalized-even wording.
- `5533689202`: complement symmetry and odd rank give formal skew-self-adjoint Picard–Fuchs background, but self-duality alone does not select a Ramanujan point.
- `5533695230`: finite cofactor/minor reconstruction of the selector was identified.
- `5533738331`: polynomial selector and CM parameter are distinct coupled observables; e.g. `26390/1103 != pi sqrt(58)`.
- `5533745356`: for generic `z`, odd symmetry defines a selector section `z -> [P_z] in P^c`; Ramanujan points are arithmetic collapse plus a separate even/completion condition.

### E. CP12–CP14 — arithmetic collapse and class fields at `c=1`

- `5533768484`: a pi-free signature-4 scan over `z=q^-4`, `2<=q<=1000`, finds low-height rational selector hits only at `q=3,7,99`, recovering the complete classical fourth-power Type-D sublist; the primitive `q^-2 -> q^-4` double hits are exactly `q=3,99`, matching the earlier Pell precision ladders.
- `5533840645`: in signature `1/6`, `z=1728/j`; the selector recovers the complete class-number-one singular-modulus table, including the Chudnovsky ratio `545140134/13591409`. A one-step finite spectral correction already isolates that ratio at enormous rational height.
- `5533885992`: the `c=1` selector is identified exactly with Borwein/Masser class-field data: `B/A=6/(1-s2(tau))`. CM Galois conjugation transports the selector. This closes the scalar `c=1` class-field case; do not repeat it as the rank-5 theorem.

### F. CP15 — exact rank-5 pi-free selector in Picard–Fuchs / mirror–Yukawa data

Comment `5540836463` is the current rank-5 mathematical frontier. For a fifth-order MUM equation with Frobenius basis `w0,...,w4` and `P(theta)=A+B theta+C theta^2`, the two target-free odd conditions are

`P(theta) w1 = 0`,

`P(theta)(w3 - h zeta(3) w0) = 0`.

The first condition eliminates the `pi^2 w1` contamination in the second. Using mirror variable `q`, `D=q d/dq`, `t=log q`, `delta=D log z`, `D^3 T=1-K`, one can write

`[A:B:C] proportional to (F,nabla F,nabla^2 F) cross (G_h,nabla G_h,nabla^2 G_h)`,

where

`F=t-D^2T`,

`G=(1/6)t^3-T+t DT-(1/2)t^2D^2T`,

`G_h=G-h zeta(3)`,

`nabla=delta^-1 D + delta^-1 D log w0`.

The missing theorem is not existence of this section; it is its algebraicity/Galois behavior at CM or arithmetic points for rank 5 and then general `c`.

### G. CP16 — finite identification theorem; exact interval certificate still missing

Comment `5540925126` proves at theorem level that truncated selector entries have error

`O(rho^(N+1) N^(-1/2))`,

and, under a nondegenerate selector gap, the projective ray inherits the same exponential scale. Distinct primitive integer/rational projective rays of affine height `<=H` have separation on the order of `H^-2`; hence a certified selector enclosure narrower than `1/(2H^2)` contains at most one such ray. Therefore

`N_id(H)=2 log H/kappa + O(log log H)`, `kappa=-log rho`,

up to conditioning constants.

The numerical rank-5 four-item demonstration in CP16 is not yet an interval certificate. Do not return another high-precision-decimal-only reconstruction as completion.

## 2. Frozen conceptual boundaries

1. Finite spectral/selector theorems do not prove the `1/pi^c` evaluation.
2. Self-duality is a family-wide background structure, not the arithmetic selector of special points.
3. Odd-selector existence at generic `z` is not a CM criterion.
4. Low-height selector collapse alone is not sufficient for `1/pi^c` completion outside special modular loci.
5. The scalar `c=1` Borwein/Masser Galois bridge is prior art plus completed synthesis; successor work must add rank-5/general-`c` content or a genuine obstruction.
6. Any `2c+1` archimedean/p-adic identification remains conjectural until an exact valuation/filtration bridge is proved.
7. Interval-certification work must expose exact rational/ball bounds and condition/separation constants; floating-point proximity is evidence only.

## 3. Successor task split

Three independent claimable successor units are prepared from this handoff:

- `RS-1195-RANK5-SELECTOR-GALOIS-CLASSFIELD` — prove or kill rank-5/general-`c` class-field/Galois transport of the pi-free selector.
- `RS-1195-SELECTOR-INTERVAL-HEIGHT-CERT` — turn CP16 into an auditable finite interval/height uniqueness certificate on at least one nontrivial `1/pi^2` formula.
- `RS-1195-RANK-SPINE-PADIC-BRIDGE` — lower-priority pressure test of whether the analytic rank spine `2c+1` actually controls p-adic supercongruence depth.

These tasks share parent objective `EM-PI-POWER-SPECTRAL-SELECTOR` but are mathematically separable. Results may be positive, negative, or mixed.

## 4. First-read order for a new researcher

1. This file.
2. Issue `#1195` only at the checkpoint comments named by the selected task.
3. The selected taskbook.
4. For `c=1` background only when needed, consume CP14 rather than replaying singular-modulus scans.
5. Load external prior art only after the exact task-local object is fixed; distinguish classical modular/Picard–Fuchs results from the finite-precision synthesis.

## 5. Return discipline

Return exact statements, weakest assumptions, theorem/counterexample status, and source references. Preserve the separation:

`FINITE SPECTRAL DATA -> PI-FREE SELECTOR -> ARITHMETIC/HEIGHT RECONSTRUCTION -> EXTERNAL MODULAR COMPLETION`.

If a successor route fails, identify the smallest failed implication and leave the earlier layers intact.