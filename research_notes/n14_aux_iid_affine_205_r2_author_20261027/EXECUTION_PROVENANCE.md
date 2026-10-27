# Stage205 executable evidence and provenance — 2026-10-27 Asia/Shanghai

Parent: Stage204 immutable commit e067bd3fa3fd6809a7fabc19cedfb7f4f04f481d, existing Draft PR #1571. All code uses Python standard-library Fraction and exact integers; no numerical approximation, hosted CI or network experiment. Global read snapshot 9c2677392c705fdb68294188ba38b24ae9e2cffd; EM control snapshot 3bc9cebddc821dcf38dfad011fdfc148ec47885d.

Observed local primary output: `STAGE205_AUTHOR_EXACT_FULL_REAL_PASS 329164`. Four deterministic policies' independent conditional-suffix DP and full unmerged integer-numerator DFS observations matched; node counts 84856+84856+79726+79726=329164. Only two Bellman ties T=(12,3,1) P/C and Z=(14,0,0) P/Q; 680 states and 1238 positive gaps. Mixed four-vector is exactly zero, z(u) feasible on [0,1], both time differences >0 and both balanced endpoint Lagrangians equal H205.

Observed separate standalone reference run: `STAGE205_REFERENCE_EXACT_PASS 329164 width 5083984375/71328803586048 slope 32400/137`. Actual executed script supplied as REPRO_STAGE205.py.

Observed Stage206 scan: `STAGE206_DUAL_SCAN_PASS`; actual code supplied as scan_stage206.py. Exact scan gives first switch (5,0,1) C->Q; K206=25155568056/213144883 and exact dual contact identity. This is a Stage206 **dual-only** result.

Native current-task listing requested this turn returned `CONTROL_QUOTA`. This GitHub author contribution is PORTABLE_AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED. Active task owner, Source CLAIM/Result and independent Driver review not established. Remote source readback establishes persistence, not remote execution or separate mathematical review. Source project P000 V5 is not altered or claimed by external IID computation.