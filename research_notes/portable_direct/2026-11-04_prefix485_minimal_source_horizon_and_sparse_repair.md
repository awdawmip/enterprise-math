# PREFIX-485 — Sharp four-step source-order witness, finite-horizon quotient and sparse integer repair

Date: 2026-11-04 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED. Author-side portable result, not an authenticated TASK Result or physical-time/phase-dynamics claim.

## Provenance and exact model

Continue PREFIX-484 at `bd0f7743c4d1493c2bc944d525dd72aebbd4efc2`; immutable task scientific input pin `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Current behavioral authority was read separately from global 00_BOOTSTRAP/OPERATING_MANUAL, project P000 and ACTIVE Heartbeat X6, joint observer-preservation, docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context, docs/PORTABLE_RESEARCH_PROTOCOL.md and research_priorities/research_method.json.

Use an explicitly embedded ordered-path observer inside six native spatial axes X6: ten signed ordinary primitive steps a/A,b/B,c/C,d/D,e/E, and special x as first step or after KMP gate w (w=aab or aba in computations); x resets KMP state. Ordinary letters are always legal. This is a restricted observable, not a replacement for native X6, ordered provenance or time.

Let u_i,v_i count positive/negative occurrences, y_i=u_i-v_i, p_i=min(u_i,v_i), s=#x, and M have three rows:
    (1,1,1,1,1)
    (0,1,0,2,1)
    (0,0,1,0,1).
Observe O=(s,y_a,y_b,y_c,y_d,y_e,V,W), where (S,V,W)=Mp; n is external word length. The KMP suffix state q is retained. A source automaton t has N (no b/B/c/C yet), B (first b/B), C (first c/C). B,C are absorbing. The requested Boolean output F=1 exactly in state B. Source does not control legality.

## Theorem 1 — exact horizon-H quotient of the source residual

Fix any n, w and any nonempty BRC-KMP base fiber (O,q), and let T subseteq {N,B,C} be source states realized by legal paths in it. Two source histories are equivalent at horizon H if F agrees after every common legal suffix of length <=H, including the empty suffix. Then

    classes(H=0) = 1 + [ B in T and (N in T or C in T) ],
    classes(H>=1) = |T|.

Proof: at empty suffix B gives output 1 and N,C give 0, yielding the first formula (all T nonempty). For H>=1, the ordinary suffix b is legal from every q and sends N to B but C to C; thus N and C differ. B already differs from each at the empty suffix. The three-state deterministic source automaton tracks F under every longer suffix. Base O/q updates depend on the appended direction, not source; legality depends on q alone. This is an exact future-safe factorization for this specified Boolean observer, not full ordered-path recovery.

## Theorem 2 — sharp shortest three-source witness

For w=aab and w=aba, length n=4 is the minimum length of a BRC-KMP fiber realizing N, B and C simultaneously. Explicit paths are

    aAeE  : source N
    bBcC  : source B
    cCbB  : source C.

All three are legal, with n=4, s=0, signed displacement y=(0,0,0,0,0), (S,V,W)=(2,1,1), KMP q=0 and native positive path weight 216 (positive ordinary weights 6,12,18,24,36 and all negative weights 1). F at the empty suffix gives (0,1,0), and after suffix b gives (1,1,0).

Proof of minimality: suppose n<=3 and the same base fiber realizes N,B,C. N contains no b/B/c/C, hence common y_b=y_c=0. A B history then must contain both b and B, so p_b>=1; a C history must contain both c and C, so p_c>=1. The elementary identity 2 sum_i p_i = n-s-sum_i |y_i| implies sum_i p_i<=1 for n<=3. Thus for B its only nonzero pair count is p_b=1, giving (V,W)=(1,0), while for C only p_c=1, giving (V,W)=(0,1), contradiction. The length-four construction attains the lower bound. This improves the prior length-twelve lower-bound witness, and is independent of finite search.

## Theorem 3 — explicit sparse additive repair

For the above M, retaining p_d and p_e alongside (S,V,W) exactly recovers all five cancellation counts:

    p_a = S - V - W + p_d + p_e
    p_b = V - 2p_d - p_e
    p_c = W - p_e.

An integral basis of ker_Z(M) is (1,-2,0,1,0) and (1,-1,-1,0,1), so ker rank is 2. Therefore two extra additive integer coordinates are necessary and sufficient for full p reconstruction in the fixed-coefficient additive linear class (PREFIX-483 rank formula); this direct codec has reconstruction coefficients of magnitude <=2. A signed primitive append increments p_d or p_e only on a cancellation event on that axis, and updates all components exactly.

Each p_d,p_e is in [0,floor(n/2)], giving the elementary fixed-width bound 2 ceil(log2(floor(n/2)+1)) bits for these two residuals, in addition to baseline observation and KMP history. The source carrier adds at most one bit for horizon H=0, and two bits for H>=1 on a fiber where all three classes occur. These source and additive coordinates preserve different observable distinctions. A full Smith transform provides a general integer-lattice certificate for arbitrary observation matrices, but dense transform coefficients are unnecessary for the fixed sparse M here. The stated update/decode costs are constant-time arithmetic counts for the fixed observer; no general bit-complexity superiority is asserted.

## Executed exact integer certificate

The companion Python-standard-library program `prefix485_certificate.py` implements (i) compressed BRC-KMP-source ordered-path multiplicity DP and (ii) an independently aggregated KMP-source automaton DP. It checks total paths and each source population for n=0..8; source words and legal append are checked directly. A second independent local program `prefix485_source_minimal.py` also performed direct ordered-word enumeration for n<=3, independently confirming the shortest-witness boundary. Exact whole-number results:

| gate | n | base (O,q) | H0 classes | H>=1 classes | 1-type fibers | 2-type fibers | 3-type fibers | ordered paths |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| aab | 4 | 1278 | 1541 | 1542 | 1015 | 262 | 1 | 11001 |
| aba | 4 | 1280 | 1543 | 1544 | 1017 | 262 | 1 | 11001 |
| aab | 6 | 10711 | 14582 | 14617 | 6840 | 3836 | 35 | 1100320 |
| aba | 6 | 10713 | 14583 | 14617 | 6843 | 3836 | 34 | 1100320 |
| aab | 8 | 58496 | 87405 | 87691 | 29587 | 28623 | 286 | 110054001 |
| aba | 8 | 58498 | 87381 | 87640 | 29615 | 28624 | 259 | 110054001 |

The executed certificate ends ALL_CHECKS_PASS. Finite DP computations are verified only for n<=8; Theorems 1 and 3 hold for their general stated domain by proof, and Theorem 2 gives a sharp infinite-length earliest witness. This study computes exact BRC positive-count observations and paths; it does not evaluate a native physical evolution, classical pi/trigonometric expansion, or phase/signed amplitude.

## Next precise research question — PREFIX-486

Determine eventual growth and rational generating functions of the number of base fibers with exactly 1, 2 or 3 source types, and explain the difference (286 versus 259 at n=8) between aab and aba. Cross-check lattice fibers with an independently derived symbolic/Presburger representation, and analyze whether horizon-zero source compression savings have an asymptotic density. Retain exact future operation and output scope when considering other provenance queries.

## Real authority

GitHub principal awdawmip was verified push/admin. Native Sites gateway at 2026-11-04T06:51:20Z reported static_machine_readonly and research_authority_granted=false. One current task list attempt returned CONTROL_QUOTA. No verified live owner, native CLAIM, authenticated Result, independent Review or Admission was obtained. This report is a durable author-side source artifact, and no previous-owner identity is borrowed.
