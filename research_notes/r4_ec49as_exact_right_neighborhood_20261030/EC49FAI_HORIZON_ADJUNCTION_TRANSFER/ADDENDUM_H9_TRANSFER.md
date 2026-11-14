# EC49FAI Addendum — 80 ≤ E*(H9,M5,S≤6) ≤ 94, with complete native-X6 witness

Date: 2026-11-04. **AUTHOR-LEVEL EXACT DERIVATION AND EXECUTED INTEGER WITNESS, NOT INDEPENDENTLY REVIEWED OR ADMITTED**. This addendum strengthens EC49FAI's conditional H9 transfer lemma without modifying the frozen H8 scientific input `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.

## Statement

Consider the **new auxiliary H9** model: precisely the same seven ordered signed native-X6 operation codes `a..g`, nine-history five-bucket T4/T2 observer, net signed displacement `(2,0,0,0,0,0)`, horizon-wise rational observation rank nine, exact positive-step full six-axis BRC keys, and distinct nonempty signed primitive-prefix cost E used by the frozen H8 model, now over horizons h=2,...,9. Impose exactly M=5 globally distinct keys and at most S=6 distinct transfer signatures.

**Theorem:**

`80 <= E9*(M=5,S<=6) <= 94.`

These are author-side mathematical bounds. They are not an exact H9 optimum, a physical Heartbeat evolution result, or a change to EC49FAH's H8 theorem.

## Lower bound: exact M4/M5 restriction plus new-horizon terminal separation

EC49EXJ's published author-side finite exhaustive result gives `E8*(M=4,S<=6)=90` over the same complete seven-operation signed-X6 observer model, across all 55,493 eligible four-key schedules. See `EC49EXJ_H8_M4_S6_GLOBAL_EXACT/README_EC49EXJ.md` and `EC49EXJ_COMPLETE_EXECUTED.json` (both read from the existing Draft PR). EC49FAH gives `E8*(M=5,S<=6)=76` by 12,356 remaining schedule certificates and four explicit witnesses. Their scientific pin is the same; their formal independent review is pending.

Deleting h9 from any legal H9/M5 witness leaves H8 with either four or five complete keys and at most six signatures. Therefore the H8 restricted prefix union costs at least `min(90,76)=76`.

The actual native operation encodings are:

`a=(-1,-1); b=(-2,-2); c=(+1,+2,-1,-2); d=(+2,+1,-2,-1); e=(+3,+1,+1,-3); f=(+1,-1); g=(+2,-2)`.

Each operation has at least two primitive steps. Their ordered first-two-step pairs are all distinct, so the code is prefix-free and the first two native primitive steps identify each operation. For a **fixed positive integer operation horizon h**, no distinct completed h-operation words are prefix-related in the expanded primitive-step language. Moreover, the last two signed primitive prefixes of every h-word lie within its hth operation; none can occur within a completed word of smaller operation horizon, and these two terminal prefixes are distinct across different h-operation words (the two-step distinguishing property rules out collisions). Thus every *distinct* new-horizon h9 word forces **two** additional signed primitive-prefix edges beyond every selected h2..h8 word.

For one h9 observer signature, its deterministic nine-initial-history to five-terminal-bucket transfer matrix has rank at most five. Hence rational rank nine at h9 requires at least two different complete signed-word transfer signatures and therefore at least two distinct h9 words. This forces **at least four** new primitive prefixes. Consequently

`E9 >= min(E8_M4,E8_M5)+4 = 76+4 = 80.`

The bound is independent of the cache key assigned at h9, provided the declared H9 horizon-wise rank and exact-key constraints hold. This is a direct general-horizon proof of the terminal two-prefix inequality for the *specific pinned native operation code*, not an extrapolation of the earlier h≤8 computed certificate.

## Upper bound: explicit 94-edge, M=5, S=6 construction

Reuse the complete verified EC49EXJ 90-edge H8/M4 native word construction, and add **two** h9 words obtained by appending operation `g=(+2,-2)` to the two h8 T2 witnesses:

| h | Selected exact operation words | Complete positive six-axis BRC key | Cumulative signed primitive-prefix E |
|---:|---|---|---:|
| 2 | ce,de,ec,ed | (3,1,1,0,0,0) | 28 |
| 3 | feg,gef | (3,1,1,0,0,0) | 42 |
| 4 | fegd,gefd,gefc,fegc | (4,2,1,0,0,0) | 58 |
| 5 | fegfg,geffg | (4,2,1,0,0,0) | 64 |
| 6 | geffgd,geffgc,fegfgd,fegfgc | (5,3,1,0,0,0) | 80 |
| 7 | fegfgfg,geffgfg | (5,3,1,0,0,0) | 86 |
| 8 | fegfgfgg,geffgfgg | (5,4,1,0,0,0) | 90 |
| **9** | **fegfgfggg,geffgfggg** | **(5,5,1,0,0,0)** | **94** |

The h9 words have the original T2 signatures `1836425` and `1866380`. The h9 nine-history one-hot observation matrix over their two transfer maps has rank **nine** over Q, as independently confirmed by full 9×10 matrix reduction modulo prime 1,000,003. Every horizon has rank nine, all words exactly return signed displacement (2,0,0,0,0,0), every horizon's complete BRC key is constant, there are precisely five global complete keys and precisely six transfer signatures. The two new g-pairs contribute exactly four distinct new prefixes. This attains E=94 and proves the upper bound.

## Reproduction and real status

The stand-alone `VERIFY_EC49FAI_H9.js` was actually executed with exact integer operations and a 9-row modular matrix-rank checker. `EXACT_REPORT_EC49FAI_H9.json` records every word, key, signature, horizon rank and prefix count. A separate Python+SymPy rational checker also obtained E8=90, E9=94, eight exact ranks equal to nine, M=5 and S=6; no Source-native Driver authority is inferred.

**Next discriminating question:** refine the gap `80<=E9*<=94` by exhaustive compatible H9 schedule classification and a prefix-cover lower bound; specifically test whether an H9 completion from any of the H8/M5 76-edge equality schedules can preserve five full keys, and construct cost <94 or prove it impossible for that subfamily. Verify upstream H8 certificates independently as a distinct Driver acceptance track. Preserve frozen H8 scientific pins and do not promote these author-side results without actual native review.
