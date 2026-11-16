# R762CH — Full X6 closed-path pair-area carrier and frame-change obstruction

**Task lineage:** RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142; frozen P000 science `a72226e2430ffa4786321ac86e7f0c599d5f0389`. **Predecessor:** R762CG, PR #2570@80bc435f773b87db000630898b829137f3831f6f. **Evidence:** author-side exact Python checks; **independent review:** NOT_REVIEWED.

## Question and typed model

R762CG supplies three rooted oriented-area residues for one fixed signed three-Port frame and explicitly keeps the register rule across Port replacement separate from a globally path-derived area. Here we determine the exact information needed if an observer may later choose *different* Port frames and inquire about the ordered-path area of their rooted pairs.

Fix a chart anchor on the full native X6 Cell torsor; an elementary path is a finite word H=(d_1,...,d_m) with each d_t in {±e_1,...,±e_6}. A **closed** path satisfies sum_t d_t=0 in Z^6. This uses only P000 primitive axis steps; no native two-dimensional plane, new spatial direction, or unlicensed triadic event is introduced.

For 1<=i<j<=6 let

C_ij(H) = sum_{1<=p<t<=m} d_{p,i} d_{t,j} in Z.

Define C_ji(H)=-C_ij(H) **for closed H**. The 15-entry alternating matrix C(H), or equivalently its formal element in the rank-15 module wedge^2(Z^6), is a *path provenance carrier*, not an expansion of the six spatial axes. Reduction modulo an integer q>=2 gives C_q(H) in (Z/qZ)^15. For a signed named frame P=((a_1,s_1),(a_2,s_2),(a_3,s_3)) with distinct axes and s_j=±1, its three rooted readouts are

r_j(P,H)=s_j s_(j+1) C_(a_j,a_(j+1))(H) mod q

with cyclic j and the oriented convention C_ba=-C_ab.

## Theorem 1 — canonical closed-loop transport and 15-component upper bound

For closed primitive paths H,K, C(HK)=C(H)+C(K). Every axis permutation pi in S6 acts by the alternating relabeling C_(pi(i),pi(j))(pi H)=C_ij(H); reversing an axis orientation changes the corresponding pair signs. In particular a frame substitution P->P' has a deterministic *path-faithful* transport
r(P',H)=extract_(P')(C_q(H)),
and additional closed loops update C_q by addition. These identities hold for any sequence of frame readout changes and closed loops.

**Proof.** Split the defining ordered-position sum for HK into within-H, within-K, and cross-block terms. The last term is (sum_H d_i)(sum_K d_j)=0. Since each primitive step has support on just one axis, for closed H the identity
0=(sum_H d_i)(sum_H d_j)=C_ij(H)+C_ji^raw(H)
makes the reversed pair exactly negative. Relabeling the signed primitive coordinates proves covariance. All extraction maps are signed selections of those 15 entries, so they commute with arbitrary later frame choices. QED.

**Scope:** This is a universal carrier for the *declared pair-area observer*. It does not assert that the native TRIADIC_CLOSURE_E event law reads these coordinates, or that V17/V29/V39 already implement this transport.

## Theorem 2 — exact obstruction to transporting only the current three rooted areas

Take the old frame P=(+e_1,+e_2,+e_3) and the permitted rooted loops of R762CG:
B_23=(+e_2,-e_2,+e_3,-e_3),
L_23=(+e_2,+e_3,-e_2,-e_3).
Their old rooted area triples are (0,0,0) and (0,1,0). Both permit the candidate T_(3,4), because the third rooted residue is 0. In the new frame P'=(+e_1,+e_2,+e_4), **both complete histories have path-derived area (0,0,0)**. Therefore a reframe operation that simply recomputes and retains only the new three rooted areas merges these histories. After the reverse frame change 4->3, their path-derived old rooted triples differ again, and the old-frame guard for a replacement at Port 2 distinguishes them.

Thus **reprojection to only the three currently rooted pair areas is not an all-future-safe source quotient when reversible frame readouts and future pair guards are allowed**. The original R762CG T-rule instead preserves its three *registers*; on L_23, their preserved post-T value is (0,1,0), whereas area freshly extracted from the post-T frame is (0,0,0). That is an exact semantic distinction, not an inconsistency in R762CG's explicitly register-based candidate.

**Proof:** Directly evaluate C_23(B_23)=0 and C_23(L_23)=1, all other C_ij=0. The two frame readouts and guards follow by substitution. All histories have the same Cell endpoint, primitive-step time four, attached initial Port frame and signed-direction histogram; the opposite frame-change observations are pair diagnostics, not claims of independently licensed native events. QED.

## Theorem 3 — exact BRC repair capacity for an arbitrary family of accessible pair probes

Let E be any subset of the 15 unordered axis pairs and put d=|E|. Fix q>=2. For each pair i<j in E, choose **exactly q labeled four-step slots**, each independently filled with
B_ij=(+e_i,-e_i,+e_j,-e_j) or
L_ij=(+e_i,+e_j,-e_i,-e_j).
Concatenate the d pair-blocks in a fixed order. Every one of the 2^(qd) distinct **labeled source histories** has the same full X6 Cell endpoint, time 4qd, and entire 12-direction signed-step histogram: each orientation ±e_i occurs q deg_E(i) times. The observed pair-area residues C_ij mod q, for (i,j) in E, attain *all* q^d vectors. For each pair-and-phase probe
Q_(ij,k)(H)=[C_ij(H)+k=0 mod q], 0<=k<q,
different residue vectors have different response signatures. Consequently the exact observer quotient on this common coarse fibre has

K_E(q)=q^d,  R_E(q)=ceil(log_2(q^d)) fixed bits.

This bound is both necessary and achieved by storing the d residues, with no assertion about stronger future-event observations. If all 20 three-axis frame selections are available as *pair diagnostic readouts*, E is all 15 pairs, so K=q^15 and R=ceil(15 log_2 q). For a fixed single three-Port frame's three rooted pair probes, d=3, recovering the q^3 scale of R762CG under the same abstract pair-observer interface.

**Proof.** For each pair, B contributes 0 to every C; L contributes +1 to its own pair and 0 to the other 14 entries. This follows from the single-axis support and the closed-loop concatenation law. Choosing k L-slots gives residue k mod q, so all q residues occur for each pair independently; the fixed histograms and lengths follow directly from B/L. Distinct d-vectors differ at one pair, and the phase probe with k congruent to minus the first phase separates them. Storing the residues makes all declared probes deterministic, establishing both inequalities. QED.

## Theorem 4 — exact positive N-BRC weight, with no signed cancellation

In the group algebra N[(Z/qZ)^d], the labeled-source generating function is
F_(q,E)(x)= product_((i,j) in E)(1+x_ij)^q, subject to x_ij^q=1.
Its residue coefficient is w(a)=product_((i,j) in E) f_q(a_ij), where
f_q(0)=2; f_q(t)=binom(q,t) for 1<=t<q.
Indeed k=0 and k=q both yield residue zero, while any 1<=t<q has the single possibility k=t. Therefore sum_a w(a)=2^(qd) exactly. The weights count ordered source choices: they are not force amplitudes or a signed physical balance law.

For all 15 pair probes, q=2 gives 32768 classes, 15 bits, 2^30 source histories; q=3 gives 14,348,907 classes, 24 bits, 2^45 histories; q=7 gives 4,747,561,509,943 classes, 43 bits, 2^105 histories.

## Validation and precise scope

`R762CH_VERIFY.py` computes primitive paths and ordered pair sums using exact integers. Checks: all 15 B/L+/L- loop identities and their histograms; 720 axis permutations × 15 generators (10,800 covariance cases); all 20 unordered triples × 8 sign frames (160 extraction checks); q=2..10 each of 15 independent basis witnesses, fixed coarse histograms and integer BRC normalization; 6 full selected q-adic multi-pair witnesses; explicit B23/L23 frame-switch obstruction. **11,156 author-side assertions/checks** passed. `R762CH_EVIDENCE.json` records those counts and values. General theorems have direct proofs above; finite tests validate implementations and examples. Independent review NOT_REVIEWED.

**Native event boundary:** The available frozen P000 and X6 Cell/source records specify primitive signed adjacency and triadic arity, but do not supply a proved exact transport of the authentic `TRIADIC_CLOSURE_E` event through arbitrary pair charts. In this note frame changes and pair guards are typed diagnostic/candidate operations. Prior R762CG's explicitly register-based candidate remains valid with its original event semantics.

**Next discriminating question:** Obtain the authentic Cell/Port/Link license for `TRIADIC_CLOSURE_E` and V17/V29/V39. Determine the actually accessible pair family E and any cross-pair constraints. Prove the event language factors through a smaller admissible pair quotient, or exhibit a legal separating suffix demanding dormant C_ij entries. If event paths cross Port substitutions, specify whether the global 15-entry area or an enriched frame-register transport is the correct BRC state.
