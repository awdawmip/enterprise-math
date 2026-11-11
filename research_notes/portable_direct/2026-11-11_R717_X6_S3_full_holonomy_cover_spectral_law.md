# R717 — Full six-value X6/BRC holonomy cover, exact spectral counts and optimal typed ring execution

Date: 2026-11-11 Asia/Shanghai. Parent: RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142 (lineage only; owner requires a fresh native receipt). Classification: author-side mathematical theorem with a full finite integer matrix certificate, not a formal native Result or independent Review.

**Scientific pin:** awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389, including locked P000 V5, V17 slot transport, V20 native triad update, V29 typed positive occurrences and V36 ring copy. Inputs reused without changing their scope: R709b@15057fffe4aef6610e8686b20495771cd071f8ef, R711@8fe4c9ce43183e9394d1e4047585ba51c336c483, R712@e74bb4deb28b07bbfb12c147a282a336d72dd4e5, and R716b@1ed250c30b02e42cc0eb57beded21eed8630df9d.

## 1. Carrier, BRC interface and question

The previous balanced four-packet family R709b gave three even S3 holonomies, and R716b classified optimal five-phase schedule bracelets. The present question is whether the **full** native active-triad path-formal BRC population can display more pointed relationship outcomes, and how many states a coarse future observer must retain.

Let J=J(6,3) consist of the 20 three-element subsets of the six native axes {0,1,2,3,4,5}. Two distinct triads are adjacent iff their intersection has size two. Fix S={0,1,2}. A rooted closed path W=(T_0=S,T_1,...,T_m=S) has precisely m one-axis replacement edges. Every distinct ordered W is retained as one unit-positive, source-labelled PATH-FORMAL BRC branch. There is no signed or destructive cancellation of these positive branches.

A V17 lift starts with three **named slots** (0,1,2). At each T->U, retain both common axes in their original slots and replace the unique exiting axis in its slot with the entering axis. On return, slots form a permutation of S. Let h(W) be the tuple of positions occupied by axes 0,1,2 respectively, an element of S3. This defines the precise observer on the original path: N_m(h)=# {closed m-edge positive branches W with h(W)=h}. Native Cell spatial coordinates, three-axis active triads, slot-frame histories and finite scheduler phases are separate types; no two-dimensional native plane is introduced.

## 2. Theorem R717-A — exact universal six-state histogram

For every integer m>=1, write E_m=N_m(e), T_m=N_m(tau) for **each** of the three transpositions, and C_m=N_m(c) for **each** of the two 3-cycles. Then:

    120 E_m = 9^m + 10*6^m + 15*3^m + 18*2^m + 9*(-1)^m + 47*(-3)^m
    120 T_m = 9^m - 5*3^m + 9*(-1)^m - 5*(-3)^m
    120 C_m = 9^m - 5*6^m + 15*3^m - 9*2^m + 9*(-1)^m - (-3)^m.

The exact total number of returning positive BRC branches is

    R_m = E_m + 3*T_m + 2*C_m
        = (9^m + 5*3^m + 9*(-1)^m + 5*(-3)^m)/20.

At m=0 there is exactly one empty identity history and none of the other five; m=0 is an explicit boundary case because the lift adjacency also has a zero eigenvalue.

**Proof and full finite certificate.** Lift the 20 unordered triads to all 120 *ordered* triples of distinct native axis labels. Let A be the 120x120 integer adjacency matrix: A[u,v]=1 iff v differs from u in one named slot, replacing that slot's axis with any of the other three axes not in u. Each vertex has exactly 9 neighbours. A is symmetric and connected; the companion Python verifier constructs and checks every row.

Every J(6,3) edge has exactly one successor from an ordered lift. If v(h) is the final ordered triple such that v(h)[h(i)]=i, the path lifting bijection gives

    N_m(h) = (A^m)[ (0,1,2), v(h) ].

The verifier explicitly constructs I,A,...,A^7 with exact integers and confirms **all 14,400 entries** of the operator identity

    P(A) = 0,
    P(x) = x(x+1)(x+3)(x-2)(x-3)(x-6)(x-9)
         = x^7 - 16x^6 + 58x^5 + 120x^4 - 711x^3 + 216x^2 + 972x.

This is an exhaustive finite proof certificate for one fixed matrix, not a sampled large-m assertion. Thus every matrix-entry sequence satisfies the same seventh-order linear recurrence at every m. The seven characteristic roots are distinct: (9,6,3,2,0,-1,-3). Its first seven exact terms determine the unique exponential coefficients by an invertible Vandermonde system. Direct integer transition DP supplies those terms.

The coefficients for each conjugacy class, in the stated root order, are:

| class / root | 9 | 6 | 3 | 2 | 0 | -1 | -3 |
|---|---:|---:|---:|---:|---:|---:|---:|
| e | 1/120 | 1/12 | 1/8 | 3/20 | 1/6 | 3/40 | 47/120 |
| each transposition | 1/120 | 0 | -1/24 | 0 | 0 | 3/40 | -1/24 |
| each three-cycle | 1/120 | -1/24 | 1/8 | -3/40 | -1/12 | 3/40 | -1/120 |

All exact initial entries are also checked by the companion source. Equality of the three transposition columns and of the two cycle columns follows from conjugating root axes by their label permutations (the full 6-axis edge relation is equivariant). For positive m the 0^m column vanishes, giving the displayed universal formulas. The linear recurrence and seven initial values prove all positive m simultaneously. QED, conditional only on the fully executable fixed finite matrix lemma checked by the included source.

For example:
m=2: (E,T,C)=(9,0,0);
m=3: (18,6,0);
m=4: (207,48,9);
m=5: (1080,492,198).
Here T and C denote counts **per individual** group element, not their aggregate classes.

## 3. Theorem R717-B — minimal universal cover length is four

Define H_m={h: N_m(h)>0}. The complete classification is

    H_1=empty,
    H_2={e},
    H_3={e, three transpositions},
    H_m=S3 for every integer m>=4.

Indeed the exact formula yields positive counts for all six h at both m=4 and m=5, and the attached JSON lists six explicit paths for each length. To extend a rooted path by two edges, append at the root the native admissible excursion 012->013->012. The two replacements act on the same slot and their product is identity; consequently all six outcomes persist at every length m+2. Starting from four and five proves the assertion for all m>=4. QED.

The permutation parity of h is independent of m parity. In particular at m=3 there are both identity and transposition loops; at m=4 all six elements already occur. The earlier R709b three-element even-h family was an explicit proper subset of this larger positive BRC carrier.

## 4. Theorem R717-C — same optimal event schedule, six different pointed future outcomes

Fix an arbitrary closed m-step path W with m>=4 and set up one **labelled m-Cell physical ring**, with each Cell i initially bearing the active triad T_i. Every Cell also carries two token inventories n_i^+=n_i^-=1 and matching typed ports. The declared R709b candidate gate on edge (i,i+1) uses the **old** state and fires iff neighbours are Johnson-adjacent and the appropriate right + and left - source tokens are present. For each firing, post one right-to-left positive typed + occurrence and one left-to-right positive typed - occurrence. All gates and active triads are frozen for the macrostep, then the V20 old-neighbour copy is committed simultaneously.

The all-adjacent cyclic word and uniform inventories imply, inductively for every integer t>=0,

    fire_i(t)=true,
    n_i^+(t)=n_i^-(t)=1,
    X_i(t)=T_(i+t mod m).

Thus Cell 0 follows W in its first m macrosteps and returns to the root while carrying exactly the path's pointed h. All six witnesses share this same physical ring and gate, and after m macrosteps their complete V29-style positive port counters (each species Rin=Rout=m at each Cell) and the signed physical net current are equal.

Make the transfer ordering concrete by using the **same phase-pair word for every initial field**, independently of the target h. On each physical edge the earlier phase transfers + from right to left and the later phase transfers - from left to right.

For even m>=4 use the four-phase pair word

    12,34,12,34,... (m/2 repeats);

for odd m>=5 set a=floor((m-1)/4), b=(m-1)/2-a and use the five-phase word

    (12,34)^a, 15, (23,45)^b.

Every two adjacent edges have disjoint phase sets, including wrap-around; no Cell is incident to more than one elementary event in a phase. Each source sends at most one token of a given type in a macrostep and initially has that token, so token stocks never become negative at the intermediate boundaries. After all stages the stocks return to one and the frozen triads shift.

At boundaries the time-indexed signed physical-edge current vector is **entirely determined by the phase-pair word**. Therefore it is the same edge-by-edge and time-by-time for all six differing BRC root paths, not just the final aggregate current. The absolute temporal residual profile D is:

    even m: D=(m/2, 0, m/2, 0),
    odd m:  D=(a+1,b+1,a+1,b+1,0).

The execution requires exactly four phases when m is even and five when m is odd; R711 supplies sharp capacity lower bounds. The odd schedule also attains simultaneously the sharp total residual m+3 and sharp peak ceil((m+3)/4) from R712. The even displayed schedule has residual area m (each physical edge must be unmatched across at least one phase boundary) and peak m/2 (within this four-stage edge-pair construction).

**Observer fiber and minimum information.** Suppose the observer retains the root and final triad 012, physical ring topology, all stocks, full completed positive port counters and **the entire signed microphase-current history**, but does not retain the original joint triad field or rooted BRC path ordering. For any m>=4 the same retained observation arises from all six distinct pointed S3 outcomes. Hence the smallest worst-case fixed-length encoding that restores h needs precisely

    ceil(log2 6)=3 bits.

It is sufficient to encode one of the six h values, and necessary because fewer than three binary bits have fewer than six messages. This is an exact observer-specific residual-fiber result; retaining the joint triad field makes the observer strictly more informative. QED.

**Native interface boundary:** local conserved inventory, automatic stock gate and four/five-phase frozen prepare/commit timing are the explicit **candidate extension** made in R709b/R711, not a claimed replacement for every frozen native Link/Port permission. Native six-axis adjacency and V17 slot transport are exact source interfaces; matching this candidate scheduler to native Link/Port execution timing is the next testable question. The spatial X6 affine torsor coordinates are not collapsed into a slot label.

## 5. Theorem R717-D — exact mixing rate for positive path counting

Normalize returned positive unit BRC branches by their total number R_m, letting P_m(h)=N_m(h)/R_m for m>=2. This defines a **counting measure** over a specified finite path population, not a physical stochastic scheduler.

From the exact formulas and R_m=9^m/20+O(3^m), the leading deviation coefficients for identity, each transposition, and each three-cycle are respectively +5/3, zero, -5/6 times (2/3)^m. Hence

    P_m(e)=1/6+(5/3)(2/3)^m+O((1/3)^m),
    P_m(each transposition)=1/6+O((1/3)^m),
    P_m(each three-cycle)=1/6-(5/6)(2/3)^m+O((1/3)^m).

Summing absolute deviations over all six h yields the sharp total-variation asymptotic

    TV(P_m,Uniform(S3))=(5/3)(2/3)^m+O((1/3)^m),
    lim_(m->infinity) TV(P_m,Uniform(S3))^(1/m)=2/3.

The coefficient of 6^m is 1/12 for e, zero for transpositions and -1/24 for each three-cycle. This coefficient split supplies the exact leading term. QED.

## 6. Reproducible certificate and evidence classification

Companion Python script: R717_X6_S3_COVER_VERIFY.py. Run with Python standard library; it constructs all 120 ordered-triad states, checks the nine neighbours, symmetry and connectivity, verifies all 14,400 entries of P(A)=0 by exact integer multiplication, checks class-by-class histogram identities for m=0..60 (the formula itself is for m>=1), constructs six explicit closed paths for each of m=4 and m=5, and simulates all six variants at every m=4..33 with actual frozen-gated stock conservation and four/five microphases. The attached JSON records the nontrivial witnesses and numerical evidence. Exact local run result:

    R717_EXACT_X6_LIFT_S3_SPECTRAL_AND_PHASE_FIBER_PASS.

**Reuse status:** COMPOSE_APPLIED. BRC source-labelled paths and native V17 transport were used directly; R709b counterflow model and R711/R712 phase certificates were composed within their explicit scope. The 120-state ordered-triad adjacency is a finite representation of the same native path-formal carrier, not an independently claimed top-level BRC algebra. The finite operator matrix has a universal mathematical consequence for all m because it annihilates the transition operator, not because an arbitrary finite sample is extrapolated.

Independent mathematical Review: UNREVIEWED. Formal native CLAIM/Result: NOT AUTHORED by this independently published research. Physical heartbeat and Link/Port deployment: NOT ASSERTED.

## 7. Next discriminating research question

Read frozen current-science Link/Port admissibility and V29 event time semantics at exact immutable input pin. Test the length-four identity and both parities with these concrete phase assignments. If the native interface rejects an event combination, remove exactly the forbidden events or add the smallest justified typed prepare/commit extension; compute the resulting restricted reachable h states and new exact transfer operator. Preserve original positive source labels and time-indexed signed-current observations so any loss of coverage can be traced to the specific native rule.
