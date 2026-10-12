# Complete Cauchy-layer covariance reduction and declared inner-mechanism obstruction

Driver-ID: EM-DVR-FBF223 / CONTROL_PLANE
Driver-Session: MCP-cd5eefdde49843898b2a70c1af94d8dd
Driver-Authority: DA-A1DB35C00ED2F8C2A9FA
Task: RS-PERFECT-PRIME-AP-BINOMIAL-CAUCHY-LAYER-COFACTOR-POSITIVITY
Publication: TP2-5A3E91C7D2B40F681AC3
Frozen-Result: RR-A4EBF925BE07691C8C16
Review disposition requested: ACCEPTED / TASK only / parent OPEN

Root is the actual current nonauthor native Driver for this review. Prior Root identity/session history is retained: EM-DVR-FBF223, EM-DVR-4C90FB, EM-DVR-C1A1D9, EM-DIRECT-E1F2B6, EM-DIRECT-FA0C27, EM-DIRECT-49ADE6. The primary frozen-result author is EM-PPTAPBCP1-646AAA. Root has read the existing scientific return and historical review before this directed nonblind assessment; no blind or clean-room status is claimed. The auxiliary algebraic reader /root/backend_route_audit is UNKNOWN / DIRECTED_NONBLIND and supplies no native authority. The original helper draft is retained unchanged and explicitly attributed below.

## Scope and actual current intake

The result's full3516B from immutable Source7ba10a0854d96df96a50aec004f79413749d3403 has SHA256dd0c8f552c510d930b1ccf798db8582813fcea3ed19c81f3a4ca69a9ac7aa58b and Gitblob a47bef2117025ab825b1d420debcaf9ec1292e94. Root's own actual result read530 is complete, hash-verified and byte-identical; it binds own continuation529, whose unrestricted source_access_policy.verified_driver_review_view is true. Root independently fetched all4 scientific output files and the historical Driver report at that same Source; their bytes/SHA256/Gitblob match the frozen manifest. The old DR-9986FE430DB065EA8EF2 is preserved as an historical ACCEPTED source record, binding precisely this RR SHA.

The current native exact review-flow531 at18:04:33UTC/Sourcec9bddf939b23c653658f2b532966df7b2b4f778a identifies this same Root SID/DA/Driver and reports exact_reviews=[], review_ids=[], NO_REVIEW, terminal=false, reference_passes=[] and operational_review_authority=null. Root's current verified Driver intake therefore requests its first operative review of this exact frozen result. The historical Source DR is neither erased nor recounted as an operative parallel review. These observations do not diagnose why it was not admitted, and no hash drift is alleged. There is no live scientific claim or lease on current Task528. No other chat is stopped or taken over; the native parallel-review machinery retains control over any concurrent review.

## Root mathematical assessment

Root independently verifies the identities below: single-sided degree<=n division, the second outer finite-difference cancellation required for gh of degree<=2n, total-coordinate determinant detV_x with the original right-node values retained, positivity of the aggregate beta mass even at t=1, the cofactor determinant lemma, and the bordered inertia computation with the invertible change (r,x)->(r,y=r+x). This accepts the declared inner-definiteness mechanism obstruction. It does not claim a zero of the full outer determinant or the least failure of a different mechanism. The t=0 rank-degenerate case is explicitly excluded from the inner inertia claim.

This is a proof review and current intake of existing scientific work; no old checker or fixed-dimension census is rerun, no new scientific Task/claim is opened, and no novel theorem claim is attached to the Source reuse. The actual remaining problem detS_m(t)!=0 for allm>=2,0<t<=1 already has an outer-determinant successor TP2-C4B48A416649C9324011; it must not be duplicated. Coefficient positivity is a sufficient route, not an equivalent necessary target.

## Attributed auxiliary derivation, reviewed by Root

# 旧 Cauchy 多层负边界：数学审查草稿

对象：`RR-A4EBF925BE07691C8C16`，Task `RS-PERFECT-PRIME-AP-BINOMIAL-CAUCHY-LAYER-COFACTOR-POSITIVITY`，publication `TP2-5A3E91C7D2B40F681AC3`。

本稿由 `/root/backend_route_audit` 作定向非盲数学辅助，身份 `UNKNOWN / DIRECTED_NONBLIND`。它重建已有返回的论证，不是新的 native 审查，不借用 Root 的 DA 或会话；Root 尚未最终 Source/native 签署。本稿不宣布 Task DONE、母 Goal 完成或当前 review-flow 的原因。未重跑 checker，也未作新实验。

**数学结论草稿：全交替层 cofactor 到外层 signed covariance 行列式的约化成立；内层块对所有 m>=3 都不定，确实阻断逐块正定/负定的既定机制。此为原 Taskbook 明文允许的负边界返回，既未证明也未反驳母问题全 m 非消失。**

## 1. 完整双二项式层 residue：两次余式消去

令 n=m-1，b=m^2，i,j,s=0,...,n，并记

    u_i=-(i+1), y_j=mj, z_(j,s)=y_j+bs,
    w_i=(-1)^i binom(n,i), w_j=(-1)^j binom(n,j).

对 degree<=n 的 g,f,h,k，用 p_i=g(u_i)、q_j=f(y_j) 表示原左右向量。单层 Laplacian 的双线性型是

    B_s((g,f),(h,k))
      = sum_(i,j) w_i w_j
          [g(u_i)-f(y_j)][h(u_i)-k(y_j)]/(z_(j,s)-u_i).

定义

    R_P(z)=sum_i w_i P(u_i)/(z-u_i),
    c(z)=sum_i w_i/(z-u_i)=n!/product_(r=1)^m(z+r).

最后一个式子由简单分式留数或 n 阶有限差分直接得到。对 degree P<=n，由

    R_P(z)-c(z)P(z)
      = -sum_i w_i [P(u_i)-P(z)]/(u_i-z)

可知右边对 u_i 的次数不超过 n-1，故内层 n 阶二项式差分将它完全消去。因此 R_g=cg、R_h=ch。

**对 gh 不能直接沿用这一单边插值结论。** gh 的次数可达 2n。其除法余式经内层差分后，只有 u_i 次数至少 n 的项可能留下；总次数最多 2n-1，故留下的是关于 z 的次数至多 n-1 的多项式 E_(gh)(z)：

    R_(gh)(z)=c(z)g(z)h(z)+E_(gh)(z),  deg E_(gh)<=n-1.

固定 s 后，z_(j,s)=mj+bs；外层 n 阶二项式差分给出

    sum_j w_j E_(gh)(mj+bs)=0.

展开原 B_s，交叉项利用 R_g=cg、R_h=ch，gh 项利用这第二次消去，才得到完整的层 residue：

    B_s=sum_j w_j c(z_(j,s))
             [g(z_(j,s))-f(y_j)][h(z_(j,s))-k(y_j)].

这一步保留了完整 i、j 两个二项式求和，没有把 degree 2n 的 gh 错当成 degree<=n 的单边插值数据。

## 2. 全层叠加、正聚合质量与完成平方

置

    lambda_(j,s)=(-1)^s binom(n,s)t^s c(z_(j,s)),
    Dcal_j=sum_s lambda_(j,s).

有限层求和与 beta 积分表示给出

    Dcal_j(t)=integral_0^1 v^(mj)(1-v)^n(1-t v^b)^n dv.

故 Dcal_j>0 对全部 m>=2、0<=t<=1 成立。特别在 t=1，积分核在 0<v<1 上仍严格为正；端点 v=1 处的消失不使积分为零。

令

    mu_j(g)=sum_s lambda_(j,s)g(z_(j,s))/Dcal_j,
    Ccal_j(g,h)=sum_s lambda_(j,s)g(z_(j,s))h(z_(j,s))
                 -Dcal_j mu_j(g)mu_j(h).

直接完成平方得到

    B_t=sum_j w_j Dcal_j [f(y_j)-mu_j(g)][k(y_j)-mu_j(h)]
          +sum_j w_j Ccal_j(g,h).

这是 signed covariance 的代数恒等式；lambda 有交替符号，不能把 Ccal 当作正概率质量下必然非负的 variance。全部三层及更多层的干涉仍保留在外层和中。

在非恒定多项式基 X,...,X^n 上，记 C_j 为 Ccal_j 的矩阵，S_m=sum_j w_j C_j。常数方向在每个 Ccal_j 中均为零。

## 3. Canonical cofactor：只有 V_x 的平方因子

原右变量本来就是 q_j=f(y_j) 的任意节点值；不必再引入右侧多项式系数。若 a 是 g 的系数向量，令

    p=V_x a,  V_x[i,r]=u_i^r,
    q=mu(a)+eta.

从新坐标 (a,eta) 到原坐标 (p,q) 的总变换是块三角矩阵 P，其右下块为 I，故

    det P=det V_x,
    |det V_x|=product_(k=1)^n k!.

完成平方后的合同矩阵为

    P^T L_t P = S_m^full direct_sum diag(w_j Dcal_j),

其中 S_m^full 的第一行列（g 的常数方向）为零，其余主块为 S_m。又因为 mu_j(1)=1，P 将该单一常数坐标 e_0 映到原完整 all-ones gauge 向量。

原 L_t 对称且 L_t 1=0，故 adj(L_t)=tau_m(t) 11^T；若秩更低则两边同时为零。使用对奇异矩阵也成立的合同伴随式

    adj(P^T L_t P)=det(P)^2 P^(-1)adj(L_t)P^(-T)

并比较 e_0e_0^T 项，得到

    tau_m(t) = [product_j w_j Dcal_j(t)] det S_m(t)
                / [product_(k=1)^n k!]^2.

没有额外 V_y 因子：右侧一直使用原 q_j 节点坐标，完成平方的 eta 平移是单位行列式三角变换。每个 w_j 非零、Dcal_j>0，因而在 0<t<=1 上

    tau_m(t)!=0  iff  det S_m(t)!=0.

## 4. 内层行列式与全 m 惯性

以下要求 **0<t<=1**。此时每个 lambda_(j,s) 都非零，符号为 (-1)^s。对固定 j，令

    Lambda=diag(lambda),
    A=Lambda-lambda lambda^T/Dcal_j.

A1=0。删去任意一个坐标后的行列式引理给出

    det A[hat(k),hat(k)]=product_s lambda_s/Dcal_j.

完整节点 Vandermonde 把恒定列与非恒定列分开。设

    Delta_j=product_(r<s)(z_(j,s)-z_(j,r)),

则同样的伴随合同公式给出

    det C_j=Delta_j^2 product_s lambda_(j,s)/Dcal_j.

节点互异，故 C_j 非退化，且其行列式符号为 (-1)^(n(n+1)/2)。

更强的惯性结论来自边框矩阵

    G_j=[[Dcal_j,lambda^T],[lambda,Lambda]].

其二次型是 sum_s lambda_s(r+x_s)^2。以 y_s=r+x_s 作可逆变换，得到一个零方向以及 Lambda 的惯性。若 e=floor(n/2)+1、o=ceil(n/2)，则 In(G_j)=(e,o,1)。另一方面 Dcal_j>0，Schur 补给出

    In(A)=(e-1,o,1).

去掉其唯一常数核，并经非恒定 Vandermonde 拉回，得到

    In(C_j)=(floor(n/2),ceil(n/2),0).

所以 m=2 内层负定；所有 m>=3、每个 j、全部 0<t<=1 的内层都不定。合同变换不能将这些内层变为正定或负定。因此以“每个内层块都定号”为前提的 direct conditional-variance / termwise positive inner Andreief 机制被确切阻断；这不排除其他保持完整符号抵消的 Andreief 或外层证明。

**t=0 不在这个惯性结论中。** 此时只有 s=0 的 lambda 非零，A=0、C_j(0)=0；不能延续上述非退化惯性。返回借助已有 accepted crossing theorem，另行获得 ord_(t=0)tau_m=m-1，二者没有冲突。

## 5. 已有证据的强度与真正剩余问题

本稿重建的全 m 结论是精确 full-layer residue、outer determinant 约化、Dcal_j 的正性，以及内层 determinant/inertia 障碍。首端点强制阶数沿用既有非退化 crossing 输入。

旧材料中的 m<=10 Möbius/Bernstein 残余系数全正是固定有限维的精确证据，不是全 m 定理。按既有精确归一化，系数全正是导出残余多项式正性及 cofactor 非消失的更强充分条件；它不是非消失的必要条件。真正的逻辑等价是上节的 tau 非消失 iff det S_m 非消失，以及精确变量代换对应的点值关系，不能升级成“系数全正 iff 非消失”。

尚未解决的最小问题仍是原定义下

    det S_m(t)!=0，所有 m>=2、0<t<=1。

内层不定不意味着外层交替和奇异；同样，有限维观察到外层惯性稳定也不能证明全程稳定。“惯性连续”仅在已经排除零特征值的区间上适用，不能循环用来排除待证零点。

原 Taskbook 的 Kill/return 条款明确允许“声明的 positivity mechanism 失败、母定理保持开放”。本 RR 的负边界与该分支相符；历史 DR 也只接受到这一范围。不存在从本次静态数学阅读中得出的、要求重做旧有限 checker 或改写已接受核心证明的实质缺口。现有 outer covariance 后继任务已经准确承接剩余问题；本稿不另设任务。

## 6. 供 Root 最终审阅的引用

本稿依据同目录 `STATIC_MATHEMATICAL_SCOPE_MEMO.md` 中的完整路径引用，以及 `STATIC_MATHEMATICAL_SCOPE_READ_PINS.json` 的逐字节 pin。关键绑定如下：

* 返回 `research_returns/PERFECT_PRIME_AP_BINOMIAL_CAUCHY_LAYER_COFACTOR_POSITIVITY_RETURN_20260901.md`：SHA256 `8d189093d0381743c734698e0dd47b4977d799ade23f268047f067f74eb504ee`，Git blob `340a17c17156e633f0c107023507ceb5498a3763`；重点 §§2–6、8。
* 原 Taskbook `research_tasks/PERFECT_PRIME_AP_BINOMIAL_CAUCHY_LAYER_COFACTOR_POSITIVITY_20260831.md`：Git blob `9b11446b5d2bc9bcca186c13bad361064990734e`；Hard target / Success, kill, and return criteria。
* RR-A4EBF925BE07691C8C16：SHA256 `dd0c8f552c510d930b1ccf798db8582813fcea3ed19c81f3a4ca69a9ac7aa58b`。
* 历史 DR 文本 `driver_reviews/PERFECT_PRIME_AP_OUTER_CONDITIONAL_COVARIANCE_DRIVER_REVIEW_20260901.md`：SHA256 `f4ea06492cf4c31dfc1f3b12dd07361d6e19ead2abe328cbbcc0a98d5e4775f2`；其 DR-9986FE430DB065EA8EF2 记录绑定同一 RR SHA。

所有 native/current-flow 判断和最终签署均留给 Root 自己的真实上下文。本稿没有把旧 DR 的历史 ACCEPTED 字段转换成本次新的 native disposition。


<!-- ENTERPRISE_MATH_DRIVER_TASK_COMPLETION_ASSESSMENT_V1
{
  "schema": "ENTERPRISE_MATH_DRIVER_TASK_COMPLETION_ASSESSMENT_V1",
  "driver_id": "EM-DVR-FBF223",
  "task_id": "RS-PERFECT-PRIME-AP-BINOMIAL-CAUCHY-LAYER-COFACTOR-POSITIVITY",
  "publication_id": "TP2-5A3E91C7D2B40F681AC3",
  "result_id": "RR-A4EBF925BE07691C8C16",
  "result_record_sha256": "sha256:dd0c8f552c510d930b1ccf798db8582813fcea3ed19c81f3a4ca69a9ac7aa58b",
  "original_hard_target_disposition": "SATISFIED_BY_DECLARED_MECHANISM_NEGATIVE_BOUNDARY: the exact full AP cofactor is reduced to the outer determinant; every inner signed covariance is indefinite for all m>=3 and 0<t<=1. This satisfies the explicit Taskbook terminal negative-return alternative for the declared inner-definiteness mechanism, not the parent all-m cofactor-nonvanishing theorem.",
  "disposition": "SATISFIED",
  "terminal_scope": "TASK",
  "assessment": "The actual original Taskbook permits an exact declared-positivity-mechanism obstruction with the parent theorem OPEN. Independent algebraic review reconstructs the complete double-binomial residue (including the degree-2n remainder cancellation), square completion, the correct V_x-only cofactor factor and full inner determinant/inertia. The outer determinant remains unresolved; finite m<=10 coefficient positivity is regression and only a sufficient route. This decision requests Task-only acceptance of that documented negative alternative, without treating inner indefiniteness as a cofactor counterexample or granting parent, Foundation, Working Truth or L4 promotion."
}
-->
