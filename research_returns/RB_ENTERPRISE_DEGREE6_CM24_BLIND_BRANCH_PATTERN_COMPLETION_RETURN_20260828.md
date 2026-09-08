# Ramanujan–Borwein × Enterprise degree-six CM(-24): branch-pattern stage return

Status: `STAGE_RETURN_CANDIDATE / BLIND_BRANCH_PATTERN_INCOMPLETE`.
Source comparison: `SOURCE_COMPARISON_UNRESOLVED`.
Recorded at: `2026-09-08T16:29:36.532491Z`.

This return freezes a strictly smaller exact algebraic frontier. It does not reconstruct a map, exclude either whole remaining pattern, satisfy the hard target, or close the parent objective. The exact taskbook expressly permits the primary verdict `BLIND_BRANCH_PATTERN_INCOMPLETE`; its stronger successor-gate example of excluding one whole pattern has not been achieved. A canonical Result and Driver decision are not created by this document.

本阶段真实排除了 4+2 型中 180 个几何参数组件，仍有 540 个 4+2 组件和 1440 个 2+2+2 组件未解。1980 是带连续参数的有限索引族数量，不是已构造映射数或有限解集。原域下降、完整 RR/ODE 及原始候选比较均有明确未完成项。

## 1. Exact execution and blind-freeze provenance

| Field | Source-backed value |
| --- | --- |
| Task | RS-RB-ENTERPRISE-DEGREE6-CM24-BLIND-BRANCH-PATTERN-COMPLETION |
| Publication | TP2-032D4712B5CB0E5D2376 |
| Researcher | EM-HODGEH0O-82EF42 |
| Winning claim | chatgpt-rb-blind-20260908-1943ccc582e1463bbcef0c6ab3c7db1b |
| Execution | ER-B78C668C38B9A9C54D9D |
| Claim source | Issue #240 comment 5586114827, created 2026-09-08T13:44:14Z |
| Execution source | 07af62e91f5178d9538d90c310f66fc9fa73f0dc |
| Parent objective | RB_ENTERPRISE_THEOREM_PACKAGE_V2_INDEPENDENT_VALIDATION — OPEN |
| Exact taskbook | research_tasks/RB_ENTERPRISE_DEGREE6_CM24_BLIND_BRANCH_PATTERN_COMPLETION_20260828.md |
| Taskbook Git blob | 3127e4eb3b2e987075f453d773a3bb21a5c8f09c |
| Taskbook SHA256 | 0249807db62a8e2753a0eb38cce1a0afb1d5bc17ffce02117a8ebcba0bbe15aa |

The actual prior runtime authorization is preserved in `research_artifacts/RB_BLIND_BRANCH_PATTERN_COMPLETION_20260908/execution_authorization.json`, SHA256 `134414b20f551e2556d1ff49af21f7b227b29a30f7fe4e396d2936dd9297adfa`. The original ER bytes, including CRLF, remain unchanged. This return does not issue a new claim or extend a lease.

Before the new raw freeze, the only external mathematical inputs read were these two exact task-whitelisted sources at `c73816d3552b4247861e12e476101e94a4a2ce5a`:

| Source | SHA256 |
| --- | --- |
| research_artifacts/RB_ENTERPRISE_DEGREE6_CM24_BLIND_REPLICATION/raw_freeze_reduction.json | 0740e43ae09bc28fcb2facada23ea5e9fdfa535829e547eed27d2128dd6e8207 |
| scripts/check_rb_enterprise_degree6_cm24_blind_replication.py | c3ad29911348934d28e136f95dbced12fa2b9a4ccab5b7f3c40e31d46911bfe5 |

Both were read, not executed. No originating explicit X/Y, coefficients, basepoint, twist, period answer, load-bearing replay, containing journal, or targeted external search was inspected before freezing. This is the executing context's actual exposure disclosure, not a claim about inaccessible history. Prior unrelated control/X6/H0O work and shared owner context were disclosed. The task has prose `BLIND_FORWARD` and no machine `source_firewall.mode=BLIND_INDEPENDENT`; no canonical PRE_MATH stamp was manufactured or backdated.

The new raw artifact is `research_artifacts/RB_BLIND_BRANCH_PATTERN_COMPLETION_20260908/raw_freeze_branch_patterns.json`:

- phase: `BLIND_BRANCH_PATTERN_FREEZE`;
- actual creation: `2026-09-08T16:04:28.017752Z`;
- file SHA256: `a9bac29196d70c40e0b08eb9efc23a3a5c07add447479bca979a11b885bec9b2`;
- canonical payload SHA256: `45258b1482b73515d6057aa5bace2cf0828e1d61834f0e386c466fadaa036cc0`;
- immutable source: `7791ddf5c969bb580cff04b1cb742ec3f9d8a9b9`, tree `9f1724cc12dd9da7671556627cbad278c7be0597`, parent `ad05f1ce0e1f06b64268681a1a57d08d2032e6ca`.

Root confirmed both raw-freeze files by full-content and Git-blob readback before authorizing post-freeze retrieval. The freeze binds four published checkpoints, 29 file versions and 27 effective paths. Its metadata integrity run also checked the original ER, the exact taskbook/publication and both parent sources, and rejected an in-memory residual-count mutation. It did not replay mathematical checkers. The freeze and its receipt remain immutable; later routing/return material is separate.

## 2. Completed assignment classification and geometric RR reduction

The frozen curves are C: t²=R³−3R and D: w²=(R+2)t. The six cover branch points are C[2] together with P and −P, where P=(-2,i√2). The permitted k and lambda remain fixed. The parent exclusion of 6+0+0+0 was consumed, not recomputed; no exact contradiction requiring it to be reopened was found.

| Pattern | Raw labelled assignments | Fixed lambda, fixed k target V4 orbits | Cover-only V4 plus source flip | S4 transport plus source flip |
| --- | --- | --- | --- | --- |
| 4+2+0+0 | 180 | 45 | 33 | 11 |
| 2+2+2+0 | 360 | 90 | 54 | 9 |

The actual source involution t↦−t changes the critical divisor t=−k to t=k. It is not a symmetry of the fixed-k ODE. General anharmonic relabeling transports lambda; it cannot be used as an extra fixed-parameter quotient. Thus only the 45/90 column is used in the component census. The integer checker constructs and partitions all raw assignments and separately tests these distinctions.

Each representative is transported by an allowed V4 relabeling to an empty infinity fiber; the two choices in 4+2 are recorded without deleting or merging an orbit. For an even subset S_a of finite-fiber branch points, the geometric representative G_a obeys div(G_a)=S_a−2B_a. For a pair, a chord/tangent quotient supplies the representative after a symbolic half-point choice. The finite representatives are chosen with product G_0 G_1 G_lambda=(R+2)t. The unramified geometric classes are represented by 1, R, R−sqrt(3), R+sqrt(3).

Compatible torsion triples satisfy T_0+T_1+T_lambda=O: 16 choices, with the other 48 of the 64 triples excluded by compatibility. These are classes over an algebraic closure; this is not a classification of all original-field square classes. Constants, half-point definition fields and descent remain explicit obligations.

Writing gamma_a for a chosen torsion representative and B'_a=B_a+O−T_a gives

X−a = alpha_a G_a gamma_a u_a²,

with u_a in L(D_infinity−B'_a), where deg(D_infinity)=3. The dimensions are (1,2,3) for 4+2 and (2,2,2) for 2+2+2, in the recorded empty-infinity normalization. The variable pole class D_infinity~2O+S remains a parameter. The correct coupled equations are

alpha_0 G_0 gamma_0 u_0² − alpha_1 G_1 gamma_1 u_1² = 1,

alpha_0 G_0 gamma_0 u_0² − alpha_lambda G_lambda gamma_lambda u_lambda² = lambda.

After replacing u_a by v_a/d, their right sides are d² and lambda*d². No sign reversal is allowed. The independent differential/ODE, constant compatibility, exact degree and local denominator/basepoint gates have not been solved merely by writing these equations.

## 3. New partial theorem: every geometrically trivial finite empty class is impossible

In the 4+2 pattern, normalize one empty special fiber to infinity and call the other empty value e. Then the geometric square class of X−e must be nontrivial. This excludes exactly four of the sixteen compatible triples for each of the 45 fixed-parameter assignments.

Here is the proof chain, with the full proof and coefficient certificate preserved in the third checkpoint. A trivial class would give X=e+g² over the algebraic closure with deg(g)=3. The special X-fiber containing four branch points splits into two degree-three g-fibers. At its branch points the multiplicity is one and elsewhere it is even. Their branch-point counts must therefore split 3+1. One full fiber is a triple of distinct points U,V,W in the six-point branch divisor, forcing the pole class of g to be 2O+S with S=U+V+W.

The twenty triples give exactly ten possible S: C[2] and ±P+T for nonzero T in C[2]. Their finite horizontal coordinates u belong to Q(sqrt(3)), whereas k²=12sqrt(2)−10sqrt(3) does not. Hence these S avoid every ±Q with t(Q)=−k, and both v−k and 18u+k² are nonzero for S=(u,v).

The three Q lift to simple zeros of the prescribed differential on D. Local degrees force every Q to be a critical point of g, including g=0 and poles. A nonzero finite special g-value would force degree four and already contradict deg(g)=3. Thus the argument is not an unchecked inference from a rational derivative at a denominator zero.

S=O is excluded by the earlier L(3O)=<1,R,t> determinant argument. For a finite S use the three-dimensional basis <1,R,h>, h=(t+v)/(R−u), of L(2O+S). The cleared derivative at the three Q gives a homogeneous linear system in the three 2-by-2 numerator/denominator minors. Its integer-polynomial determinant is

det(M)=2k(v−k)²(18u+k²).

All factors are nonzero in the finite pole-class scope just proved. Therefore all three minors vanish, making g constant, a contradiction. Q≠±S justifies the denominator clearing, including pole frames. The determinant is not being promoted to a classification at arbitrary basis-degenerate S.

This excludes 45*4=180 geometric components of 4+2. No field extension or constant-square-class change can rescue a geometrically trivial class. It does not exclude the nontrivial classes or any 2+2+2 component.

## 4. New necessary filter for the nontrivial empty classes

For each nontrivial gamma=R−r_T, the normalization C_T of zeta²=gamma is a connected unramified double cover of C. The function g in X=e+g² now has degree six on C_T, not degree three. The preceding 3+1 argument must not be reused for it.

With D_infinity~2O+S, choose d in L(2O+S), n in L(3O+S−T); both spaces have dimension three, and g=zeta*n/d. Put D=2delta. Since Dgamma=2t, the exact cleared critical numerator is

W = t*n*d + gamma*((Dn)*d − n*(Dd)).

The checker verifies the derivative relation after clearing zeta²=gamma and zeta*D(zeta)=t, together with

W(rho*n,rho*d)=rho² W(n,d).

At each Q a regular local frame with no common numerator/denominator zero is required. The condition W(Q)=0 then covers finite values, zeros and poles. A common nonunit frame must be removed first. The exact examples n=d=1 and rho=t+k show respectively why dropping the connection term or retaining a vanishing common frame creates a false positive. These are lower-degree counterexamples to a proposed criterion, not reconstructed task maps.

This gives three necessary bilinear critical conditions once actual RR bases are specified on valid charts. It neither solves those systems nor proves the full ODE. It removes no additional component and makes no claim about the 2+2+2 class.

## 5. Exact residual and execution evidence

| Family | Before the new obstruction | Excluded | Remaining |
| --- | --- | --- | --- |
| 4+2+0+0 | 720 | 180 | 540 |
| 2+2+2+0 | 1440 | 0 | 1440 |
| Total | 2160 | 180 | 1980 |

A component is a geometric square-class/RR parameter family with a variable pole class and coefficients, not a zero-dimensional solution or a map. The reduced certificate is a finite-indexed exact geometric specification with necessary equations and a proved excluded subset. It is not a fully expanded, solved original-field polynomial system.

All paths in this table are beneath `research_artifacts/RB_BLIND_BRANCH_PATTERN_COMPLETION_20260908/`, except the assignment script and its test under `scripts/` and `tests/`.

| Checkpoint / published commit | Actual preserved evidence | Certificate SHA256 |
| --- | --- | --- |
| Assignment / b8c4fb6c8e86080699c67b65b863e1ce791f1263 | Integer assignment/orbit enumeration, readonly byte replay, 3 focused tests, selected static gate | a83524c6b9b8cb6e00561c014e7129c614e9b1c46eedcbd9c9e79f2ff5ee89a0 |
| Corrected square-class/RR / 2a2b39cc41b96c827df83cbe42f6c1882da05894 | 16 compatible/48 incompatible triples, 2 cleared identities, sign regression, readonly replay, 5 focused tests, selected static gate | d861e5b4d9d5b562c7e2a972c56b30144f2cd41275963f80a3aa80c5f1d3a289 |
| Empty-fiber obstruction / 77858e87d1ac0b277ca3d1e242432928019f398f | 3 integer identities, altered-coefficient rejection, all 20 branch triples, 3 focused tests, readonly replay, selected static gate | 1757b252b5926bcda198e4a652259e8d46da4cd3a32464ae66c09f3d403eafb9 |
| Twisted critical numerator / ad05f1ce0e1f06b64268681a1a57d08d2032e6ca | 3 twists, 6 derivative/frame identities, 6 omitted-term/nonunit-frame counterexamples, readonly replay, one-file static gate | a36593100cdc3a67465c45b1569222349575cda61660576595e4541df5056ef8 |

The original run receipts are `assignment_execution_receipt.json`, `squareclass_rr_execution_receipt_v2.json`, `empty_fiber_execution_receipt.json` and `twisted_critical_execution_receipt.json`. They preserve actual argv, exit codes and combined tool outputs at their original source versions. None was rerun for this stage closure. The local geometry and field arguments are paper proofs, not an independent generator replication or formal proof-assistant verification.

Root rejected an earlier RR draft because four difference signs were reversed. The corrected V2, including a genuine polynomial sign regression, is the active source. The earlier four-test receipt and rejected manifest hash remain historical evidence, not PASS evidence for the corrected paper. One duplicated Python-directory command failed to start; the later correct-runtime static command passed. These facts remain visible in the V2 receipt.

The checkers use integer enumeration and cleared formal polynomials. They do not evaluate ordinary division, remainder, roots, rational-function values, Fraction/float, or BRC calls. Symbolic quotient expressions and algebraic generators on a curve are paper data, not newly evaluated rational arithmetic, native spatial axes or a substitute for BRC. Parity, multiplicity and local valuation data were preserved before reduction. No ornamental BRC invocation or native migration is claimed; no new generic tool or family is registered.

## 6. Post-freeze source attempt and explicit comparison debt

After root confirmed immutable freeze commit `7791ddf5c969bb580cff04b1cb742ec3f9d8a9b9`, two bounded retrieval rounds were completed. The first used the exact original blind taskbook at c73816d and the two specifically suggested GK routes at `97fb3048dcb9ca1589006801d589525c31de7899`. The parent taskbook has no origin commit/path; the GK routes concern other directions. The second used three connected GitHub code-index queries, bounded to six results each: GK `CM24`, GK `Fermat`, and EM `Ramanujan Borwein`. All returned zero results without an error.

The source pins, original argv and query results are in `post_freeze_comparison.json`; `post_freeze_comparison.md` gives the scope. This is not an exhaustive source/history search. It does not show that the originating map is absent, that the self-audit is false, or that the task's formula cannot exist.

No originating formula, coefficients, basepoint, twist, scaling value or exact replay was actually obtained. Therefore no originating formula/scaling comparison, equivalence check, mismatch verdict or completed originating-candidate dedup is claimed. The correct status is `SOURCE_COMPARISON_UNRESOLVED`. A source holder must provide an immutable repository/commit/path before a separately recorded comparison can be made. Nothing found later may be inserted into the blind raw freeze or relabeled as an independent reconstruction.

No new mathematics was performed after the raw freeze. The limited routing reads belong to Phase B; the earlier blind proofs retain their original frozen bytes and provenance.

## 7. Task-output matrix and remaining obligations

| Required output | Stage status |
| --- | --- |
| 1. Complete symmetry-reduced assignments | Completed with explicit fixed-parameter, cover-only and transported-label distinctions. |
| 2. All four exact original-field square classes | Partial geometric representatives/compatibility and empty-infinity normalization; constants and descent unresolved. |
| 3. RR solution or obstruction for every survivor | 180 components obstructed; 1980 parameter components remain unsolved. |
| 4. Explicit map, degree, basepoint and target data if found | No map reconstructed; not supplied. |
| 5. Frozen ODE and pullback differential verification | Necessary identities/local filters only; no complete surviving-map verification. |
| 6. Independent period scaling if a map is found | Not derived. |
| 7. Both-pattern exclusion if no map exists | Not proved; no nonexistence claim. |
| 8. Timestamped SHA raw freeze before unblinding | Completed at the exact immutable commit and hashes above. |
| 9. Deterministic exact checker | Completed for the declared partial certificates; not a full map solver. |
| 10. Originating-package comparison | SOURCE_COMPARISON_UNRESOLVED after two bounded retrieval rounds; not passed. |
| 11. Durable return | This exact designated return path, pending owner source publication at creation. |

Nonempty residue: original-field half-point/constant square-class descent; explicit RR bases across all pole-class and regular-frame charts; the coupled fiber equations and full independent ODE for all 1980 survivors; exact map/degree/basepoint and independent differential/period normalization if a map is found; both-pattern exclusions if nonexistence is claimed; and the exact originating source required for Phase-B comparison. There is no all-pattern exclusion hidden behind a finite count.

Owner selected this legal INCOMPLETE stage return rather than extending the current computation. No new solver, claim, task or automatic mathematical successor is started here. The immediate evidence action is owner intake plus recovery of the exact originating source; a later mathematical continuation must preserve this frontier and its unresolved gates. Formal Result/Driver disposition and any review-followup decision remain the owner's canonical-writer responsibility. The parent remains OPEN.

Researcher-ID: EM-HODGEH0O-82EF42 / RS-RB-ENTERPRISE-DEGREE6-CM24-BLIND-BRANCH-PATTERN-COMPLETION
Global-Knowledge-Sync: main@97fb304 / GLOBAL_KNOWLEDGE_V1
