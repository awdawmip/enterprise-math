# EC49FFM — Universal exact single-key four-low-signature BRC prefix optimum

Date: 2026-11-09. Status: AUTHOR ANALYTIC PROOF + EXACT FINITE AUDIT; independent Driver review and native Result admission pending.
Frozen scientific input: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Original native six-operation model: ../EC49FFJ_NATIVE_PREFIX_TRIE_20261109/BRC_ORIGINAL_MODEL_EC49FFJ.py, Git Blob 6350340fbe869f17b5a50bd1ba30640db44a3a99. This note uses the original ordered signed X6 microsteps, complete key, and nine-state DFA, not a quotient of their path/provenance.

## Theorem (all integer observation windows h >= 4)

Let four operation words share ONE admissible complete BRC key K=(x,y,z) at window h and give the four observer signatures 1,2,4,8. Let C_native count distinct nonempty native signed-X6 microstep prefixes in the union of their four expansions. Over all K and all eligible quadruples,

**C_min(h) = 4h + 16 for every integer h >= 4.**

In particular H10 globally has exact optimum 56, including all z>=2 keys; no further H10 enumeration is necessary for this optimum. The statement is deliberately single-window, single-complete-key, and four-low-signature; the five-key multiwindow <=93 mother problem remains open.

## Definitions from frozen model

The six operation codes are a=(-1,-1), c=(+1,+2,-1,-2), d=(+2,+1,-2,-1), e=(+3,+1,+1,-3), f=(+1,-1), g=(+2,-2), with each signed integer denoting a native X6 axis microstep. The nine-state transition table and readout are copied in VERIFY_EC49FFM.py. All six codes begin with distinct ordered pairs of signed microsteps, so the next operation is decoded by its first two microsteps.

At window h, all legal words with a fixed complete key (x,y,z) have operation counts

- #a=z-1; #e=z; #c+#d=x+y-h-1>=1;
- #f=h+1-y-2z>=0; #g=h+1-x>=0.

Consequently the common native length is L=2(x+y+z-1), and x+y>=h+2 and z>=1 imply L>=2h+4.

## Lemma 1: output 4 and output 1 have different first native steps

From the exact nine-state DFA, the possible low signatures after each first operation, allowing arbitrary later operations, are:
a->{2,8}, c->{4}, d->{1}, e->{2,8}, f->{2,4}, g->{1,8}.
Thus output 4 requires an initial c or f, both starting with signed +E1; output 1 requires initial d or g, both starting with +E2. Any four witnesses for all signatures have at least two distinct prefixes at every microstep depth 1..L.

## Lemma 2: last three signed microsteps cannot distinguish two different low outputs

For any two same-native-length operation words whose terminal signatures are both in {1,2,4,8}, equality of their signed native prefixes of length L-3 forces their terminal signatures to be equal.

Proof: Let s be the signed length of their maximal common *complete-operation* prefix. Distinct operations have distinct first two signed steps. If they share L-3 signed steps but eventually differ, the first differing operation must begin after at least L-4 steps. All operation lengths are even (2 or 4), so s=L-4 or s=L-2.

If s=L-2, both remaining operations are among a,f,g; all three leave every noninitial DFA state unchanged. The common prefix has already consumed operations (L>=12), hence both terminal outputs agree.

If s=L-4, the remaining 4 microsteps must be one of the three length-4 codes c,d,e or one of the nine concatenations of two length-2 codes in {a,f,g}. Equality of signed prefixes through L-3 forces these two suffixes to have the same first signed microstep. A finite check of the original transition table at all nine possible entry states gives: among these 12 suffixes, any two with the same first microstep and with low terminal signatures always have *the same* terminal signature. Details: among distinct code classes the only first-microstep collisions are c versus f(a/f/g), and d versus g(a/f/g); the other length-2 tails preserve each noninitial state. Directly checking the nine-state table shows neither collision produces two distinct low outputs. The executable verifier includes the complete 9 x 12 check. This proves the lemma.

## Lower bound

Choose four witnesses giving 1,2,4,8 at the common K. By Lemma 1 the signed-prefix union has >=2 nodes at each depth 1..L-4. By Lemma 2 all four distinct low signatures have distinct signed prefixes at depth L-3, hence >=4 at each of the final four depths L-3,L-2,L-1,L. Therefore

C_native >= 2(L-4)+4*4 = 2L+8 >= 4h+16.

These are exact integer inequalities over all eligible K, including arbitrarily large h and all legal z, so the lower bound is not extrapolated from finite H9/H10 classifications.

## Matching infinite family

For every integer h>=4 and 4<=x<=h define

K=(x,h+2-x,1), r=x-3>=1, s=h+1-x>=1.

Use four words (the subscripts denote terminal readouts):
w4=f^r e g^s c; w2=f^r e g^s d;
w8=g f^r e g^(s-1) c; w1=g f^r e g^(s-1) d.

Each has exactly h operations, one complete key K, native length L=2h+4, and the required low output. The f-leading and g-leading pairs have different first signed microsteps. Inside each pair the native expansions share exactly L-4 microsteps, then c/d split into distinct four-step endings. The union has 2[(L-4)+8]=2L+8=4h+16 nonempty signed prefixes, attaining the lower bound. There are h-3 different attaining complete keys in this family.

## Exact independent author checks

Executed VERIFY_EC49FFM.py with Python integer tuples and no classical pi/trigonometry: (1) six pairwise-distinct two-step operation code prefixes; (2) complete nine-state reachability after all six possible first operations; (3) every one of the 9x12 DFA-state/four-step-suffix cases; (4) exhaustive enumeration over all 200 legal keys at h=2..9 (781882 retained nonzero low-signature words) confirming the L-3 prefix lemma; (5) 81 exact infinite-family witness instances for h=4..200. Exact stdout: RUN_EC49FFM.json. The universal proof uses Lemmas 1 and 2 plus the displayed construction; the finite tests check its model transcription and mechanism.

The original frozen code and actual signed path were retained through all comparisons. Formal independent Driver review is still required for project mathematical admission. Protected P000 and ACTIVE worldview unchanged.

## Next mathematically discriminating task

Return to the multiwindow/five-complete-key <=93-edge mother problem. Build a multi-key signed-prefix lower certificate that accounts for cross-key sharing, or search a new feasible observation-demand configuration outside prior 22-24 path exclusions. Reuse the universal single-key bound when an entire set of four low signatures is forced onto one complete key at a window; do not sum these lower bounds across keys/windows without a proven disjointness/fiber certificate.
