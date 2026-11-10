# D25/LIFT: exact scalar second digits and normalization ambiguity

Date: 2026-11-10. Status: **AUTHOR_PROVED / EXACT_INTEGER_COMPUTED / UNREVIEWED / NOT_ADMITTED**. This is author-portable evidence, not a native task checkpoint, an original H0/B0 experiment or an independent review.

Mother objective: `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`.
Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`.
Scientific Source pin remains `c47e13e4aba0e006366f989d6334d443f6333ae3`.

## Scalar input and exact observation

Reuse, without reproving, the frozen parent reduction in `research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE_RETURN_20260828.md` and the accepted UR/JT0 first-digit result.

For prime `p >= 13` with `p mod 24 in {13,19}`, set

`B_0=1,quad B_{k+1}=B_k (6k+1)(3k+1)/(36(k+1)^2)`,
`g=sum_{k=0}^{p-1} B_k`, `h=sum_{k=0}^{p-1}(12k+1)B_k`, and `G=g/p`.
The frozen first digit gives `p|g` and `G*h = 1 (mod p)`. Keep `g mod p^3`, `G mod p^2`, and `h mod p^2` before forming the live residual `Delta=(Gh-1)/p mod p`.

**Carry lemma.** Let `G=a+pb`, `h=c+pd` modulo `p^2`, with four canonical digits in `[0,p-1]`. Since `ac=1 (mod p)`, `q=(ac-1)/p` is integral, and

`Delta = q + bc + ad (mod p)`.

This exhibits the exact contributions of the first-digit carry and both second digits. Computing `g` only modulo `p^2` or `h` only modulo `p` loses an essential input to this observer.

Two author-run, exact-integer implementations agree: the modular recurrence and an independent numerator/denominator product evaluation of each rational `B_k`, where `B_k = product_{j<k}[(6j+1)(3j+1)] / [36^k (k!)^2]`. All denominators remain p-units for `0<=k<p`.

| p | g mod p³ | G mod p² | h mod p² | Gh mod p² | Delta mod p |
|--:|--:|--:|--:|--:|--:|
| 13 | 988 | 76 | 149 | 1 | 0 |
| 19 | 1596 | 84 | 50 | 229 | 12 |
| 37 | 25493 | 689 | 547 | 408 | 11 |
| 43 | 47558 | 1106 | 1659 | 646 | 15 |
| 61 | 146583 | 2403 | 333 | 184 | 3 |
| 67 | 62444 | 932 | 1485 | 1408 | 21 |
| 211 | 7297646 | 34586 | 32576 | 25110 | 119 |
| 373 | 24495656 | 65672 | 62835 | 73109 | **196** |

In particular, at p=373, `G=24+373*176` and `h=171+373*168`, with `(24*171-1)/373=11`, so `Delta=11+176*171+24*168=196 (mod 373)`.
These eight values are an exact, bounded scalar witness, not a uniform proof of LIFT or an evaluation of the frozen target `R_p`.

## Algebraic unit-normalization lemma

For every such p and integer `r>=1`, let `R_r=(Z/p^rZ)[T]/(T^2-2)` with `sigma(T)=-T` and `N(x)=x sigma(x)`. Since `(2/p)=-1`, `R_1=F_{p^2}`. The norm map `N:R_r^* -> (Z/p^rZ)^*` is **surjective at every r**. At r=1 this follows from the cyclic finite-field multiplicative group. Given a lift correct modulo `p^k`, multiply by scalar `1+p^k t`: its norm changes by factor `1+2p^k t (mod p^{k+1})`. Choose t to correct the next digit. Induction proves the assertion.

Thus an *unspecified* coefficient normalization `eta` can make `N(eta)N(alpha)` equal **any** unit scalar target, without establishing a native Frobenius identification. At p=373, the previously recorded **ordinary Hesse candidate** `N(alpha)=122102 (mod 139129)` and the independently computed frozen scalar `Gh=73109 (mod 139129)` differ. The exact ratio is `57610 (mod 139129)`; an explicit unit is `eta=119475+T` with `N(eta)=119475^2-2=57610 (mod 139129)`. Hence `122102*57610=73109 (mod 139129)`. This is an algebraic normalization witness **only**, not the authentic native eta, rank-one module or signed/odd Hesse/Green observable.

The BRC carriers remain separate: original ordered rational `B_k` population, source-tagged `g,h`, exact p-adic carry, ordinary Hesse coefficients, and the future native H0/B0 semilinear/signed ports. Similar notation `G_p` in the original scalar reduction and Hesse companion does not identify those quantities.

## Reproduction and continuation

Full local author package: `D25_SCALAR_SECOND_DIGIT_NORM_OBSERVER_AUTHOR_PORTABLE_20261110.zip` (5 files: source, exact JSON certificate, theorem, handoff, verification log), SHA-256 `57b44d3e46342195c21a8e1acd09541704a9ca2dec7aa63970b2013bb4714d95`. Certificate SHA-256 `273cd2769a8ce7f2272e0469ea11ffa810bcc50c02ae388afb00ed09e93b5895`. These hashes describe the author-side files and do not establish an uploaded native artifact.

Original Source read-only D25 continuation request `h40-20261110-1151-d25-exact-read-only` was `SUCCEEDED` with `execution_authorized=false`. Current `recovery_status` returned `SITE_CONTROL_OWN_ISSUED_SESSION_REQUIRED`; own winning CLAIM/open/run and native Source writer were **not** obtained. Preserve predecessor Source completed units and task publication; this note is an author derivation outside native checkpoint admission.

**Next exact action:** obtain the authenticated original-class fixed H0/B0 divided-power module and `[X]U mod p^2`, prove its actual rank, semilinear direction and pinned normalization eta, then compute the frozen `R_373` and compare with the present `Delta_373=196`. If rank-one, use the verified eta when comparing the native square to the separate ordinary Hesse candidate. Preserve signed odd port. No new dispatch or predecessor claim borrowing.

Separately, the original UR V2 four-file bundle (94,687 bytes; SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`) remains unlocated after a bounded source/library/local check. Already completed UR mathematics is not repeated; authentic bytes plus permitted writer/provenance/checkpoint are still needed.