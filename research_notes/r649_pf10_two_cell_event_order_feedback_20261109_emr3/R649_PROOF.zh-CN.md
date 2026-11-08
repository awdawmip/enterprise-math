# R649｜双 Cell TRANSFER 事件顺序反馈碰撞与有限状态闭合

Date: 2026-11-09 (Asia/Shanghai). Mode: author-side TASK-related exact auxiliary model research; not formally CLAIMed or independently reviewed.
Frozen input: signed BRC R462@18783e01e3646c72b7aab3b16d3f565e83e6446f. Typed source: V29 and V26/V27/V17@b62110008321d9147212cb89f2627ff613c2550d.
Direct source code: experiments/x6_network_event_ledger_v29_20260906/check_network_event_ledger.py (blob 2a67e8d4c79912147e0bd1c036065152792e6877); experiments/x6_dynamic_law_holonomy_v24_20260906/check_channel_circulation_bridge.py (blob 5618dae00632f9f796d3f5a6a692c248ea699131).
Predecessor: R648@99ee3bcd7bd790faf4f4494ca32560e6966a1226. P000, X6 axis/port distinction and ACTIVE worldview retained.

## 1. Concrete time-ordered auxiliary coupling

Take two distinct typed X6 Cells x,y, each with four declared internal PF10 ports 0,1,2,3. Assume an allowed x→y transfer link; this is an explicit interface premise, not a derivation of native Cell adjacency. The 6 axis labels index the 20 active triads, while the 4 port labels index PF10 fields; they are separate types.

Each Cell contains the original V29 nonnegative M, rin, rout. Define u=M1−Mᵀ1+rin−rout, Ω=M−Mᵀ, c(S) the original V23 four-field code, and for each adjacent triad T sharing two axes with S the exact V27 signed integer score:

Φ(S,T)=uᵀc(T)+c(S)ᵀΩc(T).

A single auxiliary update is explicitly ordered:
(a) perform one legal labeled V29 TRANSFER(x,a,y,b);
(b) independently at each of x and y calculate V27 scores from its *new* ledger, require a unique maximizing neighbor T, and replace current S by T;
(c) transport the three V17 slots: common members preserve their slot, arriving member inherits the departing member’s slot.

This is a concrete compositional test of three source-defined operators, not a claim that the source already prescribes this event-to-triad timing.

For a directed link, R648 adds the nine counters Z_ab=N_ab for a,b<3, allowing recovery of all 16 cumulative source/target pair counts N from the original row/column margins. These counters are retained in both histories below.

## 2. Exact two-event counterexample

Set the nonnegative internal PASS seed on x to M_x=E_{3,0}; set M_y=3(E_{0,1}+E_{2,0}+E_{2,3}+E_{3,0}). All rin,rout start zero. Initial active triads for both Cells are S0=(0,1,2), with slot identity 0→0,1→1,2→2.

Let e=TRANSFER(x,0,y,0) and f=TRANSFER(x,1,y,1).

Compare A=(e,f) and B=(f,e). Both histories contain one e and one f. Their final complete V29 M,rin,rout fields are IDENTICAL in each Cell, including after the entire coupled evolution; all derived (u,Ω) are therefore identical. The full ordered-pair *count matrix* N^xy is also identical: N_00=N_11=1, all other entries zero; hence the additional R648 9+9 counters also agree.

Nevertheless, source-rule exact score calculations at the intermediate prefixes give:

| History | Cell | Step 1: winner, unique gap | Step 2: winner, unique gap | Final (triad; slots in sorted triad order) |
|---|---|---|---|---|
| e then f | x | 025, gap 1 | 012, gap 1 | (012; 0,1,2) |
| f then e | x | 123, gap 1 | 135, gap 1 | (135; 1,0,2) |
| e then f | y | 024, gap 3 | 124, gap 1 | (124; 0,2,1) |
| f then e | y | 024, gap 2 | 124, gap 1 | (124; 0,2,1) |

All eight selected maxima are strict among the nine legal adjacent triads. Both histories conserve the total charge Σ_cΣ_i u_{c,i}=0 after each TRANSFER, and their V29 counters are nonnegative.

Consequently, a summary consisting only of the **entire final V29 ledgers together with the exact R648 source-pair count matrices** fails to recover the endpoint of this proposed ordered V29→V27→V17 observer. The failure occurs at two events. For this fixed seed and prescribed multiset {e,f}, an added binary variable distinguishing the two orders is necessary and sufficient to recover the two possible endpoint outputs (exactly one bit of finite information). It is not a global one-bit bound for arbitrary-length histories.

The lower bound on counterexample length is exact: with zero or one TRANSFER, the event history is determined from its event multiset (and one transfer also from its unique source/target row/column nonzero positions). Thus no order collision exists with fewer than two events in this model.

## 3. Full-state finite repair and future-update theorem

Let each Cell additionally retain its **current** active triad S_c and bijective slot map σ_c:S_c→{0,1,2}. Define

Q=(complete V29 Cell ledgers, Z^{xy},Z^{yx}, (S_x,σ_x), (S_y,σ_y)).

For every incoming *labeled, authorized* V29 PASS or TRANSFER, and where the indicated V27 maxima are unique, Q deterministically specifies its next Q under the explicit event-first protocol (with the declared set of Cells updated after each event). Proof: V29 and Z increments depend only on the event label; u and Ω are functions of the resulting ledgers; the nine candidate scores use only the local current S and those integers; the unique maximizer determines T; and source V17 slot inheritance is a deterministic function of (S,σ,T). Induction gives closure under every finite such event word.

For two Cells there are at most 120² possibilities of the pair of triad-slot states, conditional on the stored ledger/paired counts. This is an **upper bound** for this state extension, not a reachability/minimality claim for the actual eventwise network. Other source-sensitive feedback may additionally require history or reservoir data specified by its own interface.

For any observer that asks only for the current V27 next-score and can ignore V17 output, the current triad S plus (u,Ω) already suffices at a fixed Cell and event boundary; for observers asking exact V17 slots, the slot map is retained. This preserves the dependency-directed residual principle.

## 4. Exact independent finite verification

R649_VERIFY.py recreates the declared source V23 code and V27 integer scoring, source V29 per-event increments, R648 3×3 paired reconstruction, and V17 slot inheritance; does not use floating point. It checks both witness words including all strict score gaps and full-ledger equality, then examines every x-seed count vector in {0,1,2,3}^4 (256 choices), every pair of distinct x send ports (6 choices), the two event orders with receivers fixed to 0 and 1, and y-seed=(3,3,3,3). That finite domain has 1,536 unordered seeded/event-pair cases. The exact checker finds 416 cases strict along both two-step histories and 30 of these with different endpoint augmented states.

The algebraic proof of deterministic Q update is valid for arbitrary finite event words satisfying the stated unique-max and event-authorization premises; the 1,536-case search establishes only the declared bounded classification.

Expected marker: R649_TWO_CELL_ORDER_FEEDBACK_COLLISION_PASS.

## 5. Remaining research problem

Obtain an actually registered X6 adjacency and permission relation for transfer between chosen native Cell addresses, and a source-admitted timing/coupling law (which Cells perform triad updates after each event). Then test whether the finite Q is sufficient for the physical observer family or whether one must carry further network inventories or route-dependent memory. Compare a genuinely local event selector with R647's B-only controller. Formal Source Owner/CLAIM, independent Driver and admission retain their distinct routes.