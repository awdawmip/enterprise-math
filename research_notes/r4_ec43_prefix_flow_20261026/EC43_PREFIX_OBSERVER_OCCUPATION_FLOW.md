# R4-EC43 — Exact prefix-observer occupation flow for two-measure positive BRC

**Evidence status:** Author-side complete mathematical arguments and exact finite code checks. This is not a formal Enterprise Math Task CLAIM, native Result, Guard pass, independent Driver acceptance, Working Truth or Heartbeat/X6 theorem.

## Authority, source scope and lineage

- Authenticated connected GitHub actor: awdawmip. Live Source task and owner query attempted through native gateway and returned CONTROL_QUOTA. No live owner or CLAIM is inferred.
- One fixed knowledge read: awdawmip/chatgpt-global-knowledge main@ad6b20175a75b09038ffaa5e43ec737463299e1e. Entry files: 00_BOOTSTRAP.md and OPERATING_MANUAL.md. Loaded project role router, P000_STARTUP and P000_REALITY_FOUNDATION (matching original Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc) and ACTIVE 我眼中的世界. P000 is ACTIVE_LOCKED; fixed_heartbeat_program is null.
- Source reading pin: awdawmip/enterprise-math main@3904b76c1bf49d5341b59f3a1aeebe059d0a0dad. Relevant current rules: docs/PORTABLE_RESEARCH_PROTOCOL.md, research_persistence_policy.json, control_plane/research_delivery_policy.json, docs/RESEARCH_ACTIVITY_PROTOCOL.md, definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json, definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json, research_method_inventory.json and tool_invocation_policy.json.
- Direct scientific predecessor: R4-EC42 author-side result, immutable 5b079d3e38650e2138c10687ec3d76aa27873063, research_notes/r4_ec42_timing_profile_20261026/EC42_THREE_STAGE_STOPPING_PROFILE.md. EC42 handled a first-stage quotient then revealed original source paths. The present result controls stagewise quotients at *every* decision.
- Typed BRC reuse: existing T0_BRC positive-rational labelled-source carrier and its provenance/branch multiplicity constraints, and EC40–EC42 exact two-measure stop/decision observers, applied at their stated scopes. Ordinary exact finite-tree occupation flows are a specialization, not a newly claimed generic tool family.

This is a finite two-hypothesis abstract *positive labelled-source decision tree*, not a six-dimensional physical update. Decision depth is not native Heartbeat time. No third-slice-coordinate transfer or native physical propagation is asserted.

## 1. Exact object and prefix-respecting observer

For t=1,...,N, let H_t be finite sets of complete ordered source histories with a unique parent pa(h) in H_{t-1}, and let strictly positive rational uncontrolled P and Q path-prefix masses m_i(h) obey:

- sum over H_1 of m_i(h) = 1 for both i in {P,Q}.
- For each t<N and h in H_t, m_i(h) = sum over children k of h of m_i(k).

At any reached history a policy may stop and declare P, stop and declare Q, or continue, except that continuation is disallowed at t=N. Randomized policy decisions depend only on available observed history, with the *same decision law* under P and Q. The four exact observables are

$$
v=(e_P,e_Q,t_P,t_Q)=
(P(\text{declare Q}),Q(\text{declare P}),\mathbb E_P[\tau],\mathbb E_Q[\tau]).
$$

A family of surjective statistics T_t:H_t -> X_t retains its *own prefix* when there are parent maps pa_X:X_{t+1}->X_t satisfying

$$
T_t(pa(h))=pa_X(T_{t+1}(h)) \quad\text{for all }h\in H_{t+1}. \tag{43.PREFIX}
$$

The disjoint union of X_t is then a rooted *observer forest*: the current observed node uniquely encodes the chain of earlier *retained* observations. Original hidden history need not be reconstructible. Define aggregated uncontrolled masses

$$
M_i(x)=\sum_{h:T_t(h)=x}m_i(h).
$$

Mass conservation and the prefix identity give
$$
\sum_{y:pa_X(y)=x}M_i(y)=M_i(x)
$$
for every nonterminal x and both hypotheses. All original multiplicities, source labels, and branch identities are retained before the declared four-observer quotient.

## 2. Theorem EC43.1 — exact rational occupation-flow polytope

Introduce at every observer node x nonnegative survival s_x and action occupation factors z_x^P,z_x^Q,z_x^C, satisfying the following linear system:

$$
\begin{aligned}
s_x&=1 && (x\in X_1),\\
s_y&=z_{pa_X(y)}^C && (y\in X_t,\ t>1),\\
z_x^P+z_x^Q+z_x^C&=s_x &&(\text{all }x),\\
z_x^C&=0 &&(x\in X_N),\\
s_x,z_x^P,z_x^Q,z_x^C&\ge0. &&
\end{aligned}\tag{43.FLOW}
$$

**Claim.** The *entire attainable region*, over all randomized stagewise policies depending only on current x, is exactly the linear image

$$
\begin{aligned}
e_P&=\sum_x M_P(x)z_x^Q,
&
e_Q&=\sum_x M_Q(x)z_x^P,\\
t_P&=\sum_x t(x)M_P(x)(z_x^P+z_x^Q),
&
t_Q&=\sum_x t(x)M_Q(x)(z_x^P+z_x^Q).
\end{aligned}\tag{43.OBS}
$$

It is a compact rational convex polytope (rational vertices and inequalities), and no enumeration of the exponentially many complete deterministic policies is required to write this description.

**Proof (both directions).** For a behavioral observer policy write q_x^a for its action probabilities a in {P,Q,C}. Because (43.PREFIX) forces every original history h with T(h)=x to have the *same entire compressed ancestor chain*, the probability of surviving all earlier decisions is a single s_x common to those hidden histories and to both hypotheses. Roots have s_x=1, and a projected child y satisfies s_y=s_{pa_X(y)}q_{pa_X(y)}^C. Put z_x^a=s_x q_x^a, proving every equation (43.FLOW). Under hypothesis i the mass arriving at x is M_i(x)s_x, so weighted stopping/decision sums yield exactly (43.OBS).

Conversely, take any feasible nonnegative (43.FLOW). If s_x>0 set q_x^a=z_x^a/s_x; if s_x=0 choose an arbitrary legal distribution because every corresponding z is zero. Induction from observer roots proves these choices realize precisely the specified survival and occupation factors. Therefore the original behavioral policy produces (43.OBS), proving both set inclusions. Root normalization and positivity bound all flows; rational input coefficients imply rational polyhedrality. QED.

**Scope boundary.** The result concerns this declared four-scalar stop/decision observer with perfect recall of *retained* observations. It does not establish preservation of all hidden source labels or any future operation outside the declared decision tree.

## 3. Theorem EC43.2 — Bellman exact primal/dual certificate

For real support normal lambda=(alpha,beta,gamma,delta), let d=t(x), and set
$$
A_x=\beta M_Q(x)+d[\gamma M_P(x)+\delta M_Q(x)],
\quad
B_x=\alpha M_P(x)+d[\gamma M_P(x)+\delta M_Q(x)].
$$
These are respectively the contributions per unit survival factor when stopping at x and deciding P or Q. Evaluate from the leaves upward:
$$
U(x)=
\begin{cases}
\min(A_x,B_x),&d=N,\\
\min\left(A_x,B_x,\sum_{y:pa_X(y)=x}U(y)\right),&d<N.
\end{cases}\tag{43.DUAL}
$$
Then the exact minimum linear support of the attainable region is
$$
\boxed{V_X(\lambda)=\sum_{x\in X_1}U(x).}\tag{43.SUPPORT}
$$
For rational masses and lambda, all values are exact rational and the computation takes O(number of observer nodes) arithmetic operations; rational integer-bit complexity may grow.

**Proof and explicit dual lower bound.** Each U(x) is no greater than the stop-P cost A_x or stop-Q cost B_x, and at an internal node no greater than the sum of children's U. Multiply these valid inequalities by the respective nonnegative flows z_x^P,z_x^Q,z_x^C. Since their sum is s_x, add all node inequalities. The continuation terms telescope exactly via s_y=z^C_{pa_X(y)}. What remains is the dual lower bound
$$
\lambda\cdot v\ge\sum_{root\ x}U(x).
$$
Select at every x a deterministic action achieving the relevant minimum defining U(x); where s_x=0 the action is immaterial. All inequalities used along this policy's positive-flow nodes become equalities, attaining the bound. This is simultaneously a primal minimizing policy and a dual certificate, proving (43.SUPPORT). QED.

**Finite, exact four-region equivalence procedure.** Denote by R_H the full-original-information region (identity observer) and R_X the prefix-statistic region. Every compressed policy is also a full-history policy, hence R_X is contained in R_H. From (43.FLOW)/(43.OBS) obtain an exact rational H-representation of R_X by polyhedral projection, including *paired affine-hull equalities* as inequalities lambda_j dot v >= b_j. Then
$$
R_H=R_X\iff V_H(\lambda_j)\ge b_j\ \text{for every such inequality}.
$$
This is necessary and sufficient because every point in R_H must satisfy each defining inequality of R_X, and sufficient because the inequality family defines R_X. V_H is supplied exactly by (43.DUAL) on the identity tree. Failed inequality gives a constructive separating normal and full-history policy witness. Finite rational facet/projection procedures exist; **none was executed in this run** and facet output may be exponential. The linear-work bound applies to one *support query*, not full equivalence enumeration.

## 4. Exact EC42 witness reproduced by a new occupation-flow calculation

There are first histories a,b, each of common initial P/Q mass 1/2. Ordered terminal labels are (z1,z2) in (00,01,10,11). Strictly positive source counts out of 8 per history and hypothesis:

| h and hypothesis | 00 | 01 | 10 | 11 |
|---|---:|---:|---:|---:|
| a / P | 3 | 3 | 1 | 1 |
| a / Q | 1 | 1 | 3 | 3 |
| b / P | 3 | 1 | 3 | 1 |
| b / Q | 1 | 3 | 1 | 3 |

The full tree has 14 nodes. An observer merging just the first-stage nodes a,b into x and then revealing the full ordered later labels has 13 nodes and satisfies the prefix law: all four depth-two nodes have the same retained parent x. For lambda=(1,1,1/6,1/6), the Bellman root values are
$$
U_H(a)=7/12,\quad U_H(b)=2/3,\quad U_X(x)=4/3.
$$
Consequently
$$
\boxed{V_H=5/4,\quad V_X=4/3,\quad V_X-V_H=1/12}.
$$
An optimal full strategy continues at a and stops at b; the compressed first decision must be shared. This agrees with EC42's independent full-policy enumeration while replacing its search by a per-node rational primal/dual certificate.

The companion verifier enumerates **625 signed integer normals** in {-2,-1,0,1,2}^4, finding **4 strict support gaps**, and independently checks the Bellman support against the algebraic EC42 first-decision decomposition for every normal. The separately run full Python Fraction verifier also checked 200 seeded randomized policies against *original source-path* probabilities, plus 27 structural checks. The universal theorem is established by the proof, not extrapolated from these tests.

## 5. EC43.4: rigorous boundary when a statistic forgets an observed ancestor

At depth 1 keep distinct a,b, with uncontrolled positive masses
$$
(m_P(a),m_P(b))=(3/4,1/4),\quad
(m_Q(a),m_Q(b))=(1/4,3/4).
$$
Each root has exactly one deterministic child, respectively (a,0) and (b,0). At depth 2 erase the first label by merging both children into x. This is a multiple-parent observation node, **violating (43.PREFIX)**, because its previous observed symbol could be a or b.

The policy stops at a, continues at b, then at x declares Q. The probability of reaching x equals 1/4 under P and 3/4 under Q. Yet the uncontrolled aggregated masses are M_P(x)=M_Q(x)=1. A common survival scalar s_x would require simultaneously s_x=1/4 and s_x=3/4, impossible. Thus the simple prefix-flow equation cannot be applied without alteration. This counterexample does not assert that *all* forgetful statistics are unsafe; it proves only that forgetting an ancestor invalidates the general single-scalar occupation-flow derivation. An exact extension must retain conditional arrival mixtures, predecessor-indexed flows, or a perfect-recall refinement.

## 6. Reproduction, limits and EC44 next question

Published verification: EC43_verify.js plus EC43_JS_REPORT.json use exact scaled integers (source masses denominators 16, signed normals) for 625 support checks, the 14/13 node graph and the 1/12 witness. A separate complete Python Fraction execution (available in the accompanying locally exported EC43 evidence bundle) has 625 supports, **200** independent randomized-policy path/flow comparisons and 27 structural checks; the latter is not claimed to have been run by the GitHub JavaScript program. Neither tool performs native X6 propagation. Evidence is author-side only; the current Research Activity Guard, native Result, independent Driver mathematical review, and canonical math admission are not passed.

**EC44 precisely remaining:** For a finite *non-prefix-respecting* observer which forgets retained ancestors at later stages, find the minimal exact hypothesis-coupled occupancy carrier. Determine whether predecessor-indexed survival plus P/Q conditional weights linearizes four-observer propagation when the policy has only current symbol and randomized private memory, and distinguish true behavioral region from its publicly correlated convex hull. Produce an exact rational restricted theorem or minimal counterexample with original-source integer counts. Separately, obtaining an actual native X6 heartbeat update, selected three-axis slice with explicit third coordinate, and independent time correspondence remains pending (P000 fixed_heartbeat_program=null).
