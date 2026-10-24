# R259 — uniform three-way BRC provenance collisions at every future depth

**Date:** 2026-10-24. **Status:** UNREVIEWED AUTHOR-SIDE EXACT MATHEMATICAL DRAFT. This paper is a scoped result in the R256–R258 finite positive-branch affine model; it does not establish R193's actual observer, native P000 heartbeat admissibility, a formal task CLAIM, or independent mathematical acceptance.

## Frozen inputs and typed scope

Read authority: GLOBAL_KNOWLEDGE_V1 main@3c2c0e673b75da00e683abd1c43300b346b9d62e, P000 startup and matching original P000 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc (ACTIVE_LOCKED). Enterprise Math Source read pin: main@cfcb4de1bff4d5b533108937068af754f71b84b7. Exact native interfaces inspected: src/enterprise_math/brc_transport.py and src/enterprise_math/brc_control_port.py; portable rule docs/PORTABLE_RESEARCH_PROTOCOL.md. R258 source: immutable commit d5d0d02db58ec917ede3d48615b77e7bd586787c, research_notes/R258_SEVEN_REACHABLE_PRODUCT_STATES_MINIMAL_QUERY_20261024.md.

The model uses original nonspatial controls Q={0,1,2}, distinct source-edge selectors a in {0,1}, path weight 1 and positive raw multiplicity 1 on each edge. From q, selector a determines (next q, affine sign eta, translation b on native E1):

    q    a=0                  a=1
    0    (2,-1,-1)            (2,+1,-1)
    1    (0,-1,-1)            (0,+1,-1)
    2    (1,+1,+1)            (2,+1,-1)

The complete formal six-axis action is F_eta,b(z)=diag(eta,eta,1,1,1,1) z + b E1, relative to a chosen native Cell. First effect (eps,k) followed chronologically by an edge (eta,b) produces (eta eps, eta k+b), in the exact positive BRC Affine.then sense. The six spatial axes are retained; q and query state are *nonspatial*. Formal edge-word length is not calibrated heartbeat time. No final Cell address is emitted.

The three-state DFA R={0,1,2} remembers whether a source word contains substring 00. State 0: not seen, last symbol not 0; state 1: not seen, last symbol 0; state 2: already seen (absorbing). Its transitions and immediate Boolean observation g are:

    r        0-next       1-next       g(r)
    0          1            0           0
    1          2            0           0
    2          2            2           1

For a length-m raw word, define its *unmarked joint effect observer* O_m as (m, terminal original q, weight=1, complete six-axis affine effect). It deliberately omits the ordered raw source word and DFA mode. A richer future query asks for the Boolean source predicate now and under allowed future BRC compositions. Aggregated positive weights do not encode signed phase cancellation.

## Lemma 1 — three base fibres

Exact branch-by-branch composition gives the following groups. Within each row all three words share (terminal q, affine eps, translation k), while their final DFA modes are respectively 0,1,2:

    m    DFA-0 word     DFA-1 word     DFA-2 word      shared (q,eps,k)
    7    1110101        1011010        0000000        (2,-1,+1)
    8    11110101       10111010       00011010       (2,-1,+2)
    9    101101011      010101010      000000011      (2,-1,-1)

These are nine finite exact identities obtained by applying the displayed transition tables; both attached standalone integer verifiers explicitly reproduce them. Notice that applying a *common suffix* to the depth-seven triple need not preserve its three different modes; the following proof instead uses a common **prefix resetting the source monitor**.

## Lemma 2 — same-effect reset loops

Three words begin and end at product control (q,r)=(0,0):

    p = 101       length 3    affine (+1,-1)
    u = 1011101   length 7    affine (+1,-3)
    v = 1101101   length 7    affine (+1,-3)

In particular u and v are different raw ordered source histories even though their original control, source-monitor mode, path weight and complete six-axis affine effects agree. Prefix concatenations of these words reset to (0,0), have affine sign +1 and offset equal to the sum of their listed offsets.

## Theorem — uniform three-way collisions with exponential raw multiplicity

For every integer m >= 7 there is at least one *single* unmarked joint effect fibre O_m containing histories with all three possible DFA modes. Explicitly, choose the unique j in {7,8,9} with j congruent to m modulo 3, then write

    h=(m-j)/3 >=0,    h=7K+r,   0<=r<7.

Thus m=j+21K+3r. Construct a prefix from 3K independently chosen seven-letter blocks, each selected from {u,v}, followed by r copies of p. Every such prefix has length 21K+3r; it resets product control to (0,0), and has the *same* complete affine action (+1,-9K-r). Exactly 2^(3K) distinguishable raw prefixes arise from the choices of u versus v.

Append to any such prefix one of the three base words of length j in Lemma 1. Because each suffix starts from (0,0), its own control/DFA evolution is unchanged. Each resulting full word has the same original terminal control 2 and the same six-axis affine action

    (eps,k) = (-1,b_j+9K+r), where (b_7,b_8,b_9)=(+1,+2,-1).

Indeed chronological affine composition changes the prefix translation -9K-r by suffix linear sign -1, yielding +9K+r, and adds the suffix translation b_j. For *each* final DFA mode there are at least 2^(3K) different positive-weight raw histories with this exact observer. Therefore one complete-effect fibre has at least 3*2^(3K) histories and represents all three source-query modes. This proves the assertion for **every** m>=7, not only a tested finite range. QED.

## Consequences and precise limits

1. Even terminal control, full six-axis affine effect, total path weight and known step depth do not determine the current substring-00 query for any m>=7: same fibre contains g=0 and g=1 histories.
2. A fixed *one-bit* residual attached to an individual history cannot preserve the full current-and-future query mode on these fibres. The three modes are right-distinct: r=2 is accepted immediately; r=0 and r=1 currently reject but differ after selector 0, because delta(0,0)=1 and delta(1,0)=2. The complete two-branch BRC packet also distinguishes them in the query-resolved future histogram: at original q=2 its selector-0 edge has distinct destination q=1 from selector-1 destination q=2. Hence at least 3 residual values (2 fixed binary bits) are necessary *for this fibre* for all-future query preservation.
3. Recovering **all individual raw histories** within the single constructed fibre requires at least ceil(log2(3*2^(3K)))=3K+2 extra binary tag bits in the worst case. This is only a constructive lower bound, not the exact global maximum-fibre size or a replacement for R254/R255's sharper general asymptotics.
4. For m=7+21K the displayed fibre has at least 3,24,192,1536,12288,98304 raw histories at m=7,28,49,70,91,112. At *every* other m>=7, bases j=7,8,9 and the three-letter loop fill the missing residue classes.
5. This is not a proof that all globally effect-aware BRC representations require seven control states: R258's seven-state minimality applies only to its deterministic Moore interface. This theorem supplies a *persistent 3-mode local lower bound* for any representation that must answer these future queries on the displayed fibres.

## Verification status and continuation

Author-side Python exact BRC branch-count propagation: all depths 0..128, all 2^m raw words independently enumerated for each m<=12, positive total multiplicity 2^m, first triple at depth 7, reset identities and bases, lower bound for each m>=7, explicit six-axis diagonal/offset checks. Author-side independent C++17 big-integer propagation: depths 0..128, first triple depth 7, all lower bounds, 2967 constructive sample-word evaluations up to length 511. Both PASS. Infinite-horizon conclusion relies on the preceding symbolic prefix proof, not on a 128-depth extrapolation. A fuller C++ source and cold-start bundle are supplied in the corresponding local R259 research evidence package; this GitHub note and its companion Python verifier/report retain the exact resumable mathematical frontier.

Native source was **inspected but not imported/executed**; no Source Result, active OWNER/CLAIM, independent Driver review or R193 transfer is asserted. Native control dispatch for this author run returned CONTROL_QUOTA. This research source is a draft, not promotion or acceptance. The original R193 labelled-edge, observer and time-port source remains to be fetched; a valid mapping to this query model and a native P000 heartbeat update proof are pending.

**R260 next scientific action:** locate the immutable true R193 source-edge and future-query contract, prove a typed observer-preserving embedding or a minimal obstruction, and run original ControlPacket.from_edges / then / EffectHistogram against the exact R259 edge schedule in a permitted, pinned Source environment. Separately test whether an effect-aware global control quotient can reduce seven states without violating the unavoidable 3-valued source modes on these fibres.

Global-Knowledge-Sync: main@3c2c0e67 / GLOBAL_KNOWLEDGE_V1
