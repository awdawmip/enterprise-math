# R284GP — Closed crossing invariant and all-parameter sharp capacity (SMT-backed)
2026-11-24. Informed portable continuation of the frozen auxiliary four-phase fixed binary tag model; author analytic derivation plus exact integer SMT calculation, NOT_REVIEWED. No native X6 physical or BRC arithmetic attribution. P000 and ACTIVE worldview unchanged. Original registration r1-20261124-0256-r284gd-session-v1 read back SUCCEEDED: EM-DIRECT-0C386E / RA-B82240E8488EF5A1DA5186C4. Current owner inventory r1-20261124-1300-owner SUCCEEDED, error=null, snapshot INV-3d1dbee070fcc0dc311df41122fe7196 as of 2026-11-24T05:03:46.298606Z, Source 8c65067dfaa0cde6a032472d9cb7a9162ac81478, no LEASED tasks returned. No shared CLAIM or formal task mutation.

## Result
For all integers q>=0, u>=1 in the frozen model, the exact minimum width is
```
F(q,u) = min(4q+8u+2, max(5q+5u+2,6q+4u+2)).
```
The entire remaining region q>u is excluded below F by a single unbounded QF_LIA calculation, using only the first two consecutive edges' crossing conditions plus the four GE adjacent and two GM opposite conditions. This is an SMT-backed mathematical conclusion with an analytic reduction; it is not a finite extrapolation or a separately independently checked solver proof. The low region q<=u is already established by GM, the global matching upper bound by GK (including the repeated Gray construction). Independent certificate replay and human simplification remain valuable next work.

Frozen inputs (all exact commits, no rebase):
- GO @63259e6e1442122866e477bea6eda3d6c00a45c9:research_notes/portable_direct/R284GO_EXACT_SINGLETON_ORDER_AND_PREFIX_CROSSING_20261124.md.
- GN @afae60df3e811e985f53284b629e5c468649ee34:research_notes/portable_direct/R284GN_FULL_SEVEN_MODE_PREFIX_DISTANCE_AND_U4_SHARP_20261124.md.
- GM @a06ff527a1494a6a61b6964f9a753bcb35ab7433:research_notes/portable_direct/R284GM_GLOBAL_LOW_OMISSION_SHARP_CAPACITY_AND_RIGIDITY_20261124.md.
- GE @a112519ea319ef0e0bdf10ee01d817e10fd3dcd5:research_notes/portable_direct/R284GE_EXACT_ADJACENT_ROLLBACK_CAPACITY_20261124.md.
- GK @9c56aa402a9f36352c11ea721fe5b1bba580fdf1:research_notes/portable_direct/R284GK_LOW_OMISSION_THREE_PATTERN_CONSTRUCTION_20261124.md.
- GJ @5df644efe9d0fc36c0b317688c284543c8e0c585:research_notes/portable_direct/R284GJ_SHARP_BOUNDARY_Q4U_MINUS3_20261124.md (for finite crosscheck coverage).

## GP1. Four-affine crossing invariant
Fix nonnegative integer histogram x1,...,x7, q>=0 and integer r>=1. Normalization and the attempted-prefix path are GO/GN. Let P=x1,A=x3,B=x5,C=x6,V=x7, and [z]+=max(0,z). Put
```
t=[V-q]+-q, d=[V+C-q]+-2q, l=[P-q]+
K0=[t]+, K1=t+A-q
C0=max([x2-q]+ + [C-q]+ - q,d), C1=d+A+x2-q
J0=max(0,l-q,t+[l-q+C]+), J1=max(P-3q,-2q)
E0=t+x4+B+max(C-2q,-q)
E1=t+x4+B+max(P-3q+C,-2q).
```
Expanding GO's hinges gives exactly
```
k(a)=max(K0,K1-a), c(a)=max(C0,C1-a),
J(a)=max(J0,J1+a), C_GO(a)=max(E0,E1+a).
```
Indeed [P+a-q]+ and [a-q]+ give the constant and slope-one pieces; the remaining GO terms are constant. Hence the only crossing indices that need testing are those where k(a+1),c(a+1),J(a) are all below r. If max(K0,C0,J0)>=r this set is empty. Otherwise it is the integer interval
```
lo=max(0,K1-r,C1-r), hi=min(A-1,r-1-J1).
```
If lo>hi it is empty. Assume the original endpoints satisfy GN2/GN3. By GO monotonicity H(a)>=0 and L(a+1)<=B throughout. Where k or c is >=r the lower bound L is zero; where J>=r the upper bound H is B. These crossings are automatically safe. On the active interval the crossing condition L(a+1)<=H(a) is exactly
```
q-P+2r <= max(C0,C1-1-a)+max(E0,E1+a).
```
The sum on the right is max(U0,U1,W+a,Z-a), where U0=C0+E0, U1=C1-1+E1, W=C0+E1, Z=C1-1+E0. Note U0+U1=W+Z. The minimum over integer a in [lo,hi] is exactly
```
M=max(U0,U1,W+lo,Z-hi).
```
Proof: each term gives a lower bound. Set m to that maximum. The constraints W+a<=m and Z-a<=m define the integer interval [Z-m,m-W], which is nonempty since 2m>=U0+U1=W+Z. It intersects [lo,hi] since m>=W+lo and m>=Z-hi. An integer in the intersection attains the bound. This also gives a worst-crossing witness by selecting a=max(lo,Z-m).

Therefore, given endpoints, the exact edge criterion is the single finite disjunction
```
max(K0,C0,J0)>=r OR lo>hi OR
max(C0+E0,C1-1+E1,C0+E1+lo,C1-1+E0-hi)>=q-P+2r.
```
No enumeration of a, no generic branch traversal or b-search is needed. This is a fixed arithmetic comparison count independent of width, with integer bit complexity still dependent on operand size. The proof uses the entire seven-mode source-group structure via GO/GN; it does not equate different histories using a marginal residual total. For the global necessary test, endpoint tests may be dropped (all safe protocols already meet endpoints); doing so only enlarges the feasible set.

## GP2. Unbounded integer lower bound
For every feasible protocol, GE imposes overflow >=q+4u+1 on the following three source group totals on each edge:
(1,3,5+7); (2,6,5+1); (4,3,5+2); (7,6,5+4).
Here indices denote multiplicities, e.g. 5+7=x5+x7. GM opposite cuts are exactly the two matrices [x1,A; C,x4] and [x2,A; C,x7]; at least one cell >=2q+r, row/column >=3q+r, or full >=4q+r is required for each. r=2u+1. GO's edge 1 is the permutation (x2,x4,x6,x7,x5,x3,x1) in the GP1 argument order (new bit i is old bit i+1 XOR old bit 1; the last bit is old bit 1). Apply GP1 to the original edge and this rotated edge. Every feasible protocol satisfies this relaxed conjunction. For q>u its sub-F width is expressed exactly by
(q<=2u AND n<6q+4u+2) OR (q>=2u AND n<4q+8u+2).
The SMT-LIB file declares q,u and all seven x as unbounded Int, u>=1, q>u, x>=0. Only addition, integer comparisons and constant multipliers are present. There is no bound on u, q or n; no approximation. Its result UNSAT eliminates the relaxed conjunction, hence every actual safe protocol below F. Constant columns, if present, cannot help separation and can be removed as in GK/GE. The same lower bound holds for full width. Combine with GM low-region theorem and GK upper bounds to obtain F on all q>=0,u>=1.

Exact executed calculation: local libz3 4.13.3.0, Z3_eval_smtlib2_string on the exact SMT-LIB bytes, returned 'unsat'. A second run with '(set-option :produce-proofs true)' prepended and '(get-proof)' appended also returned unsat and a 991788-byte output including the generated proof term in approximately 0.37 seconds in that execution. Output SHA256 25eaf7f7d9d7ac026d01357425b443a3c1d304b53ac7674dbcfca15a9983ef1c (local proof output, not independently replayed; solver version can affect proof syntax/bytes). Reproduce using the saved SMT2 query with z3 -smt2 FILE; optionally prepend/append proof commands as above. The timeout option is 18000 ms; actual result was UNSAT, not unknown. No solver trust is needed for GP1's derivation, but GP2's exclusion uses the integer solver result. Do not promote this to independent Review or formal project Result without actual applicable verification.

SMT query exact immutable commit 46993baa50424690e4bba39b3a625f9ebdd09455:research_notes/portable_direct/R284GP_all_parameter_lower_bound.smt2, blob fd24f788fe782948ecef2fe914982579abe625b8, SHA256 6ed06e40130b3c8e84c2750abb2412fbc0c5d85ac666266eacf5316040f6baed; remote blob matches executed bytes.

## GP3. Independent finite algorithm crosschecks
C++ code @9045f1783e37e9bbcc8126d356c3b1a02bd80b1e:research_notes/portable_direct/R284GP_closed_crossing_checker.cpp; blob 39bbde4da3a14bb132e4a585ee1d6bd064c61d82; SHA256 08b4314afa1bf800e2b70243926c01525d24ef60520a6390d046c99fd2e7a061; remote blob equals executed local source. Compile g++ -O3 -std=c++17 FILE -o check. No args: tests x_i in 0..4 (5^7), q=0..4, r=1..7, 2734375 comparisons against original GO scan; 640260 true, 0 mismatches. This checks GP1 vs GO, not the upstream physical model independently.

With args u [q_start q_end], enumerate exact width F-1, by A=x3, C=x6, B=x5, S=n-A-C-B, t=x1+x4, v=x2+x7=S-t, and x1 and x2 as free splits. Every nonnegative histogram of that width has exactly one such representation. Necessary pruning for a pair with singleton total s: max(A,C,s)>=2q+r OR max(A,C)+s>=3q+r OR A+C+s>=4q+r. Every qualifying opposite cut implies at least one of those inequalities. Then check exact opposite cuts, GE, and all four rotated edge decisions; all arithmetic within signed 64-bit range for tested values. A safe smaller-width protocol could be padded by an extra nonconstant column ignored by the decoder, with its nominal changing attempts added to the original schedule: projection preserves original attempts and omission/noise budgets and duplicates an existing projected prefix; hence exclusion at F-1 excludes all smaller widths.

Actual outputs (q | n | passed both opposite and GE | first failed edge 0,1 | safe):
u=5
6|57|19|10,9|0
7|63|252|134,118|0
8|69|1484|783,701|0
9|75|5776|3039,2737|0
10|81|17429|9156,8273|0
11|85|16512|8475,8037|0
12|89|16156|8147,8009|0
13|93|16044|8036,8008|0
14|97|16019|8011,8008|0
15|101|16016|8008,8008|0
16|105|16016|8008,8008|0
u=6
7|67|19|10,9|0
8|73|252|134,118|0
9|79|1484|783,701|0
10|85|5776|3039,2737|0
11|91|17429|9156,8273|0
12|97|44210|23199,21011|0
13|101|42181|21700,20481|0
14|105|41264|20874,20390|0
15|109|40908|20524,20384|0
16|113|40796|20412,20384|0
17|117|40771|20387,20384|0
18|121|40768|20384,20384|0
19|125|40768|20384,20384|0
20|129|40768|20384,20384|0
u=7 (partial row, q=8..14 only)
8|77|19|10,9|0
9|83|252|134,118|0
10|89|1484|783,701|0
11|95|5776|3039,2737|0
12|101|17429|9156,8273|0
13|107|44210|23199,21011|0
14|113|98866|51838,47028|0
Counts: 9631990195 innermost checked partitions (after pruning), 8798877387 passed opposite cuts, 687153 passed both GE and opposite, 351336 fail edge 0, 335817 fail edge 1; no survivors, no checks on edges 2/3 needed after failure. u=5,6 rows complete by GM/GJ and GK. u=7 scan stopped after q=14; do not claim complete finite coverage at u=7. The unbounded SMT calculation covers the entire q>u domain separately; do not conflate the finite crosschecks with its proof.

## Next
The previous all-parameter capacity conjecture is settled at the level of exact SMT-backed proof under the frozen source lemmas. Derive short human-readable lower-bound cases or an independently checkable certificate for GP2, and classify all minimizing histograms at q>u (GM already classifies q<=u except q=0). The empirical first-two-edge failure in every scanned sub-F candidate is upgraded to a solver-backed universal exclusion; no need to repeat those finite capacity scans. No independent mathematical review yet.
