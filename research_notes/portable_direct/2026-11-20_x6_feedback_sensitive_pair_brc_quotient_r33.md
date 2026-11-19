# X6 R33 — Feedback-sensitive probes: exact pair-product Boolean-BRC future quotient

Status: CONDITIONAL_AUTHOR_PROOF / EXACT_FINITE_CHECK_PASS / NOT_REVIEWED  
Date: 2026-11-20 (Asia/Shanghai)  
Task: RS-X6-NATIVE-TIME-DYNAMICS; publication TP2-91D4A7C2F63805BE21A3  
Researcher: EM-X6-214D9C; original session MCP-d467c19ce42d4d7fa65a3901db1cf6b2; Activity RA-545183ADD4EF71C3E4698AEE  
Frozen P000 scientific pin: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json (V5).  
Predecessor: R32 phase-coupled public Link quotient, source blob f578812209e7e27cad49736e28ec5de18d6ababd.

## 1. Exact finite feedback model

Let Θ be a finite set of preserved hidden provenance histories, S a finite set of complete public/operational states (named Cell, source phases, probe-used flags, Link state, ledger when necessary), and Σ a finite alphabet of fully named ordered source/Port events. For each θ and label a, T_θ(-,a):S⇀S is a deterministic partial transition preserving θ. A successful word is one for which every transition exists; the empty word succeeds. L_h(θ;s) denotes successful words of length at most h from a fixed common initial state s, and L_∞ denotes all finite successful words. The event model is conditional; native TRIADIC_CLOSURE_E admission remains a separate mapping question.

## 2. Exact pair-product theorem

For θ,η, form the common-prefix graph on S×S. A label a gives an edge (u,v)→(T_θ(u,a),T_η(v,a)) when both transitions exist. A pair is mismatched by a if exactly one transition exists. Let r(θ,η;s) be the minimum number of common edges from (s,s) to any mismatched pair, or infinity when none exists. Then the shortest distinguishing successful word length is

\[
\boxed{\delta_s(\theta,\eta)=r(\theta,\eta;s)+1,\qquad
L_h(\theta;s)=L_h(\eta;s)\ \Longleftrightarrow\ \delta_s(\theta,\eta)>h.}
\]

Here infinity plus one remains infinity. The minimal classes for the *initial public fiber* are Θ modulo this exact language equivalence. Their optimal fixed-length hidden-history storage is \(\lceil\log_2 C_h(s)\rceil\), where \(C_h(s)\) counts classes. If at most M reachable common-prefix pair states exist, every finite shortest distinction has length at most M. In particular, if \(|S|\le N\), then \(\delta\le N^2\) whenever finite, and \(\sim_h=\sim_\infty\) for \(h\ge N^2\).

**Proof.** Choose a shortest word lying in the symmetric difference of the two success languages. Its proper prefix succeeds under both histories, whereas its final letter is enabled on exactly one side. Thus that proper prefix reaches a mismatched pair in the common-prefix graph. Conversely a common-prefix path followed by a mismatch letter succeeds on precisely one side. Breadth-first search computes the shortest such word. If a shortest pair path repeated a pair, deleting the intervening cycle would leave a shorter path to the same mismatch; thus its length is at most M−1, and adding the final letter yields M. Since equality of successful word sets is an equivalence relation, BFS defines a partition, and an index per distinct class attains the information lower bound. QED.

This theorem permits feedback probes, history-dependent public updates, and shared ledger transitions as long as they are encoded in complete finite states. At a bounded observation horizon the quotient is a graded time-to-go representation; an ungraded Markov claim requires a separate transition-congruence test.

## 3. Two-source feedback counterexample to extrapolating R32

Take two named intact triadic carriers already in preparation phase 2. Both one-use probes are unused. The public Link bits initially are x_0=0,x_1=1 and hidden provenance bits θ_0,θ_1∈{0,1}. Event Q_0 is enabled iff θ_0=1, marks Q_0 used and *resets x_1 to zero*. Event Q_1 is enabled iff θ_1=1 or x_1=1 and marks Q_1 used. No other events exist. All event labels carry their source identity.

At h=0, all four histories are equivalent. At h=1, histories group by θ_0, giving two classes. At h≥2 the exact classes are

\[
\boxed{\{(0,0),(0,1)\},\quad\{(1,0)\},\quad\{(1,1)\},\qquad C_h=3.}
\]

The two histories with θ_0=0 are permanently indistinguishable: Q_0 is unavailable and Q_1 remains publicly enabled regardless of θ_1. With θ_0=1, the word Q_0Q_1 succeeds exactly when θ_1=1. Thus it is a shortest two-event witness for (1,1) versus (1,0). Fixed-length information is 0,1,2 bits at horizons 0,1,≥2 respectively. The three classes **cannot** be fibers of projection onto any fixed subset of the two raw source bits (which would give 1,2 or 4 classes).

R32's *nonprobe-only* unmask distances here give D_0=0 and D_1=infinity, leading to only two classes if its formula were applied beyond its inert-probe hypothesis. Removing an earlier Q_0 from the common prefix is no longer legal because Q_0 changes the Q_1 Link guard. This is a scoped counterexample to that generalization, not to the R32 theorem.

## 4. Reproducible evidence

The accompanying exact Boolean-BRC JavaScript independently implements (i) common-prefix pair-product shortest-divergence BFS and (ii) direct enumeration of complete successful labelled word languages. It checks all 4 hidden histories and all 6 unordered pairs for depths 0–4 in the feedback construction. It also generates 96 reproducible seeded deterministic partial controllers, each with 3 public states, two event labels and 4 hidden histories, and verifies all 576 history pairs by direct enumeration through N²=9 events. These tests check implementation and a finite family; the unrestricted finite-controller statement follows from the symbolic proof above.

Evidence: x6_feedback_product_brc_verify_r33.js and x6_feedback_product_brc_results_r33.json in this directory.

## 5. Current scientific boundary and next step

To admit a true P000 TRIADIC_CLOSURE_E event, first specify the complete whole-triad native event: three-force closure witness, six-axis Cell update, rotation/frame, signed Port identity and order, Link/ledger updates, provenance/multiplicity and observable trace. Compare its actual enabled labels with T_θ and construct a trace-preserving representation before using this quotient as an original native-time law. Next: measure the state/information cost of shared-resource or multi-source feedback, and separately compare event count, periodic phase and precision-refinement clocks in the preserved taskbook. P000 remains unchanged, and this conditional result has no independent Review.