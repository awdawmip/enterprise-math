# R294 — BRC 28个候选完整效果的最终严格全序（不依赖局部CLT/Edgeworth）

2026-10-26。作者侧代数奇点证明、整数复算；**尚未经独立 Driver 审核/原生 Source 数学接纳**。适用于正权、有序六边 BRC 辅助来源计数模型，不是原生 X6 Cell 动力学、心跳时间或物理残差的定理。

## 0. 来源、前沿及严格作用域

GLOBAL_KNOWLEDGE_V1 固定读 `awdawmip/chatgpt-global-knowledge:main@40ae4bf39f84a1ad1b122a824019ef562a5e4bc1`；同一快照载入 `00_BOOTSTRAP.md`、`OPERATING_MANUAL.md`、Enterprise Math 项目路由、`P000_STARTUP.json`、`P000_REALITY_FOUNDATION.json` 和 ACTIVE `我眼中的世界.md`，以及本任务触发的 BRC/数学/代码/活动/进度规则。P000 原件 Git blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`，与启动投影一致。

EM 规范固定读 `awdawmip/enterprise-math:main@3bab655d58d3795b939517514de7594004c85655` 中的 `docs/PORTABLE_RESEARCH_PROTOCOL.md`、`research_persistence_policy.json`、`docs/RESEARCH_ACTIVITY_PROTOCOL.md` 和 `docs/HEARTBEAT_BRC_ONLY_ARITHMETIC.md`。数学上引用 R283 @ `98eb41b63bb29c9b32d79ba5d9b4ef74d0975fa0` 的完整效果 Laurent Green 函数以及 R293 @ `e45b32cc389fdf19a24af8da420030165b4e824a` 的28效果窗口。**两者仅有作者侧证明；本结果的无穷全序明确以这两个前提为条件。** 相比 R283 的前三峰渐近，这里的新路线不使用 R280 局部中心极限定理或 R281 Edgeworth 展开。

原始有序转移（`q,bit -> q',eta,c`）：
- q0: bit0→(2,-1,-1)，bit1→(2,+1,-1)；
- q1: bit0→(0,-1,-1)，bit1→(0,+1,-1)；
- q2: bit0→(1,+1,+1)，bit1→(2,+1,-1)。

禁止相邻00；初始 `(q,epsilon,k)=(0,+1,0)`；有序右复合 `(epsilon,k)★(eta,c)=(eta epsilon, eta k+c)`；`P_n(epsilon,k)` 只计终态q0且保留每个原始来源词为1份的正整数重数。

## 1. 统一代数核及奇偶对齐

设 `y=x²`，
\[
\rho=(3-\sqrt5)/2,\qquad\varphi=(1+\sqrt5)/2,
\]
\[
D(y)=(1-y)(1-y^3)(1-3y+y^2),\qquad
J(y)=\frac1{(1+y)\sqrt{D(y)}}.
\]
令唯一 `h∈y⁴ℕ[[y]]` 满足
\[
h=y^4+(y+2y^2+y^3+y^4)h+y(1+y)^2h^2,
\quad w=(1+y)(1+h).
\]
R283 精确 Laurent 提取及 `u=xw` 给出，对 `m≥1` 的正符号和 `m≥2` 的负符号：
\[
F_m^+(x):=\sum_nP_n(+1,-m)x^n
 =x^{m+2}J(y)w^m(1-y+y^2-yw),
\]
\[
F_m^-(x):=\sum_nP_n(-1,-m)x^n
 =x^{m+2}J(y)w^{m-2}(1-yw).
\]
固定端点 `m=0` 或 `m=1` 的公式必须单独处理，不可错误地把通常公式延拓到禁用指标：
\[
F_0^+=J(y)[1+y+y^2-y(2+y)w],\qquad
F_0^-=J(y)y^3 w(w-1),\qquad
F_1^-=x^5J(y)(w-1).
\]
这些式子可直接从 R283 给出的 `G_±(x,z)` 对 `z^0,z^1` 及 Green 方程提取；独立原始来源DP复核如下。

对于 `m≡p (mod 2),p∈{0,1}`，定义对齐生成函数
\[
C_m^\epsilon(y)=\sum_{r\ge0}P_{2r+p}(\epsilon,-m)y^r=J(y)N_m^\epsilon(y).
\]
普通指标时取 `s=⌊m/2⌋+1`，有
\[
N_m^+=y^sw^m(1-y+y^2-yw),\qquad
N_m^-=y^sw^{m-2}(1-yw).
\]
三个例外：`N_0^+=1+y+y²-y(2+y)w`, `N_0^-=y³w(w-1)`, `N_1^-=y²(w-1)`。

## 2. 28个效果的全长度后段严格排序

令 `t=1-y/ρ`；解 `yw²-(1+2y²-y³)w+1=0` 的形式支，精确 Puiseux 展开为
\[
w(y)=\varphi-\beta\sqrt t+\gamma t+O(t^{3/2}),\quad
\beta^2=\frac{-5+3\sqrt5}{2},\quad
\gamma=\frac{11-3\sqrt5}{4}.
\]
\[
J(y)=A_0t^{-1/2}(1+O(t)),\quad
A_0=\frac1{(1+\rho)(1-\rho)\sqrt{(1-\rho^2)(1+\rho+\rho^2)}}>0.
\]
将每个 `N_m^epsilon(y)` 代入同一 Puiseux 展开。所有在同一奇偶类的效果具有**相同的领先常数**：
\[
N_m^\epsilon(y)=K_p+b_m^\epsilon\sqrt t+K_pR_m^\epsilon t+O(t^{3/2}),\quad
K_0=\rho^3,\ K_1=\rho^3\varphi.
\]
在带分母4的二次数域中，直接代数展开并化简得

\[
4R_m^+=-3-8m-15m^2-4s+(5+2m+7m^2)\sqrt5
\quad(m\ge1,s=\lfloor m/2\rfloor+1);
\]
\[
4R_m^-=-9-18q-15q^2-4s+(5+8q+7q^2)\sqrt5
\quad(m\ge2,q=m-2,s=\lfloor m/2\rfloor+1);
\]
例外值
\[
4R_0^+=-7+5\sqrt5,\quad
4R_0^-=-37+17\sqrt5,\quad
4R_1^-=-10+4\sqrt5.
\]

**结论（严格但尚无有效起点）。** 在 R293 的28效果窗口之内，所有充分大偶数长度的效果计数，从大到小依次为：

`(+,-4) > (-,-4) > (-,-2) > (+,-6) > (+,-2) > (-,-6) > (-,0) > (+,-8) > (+,0) > (-,-8) > (+,-10) > (-,-10) > (+,-12) > (-,-12) > (+,-14)`。

所有充分大奇数长度依次为：

`(-,-3) > (+,-5) > (+,-3) > (-,-5) > (-,-1) > (+,-7) > (+,-1) > (-,-7) > (+,-9) > (-,-9) > (+,-11) > (-,-11) > (+,-13)`。

顺序的**全无限尾部证明**：由于
\[
D(y)=(1-y)^2(1+y+y^2)(1-y/\rho)(1-\rho y),
\]
最近分支奇点 `ρ` 唯一（其他相关奇点模长≥1），每个对齐级数有标准平方根局部延拓。任意同奇偶的两个候选 a,b，领先 `K_p` 精确抵消，而 `b_a-b_b` 乘 `J\sqrt t` 给出解析常数项，不控制大阶系数；首个非解析项来自 `t`，其系数为 `A_0K_p(R_a-R_b)\sqrt t`。平方根系数传递
\[
[y^r]\sqrt{1-y/\rho}
=-\frac{\rho^{-r}}{2\sqrt\pi\,r^{3/2}}(1+O(r^{-1}))
\]
故
\[
\boxed{P_{2r+p}(a)-P_{2r+p}(b)=
\frac{A_0K_p}{2\sqrt\pi}(R_b-R_a)\rho^{-r}r^{-3/2}
(1+O_{a,b}(r^{-1}))}.
\]
比较 `R` 必须**升序**；用 `A+B√5` 的严格整数平方比较，无浮点近似，检查上述同奇偶每一对相邻 `R` 具有严格正差。因此每个有穷候选集有共同的（目前非有效的）永久全序起点。**只在额外使用 R293 的28窗口定理时，上述全序才提升为全部完整效果的最终排名；它不能从一个有限DP窗口外推。**

由最小二次域相邻差得
\[
R_{(-,-4)}-R_{(+,-4)}=\frac{170-76\sqrt5}4>0
\quad(\text{偶数前二}),
\]
\[
R_{(+,-5)}-R_{(-,-3)}=\frac{-380+170\sqrt5}4>0
\quad(\text{奇数前二}).
\]
将 `r=(n-p)/2`、`ρ^{-1}=φ²` 换算，得到峰隙系数与 R283 数值一致：偶数约 `0.000670306647446`、奇数约 `0.001498851229459`，乘 `φ^n/n^(3/2)`；现证明不调用 R280/R281，不过仍条件依赖所采用的精确原始生成核及28窗口。

## 3. 可执行验证证据及其有限边界

`R294_verify_fixed_window.js` 用 JavaScript BigInt 从 `h` 固定点方程、`w` 的精确整数卷积、`J=1/((1+y)√D)` 微分递推独立生成所有奇偶28候选效果 GF；又从六边来源字母、相邻00约束、终态、完整仿射右复合进行原始整数DP。

实测 `n=0..180` 上共 `2535` 个完整效果系数与独立来源DP一致；`n=81..180` 的全部 `100` 层最强三效果符合严格排序；二次域 `R` 顺序全部采用纯整数比较（`a²-5b²` 符号）。运行返回 `PASS`。精确结果 `EXACT_EVIDENCE.json`。上述有限运行不证明无限长度归纳，不替代代数奇点证明；Puiseux 系数与 R283/R293 输入仍需独立形式化审查。

## 4. 真实权限、留下的问题

真实 GitHub 用户 `awdawmip`，对 `enterprise-math` 具有写入权限。原生 `em_control_tasks` 返回 `CONTROL_QUOTA`；`em_session_start` 返回 `STATIC_READONLY_SCOPE_DENIED; operation_sent=false`，故无法权威核实活跃 owner，亦未产生原生研究 CLAIM、Source Result、Driver 复核或数学接纳。本材料是作者侧研究分支，不代表状态机的数学推广。P000 与 ACTIVE 世界观未变；不把正权路径质量冒充有符号/复振幅抵消。

**下一精确单元**：对有限的28候选相邻差建立具有显式整数阈值的无穷尾部不等式（可复用 R293 的有理数比值锥、Puiseux 有效余项或正系数滤波器），并对阈值前所有长度穷尽DP；再处理 clean/dirty 六通道共同峰 `B_n=Λ_n` 的独立条件与驱动审核。R294 所得仅为最终全序的**存在性**结论，**不声称 N_peak=81，也不声称 B_n=Λ_n**。
