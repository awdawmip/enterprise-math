# QFT/Shor correlation optimization: exact carry execution

The single-displacement two-carry contraction is now implemented and tested
against complete actual native matrices. Complete typed modular alias
discovery reconstructs the old Gamma observables. A whole-period aggregator
also runs and reduces repeated displacement work on its matched fixtures.
General efficient QFT/Shor dequantization remains open.

Read [EXECUTION_NOTE.md](EXECUTION_NOTE.md) for the executed carry/alias
results and measured tradeoff. The root checker passed 134 D6 coefficients,
two full D61 matrices, ten assembled Gamma matrices and sixteen rejection
controls, retaining 8,859 actual core-call receipts. The separate complete
alias checker passed twelve cases and twelve negatives, retaining 244
receipts. The actual noncommuting order control is detected by a residual
matrix entry even though its diagonal agrees under the wrong order.

Read [PERIOD_AGGREGATION.md](aggregation_theory/PERIOD_AGGREGATION.md) for
the symbolic whole-period lemma and its limited rank obstruction, then
[PERIOD_EXECUTION_NOTE.md](aggregation_theory/PERIOD_EXECUTION_NOTE.md) for
the separate implemented tests. The first eight whole-period matrices
match complete alias sums, with 2,568 raw core-call receipts. In those
equal-target comparisons, aggregation uses 672 versus 1,266 phase-vector
actions on N21 and 480 versus 696 on N65. This comparison is against the
new per-displacement sum; it is not a speedup claim over every old sampler.
An additional nine complete boundary matrices pass with 377 raw core-call
receipts: pure two-power q=1, s=i, and s>i, including negative displacement
and the no-alias zero case. These are a separate execution, preserving the
original eight-case source and evidence.

For certified R=2^s q and s<=i, the aggregation lemma costs
O(q(i-s)+s) full-matrix transition groups, plus word lengths, integer bit
cost and discovery/verification. The present implementation still discovers
and replays the entire period in O(R). The symbolic small-odd-part discovery
route is not yet the executed backend. Large odd q remains the central
unresolved regime; a same-information classical order/factor comparator
must receive any order learned by the simulator.

[CONTINUE.md](CONTINUE.md) specifies the next useful mathematical work in
a form that any conversation can resume. [DEPENDENCIES.md](DEPENDENCIES.md)
pins the historical source/bank chain. The publication manifest binds the
current text files, and `readable_evidence/INDEX.json` restores every original
gzip byte from complete base64 chunks. Raw failures and superseded alias
validation evidence are retained and labelled. Reviews in `review/` are
shared-context source reviews, not independent admission.

Status: AUTHOR_SHARED_CONTEXT_SYMBOLIC_AND_ACTUAL_BOUNDED_NOT_ADMITTED.
No new ideal-QFT reference, general factoring advantage or physical-axis
change is claimed. Important research files are mirrored separately to the
authorized Drive research-material folder with an exact-byte readback receipt.

Global-Knowledge-Sync: main@06788df / GLOBAL_KNOWLEDGE_V1
