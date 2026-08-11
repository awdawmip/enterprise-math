# Run-Length Normal Form for Infinite Prefix-Observable Word Semantics

Status: `RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID: `R-8F3K`

Full prefix-observable OR semantics is infinite over unbounded word length, even though terminal effects form a finite monoid. Infinite semantic cardinality, however, does not imply that an operation requires an arbitrarily long **structural** description.

The cumulative OR trace changes at most k times. This yields an exact run-length normal form with at most k phases and a closed composition law.

## 1. Phase normal form

For a nonempty word, record

`((g_1,r_1),...,(g_s,r_s))`.

Here:

- `g_1,...,g_s` are the distinct generators in first-appearance order;
- `r_i>=1` is the number of consecutive prefix positions for which the cumulative mask remains at the level reached after introducing `g_i`;
- `sum r_i=H`;
- `s<=k`.

Example:

`a a b a c c`

has phase form

`((a,2),(b,2),(c,2))`.

The stutter `a` after b changes no cumulative mask and is absorbed into b's phase duration.

## 2. Exact decoding

Start from mask0. For each phase `(g_i,r_i)`:

1. OR in generator bit `g_i`;
2. emit the resulting mask `r_i` times.

This reconstructs the complete H-step prefix trace exactly.

Therefore the phase form is sufficient for full prefix-state observation.

## 3. Canonical representative word

A canonical literal representative is obtained by repeating each newly introduced generator for its phase duration:

`g_1^r1 g_2^r2 ... g_s^rs`.

It has the same prefix trace as the original word and normalizes back to the same phase form.

Thus arbitrary semantically invisible stutter choices are removed.

## 4. Closed exact composition

Let left form L have a set of already-seen generators. Scan right phases in first-appearance order.

- If right generator g is already seen on the left, its whole run creates no new cumulative mask; add its duration to the current final left/output phase.
- If g is new, append `(g,r)` and mark g seen.

The resulting form equals normalization of literal word concatenation.

The branch exhaustively checks this composition law on bounded word pairs.

The empty form is identity, so the phase forms constitute an exact formulaic operation monoid for prefix semantics.

## 5. One-generator specialization

For k=1 every nonempty word has form

`((a,H))`.

Composition adds durations:

`H_total=H_left+H_right`.

Hence the infinite prefix-word semantics reduces to nonnegative duration addition, despite having only one nonidentity terminal transformation.

This is the smallest possible witness that infinite semantic cardinality can still have a finite-dimensional formulaic presentation.

## 6. Exact class count from the normal form

Fix exact word length H and phase count s.

Choose the ordered distinct generator identities in

`P(k,s)=k!/(k-s)!`

ways.

Choose the positive duration composition

`r_1+...+r_s=H`

in

`C(H-1,s-1)`

ways.

Therefore

`N_s(k,H)=P(k,s) C(H-1,s-1)`.

Summing over `s=1..min(k,H)` reproduces the parent exact prefix-trace count.

The executable layer checks the count phase-by-phase against exhaustive literal-word normalization.

## 7. Polynomial semantic growth for fixed k

For H>=k:

`N_prefix(k,H)=sum_(s=1)^k P(k,s) C(H-1,s-1)`.

This is a polynomial in H of degree `k-1`.

The top term comes from s=k:

`k! C(H-1,k-1)`.

Its leading coefficient is

`k!/(k-1)! = k`.

Thus for fixed k:

`N_prefix(k,H) = Theta(H^(k-1))`,

with leading asymptotic `k H^(k-1)`.

The branch mechanically verifies that the `(k-1)`-th forward difference is constantly `k!` after H>=k.

## 8. Three growth regimes

For fixed k and increasing exact word length H:

### Literal syntax

`N_literal=k^H`.

Exponential in H.

### Full prefix semantics

`N_prefix=Theta(H^(k-1))`.

Polynomial in H.

### Terminal transformation semantics

Once H>=k:

`N_terminal=2^k-1`.

Constant in H.

So semantic quotienting removes exponential syntax redundancy, while prefix timing prevents the complete saturation enjoyed by terminal effects.

## 9. Simple RLE storage upper bound

For one concrete s-phase form of total length H, a simple fixed-width encoding can use:

- `ceil(log2 k)` bits per generator ID;
- `ceil(log2(H+1))` bits per run length.

Hence

`B_RLE <= s [ceil(log2 k)+ceil(log2(H+1))]`,

with `s<=k`.

For fixed k this is `O(k log H)` bits.

Materializing every prefix mask directly uses

`kH`

bits.

Thus compact operation state and fully materialized observable history have very different storage scaling.

## 10. Information lower bound

For fixed phase count s there are exactly

`P(k,s) C(H-1,s-1)`

forms.

Any injective binary code therefore needs at least

`ceil(log2[P(k,s) C(H-1,s-1)])`

bits in the worst case for that phase stratum.

One can approach this by ranking:

- the ordered distinct generator tuple;
- the `s-1` positive-composition cut positions among H-1 slots.

The simple field encoding is not claimed bit-optimal; it is a transparent constructive upper bound.

## 11. Sharp k=5,H=100 storage illustration

Full materialized prefix trace:

`5*100=500` bits.

Worst-case simple five-phase RLE:

- generator ID width3;
- run-length width7;
- total `5*(3+7)=50` bits.

So even this simple representation gives a tenfold storage reduction while remaining exactly decodable.

At H=1,000,000 the materialized trace uses five million bits, while the same simple five-phase representation remains only O(log H) per duration field.

## 12. Composition cost is horizon-independent at the structural level

Each normal form has at most k phases. Composing two forms scans at most k right phases and produces at most k phases.

Therefore high-level structural composition work is O(k), independent of the two literal word lengths.

Run-length integer additions contribute bit cost logarithmic in the accumulated horizon.

This is another instance where a long future history has a compact exact compositional summary.

## 13. Decoding cost cannot disappear if the full history is requested

The compressed form can be composed without expanding the H-step trace.

But if the consumer asks to **observe all H prefixes**, those H outputs must eventually be materialized/streamed. The prefix-scan generation studies that execution cost separately.

Therefore:

`compact semantic state`

does not imply

`zero-cost full observable history`.

The two interfaces must remain distinct.

## 14. Relationship to P024

P024's guarded `(T,H)` profile showed that an infinite operation language can have a finite-parameter exact normal form with closed composition.

The current prefix-run form gives a second independent example:

- parameter dimension is bounded by generator count k;
- unbounded word horizon lives in integer duration fields;
- literal syntax can grow without bound while exact operation state remains finitely parameterized.

This supports a broader Stage131 principle: **finite operation cardinality is not required for compact exact law presentation.**

## 15. Stage131 consequence

The semantic-resource hierarchy now distinguishes:

- literal word length;
- number of semantic classes;
- parameter dimension of an exact normal form;
- bit size of normal-form parameters;
- cost to compose normal forms;
- cost to materialize declared outputs.

None of these is determined by the others alone.

## Owner-local assets

- `src/enterprise_math/prefix_run_length_normal_form.py`;
- `src/enterprise_math/prefix_run_length_resources.py`;
- corresponding tests;
- this bilingual theorem note.

## Prior art / status

Run-length encoding, positive compositions, ordered first-appearance forms and idempotent semigroup reductions are standard prior mathematics/CS. P023/A2 retains future-signature/precision ownership. This Draft owns only the exact finite-parameter prefix-word representation specialization.

No repository strict CI, `EXECUTABLE_CHECKED`, or canonical claim. `CI_NOT_REQUIRED_FOR_RESEARCH`. Hard block: `NONE`.
