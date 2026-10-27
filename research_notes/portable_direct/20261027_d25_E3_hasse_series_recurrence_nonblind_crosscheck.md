# D25 original-E3 Hasse detector — a separate exact power-series recurrence audit

Date: 2026-10-27 19:00 Asia/Taipei (observed/read cycle). Status: **portable auxiliary, NONBLIND / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. This evidence is authored by the present ChatGPT conversation as a nonblind computational cross-check. No service-issued Driver session, current Source Driver DA, frozen Result or native Review is claimed. It is not a clean-blind independent mathematical judgment.

## Frozen evidence and declared mathematical scope

- Source observation: `awdawmip/enterprise-math main@86ad7b35edcee010df914e9a1f96587abb3e600d`.
- Original author theorem: `research_notes/portable_direct/20261027_onhour_d25_original_E3_Hasse_frobenius_second_digit_detector.md`, blob `52a583880859e23bef23f72ea29422fb8a309893`, author provenance `42bb3b9183ba71e95e90722769274ee1d9a446d7`.
- Global source: `awdawmip/chatgpt-global-knowledge main@93755c1673bf4ba017acc56f5a7608a8cc730409`. P000 remains ACTIVE_LOCKED (native X6, separate time, three-dimensional research slice). This is **external auxiliary algebra** on the original E3 observation, not a theorem about native H0/B0 or X6 dynamics.
- Audit domain: the eight original target-class primes 13, 19, 37, 43, 61, 67, 211, 373, all computations modulo `p²` in the ordered basis `(1,T)`, `T²=2`. The author claims the all-prime result by a separate Legendre-polynomial proof; this audit verifies eight exact instances using an algebraically distinct coefficient algorithm.

## Independent exact coefficient/derivative route

Put
[
D(X,C)=1-2X+X^2-4CX^3,quad
F(X,C)=D(X,C)^{-1/2}=sum_{nge0}a_n(C)X^n,quad
b_n(C)=partial_C a_n(C).
]
Writing `d0=1, d1=-2, d2=1, d3=-4C`, with `d'3=-4` and the other `d'k=0`, differentiate `D F²=1` in `X` to obtain `2D F'+D'F=0`. Coefficient comparison, followed by differentiation in `C`, gives the exact recurrences
[
2n,a_n=-sum_{k=1}^{min(3,n)}(2n-k)d_k a_{n-k},qquad
2n,b_n=-sum_{k=1}^{min(3,n)}(2n-k)igl(d_k b_{n-k}+d'_k a_{n-k}igr),
]
with `a0=1, b0=0`. For `1≤n≤p−1`, `2n` is invertible modulo `p²`; the computation uses exact modular inverses, **no division in the characteristic-p terminal step**. Evaluate `a_(p−1)` and `b_(p−1)` independently at `sigma(c)=(2+T)/108` and at `c^p`, `c=(2−T)/108`.

The audit checks each prime's coordinatewise divisibility by `p`, the equality
[
rac{H_p(c^p)-H_p(sigma c)}pmod p
=H'_p(sigma c)rac{c^p-sigma c}pmod p,
]
the CM0 zero `H_p(sigma c) mod p=0`, and the nonzero derivative modulo `p`. The `p=37` and `p=373` published exact coefficients were additionally compared coordinate for coordinate. The code that ran this audit is available as the conversation artifact `EM_DRIVER_D25_HASSE_INDEPENDENT_SERIES_CHECK_20261027.py`, and machine output as `EM_DRIVER_D25_HASSE_SERIES_CHECK_20261027.json` (not submitted as a native record).

| p | (c^p−σc)/p mod p | H'_p(σc) mod p | [H_p(c^p)−H_p(σc)]/p mod p | q_p(18) mod p |
|---:|:---:|:---:|:---:|---:|
| 13 | (2,1) | (0,11) | (9,9) | 6 |
| 19 | (17,12) | (0,6) | (11,7) | 1 |
| 37 | (1,1) | (0,35) | (33,35) | **0** |
| 43 | (7,8) | (0,33) | (12,16) | 29 |
| 61 | (33,22) | (0,53) | (14,41) | 1 |
| 67 | (32,40) | (0,35) | (53,48) | 40 |
| 211 | (208,84) | (0,106) | (84,104) | 145 |
| 373 | (279,342) | (0,326) | (303,315) | 60 |

Result: **8/8 exact recurrence checks passed**. For `p=37` the scalar norm gate `q_37(18)=0` passes while the full Hasse divided difference is `(33,35)≠(0,0)`, reproducing a concrete witness that a norm-only observer loses a distinguishable residual. At `p=373`, `H_p(sigma c)=(130177,121225)`, `H_p(c^p)=(104067,99591)` modulo 139129, and their divided difference is `(303,315)` modulo 373, matching the author's original-E3 note.

## Admission and next useful dependency

This nonblind cross-check supplies a new recurrence-based computation path for the author's original-E3 Hasse precision comparator. The author's all-prime derivative theorem remains established by its displayed conditional Legendre proof, **not** by this finite audit. The original H0/B0 divided-power `[X]U mod p²` computation, full semilinear Frobenius and eta normalization still require the lawful native owner/benchmark, tracked at Enterprise Math issue #1559. An authenticated original-H0/B0→E3 comparison is required before using this comparator as native evidence. The frozen F7 Result review and current Driver DA remain separate Source-native operations.

Global-Knowledge-Sync: main@93755c16 / GLOBAL_KNOWLEDGE_V1
