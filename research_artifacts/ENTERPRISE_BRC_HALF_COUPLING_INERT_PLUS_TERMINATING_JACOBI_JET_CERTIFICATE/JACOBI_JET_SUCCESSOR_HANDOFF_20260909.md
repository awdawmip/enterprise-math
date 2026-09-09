# Inert-Plus Jacobi-Jet Successor Handoff — 2026-09-09

Status: `DURABLE_HANDOFF / PARENT_STRICT_REDUCTION_FROZEN / LC_SUCCESSOR_PUBLISHED / SECOND_DIGIT_P3_FRONTIER_DEFERRED`

Parent task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-TERMINATING-JACOBI-JET-CERTIFICATE`
Parent publication: `TP2-A19C97A703AF47D1CBEC`
Parent objective: `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`

This file is a continuity index for successor researchers. It does not grant theorem, Working Truth, Foundation, review, or task-publication authority.

## 1. Start here: immutable durable chain

The strongest frozen parent result is available at immutable commit
`f6ac88de1e02e2b0f1b05e673a5cb3802c4e680f`.

Read these in order:

1. `research_result_records/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-TERMINATING-JACOBI-JET-CERTIFICATE/RR-82F6383FB6634F72B457.json`
2. `research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE_RETURN_20260828.md`
3. `research_artifacts/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE/ur_legendre_companion_connection_frontier_20260909.json`
4. parent task publication `research_task_records/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-TERMINATING-JACOBI-JET-CERTIFICATE/TP2-A19C97A703AF47D1CBEC.json`.

The first-digit continuation is already an official immutable V2 task:

- task: `RS-ENTERPRISE-BRC-INERT-PLUS-LEGENDRE-COMPANION-CONNECTION-CERTIFICATE`
- publication: `TP2-E55A63488AC0A711D567`
- taskbook: `research_tasks/ENTERPRISE_BRC_INERT_PLUS_LEGENDRE_COMPANION_CONNECTION_CERTIFICATE_20260909.md`
- state at publication: `READY / P2 / MEDIUM / CONTINUATION`.

A successor working the first digit should consume that taskbook and its pinned sources, not reconstruct the parent from chat history.

## 2. Frozen theorem-strength facts

For primes

`p ≡ 13,19 (mod 24)`, `p=6m+1`, `n=(p-1)/3=2m`, and `t^2=1/2`, the parent execution proved at theorem strength:

- the terminating quadratic/Legendre transport `H_m(z)=Q_m(1-z)` in the required finite field interface;
- the discriminant `-24` Hesse-CM zero `Q_m(1/2)=P_n(t)=0 (mod p)` (`CM0`);
- simple-root transversality `Q'_m(1/2) != 0 (mod p)` (`SIMPLE`).

The parent then proved exact equivalences

`JT0 <=> UR`,

where

`UR: (g/p)(-6 Q'_m(1/2)) = 1 (mod p)`,

and

`JT2 <=> UR + LIFT`,

where the second digit is the single scalar lift

`LIFT: ((g/p) h - 1)/p = R_p (mod p)`

after the parent cutoff-safe reconstructions. The cutoff-sensitive `Phi_xx` information remains inside `g/p (mod p^2)`; it was not discarded.

The later Legendre-companion frontier gives another exact equivalence

`JT0 <=> UR <=> LC`,

with

`LC: g/p = -t W_{n-1}(t)/6 (mod p)`,

`W_{n-1}(t)=sum_{j=1}^n P_{j-1}(t)P_{n-j}(t)/j`.

`LC`, `UR`, `JT0`, `LIFT`, and full `JT2` remain unproved in the all-prime sense unless a later Result explicitly supersedes this handoff.

Do not reopen `CM0`, `SIMPLE`, the eliminated Clausen tails, or the earlier harmonic-block bookkeeping without an exact contradiction to the frozen chain.

## 3. First-digit task already published

The active continuation `RS-ENTERPRISE-BRC-INERT-PLUS-LEGENDRE-COMPANION-CONNECTION-CERTIFICATE` asks for a proof, refutation, or strict reduction of `LC`.

Its exact finite deformation is

`F_p(epsilon)=sum_{k=0}^{p-1} (-n/2+epsilon)_k ((n+1)/2-epsilon)_k /(2^k (k!)^2)`,

with `g=F_p(p/6)`.

The critical cutoff guards are:

- retain `F_p(0)/p`; `CM0` is divisibility, not exact vanishing of the divided digit;
- retain the post-termination terms resurrected to first p-adic order when `epsilon` leaves zero;
- do not replace the finite p-term deformation by an uncontrolled infinite hypergeometric parameter derivative.

Preferred mechanisms recorded in the task are a terminating parameter-derivative/telescoping route and a structurally distinct discrete Legendre Green/Wronskian or finite-field route.

## 4. Deferred second-digit / p^3 quadratic-transform packet

The material below is a research frontier, not a theorem and not a separately published task. The current sequencing rule is to close `LC/UR` before reopening `LIFT`, unless an authorized later task explicitly selects the independent p^3-transform theorem itself.

Work in the unramified quadratic ring with `s^2=2`, put

`t=s/2`, `u=(1-t)/2`, so `4u(1-u)=1/2` and for the target inert primes `u^p=1-u`.

Define

`g = sum_{k=0}^{p-1} (1/6)_k (1/3)_k /(2^k (k!)^2)`,

and

`L_p(u)=sum_{k=0}^{p-1} (1/3)_k (2/3)_k u^k /(k!)^2`.

The Mao-Pan quadratic-transform route supplies the mod-p^2 transport used in the exploratory reduction; the candidate p^3 defect is

`delta_p = (g-L_p(u))/p^2 (mod p)`

in `F_{p^2}=F_p[s]/(s^2-2)`.

### Exact finite regression, not proof

A fresh exact modular recomputation on 2026-09-09 checked every target prime `p<2000`:

- target primes: `77`;
- all had `g-L_p(u)` divisible by `p^2` in both quadratic coordinates;
- all `77/77` had equal coordinates in the basis `(1,s)`, hence
  `delta_p in (1+s) F_p`;
- sample coordinate values `(p,c_p)` in `delta_p=c_p(1+s)` include
  `(13,10)`, `(19,14)`, `(37,17)`, `(43,5)`, `(61,12)`, `(67,38)`, `(109,30)`, `(139,24)`.

This is falsification/regression evidence only. It must not be promoted to an all-prime statement without proof.

### Candidate structural explanation

The working derivation observes that the p^3 quadratic-transform defect, after extracting the forced `p^2` and the first post-classical support factor, is governed by the same hypergeometric differential operator as the symmetric Legendre/Hasse side. The inhomogeneous term is a finite geometric-sum-type polynomial that is anti-invariant under `u -> 1-u`. Therefore the symmetrized residual is forced into the homogeneous Hasse solution space. The remaining unresolved point is the exact homogeneous normalization at the supersingular root.

This mechanism is promising because Frobenius sends `u` to `1-u` and the observed defect line `(1+s)F_p` is a one-dimensional Frobenius eigendirection. The exact operator normalization and the exclusion of a residual Hasse component still require a durable proof; do not quote the exploratory differential equation as theorem strength.

### QTF3 candidate

A particularly small p^3 target suggested by this route is the fixed-point lift

`sum_{k=0}^{p-1} (1/3)_k(2/3)_k /(2^k(k!)^2)`

`    = sum_{k=0}^{p-1} (1/6)_k(1/3)_k /(2^k(k!)^2)    (mod p^3)`.

Call this candidate `QTF3` for handoff purposes. It is not proved here. Before using it as a successor task, verify the exact normalization/sign against the frozen definitions and prove that it is genuinely sufficient for the desired second-digit reduction rather than merely correlated with the finite regression.

## 5. BRC carrier / information-loss boundary

The adequate carrier for this research is not positive total branch mass. Preserve:

- the labeled truncation index `k`;
- p-adic valuation layers through the required p^2/p^3 precision;
- parameter-jet / derivative data until the finite connection has been justified;
- the two Frobenius-conjugate quadratic-extension ports `u` and `1-u`;
- sign/conjugation provenance.

Taking absolute values, merging the two conjugate ports, or retaining only a positive total loses exactly the cancellation needed by `UR/LIFT`.

## 6. Current smallest actions

First digit, dispatchable now: execute the already-published `LC` task and prove/refute/strictly reduce the finite connection while retaining the divided centered digit and resurrected cutoff tail.

Second digit, deferred packet: after `LC/UR` closes, revisit `LIFT` using the p^3 quadratic-transform/Frobenius eigendirection. The first proof obligation is to turn the observed `delta_p in (1+s)F_p` into an all-prime theorem or to produce a counterexample; only then identify its scalar coefficient and its exact contribution to `R_p`.

## 7. Explicit nonclaims

- no proof of `LC`, `UR`, or `JT0` is claimed here;
- no proof of the defect-line statement for all primes is claimed here;
- no proof of `QTF3`, `LIFT`, or `JT2` is claimed here;
- no proof of Zhi-Wei Sun A14(ii) is claimed here;
- finite regression is not theorem evidence by itself.
