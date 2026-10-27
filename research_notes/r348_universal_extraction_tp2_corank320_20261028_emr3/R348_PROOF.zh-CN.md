# R348｜有符号 BRC 全指标有理抽取证明及第320条 Newton 内区 TP₂ 正性带

日期：2026-10-28。状态：**AUTHOR_SIDE_PROOF / EXACT_COMPUTATION / DRIVER_UNREVIEWED / NOT_ADMITTED**。读取时固定全局快照 \`awdawmip/chatgpt-global-knowledge@b074f7c2e17dce72232272df935e71823a0dff15\`、项目控制基线 \`awdawmip/enterprise-math@b2ae357431fef548a065950ac2362310459bf4c7\`；历史作者来源 R330 \`7c73f56263c3f0515aa28e55ced2d4c703b8e086\`、R346 \`37516cc5bb8d72098ce25f2d64881ec5da4279cd\`、R347 \`e66e12f57be134a2b0ec3350c88499a26433bad5\`。

## 一、原始数学对象与观察范围

研究完整十二项**保留负号**的有序六边 K/J 辅助 BRC 递推：\(\ B_0(t)=1+t,\quad B_s(t)=J_s(t)+\sum_{i=1}^{\min(12,s)}K_i(t)B_{s-i}(t)\)；\(K_i,J_s\) 采用 R330/R347 不变的原始整数系数定义。不把负支路绝对值化，不以正质量代替带符号组合结构。定义

\[
D_{q,k}=\sum_{u=0}^{k}(-1)^{k-u}\binom ku\,2^{q-u}[t^q]B_{q+u}(t),\quad 0\le k\le q,
\]
\[
M_{q,k}=D_{q,k}D_{q+1,k+1}-D_{q,k+1}D_{q+1,k}.
\]

这里 \(q,k,r,u\) 是**辅助组合索引**，不是 P000 原生空间维数、时间或 Cell 序列。本轮没有给出从此组合观察量到六维 X6 完整状态、联合路径与动力学的无损映射；因此不作原生心跳世界物理推断。P000 与 ACTIVE 世界观均保持不变。

## 二、定理 A：此前 R330 载重前提的全指标作者侧代数证明

**精确命题：**对每个整数 \(r,u\ge0\)，存在有理多项式 \(H_r(u)\in\mathbb Q[u]\)，次数至多 \(r\)，使

\[
\boxed{D_{r+u,u}=5^uH_r(u).}
\]

证明不以任何 r 的有限枚举取代全指标论证。

**步骤 A1｜有符号原始母函数及分次次数界。** 置 \(K(x,t)=\sum_{i=1}^{12}K_i(t)x^i,\ A(x,t)=1+t+\sum_{s=1}^{10}J_s(t)x^s,\ U(x,t)=A(x,t)/(1-K(x,t))=\sum_{s\ge0}B_s(t)x^s\)。记 \(K^{(a)}(x)=[t^a]K,\ A^{(a)}(x)=[t^a]A\)。完整 K/J 定义中每个 \(K_i\) 为 \(t^{i-1}(1+t)^j\) 的有限带符号组合，且 \(J_s\) 带 \(t^s\) 因子，所以对所有 \(a\ge0\) 有

\[
\deg_x K^{(a)}\le a+1,\qquad \deg_x A^{(a)}\le a.
\]

原始 K/J 给出 \([t^0]K=2x\)、\([t^1]K=3x-x^2\)，尤其 \(K^{(1)}(1/2)=5/4\)。

**步骤 A2｜形式换元的全指标有限 y 多项式。** 令 \(y=1-2x,\ t=yz\) 并定义

\[
\mathcal P(y,z)=yU((1-y)/2,yz)=\frac{\mathcal N(y,z)}{\mathcal E(y,z)},\quad
\mathcal N=A((1-y)/2,yz),\quad
\mathcal E=\frac{1-K((1-y)/2,yz)}y .
\]

由于 \(1-K((1-y)/2,0)=y\)，上式分母消去 y 是合法的**形式多项式**运算。展开得到

\[
\mathcal E=1-\sum_{a\ge1}y^{a-1}z^aK^{(a)}((1-y)/2),\quad
\mathcal N=\sum_{a\ge0}y^az^aA^{(a)}((1-y)/2).
\]

于是 \( [z^a]\mathcal E,\ [z^a]\mathcal N \) 都是 y 次数至多 \(2a\) 的多项式，而且 \([z^0]\mathcal E=1\)。在 z 进制形式幂级数中用几何级数展开 \(\mathcal E^{-1}\)，每个固定 z^q 的系数只涉及有限次乘积，因而

\[
\boxed{\deg_y [z^q]\mathcal P(y,z)\le2q,\quad \forall q\ge0.}\tag{A1}
\]

这一步是对任意 q 的代数次数证明，不是假设解析收敛。

**步骤 A3｜所有 j 的分母极点与分子次数归纳。** 写 \(\mathcal N=\sum N_j(z)y^j,\ \mathcal E=\sum E_j(z)y^j\)。从上面 z^a 项的最小 y 次数知 \(\deg_zN_j\le j,\ \deg_zE_j\le j+1\)，而且 \(N_0=1,\ E_0=1-\tfrac54z\)。设 \(\mathcal P=\sum G_j(z)y^j\)，令

\[
G_r(z)=\frac{g_r(z)}{(1-\tfrac54z)^{r+1}},\quad g_0=1.
\]

由 \(\mathcal E\mathcal P=\mathcal N\) 的 y 系数恒等式，对每个 r≥1 得到

\[
\boxed{g_r=N_r(1-\tfrac54z)^r-\sum_{j=1}^r E_jg_{r-j}(1-\tfrac54z)^{j-1}.}\tag{A2}
\]

若 \(\deg g_{r-j}\le2(r-j)\)，第 j 求和项次数不超过
\((j+1)+2(r-j)+(j-1)=2r\)，首项 \(N_r(1-\tfrac54z)^r\) 也不超过 \(2r\)。由 \(g_0=1\) 归纳得

\[
\boxed{\deg_z g_r\le2r\quad\forall r\ge0.}\tag{A3}
\]

此处补足此前只有限度检查过的 R330 全指标 g 次数界。

**步骤 A4｜只留 j≤r 的系数抽取，无遗漏高阶 y 项。** 直接按前向差分公式，

\[
D_{q,k}=2^{q-k}[x^{q+k}t^q](1-2x)^kU(x,t).
\]

设 \(w=2x,\ k=q-r,\ t=(1-w)z\)，换元给出

\[
D_{q,q-r}=4^q[w^{2q-r}z^q](1-w)^{-r-1}\mathcal P(1-w,z).
\]

(A1) 确保 \([z^q]\mathcal P\) 的 y 次数≤2q。若 j>r，因 \(j\le2q\)，对应 \((1-w)^{j-r-1}\) 是次数≤\(2q-r-1\) 的普通多项式，不能贡献 \([w^{2q-r}]\)。余下 j≤r 项的二项式系数为 \(\binom{2q-j}{r-j}\)。所以对所有 \(q\ge r\ge0\)

\[
\boxed{D_{q,q-r}=4^q\sum_{j=0}^r [z^q]G_j(z)\binom{2q-j}{r-j}.}\tag{A4}
\]

**步骤 A5｜显示 H_r 的有限公式、处理 q<m 边界。** 由 (A3) 写 \(g_j(z)=\sum_{m=0}^{2j}g_{j,m}z^m\)。其分母展开的 \([z^q]\) 为

\[
[z^q]G_j(z)=\sum_{m=0}^{2j}g_{j,m}(\tfrac54)^{q-m}\binom{q-m+j}{j}.
\]

当 q<m 时，\(q\ge r\ge j\) 且 \(m\le2j\) 意味着 \(0\le q-m+j<j\)，故右侧通常整数二项式恰为0，和本应消失的负次系数一致；没有使用错误的负上标组合数外推。令 \(q=r+u\)，分离 \(5^u\)，得到

\[
\boxed{H_r(u)=\sum_{j=0}^r\sum_{m=0}^{2j}g_{j,m}5^{r-m}4^m
\binom{r+u-m+j}{j}\binom{2(r+u)-j}{r-j}.}\tag{A5}
\]

每项对 u 的次数最多 \(j+(r-j)=r\)，所以 \(H_r\in\mathbb Q[u]\)、\(\deg H_r\le r\)，定理 A 得证。此证明是**作者侧可独立复核的数学推导**，不是形式化证明器或 Driver 接纳记录。

## 三、R348 新的 10 条无界 TP₂ 差分带

令 \(L_r(v)=5^rH_r(v)\) 及

\[
Q_r(v)=L_r(v+1)L_r(v+2)-L_{r-1}(v+2)L_{r+1}(v+1).
\]

从定理 A 的四个 D 因子可直接推得

\[
M_{r+k,k}=5^{2k+1-2r}Q_r(k-1),\quad r,k\ge1.
\]

\(\deg Q_r\le2r\)，所以对所有 v≥0 有完整 Newton 展开

\[
Q_r(v)=\sum_{i=0}^{2r}\Delta^iQ_r(0)\binom vi.
\]

从**原始完整十二项带符号** K/J 递推重新计算 \(B_0,\ldots,B_{965}\) 并保留 t 次数≤643，重建 \(H_{300},\ldots,H_{321}\)，核验各行第 r+1 次差分为0、最高差分为 \(6^r\)。对新 r=311..320 的完整 \(2r+1\) 项 Newton 差分，合计

\[
\sum_{r=311}^{320}(2r+1)=\boxed{6320}
\]

项**全部严格正整数**、0项非正；十项最高差分均恰为 \(30^{2r}\mathrm{Cat}_r\)；40个 r,k=1..4 的原始 D 子式与 Q 的分离恒等式精确一致；前沿 r301 的603项与 r302..310 的5517项旧证书 SHA256 完全一致。无浮点判号。

新6320项规范逐行 \`r,i,decimal_integer\n\` 的原始数据 SHA256：
\`aa2bb5fbef46dc15aa766df196077f95fd5d4e4165d78fca7cab42db26b521d0\`。完整程序、全部数字、机器证据、本证明全文存于可复现 R348 交付 ZIP。

结合前沿 R345–R347 已留存的 r≤310 作者侧完整正系数证书以及本轮的**全指标次数定理 A**，可得作者侧数学结论：

\[
\boxed{M_{q,k}>0,\quad k\ge1,\quad1\le q-k\le320.}
\]

结合 R341 的相邻比值望远镜与已证相应 D 正性，内区合法非相邻二阶子式 \(D_{q,k}D_{p,\ell}-D_{q,\ell}D_{p,k}\) 在 \(1\le k<\ell\le q<p,\ p-k\le321\) 内严格为正。这里“无界”仅指**固定 q-k 后 k 任意增大**，不证明双指标全域 TP₂，更不证明全局 TP₃ 或边界 k=0 的二阶非负；R339 和 R342 的负子式仍有效。

## 四、已执行的复算与依赖审查

本轮在独立容器中实际运行 \`python R348_verify.py\`，严格整数/Fraction 全证书 PASS；并运行 \`python R348_kernel_audit.py\`（SymPy 精确有理数），对 r=0..5、u=0..8 共54个原始 D 值比对显示公式一致，同时核验 \(K^{(0)},K^{(1)},E_0,g_0,\ldots,g_5\) 的有限数值/次数。有限抽查是 **(A1)–(A5) 形式证明的校验**，不是无界结论的逻辑替代。

原始执行源码 SHA256：
- \`R348_verify.py\`: \`599b0ce7cc5a79ffede4bac2f21b96a9a08b43c527ac529a2067903f80ec7738\`;
- \`R348_kernel_audit.py\`: \`1442835a74a8b1872156e550ee6c0f97733e42221e2349527cd93c5bb137c1b9\`;
- \`R348_EVIDENCE.json\`: \`93b3ff0db0fdbfea042b94207384689fe9a8a03eef0035bbb449103fb8ce9bb8\`;
- \`R348_KERNEL_EVIDENCE.json\`: \`466bd1abfe5ed9991c2130e38aad6309686a52f7ec86f8789a1d6bfb6ee21132\`.

GitHub 作者身份 awdawmip，项目 admin/push；原生服务 source_sync 存在 CODE_REVIEW_REQUIRED 且研究权限字段 \`research_authority_granted=false\`，控制配额为5/5。未权威核实当前 active owner、未取得本任务原生 CLAIM、Result、Driver review、数学准入。GitHub Draft PR 属于可移植作者侧科学材料保存，不绕过原生控制授权。

**最小下一问题：** 由独立审阅者逐项核验 (A1)–(A5) 尤其 y-次数、q<m 边界及 K/J 符号来源；寻找 r,k 同时增长的正锥/真实反例；或计算 r=321 的643个完整 Newton 系数。P000、ACTIVE 世界观及旧 Result/Review 不变。
