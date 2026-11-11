# R5 — Fourth bilateral resonance coalescence, with a simultaneous minimizer switch on the negative edge

**Date:** 2026-11-12 (Asia/Shanghai). Researcher-side exact rational finite computation. Same frozen external 28-mass P/Q–BRC Blackwell observer, fifteen labeled BRC atoms and scientific pins as the sibling `RESEARCH.md`. This does not alter P000 or assert native X6 transfer.

Let `x=155682221/25142124560000000` and `t_q(eta)=(x-23eta)/q` for `q∈{15,12,3}`. Retain all 1144 fixed interior first-zero thresholds `36x/k` from the original target0/source3 integer subset sum spectrum. Following the certified third signed collisions `eta3+=x/6233`, `eta3-=-x/6187`, the fourth collisions between a moving and a fixed phase are:

| sign | fourth eta | merged epsilon | first-zero masks at phase | legal 15-atom orders before | after | loss |
|---|---|---|---:|---:|---:|---:|
| positive | `x/4991=155682221/125484343678960000000` | `36x/434=1401139989/2727920514760000000` | **4085** | **347184510312** | **207530420752** | **139654089560** |
| negative | `-x/4945=-155682221/124327805949200000000` | `36x/430=1401139989/2702778390200000000` | **4078** | **343192915116** | **205040640100** | **138152275016** |

At either exact parameter edge, the complete 32768-mask/28-coordinate prefix test yields **1146 distinct interior first-zero phase values**. Rational points immediately inside and outside each edge have 1147; the exact interval assertion on the approach to the positive edge follows the pre-existing no-minimizer-switch bound `|eta|<x/4945`. The negative edge lies exactly at that minimizer-switch bound; only its exact edge and immediately adjacent rational samples are asserted by this new finite execution beyond the earlier certified range.

**Adjacent two-cut attribution**, on a rational parameter between the third and fourth edge:
- positive: fixed k434 first (17 masks, 838670712 order losses), then moving q12 (4068 masks, 138815418848 order losses). Exact total 4085 masks and 139654089560 orders.
- negative: moving q12 first (4065 masks, 137622692288 losses), then fixed k430 (13 masks, 529582728 losses). Exact total 4078 masks and 138152275016 orders.

A new structural coincidence occurs at the negative fourth edge `eta=-x/4945`: **the first coordinate-minimizer switch and the fourth phase-value collision occur at the same parameter**. For prefix subset bitmask **14357** the minimizing first-zero coordinate changes from **(target 1, source 3)** just inside to **(target 0, source 3)** just outside, with *both* active and equal at the edge. That tie is at `epsilon=36x/430`. These exact minima follow directly from the published rational 28-coordinate prefix expression `min_{k:P(S)_k<0} -36[X_k+eta H_k]/P(S)_k`. The equality explains why the previously proven fixed active-index chamber ends at this same edge; it does not by itself settle the full phase arrangement beyond that boundary.

Proof/evidence: `VERIFY_FOURTH_COLLISION.py` imports the sibling self-contained rational verifier, checks complete first-zero spectrum and exact before/after integer Boolean-lattice schedule counts at both fourth edges and their neighboring points; `FOURTH_OUTPUT.txt` records its local executed output. The explicit mask-14357 minimizer computation is derived from the same exact prefix vectors and is independently inspectable with that script's `P, X, H, V` arrays.

**Next:** resolve all minimizer-switch events immediately beyond `-x/4945`; distinguish moving/fixed phase collision from the birth, death or reallocation of active first-zero-coordinate families. Independently audit the broader fifteen-step hidden-fiber upper-bound question. Formal Source Result and independent review pending.
