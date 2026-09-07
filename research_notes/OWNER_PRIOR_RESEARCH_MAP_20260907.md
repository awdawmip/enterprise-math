# Perfect Prime / RH / Hodge：有界旧研究证据地图

辅助工作包：`/root/stability_research`；`ANCHOR_EXPOSED / READ_ONLY_HISTORY_MAP`。
本文件不领取三条线路，不继承任何 claim，不声明 live ownership、当前任务状态、Working Truth、canonical promotion 或新审查权力。

读取快照：本地 repository commit `fb260d16f7bc2995bec3ae30275dbddaabf4f467`。Global 知识租约另为 `main@4fa7d7d`，两者不可混淆。
本次只新增本地图；未改旧结果、Foundation、taskbooks/claims，未重跑旧计算，无 remote/commit。

## 1. 取舍与路由强度

当前 [native router](D:/em/owner-20260907/definitions/00_CURRENT_NATIVE_FOUNDATION.md:39) L39–73 列出原生定义与 BRC registry，L254–302 路由具体 BRC 方法；[Common Surface](D:/em/owner-20260907/docs/RESEARCH_COMMON_SURFACE.zh-CN.md:21) L21–41 区分 canonical、WIP、可执行证据并指向编号状态/定理索引。

在上述两文件、其直接列出的六个 BRC theorem ledgers、`research_common_surface.json`、`docs/PROBLEM_STATUS.*`、`docs/THEOREMS.*`、`research_method_inventory.json` 的有界名称检索中，没有发现 Perfect Prime/RH/Hodge 的显式主题入边。这不是整个依赖图不可达的证明，也不是旧结果不存在。

经 owner 明确允许，以下继续读取已经定位的 exact historical material，分别标为“历史可见”与“当前 native 显式主题入边未核实”。主证据限制为 Perfect Prime 3 份、Hodge 3 份、RH 5 份。日期上的“最新”只指本轮已定位的证据切片，不宣称全仓库所有历史中绝对最新。

| 主题 | 历史可见的最强实质交付 | 当前 native 入边 | 本次处置 |
|---|---|---|---|
| Perfect Prime | 2026-09-03 signed-secant / Bernstein / HCM0 精确接口，附历史接受审查 | 未发现上述当前索引中的显式主题入边 | 保留可消费系数接口；父非零性未闭合 |
| RH | 2026-09-06 X6/Pair-BRC 运输接口；修正后的 prime+Carleman 有限矩阵路线；sine 基频率尾界 | 主题入边未核实；笔记自身明确采用 P000/X6 与 BRC 标签纪律 | 保留精确有限接口和条件；不给 RH 证明状态 |
| Hodge | 2026-09-02 非 split Weil sixfold 的显式异常投影器和来源族 no-go，附历史接受审查 | 未发现上述当前索引中的显式主题入边 | 保留探测器及严格限制的负向边界 |

不能用通用 BRC 工具已经 canonical 的事实，把这些历史应用自动升级为 canonical theorem。历史 review 的 disposition 只按其当时记录转述，本图不验证现时 lease、任务存活或后续任务是否完成。

## 2. Perfect Prime：已闭合的是系数接口

**主证据。** PP1 [历史 review](D:/em/owner-20260907/driver_reviews/PERFECT_PRIME_AP_RESIDUAL_MOBIUS_BERNSTEIN_COEFFICIENT_DRIVER_REVIEW_20260903.md:10)；PP2 [research return](D:/em/owner-20260907/research_returns/PERFECT_PRIME_AP_RESIDUAL_MOBIUS_BERNSTEIN_COEFFICIENT_POSITIVITY_RETURN_20260903.md:21)；PP3 [exact checker 源码](D:/em/owner-20260907/research_checks/PERFECT_PRIME_AP_RESIDUAL_MOBIUS_BERNSTEIN_COEFFICIENT_POSITIVITY_CHECK_20260903.py:74)。

### 真正证明到哪里

在 PP2 固定的 AP/Cauchy 原子 Gram 模型中，对每个 `m>=2`，令 `n=m-1,D=2m-1,d=n(2m-3)`。每个非零 D 原子 Cauchy–Binet 基必须覆盖所有 m 个外层 j-group；其行列式平方分解成固定外层 Vandermonde 平方乘 `n×n` 组内 secant-difference determinant 平方。每一项单独含端点因子 `x^n(1+x)^n`，不是有符号项求和后偶然消去产生的因子。见 PP2 L137–315；PP1 L29–57 对接受强度作同样限定。

除去端点因子后的精确接口为

\[
q_{m,a}=V_x^{-2}\sum_{I:\,A_I=n+a}\varepsilon_I\Gamma_I,\qquad
[x^k]\widehat B_m(x)=\sum_{a\le k}q_{m,a}\binom{d-a}{k-a},
\]

其中非零基的 `Gamma_I>0`，但 `eps_I` 两种符号都实际出现。设

\[
h_{m,a}=(-1)^a q_{m,a}/\binom da,
\]

则

\[
\frac{[x^k]\widehat B_m(x)}{\binom dk}=(-1)^k\Delta^k h_{m,0}.
\]

这是一条对所有 m 的代数等价式：系数严格正性恰等价于初始行 HCM0，而不是已经证明 HCM0。见 PP2 L317–437；PP1 L59–81。

### 已证、有限证据、未知的分界

- **已证的历史交付：** 上述 secant 展开、逐项端点因子、系数/HCM0 等价。
- **只有限验证：** 更强的所有 shifted differences `(-1)^k Delta^k h_{m,r}>0`，历史记录仅覆盖 `2<=m<=10`；本轮没有重跑。PP2 L568–591 还明确 m=11 的尝试耗尽当时预算，没有可接受结果。
- **仍未闭合：** all-m HCM0、`Bhat_m` all-m 系数正性、父 critical-cofactor/determinant 非零性。失败发生在 `r>0` 只否定更强 shifted-HCM 路线，不自动否定 HCM0 或父定理。见 PP2 L518–566；PP1 L83–103。
- **未核实：** “Perfect Prime”原始命名所指的完整素数分类定义及其与上述父 cofactor 的全部原始桥接，不在这三份材料的自足范围。本图不把矩阵接口包装成新的素数判定器。

### 实际工具与 consumer 接口

实际使用的是 Cauchy–Binet、Vandermonde、组内行差、精确 `Fraction` determinant/interpolation 和 finite differences。PP2 L568–593 明确 `method_harvest=RESULT_ONLY`，没有新 general-purpose family。这三份主证据没有展示对现有 positive-BRC runtime 或原生 X6 几何坐标的实际调用；其 polynomial-coordinate gauge 是代数坐标，不应改名为原生空间坐标。正的 `Gamma_I` 与独立符号 `eps_I` 应继续区分。

可调用的准确本地函数在 PP3：

| 函数 / 行 | 输入与输出 | consumer 必须保留的边界 |
|---|---|---|
| `actual_h(m,t)` L74；`actual_tau(m,t)` L84 | 给定固定 m 和精确有理 t，返回原模型矩阵及其 gauge cofactor | 按任务域使用 `m>=2` 与 `Fraction`；这不是全 m 非零证书 |
| `q_coefficients(m)` L119 | 由已知有限次数界内的精确插值返回 `q_{m,a}` 的升幂有理列表 | 有限固定 m 计算；规模随 m 增长，m=11 历史预算失败不能解释成反例 |
| `secant_delta(m,groups)` L142；`cb_q_coefficients(m)` L161 | 构造组内 secant 矩阵，或枚举小 m 的 signed-secant 系数 | 每个 group 非空；`cb_q_coefficients` 有组合枚举成本 |
| `finite_hcm(q)` L241 | 返回该有限 q 的差分表摘要、digest、shifted-HCM 布尔值 | 函数直接 `assert` 初始行严格正，不是遇到反例也总返回结构化结果的通用判定 API |

本图不运行这些函数；CLI `--m` 和默认 `m=2..8` 仅按 PP3 L275 起源码说明。

**已有准确 gap：** PP2 命名的 `AP_SIGNED_SECANT_BASIS_HAUSDORFF_LIFT`，首先是 HCM0 初始行；全 shifted Hausdorff/moment lift 只是更强可选路线。这里不另造 successor，也不据历史 successor 字样断言现时 ownership。

## 3. RH：精确观察/尾界与未认证有限矩阵必须分开

**五份主证据。** RH1 [X6/BRC frontier](D:/em/owner-20260907/research_notes/RH_X6_BRC_TRANSPORT_FRONTIER_20260906.md:8)；RH2 [earthmover bridge](D:/em/owner-20260907/research_notes/RH_MOBIUS_EARTHMOVER_BALANCED_DIVISOR_BRIDGE_20260906.md:20)；RH3 [threshold ablation](D:/em/owner-20260907/research_notes/RH_THRESHOLD_BLOCK_ABLATION_MATRIX_SYMBOL_ROUTE_20260906.md:8)；RH4 [Carleman correction](D:/em/owner-20260907/research_notes/RH_ARCH_BOUNDARY_CARLEMAN_PRINCIPAL_DECOMPOSITION_20260906.md:8)；RH5 [sine tail certificate](D:/em/owner-20260907/research_notes/RH_SINE_BASIS_ARCH_DIAGONAL_TAIL_INERTIA_CERTIFICATE_20260906.md:16)。

RH3 显式引用 RH4 修正旧应用目标；RH5 进一步把有限频率积分认证与已证明的无穷尾界分开。其他同日文件只用于标题级定位，未纳入主证据或消费其数学结论。

### 实际原生工具及可消费的精确接口

**Factor/X6 局部端口。** 对 `omega(n)<=6` 且保留各 prime labels 的整数分解，RH1 L31–76 给出注入到六个 native slots 的局部端点，保存 `Omega(n)`、`sum e_p^2` 和 `Omega(n)!/prod e_p!`。这是有标签算术 fiber 的局部几何，不是全体整数的全局 X6 identity；prime labels 也不是第七、第八个原生空间轴。

**Pair-BRC。** 取 `W_x(n)=mu(n)^2 n^-2 exp(-x/n^2)`，并保留两个端点的 prime-support labels。按对称差大小 r 聚合正 pair mass，得 `H_x(z)=sum_r H_r(x)z^r`。RH1 L151–191 给出

\[
H_x(1)=A_x^2,\qquad H_x(0)=V_x,\qquad H_x(-1)=P_2(x)^2.
\]

末式的 parity 是最后的 signed readout；不能把 positive mass 本身当成 Möbius cancellation。RH1 L193–247 的容量边界是：若把正质量合并成 M 个状态，collision 至少为 `A_x^2/M`；结合该笔记引用的正平方自由尺度，固定64状态或无标签 exponent shape 不足以保留所需 collision scale。尺度渐近依赖旧笔记指定的经典算术输入，不能由有限 X6 图自行推出。

**运输等价接口。** RH2 L20–107 定义两条 `mu=+1/-1` 的升序平方自由整数流 `a_j,b_j`，同秩配对，严格给出 cut flux `|M(t)|` 和

\[
W(X)=\sum_j |[a_j,b_j]\cap[X,2X]|=\int_X^{2X}|M(t)|dt.
\]

在经典 Mertens/解析延拓/函数方程接口下，`W(X)=O_epsilon(X^(3/2+epsilon))` 对每个 epsilon>0 等价于 RH。此为重述/接口，不是该 bound 的证明。这里按 `mu` 定义两条流是任务本身的声明域；零 Möbius 值在原整数域仍存在，不能把该流误称为包含所有整数的 census。算术排序线也不是新 native axis。

**有限阈值矩阵。** RH3 L43–126 对有限 Hermitian `A>0,D>0` 和 cross B，定义

\[
M_\eta(B)=\begin{pmatrix}\eta^2 A&B\\B^*&D\end{pmatrix},\qquad
r_B(\eta)=n_-(M_\eta(B))=\#\{\sigma_j(A^{-1/2}BD^{-1/2})>\eta\}.
\]

当 `B=B0+E, ||E||<=eps`，以 `M_eta(B0)` 的 `±eps` 两个计数阈值夹住 `r_B`；若另有 rank<=r 的 K 修复，计数界放宽 `2r`。这是有限矩阵惯性/范数证书，输入必须包括严格正定的对角块和可核验的 gap/tail，不能用浮点近似直接替代。

RH3 L24–41 记录 T2 block finite certificate、T4 collision capacity、T6 safe quotient、T8 labelled observable spectrum 的 `REUSE_APPLIED`。这里 BRC 是保留 `(A,B,D)` 与 prime/arch/pole 来源标签的关系 carrier；这五份笔记没有给出可据此声明 `REUSE_EXECUTED` 的特定 Python runtime 调用。

### 必须沿后续修正消费，不能复活旧误删

RH3 L8–22 已明确更正：不能把整个 raw continuum archimedean cross 视作有限秩加任意小范数尾。RH4 L39–190 推出

\[
K_\infty(s)=-e^{-|s|/2}/(1-e^{-2|s|}),\quad
K_\infty(s)=-1/(2s)+G(s)\quad(s>0),
\]

其中 G 在 `|z|<pi` 解析。接触的同号 old/shell 分支保留非紧的 `-1/[2(u+v)]` Carleman 主项，其对数坐标符号是 `-pi/[2cosh(pi xi)]`。因此可用参考是

`B_ref=B_prime+B_Cauchy/Carleman`，

只有 regular arch remainder 和另行处理的 pole term 能进入所声明的小尾修复。RH4 L24–32 把这明确归为 BRC observer-preservation：薄边界并不代表关系可以删掉。跨分支标签不能在证明之前 recoalesce。

### 最新已证明尾界与仍条件性的数值结论

RH5 L16–154 对长度 ell、每个反射分支 N 个 Dirichlet sine modes，取 `alpha_k=k*pi/ell`、`T>max(7,alpha_N)`，给出

\[
0\preceq\Delta_{arch}(T)\preceq B(\ell,N,T)I,
\]

\[
B(\ell,N,T)=\frac{16}{\pi\ell}\frac{3\log T+1}{9T^3}
\sum_{k=1}^N\frac{\alpha_k^2}{(1-(\alpha_k/T)^2)^2}.
\]

RH5 L186–222 的消费规则：当 cross 已固定或独立认证，cutoff-free threshold matrix 等于有限 cutoff matrix 加 PSD 对角尾。若有限矩阵已严格证明有 q 个负特征值，且最大负值 `<-max(eta^2 B_A,B_D)`，则尾部不能改变这 q 个负惯性计数。

但 RH5 L224–294 明确：`N=8` 的 reference/full-cross 负 gap 当前材料仍是 floating diagnostic；还须对有限 `[0,T]` 的每个矩阵项做 interval enclosure 和 interval LDL*/inertia。`eta=0.999` 尤其依赖独立交叉尾和舍入预算。有限基的 cutoff-free 惯性也不是无限算子的惯性，没有 eta=1 或 RH 证明。本文只转述显式公式；没有重跑十进制预算，没有重新认证旧浮点数。

**已有准确 gap：** RH5 L274–284 指定的最小未闭合单元是 first-step `N=8, log2→log3`，从 `prime+Cauchy` reference、T=2000 开始认证有限矩阵并接上 PSD 尾。另一个较早的算术目标 RH1 L592–627 是同秩差 `|a_j-b_j|<<j^(1-delta)` 的某个固定 power saving；这两个现存缺口属于不同接口，不能凭地图把它们合并成同一个已证明机制。

### 本次阅读发现的精确消费范围缺口

RH1 L249–277 把未正规化积分

`E_sigma=integral_0^infinity |P_2(x)|^2 x^(1-sigma) dx`

写在 `sigma>1/2` 下，并使用 `Gamma(2-sigma)` 核。**不能把“every sigma>1/2”字面消费到 sigma>=2。** 因绝对收敛，`P_2(x)→sum mu(n)/n^2=1/zeta(2)>0` 当 x→0；于是低端行为为正常数乘 `x^(1-sigma)`，在 sigma>=2 发散。相同核的 Laplace 积分也要求 sigma<2。

所以本图只允许把该未正规化能量/核接口放在 `1/2<sigma<2`；其他范围必须另给低端截断或正规化定义。此处仅记录可直接检查的范围缺口，不改原文件、不宣告 RH 路线失效，也不伪造已修复状态。

## 4. Hodge：异常投影器与来源族 no-go，缺的仍是 seed

**主证据。** HG1 [历史 review](D:/em/owner-20260907/driver_reviews/HODGE_H0N_NONSPLIT_WEIL_EXCEPTIONAL_CH3_SEED_OBJECT_DRIVER_REVIEW_20260902.md:12)；HG2 [research return](D:/em/owner-20260907/research_returns/HODGE_H0N_NONSPLIT_WEIL_EXCEPTIONAL_CH3_SEED_OBJECT_RETURN_20260902.md:33)；HG3 [task-local checker](D:/em/owner-20260907/research_checks/HODGE_H0N_NONSPLIT_WEIL_EXCEPTIONAL_CH3_SEED_OBJECT_CHECK_20260902.py:65)。

### 固定对象和已证明的强度

HG2 L33–99 固定 `K=Q(i)`、Hermitian form `diag(1,1,1,-1,-1,-3)` 的非常一般 Weil sixfold，判别类 `[-3]` 与 split `[-1]` 不同；目标满足 `NS_Q=Q theta`，异常 `W_K=wedge_K^6 H^1` 是有理二维 `(3,3)` 子空间，且 `W_K intersect Q theta^3=0`。

**这里的 sixfold、K^6、Hodge embedding blocks 是代数几何/上同调类型，不是原生 signed X6 Cell 身份。** 本图不因“六”相同就添加空间坐标解释。

HG2 L101–172 构造精确 separator：取 target algebraic endomorphism `u=1+2i`，其 degree-six blocks 有已列出的七个特征值，设

\[
P(t)=\frac{-(t-125)(9881t-609029)(t^2+70t+15625)(t^2+150t+15625)}{57000000000000000}.
\]

`Pi_W=P(u*|H^6)` 在两块 exceptional eigenvalues 上为1，在其余五块上为0，是代数对应诱导的有理投影器。它杀掉 `theta^3`，但不会凭空提供非零代数输入。

HG2 L174–255 的已证来源族 no-go：semihomogeneous rank-r bundles 满足 `ch_3(E)=c_1(E)^3/(6r^2)`，由 `NS_Q=Q theta` 得零 exceptional projection；有限 shifts/direct sums/extensions/cones 通过 K0 加法保持该结论。独立验证输出仍为 semihomogeneous 的 Fourier–Mukai 子族，以及相关 Chern data 全来自 divisor algebra 的预期余维3 Thom–Porteous 子族也被排除。

**不能扩张到：** arbitrary direct summands/Karoubi completion、任意 Fourier–Mukai 输出、任意代数对应。尤其 `Pi_W` 自身就是非零到 W_K 的 algebraic correspondence；不能声称“所有 correspondence 都到不了 W_K”。HG2 L257–276 和 HG1 L29–38 明确拒绝这些强化。

### consumer 的准确接口、实际工具与条件

- **数学接口：** 给出固定目标上的代数/derived object E，并独立证明其 target-side 几何假设及 `ch_3(E)`，然后计算 `Pi_W(ch_3(E))`。非零才是新 seed；投影器存在不等于 seed 存在。
- **条件放大：** 若已经取得一个非零有理代数 `w in W_K`，则 `{w,u*w}` 构成 W_K 的有理基，因为其二次最小多项式判别式 `-7744` 不允许有理特征线。该事实不提供 w。见 HG2 L154–172。
- **源码接口：** HG3 L65 的 `projector(z)` 接受高斯有理数 `(real,imag)` 对，精确计算上述 P(z)，不是一般几何对象或任意矩阵的 projector API。该脚本 L79 起有顶层 checks/print，导入会执行验证；不是已抽出的无副作用 production module。本轮只读源码。
- **实际工具：** rational spectral separation、Gaussian arithmetic、K0/Chern character、Mukai semihomogeneous 公式、Thom–Porteous。HG2 L305–313 明确 `NO_TOOL_PAYLOAD`；主证据中没有 positive-BRC runtime 或 native-coordinate 执行证据。不能以项目通用 BRC substrate 存在代替实际调用证明。
- **验证强度：** HG1 L18–27、HG2 L291–303 记录历史 `20/20 PASS`，仅覆盖有限/符号证书层；本轮未重跑，也不把 checker 当成 Mukai 等无界几何定理的证明。

**已有准确 gap：** HG2 L315–327 尚需构造目标侧非零 exceptional `ch_3` seed 或能产生非零投影的代数 source class。HG1 L40–50 指向一个严格限定的 successor： genuinely non-semihomogeneous、intermediate-support Fourier–Mukai/GRR family，终止条件是非零 seed、该明确族的零投影定理或 exact instantiation obstruction。本图不核实该 successor 的当前执行状态。

HG2 L278–289 的外部文献判断仅按其 2026-09-02 的历史 routing statement 保存；本轮没有更新外部文献，不据此声称截至今日仍不存在覆盖目标的新定理，更不推出非代数性或 Hodge conjecture closure。

## 5. 来源固定与消费者读取规则

以下 source SHA 是 Git blob SHA，均在本地读取 commit `fb260d16f7bc2995bec3ae30275dbddaabf4f467` 可解析；本次检查这些主证据没有工作树修改。文件路径和具体行已在各节给出。source commit、blob、历史记录中自带的 result digest 是不同层次，不应相互替代。

| ID | 主证据 Git blob SHA |
|---|---|
| PP1 | `53d86a4efd57deb55ad03d787ae8d30d46a5e933` |
| PP2 | `19a0bcf5eee3c6100443d66ed9a53d2979a5ace0` |
| PP3 | `8081c1908629f4f7bb0a52c2061e73885bda17ea` |
| RH1 | `aa31732a125424ee1780da5567464ce1ca14bfd1` |
| RH2 | `3a316b444e3aedb5090ee5404a0cecb499a3e3d5` |
| RH3 | `21648879a43e517f92c633ff237cb4d7822db4db` |
| RH4 | `4fadd43fb4eb25af5444f5b422120e8c3d4f9466` |
| RH5 | `18a5224e40c70e5ba95e6def44bc575f2ce693cb` |
| HG1 | `4074938be40dd54aa56997f3fafb6112482365ad` |
| HG2 | `b504f4e3aa5401988cb3f51d699115489db3ee1c` |
| HG3 | `24852cc62bc2ace0254e0c4a65af54c02fc9f1e7` |

共同路由源：native router blob `997f8b4a1d27bc7645959967b217972aa2454ef4`；Common Surface blob `9b4a7a4e2bcda5a7fbaf5f3f35aa10b5762b2af7`。共同路由只提供当前类型/入口约束，不为各历史应用追加真值。

新 consumer 应从准确数学接口进入，先保留该接口的对象类型、符号、来源标签、前提与 cutoff，再判断其问题是否适用；不要从旧标题或历史接受状态推断父猜想已解。未核实的 current-native 入边、正式可复用 package 与后续 live status 均保持未核实，本图不为填满目录而补造它们。

辅助工作包：`/root/stability_research`。

Global-Knowledge-Sync: main@4fa7d7d / GLOBAL_KNOWLEDGE_V1
