# D25/LIFT — 不等来源路径质量下的多来源 BRC 整数缺损与锐有限时间传递定理

- 日期：2026-10-30。性质：`AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE`。
- 母问题：给定六轴原生来源、观察端口、操作、时间语义及 BRC 整数路径，研究何时可安全压缩，以及未能精确下降时的有界信息缺损。本文是**辅助有限正整数路径核定理**，不是原生 X6/H0/B0 实验。
- 直接承接既有作者侧定理 `D25_BRC_CONDITIONAL_PRIVATE_NOISE_TWO_COPY_GRAM_RIGIDITY_AND_COUPLING_BOUNDARY_20261030.md` 与本轮首单元 `D25_BRC_INTEGER_GRAM_RESIDUAL_MULTICOPY_FINITE_HORIZON_STABILITY_20261030.md`。前者证明零 Gram 缺损的双来源刚性；后者在所有来源总路径数固定时给出可归一化的 TV 界。**本单元取消其同质量前提，在原始不归一化整数 BRC 层得到新的多来源及全部时间观察历史界**。标准张量望远镜/正算子扰动公式不宣称为新发现。
- P000 与 ACTIVE 心跳世界不改动：六维原生空间、独立时间、三维切片、路径和来源残差、正整数重数。数学科学 Source pin 保留 `c47e13e4aba0e006366f989d6334d443f6333ae3`。内文 `X,Y,V` 是声明明确的有限辅助载体，而非新空间轴或自定义世界公理。

## 1. 带标签来源、共享操作、观察端口与不等总质量

令 `X` 和 `Y` 为非空有限集合，`C:X→Y` 为满射。每个观察纤维 `C⁻¹(a)` 选择代表 `r_a`。共同分支标签组成有限集 `B`，其权重 `w_b∈ℤ_{>0}`。每个标签有原始非负整数**单来源私有路径重数核**

\[
V_b(x,z)\in\mathbb Z_{\ge0},\qquad
v_b(x,a)=\sum_{z:C(z)=a}V_b(x,z),\qquad
s_b(x)=\sum_{a\in Y}v_b(x,a).
\]

本单元**允许 `s_b(x)` 依赖原始来源 `x`，甚至为零**。单步操作的精确定义为：对一组 `m≥1` 条可复制的带标签来源，选择一个共有分支 `b`（权重 `w_b`），给定 `b` 后各来源的私有路径条件独立，所以对应原始路径与观察行分别为

\[
L_m(\mathbf x,\mathbf z)=\sum_b w_b\prod_{i=1}^mV_b(x_i,z_i),\quad
K_m(\mathbf x,\mathbf a)=\sum_b w_b\prod_{i=1}^m v_b(x_i,a_i).
\]

这是**未归一化、保留每条来源原始标签和整数路径数**的 BRC 类型。观察行总质量

\[
S_m(\mathbf x)=\sum_{\mathbf a\in Y^m}K_m(\mathbf x,\mathbf a)
=\sum_b w_b\prod_{i=1}^ms_b(x_i)
\]

一般随来源变化。时间由操作序列的整数步长另行标记，**不能借归一化概率表述消除原始质量差**。定义观察商代表元组 `\mathbf r(\mathbf x)=(r_{C(x_1)},\ldots,r_{C(x_m)})`。

固定上一单元的有来源、逐标签整数平方缺损：

\[
\boxed{D(x)=\sum_b w_b\sum_{a\in Y}[v_b(x,a)-v_b(r_{C(x)},a)]^2.}\tag{1}
\]

## 2. 定理 A：来源质量可变时的精确多来源整数界

给定任意 `\mathbf x=(x_1,\ldots,x_m)`，记 `r_i=r_{C(x_i)}`。对每个 `i,b` 定义纯整数系数

\[
 c_{b,i}(\mathbf x)=\prod_{j<i}s_b(r_j)\prod_{j>i}s_b(x_j),\qquad
 \Lambda_i(\mathbf x)=|Y|\,D(x_i)\sum_b w_b c_{b,i}(\mathbf x)^2,
\]

空积定义为1。于是有**非负整数根号取整**的统一不等式：

\[
\boxed{\left\|K_m(\mathbf x,\cdot)-K_m(\mathbf r(\mathbf x),\cdot)\right\|_1
\ \le\ \sum_{i=1}^m \operatorname{isqrt}(\Lambda_i(\mathbf x)).}\tag{2}
\]

同时，原始整数总路径数的缺损自动满足

\[
\boxed{|S_m(\mathbf x)-S_m(\mathbf r(\mathbf x))|
\le\|K_m(\mathbf x,\cdot)-K_m(\mathbf r(\mathbf x),\cdot)\|_1.}\tag{3}
\]

**证明。** 固定标签 `b`，按顺序替换向量 `v_b(x_i,·)` 为代表向量 `v_b(r_i,·)`，在整数张量积中严格望远镜展开：

\[
\bigotimes_i v_b(x_i)-\bigotimes_i v_b(r_i)
=\sum_{i=1}^m
\Bigl(\bigotimes_{j<i}v_b(r_j)\Bigr)
\otimes\bigl[v_b(x_i)-v_b(r_i)\bigr]
\otimes\Bigl(\bigotimes_{j>i}v_b(x_j)\Bigr).
\]

所有未替换因子均为非负整数向量，故其 `\ell^1` 范数的乘积**恰好**为 `c_{b,i}`（不需要假设质量相等）。于是按标签与来源序号三角不等式，左侧至多

\[
\sum_{i=1}^m\sum_b w_b c_{b,i}\|v_b(x_i)-v_b(r_i)\|_1.
\]

对每个 `i`，先在有限 `Y` 上使用 `\|u\|_1\le\sqrt{|Y|}\|u\|_2`，再对标签采用正整数权 Cauchy–Schwarz，得到

\[
\sum_b w_b c_{b,i}\|v_b(x_i)-v_b(r_i)\|_1
\le\sqrt{|Y|\sum_b w_b c_{b,i}^2}
\sqrt{\sum_b w_b\sum_a[v_b(x_i,a)-v_b(r_i,a)]^2}
=\sqrt{\Lambda_i}.
\]

每个分项被控制的原始数值是整数，所以不大于 `isqrt(\Lambda_i)`，逐项相加即 (2)。对所有观察目标求和后使用 `|Σu|≤Σ|u|` 得 (3)。所有端点、赋值和重数均为严格整数。证毕。

**特殊情况与缺损类型。** 若 `D(x)=0` 对所有原始来源成立，则每条标签的观察向量在纤维上严格常数，包含总路径质量严格下降，恢复旧零缺损定理。若 `D>0`，(2) 量化保留而不否定来源结构残差。若 `s_b(x)=s_b` 恰好与来源无关，`c_{b,i}=s_b^{m-1}`，(2) 精确退化为本轮首单元的固定质量定理，因此不重复其证明。注意质量变化是非归一化整数行缺陷，不是普通概率 TV。

## 3. 定理 B：全部时间有序观察字的非归一化整数误差

时间推进定义为：在每个离散操作时刻重新使用同一个原始 `L_m` 正整数路径核；真实隐藏来源可保留其全部 `m` 个坐标。以 `\overline K_m(\mathbf y,\mathbf a)=K_m(\mathbf r_{\mathbf y},\mathbf a)` 定义**仅观察商上的代理整数路径核**。原始链从任一确定初始 `\mathbf x_0` 开始；代理从 `\mathbf y_0=C^m(\mathbf x_0)` 开始。每一步同时记录**时间有序、m 源联合**观察 `\mathbf y_t`；研究的对象是完整历史字，而不是终点或单时刻布尔支持。

定义如下有限非负整数（只读原始核和本次观察商）

\[
\delta_m:=\max_{\mathbf x\in X^m}
\|K_m(\mathbf x,\cdot)-\overline K_m(C^m\mathbf x,\cdot)\|_1,
\quad R_m:=\max_{\mathbf x\in X^m}S_m(\mathbf x),
\quad\overline R_m:=\max_{\mathbf y\in Y^m}S_m(\mathbf r_{\mathbf y})\le R_m.
\]

对全部观察历史长度 `t`，令 `\mu_t` 和 `\overline\mu_t` 分别是真实与代理的**原始路径整数重数**；初始同观察的历史长度0视为一条空字。则无须要求正质量总数固定，有

\[
\boxed{
E_t:=\|\mu_t-\overline\mu_t\|_1
\le\delta_m\sum_{j=0}^{t-1}R_m^{t-1-j}\overline R_m^j
\le t\delta_m R_m^{t-1}
}\quad(t\ge1).\tag{4}
\]

当 `R_m=0` 时所有一步后计数为零，对 `t≥1` 直接有 `E_t=0`；几何项中的零幂按正常空积约定，不需把零分母嵌入公式。

**证明。** 对任一 `t`，让 `\rho_t(w,\mathbf x)` 记录时间有序观察字 `w` 及实际隐藏终态 `\mathbf x` 的非负整数真实路径重数。其观察边缘 `\mu_t(w)=\sum_{\mathbf x}\rho_t(w,\mathbf x)`，真实全部路径数至多 `R_m^t`（由每个原始状态的整数行总量不超过 `R_m` 逐步归纳）。下一步真实观察历史计数为

\[
\mu_{t+1}(w\mathbf a)=\sum_{\mathbf x}\rho_t(w,\mathbf x)K_m(\mathbf x,\mathbf a).
\]

添加中间项 `\sum_{\mathbf x}\rho_t(w,\mathbf x)\overline K_m(C^m\mathbf x,\mathbf a)`。它与真实新增历史的 `\ell^1` 差至多 `\delta_m\sum_{w,\mathbf x}\rho_t(w,\mathbf x)\le\delta_m R_m^t`。在每条真实历史字 `w` 上，当前观察 `C^m\mathbf x` **必然等于其最后一个观察字母**（`t=0` 时等于指定初始观察）；所以该中间项恰是以 `\overline K_m` 从 `\mu_t` 延伸一步。把它同真正的代理历史 `\overline\mu_{t+1}` 比较，非负整数行的诱导 `\ell^1` 算子范数至多 `\overline R_m`，从而

\[
E_{t+1}\le\delta_m R_m^t+\overline R_m E_t,\qquad E_0=0.
\]

归纳解得 (4)，且因为 `\overline R_m\le R_m`，每个几何项不大于 `R_m^{t-1}`。证明全过程直接作用于原始**非归一化整数来源质量**，没有要求概率构造或引入分母。证毕。

将 (2) 的来源逐点 `isqrt` 证书取 `X^m` 最大值，即给出无需枚举所有目标字的一项合法 `\delta_m` 上界；如果取得实际 `K_m`，仍可用更紧的精确 `\delta_m`。这不是跨尺度统一界：对增大 `m` 或 `t` 必须明示 `R_m,\delta_m` 如何增长。

## 4. 全时长锐性及不能按概率压缩的最小反例

取两个带标签原始来源 `X={r,x}`，**仅一个**观察符号 `Y={0}`、`C(r)=C(x)=0`、单标签 `B={0}`、`w=1`，定义

\[
V(r,r)=1,\qquad V(x,x)=2,
\]

其余转移重数为零（`2` 表示两条不同的原始整数路径）。代表选择 `r_0=r`。则 `v(x,0)=2,v(r,0)=1`，因此 `D(x)=1`，一步 `\ell^1` 源质量缺损为1，(2) 的 `isqrt` 精确取等。`\delta_1=1,R_1=2,\overline R_1=1`。从原始来源 `x` 出发的唯一观察历史字在时间 `t` 上有 `2^t` 条带来源路径；代理只有 `1` 条，所以

\[
\boxed{E_t=2^t-1
=\delta_1\sum_{j=0}^{t-1}2^{t-1-j}1^j,\qquad\forall t\ge1.}\tag{5}
\]

(4) 的精确几何式对**全部时间长度**取等，不是有限次数拟合，也说明不能一般地删除 `R_m` 的乘性增长。另一方面，两者若各自单独归一化，观察分布同为单点质量，所有 `TV=0`；因此**零归一化 TV 完全不能保证 BRC 整数路径重数保真**。这构成前一个固定质量定理的实质范围边界，不是旧证明的重复。

为验证非单点观察的情况，另取 `X={r,x,c}`、`C(r)=C(x)=0,C(c)=1`；令真实 `x` 有两条自环，代表 `r` 分别一条到 `r` 和一条到 `c`，`c` 有三条自环。于是 `\delta=2,R=3,\overline R=3`。作者程序逐一计算 `t=1,…,8` 的完整观察字计数差及上界，均满足 (4)，而真实/代理路径总重数在 `t≥2` 通常不同。这个有限样例并不承担一般证明责任。

## 5. 真实检查范围、可复现证书与科学地位

程序：`d25_brc_nonnormalized_mass_defect_checker_20261030.py`；同名 `_author_check_20261030.json` 是脚本真实运行的标准库整数 JSON 输出。它精确枚举两条共有标签 `(w_0,w_1)=(1,2)`、带来源身份 `X={0,1,2}`、观察 `C(0)=C(1)=0,C(2)=1`、各个 `v_b(x,·)` 取自五个非零整数行 `(0,1),(1,0),(0,2),(1,1),(2,0)` 的所有 `5^6=15,625` 个模型。检查所有来源元组 `m=1,2`：`187,500` 个配置内原始来源元组、`656,250` 次目标观察行求值、`89,530` 个非零整数观察残差、`65,736` 个原始来源总质量不一致情形、`19,750` 次非平凡上界取等；全部为 `PASS`。同时真实逐字枚举非均匀多状态 `t=1,…,8` 和锐单点 `t=1,…,9` 的整数历史重数及界。

**证明强度：** 对任意有限 `X,Y,B` 与任意 `m,t` 的结论来自第2—4节代数证明；计算只交叉核验上述明确有限类，不冒充对全部输入的穷举。数学方法是正整数路径核的张量范数与有限时间正算子扰动应用；需要独立数学审阅和现有 Source Result/Driver 才能申请项目准入。`UNREVIEWED / NOT_ADMITTED`。

## 6. BRC 复用、原生桥缺项与下一动作

BRC 决议 `COMPOSE_APPLIED`：前项 Gram 保留 `b,x,a` 整数赋值与路径；本项保留 `s_b(x)` 这一不能删的**来源质量残差**、隐藏终态、m 来源联合操作、全时序观察字和正整数重数，避免对原始计数静默概率化。当 `D` 和 `\delta` 非零，不把偏差称为噪声或模型失败；用 `(2)–(4)` 预算其未来累计并检验是否可接受。

**原生 X6 仍缺的必要事实**：实际带标签来源和复制规则、每条共有/私有分支的完整 `V_b` 或相关联合核、观察端口、时间更新与环境记忆、是否有限/如何截断、合法来源数和读取尺度。当前 `definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json` 只给出 P000 时空语义，`fixed_heartbeat_program=null`；不能把辅助模型 `V_b` 当成真实原生算子。原生精确或误差归因前还要满足项目 BRC-only 的类型约束。若存在给定标签后的私有跨来源相关，本文所有乘积 `L_m`、`K_m` 的前提不成立；必须先获取真实联合整数核，再另行研究，不得误用本界。

正式 Source writer、CLAIM/OPEN、checkpoint、Result 和独立 Driver 审阅均须经合法当前权限取得。现有 Gateway/Sites 为只读、授权/绑定欠缺；本文仅为中立保存的**作者侧**可移植数学，不能充作 predecessor completed_units 或原生实验。若未来 Source seed 是 `CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS`，必须先完整回读 `input_artifacts`，然后使 `frontier_notes.completed_units=[]`，本文仅作 `staging/do_not_repeat`。

UR V2 四文件打包原件仍须单独获得真实 `94687` 字节且 SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76` 并核对来源；既有 UR 数学不再重做。下一科学最小单元优先为**条件相关私有分支下整数质量缺损如何类型化传递**或真实 X6 观察/动力学核实际可取得时的逐项交换图与反例，而非重新证明当前不等质量界。
