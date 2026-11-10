# D25/W216: two exact target-class scale-boundary countercertificates

**Date:** 2026-11-10; **classification:** AUTHOR_SIDE / EXACT_FINITE_COUNTEREXAMPLES / VERIFIED_COMPUTATION / UNREVIEWED / NOT_ADMITTED / NATIVE_H0_B0_NOT_RUN. Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Logical lane: `chatgpt-research-onhour-enterprise-math-20260923` (not maintenance).

## 1. Exact question and distinction

Consume the existing W216 prime-power first-carry conjecture, **not** a new native experiment. For p>3, put
[
A_k=\binom{2k}{k}^2\binom{3k}{k}/216^k,\qquad
W_n=\sum_{k=0}^{n-1}(6k+1)A_k,\qquad
\chi_p=\begin{cases}1&p\equiv1\pmod3,\\-1&p\equiv2\pmod3.\end{cases}
]
Set `W_{p^0}=1`. For r>=1 define `D_{p,r}=W_{p^r}-chi_p*p*W_{p^{r-1}}`; when `p^(3r)|D`, let `E_{p,r}=D/p^(3r) mod p^2`.

Earlier author's finite work observed `E_{p,r}=E_{p,1} mod p`, including target p=13,19 mod24. A mathematically distinct and falsifiable strengthening is:

> **FALSIFIED:** `E_{p,r}=E_{p,1} mod p^2` for every r>=2 on both target classes.

We obtained exact countercertificates at p=13 and p=19 for r=2, and then inspected r=3,4. The r>=2 values appear stable at this extra digit; that new stabilization remains a candidate, not a theorem.

## 2. Exact data, signed and p-adic provenance

All entries are `E_{p,r}` reduced modulo `p^2`; the prerequisite `v_p(D_{p,r})>=3r` was checked explicitly for every entry.

| p | p mod24 | E_1 | E_2 | E_3 | E_4 | (E_2-E_1)/p mod p |
|---:|---:|---:|---:|---:|---:|---:|
| 13 | 13 | 126 | 61 | 61 | 61 | 8 |
| 19 | 19 | 88 | 297 | 297 | 297 | 11 |
| 37 | 13 | 537 | 870 | 870 | — | 9 |
| 43 | 19 | 1266 | 1438 | 1438 | — | 4 |
| 61 | 13 | 373 | 2447 | 2447 | — | 34 |
| 67 | 19 | 3941 | 591 | 591 | — | 17 |

For p=13, `E_1=126`, `E_2=61` modulo169 and `61-126=-5*13` (so second-digit defect is 8 mod13). For p=19, `E_1=88`, `E_2=297` modulo361 and `297-88=11*19`. Both satisfy equality modulo p, exactly the previously observed first carry, while disproving equality modulo p^2.

The two largest new runs were n=13^4=28,561 and 19^4=130,321 terms, respectively, at precision p^14. Their exact residues:
- `p=13,r=4`: `W_{13^4}=2136929591474145 (mod 3937376385699289)`; `D_{13,4}/13^12=61 (mod169)`.
- `p=19,r=4`: `W_{19^4}=524840080672658674 (mod 799006685782884121)`; `D_{19,4}/19^12=297 (mod361)`.

The tested target-class precision-stabilization candidate is
[
E_{p,r}\stackrel{?}{\equiv}E_{p,2}\pmod{p^2},\qquad r\ge2.
]
It holds in all **six** listed primes through r=3, and in p=13 and p=19 through r=4. It has not been proved for any infinite family. The counterexamples to the first-scale stronger statement, however, are final for the stated universal candidate.

## 3. Independent exact reproduction paths

Code `d25_w216_primepower_second_carry_scale_boundary_20261110.py` implements two independently constructed `W_n` computations:

1. **Factorial p-unit method:** strip all p factors in factorials up to `3(n-1)`, retain factorial p-valuations, calculate the exact rational `A_k=(2k)!(3k)!/((k!)^5 216^k)` via invertible unit factorials modulo `p^(3r+2)`.
2. **Forward recurrence:** start with `A_0=1`, update valuation/unit separately using `A_{k+1}/A_k=(2k+1)(3k+1)(3k+2)/(36(k+1)^3)`, then accumulate signed weights `(6k+1)`.

The two methods agreed at each of the 20 declared `(p,r)` cases (6 primes at r=1,2,3 plus two r=4 cases), including both independent fourth-scale target-class values. All computations used exact integers and inverses of units, no floating point. Exact independent reproduction is author-side; independent project Driver review has not occurred.

## 4. BRC / original target / next action

**BRC = COMPOSE_APPLIED.** Carrier is the labeled tuple `(p,r,k,v_p(A_k),unit_p(A_k),(6k+1),D_{p,r}/p^(3r) mod p^2)`; the interscale operation `r->r+1` matters. The loss under projection `mod p^2 -> mod p` is explicitly witnessed by p=13 and p=19: identical first-carry output but different second-carry output. This uses the actual W216 signed coefficient recurrence, not a positive-mass proxy.

The main frozen target remains `Delta_p-R_p=0 mod p` in both p=13,19 mod24 classes, from the original same-class accepted scalar interface. The new power-scale study is supplementary; it does not displace the **native fixed H0/B0 divided-power benchmark** with `[X]U mod 139129`, native module rank, semilinear Frobenius direction/normalization eta, odd signed kappa, and independent replication. Existing support Issue #1559 is OPEN / no confirmed executor on the current read. No native run/CLAIM/Result was produced in this author-side unit.

**Next exact action:** For a lawful native executor, obtain and run the specific H0/B0 p=373 representative against its original source pin, record all acceptance observables and independent reproduction. On the independent mathematical route, derive or falsify a block-transfer identity explaining `E_{p,2}=E_{p,3} mod p^2` from original signed p-adic coefficient jets, not merely more unbounded scans. Keep all previously completed LIFT certificates unchanged.

**State:** prior own Source request `onhour11-20261110-1658-exact-cont-after-unit` and new exact continuation `onhour11-20261110-1936-exact-source` both observed SUCCEEDED (read-only); Source snapshot as of 2026-11-10T11:35:07Z `ee1d5709918327b02ba1920a9d62ae10d16179d6`. Historical Researcher session `MCP-5378d3819d8947bda9049c9428493e2d` has no recoverable private capability in this client. `recovery_status` returned `SITE_CONTROL_OWN_ISSUED_SESSION_REQUIRED`. No winning own CLAIM/open run or Source checkpoint is asserted. Historical source frontier `b58330b74576153cdadde5d80a3d92df3a819a0e`, frozen science unchanged. Research/maintenance conversations are distinct.
