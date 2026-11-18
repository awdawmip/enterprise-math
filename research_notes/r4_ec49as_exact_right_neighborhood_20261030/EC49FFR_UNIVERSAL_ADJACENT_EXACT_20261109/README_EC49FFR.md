# EC49FFR — Exact universal one-key adjacent-window BRC cost

Date: 2026-11-09. Status: AUTHOR_COMPUTER_ASSISTED_UNIVERSAL_PROOF; independent Driver review and native Result admission pending.

Frozen science `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Frozen original native signed-X6 six-operation / nine-state-DFA model Git blob `6350340fbe869f17b5a50bd1ba30640db44a3a99`. This advances EC49FFQ: it closes the eight-native-edge gap in the universal lower bound.

## Exact theorem

Fix any integer `h>=5`. For each of the two windows Hh and H(h+1), require one original operation word for each low signature 1, 2, 4 and 8: eight demands. All eight words have **one identical complete BRC cache key** K=(x,y,z) with positive integer components. Cost is the number of distinct nonempty **ordered signed-X6 native-microstep prefixes** across the eight words. Operations:

```text
a=(-1,-1)        c=(1,2,-1,-2)       d=(2,1,-2,-1)
e=(3,1,1,-3)     f=(1,-1)            g=(2,-2)
```

Then the exact global optimum in this frozen model is

```
C_min^one-key(Hh,H(h+1)) = 4h+40, for ALL integers h>=5.
```

The theorem's observer, complete-key equality and native-prefix cost are preserved unchanged.

## Universal bounded-tail lower certificate

For the earlier window Hh, the complete operation-count vector `(a,c+d,e,f,g)` is

```
(z-1, x+y-h-1, z, h+1-y-2z, h+1-x).
```

For H(h+1) this vector differs by `(0,-1,0,+1,+1)`. Every selected word has native length `L=2(x+y+z-1)`. The later window requires at least one c/d, so `x+y>=h+3` and `L>=2h+6>=16`.

Let `N_t` count distinct native prefixes at depth t in a proposed eight-word solution. Original DFA signatures 4 and 1 require initial native signed steps +1 and +2 respectively; hence `N_t>=2` for every t>=1.

**Finite universal suffix lemma.** At depth L-r, for each `1<=r<=7`, a native prefix uniquely determines all complete preceding operations: every operation has even length and its first two microsteps identify it uniquely. A cut can occur at a boundary or after the first, second or third microstep of the current operation. The remaining r signed microsteps contain a finite list of operation tails, independent of h. The nine-state DFA state *before* the current operation lies in 1..8, never 0, since `L-r>=9` and no completed operation enters state 0.

The standalone exact-integer program `VERIFY_EC49FFR.py` exhausts every decoder phase, actual operation tail, possible signed first microstep, DFA state 1..8 and suffix quota vector `(a,c+d,e,f,g)`. At a fixed prefix, signatures at the later window can be combined with those at the earlier one only if their suffix quotas differ by `(0,-1,0,+1,+1)`. Prefixes serving only one horizon are explicitly included. This catalogue is an overapproximation of physically reachable prefixes, so its *minimum eight-demand set-cover number* is a rigorous lower bound for actual N_(L-r).

| Remaining native steps r | Min. required prefixes at depth L-r | Max demand labels per single prefix |
|---:|---:|---:|
| 1 | 8 | 1 |
| 2 | 8 | 1 |
| 3 | 4 | 2 |
| 4 | 4 | 2 |
| 5 | 4 | 2 |
| 6 | 4 | 2 |
| 7 | 3 | 3 |

The exceptional r=7 three-prefix cover has **exactly one** possible triple of eight-bit masks (bits 0..3: Hh sig1,2,4,8; bits 4..7: H(h+1) sig1,2,4,8):

```
00001010   01100100   10010001
```

They demand DFA states before the partially decoded operation **1, 4, 5** respectively. State 1 can only follow first operation a/e (initial native -1 or +3); state 4 only first f (+1); state 5 only first g (+2). Therefore if just three native prefixes cover all eight demands at depth L-7, those paths already have **three distinct first native steps**, i.e. N_1>=3.

If N_(L-7)>=4, disjoint-depth summation gives

```
C_native >= 2(L-8) + 4 + 4*4 + 3*8 = 2L+28.
```

If N_(L-7)=3, the extra N_1>=3 supplies the missing edge over the early baseline:

```
C_native >= 2(L-8) + 1 + 3 + 4*4 + 3*8 = 2L+28.
```

A value below 3 is excluded by the certificate. Since `L>=2h+6`, universally `C_native>=4h+40`. This bound is analytic in h: the exhaustive finite suffix check discharges a bounded combinatorial lemma whose state space is independent of h.

## Matching symbolic upper construction

Set `q=h-4>=1`, and use `K=(5,h-2,1)`. Original operation words:

| Window | sig1 | sig2 | sig4 | sig8 |
|---|---|---|---|---|
| Hh | `g^q e f d d` | `f g^q e d d` | `f g^q e c c` | `g^q e f c c` |
| H(h+1) | `g^q e f d g f` | `f g^q e d g f` | `f g^q e c f g` | `g^q e f c f g` |

As in EC49FFQ, direct DFA transitions, word count equations and signed native paths establish common key K, required signatures, native endpoint (2,0,0,0,0,0) and common length L=2h+6 for all integer h>=5. Their native-prefix count is 2 at depths 1..L-8, 4 at L-7..L-3, 8 at L-2..L. Consequently C_native = 2(L-8)+4*5+8*3 = 4h+40. This matches the lower bound.

## Reproduce / precise scope

Run `python3 VERIFY_EC49FFR.py > EXACT_REPORT_EC49FFR.json`. The program checks the finite suffix lemma for r=1..7, the exact exceptional three-mask cover, and its unique state provenance. It also independently checks the explicit family for h=5..64 (60 exact sample points). The symbolic h-independent reduction is the mathematical proof bridge; the 60 witness samples are ancillary validation.

**BRC reuse:** REUSE_APPLIED / EXTEND_EXISTING_TOOL — the original nine-state observer, full-cache-key equations and ordered signed-X6 path costs. The original mother question (22-path H2/H3 plus high signatures, <=5 full keys and `C_native<=93`) remains open and is not replaced by these eight-demand one-key windows.

**Next question:** generalize the bounded decoder-tail mask certificate to multi-window/multi-key path selection while preserving the mother's exact observation quota. No formal current active Owner/CLAIM has been established for this author's research line; do not infer canonical mathematical admission from this PR. P000 and protected worldview unchanged.
