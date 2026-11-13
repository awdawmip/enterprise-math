# Stage447-B — Exact output-word automata and asymmetric POP repair

Parent Stage446-B at `research_notes/n12_x6_native_brc_stage446b_one_append_asym_20261105_RESEARCH2/`, further continuing Stage445-B (commit `2a0924049d45ce1138f50eacebb62dce84b79210`).
Frozen scientific pins: GLOBAL `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`; Enterprise Math `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`; P000 Git blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Load current behavioral rules separately.

Stage446-B proved directly for `m<n, pP=pQ=rQ=0, rP=1` that full future equivalence is equality of `Q_(m+1)`, with Boolean support of at most two classes in the binary nonadjacent B family. It supplies weighted DP `O(n (kP+1)(kQ+1)(d+1))` and an explicit false end-suffix merge at (m,n,kP,kQ,d)=(6,10,1,2,1). Raw masses (Q_(m+1)=A,B) are (9,4), total 13. Python standard-library exact checks verified 400 parameter tuples and full 12-direction APPEND observations for 3045 actual histories.

Next research objectives:
1. Extend P-only APPEND budget to `rP=2,...,n-m`. Prove whether the exact future key is precisely the Q-original subword `Q_(m+1)..Q_(min(n,m+rP))` within a fixed present-O fiber; handle the saturation `m+rP>=n`. Build a deterministic support DP for different output words with exact integer class masses, lexicographic ranks and within-class reconstruction without enumerating the whole raw fiber.
2. Introduce asymmetric P/Q POP budgets up to two. Derive the minimal extra boundary equality and direction slots, testing proposed merges by shortest labelled operation words with full native X6 endpoint, directed J and K at every step. Preserve cases where signed-source provenance or cross-source matching distinguishes otherwise identical present observers.
3. Compare output-word DP states against Stage443-B `2^b` output enumeration, and account for exact big-integer bit cost, class-code cost, and original history decoding. At minimum produce a new parametrized proof or an exact witnessed false merge.
4. Preserve owner/CLAIM/Result/Driver admission as distinct authorization actions. Retain source-specific BRC positive integer populations; do not present quotient label as complete original provenance.

Deliver complete proof, executed self-contained checker, bounded exact evidence, and a next independent research unit in the current Enterprise Math project repository; verify remote artifact readback.
