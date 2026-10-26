# R4-EC44 — Forgetful BRC observers: exact source-indexed carrier, nonconvexity and one-bit-memory gap

**Status:** author-side proved derivation + exact finite cross-check; NOT a native Task CLAIM, frozen Result, Guard pass, independent Driver review, Working Truth, Foundation result or original-X6 theorem.

## Source scope and provenance

- Fixed account knowledge snapshot: awdawmip/chatgpt-global-knowledge **main@eb77c4eeaf1843ea5f25a89328a0becf85aea6d4** (verified 2026-10-26). Read canonical 00_BOOTSTRAP.md, OPERATING_MANUAL.md, TASK router, P000_STARTUP.json (original P000 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc confirmed) and ACTIVE 我眼中的世界.md. P000 remains ACTIVE_LOCKED with fixed_heartbeat_program=null.
- Enterprise Math input snapshot: main@867efd7b9469fda5104716ca4506b819110dd054, including docs/PORTABLE_RESEARCH_PROTOCOL.md and current persistence/delivery protocols. Immediate scientific predecessor: EC43 immutable 53ac107728137ad054e966973f0bf3aef351a7a0, research_notes/r4_ec43_prefix_flow_20261026/EC43_PREFIX_OBSERVER_OCCUPATION_FLOW.md, proving linear flow for prefix-respecting observers and asking for the nonprefix case.
- Identity: GitHub user awdawmip, repo admin. Native owner/tasks read returned CONTROL_QUOTA; native session_start returned STATIC_READONLY_SCOPE_DENIED, operation_sent=false. No native Researcher session or formal claim was created; this is independent author-side evidence.
- **BRC REUSE_APPLIED:** definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json (positive-rational branch mass, multiplicity/provenance) and definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json (joint future-operation safety), plus EC43's two-measure stop/decision observer. This is an *auxiliary finite labelled-source decision tree*, not native X6 dynamics or a three-dimensional slice. The Enterprise coordinate map cannot be applied without a specified native update and third-coordinate/time bridge.

## 1. Three controller contracts, not one

Fix finite original ordered-source history levels H_t with unique parent pa(h). Uncontrolled prefix masses m_P(h),m_Q(h)>0 are rational, sum to one over H_1 and conserve under each parent's children. A reached node may stop and declare P, stop and declare Q, or continue (C, only before terminal N). The four outputs are

$$v=(e_P,e_Q,t_P,t_Q)=(\Pr_P[\mathrm{declare}\ Q],\Pr_Q[\mathrm{declare}\ P],\mathbb E_P\tau,\mathbb E_Q\tau).$$

The declared **current-only memoryless** controller at stage t sees x=T_t(h), not necessarily the previous observed x. It chooses the **same** distribution q_x=(q_x^P,q_x^Q,q_x^C) at every original history h with T_t(h)=x. Local randomization is fresh, with no seed remembered over time. A different, *publicly correlated* controller first chooses an entire memoryless deterministic plan using a persistent ex-ante seed. Another distinct controller stores finite internal memory of its own previous observations. These three policy classes cannot be identified without proof.

## 2. Theorem EC44.1: exact quadratic original-source flow

Introduce for every original history h survival r_h>=0 and decision flows d_h^P,d_h^Q,d_h^C>=0, with

$$r_h=1\ (h\in H_1),\qquad r_h=d_{\mathrm{pa}(h)}^C\ (t>1),$$

$$d_h^P+d_h^Q+d_h^C=r_h,\qquad d_h^C=0\ (t=N),$$

and, for each pair h,k at the same stage mapped to the same current observer x, impose, for a=P,Q,C,

$$\boxed{d_h^a r_k=d_k^a r_h.}\tag{44.RANK1}$$

Then the **entire** current-only memoryless four-observer attainable region is exactly the linear image of the **nonnegative quadratic feasible set** under

$$e_P=\sum_hm_P(h)d_h^Q,\qquad e_Q=\sum_hm_Q(h)d_h^P,$$
$$t_i=\sum_h t(h)m_i(h)(d_h^P+d_h^Q),\quad i=P,Q.\tag{44.OBS}$$

**Proof, forward.** A memoryless controller yields one q_x at each current observer x. Along each original history, r_h is the product of prior continuation probabilities and does not depend on the hypothesis conditional on h; hence d_h^a=r_h q_{T_t(h)}^a. All conservation, terminal and cross-product equations follow. Summing the original source probabilities gives (44.OBS).

**Proof, converse.** For any current observer fiber containing a positive-survival history h, set q_x^a=d_h^a/r_h. Equation (44.RANK1) makes this independent of the chosen positive-survival h. If r_k=0 then all d_k^a vanish. When the whole fiber is unreachable choose any legal action vector. At terminal x enforce q_x^C=0. Induction on t reconstructs every r_h,d_h^a and the given output under this single current-symbol policy. QED.

The model is an exact **source-indexed sufficient carrier**. No claim is made that it uses the globally minimum number of state variables. Erasing (44.RANK1) falsely permits source-dependent terminal actions after source ancestry was forgotten. When T_t is prefix-respecting in EC43's sense, r_h is constant across each observer fiber, and the equations descend to EC43's **linear** observer-node occupation flow. Otherwise that descent is not justified.

## 3. EC44.2: complete membership criterion for the smallest two-root forgetful model

At stage 1 observe a or b; when continuing, stage 2 exposes a **single common symbol x**, forgetting which root was observed. The single original terminal child of a is ax and of b is bx. Original-source **strictly positive** counts out of four are

| root | P | Q |
| --- | ---: | ---: |
| a | 3 | 1 |
| b | 1 | 3 |

Write c_h for first-stage continuation probability and u_h for eventual probability of choosing Q conditional on the original root h. Let r be the **common** terminal probability of declaring Q at x. Let d_h be first-stage stopping-and-declaring-Q probability. Then

$$u_h=d_h+c_h r,\qquad 0\le d_h\le1-c_h,\quad 0\le c_h,r\le1.$$

For an observed vector v, the latent quantities are uniquely determined by the nonsingular original mass matrix:

$$c_a=\frac{3(t_P-1)-(t_Q-1)}2,\quad c_b=\frac{3(t_Q-1)-(t_P-1)}2,$$
$$u_a=\frac{3e_P-(1-e_Q)}2,\quad u_b=\frac{3(1-e_Q)-e_P}2.\tag{44.INVERT}$$

**Exact iff:** v is attainable by a memoryless current-symbol policy precisely when 0<=c_a,c_b<=1 and

$$\boxed{[0,1]\ \cap\ \bigcap_{h:c_h>0}
\left[\frac{u_h+c_h-1}{c_h},\,\frac{u_h}{c_h}\right]\ne\varnothing,}\tag{44.MEMBER}$$

with 0<=u_h<=1 for c_h=0.

**Proof.** Direct source-mass identities are
$4(t_P-1)=3c_a+c_b$,
$4(t_Q-1)=c_a+3c_b$,
$4e_P=3u_a+u_b$ and
$4(1-e_Q)=u_a+3u_b$.
Their coefficient matrix has determinant 8 and yields (44.INVERT). The inequalities for d_h=u_h-c_h r transform exactly to (44.MEMBER). Any r in the intersection reconstructs valid first-stage P/Q/C probabilities; conversely any feasible policy supplies such r. QED. For rational v this is a finite exact rational interval certificate.

## 4. EC44.3: the memoryless four-region is nonconvex, despite positive BRC source masses

Consider two pure memoryless policies:
A continues only after a, stops P after b, and at terminal x declares Q.
B stops Q after a, continues only after b, and at terminal x declares P.

Original-source counting gives

$$v_A=(3/4,3/4,7/4,5/4),\quad v_B=(3/4,3/4,5/4,7/4).$$

Their midpoint is
$$v_*=(3/4,3/4,3/2,3/2).$$

Applying (44.INVERT) forces c_a=c_b=1/2 and u_a=1,u_b=0. Since both initial roots continue with positive probability, u_a=1 forces r=1, while u_b=0 forces r=0. This contradiction proves that v_* is **not** memoryless attainable. Therefore the image (44.OBS) of memoryless nonprefix policies is generally **nonconvex**; no ordinary LP occupation polytope can project **exactly** to that set. Yet v_* is realized by a 50–50 initial public seed choosing whole plan A or B. That common seed is a persistent correlation resource, not independent memoryless decisions.

## 5. EC44.4: a public coin does not recover one bit of forgotten observation

For any finite time-indexed memoryless policy, every complete-path probability is a product of local action variables, with each current observer x appearing at most once along a path. Hence each coordinate of the four-vector is **multi-affine** in the q_x. Independently preselect a pure action for each x according to q_x; averaging the resulting pure complete plans reproduces the memoryless four-vector. Conversely every pure plan is memoryless. Thus

$$\mathrm{conv}(\mathcal R_{\rm memoryless})
=\mathrm{conv}\{v(\pi):\pi\ \text{pure current-symbol plan}\},$$

the exact region for persistent ex-ante selection among current-symbol plans.

For the two-root model there are exactly 3^2*2=18 pure plans. Take L(v)=e_P+e_Q+t_P+t_Q. If both roots continue, total expected-depth sum is 4, terminal choice is common, and error sum is 1, giving L=5. If exactly one continues, time sum is 3 and error sum is at most 3/2, so L<=9/2. If neither continues, time sum is 2 and error sum at most 3/2, hence L<=7/2. Multi-affinity and linear optimization over mixtures yield

$$\boxed{\max_{\rm memoryless\ or\ public\ correlated}L=5.}\tag{44.PUBLIC}$$

Instead store **one bit** indicating whether the observed first root was a or b. Always continue, and at the common current terminal x declare Q when stored=a and P when stored=b. This gives

$$v_{\rm bit}=(3/4,3/4,2,2),\qquad L(v_{\rm bit})=11/2>5.$$

Therefore the full observed-prefix/private-memory region **strictly contains** even the publicly correlated hull of current-symbol plans. One bit is sufficient and zero bits insufficient *for this witness*; no global minimum-memory claim is made.

More generally, if unrestricted finite internal memory can store all previously **observed** symbols (not hidden source symbols), then observed-prefix sequences form a prefix-respecting tree. EC43's linear occupation-flow theorem applies to that augmented *observable* tree and gives an exact rational polytope for the finite-horizon full-observation-history decision region. Never promote this observer-prefix claim to retention of unobserved source labels.

## 6. Computation, mathematical strength and next obligation

The companion EC44_verify.js performs **1125** exact finite-grid current-symbol checks: root action distributions with denominator 4 (15 possibilities per root) and terminal Q probability in {0,1/4,1/2,3/4,1}. It compares original-source path enumeration with original-history occupation flow, tests conservation and rank-one terminal identities, and checks (44.MEMBER). It separately checks **18** pure policies, L maximum 5, two midpoint witnesses, and a deliberately incompatible terminal-flow rank-one rejection. Independent Python Fraction verification, including byte-for-byte cold-start reproduction, is retained in the corresponding user-delivered evidence archive. The universal theorems follow from the proofs above, not finite-grid extrapolation.

**Limitations:** no native Result/Guard/Driver review/formal proof assistant; no fixed Heartbeat update, X6 three-dimensional slice third-coordinate relation or physical-time bridge. Positive two-measure source probability is not signed or complex amplitude.

**R4-EC45 next question:** For a fixed K-state stochastic private-memory controller on a general nonprefix observer, construct the smallest sufficient source-history-plus-controller-memory occupation carrier, with exact P/Q and four-output observation. Determine when its semialgebraic rank constraints admit a finite exact linear lift, and find the smallest example distinguishing K=1,2,3 while separating private observation memory from a seed selecting memoryless plans.
