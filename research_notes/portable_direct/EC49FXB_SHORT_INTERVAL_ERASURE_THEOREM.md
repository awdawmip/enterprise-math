# EC49FXB — Exact first phase-cardinality transitions for one erasure

Date: 2026-11-22 (Asia/Shanghai). Frozen scientific pin: `BRC16943`, retained. Direct predecessor: [EC49FXA](https://github.com/awdawmip/enterprise-math/pull/2968) and its [two-offset exact certificate](EC49FXA_TWO_OFFSET_SHARP_OBSERVER_THEOREM.md). Mathematical status: **AUTHOR_PROVED / EXACT_FINITE_CHECK / PARENT_DEPENDENT / NOT_REVIEWED**.

## Theorem and exact scope

Retain the 110-periodic frozen P10 / one-hole CRT/Farey auxiliary observer, the full separately indexed reflection-defect spectra of both channels and the known reference. A physical activation at site t returns the two separate Boolean readings. Require distance **r=2**, the information-theoretic condition for identifying a two-state spectral fiber after *one known channel-bit erasure*. The relative sensor offset is unknown in the **consecutive set**
`D_k={0,1,...,k-1} subset Z/110`, where **1<=k<=55**; this range is antipodal-free.

Then the exact number of fixed physical activation sites required uniformly over the 50 frozen P10 supports, full or one-hole mod11 factors and all compatible phase pairs is

```
N_fixed(D_k; 2) = 8  for k=1,2
                  9  for k=3,4
                 10  for k=5,...,55.
```

Thus the first loss of two-channel savings relative to a known offset occurs at **three** permitted consecutive phases, and a second loss occurs at **five**. The result is a sharp structural classification, not a solver's cost estimate.

## Lower bounds

In the notation of EC49FXA/FWZ, let `m_i` be the count of installed physical sites with t mod5=i. Each necessary elementary state pair is described by
`F_S(d,i,j)=m_i+m_(d-i)-c_(i,j)-c_(d-i,d-j)`
where deletion occupancies sum to `m_i+m_(d-i)` across 11 columns. For r=2, averaging over the 11 possible missing columns gives the universal requirement

```
m_i + m_(d-i) >= 3
```

for all permitted d and all i in Z/5. Summing for a single d gives 2|S|>=15, hence |S|>=8 for every nonempty phase set.

When `D_k` contains `0,1,2` (k>=3), the three fixed-point reflections `i=d-i mod5` respectively occur at (d,i)=(0,0),(1,3),(2,1), forcing `m_0,m_3,m_1>=2`. For d=1 and i=2, `m_2+m_4>=3`. Therefore |S|>=2+2+2+3=9.

When `D_k` also contains `3,4` (k>=5), the five distinct fixed-point residues, respectively i=0,3,1,4,2 for d=0,1,2,3,4, force *each* m_i>=2, so |S|>=10.

All inequalities are witnessed by actual frozen one-pair U=299 states with arbitrary admissible missing mod11 columns and allowed phase shifts, as established in EC49FWT–FWZ.

## Attaining sets

Physical sites are integers modulo110. For k=1 or 2, the following **8-site** configuration attains sampled distance >=2:
`S8={64,68,69,81,87,90,100,108}`.

For k=3 or 4, this **9-site** configuration attains it:
`S9={60,70,81,88,91,92,93,94,109}`.

For every 5<=k<=55, **10 sites** suffice:
`S10={0,1,2,3,4,5,6,7,8,9}`.
Indeed each mod5 block contains exactly two different mod11 columns, so each channel contributes at least one distinguishing bit for every d,i,j; therefore the total is >=2 even for all 55 allowed offsets.

For the first two finite witnesses, the **minimum across all 11 deleted columns** in each row (columns indexed i=0,...,4) is

```
S8; d=0: 3 2 2 2 2
    d=1: 2 2 2 3 2

S9; d=0: 3 3 2 2 3
    d=1: 3 3 2 3 2
    d=2: 2 3 2 3 3
    d=3: 3 2 2 3 3
```

The small [independent verifier](EC49FXB_SHORT_INTERVAL_ERASURE_VERIFY.js) calculates each `F_S(d,i,j)` by exact integer loops and checks all **84,700** (k,d,i,j) constraints for k=1,...,55. The companion [JSON](EC49FXB_SHORT_INTERVAL_ERASURE_OUTPUT.json) records the witness sets, minimum rows, and 55 optimal values. No numerical optimization package or approximation is needed to validate the witnesses.

## Interpretation and next question

This completes the **single-known-channel-bit erasure** problem for every proper consecutive antipodal-free phase interval. It does not treat two-bit activation erasure as one channel-bit erasure. The endpoints, signed Farey branch, affine seed and source-relational information remain separately typed before any native heartbeat-X6 dynamics use.

Next determine the r=1 noiseless and r=3 one unknown channel-bit-error phase thresholds for `D_k`, and the general r classification. Compare actual same-anchor phase feasibility before making dynamical claims. No formal CLAIM, Result or Review status is asserted.
