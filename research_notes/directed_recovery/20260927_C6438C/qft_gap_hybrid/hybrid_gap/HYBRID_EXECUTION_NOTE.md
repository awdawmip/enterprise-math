# Structural hybrid: one actual bounded execution

The sole declared run passed all 31 frozen signed answers across nine tuples.
It used 20 endpoint requests, ten direct interior requests and one interior
divisibility-zero request. The actual production cost was 36,970 full-adder
digit replays: 3,790 endpoint, 32,987 direct and **193 routing**. This includes
the new dispatch arithmetic; it is not a sum of favorable old branch costs.
The same declared answers previously cost 88,185 in the pure-direct run and
68,824 in the separate endpoint/one-window dispatcher. These are bounded
recorded arithmetic counts, not a matched wall-clock speed comparison.

The root executed the checker once after its actual new startup guard passed.
The run began at 2026-09-27T06:22:54.884563+00:00 and finished before final
serialization at 2026-09-27T06:23:02.240669+00:00. The recorded whole-checker
duration is 7.356159900082275 seconds; it includes historical evidence I/O,
production, fresh positive replay and negatives. It is not a sampler trajectory
time or a directly comparable timing ratio against earlier experiments.

## Results and paid routing

| g,k,R | Routing digits | Endpoint digits | Direct digits | Total hybrid digits | Historical pure-direct digits |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1,0,3 | 0 | 298 | 0 | 298 | 1,953 |
| 2,0,3 | 0 | 496 | 0 | 496 | 5,319 |
| 2,1,3 | 0 | 421 | 0 | 421 | 3,113 |
| 3,0,6 | 0 | 1,002 | 0 | 1,002 | 12,833 |
| 3,1,3 | 42 | 0 | 9,757 | 9,799 | 9,757 |
| 3,2,2 | 0 | 374 | 0 | 374 | 5,466 |
| 4,1,7 | 126 | 0 | 23,230 | 23,356 | 23,230 |
| 4,2,1 | 25 | 0 | 0 | 25 | 10,974 |
| 5,4,3 | 0 | 1,199 | 0 | 1,199 | 15,540 |

The two nonzero interior routes therefore cost more than their pure-direct
components alone: 9,799 rather than 9,757, and 23,356 rather than 23,230.
This overhead is retained. The endpoint-first ordering avoids all routing
arithmetic for endpoint inputs, including g=1,k=0 where the inherited highest-bit
priority applies. The new zero route is exercised at g=4,k=2,R=1 and costs 25
digits, including typed U construction, typed U/R and typed U-U. Its zero
answer is certified by the unchanged signed-residue cancellation proof.

Each tuple has one fresh hybrid object and one fresh verification object, each
containing three disjoint runners. A tuple's certificate follows a single route;
a sequence mixing endpoint/direct/zero queries in one persistent observer was
**not executed** in this test. In particular the interior zero branch has one
positive R=1 fixture, not a new execution for every nontrivial divisor R of U.
The g=3,k=2,R=2 zero answers use the endpoint route. The general routing proof
and source review must not be confused with these narrower executed fixtures.

## All executed resource categories

| Scope | Typed operations | Digit replays | Recorded host bit wiring | Recorded arithmetic bit-length calls |
| --- | ---: | ---: | ---: | ---: |
| Production | 8,349 | 36,970 | 399,985 | 23,676 |
| Positive fresh replay | 8,349 | 36,970 | 399,985 | 23,676 |
| Failed-certificate fresh replay | 2,775 | 10,595 | 115,181 | 7,787 |
| Total | 19,473 | 84,535 | 915,151 | 55,139 |

The production direct runners store 52 moment nodes from 80 requests, with
28 cache hits and maximum recursive depth three. Routing and endpoint runners
have no moment nodes or window-weight queries in this run. Maximum observed
integer widths are three bits in routing, nine in endpoint, and ten in direct.
These are saved arithmetic metadata, not total Python memory or full host-bit
complexity. Hashing, object allocation, serialization, loops and implementation
internals outside the inherited counters are not magically free or measured by
these totals.

There is one process-global actual primitive kernel observation, retained once
in the complete CALLS stream. Its reusable full-adder columns support all later
typed digit replays. Each of the three runner certificates embeds provenance
for those same columns; those copies are not three new observations. The one
core call is also not the entire cost. Resource aggregation counts each actual
runner once per executed object, not the repeated nested request records or
copies of a certificate inside the payload.

## Verification and negative evidence

All eight invalid input tuples were rejected before arithmetic. All 15
certificate mutations were rejected. Schema, own-source, dependency and boolean
input mutations account for four early rejections. The other eleven preserve
their complete fresh replay evidence. Eight of these replay the small zero
fixture; two replay the endpoint fixture and one replays the g=3,k=1,R=3
direct fixture. Their combined cost is 10,595 digits, including 242 routing,
596 endpoint and 9,757 direct digits.

The negatives cover wrong route, quotient, remainder, U, absent zero proof,
boolean zero output, typed zero subtraction, routing division receipt, nested
endpoint/direct value and nested provenance. Fresh verification reconstructs
all three runner streams in request order and compares the entire certificate
under strict JSON. Only the three explicitly named native cache call-delta
fields are normalized. Boolean and integer values remain distinct. No arithmetic
value, branch, digit cost, nested certificate or source/proof field is excluded.

No unexpected-failure artifact exists. Available-object failure capture is
implemented and source-reviewed; this successful run does not prove recovery
from arbitrary constructor, import or external-process failure. Existing success
or failure artifacts prohibit silently rerunning over them.

## Full saved-record cost readback

`read_hybrid_cost.py` is a standard-library metadata-only reader. It imports no
scientific observer and performs no native arithmetic. It read the entire new
gzip and its complete historical pure-direct comparator, checked original and
decoded hashes, current source/design/dependency pins and the startup receipt,
then checked every positive full-certificate equality and every paid negative
replay against the honest certificate for that tuple.

It also recounted digit cells, recorded bit-wiring steps and arithmetic
bit-length-call categories from the saved trace shapes. Signed-operation
indices cover every typed operation exactly once in order. Nested request
copies point to the matching complete endpoint/direct certificate; routing
operation intervals and the typed division/zero receipts agree. The reader
reconciled every per-case route total, all three cost categories and the one
global core call with the actual summary. It wrote `HYBRID_COST_READBACK.json`.
This is source-specific author readback, not a scientific rerun or independent
formal admission.

Executed source hashes:

* `hybrid_signed_gap.py`: `7daf2e04be83ed9a9124c1a2bcc79ae2cc8feb5334c4b675ed19f7a2bc918fb8`.
* `check_hybrid_signed_gap.py`: `ed54ddc3ffb9735e1610ae363b69cd58d426adb4b9c1d0cc6ba85fcf11de1da7`.

The original gzip is 517,935 bytes, SHA-256
`036242b07b480d05937b6a72ffc375dc33eea48283647964ca020b78bdb3f962`.
Its 10,382,526-byte raw JSON has SHA-256
`76efccc284001219b2ecde3523557f66e55e828125e4132a83814f25df80398b`.
Full stdout is `HYBRID_EXECUTION_LOG.txt`, SHA-256
`a3d4aae2ad68240c1a76116e611046dc7445ad460cc975e763e8298b8c9982d2`.

This version implements only the stride-one single-negative-bit scalar family.
Raw normalization and signed values remain unchanged. It does not implement
aligned progression, two-bit lifting, arbitrary masks, full matrix Gram
integration, order/address discovery, or general Shor dequantization. Its frozen
design's earlier code-only status is historical; this note records the completed
bounded run. Further work requires a separate version and its own evidence.

Global-Knowledge-Sync: main@a3609ca / GLOBAL_KNOWLEDGE_V1
