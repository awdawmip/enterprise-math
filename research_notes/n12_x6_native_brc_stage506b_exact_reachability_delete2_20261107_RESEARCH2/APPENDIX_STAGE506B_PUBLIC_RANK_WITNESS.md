# Stage506-B appendix — independent mask oracle and one-step public-rank obstruction

Date: 2026-11-07. Author-side exact finite evidence / mathematically explicit counterexample. Scientific pins inherit the Stage506-B proof.

## Independent oracle for the exposure DP

Executed `BRUTE_EXPOSURE_506B.py`, independent from the production `exact_mask` transition DP: it enumerates **all legal operation-type trees** on a sequence of original identities and inserted (-1) identities. Before each operation it records the original identities actually deleted, SET-targeted, or adjacent to the INSERT2 cut. Their initial end-offsets are compared with `exact_mask` after a full tree enumeration.

Domain: initial lengths n=0,...,10; horizons h=0,...,4; four offset sets R = {}, {2}, {0,3}, {1,2,5}. Thus **220 complete small-state cases**, all PASS. This independently tests exactness of the DP's *reachability classification*, whereas the main checker tests equality of compressed and full F future trees.

## Counterexample — one public-count scalar per opaque BRC gap is insufficient for ranked deletion

This is a new, separately scoped operation language extending Stage506 to `DELETE_LAST_PUBLIC`, which deletes the rightmost token tagged P. Consider two *already tagged* histories of length five with identical directions

`w=(+E2,+E1,+E1,+E1,+E1)`.

Source tags are
`x=(P,O,O,O,O)`,
`y=(O,P,O,O,O)`.

The word and its full F=(n,D,E) are identical in x and y. For Stage506 with h=1, R=∅, the position-only exposure mask is `{0,1,2}`, retaining the final three tokens and compressing positions 0 and 1 into an opaque gap. The gap's full F and the extra scalar **number of P labels = 1** are identical in both x and y. Their retained explicit suffix and labels are also identical.

`DELETE_LAST_PUBLIC` is legal in both. In x it deletes the +E2 token (original index 0), yielding `(+E1,+E1,+E1,+E1)` with D=(4,0,0,0,0,0) and E_(+E1,+E1)=3. In y it deletes the +E1 token (original index 1), yielding `(+E2,+E1,+E1,+E1)` with D=(3,1,0,0,0,0), E_(+E2,+E1)=1, E_(+E1,+E1)=2. Hence the future full BRC observer distinguishes the two after **one** operation.

The counterexample refutes the assertion that enriching each opaque F gap by its total P count alone suffices for arbitrary rank-based public deletion. The precise missing information is the ranked P position *together with the corresponding direction/adjacency*, or an equivalent exact response summary. It does not refute existence of stronger succinct schemes.

The executable source `BRUTE_EXPOSURE_506B.py` and its stdout `BRUTE_EXPOSURE_506B_EXECUTED.txt` are archived alongside this appendix. Here P means a pre-existing public/inserted provenance tag on the input history. The witness does not assume that either input was freshly generated from an all-original word within the limited Stage506 operation horizon.

## Next

Stage507-B should start from this one-step certificate and formulate an exact compact representation for sequences of public-ranked deletions. Test whether a bounded rightmost-P token list plus gap summaries gives a finite-horizon sufficient state, and find sharp size bounds or further witnesses where finite label counts fail.
