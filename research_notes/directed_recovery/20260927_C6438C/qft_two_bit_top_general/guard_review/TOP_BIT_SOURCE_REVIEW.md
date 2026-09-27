# Shared-context source-only review

Status: no substantive source defect found. Checker and execution-design review
remain pending; this note is not clearance to run an incomplete experiment.
No scientific module was imported or executed, and no numerical example was
generated. The review is within shared context, not independent admission.

The complete reviewed `top_bit_general.py` has SHA-256
`33a46d5f3dacf61e83cedd75cb3424f2375485b3b58984429d5c9fc76b8c96d0`.
It is compared against the frozen `TOP_BIT_GENERAL_MODULUS.md` at
`880fb9d90f9258e0b96f6f47281bd711b11bd2ec515bddb6a6212cf45266ee89`
and its review at
`e5f31e9619a3233c65af23b642d262e98996d6ca9ee538910e38c21ba412aaab`.

`_coefficients` (line 73) constructs both sets of five primitive coefficients
using the typed runner. Its ten derived coefficients, in order
`n,d,q,dq,q2,delta1,ddelta1,delta2,ddelta2,delta3`, are exactly

```text
3a0, 3a1, 6b0, 6b1, 12c,
-6a0+3b0-c, -6a1+3b1, -6b0+6c, -6b1, -8c.
```

These reproduce the already reviewed integer `3A` formula. No individual
fraction from the difference-power identity is incorrectly required to divide
exactly. `_segment` (line 108) forms the two offset tables and five required
deltas, with weighted displacement factors `b*moment + R*jmoment`. It multiplies
the matching coefficients and makes one final exact division by three. Degree
three suffices; only the frozen table interface is used.

`_orientation` (line 145) counts the whole interval below L and low interval
below H=L/2 independently. Since 0<H<L, the latter count cannot exceed the former;
the typed high-count difference is nevertheless required nonnegative. This
implements the proof's minimum without an ordinary arithmetic `min`. The high
head `b+R*low_n` is paid typed work. When a segment count is zero its head may be
outside that segment's interval, but no moment table is evaluated there; a typed
zero is recorded. Both outer heads are computed before their orientation calls.
At r=0 the negative head is R, and coincident half-modulus heads retain their
separate multiplicities. The final raw normalization stays 4^-g.

`two_negative` (line 171) explicitly admits only the top selected bit k=g-1,
strict integer inputs and stride one, with arbitrary positive supplied R. No
V-divides-R test is retained accidentally. Bit indices route public structure;
scales, coefficients, lengths, remainders, moments and values use the actual
typed runner. The code does not invoke a prior whole-query answer, comparator
or an ordinary numeric reference. The eight-table bound counts top-level calls,
not recursive arithmetic or storage.

The first entry rejects any prior inflight request. Full export also rejects
incomplete work. Orientations and segments are attached before their calls,
so completed partial semantic records are more directly retained, alongside
the raw typed/signed work. Some coefficient and weighted-sum temporaries remain
local until completion; no claim that every interrupted local is retained
should be made. The returned records, complete export and incomplete snapshots
are detached deep copies.

`verify_top_bit_certificate` (line 226) checks strict schema/source/proof/input
bindings, freshly executes every requested query and compares complete strict
semantics. It excludes only the inherited declared native cache-call delta.
Completed mismatch replays are captured before rejection; a paid exception
has an incomplete capture when requested. This relies on the frozen trusted
synchronous source, not on certificate hashes alone. Constructor/import and
failure-save I/O boundaries must be stated by the eventual checker.

The eventual test must still demonstrate the newly admitted unaligned cases,
both pieces, nonzero stretch remainder, empty segments, half-modulus and r=0
orientations, R>L, JSON round-trip, forged coefficients/counts/tables/quotients,
and retained paid failures without repeating completed evidence unnecessarily.
This source-only review does not claim any of those executions occurred.

Global-Knowledge-Sync: main@9f0e65b / GLOBAL_KNOWLEDGE_V1
