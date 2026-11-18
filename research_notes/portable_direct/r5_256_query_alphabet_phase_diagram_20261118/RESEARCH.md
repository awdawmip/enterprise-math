# R5: exact three/four-query alphabet transitions for the full 256-state observer

Date: 2026-11-18 (+08:00). Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

## Frozen experiment and meaning

Retain the **256 distinct named hypotheses** h=0,...,255 and **101** physical query budgets k=214,...,314 from frozen science pin `435e77af0d180eac32bd1f9c4c464bc4010b7551`. The exact scalar centers N_h(k) are in `EXACT_R5_ALL_101_BUDGETS.json`, SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`. Good observations belong to [N_h(k)-eta,N_h(k)+eta] with tau=2 eta>=0. Up to f observations may be arbitrarily corrupted and are unmarked. A **global alphabet** is one fixed set A of physical budgets available anywhere in the adaptive decision tree; repetitions and observation-dependent choices are allowed. The result concerns alphabet cardinality, not minimum cumulative physical budget.

## Theorem: complete phase diagram for every integer f>=0

Put

```
Q = 1744659037213380157479321600000
D = 1882951873548292168718745600000
```

The smallest global alphabet cardinality supporting a finite worst-case, always-correct identification protocol against up to f unmarked arbitrary errors equals

```
3         for 0<=tau<Q,
4         for Q<=tau<D,
infinity  for tau>=D (no finite guarantee even with all 101 budgets).
```

A three-type construction is A3={217,224,298}. A four-type construction is A4={217,218,224,298}. For either, query **each budget exactly 2f+1 times** and decode the unique hypothesis consistent with at most f errors; this is a finite constructive upper bound for every f, not a cost-optimal claim.

### Separation principle

Two candidate hypotheses a,b can share one good response at budget k exactly when |N_a(k)-N_b(k)|<=tau. If every pair is separated by at least one budget in A (strict inequality >tau), the fixed repeated batch described above has at least 2f+1 positions at which the correct-response intervals are disjoint for each pair. A shared transcript cannot have at most f errors for both candidates. Conversely, if some pair has overlapping correct intervals for *every* k in A, an adversary can supply a common error-free readout after every adaptively chosen budget; no protocol using A can guarantee identification.

### Two budgets never suffice

Exact enumeration of all 5050 unordered budget pairs shows that their joint noiseless readout `(N_h(k),N_h(l))` assumes at most **128 distinct values** for the 256 named hypotheses (the bound is attained at {214,294}). So no alphabet with <=2 types identifies all hypotheses even with f=0 and tau=0.

### Three budgets work precisely below Q

Exact integer enumeration of all 32640 unordered hypothesis pairs verifies

`min_{a<b} max_{k in {217,224,298}} |N_a(k)-N_b(k)| = Q.`

Hence A3 separates every pair whenever tau<Q.

At tau=Q, the following **complete separating-budget sets** for three pairs are pairwise disjoint:

| Pair | All k with gap > Q |
|---|---|
| (0,1) | 216..220 |
| (0,64) | 224..290 |
| (16,32) | 298..311 |

A successful alphabet of three types would have to choose exactly one member from each of these sets, hence its unique low budget would belong to {216,217,218,219,220}. However each possible low budget has a pair that is not separated by that budget and is **identical under all 93 budgets 222..314**:

| low k | witness pair | gap at k |
|---|---|---|
| 216 | (11,14) | 92195224223274674159616000000 |
| 217 | (4,10) | **Q** |
| 218 | (9,12) | 763097546646694311430717440000 |
| 219 | (9,12) | 53550705027838197293383680000 |
| 220 | (9,12) | 0 |

Thus every three-type alphabet misses a pair at tau=Q; noise monotonicity extends this exclusion to all larger tau.

### Four budgets work precisely below D

Exact enumeration over all 32640 pairs verifies

`min_{a<b} max_{k in {217,218,224,298}} |N_a(k)-N_b(k)| = D.`

So A4 separates every pair when tau<D. The pair (11,14) also satisfies

`max_{214<=k<=314} |N_11(k)-N_14(k)| = D.`

At tau>=D its correct-response intervals overlap for every available query. Even with all 101 budgets, f=0 and arbitrarily many adaptive repetitions, no scheme can guarantee identification. This completes the full phase diagram.

## Sharp near-Q corollary

At the exact integer threshold tau=Q-1, **all and only** the successful three-budget alphabets are

`{217, m, v}, 224<=m<=290, 298<=v<=311.`

Their number is **67*14=938**. The unique cheapest in sum of *distinct budget labels* is {217,224,298} with sum **739**. To verify completeness: the three forced-band pairs above still apply at Q-1. The extra pairs (9,12), (4,10), (11,14) admit low separating budgets {215,216,217}, {217,218,219}, {217,218} respectively; their intersection forces 217. The 67 middle-budget choices have the same pair-separation support at Q-1; likewise the 14 high-budget choices. Combined with budget 217 they cover every pair.

## Verification, scope, and continuation

The included `VERIFY_R5_QUERY_ALPHABET_PHASES.py` runs with Python standard library on the exact frozen integer table; `RESULTS.json` contains its actual output. All observations, margins, class counts, and separation sets are calculated with unbounded integers. It verifies the 5050 two-type partitions, the 32640 pairwise relations, the forcing witnesses, the near-Q family, and the sharp thresholds. One actual local execution finished with exit code 0 and output `R5_QUERY_ALPHABET_ALL_F`.

The theorem is confined to the frozen **scalar indexed-center observer** and its 101 declared queries. No native X6 path, provenance, signed relation or future-observer equivalence is removed. P000/Heartbeat World and the project's joint-relation preservation requirement remain in force. The prior fifth-chamber adaptive cumulative-cost interval `8335<=C_8^*<=8343` remains unresolved.

**Next discriminating scientific problem:** find the exact full-256 adaptive f=8 **cumulative physical-budget** optimum, using these query-alphabet constraints to prune candidate global supports and testing observation-dependent early stopping against the previously proved fully prepaid batch baseline.

Sources: science pin above; previous R5 exact full-alphabet threshold proof at PR #2427 commit `20c2b210c6d6ea4ed41caf6efd311c4a2c039a0d`, `research_notes/portable_direct/r5_256_identifiability_threshold_20261118/`; project `p000_reality_foundation.json`, `docs/RESEARCH_CONTINUATION_PROTOCOL.md` and `docs/PORTABLE_RESEARCH_PROTOCOL.md`.

Historical contribution provenance: `EM-DIRECT-AEEFF0`, `RA-B1A5102AD1877F18B4C40118`. This author-side GitHub publication does not claim a new native CLAIM, Review, or Activity write.
