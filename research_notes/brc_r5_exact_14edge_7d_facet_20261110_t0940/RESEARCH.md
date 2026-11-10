# R5: a certified seven-dimensional 14-edge Blackwell facet

Date: 2026-11-10 (Asia/Shanghai). Status: author-side exact-rational proof and independently executed reproduction; formal task/Result acceptance and independent review pending.

## Frozen model and provenance

Preserve the scientific pins from PR #1936: account `a01383f825ef9d43b4b754254303298c64041568`, Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Reuse the full legal P/Q–BRC seven-likelihood-ratio model, 30 Blackwell edges, 21 equations, the physical center `p0` and the exact eight-dimensional tangent `P`, as reconstructed in immutable PR #1936 commit `537ccc5575383aa112c7bdd617dad6f6e91efb59` (which in turn pins PR #1902 and PR #1930).

The seven likelihood-ratio points describe an auxiliary statistical observation. They are not the six P000 spatial axes. No P000 change, no re-pin of scientific inputs or acceptance upgrade is made.

## Exact new result

Let `r=23/17050000`, `t*=(0,0,0,-r,+r,0,0,-r)`. PR #1936 produced a lawful 14-edge coupling at `t*` by setting `E_(1,3)=0`. We strengthen that single witness to an **explicit seven-dimensional, relatively open family whose minimum coupling support is exactly 14 at every point**.

Parameterize the seven independent real variables `u=(u0,...,u6)` by
```
t0 = u0
t1 = u1
t2 = u2
t3 = -r + u3
t4 = +r + u3/80 + 13*u6/4
t5 = u4
t6 = u5
t7 = -r + u6
```
where `|u_j| <= 1/10000000` for all seven coordinates. This is a full-dimensional closed seven-cube *inside the hyperplane* `H: mu_1=E^B_(1,3)=0`. Its relative interior is a nonempty seven-dimensional open chamber. At **every** point of that cube:
1. the physical source and target satisfy all P/Q capacity constraints, `g=b`, seedless F and the two stopping-time equalities;
2. an exact Blackwell coupling exists with precisely fourteen strictly positive edges, the same support `SB\\{(1,3)}`;
3. no coupling with thirteen or fewer positive edges exists, including on the boundary of this seven-cube.

Consequently `min_support = 14` throughout this explicit seven-dimensional family.

## Proof, including the all-13-support exclusion

The fixed basis `SB` is the fifteen-edge set in PR #1936. The only `SB` edge with target row `i=1` is `(1,3)`. Its exact mass is
```
E_(1,3)(t) = mu_1(t)
           = 23/4000000 + t3/80 - t4 + (13/4)*t7.
```
The displayed parametrization makes this affine expression vanish identically. At the center `t*`, fourteen remaining basis weights are strictly positive; the zero physical slack indices are exactly `[4,15,19,23]` (zero-based), of which the `19`th is `mu_1`. Each of those four slacks has identically zero derivative in the seven tangent directions.

Exact rational one-norm margin calculations for those seven directions yield:
- smallest positive physical-slack radius: `63/75872500` (controlling slack 25);
- smallest positive fourteen-edge weight radius: `50915668197609/1262603261375726875` (controlling basis edge index 12).
Both exceed `10^-7`. Since all slack/weight maps are affine, this proves legality and existence of exactly fourteen positive edges for every real point of the seven-cube, not just tested vertices. The 21 transport equations hold as exact affine identities.

For the lower bound reuse the **ten mandatory edges** and their thirty-edge-cover dual inequalities from PR #1936 (the exact full-carrier forcing radius is `18052765669/423284426970000`). Throughout the new cube, every coordinate of `t` has absolute value less than this forcing radius; hence every feasible coupling contains these ten edges. Thus a hypothetical support of size <=13 could add at most three of the other twenty candidate edges.

Let `L` be the verified integral `5x15` left-kernel matrix of the ten forced columns and let `V=L*C_other` be the five-dimensional quotient columns from PR #1936, with `q(u)=q*=L*b(t*)+Q_7 u` after the same moment-row integer scaling. For all `C(20,3)=1140` three-subsets `S`, independently compute the exact rational left nullspace `W_S=ker(V_S^T)`, and choose a witness `w in W_S` with `w^T q* !=0`. Complete exhaustive enumeration gives:
```
rank(V_S) = 3 : 1055 supports
rank(V_S) = 2 :   84 supports
rank(V_S) = 1 :    1 support
no-three-column-span-contains-q* : 1140 / 1140
```
The minimum (over all nonzero witnessing basis functionals and all three-subsets) of
`|w^T q*| / sum_j |w^T Q_7[:,j]|`, ignoring zero slopes as infinite, is the exact rational number
`49948501046391/841518836618948125 > 1/10000000`.
Therefore at every real `|u_j|<=10^-7`, each three-subset retains a nonzero separator, and no <=13-edge coupling can exist. Smaller supports are included by extending them to a three-subset.

This proves pointwise minimum support 14 throughout the entire explicit seven-dimensional cube. In particular it strengthens the isolated boundary existence witness in PR #1936 to **minimum-support exactness** and a **positive-size relative 7D chamber**.

## Reproduction and limits

`VERIFY_FACET.py` starts from the immutable combined rational checker of PR #1936 and appends a face-specific audit of all 1140 triple supports, the exact 7D tangent, physical and coupling margins, and the dual forcing bound. The prior combined checker and this augmented remote source have not been run byte-for-byte in this session. The saved `EXACT_OUTPUT.txt` is the **actual stdout from a separately written and executed local Python/SymPy exact reproducer** of the same mathematical model; it gives all face-specific outputs and exact counts. This is computational exact algebra, not a formal proof assistant verification or independent mathematical review.

Reusable method: mandatory-edge dual inequalities -> quotient by forced columns -> all sparse-support subspaces -> rational separating normals -> a rigorous local `l_infinity` chamber radius. The same construction can classify adjacent 13/14/15-edge boundaries without conflating Blackwell observer rank with P000 native spatial dimension.

## Next discriminating mathematics

Find all 14-edge support regions meeting `mu_1=0` and determine their overlap and first 13-edge contact. Specifically test the 84 rank-two and one rank-one triple support patterns for deeper intersections outside the certified seven-cube, while retaining the original physical capacity and stopping-time constraints. Extract the exact active hyperplanes and adjacency graph; do not infer such intersections from rank alone.

Control status: research activity identity registered as `EM-DIRECT-7621D2 / TASK_RESEARCH`; formal R5 Owner/CLAIM not established by this artifact; author-side Draft PR is not a native Result or review.
