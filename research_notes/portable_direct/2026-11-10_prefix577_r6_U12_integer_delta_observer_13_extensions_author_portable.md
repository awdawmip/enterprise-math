# BRC-X6: an exact integral quotient observer for U12 and 13-policy extensions

Date: 2026-11-10. Status: **AUTHOR_PROVED / EXACT_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED**. This is author-side portable research, not Source Task CLAIM, checkpoint, Result, native H0/B0 experiment, independent review, or theorem admission.

## Frozen original-native input, inherited frontier

Science SHA256 `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Preserve the 96 original ports, six distinct labeled actions per port, source ports `(6,7,28,29)`, signs `(+,-,-,+)`, all nine frozen roots, and complete signed seven-variable next-port/reward joint observers. Direct tests of the `6^4=1296` four-tuples return exactly 38 legal deterministic policies `c_j`, (j=0,\ldots,37), indexed lexicographically. Their uncollapsed four-source-by-six-action incidence matrix is `C in Z^(24x38)`, rank 13; row index `6s+a` retains source `s` and action `a`.

Prior work (not recredited): original-native twelve-policy full-positive cone
`U=(0,1,3,6,7,8,12,17,28,29,30,31)`, published at immutable author commit `b9504c1d23f792e393f6f4503554672d1c274045`. This turn derives the additional signed quotient coordinate for all 38 legal policies, classifies all single-column rank-13 extensions and supplies exact D511 counts and a global sparse-reduction counterexample.

## Theorem A: explicit primitive integer quotient coordinate

Take `R=(0,1,2,3,4,5,6,7,10,12,13,16)` and `B=C[R,U]`. Exact integer elimination gives
`det(B)=-1` and `C[14,U] B^{-1}=(1,1,0,0,0,1,-1,-1,0,0,0,0)`.

For any original-native integer numerator vector `b`, define the exact signed residual observer
$$
oxed{\delta(b)=b_{14}-b_0-b_1-b_5+b_6+b_7.}
$$
Here `b14` is source 2/action 2, not a relabeled marginal or collapsed port.

For every one of the 38 legal original policies:
$$
\delta(c_j)\in\{-1,0,1},\quad \#(delta=-1,0,+1)=(7,24,7).
$$
The `+1` policy IDs are `(2,5,14,19,22,23,26)`; the `-1` IDs are `(10,11,32,33,34,36,37)`; all other 24 IDs (including U) have zero residual.

The stronger integer identity, on all 24 native coordinates, is
$$
oxed{c_j-C_U B^{-1}c_j[R]=\delta(c_j)(e_{14}-e_{17}+e_{20}-e_{23})}.
$$
Proof: compute `B^{-1}` by exact rational/integer arithmetic; since `det B=-1`, all coefficients are integers. Directly enumerate all 38 original nine-root-legal columns and verify the displayed identity on each of 24 rows. The residues are exactly 0, `+z` or `-z`, with `z=e14-e17+e20-e23`. Extend linearly. Thus for any legal nonnegative weights `x_j`,
$$
\delta(Cx)=\sum_{j:\delta(c_j)=+1}x_j-\sum_{j:\delta(c_j)=-1}x_j.
$$
The signed difference is a true retained original-native observer; a total positive mass projection would lose it. In particular `\delta(b)!=0` certifies `b` lies outside the *fixed* U-span; it does **not** prove any lower bound of 13 legal policies across all 38.

## Theorem B: all 14 one-column integral 13-dimensional extensions

Of the 26 lawful policies not already in U, 12 have zero quotient residual and 14 have `±1`. For any `j` among the 14 nonzero classes, `W_j=U+(j,)` has rank 13 and an explicit unimodular native minor:
$$
oxed{det C[R+(14,),W_j]=-\delta(c_j)\in\{-1,+1}}.
$$
Consequently integer coefficients in each such `W_j` are uniquely recovered from the 24 integer numerators via an integer left inverse. For `b=C_{W_j}v`, `gcd(b_0,\ldots,b_{23})=gcd(v_0,\ldots,v_{12})`; the probability vector `b/D` has true reduced denominator `D=sum(v)` iff `gcd(D,v_0,\ldots,v_{12})=1`.

This is a rank/integer-lattice result, not an assertion that any such 13-policy expression is globally 13-minimal.

## Theorem C: exact full-positive counts in a best one-column extension

For each `W_j`, count full-positive original-native vectors `b=C_{W_j}v`, `v` nonnegative integral and `sum(v)=D`, with all 24 coordinates of `b` positive. Because of the integer left inverse, every distinct integer `v` gives a distinct 24-coordinate `b`.

Exhaustively enumerate the `2^13=8192` positive-weight support subsets in each of 14 rank-13 single-column extensions. The largest D511 count within this **restricted 14-extension comparison** is achieved by `j=14` and `j=19`. For each, the complete covering support histogram by size `k=7,...,13` is
$$
h_k=(3,17,38,43,26,8,1).
$$
Hence the exact formula, valid for all positive integers D, is
$$
N_{14}(D)=\sum_{k=7}^{13}h_kinom{D-1}{k-1}.
$$
At `D=511=7*73`:
$$
oxed{N_{14}(511)=684603279358325920172736}.
$$
Relative to fixed U, there are exactly `669078474004137781858560` new D511 *distinct original 24-coordinate* numerator vectors, all lying outside the U linear span (because their coefficient of `j=14` is positive).

By the unimodular minor and Möbius inversion, vectors with genuinely irreducible denominator 511 number
$$
P_{14}(511)=N_{14}(511)-N_{14}(73)-N_{14}(7)+N_{14}(1)
=oxed{684603279300702648718843}.
$$
The exact irreducible-D511 increment outside U is `669078473954025128610733`.

The 14 eligible extensions divide into 7 equal-count groups (listed in decreasing D511 count):
```
j=(14,19)      N=684603279358325920172736
j=(36)         N=684596960382144399472896
j=(5,11)       N=684272165006414235501120
j=(10,23,37)   N=683947480489915326278464
j=(2,26,34)    N=669072155027956261158720
j=(33)         N=669065946911005995208000
j=(22,32)      N=668753678628407617886784
```
The counts concern each individual extension, **not** a disjoint union across all 14 and **not** a count of 13-minimal targets in the complete 38-policy model.

## Discriminating exact counterexample: 13 positive coefficients reduce to eight globally

For `W14=U+(14,)`, take all 13 integer coefficients equal to 1, `D=13`. Original-native numerator matrix:
```
[5,1,2,1,2,2]
[5,1,2,1,2,2]
[4,3,3,1,1,1]
[4,3,3,1,1,1]
```
This unique 13-column-basis representation has all coefficients positive. However, the **same exact 24 coordinates** arise using only eight lawful original-native policies, `IDs=(0,2,9,13,21,26,34,36)`, integer weights `(4,1,1,2,1,2,1,1)`; total D remains 13. The signed joint observer was checked at every one of the nine frozen roots. Thus being irreducible *within W14* does not imply full-38 global 13-minimality. This witness is an exact integer equality, not a solver feasibility claim.

## Independent validation and next frontier

The full conversation six-file reproducibility package contains the frozen author kernel, `verify_extension_primary.py`, a separate standard-library/Bareiss `verify_extension_independent.py`, the machine-readable full 14-extension certificate, expanded Chinese theorem and README. Primary exact tests rebuild 38 legal policies at nine roots, the rank-12 primitive chart, all 38 residuals and all 14 unimodular extensions, support histograms, primitive counts and eight-policy equality. Independent tests reproduce class counts, unimodular determinants, covering subsets by direct combinations (not the first script's bit masks), explicit distinct 24-coordinate vector counts for D7/D8/D9 `3/38/258`, and the eight-policy witness. Both returned PASS. No substitute native computational experiment was performed.

Next unresolved portable unit: use this exact `delta` observer together with the U12 coordinate chart to select full-positive D<=511 candidates; check each against **all 38** legal policies, either constructing a rational <=12 decomposition or an exhaustive integer/separating certificate ruling those out. The D13 witness is a completed compression example, not a 13-minimal candidate.

Canonical D25/LIFT/JT2 remains OPEN; user-prioritized original UR V2 four-file bundle remains unverified (94687 bytes, SHA256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`). Existing Source session/CLAIM authorization is not established here. Publishing this author evidence does not register research activity, create Source checkpoint/Result, or prove independent acceptance.
