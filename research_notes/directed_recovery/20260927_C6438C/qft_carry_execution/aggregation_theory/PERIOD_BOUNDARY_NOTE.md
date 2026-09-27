# Separate boundary execution for the unchanged period aggregator

Status: AUTHOR_ACTUAL_NATIVE_BOUNDED / SHARED_CONTEXT / NOT_ADMITTED.
This is a distinct checker/evidence unit. It does not replace, overwrite or
rerun the original eight-case artifact. The aggregator source remains
`6f2c855bec09f7cf7fc4853b55ea41f94a195ba3d3b783d18921e9a3b6465f0c`.

The checker first obtained actual typed first-return certificates, with
finite limit N, and only then chose canonical addresses from those observed
cycles. It did not insert expected orders or use ordinary modular pow.
Every result was compared entry-by-entry, including the dyadic denominator,
with the parent's same-native-word coefficient sum using an independently
discovered complete typed alias list. All nine comparisons passed.

| Input and depth | Actual R | s,q | Addresses checked | Branch |
| --- | ---: | --- | --- | --- |
| N=17,a=4,depth=3,h=001 | 2 | 1,1 | 0,1 | q=1 with two high bits |
| N=17,a=3,depth=3,h=101 | 8 | 3,1 | 0,1,7 | s=i, no high block |
| N=97,a=5,depth=2,h=10 | 24 | 3,3 | 0,1,12,23 | s>i |

For the last input, the complete alias lists are respectively {0}, {1},
the empty set, and {-1}. Thus both the positive and negative unique-
displacement branches and the structural zero branch actually executed.
All five declared branch-coverage flags are true.

The first input's two matrices are nonzero although no phase feedback is
active in its retained history. Its absence of residual entries is reported,
not interpreted as residual truncation. The second input has nonzero
residual matrix entries in all three queries. The last input uses only the
earlier exact phase and has no residual entries at that depth. All cases
still use the same full61 admission and exact six-carrier codec.

The run retained 377 native kernel CALLS and took about 3.50 seconds on
this host. Its raw payload is 6,925,770 bytes and gzip 260,098 bytes. The
separate metadata accounting counts 85,419 typed adder-digit replays,
including 12 fresh cycle-table instances (3 initial discoveries and 9
query replays) and 158 actual cycle-column requests. Equal input/table
parameters are not collapsed across separately executed instances.

Actual phase-vector applications were 0/144/72 for aggregation and
0/168/72 for the corresponding coefficient sums. Signed observer counts
were 8/24/3 versus 62/33/3. The single-alias mass query in the s=i fixture
used eight aggregation kernel calls versus seven for its coefficient sum;
the extra work is retained, so no blanket per-query speedup is claimed.
The s>i branch delegates its nonempty cases to the inherited coefficient
executor and provides no claimed arithmetic improvement there.

The q=1 fixture has four chronological high bit layers across its two
queries and two low layers: here qH=4. The s=i fixture has no high layers
and nine low layers. The s>i fixture performs no aggregation high/low
layers and reports four delegated-or-zero large-two-part queries. Matrix
boundary-slot counters exclude fresh terms, native temporaries, certificate
storage and receipts; they are not total memory measurements.

Frozen evidence:

- `check_period_boundaries.py`:
  `c3a65bad94eb481a5bb9f51d2b81854db76443ef3a1a4456a757f0b0004ec6c6`.
- `PERIOD_BOUNDARY_RESULTS.json.gz`, decompressed payload:
  `e1e94d19eb7f1155e63222710f97359be93389e88eb9bac73e1a9a154a51b35a`.
- `PERIOD_BOUNDARY_SUMMARY.json` contains the actual orders, all targets,
  alias lists, residual/zero flags, complete branch flags and cost counters.
- `summarize_period_boundaries.py` only counts that frozen evidence into
  `PERIOD_BOUNDARY_ACCOUNTING.json`; it does not execute scientific arithmetic.

This completes the requested bounded branch check. It does not implement
small-odd-part discovery, a persistent aggregation cursor, multi-query cache
reuse, a new whole-Shor sampling driver or a general complexity improvement.
No further scientific test was run after these declared cases.

Global-Knowledge-Sync: main@06788df0 / GLOBAL_KNOWLEDGE_V1
