# RH BRC count-centered carry closure handoff — 2026-09-09

Status: `READY_FOR_STATE_MACHINE_PUBLICATION / NO_RH_PROOF / PRIOR_FREE_RESEARCH_PRESERVED`

Research provenance: `EM-FREE-3EAA93 / FREE_AXIOM_DISCOVERY / ANCHOR_EXPOSED`.

## Start here

This note is the canonical source-side handoff for the Sep-5 BRC-first RH line. A new researcher should consume the frozen results below rather than replaying them from chat history.

### Durable global journals

1. V11 predictive-port BRC frontier
   - repo: `awdawmip/chatgpt-global-knowledge`
   - commit: `f03d92f90f0e7db60fc2c188f0c980c5127a90f9`
   - path: `journal/enterprise-math/2026-09-05/20260905T111421+0800-free-brc-predictive-port-v11-3eaa93.md`
   - key outputs: exact quotient-port binary tree; fair positive-rational gauge; local valuation-Haar wedge; finite-depth observer cutoff; reduction to ordinary primes above sqrt scale; unresolved low ports `j=O(N^(1/3+epsilon))`.

2. V12/V13 Mellin-Haar and centered-carry RG
   - repo: `awdawmip/chatgpt-global-knowledge`
   - commit: `21614563efe3af4ee94d3853560146901ea3eb5a`
   - path: `journal/enterprise-math/2026-09-05/20260905T114657+0800-free-brc-mellin-haar-centered-rg-v13-3eaa93.md`
   - key outputs: exact local Mellin-Haar curvature symbol; RG energy factor `2^(2 Re(s)-1)`; lattice crossover `j^3/X`; centered carry RG `E(2n)=E(n)/2-H(n)+R_n`; inherited pair-energy factor `1/8`; a fixed dyadic polylog bound for the centered innovation is sufficient for RH.

3. V14 count-centered covariance / holonomy / deconvolution
   - repo: `awdawmip/chatgpt-global-knowledge`
   - commit: `78075758a90fef59fb78fc2c13473ecdd49a7681`
   - path: `journal/enterprise-math/2026-09-05/20260905T131532+0800-free-brc-count-centered-wavelet-deconvolution-v14-3eaa93.md`
   - key outputs: `A_n=sum_{m<=n} c_m(n)`, `alpha_n=A_n/n`, `J(n)=sum(c_m-alpha_n)Lambda(m)`; integer valuation wedge `g_n=n V_S-A_n V_P`; positive-rational holonomy `Omega_n=Q_n^n/M_n^(A_n)` with `log Omega_n=n J(n)`; RH-equivalent block energy `W(N)=sum_{N<=n<2N}(J(n)/n)^2`; fixed reciprocal wavelet killing the `s=1` density mode but retaining every nontrivial zeta-zero mode; exact Mobius-log deconvolution of the divisor-error geometry.

### Current toolized frontier

The exact BRC surfaces were toolized on branch `research/brc-count-centered-carry-v14-tool`, current head at handoff time:

`437d4d595f1495d3a0486b3c06e9e2b14567db82`

Review object: `#1250`, title `[EM-FREE-3EAA93] Toolize count-centered carry BRC holonomy`.

The branch now contains the V14–V17 exact finite surfaces:

- `src/enterprise_math/brc_count_centered_carry.py`
- `src/enterprise_math/brc_mobius_geometry_inversion.py`
- `src/enterprise_math/brc_mobius_log_gauge.py`
- `src/enterprise_math/brc_prime_cutoff_factorization.py`
- `src/enterprise_math/brc_large_prime_hard_core.py`

and their BRC regression tests. At the pinned head, 22/22 BRC unittest methods were reported passing. Treat these as exact finite tools and regression surfaces, not as asymptotic estimates or an RH solver.

V14 private research bundle retained for provenance:
- Drive file id: `1YL2RsFGJeSxK0kuXi47VUd0vGa8WlhAl`
- name: `EM-FREE-3EAA93_BRC_RH_v14_20260905.zip`
- ZIP SHA-256: `1791fdc8d80742c3d82e88b1e70822296419cbf51812aa43c0e83d964ce12fd0`
- recorded metadata: `shared=false`.

## Frozen mathematical frontier

Use

`c_m(n)=floor(2n/m)-2 floor(n/m) in {0,1}` for `m<=n`,
`A_n=sum_{m<=n} c_m(n)`, `alpha_n=A_n/n`,

and

`J(n)=sum_{m<=n}(c_m(n)-alpha_n)Lambda(m)`.

The constant background is removed exactly because `sum(c_m-alpha_n)=0`. For the selected-old/all-old BRC valuation totals `V_S,V_P`, define

`g_n=n V_S-A_n V_P`,
`Omega_n=prod_p p^(g_{n,p})=Q_n^n/M_n^(A_n)`.

Then

`log Omega_n=n J(n)`.

The current derived RH interface is

`W(N)=sum_{N<=n<2N} (J(n)/n)^2`.

The existing route proves: bounded `W` is RH-equivalent, and any fixed dyadic polylog bound `W(2^k)=O(k^A)` is sufficient for RH through the already-established stable RG plus Mellin/log-derivative reverse argument. No such all-scale bound has been proved.

Predictive-port and Mellin-Haar reductions localize the unresolved hard core near

`j=O(N^(1/3+epsilon))`, equivalently ordinary primes `p >= N^(2/3-epsilon)`.

At the crossover, physical port width, reciprocal-phase coherence width and lattice error all meet at scale about `N^(1/3)`.

## Post-V14 findings that must not be lost

These were obtained while toolizing and pressure-testing closure routes; they are research-frontier observations unless explicitly marked exact.

1. **Exact reciprocal quotient-shell compiler.** The geometry `K_gamma(n/d)` is piecewise constant on reciprocal `d` shells; the half-integer jump is exactly `tau(2r+1)-1`. This was added to the count-centered tool and regression tested.

2. **Exact Mobius inversion of the geometry lifting.** The divisor-lifted carry geometry obeys

   `sum_{a<=x} mu(a) K_gamma(x/a)=c_1(x)-gamma_c`.

   Thus much of the large cancellation in the Mobius-dilation representation is structural recoalescence/inversion, not automatically a new RH estimate.

3. **Mobius-dilation Gram pressure test.** In tested dyadic and several non-dyadic blocks, the diagonal contribution grows only polylogarithmically (empirically close to a cubic log scale), while the aggregate off-diagonal term was negative and cancelled roughly 98–99% of the diagonal. Pairwise Gram signs are mixed, so there is no pairwise-negativity proof. Strong negative contributions often appear on multiplicative chains such as `e=3d`; adjacent dilations can be positive. Eventual aggregate nonpositivity is a high-risk RH-strength candidate, not a proved lemma.

4. **Prime-port / Selberg closure audit.** A standard one-interval short-interval mean-square estimate cannot simply be inserted port by port and summed. The endpoints and lengths are coupled by reciprocal BRC ports, and the required statement is a simultaneous signed square-function/Bessel-type estimate over moving ports. A theorem at that strength would deliver the missing polylog bound and therefore is itself RH-strength in this interface. Do not assume the missing uniformity.

5. **Hard-prime skeleton no-go.** On the large-prime hard layer, the power-free skeleton is carry-blind; selection information lives in thickness. Do not compress to skeleton only.

6. **Exact-tool boundary.** Exact finite factorization, shell compilation, Mobius inversion and finite sign searches do not supply the required uniform asymptotic norm bound.

## Adjacent registered RH work

Current source main also contains `RH-ROAD-AUDIT-20260909`, `RH-ROAD-KERNEL-20260909` and `RH-ROAD-TAIL-20260909` under the composite-road program. The count-centered BRC line is mathematically adjacent to the kernel task but has a distinct frozen carrier and exact-tool stack. Reuse a genuinely relevant result from those tasks if available; do not duplicate their composite-road source audit or phase-kernel work.

## Exact next research question

Can one prove, for the original von Mangoldt weights and the exact count-centered carry observer, a fixed-polylog bound

`W(2^k)=O(k^A)`

for some fixed `A`, preferably after the low-port localization, by one of the following genuinely coupled mechanisms?

- a reciprocal-port square-function/Bessel inequality at the moving-port geometry;
- an exact valuation-Haar/martingale estimate that retains the original `log p` observer;
- a global Mobius-shell Gram/recoalescence theorem that controls the total off-diagonal interaction without pairwise absolute values;
- or a rigorous no-go that identifies the exact missing RH-strength estimate and redirects the route.

A claimed closure must distinguish exact identities, finite evidence and unconditional all-scale estimates. Any route that would imply RH must be independently audited at the new analytic inequality before being treated as closed.

## Do not replay

Do not restart generic large-sieve work below the already-resolved range; do not revert to fixed-half centering when exact count-centering is available; do not use total-only BRC collapse; do not discard thickness; do not replace signed interference by positive multiplicity; do not infer an all-scale sign from finite blocks; and do not treat ordinary Selberg short-interval mean square as the required coupled moving-port square function without proving the uniform aggregation step.
