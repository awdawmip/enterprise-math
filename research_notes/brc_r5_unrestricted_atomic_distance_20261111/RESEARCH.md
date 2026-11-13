# R5: three K_(2,3) operations are optimal even without a support budget

At: 2026-11-11 Asia/Shanghai. Status: author-side exact finite certificate extension; prior theorem dependency; independent mathematical review and formal native Source Result pending.

## Frozen mathematical object

Continue the immutable R5 P/Q–BRC Blackwell auxiliary model from PR #2080, commit `21b822a381158cd951810cae2ee97c2be1643212`, and its predecessor PR #2076. Frozen scientific pins: GLOBAL `a01383f825ef9d43b4b754254303298c64041568`, Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Operational rules are read from current main, separately from frozen science. Original P000/X6 premises are unchanged.

There are seven labeled targets, dynamic source ports `S=(1,2,3,5)`, 28 dynamic transfer variables `x_(i,j)>=0`, and 15 exact observation equations `Ax=b` inherited from the pinned strictly positive physical transfer. The integer likelihood parameters are `R=(2,10,15,20,25,30,38)`. Atomic move means one signed six-arc `K_(2,3)` direction, changing source 3 at exactly three target labels while compensating the opposite direction on exactly one other source port `j in {1,2,5}`; intermediate line segments preserve the complete observation equations and nonnegative transfers.

Initial source-3 positive mask `A={1,3,4,6}`; terminal mask `B={2,3,4,5}`. Endpoints may be freely selected within the one fixed observation fiber.

## Main proposition (dependent on exact PR #2080 predecessor)

`N_atomic(A,B)=3` even when no restriction at all is placed on the peak positive source-3 support. Moreover a three-move path exists with peak exactly 5. Thus allowing an intermediate six- or seven-support state does not reduce the minimum atom count for this frozen problem.

The predecessor PR #2080 gave a verified author-side theorem: no two-atom A-to-B path with peak <=5, using 86 exact Farkas duals spanning 270 finite oriented/compensator cases. This new note *uses* that theorem as a stated dependency instead of claiming an independent recheck of its 86 duals.

## Complete classification of two-move possibilities

Each signed source-3 atom on an ordered triple `i<k<l` is proportional to the integer 3-vector
`(R[l]-R[k], R[i]-R[l], R[k]-R[i])`. The multiplier is positive, so sign-reversed atoms are considered separately.

Let `h1,h2` be the two integer source-3 7-vectors and `t=v/u>0` their multiplier ratio. Source-3 nonnegativity at the first intermediate state, the two exact endpoint zero masks, and strict positivity of their four changing labels imply

`h1[i]>=0 (i=0,2,5)`, `h2[i]<=0 (i=0,1,6)`,
`h1[0]+t*h2[0]=0`,
`h1[i]+t*h2[i]>0 (i=2,5)`,
`h1[i]+t*h2[i]<0 (i=1,6)`.

These are necessary for any two-move path, regardless of compensation ports, initial capacities, or support budget. Enumerating both signs of each of the 35 triples (70 signed atoms; 4900 ordered pairs) and solving these exact one-variable rational strict inequalities leaves exactly **50 ordered pairs**. Because any nonzero three-vector with zero coordinate sum has at most two positive and at most two negative entries, the open first segment has at most `4+2=6` source-3 positive labels, and the open second segment at most six. Thus **every possible two-move A-to-B path automatically has peak <=6**.

For these 50 pairs, 28 have peak <=5 and are covered by the predecessor's exact theorem. The other 22 have peak 6 and are new. They receive the following *exact* no-go certificate coverage:

* **18 signed-atom pairs:** source-3-only necessary relaxation is infeasible. Each of its eight equality constraints fixes total and first moment, initial three zeros and terminal three zeros. Each of its 42 capacity/positivity inequalities enforces `0<=x_(i,3)^stage<=b_i` for stages 0,1,2. A recorded rational Farkas dual excludes the pair independently of other source ports.
* **Four remaining signed-atom pairs:** for each of the nine ordered compensator pairs `(j1,j2) in {1,2,5}^2`, the complete 28-variable observation fiber and all intermediate nonnegative constraints are infeasible. The supplied **36** additional rational duals exhaust these cases.

Thus 54 new exact Farkas certificates exclude all 22 new pairs. Combined with the predecessor's exact peak-5 exclusion, all 50 necessary two-atom patterns are eliminated.

For each saved dual, write its equalities as `Ez=d`, inequalities as `Uz<=f`, `z>=0`. Stored integer vectors `y` (free) and `lambda>=0` satisfy
`E^T*y+U^T*lambda>=0` componentwise and `d^T*y+f^T*lambda<0`, a contradiction for any feasible `z`. Source-3-only matrices have 9 primal variables; full matrices have 30. The checker reconstructs every matrix and checks these products using exact Python `fractions.Fraction`, not an LP solver.

A complete three-operation transfer witness is reconstructed from the predecessor: source-3 atom triples `(1,2,6)`, `(1,2,6)`, `(2,5,6)`, compensation ports `1,2,5`, and coefficients `1544855/475661816`, `196521/67951688`, `(226755/8493961)/15` relative to the unnormalized integer atom vectors. The witness checks 15 observer equations and all 28 nonnegative variables at every step, ending in B with peak 5.

## Reproduction and evidence

The `VERIFY_R5_UNRESTRICTED_ATOMIC_DISTANCE.py.gz.b64` file is the lossless gzip/base64 encoding of the complete 7,931-byte readable Python standard-library checker. It is compressed only for lossless connector-safe transport. Recover with

`python -c "import base64,gzip,pathlib; p=pathlib.Path('VERIFY_R5_UNRESTRICTED_ATOMIC_DISTANCE.py.gz.b64');pathlib.Path('VERIFY_R5_UNRESTRICTED_ATOMIC_DISTANCE.py').write_bytes(gzip.decompress(base64.b64decode(p.read_bytes())))"`

Then run

`python VERIFY_R5_UNRESTRICTED_ATOMIC_DISTANCE.py R5_54_NEW_DUAL_CERTIFICATES.json.gz.b64`.

The second base64 file decodes to a JSON set containing exactly 54 sparse integer duals; the script opens it directly. The checked local executable was run with the decoded original data and returned `PASS_R5_EXACT_NEW_54_DUAL_CERTIFICATES`. The saved `EXACT_OUTPUT.txt` contains this run's actual scientific output.

Original LP solving was used *only to discover* certificates; proof verification uses exact integer/rational arithmetic and finite coverage of 4900 pairs. Native P000, original X6 time semantics, and physical calibration are not modified. Publication to this GitHub research branch is author-side evidence persistence, not a formal Source Result or independent review.

## Next

1. Independently reproduce this branch's decoded checker and the predecessor PR #2080's 86 duals, then ask the assigned Driver for semantic/adversarial review under the original task control authority.
2. Generalize the sign-pair filter and dual certificate method to other port masks and rational likelihood neighborhoods; identify explicit threshold surfaces at which the unrestricted atomic distance drops from 3 to 2.
3. Preserve the frozen observer and port labels when testing new parameters; derive a symbolic short cut theorem as a tool-harvest candidate.
