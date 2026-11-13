# R349｜BRC Newton 内区 TP₂：330 条无界差分带与 Newton 乘积核的严格反例

2026-10-28，作者侧研究成果。GLOBAL_KNOWLEDGE_V1 固定经当轮 GitHub 验证的 main@5b03e7f250babaf694305861ca991d84fe4cdffc；项目规范基线 main@c9a28fe95d621a2d1b9f22bb93f766a3eb739098；读取 P000 原始 V4、ACTIVE 世界观及 PORTABLE_RESEARCH_PROTOCOL。原始 P000 Git Blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc。来源：R346 有符号 K/J 源码（37516cc5bb8d72098ce25f2d64881ec5da4279cd）、R347（614bcfe65b8e0829ab46d0f9ef2c79844a602bb7）、**另一作者侧 R348** 的全指标抽取证明和 r≤320 精确证书（Draft PR #1599，5347e506bd145028d7338e9f7993dcd2a2fed97c）。发现 R348 已完成后，本轮仅计新增 r=321..330，旧 r=303 与 r=320 仅做回归验证。

## 一、数学对象与本轮结论

对象为有序六边 BRC **辅助组合模型**的完整12项带符号递推：
\[
B_0(t)=1+t,\quad B_s(t)=J_s(t)+\sum_{i=1}^{\min(12,s)}K_i(t)B_{s-i}(t),
\]
\[
D_{q,k}=\sum_{w=0}^{k}(-1)^{k-w}\binom{k}{w}2^{q-w}[t^q]B_{q+w}(t),\qquad
M_{q,k}=D_{q,k}D_{q+1,k+1}-D_{q,k+1}D_{q+1,k}.
\]
K、J 的完整原始整数定义在同一 PR 分支的 `research_notes/r346_unbounded_interior_tp2_corank301_20261028_emr3/R346_verify.py`，本轮源码逐项复用，保留负项，未将正质量误代替有符号支路。全部 q,k,r,u 是**组合索引**；没有建立与心跳世界原生 X6 Cell、联合支路或动力学的对应，不作原生物理推断。P000和ACTIVE世界观不改。

R348 的作者侧（待独立数学审查）**全指标有理抽取定理**为：对每个 r,u≥0，
\[
D_{r+u,u}=5^uH_r(u),\quad H_r\in\mathbf Q[u],\quad\deg H_r\le r.
\]
写 \(L_r(v)=5^rH_r(v)\)，
\[
Q_r(v)=L_r(v+1)L_r(v+2)-L_{r-1}(v+2)L_{r+1}(v+1).
\]
由四个 D 因子直接得到 \(M_{r+k,k}=5^{2k+1-2r}Q_r(k-1)\)、\(\deg Q_r\le2r\)。

**新精确证书：**从上述原始12项带符号 K/J 重新计算 \(B_0,\ldots,B_{995}\)，保留次数 \(t^0,\ldots,t^{663}\)；构造 \(H_{319},\ldots,H_{331}\) 并对每行使用 r+2 个直接 D 值核验第 r+1 次有限差分为0，最高 r 次有限差分为 \(6^r\)，其余有效 H Newton 差分也严格为正，\(5^rH_r\) 的系数均是整数。每行额外节点为有限计算自检，不代替 R348 的次数界证明。以前述 R348 r=320 规范641项证书 SHA256
`ef944e5a2608a1566e8b508699dbf11b0428fd85e230a428d4cbb11071aa98e6`
作精确回归，实际字节一致。

对 r=321,…,330 的 Q_r，计算全部 \(c_{r,j}=\Delta^jQ_r(0)\)，\(0\le j\le2r\)。这10条新带合计
\[
\sum_{r=321}^{330}(2r+1)=6520
\]
项**全部严格为正**，负值0、零值0。完整逐条规范文本 `r,j,十进制整数\n` 的 SHA256 为：
`88b663d75bef5c3ca8af055cd7ec1ee22799e46d55fe6e3e8a995605a89c22f5`。
验证 r=320..330 全11条最高差分 \(c_{r,2r}=30^{2r}\operatorname{Cat}_r\)；对 r=321..330、k=1,2,3,4，直接原始 B_s 重算40个 M 值，全部严格正且与 \(\frac{5^{2k+1}}{5^{2r}}Q_r(k-1)\) 精确相等。所有判号使用整数及 Fraction，无浮点推断。完整可复现程序、逐带摘要见 R349_verify.py、R349_EVIDENCE.json；8.0MB十进制原始数据在本轮附件 ZIP 中保留，脚本亦可再生全部字节。

由于 Newton 公式在整数 \(v\ge0\) 下满足
\[
Q_r(v)=\sum_{j=0}^{2r}c_{r,j}\binom vj>0
\]
（所有系数为正且 \(c_{r,0}>0\)），故**在已披露 R348 抽取和次数界作者侧证明正确的前提下**，每条新带 \(M_{r+k,k}>0\) 对全部 k≥1 成立。结合以前 r≤320 的来源证书，得到作者侧条件结论：
\[
\boxed{M_{q,k}>0\quad \forall k\ge1,\;1\le q-k\le330.}
\]
与 R341 正比值传播结合，则在合法内区 \(1\le k<\ell\le q<p,\ p-k\le331\) 上二阶子式也严格为正（同样继承上游 D 元素正性证明的依赖）。这是**330条固定余阶但 k 无上界**的区域；不是整个二维 TP₂。R339 的左边界 k=0 负二阶子式和 R342 的内部 TP₃ 负三阶子式仍有效。

## 二、通用 Newton 乘积核定理（新证明）

**定理。** 对有限 Newton 级数 \(F(v)=\sum_i f_i\binom vi\)、\(G(v)=\sum_jg_j\binom vj\)，任意 \(n\ge0\) 有
\[
\boxed{\Delta^n(FG)(0)
=\sum_{\substack{i,j\ge0\\h=i+j-n\\0\le h\le\min(i,j)}}
\frac{n!}{h!(i-h)!(j-h)!}f_i g_j .}
\tag{1}
\]
**证明。** 选一个 v 元集合；\(\binom vi\binom vj\) 计数一对分别有 i、j 个元素的子集。若两集交的大小 h，则并集 n=i+j−h。先以 \(\binom vn\) 选并集，再将其分为交集（h个）、仅第一集（i−h个）、仅第二集（j−h个），划分数恰为 \(n!/[h!(i-h)!(j-h)!]\)。所有情况互斥且穷尽，故乘积的 \(\binom vn\) 展开式系数即(1)；整数值上成立推出多项式恒等式，得证。

令 \(a_{r,i}=\Delta^iL_r(0)\)，界外索引定义为0。Vandermonde 恒等式给出移位系数
\[
A_{r,i}^{(1)}=a_{r,i}+a_{r,i+1},\qquad
A_{r,i}^{(2)}=a_{r,i}+2a_{r,i+1}+a_{r,i+2}.
\]
定义配对差：
\[
T_{r,i,j}=A_{r,i}^{(1)}A_{r,j}^{(2)}
-A_{r-1,i}^{(2)}A_{r+1,j}^{(1)}.
\]
由(1)，\(\Delta^nQ_r(0)\) 等于上述**非负整数核**对可能有正负号的 \(T_{r,i,j}\) 的精确加权和。这是可复用的新分解，但**不能假定每个 T 均非负**。

## 三、逐项配对正性策略的严格反例

从完整带符号12项递推，精确获得
\(a_{0,*}=(1)\)，\(a_{1,*}=(30,30)\)，\(a_{2,*}=(800,1980,900)\)。
因此
\[
T_{1,0,1}=(30+30)\cdot30-1\cdot(1980+900)=\boxed{-1080}.
\]
与之同时，
\[
Q_1(v)=450v^2+2070v+2620,\quad
(\Delta^0Q_1(0),\Delta^1Q_1(0),\Delta^2Q_1(0))=(2620,2520,900)>0.
\]
这是全指标逐项 \(T\ge0\) 加强命题的**无条件严格反例**，却与 Q 本身 Newton 差分全正相容；证明需保持正负配对项的精确组合，不可删除负项。

附带有限**观察**：精确检查 r=1..64 的 98,016 项 T，所有值与如下有向符号图相符：当 \(0\le j\le i\le r\) 为正；当 \(0\le i<r\)、\(i<j\le r+1\) 为负；其他位置为0。无例外但尚无无界证明。用 r=1..10 的全部120个 Q Newton 系数逐项验证(1)和 T 核卷积恰好等于直接Q差分。实际源码 R349_shift_audit.py、证据 R349_SHIFT_EVIDENCE.json；检查采用精确整数和 Fraction。

## 四、状态、复现及后继

本轮原生 `em_control_tasks` 返回 `CONTROL_QUOTA`；`em_session_start` 返回 `STATIC_READONLY_SCOPE_DENIED` 且 `operation_sent=false`。本地作者身份不等于服务签发的 Researcher-ID，GitHub 活动登记也不赋予原生 CLAIM、独立审查或数学接纳。任务活跃 Owner 未能权威确认；仍为 AUTHOR_SIDE / EXACT_COMPUTATION / UNREVIEWED / NOT_ADMITTED。

完整复现：在含 R346_verify.py 的同一 PR #1592 源分支运行 `python research_notes/r349_unbounded_interior_tp2_corank330_20261028_emr3/R349_verify.py` 和 `python research_notes/r349_unbounded_interior_tp2_corank330_20261028_emr3/R349_shift_audit.py`。源码不含外部依赖，仅Python标准库。原始系数8.0MB未写入仓库，脚本能完整再生；完整附件另保留。独立第三方应审查 R348 中 A1–A5 所证明的形式幂级数换元、y 次数截断及 q<m 边界后再认定无界延伸。

**后继：**（1）检验 r=331 的 663 个 Q Newton 差分，核对旧 Q330 摘要；（2）证明/否定全部 r 时有向 T 符号图，并寻求**核内带符号配对抵消**机制证明 \(\Delta^nQ_r(0)>0\) 的无界范围；（3）寻找真正的二维 r,k 同步增长 TP₂ 证明或精确负子式。活动 ID：`RA-EMR3-20261028-R348-CORANK303-0648`（实际注册时原计划 r303；发现已有 r≤320 而调整本次研究问题，保留同一真实本地会话/活动登记）。
