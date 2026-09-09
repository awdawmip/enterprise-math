# EM-FREE-W59A / Issue #1159 state-machine handoff

Status: `DURABLE RESEARCH HANDOFF / FREE-RESEARCH RESULTS + OPEN VALIDATION FRONTIERS / NOT FOUNDATION`
Date: `2026-09-09`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Parent issue: `#1159 Wallis 与正弦乘积的离散旋转模态`
Parent objective id: `EM-FREE-W59A-ISSUE1159-WALLIS-SINE-ROTATION`

## 1. Immutable source pins

Two source lines must be distinguished.

1. Finite theorem / Lean extraction branch:
   - `free/1159-spectral-precision-lean-w59a@269b1cafac209e42d6770b0aae4a4d8d0a981f8a`
   - primary theorem packet: `research_notes/WALLIS_SINE_DISCRETE_ROTATION_SPECTRAL_PRECISION_THEOREMS_20260903.md`
   - finite-spectrum addendum: `research_notes/WALLIS_SINE_LEAN_FINITE_SPECTRUM_ADDENDUM_20260904.md`
2. Subsequent research-extension branch:
   - `free/1159-internal-phase-euler-w59a@9e6e9abe813aa17a7eff1ee8278e2f0e9f73312c`
   - this branch contains the internal-phase, spectral-RG, spectral-arithmetic, projective-factor, and BRC-integration generations described below.

Do not infer theorem strength from branch location alone. The first branch contains a large Lean-checked finite core; the second branch is a durable free-research notebook containing theorem-candidates, corrections, exact symbolic experiments, and several compatibility readouts that still require task-local verification.

## 2. Verified finite core to consume, not replay

The following frontier was independently rederived and, where stated below, formalized in Lean without `sorry` / `admit` / custom axioms on the finite-spectrum branch.

- Exact normalized Dirichlet determinant coefficient formula
  `F_M(x)=sum_j (-1)^j x^(2j)/(2j+1)! * prod_{r=1}^j (1-r^2/M^2)`.
- Central-factorial identity
  `(2j+1)! choose(M+j,2j+1)=M prod_{r=1}^j(M^2-r^2)`.
- Explicit compact analytic WSR-T02 error certificate with the exact `cosh/sinh` main term and factorial tail.
- Finite Hermitian realization, characteristic polynomial bridge, parity-factor splitting, and actual parity root products `q` and `2`.
- Exact local spectral decimation `R(u)=u(4-u)` and ordering-free parity-mode curvature collapse.
- Hamming/Krawtchouk finite shell: genuine integer spectrum `0,...,m`, complement-reflection parity, complete eigenbasis, literal restricted determinants, and the WSR-T05 Wallis determinant identity.
- Target-free Wallis squeeze and internally defined Wallis limit.
- Algebraic Richardson kernel and the finite rational sign datum `-268/405` used in the `tau<4` argument.

The classical Chebyshev/cosine spectrum on the Lean branch is a downstream finite compatibility layer only; it is not a native premise for the finite carrier.

## 3. Durable research extensions on the internal-phase branch

These are high-value theorem-candidates / proof routes that must be validated in their successor tasks rather than silently promoted.

### 3.1 Internal phase quantization and log-free Euler completion

Primary note:
`research_notes/WALLIS_SINE_INTERNAL_PHASE_QUANTIZATION_EULER_PRODUCT_20260904.md`.

Core route:

`finite continuant -> internal power-series S,C -> first positive phase tau -> exact phase quantization -> exact finite spectral product -> direct product-defect tail -> locally uniform Euler product`.

Candidate identity:
`D_n(2-2C(theta)) S(theta)=S((n+1)theta)`.
For `theta=k tau/M`, this internally quantizes every finite Dirichlet root before classical `pi` is named. It yields
`rho_(k,M)=2M S(k tau/(2M))`, fixed-mode convergence to `k tau`, and intrinsic bounds `2k <= rho_(k,M) <= k tau`.

A direct finite product-defect argument appears to replace the older logarithmic-tail route and gives sharper explicit compact tail bounds. A transient claim that the old log-tail statement had a domain error was retracted after rechecking; do not repeat that false correction.

### 3.2 High-order precision hierarchy and scaled spectral RG

The branch develops:

- arbitrary-order dyadic annihilation filters
  `A_m = prod_{r=1}^m (4^r E-I)/(4^r-1)`;
- explicit rational weights and the candidate stability bound `sum |w_{m,j}| < 2`;
- a two-direction precision lattice increasing with dyadic resolution and annihilation order;
- lower and upper radical-only completion brackets;
- single-scale arbitrary-order formal-phase completion certificates (commit `fd07b3c9a4311e4aa401c790eb774e131d4ef054`);
- scaled spectral RG fixed point and error eigenmodes (commit `b140675ff04e728a9a1b8d84b297156c98fdbd14`);
- exact finite RG equation in the physical variable and the first universal modified-equation correction operators.

The task is to separate exact finite identities, asymptotic expansions, sign-preserving bounds, and conjectural all-orders claims.

### 3.3 Prime-decimation semigroup and spectral arithmetic

The branch develops a multiplicative decimation family `R_n` with candidate semigroup law
`R_mn = R_m o R_n = R_n o R_m`, together with the normalized determinant cocycle
`H_mn(u)=H_m(u) H_n(R_m(u))`.

For prime powers this produces a spectral generation filtration. Candidate consequences include equal prime-adic layer root-products, divisor embeddings, primitive denominator factors, spectral Möbius inversion, monic polynomial gcd/CRT laws, full and primitive discriminants, and a native prime-power resultant law.

Key durable notes / commits:
- `research_notes/SPECTRAL_CYCLOTOMIC_NATIVE_RESULTANT_LAW_20260904.md` (later corrected to remove a circular induction route);
- spectral gcd/CRT and unit resultant theorem: commit `4561f211d7c91df9535079de2810afe70ae15832`;
- native full/primitive spectral discriminants: commit `39e12429b189c63e55b851cc5e5f8c3a89579de1`;
- native irreducibility of projective spectral factors: commit `9d8e8fbcc264a0144f48637b283b6be532771b00`;
- prime-power spectral Eisenstein/Frobenius congruences: commit `3363c8776daa1365bf7770ad0dff2ab7a52b284b`;
- native Galois group of projective spectral fields: commit `196f25f0c677e4673a090dd07b69befa82af0a9c`.

The latest native-resultant route introduces aggregate quantities `A_m(d)=|Res(Psi_m,Q_d)|` and a resultant Möbius inversion specifically to avoid the earlier circular dependence between the multiple and nonmultiple cases.

### 3.4 Spectral moments, Jordan totients, and even-zeta route

From the exact finite normalized determinant, the branch extracts reciprocal spectral elementary symmetric sums and Newton power sums. Candidate finite formulas include
`Z_1(M)=(M^2-1)/6`,
`Z_2(M)=(2M^4+5M^2-7)/180`,
and
`Z_3(M)=(8M^6+21M^4+42M^2-71)/7560`.

Primitive-denominator Möbius inversion converts the polynomial-in-`M^2` coefficients into Jordan totients. The asymptotic leading coefficients, combined with internal phase quantization and the uniform radius lower bound, give a finite-spectrum route to the standard even-zeta constants with `tau` in place of the later classical name.

Further branch generations:
- Riccati recurrence for even-zeta spectral coefficients: commit `ad6fbb0a1ac98d63ff99354569ca04c0f601ee50`;
- primitive spectral Dirichlet series and an `RH readout`: commit `6bbb4454f9f2ba3cb23409846ebf414ed1dc4028`.

Important boundary: `RH readout` is a compatibility / encoding direction to audit. It is not a proof of the Riemann Hypothesis and must never be reported as one.

### 3.5 Projective spectral factors, conductor, traces, and BRC integration

Later research compresses complement-paired roots into projective primitive factors and studies their arithmetic / BRC meaning.

Key durable generations:
- projective primitive factors and BRC root-block compression: commit `e98bb1b8dca13b3556e56b0eabfdffaac9beb36c`;
- spectral binomial completion and primitive Jacobian quotients: commit `5b97edc503e9433f331407a78cc03a742e5bac6d`;
- oriented rational BRC rotation chart and spectral quotient: commit `d5c3274743f1e4eee66f3685e56bf3c0d5a516a7`;
- BRC rotation formal-group division polynomials: commit `fe0871e6ff11563dd961c064c373b99020978c7a`;
- `research_notes/PROJECTIVE_SPECTRAL_CONDUCTOR_AND_COMPLEMENT_SHEETS_20260905.md`;
- `research_notes/RAMANUJAN_SUMS_AS_PROJECTIVE_SPECTRAL_GALOIS_TRACES_20260905.md`.

The latest conductor correction is material: for odd `d>1`, the complement-sheet identity gives `|Omega_d(4)|=1`; the earlier prime-power alternative at this midpoint was wrong because `2d` necessarily has at least two distinct prime divisors.

The Ramanujan-sum note proposes a projective spectral Galois-trace realization such as
`Tr(C_n(2-alpha_d)) = c_d(n)` after exact denominator-transition analysis. This should be independently rederived before use outside the task.

## 4. Corrections and semantic boundaries that successors must preserve

1. Smallest-positive-mode statements using `a_q` start at `q>=2`.
2. `tau<4` must use the explicit finite alternating-series sign certificate, not a shorthand spectral claim.
3. The previously quoted `R_64` diagnostic decimal was corrected; no symbolic theorem depends on it.
4. The superseded C2 graph-cover holonomy interpretation from the neighboring #1158 line is not an admissible premise. The preserved internal completion equality is a separate layer.
5. The temporary claim that the old WSR-T04 log-tail statement had a zero-denominator domain defect was retracted; the new direct product-defect method is a strengthening, not a repair of that alleged defect.
6. The first native resultant induction was potentially circular. Use the corrected `A_m(d)` / resultant-Möbius route or another independently noncircular proof.
7. The odd projective midpoint mass correction in `PROJECTIVE_SPECTRAL_CONDUCTOR_AND_COMPLEMENT_SHEETS_20260905.md` is authoritative for the research branch: `|Omega_d(4)|=1` for odd `d>1`.
8. Classical Chebyshev, roots of unity, ordinary cyclotomic theory, and classical `pi` may be used as compatibility checks only when the task explicitly allows them; they must not be silently promoted to native finite inputs.
9. Publication of any successor task grants no Working Truth, Foundation status, or canonical mathematical promotion.

## 5. Minimal reading order for successor researchers

Read in this order unless the taskbook narrows it further:

1. this handoff;
2. `free/1159-spectral-precision-lean-w59a@269b1cafac209e42d6770b0aae4a4d8d0a981f8a:research_notes/WALLIS_SINE_DISCRETE_ROTATION_SPECTRAL_PRECISION_THEOREMS_20260903.md`;
3. `free/1159-internal-phase-euler-w59a@9e6e9abe813aa17a7eff1ee8278e2f0e9f73312c:research_notes/WALLIS_SINE_INTERNAL_PHASE_QUANTIZATION_EULER_PRODUCT_20260904.md`;
4. for precision/RG work: commits `fd07b3c9a4311e4aa401c790eb774e131d4ef054` and `b140675ff04e728a9a1b8d84b297156c98fdbd14`;
5. for arithmetic work: `SPECTRAL_CYCLOTOMIC_NATIVE_RESULTANT_LAW_20260904.md`, then commits `4561f211...`, `39e12429...`, `9d8e8fbc...`, `3363c877...`, `196f25f0...`;
6. for zeta/moment work: commit `ad6fbb0a...`, then `6bbb4454...` with the RH boundary above;
7. for projective/BRC work: `PROJECTIVE_SPECTRAL_CONDUCTOR_AND_COMPLEMENT_SHEETS_20260905.md`, `RAMANUJAN_SUMS_AS_PROJECTIVE_SPECTRAL_GALOIS_TRACES_20260905.md`, and commits `e98bb1b8...`, `d5c32747...`, `fe0871e6...`.

## 6. State-machine integration plan

Five claimable integration tasks should be published from this handoff, all under parent objective `EM-FREE-W59A-ISSUE1159-WALLIS-SINE-ROTATION`:

1. internal phase quantization and Euler-product completion;
2. spectral arithmetic / primitive-factor theorem package;
3. spectral moments / Jordan totients / even-zeta and Dirichlet-series audit;
4. arbitrary-order precision hierarchy and scaled-RG error modes;
5. projective spectral / BRC rotation-atlas integration.

These tasks are intentionally separable so multiple researchers can work in parallel while consuming the same frozen source pins.
