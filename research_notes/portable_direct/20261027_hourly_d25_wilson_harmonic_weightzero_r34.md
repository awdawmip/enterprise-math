# D25/LIFT R34 — Wilson–harmonic fourth-digit lift at the genuine p≡19 (mod 24) S-weight-zero source

Date: 2026-10-27 (Asia/Hong_Kong). TASK_RESEARCH logical conversation `chatgpt-research-hourly-enterprise-math-20260923`, distinct from CONTROL_PLANE_MAINTENANCE. Parent D25/LIFT/JT2 OPEN. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, frozen *scientific* source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` (not the mutable control head).

Status: **AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY**. No Source checkpoint, native original-class CM experiment, formal Result or independent review. R23's half-tail, R29's first unit residues and R33's changed-input observer are consumed, not recredited. Scope: original unchanged W/S coefficient sources.

## Genuine unresolved arithmetic input

R23 reduces the OPEN all-prime W/S bridge to `D_p ≡ −p² U_p (mod p³)` where `D_p=Σ_{j=0}^{(p−1)/2}(w_j−s_j)` and `U_p` is the genuine W-high reflected port. R29 shows that for p≡19 (mod24) the unique p-divisible S weight lies **inside** this low-half sum and gives only `w_k/p (mod p)` and `s_k/p² (mod p)`. The missing source-level higher jet is derived here.

For each prime `p≡19 (mod24)` set

```text
k=(3p−1)/8, r=(p−3)/8, R=(p−1)/2;
2k=p−1−2r, 3k=p+r, 4k=p+R;
6k+1=(1+9p)/4, 8k+1=3p;
w_k=(6k+1)(2k)!(3k)!/[(k!)^5 216^k];
s_k=(8k+1)(4k)!/[(k!)^4 2304^k].
Q_p=((p−1)!+1)/p; H_n=Σ_{i=1}^n 1/i; H_n^(2)=Σ_{i=1}^n 1/i²;
A=H_r+H_(2r);
B=(A²+H_(2r)^(2)−H_r^(2))/2;
C=r!/[4(2r)!(k!)^5 216^k]; D=R!/[(k!)^4 2304^k].
```

All displayed denominators are p-units; Wilson's theorem makes Q_p integral. The carrier preserves the original W/S series label, integer rank, valuation, normalized p-adic jet, observation precision and subsequent low-half/W-high/WZ operation. Rank is an arithmetic source index, not a P000 spatial axis.

## Theorem A — exact factorization and p-adic source jets

The following are exact rational identities (not just finite-prime observations):

```text
w_k/p = C(1+9p)((p−1)!)²
        × Π_{i=1}^r(1+p/i) / Π_{i=1}^{2r}(1−p/i),       (A1)
s_k/p² = −3D(1−pQ_p) Π_{i=1}^R(1+p/i).                (A2)
```

Define `E1=9+A−2Q_p` and `E2=B−2Q_p A+Q_p²+9(A−2Q_p)`. Then **for all** prime p≡19 (mod24), in Z_(p):

```text
w_k/p   ≡ C[1+pE1+p²E2]                    (mod p³), (A3)
s_k/p² ≡ −3D[1+p(H_R−Q_p)]                (mod p²), (A4)
(w_k−s_k)/p ≡ C[1+pE1+p²E2]
               +3pD[1+p(H_R−Q_p)]        (mod p³). (A5)
```

Consequently (A5) is a **fourth-digit source certificate** for `(w_k−s_k) mod p⁴`. The factor C must be evaluated with its actual residue modulo the indicated power, not replaced by its first digit. This is a source-specific algebraic identity, not a global W/S supercongruence.

**Proof.** Because `2r` is even and `2k=p−1−2r`, direct factorial splitting gives

```text
(2k)! = (p−1)! / [(2r)! Π_{i=1}^{2r}(1−p/i)],
(3k)!/p = (p−1)!r! Π_{i=1}^r(1+p/i),
(4k)!/p = (p−1)!R! Π_{i=1}^R(1+p/i).
```

Substituting the exact integer weights and `(p−1)!=−1+pQ_p` proves (A1),(A2). The product of the first two rational factors in (A1) has expansion

```text
Π_{i=1}^r(1+p/i) = 1+pH_r+(p²/2)(H_r²−H_r^(2))   (mod p³),
Π_{i=1}^{2r}(1−p/i)^(-1)
  = 1+pH_(2r)+(p²/2)(H_(2r)²+H_(2r)^(2))        (mod p³).
```

Their product equals `1+pA+p²B (mod p³)`. Multiplying by `((p−1)!)²=(−1+pQ_p)²=1−2pQ_p+p²Q_p²` and `(1+9p)` yields E1,E2. First-order expansion of (A2) gives (A4). Subtraction of the two original source terms gives (A5). Each step is exact or a valid p-adic expansion in p-units and holds for every prime in the claimed residue class. QED.

## Corollary — sharper but still OPEN unchanged-input WZ obligation

Let `D'_p=Σ_{0≤j≤R,j≠k}(w_j−s_j)`. Combining (A3)–(A4) with the existing R23 reduction shows that the **open** bridge `D_p≡−p²U_p (mod p³)` is **equivalent** to

```text
D'_p ≡ −pC − p²(CE1+3D+U_p)   (mod p³).         (C1)
```

Retain the p²-accurate unit C in `pC`. Equation (C1) is a reduction/necessary-and-sufficient *target*, not a proved universal cancellation. Any real unchanged-input WZ compensator must cancel the isolated W first digit and preserve its Wilson–harmonic lift, the distinct S order-two port, the W-high U_p and all corresponding Green/Hasse source labels.

## Executed author check

Python-standard-library direct integer factorial reconstruction independently evaluates the original `w_k/p`, `s_k/p²`, and their quotient difference before reducing modulo the specified powers. For **all 37 primes p<2000 with p≡19 (mod24)**, it checks (A3) modulo p³, (A4) modulo p² and (A5) modulo p³: **111 exact assertions PASS**. No float, no native CM experiment, no target-supercongruence assumption. Example `(p,k,r,w/p mod p³,s/p² mod p²,(w−s)/p mod p³)`:

```text
(19,7,2,1495,314,2388)
(43,16,5,12118,1447,29404)
(67,25,8,240789,2322,85215)
(139,52,17,1815192,10331,379183)
(163,61,20,3982703,5812,3035347)
```

The adjacent file `20261027_hourly_d25_wilson_harmonic_weightzero_r34_check.py` is the reproducible checker. The finite check is not the proof of generality. Established Wilson/harmonic expansions are used without claiming worldwide mathematical novelty.

**BRC COMPOSE_APPLIED:** source-specific valuation and harmonic jets form a typed repair coordinate. Collapsing to scalar totals or modulo-p coefficients erases information needed by the future p³/p⁴ observer; no positive-mass cancellation or P000 theorem is inferred.

## Native Source and continuation (read-only at 2026-10-27T04:22Z)

Exact ordinary-control Research-lane recovery request `emr-20261027T1220-recovery-r34-01` SUCCEEDED: no local pending mutation, run, unopened claim or unpublished upload; own service session `MCP-06f7ad61a8d841d9ba1ba1ef4d088d94` / Researcher `EM-ENTERPRISE-5298BA`; two existing neutral staging archives preserved. Current exact continuation request `emr-20261027T1221-continuation-r34-03` SUCCEEDED, route `REGISTER_NEW_SESSION_AND_CLAIM_CURRENT_PUBLICATION`, `execution_authorized=false`, native `persisted_checkpoint.state=SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED`. This recovery projection is not Source ownership. The historical predecessor-claim mismatch remains subject to control Issue #1558; the formally pinned Hesse/gauge checkpoint is not overwritten or reclassified as portable research.

**Next actual scientific unit:** investigate an unchanged-input, genuinely cross-source compensator for (C1), incorporating R28 boundary-aware Green adjoint, p≡13 W-high/S-mid distinct ports and the original six fixed-z=2 Hasse J/E sources. Separately the native D25 route needs authenticated original-class H0/B0, [X]U mod p², semilinear Frobenius eta/kappa, actual p373 experiment and independent Driver review. Scientific source pin and ACTIVE P000/worldview remain frozen. No scheduler/notification changes.
