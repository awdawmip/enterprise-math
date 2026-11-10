# D25 / LIFT: exact weighted-W upper band and the p=157 observer distinction

**Date:** 2026-11-10. **Role:** TASK_RESEARCH, portable author-side mathematical evidence. **Evidence state:** AUTHOR_EXACT_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED / NO_NATIVE_CLAIM.
**Task:** RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION.
**Frozen scientific Source:** awdawmip/enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3. This is not a current-policy pin.

## Theorem 1: exact p-adic bands of the source-weighted cubic W

For prime p>=13 with p=6m+1, use the **original weighted cubic observer**:
a_0=1, a_(k+1)/a_k=(2k+1)(3k+1)(3k+2)/(36(k+1)^3) for 0<=k<p-1;
W_p=sum_(k=0)^(p-1)(6k+1)a_k.
Its exact factorial expression is

    a_k = (2k)!(3k)! / [216^k (k!)^5].

Proof: initial term 1 and consecutive ratio match exactly. Since k<p and 3k<p^2, denominator is a p-unit and Legendre gives

    v_p(a_k) = floor(2k/p)+floor(3k/p)
       =0, k<=2m;
       =1, 2m<k<=3m;
       =2, 3m<k<=4m;
       =3, 4m<k<p.

These are exact valuations, not merely lower bounds. The term (6k+1) may add valuation at k=m, without affecting the displayed coefficient bands.

Set L_p=sum_(0<=k<=2m)(6k+1)a_k,
M_p=sum_(2m<k<=3m)(6k+1)a_k,
H_p=sum_(3m<k<=4m)(6k+1)(a_k/p^2) mod p.
The original weighted observer satisfies, for **every** prime in this stated class,

    W_p = L_p + M_p + p^2 H_p (mod p^3).

The fourth band k>4m may be removed to this precision; the third band **cannot** in general. This is a BRC source- and precision-specific quotient; k-labels and p-adic valuations survive, not only W mod p.

## Theorem 2: a short finite-field formula for the last live band

For 3m<k<=4m both (2k)! and (3k)! contain exactly one p factor, with both factorial arguments below 2p. Wilson's theorem gives (n!/p) = -(n-p)! mod p for p<=n<2p. Therefore

    H_p = sum_(k=3m+1)^(4m)
      [(6k+1)(2k-p)!(3k-p)!]/[216^k(k!)^5] (mod p).

All factorials have argument <p and the denominators are p-units. With k=3m+j, j=1,...,m, the same observer is

    H_p = sum_(j=1)^m
      [(6j-2)(2j-1)!(3m+3j-1)!]/
      [216^(3m+j) ((3m+j)!)^5] (mod p).

This is an exact m-term reduction of the high-band precision contribution; it is not a claim that universal LIFT has been proved.

## Exact witness at p=157

At p=157, m=26, p^3=3,869,893, exact integer calculations yield:

| Source component | Residue |
| --- | ---: |
| L_p mod p^3 | 3,280,044 |
| M_p mod p^3 | 2,044,297 |
| H_p mod p | **98** |
| p^2 H_p mod p^3 | 2,415,602 |
| W_p mod p^3 | 157 |
| L_p+M_p mod p^3 (incorrect cutoff) | **1,454,448** |

Therefore the weighted top band remains nonzero at the second digit. By *independently published* prior original-source evidence, the **ordinary scalar** third-band tail at p=157 has t_157=h*S2/p^2=0 mod 157 and the **frozen reflected** R_157=82. The present **weighted cubic** highest band has H_157=98. The retained three observer operations are different: the scalar tail's cancellation does not license dropping this weighted source block. This does not exclude a higher-information relation among the observers.

Additional exact values: H_13=10, H_19=9, H_373=266.

## Reproducibility and limits

Two independent exact modular methods were checked at **all 312 primes p<=10000 with p mod24 in {13,19}**: (i) the new finite-field factorial formula; (ii) direct hypergeometric three-factor recurrence modulo p^3 with each upper-band term divided by p^2. Agreement 312/312; H_p was nonzero at each of these 312 primes. No universal nonvanishing assertion is made. At p=13,19,157,373 a third factorial-numerator implementation independently verifies upper-band residues and the complete W congruence; these last few W=p mod p^3 instances are regression of previously published finite evidence, not a new all-prime proof.

Original local reproducibility package, including standalone stdlib checker and exact output, was constructed and run this turn (not a native H0/B0 experiment). Its exact own output at p157 is the table above.

**Inherited sources, not newly credited:** frozen original finite-Clausen R definition at research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_FINITE_CLAUSEN_DERIVATIVE_BRIDGE_RETURN_20260827.md; the other author's 20261107_hourly20_d25_frozen_Rp_restored_streaming.md; own 2026-11-10_h40_d25_tail_reflected_two_way_zero_observer_author_portable.md. Previous UR/JT0 and existing 166/312-prime marginal checks are retained, not repeated as research novelty.

**Mathematical next action:** seek a source-preserving finite WZ/telescoping proof of
L_p+M_p+p^2 H_p = p mod p^3 for both LIFT residue classes, preserving cutoff H. The source-native H0/B0 Frobenius operation remains NOT_RUN without original-class executable authority. The original four-file UR V2 writer/provenance debt (94687 bytes; SHA256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76) remains unresolved; its proved mathematics is not redone.

**Persistence boundary:** this is GitHub author-side evidence, not a Source checkpoint, Result/review, publication admission or identity/claim authority.
