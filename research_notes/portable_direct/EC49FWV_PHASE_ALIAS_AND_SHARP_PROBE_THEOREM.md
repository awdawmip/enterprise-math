# EC49FWV — Exact phase alias and optimal robust probe layout for a drifting Farey observer

**2026-11-22 · frozen BRC16943 · continuation of EC49FWU @ 3f78bb4454b2eff41cbf8113dd61a776fb58988b · AUTHOR_PROVED / EXACT_FINITE_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED**

## Precise model and question

Keep the inherited frozen 44-pair P10 predicate and its 50 reduced 10-bit masks U from 72 primitive directions; the modulo-11 factor V is either all residues or all but one residue. The known reference word for an anchor is `w(t)=1_U(t mod 10) 1_V(t mod 11)`, t in Z/110. A single sensor has **unknown cyclic registration phase** s in Z/110 and reports `w_s(t)=w(t-s)`. Its available baseline is the **complete indexed reflection-defect spectrum** `Delta_s(c)=|w_s triangle (c-w_s)|`; supplemental Boolean site probes may be chosen *before* seeing this spectrum (fixed installed layout), or *after* seeing it (adaptive layout). The trace/reference U,V is known when interpreting the observation; an installed universal layout works across all 50 U and all 12 V types.

The decoding target is the observed 110-bit *membership word*, not necessarily the unobservable numeric value of s. Minimum Hamming distance r of the supplemental probe responses within any common-spectrum fiber is required; r=1 gives exact readout, r=2 tolerates one known erasure, r=3 corrects one unknown bit error.

## Theorem A — exact spectral phase alias

For every frozen mask U, its ten-center intersection autocorrelation
`K_U(a)=sum_t U(t)U(a-t)` has **no nonzero translation period** in Z/10. This is a finite assertion: the self-contained verifier evaluates all 72 primitive directions, deduplicates 50 masks, and compares all 9 possible nonzero translations of each K_U.

For the full-factor case V=Z/11, the cyclic shifts have equal indexed defect spectra exactly when
`Delta_s=Delta_s' iff s=s' (mod 5)`. Since the observed word depends only on s modulo 10, this spectrum determines two distinct words (shift representatives differing by 5 modulo 10). Absolute phase in Z/110 is unobservable because the word is 10-periodic.

For the one-hole case V=Z/11 minus {z}, the indexed defect spectrum has no nonzero center-translation period in Z/110. Consequently
`Delta_s=Delta_s' iff s-s'=0 or 55 (mod 110)`.
The two words are distinct, because the ten-mask U has no period 5.

**Proof.** A shift of the word by s moves the center of its reflection defect by 2s:
`Delta_s(c)=Delta_0(c-2s)`. Chinese-remainder factorization gives
`Delta_0(c)=2(|U||V|-K_U(c mod10)K_V(c mod11))`.
For full V, `K_V=11`, so the exact period of Delta_0 as a 110-indexed sequence is 10. For one-hole V, `K_V(b)=9+[b=2z mod11]`. Summing the defect values over the ten modulo-10 centers, with b fixed, yields `2(10|U||V|-|U|^2 K_V(b))`: this has a unique distinguished modulo-11 row b=2z. Therefore a translating period must be divisible by 11. Since every K_V(b)>0, K_U's trivial stabilizer forces the period also to be divisible by 10, hence by 110. The kernel of multiplication by 2 in Z/110 is {0,55}, and in Z/10 the word aliases modulo 5.

## Theorem B — exact fixed versus adaptive robustness cost

Let `D(U)={i:U(i) != U(i-5)}` in Z/10. It is nonempty, is a union of opposite row pairs `P_i={i,i+5}` for i=0,...,4, and its size d_U has the following complete finite census:

| d_U | Number of frozen masks |
|---|---:|
| 2 | 10 |
| 4 | 26 |
| 6 | 10 |
| 8 | 4 |

For either common-spectrum pair, the exact 110-site disagreement support is a shifted `D(U) x V` under CRT, with total disagreement `d_U |V|`. The minimum is 20 for one-hole V and 22 for full V.

**Adaptive layout, worst case:** For each `1<=r<=20`, exactly r site readings are necessary and sufficient after the indexed spectrum is known:
`N_adaptive(r)=r`.
Beyond 20, a one-hole frozen mask with d_U=2 defeats even complete observation at requested Hamming distance, so the stated uniform robust requirement is unattainable.

**Universal fixed installation, worst case:** With a single layout chosen before the actual U, V and sensor phase are observed, for `1<=r<=20` the exact minimum is

```
N_fixed(r) = 5(r+1),       1 <= r <= 10;
           = 5(r+2),      11 <= r <= 20.
```

Thus exact recovery takes 10 fixed versus 1 adaptive site; one known erasure takes 15 versus 2; one unknown erroneous bit takes 20 versus 3.

**Proof of sharpness.** Choose a frozen d_U=2 mask (ten such masks exist; the actual-anchor realization is inherited from EC49FWT). Its disagreement rows are one opposite pair. The unknown shift s modulo 10 can move this pair to any P_i. The unknown shift modulo 11 can independently move the excluded column to any j because 10 and 11 are coprime. Let m_i be the number of installed sites on P_i and c_ij the count in column j (0,1,2). The worst-case distance for this authentic phase-alias pair is `m_i-max_j c_ij`. Every one of the five disjoint row pairs must achieve at least r.

When r<=10, the minimal per-pair installation has r+1 readings in distinct columns (one may be erased), and no smaller count can work. When 11<=r<=20, at most eleven columns can hold a single reading; every feasible per-pair installation then has some column with two readings, so m_i>=r+2, attained by filling all eleven columns in one row and r-9 extra sites in the opposite row. A full layout with exactly this pattern for each i works for *every* U: any nonzero D(U) contains at least one complete opposite pair. This proves both bounds. For r>20 the gap-2 one-hole state has only 20 differing sites in its complete 110-bit word.

**Separate physical resource metric:** A physical paired left/right activation may deliver two Boolean reads, unlike the site-count above. For a known anchor with a shared mirrored drift, `R(t)=L(-k-t)` implies `R_{-s}(t)=L_s(-k-t)`; the right complete indexed spectrum is a relabeling of the left and does not eliminate the phase alias. Whether a paired activation can halve the activation cost depends on the intersection of the paired disagreement sites and is **not** asserted here. Unknown anchor, independent left/right drift and native X6 state restoration are different observer models.

## Verification and continuation

Run `node EC49FWV_PHASE_ALIAS_VERIFY.js` with ordinary Node.js. The exact program checks 72 primitive classes, 50 frozen masks, all 600 full/single-hole reference states, 66,000 direct 110-center reflection identities, 66,000 spectral-shift comparisons and 33,000 direct layout checks for selected r. It also checks every r from 1 to 20 by exact opposite-pair/column enumeration. Full output is preserved in the adjacent JSON file. The finite census plus the displayed group/CRT argument establishes the universal phase and optimality theorems in the declared finite frozen family. Mathematical acceptance and independent review remain open.

**Next useful question:** With paired hardware activated once but reading both left/right bits, classify when two mirrored alias-disagreement sites can be covered in one activation, and derive the exact worst-case activation cost (separate from 110-site cost). Test the related independent left/right drift model. Preserve known anchor, signed branch, normalization, height origin and all native-X6 provenance when later composing this auxiliary certificate with an actual future observer.

**Control/provenance:** Independent portable research only. No task CLAIM, Result, Review, P000 change or native source publication event is implied by this file. The live Enterprise Math gateway status was inaccessible at the time of this research (`BACKEND_IDENTITY_CHECK_UNAVAILABLE`, `operation_sent=false`); Activity registration/owner projection is pending. GitHub science persistence is independent of the native connection.
