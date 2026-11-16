# R477｜有限正序列 PF₃ 的精确末项延拓区间、边界证书与非遗传性

日期：2026-11-02。状态：AUTHOR_SIDE_ANALYTIC_AND_EXACT_INTEGER / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING。对象：任意有限严格正实序列的半无限 Toeplitz 矩阵；signed BRC 是潜在应用。不改变 P000/ACTIVE 世界观，科学输入继承 R462 冻结 pin 18783e01e3646c72b7aab3b16d3f565e83e6446f。

## 1. 完整定理（一步末项可行区间）

设 n≥2，固定 b=(b₀,…,bₙ₋₁)，所有 bᵢ>0；对 t>0 置 a(t)=(b₀,…,bₙ₋₁,t)，越界系数为零。令半无限 Toeplitz 矩阵 T(a)ᵢⱼ=aⱼ₋ᵢ，记

\[
D_{2,j}(a)=a_j^2-a_{j-1}a_{j+1},\quad
D_{3,j}(a)=\det(a_{j+v-i})_{0\le i,v\le2}.
\]

PF₃ 指全部阶数一至三的有限子式非负。

**n=2：** T(a(t))∈PF₃ 当且仅当
\[
\boxed{0<t\le b_1^2/(2b_0).}
\]

**n≥3：** 首先检验以下与 t 无关的全部固定条件：
\[
D_{2,j}(b)>0\ (1\le j\le n-2),\qquad
D_{3,j}(b)\ge0\ (1\le j\le n-3). \tag{F}
\]
若 (F) 不成立，则不存在可使 a(t) 为 PF₃ 的 t>0。若成立，定义

\[
\begin{aligned}
A&=b_{n-1},\ B=b_{n-2},\ C=b_{n-3},\\
\Delta&=B^2-CA=D_{2,n-2}(b)>0,\\
d&=D_{2,n-3}(b)>0,\\
Q&=D_{3,n-2}(b_0,\ldots,b_{n-1},0)
  =B^3-2BCA+b_{n-4}A^2,\quad b_{-1}:=0,\\
L&=\max(0,-Q/d),\qquad
U=\frac{A^2}{B+\sqrt{\Delta}}.
\end{aligned}
\]

**结论**：
\[
\boxed{T(a(t))\in PF_3\iff t>0,\ L\le t\le U.}\tag{R477}
\]
L>U 表示可行集合为空；L=U 则只有一个可行末项。边界三阶子式允许等于零。

对于所有数据均为有理数的情况，(R477) 可用完全无根式的精确判号实现：在 (F) 成立后，只须检查

\[
Q+td\ge0,\qquad Bt<A^2,\qquad A^3-2ABt+Ct^2\ge0. \tag{Rational}
\]

## 2. 解析证明与精确裕量

使用 R474（有限严格正实系数的局部 PF₃ 充要判据），PF₃ 等价于所有局部 D₂,j 严格正、局部 D₃,j 非负（0≤j≤n）。对加上的末项 t，有：

- j≤n−2 的 D₂ 不受 t 影响，D₂,n−1=A²−Bt，D₂,n=t²；
- j≤n−3 的 D₃ 不受 t 影响，D₃,n=t³；
- 两个剩余子式的**精确恒等式**为
\[
D_{3,n-2}(a(t))=Q+td,\qquad
D_{3,n-1}(a(t))=P(t):=A^3-2ABt+Ct^2. \tag{E}
\]
其中第一式中 t 的余子式系数为 bₙ₋₃²−bₙ₋₄bₙ₋₂=d。n=3 时 d=b₀²。固定条件 (F) 是必要的。成立时 d>0，故 D₃,n−2≥0 等价于 t≥−Q/d。

末项二阶正性要求 t<t₀=A²/B。由 Δ>0，

\[
P(0)=A^3>0,\qquad
P(t_0)=-A^3\Delta/B^2<0.
\]

如果 C=0，P 为一次式，唯一正根 U=A²/(2B)；如果 C>0，P 为二次式，其较小的正根为
\[
U=\frac{A(B-\sqrt\Delta)}{C}
 =\frac{A^2}{B+\sqrt\Delta}<t_0,
\]
另一根严格大于 t₀。因此在合法二阶区间 (0,t₀) 内，P(t)≥0 恰等价于 t≤U。合并全部固定和末项条件得到 (R477)，并同时证明 (Rational) 等价。

n=2 时直接有 D₃,1=b₁³−2b₁b₀t、D₂,1=b₁²−b₀t，其余局部条件自动成立；严格二阶条件被更强的三阶上界保证，得给定公式。

**边界裕量。** 在 n≥3 的可行区间上，由 P(U)=0 得到
\[
\boxed{D_{3,n-1}(a(t))=(U-t)\bigl(2A\sqrt\Delta+C(U-t)\bigr).}
\]
并有
\[
D_{2,n-1}(a(t))\ge A^2-BU
=\frac{A^2\sqrt\Delta}{B+\sqrt\Delta}>0.
\]
故新的末项只需两个单侧量 L、U 及已复用的内部条件即可得到确切的正性余量。

## 3. 可修复的非 PF₃ 前缀：删除最高次系数不保 PF₃

选 b=(1,1,1/2,1/6)。其 D₃,2=−1/72，故 b∉PF₃；但对追加项 t，第 1 节给出
\[
\frac1{36}=L\le t\le U=\frac{3-\sqrt3}{36}.
\]

取 t=1/30，则完整 a=(1,1,1/2,1/6,1/30) 满足

\[
(D_{2,0},\ldots,D_{2,4})
=(1,\tfrac12,\tfrac1{12},\tfrac1{90},\tfrac1{900}),
\]
\[
(D_{3,0},\ldots,D_{3,4})
=(1,\tfrac16,\tfrac1{360},\tfrac1{5400},\tfrac1{27000}).
\]

据 R474，a∈PF₃。于是有限 PF₃ 序列删去最高次系数后可以失去 PF₃；研究有限尾部时不能额外假设各个前缀天然 PF₃。取 t=1/36 时 D₃,2 恰为零，而整体仍是 PF₃。

另一端点取 b=(1,5,9)，Δ=16，U=9。a(9)=(1,5,9,9) 的 D₃,2=0，整体 PF₃；a(10)=(1,5,9,10) 的 D₃,2=−71，严格负。

特别地，(1,1,1/2,1/6) 也是指数级数 1/j! 的四项截断；上述四项的确切负三阶子式定位了该截断中的末端失效。这个例子的结论只涉及声明的有限 Toeplitz 序列。

## 4. 实际执行的精确检查

运行 R477_VERIFY.py（Python 标准库 Fraction + 任意精度整数，无浮点），对长度 L=3,4,5,6，系数各取 {1,2,3} 的全部 1080 条正整数序列交叉比较：①本定理的精确区间判据；②R474 的全部局部子式；③首个 (L+2)×(L+2) Toeplitz 方块的一、二、三阶全部子式直接枚举。全部分类一致：11 条 PF₃、1069 条非 PF₃；第三条路径遇到首个负值或枚举完毕为止累计实际计算 106681 项。程序还以 Fraction 检查第 3 节的非遗传性、下边界、上边界和超界样本。结果为 R477_EXACT_PASS，分类流 SHA256：b6bcc35c653c68fd0cfc1c5f775aa576362ef0f9900e8dd20987a4788eb7e0c5。详细分长度计数见 R477_EVIDENCE.json。

对任意正实数的定理来自第2节的解析代数和 R474 的局部判据；有限枚举只是其明确范围内的独立精确回归。R474 的充分性复用 R441-A 的 Schur/LR 归约，均为作者侧证明，待独立数学审阅。

## 5. 科学输入、用途与下一问题

- 研究输入：R474（8c4ec04504fc3759f3e15d46e673da09fd7792a6）的局部 PF₃ 判据；R441-A 的 Toeplitz–Schur/LR 归约；R476Z（c442e8a84c6df4e045e9eb9158b49292a5c7f98c）的非负支撑讨论。
- signed BRC 最新已核作者侧前沿为 R475，s=249…256、奇数 r≤279 的条件性 PF₃ 拼接；本轮未对这些参数重复计算，也未增加新的 r 上限。
- 全局规范快照：awdawmip/chatgpt-global-knowledge main@77e29c24ce9a8f7cec42c9c5fc9e349db30533d9；Enterprise Math 控制 main@5165893252572c4583998013ee3fb00c6d64b2da；科学冻结 R462 pin 为 18783e01e3646c72b7aab3b16d3f565e83e6446f。
- 实际 GitHub 认证 awdawmip，push=true。原生 session_start：STATIC_READONLY_SCOPE_DENIED、operation_sent=false；活跃 owner 查询：CONTROL_QUOTA。该材料为作者侧研究，不形成 CLAIM、Result 或独立 Driver 接纳；P000/ACTIVE 世界观未改。
- BRC 复用：仅针对既有 signed BRC 的**辅助标量 Toeplitz 读数**提出可应用的新区间判据，本轮无新的原生 BRC/Shor 计算，也不改变冻结的科学输入及其分支/符号语义。

**下一单元：**对实际 H(r,s) 尾部序列提取 A,B,C,Q,d，研究 s,k 同时无界增长时能否直接证明 L≤H≤U 的统一区间下界/上界；对出现 Q<0 的位置判断正末项是否修复，避免将单侧前缀失败误认作全序列负证。并继续对 R474/R441-A 的承重证明作独立审查。
