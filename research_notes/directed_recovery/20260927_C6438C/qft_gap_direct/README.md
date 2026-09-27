# Direct signed difference autocorrelation

An exact single-negative-bit modular pair query is reduced to two degree-three floor-moment tables per nonempty oriented displacement progression. One pure-direct actual run matches all 31 frozen signed answers, using 88,185 production digit replays versus 137,611 for the earlier one-window formula. Six tuples improve and three worsen. The two costly nontrivial interior cases improve from 14,999 to 9,757 and from 49,560 to 23,230. Existing endpoint and zero shortcuts remain useful; the pure-direct total exceeds the separate endpoint dispatcher's 68,824.

Let L=2^g, U=2^k, P=2U and H=L/P. The finite autocorrelation A(d) of w(x)=(-1)^(bit_k(x)) has two affine-in-remainder branches. With d=qP+s,

    A(d) = (H-q)(P-4s)+s                 for 0<=s<=U,
    A(d) = (H-q)(4s-3P)-3s+2P            for U<=s<P.

The branch indicator is delta=floor((d+U)/P)-floor(d/P). Expanding A in d, q and delta and using differences of moment tables converts its sum over d=b+jR into fixed-degree floor sums. The full modular query uses heads r and R-r. Zero displacement occurs once, while identical nonzero progressions at r=R/2 still represent two orientations. DIFFERENCE_AUTOCORRELATION.md gives the derivation; DIFFERENCE_REVIEW.md and guard_review bind its review.

The actual implementation preserves full moment tables, signed coefficient operations, exact divisions by two and six, complete native digit traces, positive fresh replay and six paid failed replays. It uses 118 top-level tables, 128 production moment nodes and 204 production moment requests on the declared fixtures. Total production plus all fresh replays is 191,601 digits. One actual full-adder kernel observation is reused, not treated as the whole computational cost. See direct_gap/DIRECT_EXECUTION_NOTE.md for every tuple and the resource categories. The approximately 16.254-second checker time is not a matched timing ratio.

The raw 4^-g normalization and negative answers are retained. This is a stride-one scalar query for a supplied positive counting modulus. It does not discover multiplicative orders or addresses, solve arbitrary Walsh masks, or establish a small full-matrix Gram process. The fixed-degree reduction and its bounded actual costs do not close general Shor dequantization.

LSB_LIFT.md and its symbolic review give an unexecuted extension: multiplying fixed scalar weights by (-1)^x reduces the lifted query to one existing query when R is even, or a signed difference of two queries modulo 2R when R is odd. For a single-bit input at k>=1 this covers the two-bit family {0,k}. It does not identify physical semiclassical histories after their other matrices change. No two-bit execution is claimed by the 31 single-bit fixtures.

Complete gzip evidence, summary, stdout, source and metadata-only readers are preserved. Readable evidence restores the exact original gzip; the backup contains it as well. DEPENDENCIES.md pins the external runtime and historical comparator. CONTINUE.md supplies portable mathematical and implementation successors. Source publication and backup are bound by separate actual delivery receipts. Author/shared-context research is not formal admission, and P000 is unchanged.

Global-Knowledge-Sync: main@f8aa9c8 / GLOBAL_KNOWLEDGE_V1
