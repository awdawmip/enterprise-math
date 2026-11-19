# R762FR — Resettable gate queries versus one irreversible fail-stop trace

Date: 2026-11-19 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_ENUMERATION_PASS / NOT_REVIEWED.
Mother Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS. Frozen taskbook @857280d1012943290d141d1317179c40ec3cbdf8, frozen P000 @a72226e2430ffa4786321ac86e7f0c599d5f0389. Direct antecedent: R762FQ in this PR; R762FP in PR #2787.

## Exact change in observation semantics

Use the R762FQ tensor with m>=1 independent disconnected remote gates and 3^m histories in {H0,H1,H2}^m. A gate blocks exactly in state H1. Successful attempts swap H0 and H2 in the tested block, preserving the enabled status.

R762FQ permits independent experiments that reset to the initial state. In **one irreversible trace** considered here there is no reset. A deterministic controller chooses which gate to try next based on its publicly observed success and root outputs. Failure publicly reports BLOCK and **terminates the entire trace**; success gives no source-event information and the root remains (1,1). Horizon h counts attempts, not physical time.

This theorem counts distinct *single-run transcripts for one fixed policy*, maximizing over policies. It does not claim to give the universal equivalence under the entire family of separately resettable experiments.

## Theorem — Exact single-run information limit

For every integer m>=1 and h>=0 let t=min(h,m). The maximal number of distinct public single-run transcripts, over all deterministic controllers under these rules, is

C(m,h) = t+1.

Any policy that probes t distinct edges in a fixed order achieves this optimum. A transcript is the first blocked position j in {1,...,t}, or NONE if all t tests succeed. Its exact full-history fibers are

F_j(m)=2^(j-1)*3^(m-j),  1<=j<=t,

F_NONE(m,t)=2^t*3^(m-t),

with sum_j F_j(m)+F_NONE(m,t)=3^m.

Hence a sharp fixed-length *outcome code* for one optimal single-trace policy uses ceil(log_2(t+1)) bits. For h>=m the code needs ceil(log_2(m+1)) bits; independent resettable experiments in R762FQ need m bits to capture the entire gate-status vector. Full named source histories still number 3^m and require ceil(m log_2 3) bits.

### Proof

Success only flips H0 <-> H2, leaving the corresponding block enabled and the public root unchanged. Repeating a previously successful gate cannot reveal a new fact. Before the first BLOCK, the public observations are a fixed sequence of SUCCESS and identical root outputs; therefore every deterministic adaptive policy follows one fixed all-success path, with at most t distinct tested gates. The only possible transcripts are BLOCK at one of these gates, or no BLOCK: at most t+1.

A fixed order of t different gates attains all t+1 transcripts: independent block states allow us to place the first H1 at any specified position, or to omit H1 from the tested prefix. If the first H1 appears at position j, the earlier j-1 blocks have two enabled choices, the jth has one choice, and all remaining m-j blocks have three choices, yielding F_j. If no tested gate blocks, the first t blocks each have two choices and the remaining m-t each have three, yielding F_NONE. These exhaustive disjoint classes sum to 3^m. QED.

## Explicit m=6 example

Take k=13, m=6. All 729 legal histories share the same visible root. Under six resettable experiments the 64 different 6-bit status vectors require 6 bits. A single terminal-failure trace of six ordered tests has only **7** outcomes, requiring **3** bits. The exact fiber sizes are

(243,162,108,72,48,32,64).

If BLOCK is public but *nonterminating*, leaving the state unchanged, a single run can instead test all m edges and recover m bits. Thus actual native action contracts must resolve observability and termination separately.

## Verification

The companion standalone Python checker enumerates all 3^m histories and all **nonrepeating fixed-order policies** of length 0..m for every m=1..6, with exact integer comparisons of every history's trace and class fibers. Any deterministic adaptive policy has the same one all-success branch, so this enumeration covers its possible observation structure. At m=6, the checker covers **1,957** policies and **1,426,653** policy-history outcomes. Total over m=1..6: **2,371** policies, **1,511,619** outcomes. PASS. General statement author-proved; independent Review NOT_REVIEWED.

This is a candidate positive named-source BRC incidence model within a selected three-axis X6 slice; no native signed TRIADIC_CLOSURE_E Cell/Link/Port gate was certified, and P000's primitive three-force ontology is unchanged.

## Next native question

Obtain frozen, actual signed Cell/Link/Port action permissions, BLOCK visibility, failure-stop/reset policy and source-state updates. For potentially non-involutive or silent actions derive the causal single-run observer and the exact observer-safe provenance quotient, retaining P000's signed axes and named paths. This PR is portable scientific evidence, not Source CLAIM/PROGRESS, formal Result or independent Review.
