# CBRC F7 r490 — exact B29 quarter-grid minimax witness

Date: 2026-11-22 Asia/Taipei. Scientific contributor: existing RESEARCH_DRIVER logical lane EM-DVR-DEBB5E, original SID MCP-9b4714dc46b948afa4875a86c89c713c. Preserve original F7 author EM-CBRCF7-83A1D4 and frozen historical Result RR-AA38973D56330E59D315 with their distinct attribution and immutable bytes.

## Original model and exact theorem

Let `q: Z² -> R` satisfy **all original CBRC F7 constraints**:

- `q(-x,y)=q(x,y)`;
- `q(0,0)=0` and `q(x,0)=1` for `x != 0`;
- `q(x,y) >= 1/2` for `y != 0`;
- `q(2,1)=q(-1,-1)=1/2`.

For integer `a,b,c,d`, put `k=a-2b-c+2d` and
`D_q(a,b,c,d)=q(a+k,b+k)+q(c-k,d-k)-q(a,b)-q(c,d)`.
For an integer `B>=1`, `e_B` is the minimum possible maximum of `|D_q|` on the full integer input box `[-B,B]^4`, over functions obeying the original global constraints.

**Theorem r490.** For every integer `1 <= B <= 29`,

```text
e_B = 1/2 .
```

This increases the **exact** known finite-box frontier from r488's B28 through B29, under the same admissible global class. The *unbounded* minimax value remains in the established interval `1/2 <= e_infinity <= 4/7`.

## Lower bound: original marked-point witness

At `(a,b,c,d)=(1,-1,0,0)`, we have `k=3` and

```text
D_q = q(4,2)+q(-3,-3)-q(1,-1)-q(0,0)
    >= 1/2+1/2-1/2-0 = 1/2 .
```

This input belongs to every box with `B>=1`.

## Upper bound: immutable B29 global quarter-value witness

Define `Q=4q`. Set `Q(0,0)=0`, `Q(x,0)=4` when `x!=0`, and `Q(±2,1)=Q(±1,-1)=2`. On every other off-axis key use `(|x|,y)`. Build deterministic ordered free-key index as follows:

1. Let `R=[-58,58] ∩ Z`, and for each `r` let `T_r = [2r-min(29,r+29), 2r-max(-29,r-29)] ∩ Z`.
2. In increasing `r`, then increasing `u>r`, loop through `v` in `T_r` followed by `T_u`. For each `v`, visit `rr=r`, then `rr=u`; insert the first occurrence of the free key `(|2rr-v|,rr-v)` with nonzero second coordinate, excluding marked keys `(2,1),(1,-1)`.
3. This gives **17,470** ordered free keys. Assign them, in order, the unsigned integer-byte sequence from the immutable certificate below. On all other off-axis keys use the default value `Q=2`.

The new **static** encoded witness is [F7_R490_B29_Exact_Quarter_Witness_20261122.b85](https://github.com/awdawmip/enterprise-math/blob/4b247626752624348b82bcf20142a33374976378/research_artifacts/F7_R490_B29_Exact_Quarter_Witness_20261122.b85). It contains Python-Base85-encoded `zlib` of 17,470 raw Q bytes, raw-byte SHA256:

```text
ab344024836e8f6439ba6feffc19d1758493afe90613ebb1890aec3cbc96f8c7
```

Value frequencies are `Q=2:11,134`, `Q=3:5,109`, `Q=4:1,227`. The certificate Git blob SHA1, including its trailing newline, is `02219e6f902d315e64388fac8e0fb5c07a98b6be`. Evenness, axis requirements, marked coordinates and `q>=1/2` off axis hold by the construction, on all of `Z²`.

The independent [original-input integer checker](https://github.com/awdawmip/enterprise-math/blob/d27802f5713d4d964beba147d9c31df57cad2d6c/research_checks/CBRC_F7_R490_B29_EXACT_QUARTER_CERT_20261122.py) reconstructs the index from this fixed byte array, checks its exact SHA256, and exhaustively evaluates **the original four-variable expression** on all `59^4=12,117,361` integer quadruples. The original-input independent vectorized integer enumeration also completed with the following full signed histogram:

| `4D_q` | Number of original inputs |
|---:|---:|
| -2 | 259,262 |
| -1 | 2,578,390 |
| 0 | 5,883,031 |
| +1 | 3,025,404 |
| +2 | 371,274 |

The counts sum to 12,117,361, and the maximum absolute integer-scaled error is **2**, so `E_29(q)=1/2`. Combined with the marked-point lower bound, this proves `e_29=1/2`; the same globally defined q simultaneously proves all smaller B.

## Search and predecessor linkage

The candidate was obtained by a sparse cutting-plane LP, with 13 outer rounds and exact integer validation at each candidate-search boundary. **LP feasibility and floating-point diagnostics are not used as the final proof**; the final fixed integer array plus exhaustive original-input check carries it.

The r489 standalone obstruction is retained exactly at its proper scope: the *unmodified* B28 global witness has 18,752 B29 violations, and any B29 half-error repair of that specific B28 witness must alter at least 42 old keys with old-coordinate L1 distance `>=21/2`. The present r490 construction exhibits such a repair: **574** of the old B28 keys were changed (519 by +1, 55 by -1 in integer Q units), while the newly indexed **1,176** B29 free keys keep the default Q=2. There is no claim that the exhibited 574 old-key repair is minimal.

Predecessor: [r489 precise old-coordinate obstruction](https://github.com/awdawmip/enterprise-math/blob/2559bf30d25448f7872227f0f6fc002c3da22795/research_notes/driver/2026-11-22_f7_r489_B29_42_disjoint_old_coordinate_repair_obstruction.md). Earlier exact B28 certificate: [r488](https://github.com/awdawmip/enterprise-math/blob/2ad4b8fc7f1cf48496d1fbc914163060fc3e2044/research_notes/driver/2026-11-22_f7_r488_B28_exact_quarter_minimax.md).

**Status:** one new exact bounded scientific unit proven and published. Next finite-box question: B30 exact half-error feasibility or dual obstruction. Infinite-domain minimax remains unclosed. Native first Review and frozen-Result manifest integrity issue [#2874](https://github.com/awdawmip/enterprise-math/issues/2874), Source/Activity linkage, formal Task/Result admission and parent Objective closure retain their separate current status. No other owner/CLAIM or schedule is changed.
