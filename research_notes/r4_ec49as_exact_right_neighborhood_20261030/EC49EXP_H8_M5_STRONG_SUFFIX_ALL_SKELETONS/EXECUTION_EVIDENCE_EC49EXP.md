# EC49EXP verification execution

The exact Python triple checker emits 123147 arrangements; E<80 exclusions 106924, survivors 16223; identical full histogram and eight-skeleton counts were obtained by a second JavaScript implementation.

The C++17 -O3 double-key checker, compiled with g++ -std=c++17 -O3, was executed over all 1866362 distinct complete key assignments in 32 realizable collision skeletons. Observed execution: 7.72 seconds / 1536 KB (one container sample). It emitted PASS, B_EXP min=54, max=113, E<80 exclusions 1371817, survivors 494545, E<=80 exclusions 1274217. The output includes an integer histogram and all 32 per-skeleton counts. An independent JavaScript exact key-census checker recovered 32 and 1866362 with matching per-skeleton counts. The original Python (slower) maximal-clique implementation independently exhaustively checked the eight smallest double-key skeletons, total 13114 assignments; the per-skeleton min/max and E<80 and E<=80 exclusion counters all matched C++.

The separate native word literal verifier enumerated h2=8,h3=51,h4=304,h5=1770 valid operation words, tested 141842 equal-key distinct word pairs for LCP<=L-3, 24288 cross-window same-key pairs, and 479436 sampled different-key pairs for the signed-histogram common-prefix bound; all passed. All arithmetic exact integer, with zero floating-point threshold comparisons.

For complete actual stdout artifacts, the corresponding standalone local evidence bundle from the same run is EC49EXP_COMPLETE_EVIDENCE.tar.gz with SHA256 b2d945f7786ae5df4361fdd73f187d2eb48831ba991bf121e430f50d1b288f23, shared as a conversation attachment. Rerunning the published executable source reproduces the full integer histogram.
