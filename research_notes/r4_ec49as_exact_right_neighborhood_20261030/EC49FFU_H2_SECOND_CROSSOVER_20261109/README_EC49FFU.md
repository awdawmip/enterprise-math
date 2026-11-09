# EC49FFU — Second H2/Hh crossing: a two-key 4h+42 BRC native-prefix construction

**Date**: 2026-11-09. **Status**: AUTHOR_ANALYTIC_CONSTRUCTION / EXACT_INTEGER_CHECK_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED.
**Frozen science pin**: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
**Predecessor**: EC49FFT at `1cec5c2fc1146a81e2f185d84dac2bb800bb09f5`. The original BRC six-operation / nine-state observer is the EC49FFJ Git blob `6350340fbe869f17b5a50bd1ba30640db44a3a99`.

## Exact problem

For H2 and Hh, require one original operation word with each signature 1,2,4,8 at **each** window: eight labeled demands. Every word has a positive complete BRC key K=(x,y,z); count the union of **ordered signed X6 nonempty microstep prefixes**, not just endpoints. The explicit families use only two distinct complete keys, hence obey any key budget >=2.

Original words are `a=(-1,-1)`, `c=(1,2,-1,-2)`, `d=(2,1,-2,-1)`, `e=(3,1,1,-3)`, `f=(1,-1)`, `g=(2,-2)`. A legal length-h word with K=(x,y,z) has `#a=z-1, #e=z, #c+#d=x+y-h-1, #f=h+1-y-2z, #g=h+1-x`. The complete nine-state DFA is in the attached exact checker. All construction paths have endpoint (2,0,0,0,0,0).

## Theorem U1 — infinite new family

Fix any integer `h>=4` and any integer `4<=x<=h`. Use H2 key `K2=(3,1,1)`, with words by signature `4:ce, 8:ec, 2:ed, 1:de`. Set `r=x-3>=1`, `s=h+1-x>=1`. At Hh use the single complete key `Kh=(x,h+2-x,1)` and four words

- sig4: `f^r e g^s c`;
- sig2: `f^r e g^s d`;
- sig8: `g f^r e g^(s-1) c`;
- sig1: `g f^r e g^(s-1) d`.

**Exactly `4h+42` different nonempty signed native prefixes occur in the eight paths**, for every such (h,x). The family gives `h-3` different large-window complete keys with the same cost.

*Proof.* The original H2 paths have exactly 28 distinct signed prefixes. The four Hh paths have common length `L=2h+4`. Each c/d terminal pair shares `L-4` signed microsteps and forks into two four-microstep endings, costing `L+4`. The f-leading pair and g-leading pair start with distinct signed first microsteps +1 and +2, so their combined count is `2(L+4)=4h+16`. The first steps of H2 include +1,+2,+3; the Hh path starts are `(1,-1)` and `(2,-2)`, whereas every H2 second step is positive. Hence the H2 and Hh prefix sets overlap **only** at the two singleton prefixes `(1,)` and `(2,)`. Inclusion-exclusion gives `28+(4h+16)-2=4h+42`. The explicit operation multiplicities meet the key equations, and the fixed DFA yields signatures 4,2,8,1 respectively. All paths preserve their ordered signed X6 steps. QED.

## Theorem U2 — improved constructive bound and a precise counterexample

From EC49FFT there are two earlier all-h constructions of costs `8h+12` (extension) and `6h+23` (late split). Thus for integer `h>=4`:

`C_min(H2,Hh) <= min(8h+12, 6h+23, 4h+42)`.

Within **these three explicitly checked constructions**, extension wins at h=4,5; late split at h=6,7,8,9; and U1 at **every h>=10**. The complete old finite optimization at h<=8 remains as published. For h>=9 this is an upper-bound family, not an exhaustive optimum claim.

**Counterexample to the proposed next-step lower bound.** At h=10 and x=4, H2 words are `ce,ec,ed,de` with key (3,1,1). H10 words by signatures 4,2,8,1 are `fegggggggc, fegggggggd, gfeggggggc, gfeggggggd` with key (4,8,1). These eight paths have exactly **82** prefixes. Therefore the EC49FFT proposed universal lower bound `C_min(H2,Hh)>=6h+23` for all h>=6 is false: at h=10 it demands >=83, while a legal 82-edge witness exists. The earlier late-split witness costs 83 and extension 92 at h=10.

| h | Extension | Late split | U1 | Minimum of the three |
|---:|---:|---:|---:|---:|
|4|44|47|58|44|
|5|52|53|62|52|
|6|60|59|66|59|
|7|68|65|70|65|
|8|76|71|74|71|
|9|84|77|78|77|
|10|92|83|82|82|
|11|100|89|86|86|
|12|108|95|90|90|

## Exact validation and next question

The published `VERIFY_EC49FFU.py` uses the original nine-state DFA, the complete keys, the signed native six-axis endpoint, and a separate trie counting *ordered* signed prefixes. It checks all three families for h=3..32 plus h in {40,48,64,80,100}, including **752 different (h,x) pairs**. It was executed locally and passed; the full compact output is `EXACT_REPORT_EC49FFU.json`. Command: `python3 VERIFY_EC49FFU.py`.

**Next**: exact unrestricted multikey optimization at h=9,10,11, or a four-signature family improving the additive constant 42. Then use the mechanisms on the frozen original 22-demand H2/H3 / high-signature mother template with at most five complete keys and the 93-edge target. This author-side result does not assert task CLAIM, a native Result or independent Driver admission.
