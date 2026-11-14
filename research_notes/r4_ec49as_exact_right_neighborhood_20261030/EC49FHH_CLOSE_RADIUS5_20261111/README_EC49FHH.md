# EC49FHH — Closed seven-key radius-five neighborhoods for both 94-prefix BRC witnesses (2026-11-11)

## Main finite theorem

Scientific pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Inputs: frozen nine-state BRC observer, all 178,850 legal operator words and their exact ordered signed X6 native microstep prefixes, original 24 observation labels, and EC49FGJ 7-raw-cache-key 94-prefix witness profiles A/B.

For either witness and for every set Q of at most five observation labels, keep the other 24-|Q| paths fixed and permit legal replacements of Q with at most seven distinct **full raw cache keys**. The exact minimum native prefix-union cost is **94**. Thus both witnesses are radius-five local minimizers; the unrestricted seven-key global minimum still has known upper bound 94.

## New decisive lemma: unique H2 path forces back the released key

After EC49FHE, EC49FHF and EC49FHG, exactly 52 five-label key-releasing Q positions remained per witness: 16 with B=17, 20 with B=19 and 16 with B=20, where F(Q) is the fixed-path prefix union and B=93-|F(Q)|. A complete enumeration of these Q shows that each releases **exactly one** original key, and each includes **exactly one H2** observation label. In the frozen complete catalog, both H2/16 and H2/32 have **one and only one legal operator word**. For every one of the 104 witness/position instances, that forced H2 word is identical to its original witness word and its raw key equals the key released by Q.

Therefore any legal replacement returns all seven original keys: six occur in the 19 fixed paths, and the seventh is forced by H2. A completion with at most seven distinct keys can use **only those exact seven original keys**. This is a necessary and sufficient reduction of the original key budget, not an additional restriction.

## Exact native-prefix computation

Let P(w) be the complete nonempty ordered signed-X6 prefix set of legal word w. For each remaining Q the frozen full catalog contains 9,838 candidate words using the original seven keys. The exact trie group-cover solver selects one legal candidate from each of five label groups and minimizes

    m(Q) = min | union_{i in Q} P(w_i) \ F(Q) | .

The rooted prefix-trie DP assigns edge weight 0 to prefixes in F(Q), weight 1 otherwise; each terminal marks the demand labels for which its full word is legal. At a node the exact subset convolution distributes required labels among children, counting shared native edges once. Induction over the trie gives the exact minimum over every legal candidate combination. The existing solver carries a literal direct-Cartesian-product check on artificial signed-prefix cases.

Executed on all 104 remaining instances: B17 -> min added=18 (16 per witness); B19 -> 20 (20 per witness); B20 -> 21 (16 per witness). Every instance therefore has total |F|+m(Q)=94; an unchanged 94-edge witness supplies the matching upper bound. The reproducible program asserted all values and produced BRUTE_CROSSCHECK_PASS and EC49FHH_EXACT_PASS. Exact per-instance JSON (31,665 bytes) is losslessly stored as gzip+base64, SHA256 e199828a686ff768acbe1b2ff08c18d82453afee85e81ff919febd1969d2c869 after decoding.

## Full radius-five finite conclusion and provenance

Prior results establish all 25,158 Q sets per profile retaining the seven baseline keys (EC49FGX–EC49FHD) and the 17,346 key-releasing sets: 4,576 with fixed background already costing 94; 12,544 at B<=15 (EC49FHE); 62 high-budget exclusions via H9 pair (EC49FHF); 112 via H9/H8 triple (EC49FHG); and the final 52 treated here. Totals: 25,158+17,346=42,504 possible five-label sets per profile. Any smaller-radius replacement is a special case of a five-label replacement with unused selected labels retaining their original words. The existing radius<=5 theorem is therefore complete **within these two fixed witness neighborhoods**.

## Reproduce and status

From this directory in the PR branch, run: python VERIFY_EC49FHH.py. It imports the frozen generator and witness JSON from sibling EC49FGW_RADIUS5_EXACT_SCREENS_20261110, and the exact native-prefix trie solver from sibling EC49FHD_PREFIX_TRIE_RADIUS5_20261110; it regenerates the full report and checks the stated counts. Decode EXACT_REPORT_EC49FHH.json.gz.b64 with base64 and gzip to obtain the 104-case JSON. Original scientific pin and P000 are unchanged.

Status: AUTHOR_FINITE_THEOREM / EXACT_COMPUTATION_PASS / PORTABLE_DRAFT / INDEPENDENT_DRIVER_REVIEW_PENDING. A PR branch is durable scientific evidence, not canonical mathematical admission. The historical EC49AS formal task does not acquire CLAIM/Result by this publication.

Next research: begin radius-six exchanges or a global seven-key construction/lower-bound search. A potentially useful optimization is the key-forcing lemma as a preprocessing rule: an obligatory unique-word label may fix a key budget before any costly prefix-union DP. Reassess the mother problem C_min(7) ?= 94 independently of local-neighborhood optimality.
