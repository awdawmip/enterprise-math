# EC49FAJ — Exact positive-BRC-key horizon feasibility and four H9 key-reuse constructions

Date: 2026-11-04. Classification: AUTHOR_ANALYTIC_LEMMA / EXACT_NATIVE_X6_FINITE_AUDIT_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED.

## Scientific source, scope and target

This is the H9 auxiliary extension of the signed-X6 seven-operation frozen H8 model in EC49FAI. Frozen parent scientific input: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Operation codes, preserving signed order, are:

    a=(-1,-1), b=(-2,-2), c=(1,2,-1,-2), d=(2,1,-2,-1),
    e=(3,1,1,-3), f=(1,-1), g=(2,-2).

Each selected word has terminal signed displacement (2,0,0,0,0,0); its full six-axis positive BRC key counts positive steps on all six axes. Each of horizons h=2,...,9 requires nine-history T4/T2 rational observation rank nine and a single complete cache key; there must be exactly five distinct complete keys and no more than six distinct transfer signatures globally. Resource E is the number of different nonempty signed *ordered primitive-step prefixes*.

Existing author-side EC49FAI established 80 <= E9*(M5,S<=6) <= 94 using an H8 four-key E=90 witness and a new h9 fifth key. This note obtains an exact feasibility formula, a shared-key branch of the 94-edge upper bound and a concrete reduction for the next optimization. It does not establish the global H9 optimum.

## Theorem 1: exact key feasibility at any operation horizon

Fix an integer horizon h>=1 and a complete positive key K=(x,y,z,0,0,0). There exists a word of exactly h operations in the above seven-letter language with signed displacement (2,0,0,0,0,0) and positive key K **if and only if** x,y,z are integers and the following variables are nonnegative integers:

    z >= 1;
    count(a) = z - 1;
    r = count(c)+count(d) = x+y-h-1;
    count(f) = h+1-y-2*z;
    count(g) = h+1-x.

This is an exact characterization of the signed displacement and positive key, before applying observation-rank/signature predicates.

**Proof.** No available operation has positive net E2 displacement. The b operation has net -2E2, therefore every valid word has count(b)=0. Only e and a have nonzero E1 net (+2E1 and -2E1, respectively), so count(e)-count(a)=1. A complete positive key's E3 count is precisely count(e)=z. Write r=count(c)+count(d). Direct counting gives x=2z+r+count(f), y=r+count(g) and h=count(a)+count(e)+r+count(f)+count(g). Solving these four integer equations yields the displayed counts. Conversely, any nonnegative solution can be ordered into a word; set count(c)=r and count(d)=0. Every operation has the specified native signed steps, so the resulting net and positive key follow directly. QED.

**Corollary 1.1:** x+y=h+1+r >= h+1. In particular every valid h9 key satisfies x+y>=10.

**Corollary 1.2 (adjacent-horizon common key):** When K is feasible at h, it is feasible at h+1 precisely when r_h>=1. The counts change by r_(h+1)=r_h-1, f_(h+1)=f_h+1, g_(h+1)=g_h+1, with a and e unchanged. In terms of operation multiplicities this exchanges one c/d for an f plus a g. Observation transfer maps still depend on the ordering; the equality of positive keys does not by itself guarantee rank-nine transfer coverage.

**Corollary 1.3 (EC49FAB explicit four-case restriction):** All complete positive keys appearing in each of the four published 76-edge H8 witnesses (source ranks 1512,1513,2200,2203) satisfy x+y<=9. Thus simply keeping their existing five H8 keys and adding an h9 word cannot yield an H9/M5 witness. This is a scoped result about four constructions, not a universal prohibition on five-key H8 schedules.

**Finite key census:** The explicit integer count parameterization gives exactly 70 feasible complete positive keys at h8, 95 at h9, with 50 common keys. These key sets impose no observation requirements; the complete enumerator is in VERIFY_EC49FAJ.js.

## Theorem 2: four lawful 94-edge H9 constructions, with their fifth key reused

For each of the four author-side EC49FAB 76-edge witness selections, retain its h2,...,h7 word families unchanged. Let its two h7 words be p and q. Replace the eighth horizon with (pc,pd,qc,qd), and define the ninth horizon by (pfg,qfg). This yields four H9/M5/S<=6 witnesses.

The first seven horizon families are provided explicitly in VERIFY_EC49FAJ.js; the complete newly selected h8/h9 paths for all four source ranks are recorded in EXACT_REPORT_EC49FAJ.json. The full-key coincidence and exact resource counts are:

| Source rank | Shared complete h8/h9 key | Cumulative E at h7,h8,h9 |
| --- | --- | --- |
| 1512 | (5,5,1,0,0,0) | 72,88,94 |
| 1513 | (7,3,1,0,0,0) | 72,88,94 |
| 2200 | (5,5,1,0,0,0) | 72,88,94 |
| 2203 | (7,3,1,0,0,0) | 72,88,94 |

All 32 per-case/horizon observation matrices have rank exactly nine over Q, checked by nonzero rank modulo the prime 1,000,003, which implies rank nine over Q because each matrix has nine rows. Every operation word was expanded to its ordered signed six-axis primitive sequence. All words have the exact target net displacement. Every horizon has one complete positive BRC key, with five distinct keys and six distinct transfer signatures globally.

**Independent combinatorial cost calculation:** The two h7 root words have already contributed their full primitive prefixes. From these two roots, four h8 terminal c/d branches each contribute four distinct primitive edges: 16 new edges. Each of the two h9 fg suffix paths has four primitive steps, but its first f step shares the first c step after its respective h7 root. These are the only two shared post-h7 edges. Hence the h8/h9 extension uses 16+(8-2)=22 new edges, totaling 72+22=94. The verifier independently recomputes the full signed-prefix union after each horizon. The observed cumulative counts are [28,42,58,64,68,72,88,94] for ranks 1512,1513 and [28,42,46,62,68,72,88,94] for ranks 2200,2203.

The code is self-contained, using native signed step expansion, nine-history bucket transfer, modular Gaussian elimination, count-based key census and exact prefix-set construction. Run:

    node VERIFY_EC49FAJ.js > EXACT_REPORT_EC49FAJ.json

The script at this publication is byte-for-byte identical to the actually executed Node v22 source; its remote Git blob can be compared to local Git blob b47310070d1815fafe59b3d3aff477f7dd30ee7b. This is an author-side finite construction and symbolic proof; independent Driver audit and Source-native mathematical admission remain separate.

## Next unit EC49FAK

Classify the 50 arithmetically common h8/h9 keys using actual nine-history rank and <=6 signature predicates. Search joint h8/h9 prefix covers, preserving the full signed primitive history and all five global positive keys, for an explicit E<=93 witness or an exact lower-bound certificate for a precisely scoped family. The four 94-edge constructions provide a reproducible baseline for both key-reuse variants; retain EC49FAI's separate four-key H8 extension as a second valid baseline. In parallel, invite independent Driver verification of upstream author-side H8 optimality and the EC49FAI terminal separation proof.

## Parent artifacts

- EC49FAI ADDENDUM_H9_TRANSFER.md, VERIFY_EC49FAI_H9.js and EXACT_REPORT_EC49FAI_H9.json at immutable project commit bcf6023beef5dadaeecf85b49979e212fbf485e4, Draft PR #1730.
- EC49FAB four 76-edge source constructions, source ranks 1512,1513,2200,2203, from prior same-PR author research; the h2..h7 words required for reproduction are embedded in the attached script.
- P000 and ACTIVE worldview preserved; no assertion of physical Heartbeat dynamics or full native three-dimensional slice evolution.
