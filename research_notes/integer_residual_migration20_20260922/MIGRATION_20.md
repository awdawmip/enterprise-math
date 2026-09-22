# Migration 20 — shared browser uint32 carrier and Phase32 adapter

Status: validated numerical-layer candidate; original Phase32 UI is not migrated.
Remote baseline: `af159e2a4f7876fea4a565c06c5f7a4d79d8b57d` (M19).
Researcher: EM-DIRECT-4A5102 / TASK_RESEARCH.

## Recovery and scope

The interrupted preceding turn had already published M19's Phase32 report reader
and appended its activity checkpoint. Recovery consumed that frontier instead of
rebuilding the reader. The global summary was still at M18; immutable M19 source,
not the stale summary, determined this continuation.

The only production file changed in M20 is `certified_hex_browser.py`. Its old
browser carrier was fixed at 65536. The existing Python carrier already supported
explicit powers of two through 2**32. This slice extends the shared BigInt browser
implementation to the same domain, preserving its existing default APIs and
65536 output shapes. It is not another scalar family or a second quantizer.

## Exact carrier, sources and caches

`phaseBounds(tick, bits, modulus)` and `locate/population` with `phaseModulus`
accept exact power-of-two moduli from 4 through 2**32. The default is 65536.
Cardinal phase thresholds and half-angle depth derive from the actual modulus.
The rotation cache includes precision and phase depth; the phase cache includes
tick, precision and modulus. This prevents different meanings of the same tick
from sharing a cached interval after the newly supported carrier is selected.

Modulus and mathematical shifts use BigInt. Maximum unsigned tick 4294967295 and
the 2**31 sign boundary are tested without Number bitwise truncation. Bounded
array indices/counters and explicitly validated safe integer inputs can still be
JavaScript Numbers; this is not a claim that the whole JavaScript VM uses BigInt.
No approximate pixels, floating roots or trigonometric calls choose cells.

Source records persist the modulus. `verifyCellRecord` replays the recorded
modulus, exact source and precision schedule rather than implicitly assuming the
old carrier. Async population computation snapshots the source before yielding;
mutating the caller's phase array or carrier option does not change that source.
Cancellation rejects the calculation rather than returning partial success.

## Existing Phase32 semantics preserved

`populationPhase32` reuses `population` and the existing exact lexicographic tie
adapter. It retains the complete base q/r/s-priority certificate separately from
Phase32's declared nearest-A2-then-axial-lexicographic choice. It uses inverse pitch
as the certifier scale: pitch 50/100 means scale 100/50, without reduction.

Positive occupancy and collision metrics exclude zero as in the existing Python
Phase32 caller. The zero identity and its unphased certificate remain present.
Unknown cells have null complete totals, explicit unresolved identities and
occupancy bounds. Neither cancellation nor precision exhaustion invokes floats.

`parsePitch` preserves the original integer/fraction/decimal text and unreduced
ratio. `0.50` remains 50/100; `2/2` remains 2/2. It does not infer a fraction from a
Number. The old `parseScale` range and output shape are preserved. Parser domain
is the positive exact source; the eventual browser layout bounds are a separate
caller decision, not silently imposed here.

```javascript
// phi starts with null for zero; remaining entries are exact uint32 phase ticks.
const pitch = NollmCertifiedHex.parsePitch('0.50');
const population = await NollmCertifiedHex.populationPhase32(
  phi, pitch.numerator, pitch.denominator,
  {initialBits: 64, maxBits: 192, includeCertificates: true}
);
```

## Executed validation

The final gate ran 229 tests: 227 passed, zero failures/errors, two retained
missing-template skips. All 20 new tests passed. The retained 209 tests are the
unchanged M18 dependency suite, not M19's independent reader tests. The two skips
are only original deterministic Phase32 HTML/site tests because that unchanged
production template is not in this dependency slice. No numerical test skips.
An initial combined tool invocation timed out; the final grouped runner and its
clean replay both completed and generated matching result records.

New tests include frozen M19 default-record compatibility, all 31 supported
power-of-two carriers, interleaved cache keys, maximum ticks, full certificates,
modulus tampering, both local/base tie selections, exact parser parity, zero and
unresolved semantics, async mutation/cancellation and disabled floating Math.
The existing Python exact-policy targets pass; this is not a whole-JavaScript
policy checker or a whole-module float-free display claim.

Ten finite Phase32 populations matched Python: nine 4096-identity cases across
three source modes and three pitches, plus 65536 golden/pitch-one. Comparison
covers the complete population summary, complete point certificates and all
ordered cell records. The large case has 47497 occupied positive cells, 18038
collision excess and zero unresolved identities. The phase schedule is generated
by the unchanged Python caller and supplied to Node; this does not validate an
original browser phase-generator/UI port or prove universal termination.

A separate Chromium run passed nine arithmetic checks, including 48 complete
certificate comparisons and 20 phase-bound comparisons. It executes the actual
M20 shared script using set_content/add_script_tag, with no digest adapter.
It does NOT test native file/HTTP navigation, browser-native WebCrypto population
hashing, the original Phase32 UI, saved-file reopen or Safari/iOS.

Clean patch replay passed the same 229-test gate and nine Chromium checks.
Seven implementation/fixture files, tests.json and browser.json are byte-identical.
The ten population benchmarks were not repeated in that clean replay.
Patch SHA256: `cfac9095a543a24504384dca707eeb0d0c6cd28449a3a13cd2fad7708c6e10ff`.

## Reproduce and remaining work

```bash
python tools/run_migration20.py
python tools/test_migration20_browser.py
python tools/benchmark_migration20.py --mode golden
python tools/benchmark_migration20.py --mode hash
python tools/benchmark_migration20.py --mode spiral
python tools/benchmark_migration20.py --count 65536 --mode golden --pitches 1
```

Tests require the inherited Node runtime and mpmath; Chromium checks additionally
require Playwright and /usr/bin/chromium. Production math executes existing BRC
and its BigInt port, not mpmath. The delivery carries the M18 numerical dependency
slice plus the exact M19 shared browser baseline; it is NOT the full M19 checkout.
Do not copy its isolated src/enterprise_math/__init__.py into production. Apply
migration20.patch to the pinned M19 source for integration.

Next: wire the actual original Phase32 HTML caller to this adapter, retaining
literal pitch, asynchronous states, saved budgets, cancellation and source-bound
exports. Recover and test the real template rather than substituting a fixture.
M19 reader integration regression, M15 full-root-package acceptance, original UI,
independent review, default switch and main-code integration remain separate.
Geometry is still a declared A2 observer, not native X6 or mathematical admission.
