# R69 — Full integer-bit and memory crossover of circle-source certificates

Scientific input frozen: 43ec6098b1330ae86d0a7863be336c5d97f6ef34. No alteration to P000 or native BRC/Heartbeat assertions.

## Verified R68 frontier
For one fixed immutable source subtree and exact query signature, two positive closed rational parameter intervals containing the same anchor may be replaced by their exact union hull. Bounded LRU eviction is sound. On 80 exact rational models, 1,600 matched queries and 8,000 exact oracle checks per variant, R68 used 6,067 source rectangle computations versus R67's 6,883 and uncached R66's 7,959. Cap 16 or 64 had the same hits in clustered order. An adversarial 17-label alternating schedule forced cap-2 to zero hits and 630 computations; 400 unique signature queries also had zero hits. Linear certificate scanning was faster than the tree/hull on tested small inputs.

Source: research_notes/brc_s23_av_anchored_hull_20261111_r68/PROOF.md, check_r68.py, R68_CERTIFICATE_SUMMARY.json, inherited exact R67 kernel at research_notes/brc_s23_av_certificate_cache_20261111_r67/check_r67.py.

## Executable unit
Measure end-to-end integer numerator/denominator bit work, gcd, sorting, source-to-phase conversion, persistent-tree building/path-copy allocation and live/cache peak memory. Match linear R62/R64, point index R63, uncached interval R66, list cache R67 and hull cache R68 under their **same single-label interval-certification observer and deletion scope**. Start with n=16,64,256,1024; m=2,8,32; theta denominator bits=16,64,256; old root snapshots, branch-specific deletion, and sparse or frequent observation changes. Add exact large-time t ~ 10^18. Record any per-regime crossover or direct counterexample.

Test adaptive admission: estimate certificate expected reuse value relative to rational-key hashing, positive rectangle cost, retaining immutable nodes and eviction churn. Prove/adversarially validate that rejecting a cache insertion affects cost but never certification correctness. Retain branch IDs and original historical labels. Formal shared CLAIM, native Result and mathematical review require independently verified current authority.
