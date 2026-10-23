# D25/LOW — 二阶 Beta 残差不能单独清零：精确递推、耦合证书及 611 个模素数见证

**作者材料 / 2026-10-23 / TASK_RESEARCH。** 状态：AUTHOR_EXACT_RATIONAL_RECURRENCE_PROOF / EXACT_NONZERO_SECOND_MOMENT_WITNESSES / FINITE_MODULAR_FALSIFICATION / **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT / NO_FORMAL_CLAIM / NOT_NATIVE_BENCHMARK**。真实 Research 逻辑 conversation 标识为 chatgpt-research-onhour-enterprise-math-20260923，仅为本作者来源，不能据此推导服务签发的 session、claim 或 run。已有 LOW/WZ/B11 上下文已暴露，作者不具有独立审阅身份。

**母目标：** D25 SECOND-DIGIT-LIFT，Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT，published TP2-B6F4FC938FF94941C1B7。沿用历史 Source 冻结输入/checkpoint pin c47e13e4aba0e006366f989d6334d443f6333ae3，不能由更新的控制 main 自动变更。已冻结 D24 supersingular UR Result RR-AC9B3BA5BD277CE043F5 与已接纳审查 DR-610CB297F3195E8F2D9E 不重做。全局 ACTIVE_LOCKED P000 与 ACTIVE 世界观已在 global-knowledge main@674c44f8c3c194a82c63f0bba6da995d1d307ad3 核对；外部有理数积分仅用于辅助，未经 native X6 桥接。

## A. 严格承接的当前数学前沿

复用已经作者证明、尚未独立准入的 LOW 线性调和 Beta shift：

\[
p=6m+1\ \text{prime},\quad
b_n=(-1)^n2^{-n}{m\choose n},\quad w_n=6n-1,
\]
\[
\mathcal A_m=\frac{(p-1)!}{3^{p-1}((2m)!)^3},\quad
\chi_p=\frac{(4/3)^{p-1}-1}{p},\quad
C_m=\frac12\sum_{j=1}^{m}\frac{(-1)^j}{j}
+\frac23(H_{2m}-H_m)+\frac13(H_{4m}-H_m).
\]
已有单标量端点缺陷为
\[
\mathscr D_m^\beta
=\underbrace{\frac{\mathcal A_m\Theta_m-1}{p}}_{\Delta_m}
+\mathcal A_m\bigl(2^{-m}C_m+\mathsf E_m\bigr)-\chi_p,
\quad
\mathsf E_m:=\mathsf M_m+J_m^{(2)}-2V_m,
\]
\[
\Theta_m=2^{-m}[3(-1)^m-2]+I_m+J_m^{(1)},\quad
\mathsf M_m=\sum_{n=0}^mb_nw_n M_n.
\]
其中 M_n、J_r、各 Beta moment 的确切定义仍以既有
20261023_onhour_d25_LOW_linear_harmonic_beta_shift.md 和冻结 D25 来源为准。
本单元**不**重证 WZ、D24、B11、第一位、端点 611 素数的早先直接串流证书。
当前 EP/LIFT 的尚未证明全素数目标仍是 \(\mathscr D_m^\beta\equiv0\pmod p\)。

## B. 新的有限 Euler–Beta recurrence：所有整数 m 上的精确恒等式

定义对整数 \(s\ge0,\ r\ge1\)
\[
U_{s,r}:=\int_0^1x^{r-1}(x-\tfrac12)^s\,dx,\qquad
T_{m,r}:=\int_0^{1/2}x^{r-1}(x-\tfrac12)^m\,dx.
\]
则**精确有理数恒等式**：
\[
\boxed{\begin{aligned}
U_{s,1}&=\frac{1+(-1)^s}{2^{s+1}(s+1)},\\
(s+r+1)U_{s,r+1}&=\frac r2U_{s,r}+2^{-(s+1)},\\
T_{m,1}&=\frac{(-1)^m}{2^{m+1}(m+1)},\\
(m+r+1)T_{m,r+1}&=\frac r2T_{m,r}.
\end{aligned}}\tag{BETA-REC}
\]
证明：积分
\[
\frac d{dx}\bigl[x^r(x-\tfrac12)^{s+1}\bigr]
=r x^{r-1}(x-\tfrac12)^{s+1}+(s+1)x^r(x-\tfrac12)^s
\]
得到左端的 \((s+r+1)U_{s,r+1}-rU_{s,r}/2\)，区间 [0,1] 的边界值是 \(2^{-(s+1)}\)；区间 [0,1/2] 两端边界为零。首项直接积分。没有素数假设或有限测试外推。

令 \(\varepsilon_r=1\ (r\le m),\ 1/3\ (m<r\le3m)\)，
\(P_1=\sum\varepsilon_rx^r\)，\(P_J=\sum\varepsilon_rJ_rx^r\)，
则**精确**：
\[
V_m=\sum_{r=1}^{3m}\varepsilon_r U_{m,r},\qquad
I_m=\sum_{r=1}^{3m}\varepsilon_r(3mU_{m-1,r}+U_{m,r}),
\]
\[
J_m^{(1)}=\sum_{r=1}^{3m}
\varepsilon_r\left(3r+\frac{p-2}{2}\right)T_{m,r},
\quad
J_m^{(2)}=\sum_{r=1}^{3m}\varepsilon_r
\left((3r-1)J_r-\frac12\right)T_{m,r}.
\tag{BETA-PORTS}
\]
每一式都仅由原积分的逐项有限多项式展开给出；二阶 \(J_r\) 来源和 r 标号保留，未把高段反射当正权重质量。

**模精度/合法性：** 模 \(p^2\) 只评估 \(\Theta_m\)，模 \(p\) 评估 \(\mathsf E_m,C_m,\chi_p\)；对 \(s=m,m-1,\ 1\le r\le3m\)，(BETA-REC) 的所有分母不超过 \(4m<p\)，且 2、3、反射 \(3r-1\)、H 的实际分母均为 p-units。不存在模环分母不可逆。低段 harmonic \(M_n\) 按支路递增，用
\(b_{n+1}/b_n=-(m-n)/(2(n+1))\) 与 \(H_a-H_{a-n}\) 的单因子更新算出，不依赖原 \(4m\) 项 Pochhammer endpoint 串流。实际观察器含带符号原支权、r/n 标识、valuation 与 p-adic digit；这是已存在 BRC 分支矩/来源保真接口的 **REUSE_APPLIED / COMPOSE_APPLIED**，不是 X6 native benchmark。

## C. 新的非零见证否证“二阶矩单独清零”的捷径

对 \(\mathsf E_m=\mathsf M_m+J_m^{(2)}-2V_m\)，使用**另一套有理数构造**（二项式展开多项式积分 + Fraction harmonic 求和，而非上述模数递推）严格得到：
\[
\begin{aligned}
m=1,\ p=7:\quad &\mathsf E_1=-649/1296\equiv2\pmod7,\\
m=2,\ p=13:\quad &\mathsf E_2=-262753327/812851200\equiv12\pmod{13},\\
m=3,\ p=19:\quad &\mathsf E_3=-1568555346923/14163119308800\equiv1\pmod{19}.
\end{aligned}\tag{NONZERO}
\]
这直接**反驳**想以 \(\mathsf E_m\equiv0\pmod p\) 独立关闭二阶项的候选策略；不是 LIFT 反例。特别地在目标子类：
\[
\begin{array}{c|rrrrrr}
p&\mathcal A_m\bmod p&\Delta_m&C_m&\mathsf E_m&\chi_p&
\mathscr D_m^\beta\\\hline
13&5&8&9&12&11&0\\
19&12&8&4&1&7&0
\end{array}
\]
例如 \(p=13\) 时 \(2^{-m}C_m\equiv12\)，与 \(\mathsf E_m=12\) 相加是 11，乘 \(\mathcal A_m=5\) 得 3，再与 \(\Delta_m=8\) 相加得 \(\chi_p=11\)。\(p=19\) 时相应两项是 10 与 1，乘 12 得 18，再加 8 得 7。**必须耦合第一位归一化 \(\Delta_m\)、全局 \(C_m\)、二阶矩、右端 Fermat quotient；任何单项置零不是合法证明。**

把目标乘以 p 可无损改写为更适合整体验证的**耦合双 digit 目标**：
\[
\boxed{\mathcal A_m\Theta_m+
p\mathcal A_m\bigl(2^{-m}C_m+\mathsf E_m\bigr)
\equiv(4/3)^{p-1}\pmod{p^2}.}\tag{JOINT}
\]
这是由已知 beta defect 严格等价变形，**仍然 OPEN，不当作已证明全素数同余**。

## D. 与既有 611 端点证书不同的实际有限证书

随附可执行脚本
research_notes/portable_direct/20261023_onhour_d25_beta_double_observer_check.py
以 (BETA-REC)、(BETA-PORTS) 和逐 n harmonic 递推独立计算 \(\Delta_m,C_m,\mathsf E_m,\chi_p\)。这个验证完全**不读取、调用、重跑原始 endpoint 流算法**。在所有 \(7\le p\le10000,\ p\equiv1\pmod6\) 的 **611 个**素数（其中 \(p\equiv13,19\pmod{24}\) 的 312 个）上，\(\mathscr D_m^\beta\equiv0\pmod p\)：611 PASS、0 FAIL；\(\mathsf E_m\not\equiv0\pmod p\)：611/611。有限结果仅为所列域的 complete arithmetic falsification，不构成任意素数全称证明，也不是 independent Driver review。

原始有序行数据使用无表头 ASCII，每行
\(p,\Delta_m,C_m,\mathsf E_m,\chi_p,\mathscr D_m^\beta\)
加换行，行序为素数升序；611 行的 SHA256：
700559f007680b9935bd406d8692f941532ed55486fb114f2a9e07f9d272e849。
见证行：13,8,9,12,11,0；19,8,4,1,7,0；9973,8025,424,3107,9702,0。
代码同时对 p=7、13、19 运行独立精确 Fraction 构造，核对 (NONZERO)。
执行环境：Python 3 标准库，整数模逆元和 fractions.Fraction，无浮点；本次已实际执行得到 PASS，不推称 Lean/native X6 通过。

## E. 接续包与权限隔离

**最高有效科学前沿：** 既有 WZ/B11 与 D25 LOW/Beta 线性消去（作者证明）不重做；本文件新增全 m 有理 Beta moment 递推以及三个严格非零 witness 和一个直接在 LOW/Beta 端而非 endpoint 的 611 素数独立计算观察器。数学状态仍为 **UNREVIEWED / NOT_ADMITTED**，既有原生实验、正式 Result、独立审阅、全素数证明均欠缺。

**最小未完科学单元：** 对 (JOINT) 的 \(\mathcal A_m\Theta_m+p\mathcal A_m(2^{-m}C_m+\mathsf E_m)\) **联合**构造 terminating contiguous-Dixon / 参数导数 / 离散 creative telescoping 证书。保留 \(n,r\) 标签和 \(p\)-赋值，寻找产生右端 \((4/3)^{p-1}\) 的边界项；绝不再试图令 \(\mathsf E_m=0\) 或重复单纯端点扫描。若仅找到部分望远镜结构，剩余算子缺陷应原样保留，按真实范围陈述。

**Native Source 与控制接续：** 当前 direct gateway em_status 0.6.11 的本站客户端认证为 sites-em-6abdec598ad48191aebece9a8232f041-ro，research_authority_granted=false、executor_binding_configured=false；不能从静态 Sites 只读材料冒认 session/CLAIM/run。原桥请求 #6186 为 Source 未验证的 ACTIVE 投影；#6187 为 PREREQUISITE_NOT_SUCCEEDED；原 dispatch #6188 的末回执为 FAILED/TimeoutExpired（不是 NO_DISPATCH），同一 target_request_id 不重发。旧会话本地 session MCP-de3e5bafb24f43f4a5e6285e7601676a 不具 Source verified role。既有 issue awdawmip/enterprise-math#1539 负责缺口修复和合法 Researcher session/continuation_prepare→claim→open 验收；不借 maintenance conversation_id，不改变三份旧中立 staging 的来源/准入。若获得真实可用自身 Researcher 权限，先从 exact continuation 核验旧 claim/frontier，再依共享合同纳入**而非自动接纳**本作者材料并完成原 native benchmark。此 GitHub 笔记和脚本是独立来源持久化，非正式 Source checkpoint。

参考的既有证据：20261023_onhour_d25_LOW_linear_harmonic_beta_shift.md；20261023_onhour_d25_endpoint_padic_stream_611.md；directed_recovery/20260926_13C1B7/sources/hourly_new/f48dfe9d-4144-4e56-9948-00a764fb3035.md。共享操作入口 docs/AUTONOMOUS_RESEARCH_OPERATIONS.zh-CN.md。未新增 scheduler、Actions、cron；原小时研究任务继续。
