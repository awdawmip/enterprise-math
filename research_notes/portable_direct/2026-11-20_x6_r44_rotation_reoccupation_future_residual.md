# X6 R44 — Provenance-sensitive rotation reoccupies a shared Cell: exact BRC history count and future-language repair

Date: 2026-11-20 (Asia/Shanghai). Task lineage: RS-X6-NATIVE-TIME-DYNAMICS; Researcher: EM-X6-214D9C; historical Activity: RA-545183ADD4EF71C3E4698AEE.
Status: CONDITIONAL_AUTHOR_PROOF / EXACT_FINITE_LABELLED_BRC_PASS / NOT_INDEPENDENTLY_REVIEWED. An independently preserved portable research return, not a new native CLAIM, Result or accepted physical law.

## Frozen inputs and scientific purpose

Preserve the task-frozen P000 V5 at awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389, including p000_reality_foundation.json, definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md, definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json; use the six-dimensional affine X6 Cell torsor, chosen Cell anchor and source/Port/signed-frame provenance. Original input pins are not rebased to current main.

Direct predecessor: R42 port-sensitive resource conflict and R43 releasable shared-target theorem (research_notes/portable_direct/2026-11-20_x6_r43_releasable_target_future_memory.md, immutable commit 61002d21919f955b4c27a20cbc06133d278c0fdb). R43 proved that for three named Ports the immediate enabled-event mask happens to suffice for its specific release law. The next discriminating question is whether a lawful *candidate* history-sensitive reorientation can make two states with identical currently enabled masks have different complete future named-event languages.

## Definition of the conditional R44 carrier

Two named sources A and B each carry one indivisible ordered primitive three-force frame satisfying the declared P000 three-force closure type. Each may execute exactly one whole-frame transfer through one of p named Port alternatives, where p>=1. Port 0 of A and Port 0 of B target the same chosen Cell c; all other targets are distinct. p=3 is the three-Port candidate geometry of R42; p=1,2 restrict available Ports, and p>3 only stress-tests the finite combinatorics, without asserting extra native primitive Ports.

A state is (a,b,o,t), where a,b in {-1,0,...,p-1} record the used Port (-1 means unused), o in {0,A,B} is the current occupant of the shared Cell (0 is empty), and t in {0,1} records whether the candidate reorientation has been used. Initial state (-1,-1,0,0). All event labels are public and source/Port named. The positive BRC branch carrier is the set of successful serial event words, coefficient +1 per labelled word; no phases, cancellations or amplitudes are assigned.

Port transfer Xi (X=A or B): requires X unused and, if i=0, c empty; consumes the complete X triad; fills c iff i=0. For i>0, occupancy is preserved. Public clearing event R: enabled iff c occupied; empties c without resetting either source or t. Candidate rotation/reorientation T: enabled iff exactly one source has fired, c is currently empty, and t=0. It sets t=1; when the fired source originally used Port 0, its previously released Link projection reoccupies c (occupant becomes that source); when it originally used another Port, c stays empty. T does not fire another triad and is not declared an independently admitted physical heartbeat. Each T occurs at most once.

All event words are ordered changes with their own event-count clock. Refinement/precision address is held fixed in this candidate, and no event count is identified with calibrated duration or a physical heartbeat.

## Theorem R44.1 — Closed positive BRC word and state counts

For every integer p>=1, let W_h(p) be the number of successful named event words of exactly h events, including the empty word. Then

~~~text
h                    0      1           2                  3                  4       5       6
W_h(p)               1      2p    2p^2+2(p-1)       2p^2+4p-2              4p      4p-2     2
W_h(p)=0 for h>6
Total successful BRC words = 4p^2+16p-3.
Reachable decorated states = 2p^2+8p+5.
~~~

Proof of the word polynomial. Words without T are precisely R43: (1,2p,2p^2,6p-4,2) at h=0,...,4. In a word containing T, the first source either uses a nonshared Port i>0 or Port 0. In the former case, the unique T must follow that first event immediately; the other source may then choose one of p Ports, and a final R is possible only if its choice was Port 0. These yield 2(p-1) words of length 2, 2p(p-1) of length 3 and 2(p-1) of length 4. If the first source chooses Port 0, R must clear its target before T, so all words begin X0 R T. They can terminate at length 3 (2 words); next either the second source takes one of p-1 nonshared Ports and can be followed by R, or an R clears the T-produced occupation and then the second source selects any Port, optionally followed by R iff it chose Port 0. Contributions are length 3:2, length 4:2(p-1)+2, length 5:2(p-1)+2p, length 6:2. Add the two cases and the R43 words to obtain the formula. The finite event bound follows because each source fires once, T fires once, and any R must clear a prior Port-0 or T occupation.

Proof of the state count. All states with t=0 are precisely the (p+1)(p+3) R43 states. With t=1 and exactly one source used, each named used source has two states for its original Port 0 (c reoccupied/cleared), plus p-1 nonshared original Ports with c empty: 2(p+1) states total. With t=1 and both sources used, cases with neither Port 0 contribute (p-1)^2 states, exactly one Port 0 contributes 4(p-1) occupied/cleared states, and both Port 0 contributes the two possible final occupants plus the cleared state (3). Thus t=1 adds 2(p+1)+(p-1)^2+4(p-1)+3=p^2+4p+2 states. All are reachable by the legal event cases just described; sum with the t=0 count gives 2p^2+8p+5.

## Theorem R44.2 — Full future-language quotient and one-step-mask failure

For every p>=2, the complete future named-successful-word observer has exactly 13 minimal deterministic Markov classes, although there are only nine distinct immediate enabled-event masks. At p=1 there are 11 future classes and seven enabled masks. Therefore the minimal fixed-length full-future index uses 4 bits for every p>=1 (ceil(log2 11)=ceil(log2 13)=4). This improves neither the path multiplicity observer nor the full decorated-state observer without a separate certificate.

Proof and explicit quotient. The initial state is one class. Once both sources have fired, all used-Port histories collapse, for this future-word observer, to two classes distinguished by whether R remains enabled (occupied / clear). For exactly one fired source X, five classes exist when p>=2:

~~~text
O_before: occupied, t=0; remaining-source nonshared Ports and R enabled
O_after:  occupied, t=1; same immediate mask, but R no longer enables T
C0_before: clear, t=0, X originally used Port 0; other source's p Ports and T enabled
Cn_before: clear, t=0, X originally used a nonzero Port; same immediate mask
C_after:  clear, t=1; remaining source's p Ports enabled, T disabled
~~~

These classes are closed under all named events, since transitions depend only on the class. O_before and O_after differ by a suffix R T; C0_before and Cn_before differ by T Y0, where Y is the remaining source; C_after differs by immediate event T. Occupied/clear classes have different immediate masks, as do states with different remaining named source whenever p>=2. Once both sources have fired, the enabled set is {R} or empty, distinct from one-fired classes at p>=2. The initial state enables both A and B actions. Consequently the displayed 1+5+5+2=13 classes are pairwise distinguishable and form an exact transition congruence. If p=1, the Cn_before class is absent for each used source; 1+4+4+2=11. This proves minimality and the enabled-mask count.

Explicit three-Port counterexample. Compare successful histories s=A0 R and u=A1. At both endpoints A is spent, B is unused, c is empty and T is unused, so the immediate enabled mask is exactly {B0,B1,B2,T} at both states. Both permit the single event T. But after T, s has c reoccupied by A and forbids B0, whereas u leaves c empty and permits B0. Hence the shortest distinguishing future word is precisely T B0, of length two. Under R43's purely clearing transition law the same two states had identical complete future languages. The new difference is a structural source/Port-memory residual activated by a public reorientation event, not numerical error.

## Exact verification, input-to-output scope and open native bridge

Program: research_notes/portable_direct/x6_r44_rotation_reoccupation_brc_verify.js; results: research_notes/portable_direct/x6_r44_rotation_reoccupation_brc_results.json. Run with Node.js to enumerate the complete reachable state graph, all successful positive labelled BRC words, and all suffix languages for each p=1,...,8. The test independently constructs the language partition using explicit complete suffix sets and transition-refinement classes, checks every ordered pair, verifies both closed-form theorems, and checks the concrete T B0 witness. No floating-point arithmetic, pi/trigonometry, negative-mass cancellation, classical phase evolution or approximation is used. General p claims rest on the combinatorial proofs; the executable finite evidence covers precisely p=1,...,8.

The model gives a sharp **conditional counterexample to sufficiency of a current Port-admission mask**, including p=3, even when source three-force frames remain atomic. Whether a real P000 TRIADIC_CLOSURE_E event admits R or this T reorientation remains an open physical bridge; this proof neither changes the frozen P000 nor licenses a native temporal, physical-duration, or amplitude claim.

Next: extract actual Cell/Link/Port rotation-response rules and certify an event- and provenance-preserving map from the frozen-native triadic update graph to this carrier (or prove a specific obstruction). Then test whether true native futures distinguish the R44 pair. Retain R42/R43 provenance; do not repeat their word enumeration or claim a formal Task Result/Review.
