# R5: exact compensator-port rigidity in a sharp three-atom A→B template

Date: 2026-11-11 (Asia/Shanghai). Status: **author-side exact rational finite theorem with 25 stored Farkas duals and constructive endpoint witnesses**. Native independent review and formal Source Result remain separate.

## Context and precise object

Continue the pinned auxiliary P/Q–BRC Blackwell transport observer from R5 [PR #2084](https://github.com/awdawmip/enterprise-math/pull/2084) at `aa5138c0470783cf48a3cb29e2098cef6944b6ec`, with prior PR #2080 and explicit three-operation witness from PR #2076. Frozen scientific sources remain GLOBAL `a01383f825ef9d43b4b754254303298c64041568` and Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Current behavioral rules were read separately from canonical main; P000 and X6 are not modified.

Take target labels `i=0,...,6`, dynamic source ports `j in (1,2,3,5)`, likelihood integers `R=(2,10,15,20,25,30,38)`, and 28 nonnegative dynamic masses `x_(i,j)`. The pinned strictly positive 30-arc reference `E0` determines 15 exact observation equations `Ax=b` (rank 13). Source-3 masks are
`A_mask={1,3,4,6}`, `C_mask={2,3,4,6}`, `B_mask={2,3,4,5}`.

A six-arc atom `H_j(v)` places a signed three-target moment-null vector `v` on source 3 and `-v` on compensator source `j in {1,2,5}`, preserving the complete observer. Consider **exactly the following ordered signed source-3 atom template**:
```text
v1 = (-23 at 1, +28 at 2,  -5 at 6)
v2 = (-23 at 1, +28 at 2,  -5 at 6)
v3 = ( -8 at 2, +23 at 5, -15 at 6)
```
All three satisfy `sum v=0` and `sum R[i]*v[i]=0`. Positive rational atom magnitudes `t1,t2,t3` are free. Initial and terminal dynamic transfers may be any nonnegative solutions in the **same frozen observation fiber**, provided the successive exact source-3 masks are
`A_mask → A_mask ∪ C_mask → C_mask → B_mask`
and every intermediate transfer remains nonnegative. The *ordered compensator choice* is the triple `(j1,j2,j3) in {1,2,5}^3`.

## Theorem: precisely two feasible ordered compensator assignments

For this fixed signed-target atom template, the complete set of feasible ordered compensator triples is
```text
(j1,j2,j3) = (1,2,5) or (2,1,5).
```
In particular, this template requires **all three distinct compensator source ports**, and the third step necessarily uses source 5. This is a sharp classification of the fixed template among all `3^3=27` labeled assignments.

### Exact constructive side

The prior A→B positive rational witness uses `(j1,j2,j3)=(1,2,5)` with
`t1=1544855/475661816`, `t2=196521/67951688`, `t3=(226755/8493961)/15` for the unnormalized vectors above. Its 28-component initial mass vector is transcribed into the attached verifier from the pinned predecessor. The exact checker evaluates all 15 observations, nonnegative masses and exact masks at four stages.

The first two atoms have the **same source-3 direction** and act on **different compensator ports**. Swapping their chronological order and simultaneously swapping their coefficients yields `(2,1,5)` with coefficients `(t2,t1,t3)`. The two operations commute as vectors. Nonnegativity is preserved: source-1 and source-2 changes occur on separate ports, and on source 3 the first two operations have the same sign at each affected target. Exact checking establishes the four specified masks for both orders.

### Exact exhaustive exclusion

For each of the 25 other assignments, allow 28 freely chosen nonnegative initial masses and nonnegative weights `t1,t2,t3`, a relaxation of strict positivity. Let `z=(x,t1,t2,t3)≥0` (31 variables). Write

```text
E z = d,   U z <= 0
```

where `E` consists of 15 pinned observation equations, 3 initial zero source-3 arcs, 3 terminal zero source-3 arcs, and the exact requirement that source-3 target 1 vanishes at the second intermediate state: **22 equalities**. The `84` rows of `U` impose nonnegativity of **all 28 dynamic arcs** at each of the three post-operation stages. All coefficients in `E,U` are exact integers and `d` is an exact pinned rational vector.

For every excluded assignment, the attached file contains a sparse **exact rational Farkas dual** `(y,lambda)`, `lambda≥0`, such that

```text
E^T y + U^T lambda >= 0     (all 31 components)
d^T y < 0 .
```

Indeed if `z≥0` satisfied the constraints, then
`0≤z^T(E^T y+U^T lambda)=d^T y+lambda^T U z ≤ d^T y < 0`, a contradiction. All 25 distinct duals were verified using standard-library `fractions.Fraction` exact arithmetic. The largest (least negative) dual gap is `-102015427/44253536810`.

This proves infeasibility even under the relaxed endpoint zero equations. The two exact constructive cases finish the exhaustive 27-case theorem.

## Reproducibility and provenance

Files:
- `VERIFY_R5_COMPENSATOR_PORT_RIGIDITY.py.gz.b64` — lossless gzip/base64 of the exact 5,481-byte Python 3 **standard-library** checker; recovered SHA-256 `4c23463427a86cc0f157673e7d45d796bf1f4528c48f1c0a67ffb086aa4bec91`.
- `R5_PORT_TEMPLATE_25_FARKAS.json.gz.b64` — lossless gzip/base64 of 8,901-byte JSON with all 25 sparse rational duals; recovered SHA-256 `9f73274f4a2a851b1bf5fa445e5b3a91aaf7b12f7083fe7574a59c2d9724ddac`.
- `EXACT_OUTPUT.txt` — actual local verifier output.

Decode the Python checker with
```sh
python3 -c "import base64,gzip,pathlib; p=pathlib.Path('VERIFY_R5_COMPENSATOR_PORT_RIGIDITY.py.gz.b64'); pathlib.Path('VERIFY_R5_COMPENSATOR_PORT_RIGIDITY.py').write_bytes(gzip.decompress(base64.b64decode(p.read_bytes())))"
python3 VERIFY_R5_COMPENSATOR_PORT_RIGIDITY.py R5_PORT_TEMPLATE_25_FARKAS.json.gz.b64
```

Exploratory SciPy LP runs were used to discover the 27-case split and dual candidate supports. The finite theorem is checked from published rational duals and exact witnesses, without numerical solver tolerance in the verification phase. This run executed the local recovered-equivalent source with the original 25 stored duals; independent re-execution from published remote bytes remains an available next validation step.

**BRC scope:** source labels, target labels, signed residual orientation, exact likelihood moment, intermediate nonnegative positive-mass carrier and full observation equations are retained. This is an auxiliary observer-fiber theorem, not a new native X6/P000 dynamics result.

## Next research unit

The result is a **template-specific port diversity rigidity** statement. For **all** three-atom paths from A to B in this frozen fiber, determine whether there exists a path using one or two distinct compensator sources, possibly with other signed target triples and intermediate masks. Search first using a complete target-sign and compensator-pattern enumeration with exact optimization certificates; this distinguishes intrinsic minimum port diversity from rigidity of the present minimal-support template. A complementary reusable goal is to extract small symbolic port-capacity cuts from the sparse 25 duals and test rational parameter neighborhoods.
