# An actual bounded implicit-Gram prototype: exact, but more costly here

Status: AUTHOR_IMPLEMENTATION_AND_BOUNDED_EXECUTION / SHARED_CONTEXT /
NOT_ADMITTED. Researcher EM-DIRECT-C6438C;
activity RA-CAAAC604CB513AEA8BBC1DFC. The symbolic analysis file is frozen;
this separately sourced prototype implements its correlation recurrence.

## Result

`gram_sampler.py` computes the two conditional masses and continues a declared
history without constructing a work-amplitude dictionary. It memoizes actual
correlation matrices under `(depth, observed modular residue)` instead.
For six declared t4 cases using the already certified new direct words,
every conditional mass and selected mass agreed exactly with the actual
selected-child simulator. All entries of the zero-shift correlation matrix
also agreed at each of the 24 selected prefixes.

The resource result is negative at these small inputs: the correlation cache
stores more scalar slots than the selected explicit state. A small expression
DAG is therefore not presented as a demonstrated quantity compression. The
new observation is that this exact implicit representation can be executed
and its query growth and costs can now be measured separately.

## Exact representation and execution route

For raw, unnormalized amplitude rows v_w, the stored object denotes

    Gamma_i(z) = sum_w v_w v_(z*w mod N)^T,

including their amplitude-denominator squares. Here z is a residue reached
through actually certified modular multiplication, not an supplied order.
Its integer matrix and positive dyadic denominator are retained explicitly.
Initially Gamma_0(1)=e0 e0^T; other shifts give zero. These basis values are
structural 0/1 entries.

At level i, let b be the actually observed modular multiplier and T the
ordered native feedback of that measured prefix. For sign sigma, the update
implemented is

    Gamma_(i+1)(z) = 1/4 [Gamma_i(z)
       + sigma Gamma_i(z/b) T^T
       + sigma T Gamma_i(z*b)
       + T Gamma_i(z) T^T].

The two shifted residues are requested from the lazy typed multiplier and
its certified typed inverse. No complete modular table, hidden period,
factor, host `pow`, or ideal phase matrix is used. Each native left action
is the same fully admitted word's `apply_numer` on matrix columns. A right
T^T action is obtained by transposing, applying that same ordered T, and
transposing back. This preserves factor order; no commuting-phase assumption
is introduced.

Common denominators are aligned by exact bit shifts. Multi-term signed entry
sums and traces are evaluated by the frozen `PositivePathObserver`, with
actual positive graph edges, sign endpoints and kernel receipts retained.
A zero sum with no contributing paths is zero wiring; a single term is
forwarded, not misreported as a new core call. The 1/4 denominator change
comes from the actual two-H4 branch binding admitted by the program. Host
`Fraction` represents exact observations and comparisons, not a substituted
target-state propagator.

`trace Gamma_i(1)` is the parent mass, and
`trace(T Gamma_i(b))` is its signed collision term. The next raw masses are
their half-sum and half-difference. They retain zero outcomes and the raw
parent denominator. Conditional probabilities divide by a strictly positive
parent mass; no amplitude is divided by a square root.

## API and limits

```python
gram = GramSampler(admitted_lazy_program, query_budget=1000)
plan = gram.probabilities()  # parent/child masses and probabilities
gram.advance(bit)           # one declared positive-mass bit
metrics = gram.report()
evidence = gram.evidence()
```

The supplied program has already admitted complete native words, the native
two-H4 identity, optional exact carrier codec, and lazy typed permutations.
The Gram object never calls its `initial()` or `branches()` methods and never
holds labelled amplitude rows. The selected explicit simulator appears only
in the external checker as a same-native-word comparator.

History is append-only, making existing `(depth,residue)` cache entries valid.
Cache entries include full integer matrices, not only norm scalars or a DAG
node count. Query-budget exhaustion raises `QueryBudgetExhausted` and leaves
completed queries in that live object. Increasing its budget can continue.
This prototype has no durable cross-process Gram cursor or random-draw/CF
wrapper; the tests use specified possible histories, not random samples.
An interrupted query is not a successful completed factorization.

## Bounded actual evidence

The checker imports the pinned direct-word bank from payload
`79491e65feec104f2cdc9de510263efef749d8a1174f9cab4c20146a0171615c` and
forces the existing full certificate verifier. Its t4 error bound is 1/2;
these are representation comparisons, not default-width success-budget runs.

For each selected prefix it compares both raw child masses, both conditional
probabilities and the selected mass to `SelectedStreamingProgram`. It also
uses actual signed positive-path quadratic observations of the explicit
state to reconstruct every entry of Gamma_i(1), checking the complete matrix.
No ideal reference distribution is generated.

| N | Declared history | D | Distinct Gram queries | Cached matrix scalar slots | Peak explicit selected-state slots | Lazy adder-digit replays |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| 15 | 0000 | 6 | 16 | 576 | 24 | 1947 |
| 15 | 0011 | 6 | 16 | 576 | 24 | 1947 |
| 21 | 0000 | 6 | 22 | 792 | 36 | 4321 |
| 21 | 1010 | 6 | 22 | 792 | 36 | 4321 |
| 21 | 1111 | 6 | 22 | 792 | 36 | 4321 |
| 21 | 1010 | 61 | 22 | 81862 | 366 | 4321 |

Histories are written in the actual low-to-high readout order. Scalar-slot
counts measure the stated matrix cache and peak selected amplitude state,
not whole-process bytes: native banks, inverse certificates, observer traces,
plans and other caches are additional objects. The cached inverse tables
are included in the Gram modular-work report rather than silently excluded.
Computed modular-column counts are 18 for the N15 cases and 27 for N21.

For nonzero histories the actual native vector-application counts also grow:
N21/1010 uses 144 at D6 and 1464 at D61; N21/1111 uses 192 at D6. The detailed
report retains denominator/numerator bit sizes, per-table setup and column
digit work, and query keys. Counts of reused full-adder digits are separate
from calls to the BRC core.

The final run contains **756 actual BRC core calls**, including source/word
admission, Gram observers and the checker's explicit-state Gram observations.
It passes a zero-query-budget stop followed by continuation in the same
object, plus three invalid bit/query rejection controls. No durable cursor
claim is inferred from that live-object check.

Local timings in the saved summary are slower for Gram in every case. They
are not a calibrated speed benchmark: native admission and full matrix
comparisons are excluded, caches are warm, the checker separately requests
probabilities before `advance()` requests them again, and the Gram prototype
performs extra explicit positive-path observer work. The structural scalar
and query counts above already establish the narrower negative result.

## Scope and relationship to parallel work

The existing parallel research line has already implemented demand-driven
permutations and collision scheduling, and Stage95 certifies collision-free
remaining suffixes while retaining a full state recipe. This work does not
claim project-wide priority for lazy columns or selected-child materialization.
The distinct experiment here is the implicit matrix-correlation recursion on
the independently constructed, certified native word family, with optional
exact reachable-carrier encoding. The parent records the authoritative
cross-line Source and continuation alignment.

The query set can still grow toward the orbit scale. No uniform polynomial
bound on its size has been proved. Further work would need a certified query
equivalence/closure or another exact compact representation; simply storing
the recursion as a DAG does not discharge that obligation. The full-rank
correlation cache also pays D squared, making the exact six-coordinate codec
particularly relevant, while remaining a constant internal saving.

## Reproduction and bindings

The saved evidence can be read without repeating the scientific run. The
bounded checker is `check_gram_sampler.py`; the full result is
`GRAM_SAMPLER_RESULTS.json.gz` and its compact view is
`GRAM_SAMPLER_SUMMARY.json`. The checker requires dependency file hashes to
remain unchanged across the run.

| Binding | SHA256 |
| --- | --- |
| Gram implementation | `468de944518fbc6afa81a17555676436376da63921a784c810ffe8fab3ca17e9` |
| Final checker | `7972b5863f674ae808c74322c3abd8cef8c156521918183e868b4965bf1d68be` |
| Lazy streaming dependency | `635d0c4aee0aaa8d58bb0244835e08e5caa0f6a94926a5213519f40db992a257` |
| Lazy modular dependency | `08df3595a2a56dc2501bb481828093481bf76e4ac53c8b966990d233fefac1e4` |
| Carrier codec dependency | `c25149e0ab4ce92a59d2ca40cb697fe6505cd1dc8d406e9c5a2d92cb2b28c953` |
| Final uncompressed payload | `3221898729a535c3688a6845fbb6a98f0e4e9adb440f393122edc0d6757979bf` |
| Final gzip bytes | `b4e1f925d77df542639c2f1504b851717db57b25f3cc5f9f9734f35e6bd88d6c` |

The first successful execution is retained under `prior_source_guard/`;
the later run adds the dependency-stability guard and is the final binding
above. Nothing in this prototype changes the frozen compiler, ideal target,
primitive precision or P000. It remains shared author evidence, not independent
mathematical admission or efficient classical Shor factorization.

Global-Knowledge-Sync: main@61e00d2a2a3ab41f3ec43990385f46e8a7806d41 / GLOBAL_KNOWLEDGE_V1
