# Stage257 — exact adjacent five-vertex Bellman contact face
2026-10-29. Status: **AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED**. External N=12 ternary IID auxiliary model only. Parent Stage256 commit `dc5a09fd1395048c8683be786f042b8ba5b5c552` in Draft PR #1571. No native P000 X6 transfer, formal CLAIM, Source Result or independent Driver acceptance.

## Statement and exact data

For source laws `P=(1/8,1/24,5/6)`, `Q=(1/12,1/12,5/6)`, allow all randomized stop/decision policies depending on full ordered histories of length at most 12. Write `eP=Pr_P(decide Q)`, `eQ=Pr_Q(decide P)`, `tP=E_P[depth]`, `tQ=E_Q[depth]`, and `V12(a,b)=inf max(tP,tQ)` subject to `eP<=a,eQ<=b` (infinity if infeasible), for all real caps `a,b in [0,1]`.

The new exact dual is `lambdaP=3869835264/48435355`, `lambdaQ=2516141892/48435355`, `thetaP=0`, `thetaQ=1`, root `H=90579154987/1743672780`.

Define five **full** observer vectors, in cyclic error-polygon order:
```text
U1 (791411207/23219011584, 8046728185/8707129344,
    1087023623/967458816, 882110471/725594112)
U2 (1011440903/15479341056, 4981428985/5804752896,
    1298095367/644972544, 1038314759/483729408)
U3 (29383188527/139314069504, 9874231855/17414258688,
    31963078703/5804752896, 8184999377/1451188224)
U4 (30348774917/139314069504, 9753923645/17414258688,
    31316233733/5804752896, 7902199747/1451188224)
U5 (1743753479/46438023168, 16033302265/17414258688,
    2066239751/1934917632, 1622821127/1451188224)
```

**Theorem.** The exact pentagon `R257=conv{(Ui.eP,Ui.eQ):1<=i<=5}` has five strictly convex vertices and rational area `361875536423559625/303256405652583481344`. For **every real** `(a,b) in [0,1]^2`, including irrational parameters and arbitrary full-history randomization,
```
V12(a,b) = H - lambdaP*a - lambdaQ*b    IFF    (a,b) in R257.
```
The full shared edge with the preceding Stage256 region is `U5--U4` on `2a+b=69364469497/69657034752`; R257 lies on the `<=` side and Stage256 on the `>=` side, with disjoint interiors. The one-sided time dual still suffices on R257.

A strict-exterior rational cap pair, at distance `3/10000` across that old line in the exact `2a+b` observer, is
```
a*=11110053918781/87071293440000
b*=2685806568569/3627970560000
V12(a*,b*)=48250126915010865853/14643503500262400000.
```
An explicit optimal strategy root-randomizes between the deterministic policies `D_(3,Q),D_(12,Q),D_(12,C)` with respective positive rational weights
```
47417565732639347237/61486950094953906250
11416570966257880613/61486950094953906250
6530347008/151360484375.
```
They sum exactly to one, give `eP=a*,eQ=b*`, and produce `tP=569512359887299976431/175722042003148800000`, `tQ=48250126915010865853/14643503500262400000>tP`.

## Proof (finite exact dual plus complete equality fiber)

For any ordered history h with counts `s=(i,j,k)`, its exact likelihood ratio is `L(s)=Q(h)/P(h)=(2/3)^i 2^j`. Bellman minimization of `tQ+lambdaP*eP+lambdaQ*eQ`, normalized by P history mass, obeys
```
H_s = min{lambdaQ*L(s) [decide P], lambdaP [decide Q],
          L(s) + sum_z P(z) H_(s+unit_z) [continue]}.
```
Omit continue at depth 12. Direct rational backward induction checks **455 states**, **1274 action costs**, **807 strictly positive nonminimal gaps**. There are exactly 12 two-action ties: `(0,0,k)`, `1<=k<=11`, with P/continue; and `(0,1,1)` with Q/continue. At the root only continue minimizes. The value at root is exactly H above. Thus universally `max(tP,tQ)>=tQ>=H-lambdaP*a-lambdaQ*b`.

The count-state sufficient statistic is **proved for the four specified observers** rather than assumed. For any full-history randomized policy, sum its positive P-weighted visit/action masses at state s. All histories in the fiber have exactly the same Q/P likelihood ratio L(s), including any stopping randomization, so Q-action mass is L(s) times the P-action mass. The flow relation at successor count s+unit_z is `P(z)` times aggregated P continuation mass. Dividing positive action mass by visit mass constructs a count-Markov randomized strategy with identical `(eP,eQ,tP,tQ)`. It does not preserve arbitrary unmentioned observables. Conversely, independent pre-sampling of each count-state randomized action table expresses such a strategy as a convex mixture of deterministic count-state policies.

All Bellman-equality deterministic policies, up to unreachable actions, are precisely `D_(k,M)` with `k=1,...,12` and `M in {Q,C}`: after only neutral symbol 2, stop and declare P at neutral depth k (continue earlier); at count `(0,1,1)` take Q or continue according to M; everywhere else take the unique Bellman-minimizing action.

Write `B_k=obs(D_(k,Q))`, `C_k=obs(D_(k,C))`. The B_k are exactly the previously established Stage256 `C_k` and lie on the four-observer affine segment between `B_1=U5` and `B_12=U4`. For k>=2, the difference `C_k-B_k` is the same four-component exact vector
```
Delta=(-160931065/23219011584, 60154105/8707129344,
        107807495/967458816, 141399815/725594112).
```
For k=1 the difference is exactly Delta/2: the `(0,1,1)` tie can be reached via both orderings `1,2` and `2,1`, but stopping after a first neutral 2 removes the latter. These two positive source-labelled paths have equal P and Q mass, hence the exact half factor. For k>=2, all `C_k` lie on the four-observer segment from `C_2=U2` to `C_12=U3`, while `C_1=U1`. The exact error convex hull of all 24 equality policies therefore is the stated five-vertex polygon; exact cyclic cross products are strictly positive, and shoelace gives its area.

Each B_k has `tQ-tP=292565255/5804752896>0`; for C_1 add `(Delta_tQ-Delta_tP)/2>0`, and for k>=2 add `Delta_tQ-Delta_tP>0`. Every convex mixture of equality policies therefore has `tQ>tP` and saturates the Bellman lower bound. For any caps in the pentagon, choose a convex mixture matching the exact error pair to prove sufficiency. For necessity, compactness of the finite-horizon randomized history-policy simplices gives an optimizer whenever feasible. Equality in the lower bound forces both errors to saturate their caps (strictly positive lambda), and every positively reached action to be Bellman minimizing. The proven observer-specific count compression then forces the error pair into the same pentagon. This covers all real caps, not only rational sample points.

## Execution and research scope

A locally executed, standalone Python 3 `fractions.Fraction` checker exhaustively verified the Bellman table and all 24 policies through count-state DP and a **separate unmerged ordered-history DFS**. The DFS propagated independent positive rational P/Q path masses, checked both terminal masses equal exactly 1, and totaled 1974 visited ordered-history nodes plus 1324 terminal branches across the 24 policies. The script checked the four observers, all action gaps and ties, affine collinearity, half-Delta branch mechanism, exact pentagon area, strict-exterior point, positive three-way policy weights and exact primal/dual equality. Actual output included `STAGE257_EXACT_ALL_REAL_FACE_PASS` and `STAGE257_PROOF_CERTIFICATE_PASS`. This is author exact arithmetic, **not** native execution or independent peer review. BRC reuse: typed P/Q positive branch masses, provenance and observer-preserving quotient; no signed-amplitude cancellation or native heartbeat physical attribution.

Frozen reads: GLOBAL_KNOWLEDGE_V1 `main@e1a6307dd59f5e1290a1fa151115a72dee4dc886`; Enterprise Math `main@12274cc63b1f127e5db9fadebc83f21c77224075`; P000 original and startup projection blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`, ACTIVE worldview unchanged. Native `em_control_tasks` failed `CONTROL_QUOTA` and `em_status` reported `research_authority_granted=false`. Local provenance label: `EM-R2-257-20261029-0210-LOCAL`, **not** a Source-issued session or CLAIM. No two-dimensional native plane: the error-coordinate polygon is only an external statistical parameter space.

Next: Stage258 tests the outward side `U2--U3` on `2a+b=22960038649/23219011584`, starting with candidate caps `a=12018216825031/87071293440000`, `b=7754698736957/10883911680000`, strictly outside by `3/10000`. Prove feasibility or rational obstruction before asserting a new value; then find the adjacent exact primal/dual support and time-weight regime.
