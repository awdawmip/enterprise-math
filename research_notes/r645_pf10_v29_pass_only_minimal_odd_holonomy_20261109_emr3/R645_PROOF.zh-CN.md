# R645｜V29纯PASS四事件奇holonomy：严格最小构造

Date: 2026-11-09 (Asia/Shanghai)
Status: AUTHOR_SIDE_EXACT_FINITE_CLASSIFICATION / UNREVIEWED / NOT_ADMITTED
Task: RS-X6-GLOBAL-TRIADIC-FIELD-NETWORK-LAW (author-side unit; formal CLAIM not asserted)

## 1. Exact scientific input and change from R644

Source V23/V26/V27/V17 and V29 at Enterprise Math b62110008321d9147212cb89f2627ff613c2550d; frozen signed BRC R462@18783e01e3646c72b7aab3b16d3f565e83e6446f. R644@d33317e4fbf70949f758db5b20ac4defe3b53892 required five V29 events to realize its *particular* 3-cycle M=C and residual transfer bias. Here the target ledger class changes: a single Cell, only internal PASS events, Rin=Rout=0, no inter-Cell transfer. Four internal ports are independently typed from six native X6 spatial axes, with 20 selectable three-axis subsets (not Cell addresses).

V29: PASS(x;a→b) increments the nonnegative integer M_ab by one. Define I=M1, O=Mᵀ1, u=I−O, Ω=M−Mᵀ. With Rin=Rout=0, u=Ω1. Every PASS preserves the scalar Q=1ᵀu=0 exactly. For active triads S,T of three distinct members of {0,...,5}, adjacency is |S∩T|=2, nine choices per S. V23 assigns each S its four-component matching code c(S)∈{−1,0,1}⁴. Use precisely V27's signed score

Φ(S,T)=u·c(T)+c(S)ᵀΩc(T).

The protocol selects the unique argmax among the nine neighbors, else the path is not classified as a strictly determined trajectory. V17 carries both shared-member slots unchanged and transfers the departing member's slot to the entering member.

## 2. Four source-defined primitive events and exact odd three-cycle

Start with M=Rin=Rout=0 at one Cell x. Apply:

PASS(x;0→1); PASS(x;2→0); PASS(x;2→3); PASS(x;3→0).

The exact resulting nonnegative count state is

M=[[0,1,0,0],[0,0,0,0],[1,0,0,1],[1,0,0,0]],
I=(1,0,2,1), O=(2,1,0,1), u=(-1,-1,2,0),
Ω=[[0,1,-1,-1],[-1,0,0,0],[1,0,0,1],[1,0,-1,0]].

Each of the four actual V29 primitive events leaves Q=0. Complete nine-neighbor integer scoring gives:

| Current S | Unique winner T | Winning score | Second highest | Gap |
|---|---|---:|---:|---:|
| 012 | 024 | 1 | 0 | 1 |
| 024 | 124 | 2 | 1 | 1 |
| 124 | 012 | 5 | 2 | 3 |

Thus the exact cyclic trajectory is 012→024→124→012, with V17 shared-slot holonomy (1,0,2), an odd transposition. This is a closed three-step cycle from the prescribed starting triad, with no warmup step and no boundary transfer.

## 3. Sharp bounded theorem: minimum four PASS

Define the search class: one Cell initially zero, at most n internal PASS events, Rin=Rout=0, any initial active triad among all 20. A strictly determined orbit requires a *unique* V27 winner at every step until the first repeated triad; its eventual cycle must have odd V17 slot holonomy. No arbitrary tie-break is permitted.

Only 12 distinct off-diagonal PASS types can affect (u,Ω). A diagonal PASS(a→a) modifies only M_aa and leaves (u,Ω), all scores and all holonomies unchanged, so deleting such events cannot increase the minimum. A multiset of n off-diagonal types completely determines (u,Ω) and hence this observer's entire orbit; there are exactly binomial(11+n,n) such multisets.

Every strict deterministic path visits at most 20 distinct triads before the first repeat. For each of the binomial(11+n,n) multisets, the reproducible Python program checks all 20 starting triads and all nine neighbor scores at every visited vertex, stopping at a tie or the first repeated vertex and checking the exact S3 slot permutation. The exhaustion is exact integer arithmetic, no floating point.

| n | Complete multisets | Strict ultimately periodic orbits (over 20 starts) | Odd holonomy orbits |
|---:|---:|---:|---:|
| 0 | 1 | 0 | 0 |
| 1 | 12 | 0 | 0 |
| 2 | 78 | 0 | 0 |
| 3 | 364 | 0 | 0 |
| 4 | 1365 | 168 | 60 |

Exactly two n=4 seed choices give an immediately closed odd orbit from initial S=012. The displayed witness is one of those. Consequently the sharp minimum is FOUR events for the stated PASS-only, unique-winner, single-Cell V23/V27/V29 observer, regardless of initial triad.

This is not a refutation of R644's five-event bound for its *different prescribed target ledger* and transfer residuals.

## 4. All-index conservative integer dynamics (packet protocol explicitly proposed)

The V29 source specifies event increments but *does not* prescribe an autonomous event scheduler. The following is a precise auxiliary packet-boundary coupling, not a source-native physical-time law: after selecting each unique best neighbor, append the same ordered four PASS events as a packet.

Starting with the above four-event seed M₀=M, induction yields for all n≥0

Mₙ=(n+1)M, uₙ=(n+1)u, Ωₙ=(n+1)Ω.

V27 score is linear in u and Ω, so each candidate score scales by n+1. The winning three-cycle survives for all n with gaps (n+1)·(1,1,3), hence every third triad-selection step yields the odd permutation (1,0,2), and every sixth step returns the original slot assignment. Q remains exactly zero after every primitive PASS, while stored counts increase and native event order remains distinct from this quotient. The code checks 151 consecutive packet boundaries; the homogeneity argument proves all n.

## 5. Remaining task and interpretation

This supplies a sharper local zero-Q seed (four PASS, zero TRANSFER) than the previous five-event *different target* construction. The exact certificate is about the source-defined V29 primitives and V27/V17 observer under a stated packet scheduler. Open next: construct or disprove a truly local, per-primitive-event event-choice/triad-choice law, with multi-Cell entry continuity, native X6 Cell legality, covariance, retained ordered S3 history and physical inventory/energy assumptions where relevant. Neither finite network update-law closure nor Driver admission is claimed.

Reproduce exactly with Python standard library: python3 R645_VERIFY.py > recomputed.json. Expected marker: R645_V29_PASS_ONLY_FOUR_EVENT_ODD_HOLONOMY_EXACT_PASS. Full enumeration evidence: R645_EVIDENCE.json.