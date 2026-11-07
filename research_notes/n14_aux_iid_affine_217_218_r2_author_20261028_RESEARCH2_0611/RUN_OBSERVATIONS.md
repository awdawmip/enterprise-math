# Locally executed observation log — 2026-10-28 Asia/Shanghai

Source pin: GLOBAL_KNOWLEDGE_V1 main@d9859d053564a0c5b87ad606d6a885f85780880d.
Enterprise Math main@d69d13f84e26004821ff24936d750088065c4975; predecessor PR #1571 SHA 4b2ff184d394740b795b30efefb169ee293f1e2c.

## Primary exact Fraction + suffix DP + full unmerged integer P/Q tree
STAGE217_AUTHOR_EXACT_FULL_REAL_PASS 73672
Stage217: 680 Bellman states; 1238 strict positive action gaps; 4 corner visits 18457,18457,18379,18379; zero mixed coefficient; real coin endpoints in (0,1); tP>tQ; exact predecessor/successor contact.

STAGE218_AUTHOR_EXACT_FULL_REAL_PASS 66796
Stage218: 680 Bellman states; 1238 strict positive action gaps; 4 corner visits 18379,18379,15019,15019; zero mixed coefficient; real coin endpoints in (0,1); tP>tQ; exact predecessor/successor contact.

These primary executions used a local per-stage script retaining P and Q path weights as positive integers and a separate Fraction suffix DP; exact result certificates are saved as certificate217.json and certificate218.json.

## Separate independent-style reference implementation, actually executed
STAGE217_INDEPENDENT_EXACT_PASS 73672
STAGE218_INDEPENDENT_EXACT_PASS 66796
The full source actually run is REPRO_STAGE217_218.py in this directory. It implements iterative bottom-up Bellman and an explicit *ordered word* stack, independently checks the exact saved four-corner rational certificates and sign identities. No Python simulation of placement or P000 native X6 dynamics is claimed.

## Stage219 first-switch dual-only scan, actually executed
STAGE219_DUAL_SCAN_PASS
K219 314587800/3377071
H219 28050139715601809024924983/369995418708693051506688
new tie (9,4,3), C -> Q
680 Bellman states, 1238 strict gaps, minimum positive 7442425/1641256506.
The exact scan uses rational action-cost slopes and a backward recursion; cert in certificate219_dual.json. This is not a Stage219 primal proof.

Native em_status v0.6.11: research_authority_granted=false.
Native task lookup: CONTROL_QUOTA. Active owner not confirmed. No native CLAIM, Source Result, independent Driver acceptance or P000 change.
Local author identity for this distinct continuation: EM-R2-RESEARCH2-20261028-0611-LOCAL; not service issued.
