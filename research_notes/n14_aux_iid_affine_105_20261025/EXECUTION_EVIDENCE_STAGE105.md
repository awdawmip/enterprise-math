# Stage105 actual local exact-run evidence and provenance

Date: 2026-10-25 (Asia/Shanghai). Scope: external iid N=14, **author checks only**. Input: GLOBAL_KNOWLEDGE_V1 main@4292cf9480b01650cccdda42b811dd2de3057aec; prior Stage104 source and certificate. The two Python 3 programs run locally using built-in fractions.Fraction, without floating-point approximation.

## Run A — exact Bellman, P/Q moments, next dual breakpoint

Executed: python derive105.py

Observed mathematical output:

    states 680; comparisons 1240
    tied states exactly (12,0,1): (Q,C) and (8,5,1): (P,C)
    strictly positive gaps 1238; min 2872871/430414776
    negative gaps 0; predecessor dual equality difference 0
    first A: count 112, P=175/1769472, Q=175/6718464
    first B: count 12, P=48828125/725594112, Q=48828125/362797056
    suffix A: 229681/47775744, 182623/186624, 86903/73728, 42763/31104; 105 terminal words
    suffix B: 63/64, 1/144, 9/8, 13/12; 5 terminal words
    compensation c=849554069/1632000000000
    eta=348715675/4850358643851264
    alpha105=38038153259411651/109561042308169728
    V105=353483207227801957/27390260577042432
    dual slope gamma=4323250440/1992661
    pinned dual gaps at K104 and K105 nonnegative: PASS
    midpoint primal tuple = arithmetic mean of endpoints: PASS
    tP > tQ at both endpoints: PASS
    next dual-only K106=107892/101; state (11,5,4); action C
    final: STAGE105 PASS

## Run B — separately coded top-down Bellman + actual ordered-word DFS

Executed: python independent_ordered105.py

    PASS first hits, A count=112, B count=12
    u=0:   1,013,272 visited ordered-prefix DFS nodes; 675,515 visited terminal words; root moments PASS
    u=1:     995,800 visited nodes; 663,755 terminal words; root moments PASS
    u=1/2: 1,013,272 visited nodes; 675,515 terminal words; root moments PASS
    final: PASS_INDEPENDENT_ORDERED_STAGE105

The two programs were genuinely executed and the full outputs stored in the local reproducibility bundle. They share the model assumptions and are both **author side**, hence they do NOT constitute an independent Research Driver review.

## Exact source identification and archive

The exact program source bytes executed locally have Git Blob identifiers:

    derive105.py                    b5ae700e3ba251f25c3125400384f2041dd82e86
    independent_ordered105.py       3719293f99e57e5e93d0797c1a09114206575d95
    certificate105.json             b124ac5b69f489b127b0ba83990ecdbc16db7a09

The corresponding files are now versioned under this research_notes directory on Enterprise Math main and their GitHub fetch_file immutable-commit readbacks matched their published contents.

Local ZIP: EM_R5_BRC_N14_STAGE105_EXACT_AFFINE_20261025.zip

    ZIP SHA256 = dd563f1d054ce27e11984266c607f23c20f6e7b8c2c6a0fb40f644e7904a4421
    ZIP files = 8 (full expanded proof, two scripts, JSON certificate, next packet, two raw logs, SHA256 manifest)
    ZIP CRC / per-file SHA256 manifest check = PASS.

GitHub PROOF_STAGE105.md and NEXT_TASK_PACKET_106.md are independently edited concise complete renderings, **not** byte-identical to the fuller local ZIP versions. The three mathematical machine files above have exact local/remote Git Blob equality.

## Limits / status

The native control task list reported CONTROL_QUOTA and session creation was denied with STATIC_READONLY_SCOPE_DENIED (operation_sent=false). No valid active owner or native Task CLAIM, Result freeze, Driver admission or P000 bridge has been verified. GitHub writing is an author-source artifact checkpoint; do not equate it to native control-plane authorization.