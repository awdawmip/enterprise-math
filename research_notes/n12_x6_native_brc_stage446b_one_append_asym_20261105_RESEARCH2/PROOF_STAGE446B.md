# Stage446-B — Polynomial exact support for an unequal-length single-APPEND X6 history fiber

Date: 2026-11-05. Research2 continuation after Stage445-B at `2a0924049d45ce1138f50eacebb62dce84b79210`.
Status: AUTHOR_SIDE_PROOF / EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Immutable scientific inputs and scope

Frozen scientific pins: GLOBAL `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`;
Enterprise Math `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`;
P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`.
Current behavioral rules are loaded separately from canonical main.
The Stage439-B two-source future-repair theorem is author-side provenance at `7f9456031a9fdfdf12836116f178a17bf50be965`; the main new theorem below has a direct proof not requiring that theorem.

Work within the native X6 signed directions `D={±E1,...,±E6}`. Set A=+E1 and B=-E1 for an explicitly restricted binary ordered-path family. This is a static X6 auxiliary observer, not a two-dimensional native spatial model. All source histories preserve order and provenance.

Let initial lengths `3<=m<n`; `P∈{A,B}^m`, `Q∈{A,B}^n`, with A endpoints and no consecutive B in either. Fix P/Q defect populations `kP,kQ`, and fix `d=m-K`, the number of unlike original letters in the overlap. Thus the complete present observer
`O=(m,n,V_P,V_Q,J_P,J_Q,K)`
is constant on this family: for a word of length `l` with `k` internal isolated Bs, `V=(l-2k)E1` and `J_AA=l-1-2k, J_AB=J_BA=k, J_BB=0`.

**Declared future controls**: P may APPEND one arbitrary direction `z∈D` or do nothing. Q cannot be modified; neither source may POP. We observe the initial O and O after every legal labelled APPEND. The position `m+1` already exists in Q because `m<n`.

## Theorem 446.1 — Exact quotient and sharp class bound

For two histories H=(P,Q), H'=(P',Q') in the same present-O fiber F,
`H ~ H'` for every declared future observation **iff**
`Q_(m+1)=Q'_(m+1)`.

Consequently the number of distinct future equivalence classes is
`q_F = [M_A>0]+[M_B>0] <= 2`,
where `M_x= #{(P,Q)∈F: Q_(m+1)=x}` are **exact, positive-integer BRC branch populations**.
When `q_F=2`, the minimum fixed-width class label needs one bit; when `q_F=1`, zero bits.

**Proof.** The current observer O is fixed in F. One P:APPEND(z) changes its endpoint to `V_P+vec(z)`, adds exactly one P adjacency edge `(A,z)` (P ends in A), and raises P length by one. These changes and the entire unchanged Q observer depend only on O and z. Since Q has an original letter at m+1, the new positional match count is exactly
`K_after(z)=K_before+[Q_(m+1)=z]`.
For equal Q_(m+1), this expression agrees for all twelve possible z, hence every future observation agrees. For unequal Q_(m+1), choose `z=Q_(m+1)`; one expression increases K and the other does not, distinguishing the histories after exactly one labelled operation. There are no other future transitions. QED.

Note the asymmetric cross-source readout: original last letters `P_m,Q_n` and all initial observables can agree while the missing `Q_(m+1)` controls future K. The latter is exactly the A_Q direction slot in the Stage439-B repair key for this specialized budget.

## Theorem 446.2 — Exact polynomial masses without enumerating raw histories

For each forced value `x∈{A,B}`, introduce integer DP state
`C_i(a,b,h,u,v)`, counting initial length-i paired prefixes, where `a,b` count P/Q Bs, `h` counts mismatches in positions <=min(i,m), and `u,v∈{0,1}` are the most recent P/Q B indicators (P is set to 0 at indices >m). Initialize `C_0(0,0,0,0,0)=1`. For each position i=1,...,n, choose (s,t)∈{0,1}², forcing s=0 if i=1 or i>=m, and t=0 if i=1 or i=n; for i>m P is absent and s=0. For i<=m, enforce source P's endpoint/adjacency rules and add the mismatch bit `[s≠t]`. Always enforce Q's endpoint/adjacency rule, `u*s=0,v*t=0`, and at i=m+1 force t to encode x. Discard counts exceeding kP,kQ,d. Then
`C_i(a+s,b+t,h+[s!=t and i<=m],s,t) += C_(i-1)(a,b,h,u,v)`.
The desired mass is `M_x= sum_(u,v) C_n(kP,kQ,d,u,v)`.

**Proof.** A legal DP path specifies precisely one ordered pair (P,Q) with the required source-specific endpoints, no adjacent defects, total defects, overlap mismatch, and forced x; conversely each pair specifies one and only one transition sequence. Thus the terminal weighted sum is exactly M_x, not a count of DP states or a Boolean support approximation. The disjoint masses sum to the complete raw population |F|. QED.

Write `H=4(kP+1)(kQ+1)(d+1)`. Each layer has at most H states and at most four transitions per state, so both masses take `O(nH)` arbitrary-precision integer additions and `O(H)` active integer cells. Since |F|<=2^(m+n), each integer has O(m+n) bits; ordinary linear-time big-integer additions give `O(nH(m+n))` bit operations. Under one mismatch d=1, the bound is `O(n(kP+1)(kQ+1))` integer additions; it remains polynomial when both defect counts grow with input length. The same weighted completion recurrence with fixed x supplies exact lexicographic within-class ranking/unranking and complete original-history reconstruction, using O(nH) precomputed integer cells and O(n) decoding transitions. Class ranking orders only supported x values, without a two-entry table being mandatory.

## Explicit unequal-length false merge of the end-suffix-only carrier

Take `m=6,n=10,kP=1,kQ=2,K=5`, P:`AABAAA`,
Q1:`AAAAAABABA` (Bs at 7,9), Q2:`AABABAAAAA` (Bs at 3,5).
Each has exactly one original P/Q mismatch over the first six positions. Both histories have exactly the same complete O:
`V_P=4E1, V_Q=6E1, K=5;`
`J_P=(AA:3,AB:1,BA:1,BB:0)` and
`J_Q=(AA:5,AB:2,BA:2,BB:0)`.
Both original final letters are A; all POP suffix budgets are zero. Yet Q1_7=B, Q2_7=A.
One future `P:APPEND(B)` yields `K_after=6` versus `5`.
Thus retaining only the two original end-suffix letters would incorrectly merge them.

For the **entire** present-O fiber at these exact parameters the independent integer DP gives `M_A=9, M_B=4`, so `|F|=13, q_F=2`, and this is a sharp one-bit class split.

## Actually executed finite cross-check

Run `python3 STAGE446B.py`; its sole JSON line is preserved in `STAGE446B_EXECUTED.json`.
The stdlib-only program compares direct history enumeration with the independent integer DP for 400 parameter tuples `m=5..8,n=m+1..m+5,kP=0..3,kQ=0..4,d=1` (with legal limits), giving 213 nonempty fibers, 3045 total raw history instances, 86 fibers with both future classes, 53767 DP transition visits, and 3045 actual full-future signature checks. Full signatures include initial O and the 12 possible P APPEND(z) observations including full six-vector V, directed adjacency J and K. The witness K values are asserted separately. All checks passed. Finite checks support the direct general proof and exercise the exact implemented recurrence; no numeric approximations or simulated semantic placement were used.

## Next

Stage447-B: permit `rP>=2` while Q remains fixed and longer, and derive a deterministic output-word support automaton for `Q_(m+1)..Q_(min(n,m+rP))`, with exact mass and ranking. Separately allow one or two asymmetric POPs, test any proposed summary by shortest full-observer labelled traces, and measure state/bit complexity versus Stage443-B key enumeration. Preserve frozen scientific pins and formal owner/review gates.
