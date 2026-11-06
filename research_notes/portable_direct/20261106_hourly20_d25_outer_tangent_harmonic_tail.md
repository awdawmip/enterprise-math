# D25 — explicit harmonic head / carry-tail reduction for the outer-source derivative

Date: 2026-11-06. Scoped author-side portable TASK_RESEARCH, configured logical lane `chatgpt-research-hourly-enterprise-math-20260923` (no platform identity attestation). Publication `TP2-B6F4FC938FF94941C1B7`, task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, immutable scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged. Status: EXACT ALGEBRAIC REDUCTION / EXECUTED FINITE CHECKS / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT.

## Statement

Fix a prime `p=6m+1>=7`, `s=(2m,3m,4m)`. Work in `F_p`; define `H_n=Σ_{k=1}^n 1/k` and `H_0=0`, and use the labelled auxiliary sources

`U_j(x1,x2,x3)=(-1/2)^j ∏_i binom(s_i+x_i,j)`,
`F_p(x)=Σ_{j=0}^{p-1}(6j+1)U_j(x)`,
`T_i=∂_iF_p(0)`.

Define the *harmonic head* and *carry tail* using only ordinary binomial numbers and invertible finite-field denominators:

```
A_m = Σ_{j=0}^{2m} (6j+1) 2^{-j} binom(2m,j) binom(3m,j)
      binom(2m+j,j) [2 H_{2m} - H_{2m-j} - H_{2m+j}],

B_m = Σ_{r=1}^{m} (6(2m+r)+1) 2^{-(2m+r)}
      binom(3m,2m+r) binom(4m,2m+r)
      / [r * binom(2m+r,2m)].
```

**Exact theorem for all such primes:**
```
                  T_1 + T_3 = A_m - B_m   (mod p).
```

This is a reduction of the original outer-tangent conjecture `T_1+T_3=0` to one explicit finite harmonic/binomial identity `A_m=B_m`, whose two sides have distinct provenance: ordinary labelled coefficients at `j<=2m`, and the single first-source carry at `2m<j<=3m`. The reduction itself is proved for every prime in the domain. Vanishing of the right-hand side for arbitrary primes is the next open statement.

## Proof and source provenance

The identity `4m=p-1-2m` gives the finite-field binomial reflection

`binom(4m,j)=(-1)^j binom(2m+j,j)` for `0<=j<=2m`.

On that range, `U_j(0)=2^{-j}binom(2m,j)binom(3m,j)binom(2m+j,j)`. For `j<=2m`, ordinary polynomial differentiation gives
`∂_1U_j(0)=U_j(0)(H_{2m}-H_{2m-j})` and
`∂_3U_j(0)=U_j(0)(H_{4m}-H_{4m-j})`.

Because `H_{p-1-n}=H_n` in `F_p` for `0<=n<p`, we have `H_{4m}=H_{2m}` and `H_{4m-j}=H_{2m+j}`. Their sum produces the displayed symmetric harmonic second difference, i.e. the entire `A_m`.

For `j=2m+r`, `1<=r<=m`, the unperturbed first binomial factor vanishes while its derivative survives:
```
 ∂_x binom(2m+x,2m+r)|_{x=0}
 = (-1)^{r-1} (2m)! (r-1)!/(2m+r)!
 = (-1)^{r-1}/[r binom(2m+r,2m)].
```
Multiplying by `(-1/2)^{2m+r}` fixes the sign to minus, and multiplying the remaining two binomial factors gives exactly the negative summand of `B_m`. The third-source derivative vanishes here because the first binomial factor is zero. For `j>3m`, the fixed second factor `binom(3m,j)` vanishes together with the outer derivatives. Thus `T_1+T_3=A_m-B_m`. All factorials and harmonic denominators are units modulo `p`, so every step is valid in `F_p`. QED.

## Exact execution

A standalone local standard-library program `/mnt/data/d25_outer_harmonic_reduction_20261106.py` evaluated the two displayed explicit sums using factorials, inverse factorials and harmonics modulo `p`, and **independently** formed `T` by direct polynomial product-differentiation recurrence. It compared the two results for all **330** primes `7<=p<=5000`, `p≡1(mod 6)`. All equalities passed; in this bounded set each `A_m-B_m=0`.

Representative `(p,A_m,-B_m,T_1+T_3)` modulo `p`:
```
(7,    2,    5,   0)
(13,   5,    8,   0)
(19,   2,   17,   0)
(109, 46,   63,   0)
(211,178,   33,   0)
(229,218,   11,   0)
(373, 81,  292,   0)
(1093,725, 368,   0)
(3511,1513,1998,  0)
```

These are exact integer residue checks, not a universal proof that `A_m=B_m`.

## Reuse and next action

Use the two-term representation as an explicit WZ/creative-telescoping target; attempt a rational hypergeometric certificate relating the harmonic head to the first-carry tail, preserving the `j<=2m` versus `2m<j<=3m` source boundary. Separately investigate the earlier conjectural `k_p+3q_p(2)=0` and restore the original compensated `Theta_p` and frozen H0/B0/Frobenius obligations. The last author-side result `20261106_hourly20_d25_adaptive_two_port_source_codec.md` supplies an optimal first-order source reconstruction protocol; it does not prove the new harmonic equality.

Control state carried forward: original requests `em-h20-20261106-1324-d25-task-r13`, `em-h20-20261106-1324-d25-cont-r13`; Source continuation still nonterminal `WAITING_RESOURCE/EVENT_COLLECTION_IO` after same-ID reconcile. Actual successor session, own CLAIM/run and protected staging have not been verified; issue #1558 retains the control defect. No new role-bound Source checkpoint was written.
