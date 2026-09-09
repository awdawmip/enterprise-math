# Enterprise BRC inert-plus Jacobi-jet — durable successor handoff

Status: `RESEARCH_HANDOFF / PROVEN_FRONTIER_PLUS_NEW_CANDIDATE_REDUCTIONS / NO_THEOREM_PROMOTION`

Date: `2026-09-09`
Researcher: `EM-EBP6JT-25C94A`
Parent task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-TERMINATING-JACOBI-JET-CERTIFICATE`
Parent publication: `TP2-A19C97A703AF47D1CBEC`
Parent claim: `chatgpt-ebp6jt-20260907-1010-sol7f3a`
Parent objective: `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`

## 1. Do not restart the closed part

The durable 2026-09-07 execution at commit `a722292873eba2449f0959fad7b766a12741ff47` already froze an exact strict reduction. Its return is:

`research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE_RETURN_20260828.md`

and its deterministic checker is:

`scripts/check_enterprise_brc_half_coupling_inert_plus_terminating_jacobi_jet_certificate.py`.

For every prime `p=6m+1` with `p mod 24 in {13,19}`, write `P_{2m}(T)=Q_m(T^2)`. The following are theorem-level outputs of that frozen return:

- the terminating quadratic/Legendre transport `H_m(z)=Q_m(1-z)` in `F_p[z]`;
- the discriminant `-24` CM/Hesse-Hasse zero `Q_m(1/2)=0 mod p`;
- simple transversality `Q_m'(1/2) != 0 mod p`;
- `JT0` is equivalent to the single unit reciprocity certificate
  `UR: (g/p)(-6Q_m'(1/2)) = 1 mod p`;
- `JT2` is equivalent to `UR` plus one second digit
  `LIFT: ((g/p)h-1)/p = R_p mod p`;
- the cutoff-sensitive `Phi_xx` contribution remains inside `g/p mod p^2` and must not be dropped.

The same execution checked all 77 target primes below 2000 with zero regression failures. That finite scan is evidence only for the open certificates, not an all-prime proof.

Do **not** reopen the eliminated Clausen tail, harmonic-block arrays, CM-zero proof, or simple-root lemma unless an exact contradiction is found.

## 2. Frozen notation for the next stage

Let

`G_p(z)=sum_{k=0}^{p-1} (1/6)_k(1/3)_k z^k/(k!)^2`,

`g=G_p(1)`, and let

`L_p(u)=sum_{k=0}^{p-1} (1/3)_k(2/3)_k u^k/(k!)^2`.

Choose `t^2=1/2` in the unramified quadratic extension and `u=(1-t)/2`, so `4u(1-u)=1/2` and Frobenius interchanges `u` and `1-u` on the inert lane.

The Mao–Pan quadratic polynomial congruence supplies the rigorous mod-`p^2` transport between the corresponding truncated hypergeometric polynomials. Together with generalized Legendre reflection, the natural first-digit object can be carried on the Frobenius pair rather than by the original five parameter/harmonic jets.

## 3. New 2026-09-09 frontier A — UR-Legendre

The current continuation isolated the following smaller target for the first digit. Put

`n=(p-1)/3` and `t^2=1/2`.

The candidate ordinary-Legendre certificate is

`(P_{2n}(t)+2P_n(t)) P_n'(t) = -p t (mod p^2)`.

If the parameter-shift identification used in its derivation is independently revalidated, this is equivalent to `UR` and contains only ordinary Legendre values at one supersingular Frobenius point. The intended proof mechanism is the mod-`p^3` generalized-Legendre parameter recurrence at `a=-1/3`, evaluated at `t` and `-t`, with parity/reflection used to eliminate adjacent parameter terms; differentiating the same recurrence is expected to expose the transverse derivative.

**Status:** `HIGH_VALUE_CANDIDATE_STRICT_REDUCTION / EQUIVALENCE_REQUIRES_INDEPENDENT_REVALIDATION / NOT YET THEOREM`.

The successor must first prove the equivalence cleanly; finite agreement alone is insufficient.

## 4. New 2026-09-09 frontier B — QTF3 / Frobenius defect line

Continue the quadratic transform one p-adic digit. For the fixed-point specialization define the mod-`p^3` transform defect schematically by

`delta_p = (G_p(1/2)-L_p(u))/p^2 mod p`.

Exact computations in the unramified quadratic ring on the target primes showed a stable one-dimensional pattern

`delta_p in (1+sqrt(2)) F_p`.

A coefficientwise hypergeometric calculation further suggests that, after factoring the forced `u^p p^2` contribution from the polynomial transform defect, a residual polynomial `r_p` satisfies

`D r_p = (2/9)(1+u+...+u^(p-2))`,

for the relevant hypergeometric differential operator `D`. The right side is reflection-odd under `u -> 1-u`; therefore the symmetric part of `r_p` lies in the homogeneous Hasse solution space. Killing its single normalization component would prove the observed Frobenius eigenline. A stronger possible endpoint is the fixed-point lift

`sum_{k=0}^{p-1} (1/3)_k(2/3)_k/(k!)^2 2^k = sum_{k=0}^{p-1} (1/6)_k(1/3)_k/(k!)^2  (mod p^3)`.

**Status:** `EXACT_COMPUTATIONAL_PATTERN_PLUS_WORKING_DIFFERENTIAL_REDUCTION / SYMBOLIC_REVALIDATION_REQUIRED / NOT YET THEOREM`.

The successor must distinguish: (i) proof of the eigenline only; (ii) proof of the stronger fixed-point `p^3` lift; and (iii) exact connection of either statement to the inherited `LIFT` scalar.

## 5. BRC carrier / information discipline

For these successors the adequate carrier is not positive total branch mass. Preserve:

- the term label `k` until a proved quotient is applied;
- `p`-adic valuation data through the `p^2/p^3` boundary;
- value/derivative jet information at the supersingular point;
- the two Frobenius ports `u` and `1-u` and their provenance.

Taking total mass, absolute values, or collapsing the two conjugate ports early erases the cancellation and cannot certify either target.

## 6. Source chain for recovery

Primary frozen execution:

- commit `a722292873eba2449f0959fad7b766a12741ff47`;
- return `research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE_RETURN_20260828.md`;
- artifact `research_artifacts/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE/jacobi_cm_hasse_reduction_20260907.json`;
- checker `scripts/check_enterprise_brc_half_coupling_inert_plus_terminating_jacobi_jet_certificate.py`;
- execution record `research_execution_records/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-TERMINATING-JACOBI-JET-CERTIFICATE/ER-0E7A6ED487BA644FCD10.json`.

Earlier independent source execution:

- branch head `b93574bd6df37eaec211883fa7f09be575e63814` on `research/enterprise-brc-half-inert-plus-terminating-jacobi-jet-certificate-em-ebp6jt-7a4c21`.

External mechanism references used in the reduction include Mao–Pan's truncated quadratic `2F1` congruence and Zhi-Hong Sun's generalized Legendre polynomial congruences/recurrences. Sun A14(ii) remains conjectural and must never be imported as a theorem.

## 7. Recommended split

Publish two parallel continuation tasks rather than one mixed task:

1. **UR-Legendre reciprocity:** verify the ordinary-Legendre equivalence and prove/refute/strictly reduce the first-digit unit reciprocity.
2. **QTF3 / LIFT:** prove/refute the `p^3` quadratic-transform lift or its Frobenius-eigenline residue and connect it exactly to the inherited second digit.

The siblings may exchange proved lemmas, but neither should assume the other's conjectural endpoint.
