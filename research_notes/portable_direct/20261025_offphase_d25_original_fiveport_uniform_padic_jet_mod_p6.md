# D25/LIFT — a uniform source-labeled p-adic jet generator and sixth-digit certificate

2026-10-25 · TASK_RESEARCH portable author-side mathematics. **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT / NO_NEW_NATIVE_CLAIM / NO_SOURCE_CHECKPOINT / NOT_INDEPENDENT_REVIEW.** Mother objective `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`; current scientific task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Do not mistake this auxiliary source-ported scalar observer for native CM/DP data or a new authorized research claim.

## Exact previously established inputs

For every prime `p=6m+1>=13`, let `n=2m=(p-1)/3`, `H_N^(s)=sum_{j=1}^N j^(-s)`, and `q_p(a)=(a^(p-1)-1)/p`. The **original** WZ source has five labeled ports:

`S_(m+1)-S_m = E_0+E_1+E_2+E_3+E_4`, `E_j=W_(m+1,4m+j)` for `1<=j<=4`, where

`V_(r,t) = (6r)!(4r+2t)!(3t)! / [3^(6r)216^t (2r)!(t!)^2 ((2r+t)!)^2 (4r+t)!]`, `W_(r,t)=(6t+12r+1)V_(r,t)`.

The inherited exact old-edge factorization is `E_0/p = U_m C(p)`, with

`U_m = (2m)/(108^(p-1)) * prod_(k=2)^n(1-p/k)^2 * prod_(j=1)^(p-2)(1+p/j)^2 / prod_(j=1)^(n-1)(1+p/j)`;

`C(p) = [(p+1)(2p-1)^2(30p^2+77p+40)]/[2(p+2)(2p+1)(4p-1)(4p+5)]`.

For the four distinct added ports, let `sigma_p = V_(m+1,4m+1)/p^2`. Their **exact** transfer factor is

`B(p) = sum_(j=1)^4 (6p+6j+7) prod_(k=1)^(j-1) R_k(p)`, where

`R_k(p)=[(2p+2k+3)(2p+3k-1)(2p+3k)]/[4(2p+3k+1)(p+k+2)(4p+3k+11)]`, `k=1,2,3`.

Therefore the inherited identity, **before truncation**, is `(S_(m+1)-S_m)/p = U_m C(p) + p sigma_p B(p)`. The previously published exact factorial product for `sigma_p/(3/220)` is consumed rather than claimed anew; see the pinned fifth-digit source `research_notes/portable_direct/20261025_offphase_d25_original_genuine_five_port_fifth_digit_mod_p5.md`.

## New all-precision constructive lemma (rather than one new formula per digit)

For a prime `p=6m+1>=13` and any integer `1<=N<=p-2`, define, for `1<=s<=N`,

```
alpha_s = [(-1)^s q_p(108)^s - 2(H_n^(s)-1)
           + (-1)^(s+1)(2H_(p-2)^(s)-H_(n-1)^(s))]/s.

beta_s = (-1)^(s+1)/s * [
       - sum_(c in {-1,2,5,8,11}) e_c/c^s - 2q_p(2)^s - 3q_p(3)^s
       + 2(-1)^s H_(n-1)^(s) + 2H_(p-1)^(s)
       + H_5^(s) + 2^s H_4^(s) + 2^s - 2H_2^(s) - H_(n+4)^(s)
],  (e_-1,e_2,e_5,e_8,e_11)=(2,2,2,1,1).
```

For any finite coefficient sequence `ell_s`, let `J_0(ell)=1` and define the exact rational exponential-jet recurrence

`J_j(ell) = (1/j) sum_(s=1)^j s ell_s J_(j-s)(ell)`.

**Theorem (uniform labeled-source quotient jet).** In `Z_(p)`, for `1<=N<=p-2`,

```
(S_(m+1)-S_m)/p =
  2m C(p) sum_(j=0)^N J_j(alpha) p^j
  + (3p/220) B(p) sum_(j=0)^(N-1) J_j(beta) p^j   (mod p^(N+1)).
```

This is a *constructive generator* of every permitted finite jet of the original scalar five-port quotient at a **fixed** prime, not a same-prime source-to-CM/DP comparison and not a uniform polynomial with coefficients independent of `p`.

**Proof.** Substitute `108^(p-1)=1+p q_p(108)` into the exact inherited `U_m` product. Expand each formal logarithm of its factors `1 +/- p/k`; the coefficient of `p^s` is precisely `alpha_s`. For the original source-normalized `sigma_p/(3/220)`, use the existing exact Wilson-reflected factorial product, which has the factors `(1+p/c)^(-e_c)`, `(1+p q_p(2))^-2`, `(1+p q_p(3))^-3`, `prod_(j=1)^(n-1)(1-p/j)^2`, `prod_(j=1)^(p-1)(1+p/j)^2`, and the finite endpoint ratio `prod_(j=1)^5(1+p/j) prod_(j=1)^4(1+2p/j)(1+2p)/[prod_(j=1)^2(1+p/j)^2 prod_(j=1)^(n+4)(1+p/j)]`. Expanding its logarithm yields `beta_s` **including** the full-block harmonics `H_(p-1)^(s)`. Differentiation of the formal exponential gives the recurrence for `J_j`. All inputs `k`, `c` and the rational transfer denominators are p-units for the stated primes; `j<=N<=p-2` makes the recurrence divisions by `j` legal. Omitted log/exp terms contribute at least `p^(N+1)`; the first possible non-unit denominator occurs at degree `p` and has valuation `p-1>=N+1`. Substitute the exact five-port decomposition, with `p sigma_p` requiring only `N-1` jet digits. This proves the congruence without altering the labeled original ports. □

## New explicitly evaluated sixth digit (`N=5`)

The previously known tail transfer has `B(p)=A_0+A_1 p+A_2 p^2+A_3 p^3+O(p^4)` with prior coefficients. New exact Taylor division of the source rational `B(p)` gives

`A_4 = 240151883718153049 / 11643159880396800000`.

The previously known first three tail-unit log coefficients are extended by the fourth:

```
beta_4 = -91342467516959/12143831040000
         + q_p(2)^4/2 + 3q_p(3)^4/4
         - H_(n-1)^(4)/2 - H_(p-1)^(4)/2
         + H_(n+4)^(4)/4.
```

Together with `alpha_5` and the recurrence above, this constructs the **complete original five-port quotient modulo `p^6` for all target primes**, including the often lost full-block harmonic corrections. The rational source-B expansion is used only as an optional coefficient display; the verifier evaluates exact `B(p)` directly.

## Executed exact falsification, and contribution boundary

The standard-library checker `20261025_offphase_d25_original_fiveport_uniform_padic_jet_mod_p6_check.py` was actually executed. **79/79 PASS** for all target primes `<1000`: source-product `U_m` modulo `p^6`, original factorial `sigma_p` modulo `p^5`, rational `B(p)` against the new `A_4` Taylor coefficient modulo `p^5`, and the four independently labeled factorial ports against the generated complete quotient modulo `p^6`. A separate **14/14 PASS** checks the raw, uncollapsed sums `S_(m+1)-S_m` reconstructed term by term from original factorials at `p=13,19,31,37,43,61,67,73,79,97,103,109,127,211`. Example: `(S_(m+1)-S_m)/p = 4640381 (mod 13^6)` at `p=13`. All operations are exact integer, fraction and p-unit modular inverse arithmetic; no native source CM experiment or formal checker is claimed.

**New contribution:** an all-finite-precision `alpha/beta` generator and an explicitly checked sixth-digit tail transfer `A_4`/`beta_4`. **Inherited, not recredited:** the WZ telescoping identity, genuine original port labels, the exact old-edge rational factorization, the original factorial tail product, and all previous p^3/p^4/p^5 formulas. BRC/Enterprise-coordinate applicability is audited at the labeled observer level: the exact finite rational products preserve integer valuation and the four port provenance labels, but they provide no separately justified positive-mass BRC carrier or no-loss native CM/DP projection, so no forced BRC equivalence or native-six-dimensional transfer is claimed.

**Unfinished mother problem:** obtain the authentic same-class CM/Katz/crystalline/divided-power representative, its `H0/B0`/`[X]U mod p^2` normalization and the explicit transfer to native `omega+6*nabla_lambda omega` and `kappa/Delta_p-R_p`; distinguish genuine native data from any scalar WZ jet. Existing cross-stream canonical source checkpoint at `main@09f08b5` identifies a different current native Researcher and an open matching obstruction; this portable author note does not adopt that claim or count its units as its own. UR V2 four-file source bundle is still required in its exact 94687-byte form with SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`; this work does not rebuild that previously completed UR proof or assert the bundle has been recovered. Formal writer/provenance and independent review remain pending under the current Source contract.
