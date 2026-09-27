# Structural two-bit shortcuts: executed result

Status: **PASS**, the coordinator's single declared run. The unchanged six
tuples produced all 36 values equal to the immutable aligned predecessor.
The complete old payload and source pins were read; its 720-pair comparator,
old production and old fresh replays were not executed again.

Production adder-digit work fell from **77,763 to 37,503**, a **51.77% reduction**
on this fixed grid. Every tuple improved against the predecessor. Four of six
also cost less than the saved typed comparator, but the total **37,503 remains
above 35,531** for that comparator. These are recorded operation counts, not a
wall-clock speed claim or a general complexity result.

## Per-tuple evidence

Every residue r=0,...,R-1 was retained. The original raw scale remains 4^-g.

| (g,ell,k,R) | New production digits | Old aligned digits | Old typed comparator digits |
|---|---:|---:|---:|
| (2,0,1,1) | 16 | 4,664 | 387 |
| (3,0,1,3) | 11,894 | 16,088 | 2,268 |
| (3,1,2,2) | 78 | 6,800 | 2,186 |
| (3,1,2,4) | 204 | 7,273 | 2,530 |
| (4,1,3,6) | 8,065 | 18,074 | 12,547 |
| (4,2,3,20) | 17,246 | 24,864 | 15,613 |
| Total | 37,503 | 77,763 | 35,531 |

The g=3,ell=0,k=1,R=3 moment fallback and g=4,ell=2,k=3,R=20 affine case
remain more expensive than the saved comparator. No result was selected using
the cheaper historical answer. The dispatcher used only certified divisibility,
public bit indices and observed zero coefficients.

The executed routes were seven residue-histogram cancellations, 26 highest-bit
affine requests and three direct-moment fallbacks. There were 158 actual private
progression calls: 146 affine calls (including 61 empty calls) and 12 moment
calls. Thirty-eight shifted progressions were omitted for observed coefficient
zero. Their receipts explicitly say they were not evaluated and contain no
fabricated computed value, count or operation interval. The 12 moment calls
made 24 top-level table calls, with 23 retained recursive nodes, 39 moment
requests and 16 cache hits. These different counts must not be conflated.

Readback confirms aligned admission precedes cancellation, cancellation uses
the original U=2^k, and nonaligned attempts stop before the zero test. Required
affine lengths and q selections have typed signed/division receipts, as do both
exact halves in T(n), T(q). Shifted progressions have their own lengths; removed
M endpoints are explicit empty sums. Empty orientations, affine junctions,
q=0 and q=n, nonzero shifted coefficients, negative output, r=0 and coincident
half-modulus multiplicities occur in the declared grid. The surviving even-step
propagation branch after a failed zero test is not re-exercised here; the even
fixture is cancelled earlier, as declared in DESIGN.

## Current computation, including all validation work

| Category | Streams | Adder digits | Typed operations | Signed operations | Host wiring | Host bit-length calls |
|---|---:|---:|---:|---:|---:|---:|
| Production | 6 | 37,503 | 8,313 | 8,068 | 403,647 | 22,433 |
| Positive fresh replay | 6 | 37,503 | 8,313 | 8,068 | 403,647 | 22,433 |
| Paid input rejection | 2 | 43 | 5 | 5 | 475 | 18 |
| Negative fresh replay | 12 | 111,661 | 24,829 | 24,094 | 1,201,534 | 66,910 |

All **26 current streams** together contain **186,710 adder-digit replays**.
There is one global native call, `recurrent_mass_power`, 12 states, depth one,
in the first production interval. Subsequent operations replay the actual
full-adder columns. One primitive construction call is not a measure of total
arithmetic work. All retained cells were matched to those columns, and signed
outputs were linked to their typed operation outputs before recounting costs.
Native intervals are disjoint and cover the entire saved CALLS list once.

Host counts cover the arithmetic layer's bit wiring and bit-length calls, not
Python indexing, allocation, hashing or serialization. Maxima are not summed.
The production trace's observed maximum recursion depth was three and its
observed integer width seven bits; these are bounded observed counters.

The recorded interval was **28.76671770005487 seconds before success
serialization**. It includes reading the old 61.9 MB payload and a larger
negative-control set than the predecessor. Neither this elapsed value nor the
different validation totals establish an overall wall-clock improvement.
Historical comparator work is excluded from the new cost ledger.

## Fresh replay and rejection detail

Six positive fresh replays equal complete production certificates, excluding
only the declared native primitive cache-call delta. Sixteen certificate
tamper controls all reject: eleven retain complete honest replays, one retains
paid incomplete work, and four reject before arithmetic.

| Tamper | Retained honest replay digits |
|---|---:|
| Zero divisibility reason | 16 |
| Zero-route output | 16 |
| Drop half-modulus orientation | 8,065 |
| Omitted shifted coefficient | 11,894 |
| Affine canonical length | 17,246 |
| Affine typed minimum | 8,065 |
| Affine exact half | 17,246 |
| Shifted zero tail | 17,246 |
| Original branch sign | 8,065 |
| Fallback table offset | 11,894 |
| Signed output | 11,894 |
| Input changed to nonalignment, incomplete | 14 |
| Source, schema, bool input, non-string key | 0, four early rejections |

Every complete captured negative replay matches its original honest certificate.
The partial replay retains the actual alignment division with nonzero remainder
and no zero test. The attempted certificates preserve key types in a dedicated
encoding, including the non-string-key attempt.

Twelve input controls comprise ten strict-input pre-rejections and two paid
nonaligned rejections. Both paid failures are followed by a valid-input reuse
attempt; each rejects with unchanged inflight record, trace and counters. This
prevents overwriting failed work and does not claim resumable computation.
No unexpected-failure artifact exists. Existing result, summary or failure
artifacts would prevent a new run; no scientific rerun was performed for this
readback. Import failures and failure-save I/O remain outside the stated
main-run recovery promise.

## Evidence binding and author readback

- Executed `shortcut_two_bit.py`: `874d5d79f67ef5a00176b48faa2959811b925820031a90f71f80b6ba6fd5a34b`.
- Executed `check_shortcut_two_bit.py`: `e7dca9fe712c367ed5434ed88ac2027178bbf05fff1fb94373d77c8c01d39e22`.
- Frozen `DESIGN.md`: `b41ebf07ab34b9fa6981f529a5d230952b050786dd97f64eb1886827b1b3d667`.
- Startup guard: `d002bf88886316a60af33391ebaf0ef54325c0dc5f9787fb88a96c08022fb297`.
- Complete raw JSON: 57,941,257 bytes, `55f0652225cffe7a658f5528e30ebf8c90342b9422def6799285d32a7dc66be7`.
- `SHORTCUT_RESULTS.json.gz`: 2,027,431 bytes, `07ff488f357a2d80a682508f28b7f242a4cdd92c2cc15cfd54b95e884104e53a`.
- Summary: `b1c2f21969b217aff301c76e161f2b72a4b65551bd239ecab1dd9e9f4a52b970`.
- Execution log: `8c9d949168784df70b56132a0c6fe57583933250990b390dde0b84de87adf7bc`.
- `read_shortcut_cost.py`: `42897a3d63c26a1583320b4c3838ec63f6c67ccf27cb5e0c939e5560135d8b79`.
- `SHORTCUT_COST_READBACK.json`: `ea957f0c76adad4abfc32da8270d1b1fb5dcfcd483c404447e8d7be0f7322c0b`.

The standalone reader imports only standard-library I/O facilities. It reads
all new and historical raw bytes, checks source/proof/guard/native pins, follows
all new outer routing and progression operation references, verifies exact
saved replay equality, checks signed-to-typed output links and every saved
native adder cell, and recounts structural links and costs. It consumes saved
results rather than recomputing an ordinary scientific reference or rerunning
typed moments. This is author evidence under shared context, not formal
independent admission.

The result remains a bounded scalar improvement with supplied modulus R.
It supplies neither unknown-order discovery nor general unaligned mixed-floor
compression, growing-mask compression, chronological matrix aggregation, or
full Shor sampling.

Global-Knowledge-Sync: main@604893e / GLOBAL_KNOWLEDGE_V1
