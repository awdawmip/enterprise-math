# R261 — 来源查询的 Laurent–Hankel 最小线性阶数 13；遗忘平移后为 11

**2026-10-24 / AUTHOR_SIDE_EXACT_PROOF / UNREVIEWED.**
**严格边界：** 这是 R260 的有限正权 BRC 形式模型、一个固定非选择性双支路包无限重复的观察结果；不是已认证的原生心跳动力学或已接纳的数学 Result。证明的最小性是在域 K=Q(x) 的**线性实现**类别内，不是正权控制状态最小性，也不涉及逐条保留完整来源路径。

## 1. 冻结输入、来源和观察契约

- GLOBAL_KNOWLEDGE_V1: awdawmip/chatgpt-global-knowledge main@b398f5d6e3d031ba47b558c4c651d7238285ef88；P000 ACTIVE_LOCKED，global P000 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc；读取规范入口、ACTIVE 世界观、BRC/数学研究政策。
- Enterprise Math Source: awdawmip/enterprise-math main@74149f00837573d26541e1a31dff5f30ca090b6d；读取 AGENTS.md、HEARTBEAT_WORLD_NATIVE_X6_TIME、联合关系与观察保真、残差保真、PORTABLE_RESEARCH_PROTOCOL、brc_transport.py 与 brc_control_port.py。
- 前驱：R260 于提交 2f45730d1bf1064b9072ad4e57ade3f0e285d112 的 research_notes/R260_ALL_TERMINAL_FIBERS_EFFECT_AWARE_NO_GO_20261024.md。R260 的 7 模式结果是**逐路径确定性监测**，不能与本次线性 13 维结论混同。
- 原生控制端 em_control_dispatch 得到 CONTROL_QUOTA；em_session_start 得到 STATIC_READONLY_SCOPE_DENIED, operation_sent=false。未取得真实 Owner/CLAIM、原生研究活动登记、Result、Driver 审核，也未执行原生 Enterprise Math Python 导入。此 GitHub 草稿不构成原生接纳。

控制状态 q=0,1,2；每一步原始支路 a=0,1，权重与路径重数各为 1。边 (q',η,b)：

| q | a=0 | a=1 |
|---|---|---|
| 0 | (2,-1,-1) | (2,+1,-1) |
| 1 | (0,-1,-1) | (0,+1,-1) |
| 2 | (1,+1,+1) | (2,+1,-1) |

形式六坐标仿射效果定义为

$$F_{\varepsilon,k}(z_1,\ldots,z_6)=(\varepsilon z_1+k,\varepsilon z_2,z_3,z_4,z_5,z_6),\quad \varepsilon=\pm1,\ k\in\mathbb{Z}.$$

从时间先后的两步复合：

$$(\varepsilon,k)\ {\rm THEN}\ (\eta,b)=(\eta\varepsilon,\eta k+b).$$

这里只声明六个原生空间坐标槽中的**形式作用**与独立整数操作索引 m；未认证其满足 P000 的原生力学、三力闭合、旋转、最终 Cell 编码或 R193 的真实来源契约。查询自动机 r=0 表示未见 00 且上一位不是 0；r=1 表示未见 00 且上一位是 0；r=2 表示已经见过 00。其更新 δ(r,0)=(1,2,2)[r]、δ(r,1)=(0,0,2)[r]，布尔查询为 g(r)=1 当且仅当 r=2。从 (q,r)=(0,0) 可达的模式恰为

$$S=((0,0),(0,2),(1,1),(1,2),(2,0),(2,1),(2,2)).$$

声明观察为每个 m≥0 的完整正整数联合效果直方图 (q,g(r),ε,k)；唯一允许的未来操作为重复**同一个两个支路一起求和的非选择性包**，不允许选择 a 的单支路或恢复每条原始路径。

## 2. 精确保真的 14 通道提升

令 K=Q(x)，x 是 Laurent 观察不定元（**不是第七空间轴**）。定义

$$D_k=\begin{pmatrix}x^k&0\\0&x^{-k}\end{pmatrix},\quad J=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad \rho(\varepsilon,k)=D_kJ^{(1-\varepsilon)/2}.$$

J D_k J = D_{-k}，因此

$$\rho(\eta,b)\rho(\varepsilon,k)=\rho(\eta\varepsilon,\eta k+b).$$

对每一模式 (q,r)，累加所有正权路径效果矩阵 ρ，再取**第一列**：上分量记录 ε=+ 的 x^k Laurent 生成多项式，下分量记录 ε=- 的 x^{-k} Laurent 生成多项式。两组单项式系数逐 k 恰给原始正整数重数，所以该提升对声明观察无损。中间使用线性代数不把正路径变为相消的物理振幅。

令 v=e_{(q,r)=(0,0),上}∈K^14。对原始转移 q,r → q',δ(r,a)，构造 A(x)∈K^{14×14} 的对应 2×2 块 D_bJ^{(1-η)/2}，相同起终点的两条原始边相加。该 14×14 矩阵的**精确且可运行构造**见 R261_symbolic_certificate.py 中 matrices(x)。令 C∈K^{12×14} 把 r=0,1 投影至 g=0，r=2 至 g=1，但仍保留 q 与两个 ε 通道。于是

$$u_m=A(x)^m v,\qquad y_m(x)=CA(x)^mv.$$

此 y 恰编码每个 m 的全部 (q,g,ε,k) 联合直方图。选取标量 s_m(x) 为 y_m 中 (q=0,g=1,ε=+) 的通道。其明确的非矩阵定义为

$$s_m(x)=\sum_{\substack{|w|=m,\ q_m(w)=0\\r_m(w)=2,\ \varepsilon_m(w)=+1}}x^{k_m(w)}.$$

任意实现整个 y 的 d 维线性系统也能输出 s，所以这个单通道的 Hankel 秩是整体最小状态数的**下界**。

## 3. 定理 A：全部 Laurent 效果信息的最小线性阶数恰为 13

**断言。** 在 K=Q(x) 上，标量 Hankel 矩阵 (s_{i+j}(x))_{i,j≥0} 的秩恰为 13；整个联合观察 y_m 在所有 m≥0 上拥有 13 维的线性实现且不可能更小。

**上界：完全符号证书。** 由明确的 14×14 A(x) 进行精确计算：

$$\chi_A(z)=-\frac{z^2}{x^3}(z^2+1)(x^2-xz+1)(x^2-xz^3-xz+1)(x^2z^5-xz^6-2xz^2+x+z^5).$$

该多项式次数为14，令 p13(z)=χ_A(z)/z，为**首项系数 1** 的 13 次多项式。完整的矩阵恒等式是

$$\boxed{p13(A(x))=0_{14\times14}}.$$

提供的符号脚本逐一计算其 196 个分量并在有理函数域中检验等于零；没有浮点误差或有限点插值。对每个 m，将 p13(A) 左乘 A^m 再作用于 v 与 C，得到同一 13 阶线性递推，且 K 中由 v,Av,...,A^{12}v 张成的 Krylov 子空间对 A 不变。该子空间提供至多 13 维的完整输出实现。另一核对得 rank_K A = rank_K A² =12，零特征值半单，不需要 χ_A 中的第二个零根。

**下界：一个不为零的有限行列式。** x=2 时，正整数历史动态规划与独立有理数线性转移计算均得：

$$\boxed{\det(s_{i+j}(2))_{0\le i,j\le12}=\frac{163341851565859597265625}{1099511627776}\ne0.}$$

所有 s_m(x) 在取值前是 Laurent 多项式，所以其 Hankel 行列式在 x=2 非零，必在 K 上非零。无限 Hankel 矩阵秩至少13。任意 d 维线性实现的 Hankel 行列可分解为 (c A^i)(A^j v)，秩不超过 d。故 d≥13，与上界合并为**恰好 13**。证毕。

## 4. 定理 B：遗忘平移导致最小阶数恰为 11

将 x=1，仅保留 (q,g,ε) 而忘记整数 k；这**显式改变了观察语言**，不是对原完整效果的无损压缩。令 A1=A(1)。精确计算证得

$$p11(A1)v=0,$$

其中

$$p11(z)=z(z-2)(z-1)(z^2+1)(z^2-z-1)(z^2+z+1)(z^2+z+2)$$

是 11 次首一多项式。因此全体原输出投影都满足 11 阶线性递推，维数至多 11。另一方面该标量读出在 x=1 下满足

$$\boxed{\det(s_{i+j}(1))_{0\le i,j\le10}=151782400\ne0.}$$

与上节同样的 Hankel 秩论证给出下界 11，故严格最小维数 **11**。证毕。

**新的信息成本结论：** 对固定非选择性无限重复包，保留 Laurent 平移效果的最小线性维数为 13；遗忘平移后只需 11。两种观察语言所差的两个维数是可计算的精确结构残差，**不意味着**有两条原生空间轴可以删去、也不意味着可用 11 个正权 BRC 控制状态。

## 5. 独立精确验证、局限与下一问题

- R261_symbolic_certificate.py（Python/SymPy）：精确构造 A、C、v；校验 χ_A 因式、13 次全矩阵湮灭、rank A=rank A²=12、x=2 的 13×13 Hankel 行列式、x=1 的 11 次初始向量湮灭及 11×11 行列式，**PASS**。
- R261_independent_fraction_check.py（不依赖 SymPy）：用正整数路径直方图直接传播 (q,r,ε,k) 与独立 Fraction 2 通道变换，校对 m=0..24 共25个样本；核对总路径数 2^m；独立有理数消元计算相同两个 Hankel 非零证人，**PASS**。
- R261_SYMBOLIC_REPORT.json 和 R261_INDEPENDENT_REPORT.json 记录脚本实际输出，所有证明依赖的无限时间部分为对有限维矩阵的精确湮灭恒等式，不是有限步经验推断。实测范围、算术、模型均在脚本中可回溯。
- 原生 Enterprise Math ControlPacket、EffectHistogram 与 Affine.then **未在 Source 匹配的安装环境运行**；没有 R193 原始路径来源规则、时间端口对应或 P000 心跳实际更新的验证。作者侧结果不具备独立 Driver 审核或正式理论接纳地位。
- BRC 既有工具复用：REUSE_APPLIED（数学语义，正效果直方图与仿射 THEN），REUSE_IDENTIFIED_EXECUTION_UNAVAILABLE（原生模块实际 import）。

**R262 最小接续问题。** (1) 取得 R193 真实来源标识、查询与时间端口的精确规范，为当前查询建立保真映射或最短反例；(2) 在原生 Source Python 环境执行原始 Affine.then、EffectHistogram 与 ControlPacket.from_edges/.then，保留可追溯运行回执；(3) 研究此 13 维 K-线性递推是否存在合法正权 BRC 实现或精确的正性障碍，明确不混淆 R260 每历史 7 状态下界；(4) 待原生 control quota/只读角色门禁允许时再核对活跃 Owner 与原生 CLAIM、活动/Result/Driver 流程。

**状态：** 作者侧数学证明+双实现精确证据，GitHub研究草稿，非 P000/原生物理定理，非正式 Result 或独立审核。
