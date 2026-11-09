# EC49FFZ — Universal high-seed absorption for original BRC signed-X6 paths

**Date:** 2026-11-10 (Asia/Shanghai). **Classification:** author-side analytic theorem, executable integer checks, unreviewed/not admitted. **Frozen scientific input:** fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Based on original EC49FFC/FFD nine-state observer and signed-six-axis operator semantics, reusing EC49FBS/FFM/FFX/Y; P000 and ACTIVE worldview unchanged.

## 1. Precise problem and theorem

The primitive ordered signed X6 operation codewords are

    a=(-1,-1), c=(+1,+2,-1,-2), d=(+2,+1,-2,-1)
    e=(+3,+1,+1,-3), f=(+1,-1), g=(+2,-2).

Each integer denotes a signed native-axis microstep, not a one-dimensional signed scalar. The observation horizon h is the **number of operation codes**, while the native microstep length is the sum of their codeword lengths. The cost C_native counts distinct nonempty **ordered signed-X6 microstep prefixes** in the union of all selected paths.

Fix four earlier high-signature paths, unchanged from the frozen mother input:

| Observation | Operation word |
|---|---|
| H2:16 | fe |
| H2:32 | ge |
| H3:16 | feg |
| H3:32 | gef |

For each integer h≥4, add four Hh paths, one ending in each original low signature 1,2,4,8 of the nine-state observer. Each new path may have its **own strictly positive complete BRC key**; no global key cap is imposed in this auxiliary model. For an h-letter word w, the key is

    K(w)=(h+1-#g(w), h+1-2#e(w)-#f(w), #e(w))

and admissibility also requires #e=#a+1≥1 and every key component positive. The original fixed H2 seeds retain their exact frozen interpretation: fe has a zero key component and is not reclassified as a newly positive-key Hh candidate.

**Theorem (arbitrary positive full keys; unequal native lengths allowed).**

    min C_native(H2-high,H3-high,Hh-four-low) = 4h+16
    for every integer h≥4.

Moreover, four new low paths can all use one positive key, with all four high seeds *already present as operation and native microstep prefixes*, adding exactly zero new native prefix edges. This strengthens the EC49FFM single-window/single-key theorem and preserves all source branch/order information.

## 2. Infinite constructive family

For any h≥4, take any S∈{f,g}^(h−4), and write t=#g(S). The four paths are

    Hh:4  feg S c
    Hh:2  feg S d
    Hh:8  gef S c
    Hh:1  gef S d

where spaces mean concatenation. All four have exactly h operation letters, terminal signatures 4,2,8,1 respectively, final signed X6 endpoint (+2,0,0,0,0,0), and the identical strictly positive full key

    K_S=(h−t,t+2,1).

Because the words contain one e and one c/d each, every native length is L=2h+4. The two root branches fegS and gefS start in different native signed steps and share no nonempty prefixes. Within each branch, the c and d alternatives agree through depth L−4 and then add four disjoint signed-prefix edges apiece. Hence

    C_native = 2*((L−4)+4+4) = 2L+8 = 4h+16.

The fixed fe/feg paths are prefixes of the fegS branch; the fixed ge/gef are prefixes of gefS. Their native-prefix union is wholly contained in that of the four Hh paths. This gives 2^(h−4) distinct suffix-word witnesses and h−3 different complete BRC keys within the optimal family.

Illustrations: H4 optimum 32 edges (fegc,fegd,gefc,gefd), H9 optimum 52, H20 optimum 96, H100 optimum 416.

## 3. Universal lower bound without a fixed-key assumption

**Lemma A (length and root separation).** A legal low-terminal word contains at least one c or d. Indeed, from the initial DFA state, none of a/e/f/g produces a low output, and once noninitial those operations preserve the state, so reaching a low state requires c/d. Since #e≥1,

    L(w)=2h+2(#e+#c+#d) ≥ L0=2h+4.

The original nine-state table also gives these reachable low-signature sets for first letters:

    a->{2,8}, c->{4}, d->{1},
    e->{2,8}, f->{2,4}, g->{1,8}.

Thus any witness for signature 4 starts c or f, with signed first native step +E1, whereas a signature-1 witness starts d or g, with first step +E2. At least two distinct signed prefixes therefore occur at each depth 1,...,L0−4.

**Lemma B (final four signed-prefix nodes distinguish all low outputs).** Let u,v have the same operation horizon h and *different* final low signatures, but otherwise arbitrary strictly positive full keys and potentially unequal native lengths. Put ell=min(L(u),L(v)). The native expansions of u and v cannot share the initial ell−3 signed microsteps.

*Proof.* Relabel so L(u)≤L(v). The six signed codewords have pairwise distinct first **two** microsteps. At the first different operation, at most one more native microstep can coincide. Let s be the signed length of their common whole-operation prefix. As both operation words have exactly h letters, neither is a proper whole-operation prefix of the other. If they agree through L(u)−3 signed steps, necessarily s≥L(u)−4. Every operation code length is 2 or 4; therefore the suffix of u after s consists of either one short code a/f/g (length 2), one long code c/d/e (length 4), or two short codes a/f/g (total length 4).

The only possible first-microstep collisions between **different** codes are c versus f and d versus g. The a and e starting steps are unique. For every low DFA state q∈{2,3,6,7}, each of a/e/f/g fixes q, while each of c/d either fixes q or enters the absorbing dead state 8. The corresponding outcomes can be verified directly against all nine rows of the published original transition table. If a suffix beginning in a short f/g reaches a low label, then its entry state must already be that low state, and replacing f→c or g→d can only preserve the same low state or kill the path; additional suffix codes also preserve or kill that low state. Conversely, if a c/d suffix reaches low from a nonlow entry, its colliding short f/g variant cannot reach a distinct low state: short operations preserve the nonlow entry state. When the entry is low, both alternatives either keep that same low state or die. The single-long and two-short suffix cases obey the same exhaustive collision rule. Thus any two paths that agreed through L(u)−3 cannot end in different low labels. Contradiction. QED.

**Lower-bound consequence.** Each of the four paths, labelled with pairwise different low outputs, has four final signed-prefix nodes at depths L(w)−3,...,L(w), each absent from the other three paths' prefix sets by Lemma B (regardless of length disparities). These 16 nodes all lie strictly deeper than L0−4. By Lemma A, the two initial branches already supply at least 2(L0−4) distinct nodes at earlier depths. Therefore

    C_native ≥ 2(L0−4)+16 = 2L0+8 = 4h+16.

Adding frozen high seeds cannot reduce that union. The explicit family attains the lower bound. QED.

## 4. Verifiable evidence

- VERIFY_EC49FFZ_NATIVE.py (actual Git Blob 06212ace738151aeb1bdf77c9f3f85c5c5dd7e25): exact nine-state DFA, complete-key and endpoint tests, literal signed-six-axis prefix computation. Checks all 511 binary S at H4..H12, 147 default witnesses H4..H150, and selected all-g/alternating variants. Exhaustively enumerates original six-operation words at h=2..7, testing the different-output final-four separation over 4,30,176,950,4932,25060 admissible low-terminal words, respectively; PASS.
- VERIFY_EC49FFZ_HIGH23_LOWh.cpp: exact 16-mask integer prefix-trie state-quotient DP, with H2/H3 seed contribution and original EC49FBS/FFX/Y edge costs. Independently of the explicit witnesses, optimizes H4..H35, giving C=4h+16 at every integer h in the range, and H40=176. Source is a scoped adaptation of EC49FFY, not a novel generic DP.
- EXACT_REPORT_EC49FFZ.json: signed-native witness sample, DFA root reachability and exhaustive test counts. Full literal C++ run records H3..H35 are in the separately preserved author's evidence archive.

All mathematical costs/signatures and bounds use exact integers, not floating-point optimizers. Finite checks audit model transcription; the universal statement is established analytically above. Validation is author-side and awaits independent review.

## 5. Transfer to the original objective

This gives an exact local **seed absorption law**: fixed H2/H3 high outputs cost zero extra native edges when embedded into the optimal four-low Hh bundle. It provides a reusable structural block for the original frozen 24-observation challenge, with **full keys≤5 and C_native≤93**. The next discriminating action is to combine this block at an admissible late-low horizon with H4–H9's actual high/low observation quota and five-key coverage, keeping every ordered native prefix; search an exact ≤93 full-system witness or certify an explicit inventory class by a signed-prefix integer dual. Distinct-window native costs must be optimized jointly, not added as if disjoint.

Source status: original historical task text EC49AS returned NO_CURRENT_IMMUTABLE_PUBLICATION, so this author-side manuscript on PR #1730 asserts no formal CLAIM, no native Result, and no independent Driver admission. Frozen science remains pinned; P000 and ACTIVE worldview remain unchanged.
