# Demand-driven typed modular columns

Status: **AUTHOR_IMPLEMENTATION_WITH_BOUNDED_ACTUAL_EVIDENCE / SHARED_CONTEXT / NOT_ADMITTED**.
Researcher `EM-DIRECT-C6438C`; activity `RA-CAAAC604CB513AEA8BBC1DFC`.
The parent confirmed the current activity guard, `persistence_allowed = true`
and no synchronization debt before scientific execution. Frozen arithmetic
primitive Source is `0852cad130c1d877174d235687cf60c19f318c58`; no frozen source
file was changed. This is an optimization of the existing computation, not a
change to P000, the retained carrier, sampling law or phase precision.

The previous sparse compiler materializes all N modular columns and the
power-of-two identity tail. The new compiler constructs a complete inverse
witness in polynomial bit work, and computes a column only when its source
label is actually requested. It never tests completeness using `set(table)`
or by implicitly iterating over the carrier. Both preparation powers and
original-CF postprocessing now have lazy entrypoints.

## Public interface

```python
table = lazy_modular_columns(N, b)  # equivalent to LazyModularColumns(N,b)
proof = verify_lazy_permutation(table)
target = table[y]
column = table.column_certificate(y)
inverse = table.inverse()
metrics = table.report_metrics()
receipt = table.export_certificate()

factory = LazyModularFactory()    # reuses tables by (N,b)
powers, tables, origins = lazy_modular_power_chain(N, a, t, factory=factory)
trace = lazy_modular_power_trace(N, a, exponent, factory=factory)
value = lazy_modular_power_brc(N, a, exponent)

from lazy_postprocess import lazy_classical_postprocess
result = lazy_classical_postprocess(N, a, t, k)
from lazy_gcd import typed_gcd, typed_gcd_trace, verify_typed_gcd
g = typed_gcd(left, right)
```

Valid multipliers satisfy `0 <= b < N`, `N >= 2`, and are units modulo N.
The typed inverse constructor rejects a nonunit. `carrier_size` is the exact
integer `2^ceil(log2 N)` even for very large inputs. `__len__` is a convenience
for Python-sized domains; Python itself cannot return a larger-than-Py_ssize_t
length. The streaming integration must use `carrier_size`. `__iter__` raises
an explicit error to prevent accidental full-domain enumeration.

`column_certificate(y)` and `export_certificate()` return copies, so ordinary
inspection cannot mutate the private cached arithmetic result. A newly
requested column is added to the cache once; repeated accesses add no digit
replay. Inverse tables have their own lazy caches. The factory stores only
multipliers actually requested by the caller, without an all-N multiplier
inventory or an inferred order.

`verify_lazy_permutation` replays the typed inverse proof, checks source,
carrier and inverse bindings, and returns a complete-permutation certificate.
It does not request every column. `verify_column_certificate` independently
reconstructs the requested column and rejects a changed target or trace.

## Arithmetic source and exactness

The native catalog is the eight full-adder input columns returned by the
actual positive 12-state BRC kernel through
`stage78.shor_benchmark.full_adder_columns`. Its complete source/kernel receipt
is retained. The new module reuses the previously executed and frozen
`add_unsigned`, shift-add multiplication, unsigned comparison and binary long
division. Every reused digit column, input code, sum bit and carry remains in
the returned traces. No Python modular product or `pow` supplies a dynamic
target column.

For a full-adder digit, the actual catalog obeys
`x + y + carry_in = sum_bit + 2*carry_out`. Induction on the bit position gives
the declared exact unsigned sum and final carry. The frozen comparison uses
two's-complement wiring and two such additions; it retains the low difference
and sign/borrow decision. Shift-add multiplication maintains the sum of the
selected, wired shifts of the left operand. Binary long division maintains

    processed_prefix = quotient * modulus + remainder,
    0 <= remainder < modulus.

On each incoming bit, the wired value is below `2*modulus`; one typed compare
and, if needed, its retained difference give the next remainder and quotient
bit. These invariants prove that each newly computed `table[y]`, for `y < N`,
equals the intended product residue. Host bit wiring and control indices do
not constitute another propagator; the arithmetic values are obtained from
the catalog compositions. For `y >= N`, the declared extension is identity,
exactly as in the frozen modular compiler.

## A complete permutation without enumerating its columns

The constructor runs residue-coefficient extended Euclid. Initialize

    r0=N, r1=b, c0=0, c1=1.

Every step computes, through the typed integer operations,

    r0 = quotient*r1 + next_r,
    product_mod = quotient*c1 (mod N),
    next_c = c0-product_mod (mod N).

The modular coefficient subtraction first compares the two residues. If the
difference would be negative, it adds N through the typed adder before taking
the nonnegative difference. Thus each coefficient remains in `[0,N)`, and
the invariant is

    r_i == c_i*b (mod N).

The Euclidean remainder strictly decreases until zero. A final gcd different
from one is rejected. When it equals one, the surviving coefficient c is a
candidate inverse; an additional typed multiplication and division checks
`b*c (mod N) = 1`. This explicit witness alone, together with the exact typed
column rule, proves every unrequested column is covered by the following
argument.

For every `0 <= y < N`, applying the b-map and then the c-map returns y,
because the composed residue is `(c*b)*y == y (mod N)` and both outputs are
the unique representatives in `[0,N)`. The reverse composition holds too.
For every `N <= y < carrier_size`, both maps are identity. Therefore the
whole work-register map is bijective and its inverse is the same lazy
constructor with multiplier c. This argument has no exceptional unqueried
label and requires no observed order or hidden factor.

Embedding each column as one positive unit BRC edge yields exactly the
permutation matrix of the old compiler. Serial composition follows the same
edge order; a classical control takes the direct sum of identity and this
permutation. Extending it by identity on all signed fibre coordinates,
residual modes and spectator labels transports each entire row intact.
Bijectivity prevents two distinct work labels from being silently overwritten
at one destination. The sparse transport helper additionally checks for such
a collision. The proof covers arbitrary signed rows, not only positive or
initially occupied columns.

## Cost with n = ceil(log2 N)

One requested non-tail column multiplies two at-most-n-bit integers and
reduces their at-most-2n-bit product. The shift-add stage uses at most `2n^2`
adder-digit replays. The long-division stage has at most `2n` bit steps, each
with two additions of width at most `n+2`, using at most `4n^2+8n` more digit
replays. Hence one new modular column costs at most

    6n^2 + 8n

digit replays in this conservative accounting. An identity-tail column uses
no arithmetic digits. A cache hit uses no new digit replay.

Euclid has O(n) remainder steps. Each coefficient product/reduction and each
Euclidean division costs O(n^2) digits, giving O(n^3) setup work per distinct
multiplier and the same polynomial cost for replaying its proof. This is
explicitly separate from the per-column bound. The forward and inverse
constructors each perform their own setup, rather than claiming a free
inverse. Holding one setup trace costs polynomial space; the additional
column cache and its digit traces grow only with the q requested columns,
at O(q*n^2) digit records. They do not grow with unrequested work labels.

A square-and-multiply exponent of bit length L uses at most `2L` requested
columns and at most L distinct multiplier setups. The conservative total is
O(L*n^3) digits, with O(L*n^2) column work included. Shared multipliers and
already requested columns may reduce this count. A power chain of length t
has the analogous O(t*n^3) bound. This implementation does not yet propagate
inverse witnesses by squaring to eliminate repeated Euclid setups.

The complete simulation can still request exponentially many different work
labels. The optimization removes unconditional all-N precompilation; it does
not prove that the wavefunction support or total factoring runtime is
polynomial in n. If every label is eventually requested, the cache may still
cover the entire carrier. Full proof/trace serialization also has real time
and memory cost and is not represented by a count of kernel invocations.

## Original CF postprocessing is also lazy

`lazy_postprocess.py` preserves the frozen continued-fraction candidate order,
cap `N-1`, odd-returning-exponent rejection, half-power check and actual
gcd decisions. The gcd values now come from typed long division rather than
the frozen dense Euclidean graph. Its plain result has exactly the original fields and reasons;
it does not claim a candidate is the minimal order. `k = 0` still returns
`ZERO_PHASE_RETRY` before constructing any table.

The modular powers share one lazy factory within a postprocessing call. The
optional `lazy_classical_postprocess_trace` retains exponent-bit routing,
requested columns and gcd call receipts separately from the unchanged result.
The result-only interface avoids copying the full table history after every
candidate. The only source of product residues remains the lazy typed column
API. It does not call the eager compiler at the end of an otherwise lazy
sampling run.

There are O(t) inherited CF candidates for a t-bit readout, each below N, so
their exponent lengths are at most n. Sharing the successive powers of a
limits distinct setup tables to at most n. A conservative digit bound for the
modular part is O(n^4 + t*n^3), including the additional half powers. The old
CF integer-label arithmetic remains a distinct inherited `divmod` recurrence.
It is classical candidate routing, not a claim of full-adder execution for
that recurrence. Each new gcd costs O(n^3) digit replays conservatively;
there are at most O(t) candidate gcd pairs. Thus including gcd leaves the
same O(n^4 + t*n^3) typed-arithmetic bound. No all-N modular table or dense
Euclidean state matrix is hidden in the new route.

`lazy_gcd.py` applies the actual typed long-division transducer repeatedly to
the absolute input magnitudes. Input absolute value is a sign/label convention;
no host remainder supplies a Euclidean successor. Each step certifies
`a = quotient*b + remainder` and `0 <= remainder < b`. The standard identity
`gcd(a,b) = gcd(b,remainder)` and strict descent prove that the last nonzero
label is the gcd; the zero-input conventions include `gcd(0,0)=0`.
`typed_gcd_trace` retains every division operation and `verify_typed_gcd`
reconstructs the entire trace with source binding. The frozen `gcd_brc`
appears only in the regression checker as an isolated prior-actual reference.

## Resource counters and actual evidence

Counters deliberately distinguish:

- Native kernel invocations, counted from the actual `CALLS` receipt list.
  The full-adder catalog is reusable, so this count can remain zero inside a
  later table's operations without making those operations free.
- Digit replays, counted from every retained full-adder cell in each typed
  operation. Setup and requested-column work are reported separately.
- Host bit wiring within those arithmetic routines: 10 shifts/masks/ORs per
  adder digit, three complement-wiring operations per comparison, three bit
  operations per shift-add iteration and six per division iteration. Selected
  `bit_length` calls are separately counted. These counters exclude metadata,
  input-validation guards, loop/index control, hashing, allocation, trace
  export and Python's internal integer implementation. They are not a total
  CPU-instruction count or wall-clock benchmark.

The formal bounded checks compare 318 complete columns across 11 small cases
with the old actual sparse compiler. Every forward/inverse round trip agrees.
The N5 case additionally checks the full eight-column dense embedding with
the actual BRC kernel. Five modular-power results and a six-step square chain
match the old actual execution. Entire signed rows survive forward and
inverse transport. Six rejection controls cover implicit full iteration,
nonunit input, out-of-range labels, Python's large-length boundary, a changed
column target and an altered inverse witness.

Two much larger carriers were checked without full-domain enumeration:

| Width | Carrier size | Explicit forward columns | Forward column digit replays | Forward setup digit replays |
| --- | --- | --- | --- | --- |
| 127 | `2^127` | 6 | 98,955 | 99,593 |
| 256 | `2^256` | 7 | 267,810 | 398,867 |

The moduli are `2^127-1` and `2^255+19`, with b2. No primality claim is needed:
both moduli are odd. Each selected target is recovered by its separately
certified lazy inverse; identity-tail behavior and a no-new-digits cache hit
are checked. Both full forward and inverse traces are saved. The complete
modular-check process recorded two actual kernel calls: one catalog creation
and the small dense comparison. The large digit counts above remain visible
instead of being hidden by that catalog reuse.

For postprocessing, all 48 readouts of three small inputs match every original
result field. A guard that rejects any eager-compiler entry still obtains
factors 3 and 7 for `(N,a,t,k)=(21,2,6,11)`, using three lazy tables and seven
requested columns. A zero readout constructs zero tables. Those tests retain
five actual kernel calls, including the frozen reference executions and
catalog creation; new gcd work remains visible as digit replays. They use no
ordinary modular-power reference. The large-input tests are arithmetic and
permutation tests, not claims of full large-input Shor or postprocessing runs.

The separate gcd checker covers 14 pairs, including zero, negative input
magnitudes and non-coprime values. Every gcd agrees with the isolated frozen
actual execution, every typed trace replays, and a modified remainder is
rejected. Initial new-gcd executions use 1,628 adder-digit replays. The check
process records 15 native kernel calls: 14 isolated old-gcd references plus
one catalog creation. Those reference costs are not attributed to the new
typed gcd algorithm.

## Artifacts and reproduction

Run with the pinned local arithmetic source and current Python:

```powershell
& 'D:/kimi-query-bridge/.venv/Scripts/python.exe' -X utf8 -B -S 'D:/em/TEMP/sep26-shor-general/optimization/lazy_modular/check_lazy_modular.py'
& 'D:/kimi-query-bridge/.venv/Scripts/python.exe' -X utf8 -B -S 'D:/em/TEMP/sep26-shor-general/optimization/lazy_modular/check_lazy_postprocess.py'
& 'D:/kimi-query-bridge/.venv/Scripts/python.exe' -X utf8 -B -S 'D:/em/TEMP/sep26-shor-general/optimization/lazy_modular/check_lazy_gcd.py'
```

`LAZY_MODULAR_RESULTS.json.gz` contains the full small/large typed traces,
proofs, transport checks and kernel receipts; the uncompressed payload is
41,998,938 bytes. `LAZY_MODULAR_SUMMARY.json` is the compact resource view.
Postprocessing has corresponding `LAZY_POSTPROCESS_RESULTS.json.gz` and
`LAZY_POSTPROCESS_SUMMARY.json` artifacts.
The gcd checker has `LAZY_GCD_RESULTS.json.gz` and `LAZY_GCD_SUMMARY.json`.

| Binding | SHA-256 |
| --- | --- |
| `lazy_modular.py` | `08df3595a2a56dc2501bb481828093481bf76e4ac53c8b966990d233fefac1e4` |
| `lazy_postprocess.py` | `c353b8dc429e3d60c8afd9685da4cf1624dbf36785d85eee4a12f636eea0af56` |
| `lazy_gcd.py` | `b704590f055da0785d03b6026d9fa749e75218acd2764d25e90288f32db0965e` |
| Frozen sparse arithmetic | `fd9cbb019418a3c00890ba6e8cca5760e7e4d792bfd7b48306a71a66de301c46` |
| Frozen integer prechecks | `0a817aa8124cceb5440233d543073dae71de6ac1d0d4e5d50f4ee2b4808d99eb` |
| Modular-check uncompressed payload | `12e0c2056f1a9bc9a05260198ce12a54380ce75e211869d925fa8db2974501a2` |
| Postprocess-check uncompressed payload | `6f9100171c382d6c4b2e689701bfe4a754cf9a0dbce8629da64dcfc2d23dfa97` |
| Gcd-check uncompressed payload | `ff9de791411b607fbf85f5d5223856dd522264574b8d311c442be2602903bc18` |

The same-context audit of the lazy modular core reported no substantive arithmetic defect;
the parent owns integration and publication. The evidence is author execution
with shared review, not independent mathematical admission.

Global-Knowledge-Sync: main@61e00d2 / GLOBAL_KNOWLEDGE_V1
