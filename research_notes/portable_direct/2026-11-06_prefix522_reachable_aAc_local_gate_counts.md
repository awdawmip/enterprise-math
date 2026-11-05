# PREFIX-522 — A reachable aAc KMP gate on the legal four-STAR X6/BRC language

Date: 2026-11-06 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED.
Parent line: RS-X6-NATIVE-ROTATION-DYNAMICS; independent author-side mathematical work, no claim of a formal active CLAIM or physical rotation-selection law.
Frozen scientific input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Predecessor: PREFIX-521, commit 6a6dafd27fd8df11f7dfcb7fedbf98d6489d3516.
Current behavioral protocol: docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context; docs/PORTABLE_RESEARCH_PROTOCOL.md; research_priorities/research_method.json; P000/ACTIVE Heartbeat World. Definitions of the candidate four-STAR graph are inherited specifically from PREFIX-518 (not promoted to physical dynamics).

## 1. Exact research question and native population

PREFIX-521 proved that the former literal gates aab and aba never match a legal four-STAR candidate macrotrace. We therefore distinguish the sign of chart-L1: +L1 -> a and -L1 -> A. Both signs of chart-L3 -> c, chart-L2 -> b/B, and every other signed axis -> filler _. The new literal gate is **aAc**, with KMP initialized at q0=0; a full match leaves state 3, and subsequent characters update it by ordinary prefix/suffix matching.

Use native six signed axes as defined in the fixed K4 atlas: L1=AB, L2=CD, L3=AC, L4=BD, L5=BC, L6=AD. The four STARs are the incidence triples of the four K4 vertices. A legal directed phase is (STAR, previous_signed_phase, current_signed_phase). There are 48 such phases. Each phase has three candidate exits: one non-backtracking stay and two switch exits through the shared current axis. Each exit (o -> n) has two labeled *native two-primitive* BRC traces, INNER=(-o,n), OUTER=(n,-o), where o and n have opposite signs and distinct axes. These traces are genuine signed X6 Cell steps within the declared **symbolic candidate** language; they are not asserted to be the physical rotation rule. A chart h is one of the 24 K4 vertex permutations.

The theorem concerns all starting phases, every finite compatible macrotrace, each independent choice of INNER/OUTER branch, all 24 charts, and an initially empty KMP q0=0. Original branch labels and indexed Cell history remain preserved for stronger future observers.

## 2. Exact local recognition theorem

For any chart h, let a_h be the preimage signed-positive axis mapped to L1, c_h the unsigned axis mapped to L3, and S_h their unique common STAR. For d>=2 let s_d be the final directed phase after d macros, and let beta_{d-1}, beta_d be the last two branch labels (0 INNER, 1 OUTER).

**Theorem 522-A (necessary and sufficient local gate).** The KMP terminal state after d complete macros equals 3 if and only if

  s_d = (S_h, +a_h, -c_h) and beta_{d-1}=beta_d=0.

The event aAc ends exactly on the last primitive character of the final macro. It is always the last three characters of an INNER,INNER two-macro segment; in particular the pattern is reachable.

**Proof.** Each macro produces two signs that agree; adjacent macros have opposite signs. In aAc the first character is positive (+L1), the second is negative (-L1), and the third is negative (-L3). Therefore the first character must be the last character of a positive macro and the remaining two characters must be the following negative macro. Cases for the two branch labels:

* INNER then INNER gives (X,+a_h),(-a_h,-c_h). Compatibility forces the final phase to be (S_h,+a_h,-c_h). Conversely that phase and the two INNER labels produce the gate regardless of earlier path.
* INNER then OUTER would require the second macro's first primitive to be -a_h while its previous phase is +a_h, which violates the distinct-axis exit.
* OUTER then INNER would require the first macro to have previous phase -a_h and also new phase +a_h, again a forbidden same-axis exit.
* OUTER then OUTER would force the two macro phases to reverse directly from -a_h to +c_h to -a_h. Since the pair a_h,c_h shares only STAR S_h, such a reversal is the excluded stay exit; a switch STAR cannot contain a_h as an available exit.

Thus only INNER/INNER remains and the stated phase test is equivalent to a complete hit. QED.

**Explicit original-axis witness:** phases (S_A,+L3,-L6) -> (S_A,-L6,+L1) -> (S_A,+L1,-L3); branch pair (0,0) gives signed primitive word (+L6,+L1,-L1,-L3), color "_aAc", KMP q=3. Changing only the first branch to OUTER gives (+L1,+L6,-L1,-L3), color "a_Ac", q=0, even though its entire phase sequence and its last macro with branch label are unchanged. Hence endpoint plus the last single branch does **not** suffice; the two-branch lookback is sufficient and, under that restricted storage design, necessary.

At macro boundaries the suffix state q=2 (ending "aA") is unreachable because the last two primitive letters belong to a single same-sign macro. For d>=1, q=1 precisely when the last primitive letter is chart-positive L1, unless the (mutually exclusive) full-match case applies. Hence a boundary observer can reconstruct q in {0,1,3} from final phase plus two last branch labels without storing 24 complete KMP maps.

## 3. Exact combinatorial counting for every finite d

The directed 48-state phase graph is **3-in/3-out regular**. Each port has two independent native branch labels, so the labeled macrograph is 6-in/6-out regular. This is a finite K4 incidence identity: the accompanying executable certificate constructs all 48 phases, all exits and explicitly checks the incoming degree of every state. This finite exhaustive identity suffices to prove the following universal-length formulas; no extrapolation from a few path lengths is used.

For one fixed h and **all 48 possible starting phases** (each labeled path counted separately), let N_j(d) count d-macro histories with terminal q=j, and let E(d) count all indexed occurrences of aAc across all d-macro histories.

The single-macro exact finite count is N_1(1)=24. The two-macro exact count is N_3(2)=9: the gate fixes the last state and the two INNER labels, and that state has 3 incoming predecessors, each of which has 3 incoming predecessors. Every prefix or suffix of length k can be appended or prepended in 6^k ways by graph regularity. Therefore, for d>=2,

  N_3(d) = 9*6^(d-2);
  N_1(d) = 24*6^(d-1);
  N_2(d) = 0;
  N_0(d) = 48*6^d - N_1(d) - N_3(d).

At d=0 the counts are (48,0,0,0); at d=1 they are (264,24,0,0). There are d-1 potential two-macro windows; each has exactly 9*6^(d-2) matching marked histories, independently of window position. Counting matches with their index (rather than distinct paths), we obtain

  **E(d)=(d-1)*9*6^(d-2), d>=2.**

Thus, under **uniform counting of the 48*6^d labeled histories** (not a physical probability law), the fraction with aAc at the final macro boundary is 1/192 and the mean number of indexed gate occurrences is (d-1)/192. This fraction is the same in all 24 S4 charts. A single history can have multiple occurrences; E(d) counts each.

The KMP and incidence claims concern the declared symbolic candidate grammar and q0=0; no claim is made about arbitrary native letter insertions, arbitrary KMP initial states, physical time dynamics, or promotion of this candidate graph to complete X6 rotations.

## 4. Reproducible exact certificate

Program: research_notes/portable_direct/prefix522_reachable_aAc_macro_gate_certificate.js
Execution capture: research_notes/portable_direct/PREFIX522_EXACT_EXECUTION.json

The program uses standard ECMAScript and exact bounded integers. It enumerates all 48 states, all 24 S4 charts and their legal one/two-macro histories (41,472 two-macro comparisons), and every legal history through depth three in every chart (298,368 history-prefix checks). It verifies the 3-in/3-out graph, the local iff gate theorem, absence of macro-boundary q=2, the closed-form histograms and the indexed occurrence formula. Depth-three per-frame histograms are [9450,864,0,54] and occurrence total is 108. It separately checks the explicit one-branch information-loss witness. The all-d proof uses the exact local finite graph identity plus regularity, not finite-depth testing as an unbounded inference.

## 5. Next discriminating research step

Construct a weighted transfer operator over the same finite phase/branch graph that retains both the BRC six-axis pair vector and the full count of aAc events. Determine whether the bivariate (event count, selected BRC cancellation) generating functions satisfy a shorter exact recurrence than the full state matrix; preserve original branch labels for indexed Cell queries. Separately investigate arbitrary-triad signed C6 generators and a physically justified rotation-selection law, which this symbolic result does not supply.

Provenance: PREFIX-518/519/520/521 (published author-side, not admitted); current Source P000 and native joint-relation observer-preservation contract; frozen scientific input f42f2906d77f24085c123f3ccfe9667d41caa96d.
