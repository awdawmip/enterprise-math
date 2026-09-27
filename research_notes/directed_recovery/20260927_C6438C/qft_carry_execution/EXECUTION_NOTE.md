# Exact two-carry execution and its cost boundary

Status: AUTHOR_ACTUAL_TYPED_BOUNDED / SHARED_CONTEXT / NOT_ADMITTED.
All executions use the actual admitted signed native words and typed modular
arithmetic. These checks are not an ideal-QFT experiment or independent
admission. P000 physical axes and the native 61-coordinate carrier are
unchanged. Six coordinates are used only through the previously certified
exact full-word invariant embedding.

## What now runs

`carry_executor.py` implements the two-carry displacement lemma from the
previous symbolic package at EM commit
`469b16d9c7db1993c1d793fb2601fd3b1669a88b`.
For a fixed history h and prefix length i it computes the complete matrix

    C_h(d) = 4^-i sum_(0 <= n,n+d < 2^i) U_h(n) U_h(n+d)^T.

U includes the actual initial basis vector, every chronological phase word,
signed readout arms and residual coordinates. The high and low carry
boundaries are zero. Each layer uses the old signed observer's exact 1/4
factor once. A negative displacement is a transpose; an out-of-range query
is zero. No modular labels are needed to compute one coefficient after
program admission. The implementation retains two carry-indexed boundary
matrices, plus separate terms, native temporaries and observer receipts.

The executor binds the explicit history, admitted full/encoded bank, codec
and actual D61 sparse execution caches. The checker pins source hashes
before and after execution. Arbitrary Python monkeypatch detection is not
claimed. Legacy inherited gamma/mass/probabilities/advance entry points are
disabled, so they cannot silently switch this executor back to the old
memoized recurrence.

`modular_alias/typed_aliases.py` discovers **every** bounded signed displacement
with b^d=z using actual typed arithmetic. It preserves all repeated baby
exponents, uses the certified inverse target for negative displacements,
excludes duplicate zero only in that negative search, and exposes setup,
range checks, inverse validation, output count and full receipts. A found
short period is reported without hiding the cost of the still-complete
alias output. The current consumer validates exact integer displacement
types independently. The replay verifier checks semantic evidence; it does
not claim that Python's numerical equality enforces every output type or
that mutable metrics are independently certified by that comparison.

## Actual bounded results

The root checker completed once successfully in 16.89 seconds on this host,
including admission and all checks, with 8,859 actual core-call receipts.
The timing is an execution fact, not a general performance estimate.

- 134 complete D6 matrices, two declared tapes `(1,0,1,0)` and `(1,1,1,1)`,
  depths 0 through 4, all signed in-range displacements and both overflow
  endpoints, equal the actual unmerged same-word path product sums.
- Two complete D61 matrices, h=(1,0,1), d=1 and 7, equal those path sums
  and the two-sided exact D6 embedding, including the zero complement.
- Ten assembled Gamma matrices for N=21,a=2 and N=65,a=3, depths 3 and 4,
  equal the old native Gram recurrence. All four masses agree; the two
  positive depth-3 prefixes also give the same next-bit conditional masses
  and probabilities. Terminal histories have no next bit.
- A reversed chronological word in the h101,d7 fixture has the same
  diagonal but flips residual entry (0,2). Full-matrix checking detects it.
- Sixteen invalid inputs, changed bindings and forbidden legacy entries
  are rejected. Separate alias checks pass 12 complete cases and 12
  negatives, with 244 core-call receipts. The mixed int/string key collision
  found during review was fixed before the final alias and root runs.

The raw root payload SHA-256 is
`df00de760c8ca3d69b4f1fdd869a9c3e298582c7ae72d4fa4bba24a760b7ed57`;
the gzip SHA-256 is
`25f53b75d91f6601174783f9aaefc4d0f1f69d4ba85f9519ca5786c410e8c89e`.
Every observer operation and native-call receipt is retained in the gzip.
In `gamma_cases`, top-level `history` denotes the declared four-bit tape;
`depth` and the carry/Gram child evidence give the bound `history[:depth]`.

## The tested tradeoff, without a speedup claim

The following counts concern the same target set in each row, plus the
listed mass/next-bit observations. The exact query sets are in the raw
evidence. Program admission and process-wide native caches are shared.
Vector-action counts count calls even when the underlying exact quotient
has cached data; they are not wall-clock ratios.

| N | depth | aliases output | carry digit layers | carry vector actions | old Gram vector actions | old retained matrix slots |
|---|---:|---:|---:|---:|---:|---:|
| 21 | 3 | 10 | 30 | 384 | 120 | 756 |
| 21 | 4 | 10 | 40 | 882 | 168 | 864 |
| 65 | 3 | 6 | 18 | 198 | 72 | 1,224 |
| 65 | 4 | 6 | 24 | 498 | 120 | 1,368 |

The carry boundary holds 72 rational scalar slots in D6 in each row.
That is **not a full-memory peak**: term arrays, returned matrices, native
temporaries, arbitrary-width integers and retained transcripts are excluded.
Observed boundary/sum numerator maxima are 57,101,56,101 bits; denominator
maxima are 61,107,60,106 bits. Transient bit widths are not measured.
Alias discovery additionally replays 3,559; 3,458; 7,880; and 7,255 typed
adder digits respectively, including its recorded verification/setup costs.

Thus one coefficient has a polynomial contraction and small live boundary,
but summing all aliases is slower in native vector actions on these fixtures.
The complete discovery bound still contains B+ceil(2^i/B)+J and arithmetic
bit costs. A polynomial per-coefficient result is not a polynomial Shor
simulator. Whole-period aggregation is the separate next optimization in
`aggregation_theory/`, with exact-order/address discovery charged explicitly.

These source-correspondence checks add no new ideal phase-accuracy bound.
The inherited bank's recorded error certificate remains separate. No
universal joint work-label sampler or factoring advantage is established.

Global-Knowledge-Sync: main@06788df / GLOBAL_KNOWLEDGE_V1
