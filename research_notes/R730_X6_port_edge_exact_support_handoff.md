# R730 — portable X6 candidate BRC port-edge handoff

Date: 2026-11-12. Parent task `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, publication `TP2-8B7E13C5904A2D6F1142`. Source frozen science `a72226e2430ffa4786321ac86e7f0c599d5f0389`. Current normative context was read separately from canonical `main`.

Author Researcher-ID: `EM-X6-E9F77D`; Research-Activity-ID: `RA-61450C149C2C45468DF9FF63`. Native Source session registration: `6abe50f0991e3bd491c36e752fee04ff001e7653`. Researcher is *not* a formal owner merely by registration.

## Completed, reproducible science

R728's six-axis *candidate* port conflict H excludes four triple types `01k` while retaining 16 distinct-axis types. For opening only `T=01k`, `k=2..5`, at source occupation `a` of total `3m`, the number of open-T triple uses `s` has positive exact labeled-source branch multiplicity on the sharp contiguous interval
\[
\max(0,a_0+a_1-m)\ \le s\le\
\min\left(a_0,a_1,a_k,m,\{m-a_j:j\in\{2,3,4,5\}\setminus\{k\}\}\right),
\]
provided `a_k<=m`; otherwise no legal partition. The proof combines the previously proved R728 port-block feasibility and exact edge-admission transfer law.

The family `a=(m,r,m,m-r,0,0)`, `1<=r<=m`, has weighted provenance polynomial `F(z)=(m!)^2 z^r`, hence identical fully-open counts for varying r but different compulsory new-T usage counts. This supplies an exact future-count observer collision using the cap-on-new-T-uses query.

Verifier covers all 8,708 nonnegative vectors `a` for `m=1..4` at four `k` values (34,832 exact cases), plus all `r<=m<=8`. Local standard-library execution: `R730_EXACT_SUPPORT_AND_HIDDEN_ORDER_PASS`.

## Durable evidence locations

- GitHub Draft PR #2113: https://github.com/awdawmip/enterprise-math/pull/2113
- Full proof: `research_notes/R730_X6_port_edge_exact_support_proof.md`
- Executable verifier: `research_notes/R730_X6_port_edge_exact_support_verify.py`
- Finite result ledger: `research_notes/R730_X6_port_edge_exact_support_results.json`
- R728 prerequisite exact theorem and source: PR #2110 at `b825881b426fbced70ea0c38ec6146ac7815f688`.
- Separate parallel R729 named S3 observer-rank lane: PR #2112 at `5f1010b9142c297f59419ed544adb5bf397b76d5`.

The original task control packet, read in this run, reported `HANDOFF_READY / NEEDS_DISPATCH` with owner `taskbook/unassigned`, no live claim, predecessor claim `MCP-7ac116723fb07accba0ad37c` / comment `6781970912`, and a required **typed continuation** with verified preserved frontier. The author branch and session registration do not implement CLAIM, Source semantic checkpoint, frozen Result or independent Driver review.

## Smallest unfinished scientific unit

Inspect one exact lawful frozen native `Cell/Link/Port` update with source IDs, six-axis signed labels, event order and a `TRIADIC_CLOSURE_E` witness. Determine whether its *actual* allowed triad graph changes by one candidate `01k` edge, and whether V29 PASS/TRANSFER or V39 loop flow `j` can distinguish usage order `n_T`. If the law differs, preserve the precise counterevent and adapt the hypergraph and BRC branch certificate.

Keep proofs and finite support classifications in their declared candidate model. The native event and a formal Source RESULT remain open. Do not repin scientific inputs; no user credential, session secret or private access token is included here.
