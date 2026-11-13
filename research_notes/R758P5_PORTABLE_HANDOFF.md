# R758P5 portable continuation — minimal flat S3 holonomy

Frozen scientific source: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Branch: research/r758p5-checkerboard-flat-holonomy-20261113.
Lineage: R758P3 PR #2204; R758P4 PR #2208.
Research unit: source-preserving candidate X6 three-axis closed signed-unit spatial paths, not an admitted primitive three-force event.

## Completed and verified

- Proved exact candidate S3 frame group normal form H(w)=r^q for all rooted signed-axis closed words, where q is alternating signed-by-position axis index in Z3.
- Explicit length-8 zero signed-area, nontrivial-frame loop W=(+0,+1,-0,-1,+0,-1,-0,+1); q(W)=2. Same length, same Cell and A=(0,0,0) as backtrack V=(+0,-0)^4, yet H(V)=e.
- Exact local CPython exhaustive enumeration of all 46,686 distinct nonempty closed words at lengths 2,4,6,8. No zero-area nonidentity frame before length 8. At length 8: zero-area e=12,882; r=48; r²=48. Every one of 96 anomalous words uses exactly two axes, repeated two signed occurrences each; 32 anomalies per unordered pair.
- Geometric interpretation: a Z3 checkerboard edge voltage omega(x->x+eps e_a)=(-1)^{parity(x)} a gives q as boundary circulation. Elementary square voltage is 2(-1)^{parity(lower-left)}(a-b). Ordinary projected area erases this parity-resolved circulation. Combined checkerboard face flux is surface independent via discrete Stokes; individual face parity tallies in Z3 need not be.
- W^m gives an unbounded zero-area residual family with holonomy r^{2m}. For every even L>=8, adding inverse backtracks yields equal-length area-zero conjugacy-separating examples.
- Exact verification source: research_notes/R758P5_VERIFY_ZERO_AREA_MINIMAL.py.
- Exact counts and witness: research_notes/R758P5_EXACT_OUTPUT.json.
- Full proof: research_notes/R758P5_ZERO_AREA_CHECKERBOARD_HOLONOMY_20261113.md.

## Remaining obligation and next discriminating task

The full P000 native triadic closure must be instantiated as an actual Cell/Link/Port event with legal incidence and demonstrated V29/V39 update mapping. Investigate whether there is a native checkerboard/frame voltage or a distinct source-preserving invariant, then test a zero-area native event family for frame sensitivity. Do not identify a signed spatial 8-step loop with primitive 3-force balance without the native event mapping.

## Ownership and adoption

This source is an independent author-side research supplement; neither activity metadata nor the branch/PR grants a winning CLAIM, a Source Result, a Driver review, or Foundation promotion. The owner of RS-X6-TRIADIC-CLOSURE-DYNAMICS must be checked through fresh control receipts before any protected task mutation. Avoid duplicating other active research. Parent task and frozen pin remain unchanged. Proof status is exact *within the declared candidate S3 connection*.

No credentials, secret keys or personal information are included.
