# Stage456-B: exact grouped BRC count at the c=m boundary (P has no POP)

Date: 2026-11-05. Status: AUTHOR_SIDE_PROOF / EXECUTED_EXACT_INTEGER_CHECK / UNREVIEWED. Parent: Stage455-B at Git commit `8c47b9a272133efedc018161a5d18455c86d805e`, PR #1736. Frozen scientific references inherited from that parent: global `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, EM `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, P000 original blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Current behavioral context read separately via the 2026-11-05 canonical main entrypoints.

## Exact population, observer, and future operations

Take ordered source-distinct native X6 histories `P=(P_1,...,P_m)`, `Q=(Q_1,...,Q_n)`, with `2<=m<n`. Original letters are `A=+E_1` and `B=-E_1`; both source endpoints are A; no two B letters are adjacent. Fix `k_P,k_Q` original B counts and `d=m-K` original mismatching positions. Thus the original *full* six-component endpoints and full 12x12 directed adjacency matrices are also fixed (the only edges are AA, AB, BA with multiplicities determined by length and B count). Retain order, source labels, positive integer multiplicities, and every exact future observer.

P has no POP permission; Q may POP at most `b` times with `0<=b<=n-m`. Both may APPEND in any of the 12 signed original X6 directions, with fixed arbitrary nonnegative respective budgets `r_P,r_Q`. After every legal labeled operation prefix observe both lengths, each native six-component endpoint, each directed 12x12 adjacency histogram, and position-match count K. The Q-APPEND budget does not change the required original-hidden repair key in this regime.

Set `u=n-b`, `t=min(n,m+r_P)` and `g=max(0,u-t-1)`. In Stage453's indexed general repair theorem, `c=min(m,n-b)=m`. The exact future-equivalence key is the indexed original Q letter assignment on
`S=({m} if u=m else empty) union {m+1,...,t} union {u,...,n-1}`.
`Q_n=A` is fixed and may be included harmlessly. The visible-index union can overlap. Future-equivalence here means identical full observer trees for every same legal labeled control sequence. Necessity follows from Q-POP revealing its predecessor edges and from P-APPEND testing Q at `m+1,...,t`; sufficiency follows from deterministic endpoint/edge updates and the K update, with current observation O fixed. This reuses Stage453's author-side theorem with the stated scope; no new universal admission is asserted.

## Theorem 456.1: exact grouped C/T/U at c=m

There is a deterministic integer transfer counting both (i) the number `q_F` of supported distinct keys S, and (ii) the complete ordered-original-history population `|F|`, without enumerating individual histories or individual repair keys.

Let `T_m(j,z)` count original paired prefixes `(P_1,...,P_m; Q_1,...,Q_m)`, with `k_P` B's in P, `j` B's in Q, exactly `d` paired mismatches, isolated B, `P_1=Q_1=P_m=A`, and last Q letter `Q_m=z in {A,B}`. A five-coordinate integer DP `(#B_P,#B_Q,#mismatch,lastP,lastQ)` computes this array exactly.

A deterministic visible-letter automaton emits only the indexed Q letters on S, respecting the known terminal `Q_n=A` and the no-adjacent-B constraint whenever two emitted original positions are consecutive. Group distinct emitted words by summary
`sigma=(v,z_visible,q_{m+1},q_t,q_u)`, where `v` counts B letters emitted at positions strictly greater than m, `z_visible` is the exposed Q_m when u=m (otherwise unspecified), and missing boundary symbols are marked absent. Write `C(sigma)` for the number of different visible words with that summary. Each is a *different repair key*, irrespective of its hidden-population weight.

Let `U_g(h;left,right)` be the exact number of isolated-B fillings of the hidden Q-only interval `{t+1,...,u-1}` with `h` B, compatible with both adjacent boundary letters `left,right`; define `U_0(0)=1`, all other `U_0(h)=0`. The gap exists only when `g>0`, so its right neighbor `Q_u` is always visible.

For a summary sigma, define `boundary(z,sigma)` as the indicator that z equals exposed Q_m when Q_m is visible and that z and exposed `Q_{m+1}` are not both B when `Q_{m+1}` is visible. For `g>0`, the gap's left neighbor is `Q_t` when `t>m`; when `t=m` it is the *hidden* Q_m=z. Denote that neighbor by `lambda(z,sigma)` and the right neighbor Q_u by `rho(sigma)`. The population of any one key with summary sigma is

`M(sigma) = sum_(j,z) T_m(j,z) * boundary(z,sigma) * U_g(k_Q-j-v; lambda(z,sigma), rho(sigma)).`

For g=0 the U factor means only the Kronecker condition k_Q=j+v, and adjacency Q_m/Q_(m+1) is handled by the boundary indicator or by the visible-letter automaton when Q_m itself is exposed. All hidden constraints are entirely within the paired prefix and optional single Q gap, connected at constant-size boundary letters. Accordingly,
`q_F=sum_sigma C(sigma)*[M(sigma)>0]` and
`|F|=sum_sigma C(sigma)*M(sigma)`.

Proof: every admissible original history partitions uniquely into its indexed visible Q key, paired prefix and Q-only gap. Given sigma, the quantities that affect hidden completions are exactly remaining B counts, the paired mismatch target and the neighboring edge letters. Therefore every visible key counted by C(sigma) has the same hidden completion multiplicity M(sigma). Conversely concatenating any admissible prefix, visible word and gap satisfying the boundary relations yields exactly one admissible ordered original history. The partition is disjoint and exhaustive. This also proves that the Boolean-support sum counts distinct supported future keys.

The prefix DP has polynomially many integer states in `m,k_P,k_Q,d`; visible-word C uses a constant set of boundary letters plus `v`, the last emitted index/letter, and position; U uses a 2-state B-count recurrence. Direct memoized evaluation is bounded conservatively by `O(N^5)` exact integer arithmetic operations for `N=max(m,n)`, with integer result lengths `O(m+n)` bits; time for big-integer arithmetic and dictionary handling is additional. This is not a general sorting complexity statement.

## Strict information-loss witness

`m=2,n=6,k_P=0,k_Q=2,d=1,b=0,r_P=0`. Then `P=AA`; the only eligible Q words are `ABABAA` and `ABAABA`. Both are in one current-observer fiber and one future class, and have total BRC population 2. Here `Q_m=Q_2=B` is hidden, `t=m=2,u=n=6`, and the hidden gap is `Q_3,...,Q_5`. If the U gap is erroneously computed with its left neighbor fixed to A, an extra inadmissible history `Q=ABBAAA` is counted, falsely returning population 3; the actual Q_2=B excludes adjacent Q_3=B. Thus the coupling through hidden `Q_m` is necessary for exact mass.

## Verification and current scope

A separately coded brute enumerator builds every A/B history satisfying endpoints, defect isolation and exact `(k_P,k_Q,d)`; it groups by the indexed key S. A deterministic seeded 1600-case test compares `q_F` and `|F|` exactly with the grouped DP, with all 1600 passing, 729 nonempty fibers, aggregate population 15650, and aggregate class counts 1268. This independently checks the new c=m arithmetic. The full future-equivalence identification is inherited from Stage453, not directly exhaustively re-enumerated in this run.

Large nonenumerated examples all have `(m,n,k_P,k_Q,d)=(64,80,15,17,1)`, `|F|=5,061,384,194,832,966`:
`(b,r_P)=(0,0): q_F=1; (5,0):13; (5,3):55; (16,0):315.`
Another case `(m,n,k_P,k_Q,d,b,r_P)=(92,126,20,25,3,12,7)` has `q_F=12685`, `|F|=1121449082621221549433213976`. Source code and the exact run output are attached in this directory.

## BRC typing and continuation

BRC carrier = source-distinct ordered original path pairs; Boolean support = which visible indexed repair words have positive completion mass; positive integer mass = exact number of original history pairs per repair word; observer = full native endpoints/J/K after each legal future operation; port quotient = exact future-equivalence keys S. Input A/B restriction is an explicitly embedded subfamily of native six-axis signed-direction paths; future actions retain all twelve directions. No phase-amplitude cancellation or physical time evolution is asserted.

Researcher `EM-DIRECT-2D9D84`; activity `RA-01525A0AEF2AC11F3C96232B` registered with Source. This is author-side evidence on the Draft PR; formal task owner, CLAIM, Result and independent review have separate gates.

Next: generalize the grouped transfer to pP=0 and c<m (Q can POP below P), and build key rank/unrank using weighted summarized automaton counts. Preserve hidden-terminal coupling and the actual bit complexity.