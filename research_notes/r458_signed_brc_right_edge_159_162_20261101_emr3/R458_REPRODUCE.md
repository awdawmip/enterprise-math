# R458 reproduction and portable handoff

Scientific unit: signed BRC right-edge s=159,160,161,162; extra explicit leading coefficient formula for all s>=4; r=183,185 entire-row checks. Reviewer status UNREVIEWED / NOT_ADMITTED.

Fixed knowledge snapshot: GLOBAL_KNOWLEDGE_V1 main@301e34842658e23e49724e5dd846a9952258ba50; EM main@96dbd541e2c8f4f873aaf4ee37a42cf6af0f3278. Prior source R457 PR #1708 head 10b55e0d7da1ff24372b7a698bb9bd19cf6c4333.

Use Python 3 with arbitrary-precision built-in integers. In this directory, run each separately:

    python R458_VERIFY.py 159 159
    python R458_VERIFY.py 160 160
    python R458_VERIFY.py 161 161
    python R458_VERIFY.py 162 162
    python R458_ROW_VERIFY.py

Each solo certificate run prints RAW PASS and R458_EXACT_PASS; its R458_EVIDENCE.json is overwritten by the next run, so retain or rename individual generated results. R458_EVIDENCE_ALL.json is the consolidated summary and expected order-specific hashes. The exact polynomial SHA256 algorithm is in R458_VERIFY.py; it hashes order, polynomial length, and length-prefixed unsigned big-endian integer coefficients. Row streams use different documented length-prefixed encoding. Leading-coefficient analytic identities and nine small-s checks are described in R458_PROOF.zh-CN.md.

All 4 s checks completed separately. Source lineage: R458_VERIFY.py is bytewise R456_VERIFY.py with the substring R456 -> R458; row verification adjusts r to 183,185 and expected counts. Raw signed convolution and positive Catalan expression were crosschecked. No floating-point sign test or formal-admission claim.

BRC observer: exact signed-to-scalar auxiliary map, no native six-axis X6/three-dimensional-slice isomorphism asserted. Next task is s=163/164 or uniform positive lower-coefficient proof. GitHub PR handoff carries research notes; gateway active owner lookup returned CONTROL_QUOTA and authority_granted=false.