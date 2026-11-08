# S23/AV: exact first observation-capacity jump, two long plateaux, and linear-size gap enumeration

Date: 2026-11-08 (Asia/Shanghai). Author-side exact mathematical and computational certificate; independent review pending.
Frozen science: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Predecessors: PR #1777, especially `research_notes/brc_s23_av_universal_order_and_h30001_20261108_r1/PROOF.md` and the certified `N(510)=2455069` eleven-residue lower bound.
No scientific repinning; project P000 V5 and joint observer preservation continue to apply to the underlying project. This theorem concerns the explicitly typed two-point auxiliary S23/AV likelihood-sign observer.

## Theorem (first exact jump and two maximal certified plateaux)

For the two-point iid auxiliary label-(1,3,4) experiment with
`P0=(1/2,1/4,1/4)`, `P1=(5/7,1/4,1/28)`, retain the complete joint count of labels 1 and 4, with label 3 supplying the remaining count. Put

`r=log(7)/log(10/7)`,
`T_H={r*v-j: v,j>=0, v+j<=H}`,
`E_n={k-r*l: k,l>=0, k+l<=n}`.

Let `N(H)` be the least integer `n` such that each open cell of `T_H`, including the two exterior cells, is met by `E_n`. Then:

**(1)** `N(H)=2455069` for every integer `510<=H<=380805`.

**(2)** The **first** H after 510 with increased capacity is `H=380806`, and its exact value is

`N(380806)=4530352`.

**(3)** `N(H)=4530352` for every integer `380806<=H<=649492`.

The proof uses one exact finite certificate at each endpoint and monotonicity from `T_H subset T_(H+1)`. Statements (1) and (3) are exact over their displayed integer domains.

## A. Certified integer ordering through H=649492

Use `P=2074774, D=380295, A=79, B=431, W=A+B=510`. The exact identities are

`gcd(P,D)=1`, `P*A-D*B=1`, and `P+D=2455069`.

The previous 45-term atanh-series with explicit geometric tail bounds for log(2), log(8/7), log(5/4) establishes

`LO/10^26 < r < HI/10^26`,
`LO=545569623581288298975349314`, `HI=LO+1`.

Let `alpha=P-r*D`. The integer enclosure computed from these bounds proves

`0 < alpha < (P*10^26-LO*D)/10^26`
and
`649492*(P*10^26-LO*D) < 10^26`.

Consequently, for all distinct `(v,j),(v',j')` in the triangle `v+j<=H<=649492`, their real thresholds are ordered exactly by the integer key

`K(v,j)=P*v-D*j`.

Indeed, a zero key difference would have `(delta v,delta j)=m*(D,P)` by coprimality, hence its two endpoints could fit in the nonnegative H-triangle only if `H>=P+D=2455069`. For nonzero integer key difference, the perturbation is `(r*D-P)*delta v` with magnitude less than 1, so it cannot reverse the sign. This extends the earlier sufficient `H<D` key criterion to the stated certified range without changing the ordering formula.

## B. Linear-size enumeration of all consecutive gap classes

The vector `w=(79,431)` raises `K` by exactly **one**. Whenever both endpoints `(v,j)` and `(v+79,j+431)` are in the H-triangle, their thresholds are consecutive, because no integer key lies between.

Partition the entire H-triangle into maximal chains under translation by `w`. Each chain has one unique start `(v,j)` with `v<79 OR j<431`, and consists of

`(v+79*t, j+431*t)`, `0<=t<=floor((H-v-j)/510)`.

Its integer keys form one consecutive interval. Different intervals cannot overlap by key injectivity; sorting only the chain starts by their key also orders the intervals. Every consecutive threshold pair is either an internal w-edge or a single edge between successive chain intervals. Thus the program `CHAIN_STREAM.cpp` exhausts all gap classes by visiting only starts, accumulating internal w-edges algebraically, and recording one interchain edge per neighboring pair of chains.

For `H>=510`, there are exactly

`M=(H+1)*(H+2)/2` thresholds,
`c_w(H)=(H-509)*(H-508)/2` consecutive w-edges, and
`M-c_w(H)=510*H-129285` chains.

The compressed enumeration therefore uses `O(H log H)` fixed-word ordering operations and `O(H+C_H)` memory in the certified range; `C_H` is the number of different gap vectors. It avoids `O(H^2)` full-threshold enumeration and preserves every future threshold cell.

For each gap vector `(dv,dj)` the stream records: class cardinality; `V=max(v_left)`; `J=max(j_left)`; and `S=min(v_left+j_left)`. A uniform shifted prefix witness for the entire class is a pair `(K,L)` satisfying

`K>=J, L>=V, K+L<=n+S`, and
`0<K-r*L<r*dv-dj`.

The rigorous rational/integer checks are
`K*10^26>HI*L` and `(K+dj)*10^26<LO*(L+dv)`.
Then each left endpoint `(v,j)` is covered by `(k,l)=(K-j,L-v)` with `k+l<=n`.

## C. Complete endpoints for both plateaux

`CHAIN_STREAM.cpp` and `VERIFY_PLATEAUX.py` were actually executed; the verifier certifies the log interval, ordering, every compressed-class count and range, gap positivity, explicit shifted witnesses for every non-w class, and the two exterior cells.

| H | Total thresholds M | w chains | Gap classes | Largest non-w required prefix | Exterior prefix lengths |
|---:|---:|---:|---:|---:|---:|
| 380805 | 72506795221 | 194081265 | 766 | 2077762 | 69800, 2077557 |
| 380806 | 72507176028 | 194081775 | 766 | 2077761 | 69800, 2077562 |
| 649492 | 210920903271 | 331111635 | 1293 | 3543585 | 119049, 3543432 |

The dominant w-gap class has, at each displayed H, `V=J=H-510, S=0`. For its left endpoints with `v<=D`, use the original witness `(K,L)=(P,D)`, with `K+L=2455069`. For `v>D`, use `(K,L)=(4149979,760669)`, with `K+L=4910648`. At `H<=649492`, each such endpoint has `D+1<=v<=H-510<=648982<760669`; therefore this second witness has prefix length at most

`4910648-(D+1)=4530352`.

For H=380805 every w-left coordinate has `v<=D`, so the first witness suffices. At H=649492 all non-w classes and both exterior cells are covered within 4530352. Thus `N(380805)<=2455069` and `N(649492)<=4530352`.

## D. Exact minimality at the first exceptional gap

At H=380806 the two thresholds with left `(v,j)=(D+1,0)=(380296,0)` and right `(D+1+A,B)=(380375,431)` are consecutive because their integer keys differ by one.

A prefix in this gap, translated by `K=k+j=k` and `L=l+v=l+380296`, must obey

`L>=380296`, `0<K-rL<rA-B`.

Write the integer `C=D*K-P*L` and `alpha=P-rD>0`. The gap condition becomes

`0 < C+alpha*L < 1-alpha*A`.

The verified rational inequalities include

`alpha*(760669+79)<2`,
`alpha*(380295+79)<1`,
`alpha*(2*380295+79)>1`.

For `380296<=L<=760669`, the gap inequality forces `C=-1` or `C=0`.

If `C=0`, coprimality forces `L` to be a multiple of D; the sole possibility in the interval is `L=2D=760590`, which violates the upper gap inequality because `alpha*(2D+A)>1`.

If `C=-1`, the Bézout identity `P*A-D*B=1` forces `L=A (mod D)`. The possible values are `D+A=380374` and `2D+A=760669`. The first violates `alpha L>1). The second gives `K=4149979` and satisfies both gap inequalities by strict rational checks.

Hence there is no prefix point in this open cell with `L<760669`. At the first possible value `L=760669`, the unique `K=4149979` yields the prefix

`(k,l)=(4149979,380373)`, length `4530352`.

Any larger `L` has strictly larger `K+L` because `K>rL` and the gap width `rA-B<1`. Thus this cell's exact first-entry prefix length is **4530352**, yielding `N(380806)>=4530352`. Section C proves the matching upper bound at this H and also at H=649492.

Finally, the previously certified `N(510)=2455069` lower bound and monotonicity give the first plateau, the exact first jump, and the second plateau through 649492.

## Reproducibility and frontier

Compile `CHAIN_STREAM.cpp` with `g++ -O3 -std=c++17` and generate three complete finite class tables at `H=380805,380806,649492`. Then run `python VERIFY_PLATEAUX.py CLASS_380805.csv CLASS_380806.csv CLASS_649492.csv`. This recreates all three endpoint certificates, including every non-w class witness, with exact integers and Fraction rational enclosures. The script's bounded witness search only establishes existence; successful witnesses are checked by exact inequalities.

As regressions, the compressed stream produced byte-for-byte identical class tables to the earlier full stream at H=7000, H=30000, and H=50000. The H=50000 full stream individually processed 1,250,075,001 thresholds; the compressed stream processed 25,370,715 starts.

The S23/AV auxiliary likelihood count is a source-conditional retained joint observer, not a primitive X6 spatial model. This proof introduces no projection of the full six-source/ten-label mother model. The mother-map and the four-observation minimax question remain separate open tasks.

The next mathematical frontier is H=649493. The fixed integer-order key P,D no longer meets the simple certified bound `H*(P-rD)<1`; a new convergent and/or a refined cone-specific integer-order argument can continue the gap-chain method. All research publication here is author-side pending independent mathematical review, without a native Source CLAIM.
