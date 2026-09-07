# Independent audit: eight-positive weighted raw-three-marginal trades

Status: **PASS_WITH_STATED_SCOPE / INDEPENDENT_DERIVATION_CHECK**.
Role: `ANCHOR_EXPOSED` internal owner helper; this is not an allocated
Researcher-ID, registered claim, official review, or Foundation promotion.
The author note, author checker, production modules, and path-monitor
directory were not modified by this audit.

**Conclusion.** The supplied proof is valid for a finite rational signed
array on one common raw signed X6 chart with all 20 three-axis marginals
zero and exactly eight distinct positive spatial cells. It forces exactly
eight negative spatial cells, one common nonzero absolute coefficient,
and the two parity classes of a four-bit cube embedded through actual axis
level dictionaries. No gap or counterexample was found. In particular,
the proof does not assume the negative support bound it is meant to prove.

## Audited bytes and evidence independence

SHA256 values of the read-only author inputs:

| File | SHA256 |
|---|---|
| `OWNER_WEIGHTED_TRADE_FRONTIER_20260907.md` | `520a41ee878aeb1d1c546a7c088ae1c86f0acbe8292d7356d00436322b6f20be` |
| `owner_weighted_trade_20260907_check.py` | `7df5c60cdc365bb27d84ad3f8e2597db5259b3c10670cdaee677cc1489cb5de4` |

The independent checker is
`owner_weighted_trade_independent_audit_20260907.py`, SHA256
`a3ff5ff994c5815078a75fb9fe298bacb5582443a7b78725675b493664c6fc73`.
Its actual output is
`owner_weighted_trade_independent_audit_20260907.json`.
It imports only the Python standard library: it does not import or execute
the author checker, project observers, a BRC implementation, or an optimizer.
It hashes all three code/note inputs before and after execution and checks
that the bytes are unchanged. Reading the author checker establishes what
its finite tests cover; its output is not used as mathematical authority.

The derivation below reuses the already established support-slicing bound:
a nonzero signed array with all marginals through order k zero has at least
2^k positive and 2^k negative locations. It does not reopen that theorem or
the completed seven/eight-support recovery result. The new audit target is
the equality classification with only the positive support count prescribed.

## Proof reconstruction and critical checks

Let P and N be the positive and negative spatial supports after collecting
all coefficients at identical raw cells. Finite support makes every lower
marginal a sum of three-axis marginal fibers, so all orders 0, 1, and 2 also
vanish. Each fiber therefore has equal total mass from the two nonnegative
sides. If it has no positive support, it cannot have negative support.
This is the point where positivity is essential; signed cancellation within
one side is not allowed.

**Single- and double-slice counts.** A nonzero slice fixing one axis has all
two-axis marginals on the other axes zero. It has at least four positive
locations. Thus no physical axis has more than two levels anywhere in P or
N; a varying axis has four positive locations at each level. A level used
only by N is excluded by its one-axis fiber, rather than silently dropped.
A nonzero slice fixing two axes has all one-axis marginals on the remaining
axes zero and has at least two positive locations. These statements concern
counts, even when the coefficients differ.

Consequently, two varying bit-labeled axes have positive count table

`[[a, 4-a], [4-a, a]]`, with `a in {0, 2, 4}`.

The values 1 and 3 each create a nonzero pair slice with only one positive
location and are impossible. Values 0 and 4 identify complements or
duplicates on P. Their forbidden pair patterns force the same relation on
N. Constants are likewise inherited by N. Taking one representative per
varying column class modulo complement loses no spatial distinction:
every original coordinate on both sides is determined by these bits and
its fixed level dictionary. Every pair of distinct representatives has
each of its four patterns exactly twice.

**Existence of an all-once triple.** For three such representatives, the
pair-count equations give `n_abc = 1 + alpha (-1)^(a+b+c)`. One can derive
this directly by fixing `n_000`: each pair sum is 2, successively determining
the other seven entries. Integrality and nonnegativity force
`alpha in {-1,0,1}`. Thus the triple is either all eight patterns once or
one parity class twice. If no triple were all-once, fix two representatives
A and B. Every other representative C would obey `C=A+B+constant` on P.
Then all physical columns would be functions of just A and B, yielding at
most four distinct positive cells. Fewer than three representatives already
has this same cardinality obstruction. Eight distinct positives therefore
force an all-once triple of three actual physical axes.

**Balanced extra columns really are affine.** Use that actual triple to
label the eight rows by `u in F2^3`. For another representative z, its four
one-rows have exactly two ones in each basis coordinate, by pair balance.
Their XOR is therefore zero. Four distinct vectors with XOR zero form an
affine plane: after choosing one as origin, two of the nonzero differences
are independent and the third is their sum. Hence the indicator of those
four rows is a nonconstant affine character. Exchanging z's two level names
removes its constant term. Characters of one basis bit were already removed
as duplicate/complement classes, so the only possibilities are the three
pair sums and the triple sum. This classification uses the eight-row size;
it is not an unsupported assertion that arbitrary balanced Boolean
functions are affine.

**The negative-support gate uses actual raw triples.** Negative points
already obey the constant, duplicate, complement, and allowed-level
constraints. Let v denote the three basis bits of one proposed negative
point. If a pair-sum representative z12 is present, the actual raw triple
`(u1,u2,z12)` has positive support only on `z12=u1+u2`. The negative point
must obey this same equation. All present pair-sum representatives are
forced in this way. If the triple-sum representative q is also present,
the actual triple `(z12,u3,q)` forces `q=z12+u3`; these are three distinct
physical representative axes. Thus any pair-sum present forces all remaining
bits of the negative point to coincide with the unique positive row with
basis label v. This contradicts disjoint collected supports. With no extra
representative, the three basis bits already give that contradiction.

The only nonempty negative-support possibility is therefore exactly four
representative types: the three basis bits and their triple sum. P is one
four-bit parity class. Restoring physical duplicates/complements and
constants embeds the full four-bit cube injectively, because every one of
the four types has an actual physical representative. N can use only the
other eight cube points. The existing support lower bound says `|N|>=8`,
so all eight are present. This argument excludes nine or more negative
locations before any amplitude assumption.

**Amplitude equality follows from actual cube edges.** Project onto any
three of the four representative physical axes. Each resulting fiber on
the sixteen-point support consists of exactly one even and one odd cube
vertex. Extra physical axes do not add points to that fiber: they are fixed
functions of the representative bits and the embedding is injective.
The zero marginal equates the two absolute coefficients. Taking the four
possible omitted representatives covers every edge of the connected
four-cube and forces one common amplitude lambda. This proves the amplitude
step without relying on the separately stated minimum-total-support lemma.

## Six-axis coverage and independent finite checks

There can be at most six representative classes because there are only six
physical axes. Once the three actual basis axes are chosen, at most three
of the four extra character types fit. The author's 15 subsets are exactly
`sum(C(4,k), k=0..3)=15`. Omitting the set of all four extras is correct:
it would require seven distinct physical axes. Constants and repeated types
consume physical axes and do not create additional representative classes.
The proof itself does not need an unmentioned seventh axis or a new native
dimension. This audit makes no theorem claim outside the stated X6 setting.

The independent code enumerates binary column families directly, without
starting from the author's four-character list. Choose two distinct
representatives and order the eight rows so each of their four patterns
occurs twice. Normalize every other column to have first-row value zero,
using its freely reversible level labels. There are nine possible additional
columns balanced against those first two. Enumerating pairwise balanced
subsets, with at most six total representative axes, covers every admissible
positive count structure up to row order, axis order, and level complements.
It is not an enumeration of weighted arrays or a count of isomorphism
classes; equivalent structures may appear more than once.

| Representative axes r | Eight distinct positive rows | No negative point allowed by raw projection join | Eight negative points allowed |
|---|---:|---:|---:|
| 3 | 8 | 8 | 0 |
| 4 | 20 | 16 | 4 |
| 5 | 20 | 20 | 0 |
| 6 | 10 | 10 | 0 |
| Total | 58 | 54 | 4 |

For all 58 families the checker explicitly finds an all-once actual triple
and verifies the affine character conclusion. It then pads to six physical
coordinates and computes the allowed support join using the **twenty raw
three-axis projection tables**, not a Fourier or character surrogate.
Only the four indicated four-representative cases have any negative cells
available. For each one, direct signed raw fiber sums vanish for unit parity
coefficients, and the raw incidence matrix on the sixteen available cells
has rank 15 over Q. Its one-dimensional kernel independently rules out
unequal amplitudes on that support.

Further checks independently establish:

- The allowed pair count parameter is exactly `{0,2,4}`. All eight
  coordinate-balanced four-subsets of the three-cube become subgroups after
  translation; this checks the affine-plane step by closure under XOR.
- All 3,360 assignments of six physical axes to four represented bit types
  or a constant give zero in every raw three-axis fiber for the parity array.
  Bit complements and arbitrary distinct integer level dictionaries preserve
  this identity by bijective relabeling of each raw axis. They do not assert
  a native coordinate rotation or a geometric symmetry.
- A separate embedding with signed, nonadjacent coordinate levels and a
  repeated/complemented axis passes the same direct raw test and has rank 15.
  Its amplitude is `5/13`; increasing one positive coefficient by `1/13`
  produces twenty nonzero raw fibers, so the unchanged observer detects the
  deliberately malformed amplitude assignment.
- Deleting one positive cell from that exact parity trade gives stacked raw
  defect `100/13` and ratio `3/4`, computed from the literal twenty tables.

Actual command from `D:\em\owner-20260907`:

```text
python -X utf8 research_notes/owner_weighted_trade_independent_audit_20260907.py
exit_code: 0
status: PASS
elapsed_seconds: 1.314
distinct_column_families: 58
all_six_axis_type_assignments: 3360
signed_level_embedding_raw_kernel_rank: 15
single_amplitude_tamper_nonzero_raw_fibers: 20
deleted_positive_raw_defect: 100/13
deleted_ratio: 3/4
```

The elapsed value records this run and is not a complexity or performance
guarantee. These finite checks corroborate the proof; the proof is what
handles arbitrary rational weights and arbitrary allowed integer labels.

## Findings, authority boundary, and remaining open question

No proof correction is required for the audited bytes. The distinction
between eight positive *locations* and integer trade volume is handled
correctly: clearing denominators need not produce volume eight, so a
minimum-volume classification alone would not establish the theorem.
The author's own checker appropriately calls its work finite regression,
rather than a weighted-support search or a substitute for the derivation.

The deleted-point implication is exact. The classified trade has total
positive mass `W=8 lambda`, each removable positive weight is `w=lambda`,
and hence `w/W=1/8>2/21`. After deletion its L1 norm is `15 lambda` while
its twenty-table defect is `20 lambda`, giving `3/4`. This closes the stated
light-cell deletion route through an eight-positive zero-marginal trade.
It does not classify all arrays with at most seven positives or determine
their optimal stability constant. The wider interval cited in the author
note was not independently re-proved in this bounded audit.

Counts are collected spatial supports, not BRC branch identities; the signed
array is an algebraic difference of two nonnegative populations. The claim
requires all twenty **raw** three-axis marginals in one common chart.
It does not cover independently rebased/min-zero tables, projected mass-only
substitutions for exact weight histograms, incomplete collections of raw
tables, or signed physical branch primitives. P000 foundations are unchanged.

Global-Knowledge-Sync: main@4fa7d7d / GLOBAL_KNOWLEDGE_V1
