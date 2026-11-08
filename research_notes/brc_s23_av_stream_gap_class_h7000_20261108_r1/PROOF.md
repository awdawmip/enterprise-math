# S23/AV: streaming exact gap-class certificate at H=7000

Date: 2026-11-08 (Asia/Shanghai). Status: **author-side finite proof/certificate, pending independent mathematical review**.

Frozen scientific input: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Predecessor: `research_notes/brc_s23_av_gap_class_h5000_20261108_r1/PROOF.md` at commit `83ec2f3dd0dfc5e24aa89578a927612b5a7c270c`.

## Theorem and scope

For the iid two-point S23/AV experiment with laws on labels (1,3,4)
`P0=(1/2,1/4,1/4)`, `P1=(5/7,1/4,1/28)`, define
`T_h={10^i/7^s : 0<=i<=s<=h}` and let `N(h)` be the minimum common prefix length `n` whose attainable likelihood-ratio values occupy every open cell determined by `T_h` (label 3 permits padding). The new endpoint certificate proves

```
N(7000) <= 2455069.
```

Using the earlier exact lower bound `N(510)=2455069` plus the threshold nesting `T_510 subset T_h subset T_7000`, it follows that

```
N(h)=2455069 for every integer h with 510<=h<=7000.
```

This adds 2,000 horizons over H=5000 and 4,000 over H=3000. The mathematical result is scoped to the two-point auxiliary sign observer.

## Complete finite endpoint proof

Put `r=log(7)/log(10/7)`, `t(v,j)=r*v-j` for nonnegative `v,j` with `v+j<=H`, and `E(k,l)=k-r*l`. Each attainable prefix ratio corresponds to `(k,l)`; label 3 pads a prefix to length n. Unique factorization proves `r` irrational, so all `(H+1)(H+2)/2` threshold coordinates are distinct.

The code computes the rigorous rational interval
```
lo/Q < r < hi/Q, Q=10^26
lo=545569623581288298975349314
hi=545569623581288298975349315.
```
It uses 45-term rational atanh expansions for ln(2), ln(8/7), ln(5/4) and strictly positive explicit tail bounds.

**O(H) heap; O(H+C_H) total memory exact ordering.** For fixed `v`, the points `t(v,j)` increase as `j=H-v,H-v-1,...,0`. Initialize one row-head for each `v=0,...,H`, keyed by the exact integer `lo*v-Q*j`. On each pop, advance only that row, increasing its integer key by exactly `Q`. Heap merging emits every triangular lattice pair precisely once, with `O(H)` live heap entries, `O(H^2 log H)` ordering time. Let `C_H` be the number of realized adjacent gap classes; accumulating their summaries uses an additional `O(C_H)` memory. The exact H=7000 run has `C_H=33`. A uniform upper bound on `C_H` is a separate open mathematical question. Every consecutive output pair is checked by the adverse-endpoint strict integer inequality `(lo if dv>=0 else hi)*dv > Q*dj`, establishing the actual increasing order, not merely an approximate sort. A wrong approximate ordering must fail this check. At H=7000, all 24,510,501 coordinates are covered, forming 24,510,500 adjacent bounded cells.

**Uniform displacement-class lift.** For each actual adjacent class with displacement `(dv,dj)`, accumulate `V=max v_left`, `J=max j_left`, `S=min(v_left+j_left)`. A pair of integers `(K,L)` satisfying
```
K>=J, L>=V, K+L<=2455069+S,
0<K-r*L<r*dv-dj
```
gives, for every cell in that class, a valid witness
```
(k,l)=(K-j_left, L-v_left).
```
The open-cell inequalities and witness length follow by direct substitution. The code certifies the irrational inequalities by their adverse rational endpoints:
```
K*Q > hi*L,
(K+dj)*Q < lo*(L+dv).
```
It constructs and checks a witness for each of the **33** realized classes. For the dominant `(79,431)` class, use `(K,L)=(2074774,380295)`, giving a maximum prefix length of 2,455,069; all other classes use a checked short witness. The exterior cells have explicit valid witnesses `(k,l)=(0,1284)` and `(38190,0)`.

Hence every open threshold cell has an attainable prefix of length at most 2,455,069, proving the endpoint upper bound. The lower bound and monotonicity cited above finish the interval theorem.

## Actual verification and provenance

Reproducible executable source: `VERIFY_STREAM.py`. Executed locally under CPython with `python s23_h10000_gapclass.py 7000` (same source text, locally named `s23_h10000_gapclass.py`). The run's exact transcript is `RUN_EVIDENCE.txt`, including **all 33 class witnesses**, count totals, boundaries and digest.

Independent regression at H=5000 gave the **identical prior** 29-class certificate digest `9d51dbf18b2e242f7fc20d6d1514f1265f2399bb69502922b27fb3defc3c0e29`, confirming the streaming reimplementation against the prior in-memory sort result.

H=7000 reports 33 classes, all covered, and class table SHA-256 `2aef3d6d6f687ae0ebed385e34653a822139f49c881d2a0dfaf7ce325643242d`. Executed local source SHA-256: `eb004919adc10975403ddadc2d3f900074b2f4f5fc454607cb259202187317c2`. Real output SHA-256: `9d40c02809cabf3686bb0b191a72da35ee186654e82f4605616b781e0e9ac4cd`.

The method reuses the exact likelihood observer and class-lift lemma from the predecessor; the new engineering contribution is the streaming exact ordering with `O(H+C_H)` memory rather than storing `O(H^2)` threshold coordinates. BRC information retained: joint label-1/label-4 counts, unit-ratio label-3 padding, and future horizon. This is not an X6/native-geometric transfer.

## Smallest next mathematical step

Derive adjacent gap classes *without* enumerating all `O(H^2)` points (Farey / continued-fraction / three-distance structure adapted to the triangular lattice), then obtain a parameterized H range for which all class lifts stay below the sharp n bound. Locate the first H at which N(h)>2455069. Keep the full-parameter delta_4 minimax and six-source/ten-label mother-model map as separate parent objectives.

Control provenance: Native MCP status/session/owner calls returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH`, `STATUS_DATABASE_UNAVAILABLE`, `operation_sent=false` on 2026-11-08. This note is a published author-side frontier, not an authenticated claim, accepted result or independent review.
