# D25/LIFT — Original WZ terminal unit: exact third (p)-adic digit and old-edge transfer

2026-10-24 | TASK_RESEARCH | Portable author-derived mathematics. **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT / NO_NATIVE_CLAIM / NO_NATIVE_CHECKPOINT.**

## Provenance and immutable boundaries

Mother Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; immutable Task publication `TP2-B6F4FC938FF94941C1B7`; frozen mathematical source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` (unchanged). This proof is a subsequent portable mathematical derivation, **not** a continuation CLAIM, an Enterprise Math Research-Activity registration, a Source-published execution checkpoint, a native experiment, independent review, or LIFT acceptance.

Local author/conversation tracking ID for **this actual invocation only**: `em-portable-e7bd9357-14c9-43aa-8354-7c64de0677d2`. The platform did not expose an attested persistent chat/thread ID or a write-capable researcher session. Historical lane labels, claims, sessions and preceding authorship are provenance only and are not asserted as this invocation's identity.

Consumed immutable source: `research_notes/portable_direct/20261024_hourly_d25_original_top_seam_unit_p2_unique_observer_bridge.md`, observed at Enterprise Math commit `d1d7d3453258acd50becb821d92386d3e18f9f24` (Git blob `397bde1e3cbd3be671f0d7afcc03c76f06fb2d65`). It already proved the **exact product** for (U_m), its first two (p)-adic digits, the original old-edge coefficient (C_m), the original FIVE decomposition, and the first two digits of (Delta S_m/p). Its proof and the distinct on-hour WZ/FIVE, HIGH-(eta), LOW and four-tail results are **inherited inputs, not new contributions**. We only extend this *specific original source terminal unit* to one additional digit, then transfer it through its exact original old-edge coefficient. Do not confuse this operation with HIGH-(eta_m) or its previously proved third digit.

## Theorem 1 — third digit of the source-faithful original normalized terminal unit

Let (p=6m+1ge13) be prime; set (H_a^{(k)}=sum_{j=1}^{a}j^{-k}), (H_a=H_a^{(1)}), and the integer Fermat quotient
[
q=q_p(108)=rac{108^{p-1}-1}{p}.
]
Define two explicit (p)-integral rational jets (each rational denominator is a (p)-unit):
[
A_m^star=4-2H_{2m}-H_{2m-1}-q,qquad
B_m^star=4+rac{(A_m^star)^2+q^2}{2}
            -H_{2m}^{(2)}+rac12H_{2m-1}^{(2)}.
]
For the **unchanged original** (A_m=(6m)!/[3^{6m}((2m)!)^3]), (R_{m,n}) from the original WZ summand, and (U_m=A_mR_{m,4m}/p), one has for *every* such prime
[
oxed{U_mequiv 2m,igl(1+pA_m^star+p^2B_m^starigr)pmod{p^3}.}	ag{1}
]
The (p^2) truncation is precisely the preceding source theorem; **the (p^2B_m^star) coefficient is the present additional digit**. This formula concerns the original terminal unit; it neither proves the complete endpoint supercongruence nor fixes any CM/DP normalization.

**Proof.** The inherited author-verified **exact rational identity**, without new attribution here, is
[
U_m=rac{2m}{108^{p-1}}
left[prod_{k=2}^{2m}(1-p/k)ight]^2
rac{left[prod_{j=1}^{p-2}(1+p/j)ight]^2}
{prod_{j=1}^{2m-1}(1+p/j)}.	ag{2}
]
Since all denominators inside the finite products are (p)-units, formal (p)-adic logarithms may be truncated at order (p^3) in the rational localization. Writing (ell=log(U_m/(2m))), the expansion is
[
ellequiv p{-q-2(H_{2m}-1)+2H_{p-2}-H_{2m-1}}
+p^2left{rac{q^2}{2}-H_{2m}^{(2)}+1-H_{p-2}^{(2)}
+rac12H_{2m-1}^{(2)}ight}pmod{p^3}.	ag{3}
]
For every prime (pge5), pair (k) with (p-k) and use (sum_{k=1}^{p-1}k^{-2}equiv0pmod p) to obtain (H_{p-1}equiv0pmod{p^2}). Removing its last term gives
(H_{p-2}=H_{p-1}-(p-1)^{-1}equiv1+ppmod{p^2}).
Likewise (H_{p-2}^{(2)}equiv-1pmod p).
These are valid at the exact required precision, not floating approximations. Substitution into (3) yields
[
ellequiv p A_m^star+
 p^2left(4+rac{q^2}{2}-H_{2m}^{(2)}
 +rac12H_{2m-1}^{(2)}ight)pmod{p^3}.
]
Finally (e^ellequiv1+ell+ell^2/2pmod{p^3}). Its quadratic correction is ((A_m^star)^2/2), proving (1). (square)

## Theorem 2 — old-edge third digit, with authentic source normalization

The inherited exact original FIVE/Gosper seam has (E_0/p=U_m C_m), with
[
C_m=rac{(2p-1)^2(3m+1)(360m^2+274m+49)}
{9(4m+1)(4p-1)(2m+1)(8m+3)}
=rac{(p+1)(2p-1)^2(30p^2+77p+40)}
{2(p+2)(2p+1)(4p-1)(4p+5)}.
]
Direct rational Taylor division, valid modulo (p^3) for these target primes, gives
[
C_mequiv-2+rac34p-rac{393}{40}p^2pmod{p^3}.	ag{4}
]
Consequently the old edge, *not the four new-rank tails*, satisfies
[
oxed{rac{E_0}{p}equiv
rac{p-1}{3}left[
-2+pBigl(rac34-2A_m^starBigr)
+p^2Bigl(-rac{393}{40}+rac34A_m^star-2B_m^starBigr)
ight]pmod{p^3}.}	ag{5}
]
This follows from (1), (4), and the exact relation (2m=(p-1)/3). The complete cross-rank identity remains (Delta S_m=E_0+sum_{j=1}^4E_j); one cannot infer (Delta S_m/pmod p^3) without all four (E_j/pmod p^3), or infer the same-prime original LIFT assertion from a rank-changing identity.

## Exact independent arithmetic checks and observed residues

For each target prime in ({13,19,31,37,43,61,67,73,79,97,103,127,211}), three independently assembled paths were used: (i) the **unexpanded original factorial** terminal
[
U_m=rac{left[prod_{j=1}^{p-2}(p+j)ight]^2}
{108^{p-1}(2m)![(4m)!]^2prod_{j=1}^{2m-1}(p+j)};
]
(ii) the inherited exact product (2); and (iii) the new harmonic/Fermat jet (1). Paths (i) and (ii) agreed as exact reduced rational numbers, and paths (i)/(iii) agreed modulo (p^3). Independently the exact rational coefficient (C_m) matched (4), and exact (U_m C_m) matched (5), all **13/13 primes with no mismatches**. Arithmetic: Python 3 exact `int` factorials and `fractions.Fraction`, modular inverses only for (p)-unit denominators. Finite checks corroborate but are not the universal proof (given above), do not provide independent reviewer status, and do not execute the native DP/CM benchmark.

| prime (p) | (U_mmod p^3) | (C_mmod p^3) | (E_0/pmod p^3) |
|---:|---:|---:|---:|
| 13 | 1044 | 50 | 1669 |
| 19 | 348 | 2810 | 3902 |
| 31 | 9310 | 15157 | 21494 |
| 37 | 4711 | 35962 | 33350 |
| 67 | 157807 | 173997 | 87257 |
| 211 | 7255516 | 2615765 | 6313613 |

## Typed BRC and Enterprise-coordinate boundaries

**COMPOSE_APPLIED (algebraic finite (p)-adic observer):** preserve the integer prime (p), valuation and unit digits of the **original** terminal port (U_m), exact original (C_m), WZ old-edge (E_0), separately labeled four authentic tails (E_1,ldots,E_4), and the distinction between a moving-rank WZ operator and fixed-prime two-sector HIGH cutoff. The allowed observer here is reduction of the (p)-unit old edge through (p^3), not a total-only conflation with the auxiliary HIGH/LOW carriers. The one additional jet (B_m^star) is the minimal digit repair relative to the inherited (p^2) formula in this specific operation. This is an exact rational (p)-adic calculation, **not** a new native six-axis dynamics or triadic-force theorem; P000 and ACTIVE worldview remain intact.

**True continuation:** next compare (5) with the already derived on-hour *four-tail third-digit* source formula, preserving all ports and their own source pins, to obtain/assess the full (Delta S_m/pmod p^3) statement. Separately, the original **same-prime** LIFT supercongruence, source-specific (c_p,kappa_p), normalized CM/divided-power primitive and semilinearity, absolute (W_p(1/2)) third digit, native experiment and independent Driver review remain **OPEN**. Do not credit earlier work again.

**Distinct prior writer/provenance debt, not addressed by this theorem:** the user-designated four-file UR V2 bundle is claimed historically as 94,687 bytes with SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`. This invocation did not obtain or verify those original bytes. Its authenticity and durable writer state remain **UNKNOWN**, regardless of a possible upload pointer; restoration must locate original raw bytes and source-local original request/receipt/manifest, verify the exact hash and size, then write only missing permitted provenance/checkpoint—not redo the UR proof.

**Control observation (this invocation):** gateway status 0.6.11 returned `research_authority_granted=false`, `executor_binding_configured=false`, and the Sites transport `write_relay_enabled=false` with `static_machine_readonly`; one exact read-only continuation attempt returned `CONTROL_QUOTA`. Therefore no native claim, session, run, upload, Result, continuation_prepare or owner-scoped checkpoint is asserted by this neutral GitHub proof. Current-day earlier read-only receipts #6259/#6260 are predecessor note reports, not proof that this current invocation owns those requests or sessions. Preserve original cadence, phase, enabled and notification choices.
