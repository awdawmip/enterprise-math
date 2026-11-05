# PREFIX-503 — Quintic W-prefix index for exact dense BRC–KMP–source ranking

Date: 2026-11-05 (Asia/Shanghai). Independent author-side continuation of PREFIX-502.
Scientific input: immutable awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Current normative context was read separately from the canonical GLOBAL_KNOWLEDGE_V1 and Enterprise Math main.
Research status: AUTHOR_PROVED; EXACT_INTEGER_CHECKED for n=0..9; UNREVIEWED; NOT_ADMITTED.
Formal CLAIM/Result/Review: not established. Live native owner query and session registration pending at preparation time.

## Defined observation

In the explicitly embedded five-axis signed-path subfamily of native Heartbeat X6, take the ten native step letters
a,A,b,B,c,C,d,D,e,E, with sixth-axis occupation identically zero. A path of length n produces y in Z^5,
BRC cancellation counts V=p_b+2p_d+p_e and W=p_c+p_e with p_i=min(n_i+,n_i-),
terminal KMP state q for gate g=aab or aba, and first B/C source t in {N,B,C}.
The readout (n,y,V,W,q,t) and arbitrary future native signed-direction appends are retained.
Control/source support K_g(n,u,v,c,s,W,V) from PREFIX-500 is used exactly, with
u=y_a, v=y_b, c=|y_c|, s=|y_d|+|y_e|. Let k_g be its cardinality.

## Theorem: exact O(n^5)-word W-prefix index with O(n) oracle work per rank/unrank

Fix n>=0 and g in {aab,aba}. Assume the PREFIX-500 exact source-support oracle and the
PREFIX-501/502 observer-safe quotient and spatial-prefix results. There is an explicit
dense lexicographic rank and inverse of all reachable (y,V,W,q,t) of length n with:

1. O((n+1)^5) shared integer words (including the PREFIX-502 spatial index).
2. O((n+1)^6) oracle evaluations for full preprocessing.
3. At most 2m+1 <= n+1 source-support oracle evaluations per rank or inverse,
   where m=(n-|u|-|v|-c-s)/2 in the selected base fiber.
   Only O(log(n+2)) other prefix-row comparisons are needed.
4. Exact optimal fixed-length state payload ceil(log2 S_g(n)) bits. The index is shared.
   The same rank/inverse operation can be used after any signed native step append
   with the already proved BRC/KMP/source update at length n+1.

Proof. For each quotient spatial key p=(u,v,c,s) of compatible parity define
m=(n-|u|-|v|-c-s)/2 >=0. For integers 0<=W<=m, 0<=V<=2m define
Z_p(W)=sum_{V=0}^{2m} k_g(n,p,W,V);
H_p(j)=sum_{W=0}^{j-1} Z_p(W), for j=0,...,m+1.
Thus H_p(0)=0 and H_p(m+1)=A(p), where A(p)=sum_{W,V} k_g(n,p,W,V)
is the aggregate weight used in PREFIX-502. Nonreachable inputs have k_g=0.
For a particular reachable control pair (q,t), the exact lexicographic residual
offset within a given signed spatial displacement is

    H_p(W) + sum_{0<=V'<V} k_g(n,p,W,V') + ord_{K_g(n,p,W,V)}(q,t).

The three summands count precisely the preceding W rows, the preceding V
fibers in that row, and the preceding controls in this fiber. They are disjoint
and cover every predecessor. For inverse, the largest W with H_p(W)<=j is the
unique nonempty row containing residual j (use the last equal entry when a
zero-weight W row creates duplicate H entries); subtract H_p(W), scan
V=0,...,2m to find the unique control-bearing fiber, and recover the control
ordinal. Hence both maps are mutual inverses and leave no unused rank.

PREFIX-502 already gives a correct O(n^4)-word signed-y prefix which descends
to the residual W,V,control block. Retaining that prefix and all arrays H_p
gives the desired complete ranking and inverse. There are O((n+1)^4)
possible p and at most n+2 H entries per p, so O((n+1)^5) words.
Enumerating all p,W,V uses O((n+1)^6) exact support checks; this populates
A and H and the previously proved signed prefix. An individual rank performs
at most V+1<=2m+1 calls. Inverse uses binary search in monotone H and
at most 2m+1 calls to identify V, plus O(log(n+2)) spatial and W row
comparisons. All table entries are integers bounded by S_g(n) with
O(log(n+2)) bits for this fixed finite-state observation model. QED.

## Time–space frontier

PREFIX-501: O(n^6) shared words, O(1) online support-oracle calls.
PREFIX-502: O(n^4) shared words, O(n^2) online support-oracle calls.
PREFIX-503: O(n^5) shared words, O(n) online support-oracle calls.

These count exact integer operations and number of support queries, with
preprocessing and the shared index separately accounted for. This is a
constructive intermediate point, not a claim of Pareto optimality.

## Executed certificate and coverage

Python 3 standard-library certificate prefix503_quintic_wprefix_certificate.py
was executed with argument 9. It independently enumerates all reachable native
ten-letter observation states for n=0,...,9 for both gates; builds exact K
only for the finite checker; constructs the quintic H and spatial-index arrays;
and compares both rank and inverse at EVERY reachable observation against an
independently sorted state list. All assertions passed (ALL_CHECKS_PASS).

n=8: aab 60,590 / aba 60,550 joint states; quartic spatial-prefix 5,426
integer cells; extra W-prefix 2,112; total 7,538.
n=9: aab 127,403 / aba 127,298 joint states; quartic spatial-prefix 8,004;
extra W-prefix 3,212; total 11,216.
Maximum source-support lookups observed per rank/inverse at n=9: 9.
A source-support dictionary built from native state enumeration exists only
inside the finite validation harness and is excluded from index-space counts.
The fully general construction substitutes the already defined exact PREFIX-500
membership oracle. Validation does not time that production oracle.

## Next executable unit — PREFIX-504

Implement a tunable sparse-V block checkpoint over each W row, retaining
the W-prefix arrays, with selectable block width b. Derive memory
O(n^5+n^6/b) words and online O(b) support checks for the selected V block,
then measure actual preparation/query throughput and peak retained-memory
without including validation-only native state sets. This directly tests the
time–space tradeoff and clarifies when the quintic point is useful.

Source references: PREFIX-500 mod12 support oracle; PREFIX-501 observer-safe
quotient and dense lex rank; PREFIX-502 absolute-value convolution and quartic
spatial prefix, all in this repository under research_notes/portable_direct.

## Native identity, task inspection and exact certificate identity (post-publication)

Native session request em-prefix503-r6-20261105T0050 returned SUCCEEDED:
Researcher-ID EM-DIRECT-C8C94A, activity RA-81791D52F94F86BE292AF79F;
the canonical source readback of that registration is at
research_activity_records/RA-81791D52F94F86BE292AF79F.json on commit
aa4f779e5208b0c7dcb6fbf7cd31508a4cb01148.
This grants author-side attribution, not a formal task CLAIM.

Exact native task query em-prefix503-task-20261105T0053 returned SUCCEEDED
with immutable publication TP2-6A1F9D8C2047E3B51C01; observed state:
RS-X6-NATIVE-ROTATION-DYNAMICS READY / NEEDS_DISPATCH, owner
taskbook/unassigned, no current CLAIM. Its mother target remains
native signed-X6 rotation/path dynamics; this BRC observation coding
is a reusable subfamily tool rather than task closure.

The published Python certificate Git blob is
aa609083a90dfe107beea7a183a65bdb7d86fe73, identical to the blob
computed from the local Python file actually executed with argument 9.
That exact published-source run returned ALL_CHECKS_PASS. The repository
summary file reports the checked ranges and principal counts.
