# D25 original-E3 Hasse detector — independent formal-power-series recurrence audit

Observed: 2026-10-27 (Asia/Taipei). Status: **PORTABLE AUXILIARY / NONBLIND / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. This is a distinct computational route prepared by the current conversation, not an independent Source-native Driver review, canonical checkpoint or result. Author provenance and existing source notes are preserved.

## Provenance and scope

- Verified Enterprise Math starting source: main@86ad7b35edcee010df914e9a1f96587abb3e600d.
- Author theorem: research_notes/portable_direct/20261027_onhour_d25_original_E3_Hasse_frobenius_second_digit_detector.md, Git blob 52a583880859e23bef23f72ea29422fb8a309893, original commit 42bb3b9183ba71e95e90722769274ee1d9a446d7.
- Global Knowledge: main@93755c1673bf4ba017acc56f5a7608a8cc730409; P000 is ACTIVE_LOCKED. The audit is auxiliary classical algebra, not a claim about native X6/three-dimensional slice dynamics or original H0/B0 divided-power [X]U.
- Actual exact verification domain: primes 13, 19, 37, 43, 61, 67, 211, 373; arithmetic in the ring (Z/p²Z)[T]/(T²−2), with each element written as (a,b) meaning a+bT. These primes are in the author's declared classes.

## Separate coefficient and derivative algorithm

Set D(X,C)=1−2X+X²−4CX³ and F(X,C)=D(X,C)^(−1/2)=Σ[n≥0] a_n(C) X^n, with b_n(C)=∂a_n/∂C. Let d_0=1, d_1=−2, d_2=1, d_3=−4C and d'_1=d'_2=0, d'_3=−4. Formal differentiation in X of D F²=1 gives 2D F' + D'F=0, hence for n≥1:

    2n a_n = − Σ[k=1..min(3,n)] (2n−k) d_k a_(n−k)
    2n b_n = − Σ[k=1..min(3,n)] (2n−k) (d_k b_(n−k) + d'_k a_(n−k)).

Initial conditions a_0=1 and b_0=0. For 1≤n≤p−1, every 2n is invertible modulo p². The coefficient H_p(C) is exactly a_(p−1)(C), and H'_p(C) is b_(p−1)(C). This avoids the author's explicit integer-binomial sum and Legendre recurrence; both algorithms calculate the *same original-E3 coefficient*, rather than a renamed replacement model.

The audit forms c=(2−T)/108, sigma(c)=(2+T)/108, computes c^p modulo p², and checks coordinatewise divisibility by p, the exact first-order Taylor quotient modulo p, the accepted-CM0 premise H_p(sigma(c)) mod p = 0 for each tested prime, and nonzero H'_p(sigma(c)) modulo p. Every calculation uses integers, modular inverses and explicit ring pairs.

| Prime p | δ=(c^p−sigma(c))/p mod p | H'_p(sigma(c)) mod p | (H_p(c^p)−H_p(sigma(c)))/p mod p | q_p(18) mod p |
| ---: | :---: | :---: | :---: | ---: |
| 13 | (2,1) | (0,11) | (9,9) | 6 |
| 19 | (17,12) | (0,6) | (11,7) | 1 |
| 37 | (1,1) | (0,35) | (33,35) | **0** |
| 43 | (7,8) | (0,33) | (12,16) | 29 |
| 61 | (33,22) | (0,53) | (14,41) | 1 |
| 67 | (32,40) | (0,35) | (53,48) | 40 |
| 211 | (208,84) | (0,106) | (84,104) | 145 |
| 373 | (279,342) | (0,326) | (303,315) | 60 |

**Observed finite result: 8/8 exact checks PASS.** At p=37 the scalar norm/Fermat quotient gate q_37(18)=0 passes, but the two-component divided Hasse difference is (33,35) ≠ (0,0), so that scalar compression loses an observer-visible distinction. At p=373, H_p(sigma(c))=(130177,121225), H_p(c^p)=(104067,99591) modulo 139129, giving quotient (303,315) modulo 373.

The author provides an all-target algebraic proof using finite Legendre polynomials and a simple-zero argument, *conditional on accepted CM0*. This finite recurrence audit corroborates eight specified cases. It does not independently prove the universal theorem, settle original LIFT or supply native H0/B0 Frobenius evidence.

## Native admission and next dependency

The original H0/B0 benchmark first at p=373 still requires actual original-category [X]U mod p², integral basis and eta normalization, full semilinear Frobenius direction, signed odd observer and the frozen Δ−R comparison; existing Enterprise Math issue #1559 tracks that original request. The authentic H0/B0→E3 bridge must be established before interpreting this exact Hasse detector as native evidence. CBRC-F7 frozen Result still needs independent current exact-set Driver review with actual DA.

The executing conversation had access to GitHub archival publication but Site scope only source:read/control:read and no current Driver DA. The corresponding script and complete output are preserved as conversation artifacts EM_DRIVER_D25_HASSE_INDEPENDENT_SERIES_CHECK_20261027.py and EM_DRIVER_D25_HASSE_SERIES_CHECK_20261027.json. No native Driver write, Source CLAIM, OPEN, Review, Reference, Synthesis, Follow-up or new task was made.

Global-Knowledge-Sync: main@93755c16 / GLOBAL_KNOWLEDGE_V1
