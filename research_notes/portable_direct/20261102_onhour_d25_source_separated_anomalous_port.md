# D25 / SECOND-DIGIT-LIFT: source-separated anomalous carry ports (2026-11-02)

**AUTHOR-DERIVED / PROVED LOCAL LEMMAS / EXACT FINITE CHECKS / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_EXPERIMENT.**
Neutral mathematical evidence only; not a Source checkpoint, Researcher CLAIM, run, review, or original H0/B0 computation.

- Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`
- Publication: `TP2-B6F4FC938FF94941C1B7`
- Frozen scientific Source pin (unchanged): `c47e13e4aba0e006366f989d6333ae3`.
- Parent target remains `Delta_p-R_p=0 (mod p)` for all `p=13,19 (mod 24)`, or an original-definition counterexample or strict reduction; accepted D24 first digit is not reopened.
- Consumes the prior two-digit result: `f1a9237ff70c89416a4be5e8f8ecf1e97609d7b5:research_notes/portable_direct/20261102_onhour_d25_joint_two_digit_carry_transfer.md`.

## 1. Original typed carriers and exact carry digit

For each prime `p>3` and `k=ap+b` with `0<=a,b<p`, keep both original sources separately:
```
A_k=(2k)!(3k)!/(k!)^5,   w_k=(6k+1)A_k/216^k  (source W),
B_k=(4k)!/(k!)^4,       s_k=(8k+1)B_k/2304^k (source S).
```
The coefficient rings are `Z_(p)`; weights, signs, index, factorial units and valuations remain in the observer state. These are auxiliary arithmetic indices, not Heartbeat World native X6 coordinates.

For `j=2,3,4`, define `c_j=floor(jb/p)`, `R_j=ja mod p`, `Q_j=floor(ja/p)`, and `delta_j=floor((R_j+c_j)/p)` (0 or 1). Define in the finite field:
```
Theta_j=(-1)^delta_j * ((R_j+c_j) mod p)!*(Q_j+delta_j)!
                           / ( R_j! * Q_j! * c_j! ).
```
**Digit-factor lemma, for every p>3 and every 0<=a,b<p:**
```
A_(ap+b) / [p^(delta_2+delta_3) A_a A_b] = Theta_2*Theta_3  (mod p),
B_(ap+b) / [p^delta_4 B_a B_b]           = Theta_4           (mod p).
```
Both quotient units are p-integral. Specifically
`v_p(A_(ap+b))=v_p(A_a)+v_p(A_b)+delta_2+delta_3` and
`v_p(B_(ap+b))=v_p(B_a)+v_p(B_b)+delta_4`.
When `delta_j=0`, `Theta_j=binomial(R_j+c_j,c_j)`; when `delta_j=1`,
`Theta_j=-(Q_j+1)*(R_j+c_j-p)!/(R_j!*c_j!)`.
Proof: apply the exact two-digit carry valuation and p-free factorial rule
`(n!/p^v) = (-1)^v * product_digit(digit!) (mod p)`
to the j factorial and the denominator factorials in each ratio; the high- and low-digit factorials cancel except the indicated `Theta_j`. The right-side denominators contain factorials below p, hence are invertible. Fermat reduces `216^(-ap)` and `2304^(-ap)` to their source-specific lower-digit factors modulo p.

## 2. Class-sensitive anomalous row support, modulo p^5

Let `p=6m+1`, `h=(p-1)/2=3m`. Here an anomalous W term means `delta_2+delta_3>0`, and an anomalous S term independently means `delta_4=1`. **Do not** identify index-only partitions with source-only partitions.

- W anomaly rows: `a=2m,3m,4m`; their respective b ranges start at `2m+1,3m+1,4m+1`. Their original valuation minima are respectively `2,4,6`. Thus the high W row vanishes modulo p^5, but the first and joint rows cannot be deleted termwise.
- For `p=13 (mod 24)` (p=1 mod4): S anomaly rows are `a=(p-1)/4,h,3(p-1)/4`, with minima `2,4,6`. The S joint-row **sum** vanishes mod p^5 by the earlier p^2 digit identity plus the known full-minus-half 2304 congruence mod p^3. Only the low S row can contribute mod p^5.
- For `p=19 (mod 24)` (p=3 mod4): S anomaly rows are `a=(p-3)/4,h,(3p-1)/4`; each term has valuation >=4. The joint-row sum again vanishes mod p^5; low and high S rows can contribute at order p^4. **No S anomalous term of valuation 2 or 3 exists in this class.**

The cited full-versus-half 2304 input is Guo–Zudilin, *A q-microscope for supercongruences*, Advances in Mathematics 346 (2019), 329–358, DOI 10.1016/j.aim.2019.02.008. The S tail's all-prime proof belongs to that work, not this new result.

## 3. First p^2 anomaly transport and signed BRC observer

For `a_W=2m`, `2m<b<=h`, put `C_W=A_(a_W)/216^(a_W) mod p`. There `(delta_2,delta_3)=(0,1)`, `Theta_2=Theta_3=1`. Valuations of `w_b,w_(a_W p+b)` are exactly 1 and 2, so
```
w_(a_W p+b)/p^2 = C_W*(w_b/p) (mod p);
P_W = C_W * sum_(2m<b<=h) (w_b/p) (mod p).
```
For `p=13 (mod24)`, with `a_S=(p-1)/4`, `C_S=B_(a_S)/2304^(a_S) mod p`, and `a_S<b<=h`, `delta_4=1`, `Theta_4=1`; hence
```
s_(a_S p+b)/p^2 = C_S*(s_b/p) (mod p);
P_S = C_S * sum_(a_S<b<=h) (s_b/p) (mod p).
```
Define a **partial signed source observer** `P=P_W-2*1_(p=13 mod24)*P_S mod p`. This is NOT the full signed W-2S sum, D25 Delta-R, a complete BRC quotient, or a native X6 spatial coordinate. No information-reducing collapse of the remainder is authorized without future-operator/observer certification.

## 4. Exact original arithmetic evidence

The standalone author-side integer runner `d25_anomaly_port_first_digit_20261102.py` checked 39,710 two-digit factorial-unit ratios; five primes `13,19,37,373,1171` were independently checked with original factorial terms modulo p^3; four primes `13,19,37,373` were source-split and tested through p^5, with the saved earlier complete p^2 scalar certificate as an independently cited input.

| p | C_W | sum(w_b/p) | P_W | C_S | sum(s_b/p) | P_S | P |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 13 | 12 | 6 | 7 | 10 | 2 | 7 | 6 |
| 19 | 11 | 7 | 1 | — | — | — | 1 |
| 37 | 10 | 16 | 12 | 4 | 34 | 25 | 36 |
| **373** | **169** | **27** | **87** | **196** | **24** | **228** | **4** |
| 1171 | 121 | 1107 | 453 | — | — | — | 453 |

For p=373, p^5=7,220,115,733,093. The exact anomalous original W sum is `3,273,400,399,232`, original S sum is `6,274,410,842,297`; their signed difference is `5,164,810,180,824 mod p^5`.
Its quotient by p^2 has base-p digits `4 + 306*p + 266*p^2 (mod p^3)`.
The complementary **nonanomalous W/S population plus the +p^2 baseline** equals `2,055,305,552,269 mod p^5`, exactly the additive inverse. This finite full-source compensation does not prove the all-prime D25 claim or the native operator benchmark.

A subtle correction to prior indexing: earlier W-only/S-only **index** bins included ordinary terms from the other stream. The index partition and its complete sums were valid, but cannot be reported as isolated anomalous-source contributions; the new split is exactly source typed.

## 5. Scientific continuation and missing native acceptance

**Finished**: all-prime factorial-unit transport, carry-row filtration, class-sensitive first anomaly ports, and 39,710 finite exact checks. **Still open**: uniform original Delta-R, and a source-preserving WZ/Dwork telescope yielding the nonanomalous p^3/p^4 **compensator** for the anomaly rather than fitting one prime. Next exact step: construct that compensator using the delta=0 factorial-unit block and separately test p=13 and p=19 residue classes.

Native original H0/B0 divided-power at p=373, `[X]U mod 139129`, module rank, semilinear Frobenius direction and eta, signed odd Green/Hesse, kappa and independent checker remain `PENDING_OWNER / NOT_EXECUTED` per `awdawmip/enterprise-math#1559`. This math work is not the native benchmark.

Existing Research lane is `chatgpt-research-onhour-enterprise-math-20260923`; no maintenance conversation operation. Old request `research-onhour-20261031-0205-dispatch-r15` is terminal FAILED / UPSTREAM_CODE_REVIEW_REQUIRED (issue `awdawmip/kimi-query-bridge#6633`), and was not resent. **No own verified Source Researcher session, CLAIM, run, or canonical Source checkpoint** was established. All statements remain `AUTHOR-DERIVED / UNREVIEWED / NOT_ADMITTED`; a GitHub note is evidence storage only. Existing recurrence/notifications unchanged.
