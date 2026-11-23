# T6: exact-v₂(d)=5 count rigidity modulo 64; empty-side exclusion and seven residual 64-gap profiles

2026-11-23 (Asia/Taipei). Research and exact enumeration by the continuing original Research Driver `EM-DVR-DEBB5E`. Earlier universal `v₂(d)>=6` cancellation certificates, and their contributors, are retained as prior dependencies. This is a scoped mathematical report, **not** a Native Result/Review, Task CLAIM or formal Activity publication.

## Model and dependencies

Let `A,B` be finite multisets of positive integers `e`, each independently satisfying `sum(e)<=2331`; set `d=e+1`. Let `H_k(X)=sum_{e in X}(e/(e+1))^k` and assume `H_k(A)=H_k(B)` for `k=0,...,6`. Binomial inversion gives equality of `S_k(X)=sum_{e in X}d^{-k}` for `k=1,...,6`.

Reuse the earlier published exact cancellation of all `v₂(d)>=6` denominators, including [the exact-v₂=6 certificate](https://github.com/awdawmip/enterprise-math/blob/c577f07bcd434340c500b91e4b67a5402c82c514/research_notes/driver/2026-11-23_t6_p2_sixth_universal_cancellation_three_tier.md). The theorem below is conditional on that established cancellation, not a new independent recheck of its full finite enumeration.

Write `δ_j=m_A(32j)-m_B(32j)` for odd `1<=j<=71` and `N=sum_j δ_j`. Let

`D_k=sum_{j odd} δ_j*j^(-k)`, and `L_k=sum_{j odd} (m_A(16j)-m_B(16j))*j^(-k)`.

After literal cancellation of matching `v₂>=6` terms, multiply the exact `S_k` equality by `2^(5k)`. It implies the following necessary congruences in the 2-adic integers, with inverses taken only of odd units:

```
D_k == 0                  (mod 2^k),
D_k + 2^k*L_k == 0        (mod 2^(2k)),     1<=k<=6.
```

Indeed all `v₂<=4` terms vanish in the first modulus; all `v₂<=3` terms vanish in the second. No independent rational equality of prime-valuation components is assumed.

## Theorem 1: the exact-v₂=5 population gap is divisible by 64

**Claim:** `N ≡ 0 (mod 64)`.

**Elementary proof:** For each odd `j`, write `b_j=(j^(-2)-1)/8`, a 2-adic integer because each odd square is 1 modulo 8. Put `B=sum δ_j*b_j`, `C=sum δ_j*b_j^2`; all three are 2-adic integers. Using `j^(-4)=(1+8b_j)^2` and `j^(-6)=(1+8b_j)^3`,

```
D_2 = N + 8B,
D_4 = N + 16B + 64C,
D_6 = N + 24B + 192C + 512 Σδ_j*b_j^3.
```

The first-tier condition at `k=4` gives `N=16m` for an integer `m`. The first tier at `k=6`, reduced modulo 64, gives `16m+24B=0 (mod64)`, hence `B=2m (mod8)`.

The second tier at `k=2`, divided by `2^2`, forces `L_2=-(N+8B)/4=-2B (mod4)`, so `L_2=0 (mod4)`. The second tier at `k=4`, divided by `2^4`, forces `L_4=-(m+B+4C)=-m-B=m (mod4)`. But each odd `j` satisfies `j^(-2)=j^(-4)=1 (mod4)`; thus `L_2=L_4 (mod4)`. It follows that `m=0 (mod4)`, giving `N=0 (mod64)`. QED.

Since `0<=n_X:=sum_{j odd}m_X(32j)<=floor(2331/31)=75`, the only nonzero possible population differences are `±64`. In particular any two sides whose exact-v₂=5 occurrence counts differ by less than 64 **must have the same count**. This strengthens the [earlier modulo16 and local minimal-mass note](https://github.com/awdawmip/enterprise-math/blob/d56218fd59bcbffd67935c64fc10335c82b5bee3/research_notes/driver/2026-11-23_t6_v2fifth_16_count_gap_residue_parity_one_sided_minimal_mass.md); that note's finite 16-atom local optimizer remains correct in its original strictly local scope.

## Theorem 2: an empty exact-v₂=5 side cannot face a nonempty side

If `n_A=0` then necessarily `n_B=0`, and conversely.

**Proof:** By Theorem 1 a hypothetical nonempty side against an empty side must contain exactly 64 atoms. Write the odd quotients `j_i=1+2a_i` with `a_i>=0` and `Q=sum a_i`. Its layer mass is `31*64+64Q<=2331`, so `0<=Q<=5`. The first-tier `k=3` congruence uses `j^(-3)=j (mod8)`, giving `64+2Q=0 (mod8)` and hence `Q=0 or 4`.

If `Q=4`, its five unordered positive-excess partitions are `(4), (3,1), (2,2), (2,1,1), (1,1,1,1)`. Direct exact modular evaluation gives their `D_5 mod32` as `24,16,24,16,8` respectively, all inconsistent with the first-tier `k=5` congruence.

If `Q=0`, all 64 quotients equal 1, so `D_3=D_5=64`. The second-tier congruences imply `L_3=-64/8=0 (mod8)` while `L_5=-64/32=6 (mod8)`. For every odd `j`, `j^(-3)=j^(-5) (mod8)`, hence `L_3=L_5 (mod8)`, contradiction. Therefore the count gap ±64 cannot have an empty side. QED.

## Complete necessary sieve for the remaining 64-count gaps

By symmetry put `n_A=64+s` and `n_B=s`, `s>=1`. Mass bounds force `s<=11`. Each side's odd quotients are exactly represented by the nonnegative integer partition of `Q=sum(j-1)/2` into at most its atom count, with zeros padded. Their exact layer mass is `31n+64Q`. This enumerates **every** admissible exact-v₂=5 profile on both sides, not a random subset.

Using the six congruences from the first tier above on all two-sided profiles gives the following exact finite census:

| Filter | Remaining full-budget profile pairs |
| --- | ---: |
| All pairs meeting the individual mass bounds | 382,145 |
| Six first-tier local congruences | 2,906 |
| The six second-tier congruences with an unrestricted exact-v₂=4 signature subgroup | 39 |
| Exact minimum exponent-mass feasibility for both exact-v₂=4 signatures | **7** |

The unrestricted subgroup is generated by `(j^(-k) mod 2^k)_{k=1..6}` for all odd units `j mod64`; complete finite-group closure has **2,048** distinct elements. For each first-tier-compatible profile pair, divide the signed `D_k` residue modulo `2^(2k)` by `2^k` and negate to obtain the necessary v₂=4 correction signature `T`. It must be representable as `V_A - V_B` for the two sides' actual v₂=4 nonnegative multisets.

For each of the 2,048 group elements, Dijkstra shortest paths from the zero signature using one atom `d=16j` per generator and the exact exponent cost `16j-1` compute the minimum mass of any nonnegative v₂=4 profile. Only odd `j<=41` are needed: the greatest relevant remaining side budget in the 64-gap cases is 640, and `d=16*41` already costs 655, beyond it. Every feasible v₂=4 multiset therefore has an exact path in this finite graph. For each pair, test whether some group element `V_B` and `V_A=V_B+T` have individual shortest costs no greater than the respective individual residual budgets. The seven survivors, shown with nonzero excess partitions `a_i=(j_i-1)/2` (remaining quotients have `j=1`), are:

| `n_B=s` | A excess partition (`n_A=64+s`) | B excess partition | A residual mass | B residual mass |
|---:|---|---|---:|---:|
| 5 | () | (14,7,1,1,1) | 192 | 640 |
| 6 | () | (14,7,1,1,1) | 161 | 609 |
| 6 | (1) | (14,7,1,1,1,1) | 97 | 545 |
| 7 | () | (14,7,1,1,1) | 130 | 578 |
| 7 | () | (7,6,4,4,1,1,1) | 130 | 578 |
| 8 | () | (14,7,1,1,1) | 99 | 547 |
| 8 | () | (7,6,4,4,1,1,1) | 99 | 547 |

The exact Python integer checker [T6_P2_V5_SIGNED_POPULATION_GAP64_EXACT_20261123.py](https://github.com/awdawmip/enterprise-math/blob/8ebd45da79a457168746b37b3da824d26b8ec814/research_checks/T6_P2_V5_SIGNED_POPULATION_GAP64_EXACT_20261123.py) enumerates all 382,145 pairs, recomputes the full 2,048-signature group, independently derives the minimum mass table, asserts each stage count, and outputs these seven cases. The same computation was executed locally using exact Python integer arithmetic; no floating-point tests or heuristic pruning are involved.

These **seven are candidates surviving necessary congruences**, not examples satisfying the original rational moment equations. In particular, no T6 global lower bound or general equality of all exact-v₂=5 denominator multisets is claimed. A discriminating next step is a complete v₂=3 mixed-moment sieve for the seven named candidates, or an independent odd-prime obstruction.

## Evidence and acceptance

Own mathematical contribution: `EM-DVR-DEBB5E`, preserving original p19, p17, and earlier v₂ cancellation authors. This work provides two precise analytic lemmas plus one finite exact necessary-condition classification. Scientific GitHub preservation/readback is separate from Native Source/Activity linkage, formal Review, Result and mother-objective closure. No new task ownership or formal authority is inferred from the calculations.
