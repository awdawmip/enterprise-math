# R743 — Two-token causal PASS compensation for rooted BRC triad loops

Date: 2026-11-12 (Asia/Shanghai). Status: AUTHOR-SIDE CONDITIONAL EXACT CONSTRUCTION; independent mathematical review pending.
Parent: RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142.
Frozen P000 science: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
BRC triad networks and V17 holonomies: R739@d0d37ca56ef32c5772cd7566c0826ff060d45f25 and R741@e3b3e7ec3685ac97f0e3a923c75abc3ad61e49c6.
V29 event grammar: research_notes/X6_NETWORK_EVENT_LEDGER_AND_CONTRAST_TRANSDUCER_V29_20260906.md@30fb16d39465708fd1b54c70a58d06ad20f310f8.
R742 predecessor: 2026-11-12_R742_periodic_twoport_zero_contrast_S3.md@6ef1423b4689dc691e94a19470d69210908ff8ee.

## Scientific question and modified interface

R742 constructs a two-port, four-PASS generator lift using three units of circulating stock, by using the fixed R741 per-arc codebook and placing one compensating PASS only after returning to the root triad. Does the minimum fall to **two stock units** if (i) we recolor the seven selected arcs consistently with source-conditioned decoding and (ii) permit one tagged, holonomy-identity PASS *during* a generator when its next selected arc requires it?

Keep the exact rooted loops and named V17 relations:

| carrier | I | P | Q |
| --- | --- | --- | --- |
| A | 012→014→013→012 | 012→023→013→012 | 012→023→123→012 |
| B | 012→123→124→012 | 012→023→013→012 | 012→123→013→012 |

Each of the three arc transitions emits exactly one offdiagonal V29 PASS. A separate identity PASS is emitted once per three-arc generator, tagged as an auxiliary stock-move: it preserves the current active triad, its nonzero force-source tokens, the certified TRIADIC_CLOSURE_E incidence witness, and the V17 slot mapping. Port directions F=PASS(0→1), R=PASS(1→0) act on a candidate local conserved stock b=(b0,b1) by F:(b0−1,b1+1), R:(b0+1,b1−1), subject to nonnegativity. This is a declared stock-moving refinement and guarded coupling, **not an original V29 stock rule or an established native X6 event permit**. Each arc retains its full source, target, prior vertex, BRC branch and event provenance. The two local ports are not two X6 spatial axes.

## Theorem 1: two tokens and four events are sufficient

Use common initial stock (1,1), with each port capacity 2. The source-conditioned arc PASS tables are:

| A arc | pulse | B arc | pulse |
| --- | --- | --- | --- |
| 012→014 | F | 012→023 | F |
| 012→023 | R | 012→123 | R |
| 014→013 | R | 023→013 | R |
| 023→013 | F | 123→013 | F |
| 023→123 | R | 123→124 | R |
| 013→012 | F | 013→012 | F |
| 123→012 | F | 124→012 | F |

Outgoing arcs from each source have distinct pulse labels. The three raw arc codewords and the single identity helper produce:

| carrier | generator | three arc pulses | helper timing | four actual PASS pulses |
| --- | --- | --- | --- | --- |
| A | I | FRF | R at root after arc 3 | FRFR |
| A | P | RFF | R at root after arc 3 | RFFR |
| A | Q | RRF | F after arc 1, before arc 2 | RFRF |
| B | I | RRF | F after arc 1, before arc 2 | RFRF |
| B | P | FRF | R at root after arc 3 | FRFR |
| B | Q | RFF | R at root after arc 3 | RFFR |

The early F is enabled after the first R and immediately before the next R, guarded by the *currently selected next source arc*: A on 023→123; B on 123→124. Thus it needs the present state and selected immediate transition, not the future generator word. All other helpers occur at root after returning from triad 013.

The possible four-event words, with stock prefixes, are:

- FRFR: (1,1)→(0,2)→(1,1)→(0,2)→(1,1);
- RFFR: (1,1)→(2,0)→(1,1)→(0,2)→(1,1);
- RFRF: (1,1)→(2,0)→(1,1)→(2,0)→(1,1).

All are legal, return to (1,1), have exactly two F and two R events and retain the original three-arc holonomy. Any concatenation is therefore legal by induction and satisfies for every k≥0:

    M = [[0,2k],[2k,0]], Rin=Rout=0,
    Omega=0, u=0, Gamma=4k, b=(1,1).

At k=3, twelve actual PASS events give all six distinct final named V17 relations, with the same M, same stock, same root triad and source-attached closure inventory. The six witness generator strings are III, IIP, IIQ, IPQ, IQP, PQP, with names exactly as in R741/R742. Thus the terminal count-stock observer retains a six-element holonomy fiber.

## Theorem 2: resource optimality within the one-PASS-per-arc class

Fix two offdiagonal ports, three rooted arcs per generator, source-conditioned injective arc labels, no auxiliary event *before* the first arc and a common stock state restored after every generator. Let every primitive arc still emit exactly one PASS; auxiliary events also consume actual PASS counts.

**Stock lower bound.** At root 012, two distinct outgoing arcs require different first pulses F and R, so the common starting stock must have at least one unit on **both** ports; at least two conserved units are necessary. Theorem 1 attains two, with each port capacity 2.

**Event lower bound.** A return of two-port conserved stock requires equal F and R counts, hence an even number of PASS events. Each generator has three mandatory arc PASS events, so it needs at least one additional PASS and at least four in total. Theorem 1 attains four.

**Sharp root-only obstruction for two stock units.** Under stock (1,1), the initial arc pulse cannot be followed immediately by the same pulse: FF or RR would empty its source port. In carrier A the branch 012→023 has two possible next arcs, and in carrier B the branch 012→123 has two possible next arcs. Injective coding at that second source requires both labels F,R, so one of the next arcs repeats the root pulse and is stock-inadmissible. A helper placed only after the three arcs cannot repair this prefix. Thus root-only compensation requires at least three stock units for **every** source-injective one-PASS-per-arc codebook, not merely R741's chosen assignment. An early helper is required on at least one of the three generator types if the stock is two. Theorem 1 uses it for just one type (A:Q, B:I).

The new two-stock construction changes the *scheduling location* of the compensating event and the selected per-arc codebook. R742's three-stock lower bound remains correct in its fixed-codebook/root-refill subclass.

## Verification, BRC observer scope, and next experiment

The accompanying standalone Python standard-library checker builds both seven-arc codebooks, verifies source-local injectivity, each four-event stock prefix, the 9,841 histories of generator lengths k=0..8 per carrier (19,682 total), the six relation witnesses, and independently enumerates **all 32 locally injective two-color arc assignments per carrier** to certify that no stock-two root-only model passes the first three event prefixes. It returns exact integer JSON with status PASS. All-k claims are proved by the per-generator stock-reset invariant and S3 multiplication, not by finite extrapolation.

BRC positive history weights and distinct source paths are preserved until the explicitly declared terminal count-stock projection. The projection is exactly six-to-one on the exhibited named-relation witness set; its operation-safe repair is the retained S3 relation register, not a claim of erasure of native event time. A candidate S6 axis-label covariance is obtained by transporting the entire force-source/closure/triad/codebook structure, keeping local port F,R distinct; this is the same restricted relabeling action as R741.

**Next discriminating unit:** test whether one correctly typed native X6 scheduler is permitted to emit the identity holonomy PASS at an intermediate triad as a dependency of its immediately selected next arc, while maintaining three nonzero force quanta, Cell attachment, TRIADIC_CLOSURE_E incidence, signed-axis provenance and rotation interlock. A denied intermediate identity event would identify a specific source-level guard to reformulate; permitted events would enable the two-unit realization at the actual native event interface. This note does not declare a new P000 primitive or an admitted Source Result.
