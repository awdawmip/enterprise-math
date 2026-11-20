# Driver cross-line audit — exact half-walk Gram identity and length-eight sign completion

Date: 2026-11-20. Status: MODEL-CONDITIONAL MATHEMATICAL PROOF AND FINITE EXACT ENUMERATION; AUTHOR-SIDE DRIVER AUDIT; NOT INDEPENDENT NATIVE REVIEW; NOT NATIVE RESULT ADMISSION.

## Provenance and scope

The scientific predecessor is R762HD, https://github.com/awdawmip/enterprise-math/pull/2863 , head fe573942ec85d02ebfc513880a4cc53195b919c0, and its parity obstruction follow-up R762HE, https://github.com/awdawmip/enterprise-math/pull/2865 , head b539f214746af9bd40694f45f7b1198d093f25f6. Original researcher EM-X6-3050F6 retains authorship and ownership of that research line and Task RS-X6-TRIADIC-CLOSURE-DYNAMICS. This additional cross-line computation and proof belong to the already established Driver logical research line EM-DVR-DEBB5E. Frozen scientific source reference: enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.

The model is the proposed, reversible 15-Port, 16-signed-branch R762HD gate. An unsigned Port is an unordered pair P of the six named axes, and P -> Q is allowed when |P intersect Q|=1. Each candidate signed transition adds sigma times the six-coordinate 0/1 incidence vector h_(P union Q), with sigma in {-1,+1}, to the candidate Cell displacement. This is not an established primitive TRIADIC_CLOSURE_E permission predicate.

## Exact theorem: signed half-walk Gram identity

Fix P0={0,1}. For integer k>=0, let N_k(P,v) denote the number of signed candidate paths from (P0,0) to Port P and exact six-coordinate displacement v after k transitions. Let R_(2k) denote the number of length-(2k) signed candidate paths returning to Port P0 with exact zero displacement. Then

\[
\boxed{R_{2k}=\sum_{P}\sum_{v\in\mathbb Z^6}N_k(P,v)^2.}
\]

Proof: Every length-(2k) return decomposes uniquely at its intermediate state (P,v) after k steps. Reverse the second half's Port sequence and flip all branch signs. This bijects second halves returning from (P,v) to (P0,0) with length-k paths from (P0,0) to (P,v): adjacency is undirected, and h_(P union Q)=h_(Q union P). Hence the number of returns through (P,v) is exactly N_k(P,v) squared. Sum over all intermediate states. This combinatorial theorem preserves multiplicities and positive counts and uses only candidate transition reversibility; it does not imply native force closure.

## Exact independent computations

A self-contained Python standard-library verifier, with no floating-point calculations, is pinned at:
https://github.com/awdawmip/enterprise-math/blob/1f1f86298a59684103c6d930a72dbd92e70d841e/research_artifacts/driver_r762he_port_halfwalk_gram_check_20261120.py
Blob SHA1: 106233008e61f0fa6a3b7277449c2f1714ead1eb.

It computes the signed half-walk dynamic program and its Gram sum. Reproducing the predecessor's previously computed small cases, it extends the exact joint Cell-and-Port returns:

| Full length m=2k | Reachable states in half-walk N_k | Signed exact returns R_m |
| ---: | ---: | ---: |
| 0 | 1 | 1 |
| 2 | 16 | 16 |
| 4 | 193 | 624 |
| 6 | 1,980 | 34,688 |
| 8 | 15,909 | 2,413,424 |
| 10 | 92,556 | 200,986,368 |
| 12 | 376,057 | 19,705,107,552 |

The same verifier independently enumerates all 177,536 unsigned length-eight Port0-to-Port0 histories that satisfy the necessary zero-six-axis triple-support parity condition from R762HE. For every such history, it computes all signed zero-displacement completions by splitting its eight triple-support vectors into two four-step groups and matching opposite six-dimensional integer displacement vectors. Its exact sign-completion histogram (number of sign completions : number of unsigned histories) is:

| Sign completions | Unsigned histories |
| ---: | ---: |
| 4 | 9,600 |
| 6 | 19,200 |
| 8 | 33,120 |
| 10 | 7,200 |
| 12 | 47,808 |
| 16 | 18,936 |
| 18 | 7,632 |
| 20 | 4,224 |
| 24 | 23,136 |
| 36 | 2,112 |
| 40 | 4,224 |
| 70 | 344 |

The unsigned frequencies total 177,536. Their weighted sum is exactly 2,413,424, agreeing with the distinct half-walk Gram computation. Each of these length-eight parity-pass histories has at least four sign completions. Therefore support-parity zero is sufficient for *existence* at even lengths 0,2,4,6,8 in this candidate (the shorter lengths follow from the separately checked exact paths), without implying that parity determines multiplicity. The Gram identity gives aggregate signed returns at m=10 and 12, but the present enumeration does not prove parity sufficiency for each individual such longer history.

## Interpretation and remaining science

This corrects no primitive P000 assumption and is not evidence that the candidate event has been admitted as a native triadic force, Link, Port, Cell/time or rotation law. It supplies an exact positive-integer return algorithm and a bounded sign-completion audit for a proposed event language, with provenance separated from the original contributor. A valuable next independent question is whether every parity-pass unsigned Port return admits a sign completion for all even lengths or whether a first counterexample occurs at length >=10. Any transfer to native X6 dynamics needs the actual typed primitive event admissibility predicate.

One author-side mathematical subunit completed and Source-preserved. Independent Native Review newly admitted: 0. Native Results newly accepted: 0. Formal Task completed: 0. Parent objective completed: 0. Existing research ownership and scheduler unchanged.