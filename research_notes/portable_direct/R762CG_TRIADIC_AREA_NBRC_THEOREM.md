# R762CG — Three-port discrete area cocycle and exact N-BRC path-fibre repair

**Task:** RS-X6-TRIADIC-CLOSURE-DYNAMICS, published Task TP2-8B7E13C5904A2D6F1142. Frozen science from a72226e2430ffa4786321ac86e7f0c599d5f0389; predecessor R762CF at 93a34da83acbc6d6a9ca3cc2db833677c4baef84. **Status:** Author-proved conditional mathematics, exact finite integer N-BRC checks; independent review NOT_REVIEWED.

## Definition: typed signed-X6 three-Port candidate

The native Cell carrier is a torsor over Z^6 with a selected chart anchor, never a preferred global origin. Three named force Ports P_j=(a_j,s_j), j cyclic in {1,2,3}, have distinct axes a_j in {1,...,6}, signs s_j=±1, equal nonzero primitive force quantum and directed cyclic Links 1→2→3→1. This **candidate** declares every such complete triple TRIADIC_CLOSURE_E=true, and admits no primitive stable nonzero one- or two-force balance.

Write u_j=s_j e_(a_j), v_j=s_(j+1)e_(a_(j+1)), with indices cyclic. Its three *composite* four-primitive-step Cell loops are

B_j=(u_j,-u_j,v_j,-v_j),
L_j^+=(u_j,v_j,-u_j,-v_j),
L_j^-=(v_j,u_j,-v_j,-u_j).

Each closes its Cell, increments primitive-step time by four, moves only along signed native primitive axes and has the same signed-step histogram: one each of u_j, -u_j, v_j, -v_j. The attached named forces and cyclic Links follow the Cell; no native two-dimensional plane is introduced.

For a path H=(d_1,...,d_m) with the Port frame fixed, set

A_j(H)=s_j*s_(j+1) Σ_(1≤p<t≤m) (d_p)_(a_j) (d_t)_(a_(j+1)).

For closed paths, the mod-q tuple r(H)=(A_1(H),A_2(H),A_3(H)) mod q lies in (Z/qZ)^3, for any fixed integer q≥2. Its coordinates are **path provenance**, not new spatial axes. The coarse observer O reads the final signed X6 Cell, all named signed Ports, the cyclic Links, elapsed primitive-step time, and the complete twelve-direction signed primitive-step histogram, while forgetting step order.

The future candidate transition system carries r and permits a Port replacement T_(j,b), for any axis b unused by the current triple, exactly when r_j=0. The replacement changes the axis of Port j, keeps its sign, and preserves r. Later B, L^+, L^- loops in the then-current Port frame update r by 0, +e_j, -e_j respectively. This is an **event-labelled Port-register update rule**. The area formula derives the initial registers for paths before their first Port substitution; it is not asserted to be a frame-independent area formula across substitutions.

## Theorem 1 — Discrete central cocycle

For a fixed signed Port pair, put α_t=s_j(d_t)_(a_j), β_t=s_(j+1)(d_t)_(a_(j+1)), x(H)=Σα_t, y(H)=Σβ_t and c(H)=Σ_(p<t) α_p β_t. For concatenations HK,

x(HK)=x(H)+x(K), y(HK)=y(H)+y(K),
c(HK)=c(H)+c(K)+x(H)y(K).

**Proof.** Partition ordered pairs of positions in HK into pairs contained in H, pairs contained in K, and one position in H followed by one in K. Their cross contribution is (Σ_H α)(Σ_K β). This gives the three identities, including the integral two-step nilpotent composition law (x,y,c)*(x',y',c')=(x+x',y+y',c+c'+xy'). For closed H and K, x(H)=0 so c is additive. Direct evaluation gives

r(B_j)=0, r(L_j^+)=+e_j, r(L_j^-)=-e_j,

since only the two distinct axes of that rooted Port pair occur in those loops; all other rooted pairs miss one moving axis. The three oriented Port loops generate (Z/qZ)^3. The construction is covariant under S6 axis-label permutations and cyclic C3 Port reindexings. QED.

## Theorem 2 — A single coarse fibre with exactly q^3 distinct future states

For each r=(r_1,r_2,r_3) with 0≤r_j<q, consider

W_r = [B_1^(q-r_1) (L_1^+)^(r_1)] [B_2^(q-r_2) (L_2^+)^(r_2)] [B_3^(q-r_3) (L_3^+)^(r_3)].

Every W_r has exactly 3q completed loops and 12q signed primitive steps, returns to the same Cell, keeps the same three named Ports and Links, and has 2q occurrences of **each sign** of each of the three occupied axes, with none on the three unused axes. Hence all q^3 witnesses yield exactly the same O readout. By Theorem 1 the retained residues are precisely r.

For r≠s, pick j with r_j≠s_j and choose k≡-r_j mod q. The continuation with |k| signed L_j loops of the appropriate orientation followed by T_(j,b) is legal for r and illegal for s. Thus there are at least q^3 pairwise different future event languages. Conversely, after the common O readout, all later macro-loop updates and replacement guards depend on past history only through r, and their changes to the visible Ports are identical for matching r. Thus there are at most q^3 classes.

**Conclusion:** The exact all-future behavioural quotient of this O fibre contains q^3 classes. The minimal fixed-width BRC source-repair length is ceil(log₂(q^3)) bits. This strengthens the single-pair q-class conditional example of R762CF to three independent rooted provenance coordinates on the **same native X6 Cell**. QED.

## Theorem 3 — Two-sided finite-horizon observer

Fix h≥0. The declared Boolean observer tests Q_(j,k)(r): permission for T_(j,b) after k positive L_j loops for k≥0, or -k negative L_j loops for k<0, for all j=1,2,3 and -h≤k≤h. Each Q_(j,k)(r) is [r_j+k≡0 mod q], tested from the same original state. For one Port, each residue in S_h={-k mod q : -h≤k≤h} has its own single-positive signature; every residue outside S_h has the common all-false signature. Since |S_h|=min(q,2h+1), the single-Port quotient has min(q,2h+2) classes. Independence yields

K_3(q,h)=min(q,2h+2)^3,
R_3(q,h)=ceil(log₂(K_3(q,h))) bits.

In the restricted oracle that returns **one Q_(j,k) bit per query**, the exact global worst-case identification cost is D(q,h)=3 min(q-1,2h+1) distinct point queries: each Port needs all hit phases tested if an unseen outside class remains, or all but one if every phase is hit. An adversary returning false forces this cost separately on all three Ports. Query complexity and unrestricted fixed-width code length are different quantities.

The K_3 theorem covers these stated bounded terminal guards. Any richer adaptive multi-event observation requires its own preservation theorem.

## Theorem 4 — Exact positive N-BRC branch weights

Expose all ordered choices B_j or L_j^+ in exactly q loop slots of each Port j, concatenating the three labelled blocks. There are **2^(3q)** distinct ordered source histories, all with the same coarse readout O of Theorem 2. Their exact source carrier is the positive integer N-BRC group algebra N[(Z/qZ)^3] with multiplication by cyclic convolution, rather than a collapsed scalar count.

Formally, in x_j^q=1, the branch generating polynomial is

F_q(x_1,x_2,x_3)=∏_(j=1)^3 (1+x_j)^q.

For r=(r_1,r_2,r_3), the exact coefficient is
w_q(r)=∏_(j=1)^3 f_q(r_j),
where f_q(0)=2 and f_q(a)=binom(q,a) for 1≤a<q.

**Proof.** For one Port, choosing k of its q labelled slots to be L_j^+ gives binom(q,k) histories and residue k mod q. Residue zero is reached by both k=0 and k=q, giving coefficient 2; the other residues have one possible k. Independent Port blocks multiply the three coefficients. Summing gives Σ_r w_q(r)=(2^q)^3. All classes have positive weight.

The number of source histories where terminal guard Q_(j,k) succeeds is exactly

M_(j,k)=2^(2q) f_q((-k) mod q).

For a finite horizon h, keep one singleton weighted class f_q(a) for each a∈S_h, and (when S_h is not exhaustive) one residual class of weight 2^q-Σ_(a∈S_h) f_q(a); their three-fold product is a **mass-preserving N-BRC quotient** with K_3(q,h) classes. Collapsing all branches to 2^(3q) erases future-guard provenance and is not safe for this interface. No signed cancellation is inferred from positive branch counts.

| q | all-future classes | fixed repair bits | total labelled histories | one-Port weights f_q(0..q-1) |
|---:|---:|---:|---:|---|
| 2 | 8 | 3 | 64 | 2,2 |
| 3 | 27 | 5 | 512 | 2,3,3 |
| 4 | 64 | 6 | 4096 | 2,4,6,4 |
| 5 | 125 | 7 | 32768 | 2,5,10,10,5 |
| 7 | 343 | 9 | 2097152 | 2,7,21,35,35,21,7 |

For q=7 the bounded horizon class counts at h=0,1,2,3 are 8,64,216,343, requiring 3,6,8,9 bits.

## Evidence and precise boundary

The accompanying R762CG_VERIFY.py executes integer N-BRC branch convolution with signed source paths; it checks all 720 six-axis permutations × 8 sign assignments × 3 Port pairs (17,280 loop identities), the area and histogram laws, q=2..10 phase/count/horizon results, source guard masses, all-source enumeration q=2,3,4 and the explicit q≤6 separating suffixes. R762CG_EVIDENCE.json contains the results and exact coverage. The general claims follow from the displayed proofs, not finite extrapolation.

This construction is compatible with the declared P000 six signed axes, its PERP_E native pair relation, three-force arity, separately typed time, provenance retention, and rooted C3 Port action. Its *event licence is conditional*: the authentic TRIADIC_CLOSURE_E predicate, actual native signed Cell/Link/Port admission, and a legal V17/V29/V39 transducer still require independent source-backed construction. It is not asserted that a two-coordinate formula supplies an independent native plane or complete three-dimensional slice. Review remains NOT_REVIEWED.

**Next discriminating step:** inspect the exact native signed TRIADIC_CLOSURE_E and V17/V29/V39 event rules. Test whether their legal event language factors through the 12 sign-gate atoms, the three Port-rooted oriented-area source coordinates, or a richer event-labelled path carrier. Exhibit either a typed permission-preserving map across Port substitutions or one explicit counterexample path pair and separating licensed future operation.
