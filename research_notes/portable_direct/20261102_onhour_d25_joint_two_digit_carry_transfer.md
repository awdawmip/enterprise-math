# D25: 原始216—2304双流的两位进位与共同中廊传递（2026-11-02）

**AUTHOR-DERIVED / PROVED ALL-PRIME LOCAL LEMMA / EXACT FINITE CHECK / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_EXPERIMENT。**
这是作者侧中立数学保全，不是正式 Source checkpoint、Researcher CLAIM、Result 或数学接纳。

- 母 Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT
- publication: TP2-B6F4FC938FF94941C1B7
- 冻结科学 Source: c47e13e4aba0e006366f989d6334d443f6333ae3
- 母目标：对全部 p≡13,19 (mod24) 的原始 Delta_p−R_p≡0 (modp) 或原定义反例；不重做已接纳 D24 UR。
- 本文 p-进位与算术指标是**外部辅助坐标**，不声称它们是 P000 原生心跳世界 X6 空间坐标。

## 1. 全素数逐项传递（严格命题）

对素数 p>3，h=(p−1)/2；对任意 k≥0 在 Z_(p) 内保留原始加权项

\[
w_k=(6k+1)\frac{(2k)!(3k)!}{216^k(k!)^5},\qquad
s_k=(8k+1)\frac{(4k)!}{2304^k(k!)^4}.
\]

**定理**：对于每个整数 h<b<p，逐项有

\[
\boxed{w_{hp+b}\equiv p^2\Bigl(\frac6p\Bigr)w_b\pmod{p^5}},
\qquad
\boxed{s_{hp+b}\equiv p^2s_b\pmod{p^5}}.\tag{1}
\]

其中 (6/p) 为 Legendre 符号，两个阶乘比为整数，p>3 时两个幂分母都是 p-单位。

证明：记 A_k=(2k)!(3k)!/(k!)⁵ 和 B_k=(4k)!/(k!)⁴，v 为 p-进赋值。对 h<b<p 用 Legendre 阶乘公式得

\[
v_p(A_{hp+b})=v_p(A_b)+2,\quad
v_p(B_{hp+b})=v_p(B_b)+2.
\]

这是低位 b 的赋值与第 h 个高位的赋值，加上从 b 进入下一位的进位之和；其中 v(A_h)=v(B_h)=1，A 的附加进位为 (δ₂,δ₃)=(1,0)，B 的附加进位 δ₄=1。

若 v_p(A_b)=2，则 \(\lfloor2b/p\rfloor=\lfloor3b/p\rfloor=1\)。把 n! 的 p-自由单位记为 U(n!)=n!/p^{v_p(n!)}，按 p 位逐层使用 Wilson，有

\[
U(n!)\equiv(-1)^{v_p(n!)}\prod_i(n_i!)\pmod p
\]

（n_i 是 n 的 p 进制数字）。对于 A 的比 U(A_{hp+b})/U(A_b)，新出现的高位阶乘恰为 h!、分母增加 (h!)⁵，故比值为 (h!)⁻⁴ modp；对于 B 的 v_p(B_b)=2 区域，新增高位 2! 被旧低位 2! 抵消，其余同样为 (h!)⁻⁴。

Wilson: \((p-1)!\equiv(-1)^h(h!)^2\equiv-1\pmod p\)，因此 (h!)⁴≡1 modp。权重 \((6(hp+b)+1)/(6b+1)\) 或 \((8(hp+b)+1)/(8b+1)\) 在需要的单位区域模p为1；分母比 216^{-hp}≡216^{-h}=(6/p)，2304^{-hp}≡2304^{-h}=1，因为 216=6³、2304=48²。

对于原始 b 的赋值达到3的尾段，左右两侧自动被 p⁵ 整除。故两个同余对每个 b>h 均成立。这里无需任何 Dwork 假设。

**有符号共同中廊**：两式相减后在相同原始 b 指标上求和。定义

\[
T_W(p)=\frac1{p^2}\sum_{b=h+1}^{p-1}w_b\pmod p,\qquad
T_S(p)=\frac1{p^2}\sum_{b=h+1}^{p-1}s_b\pmod p.
\]

直接有

\[
\sum_{b>h}(w_{hp+b}-2s_{hp+b})
\equiv p^4\bigl((6/p)T_W(p)-2T_S(p)\bigr)\pmod{p^5}.\tag{2}
\]

Guo–Zudilin 已证明 2304 模型全、半截断在模 p³ 相同，对全部 p>3 成立，因此 T_S(p)=0；复用其既有定理而非重新认领，得到

\[
\boxed{\sum_{b>h}(w_{hp+b}-2s_{hp+b})
\equiv p^4(6/p)T_W(p)\pmod{p^5}.}\tag{3}
\]

来源：V. J. W. Guo, W. Zudilin, *A q-microscope for supercongruences*, Advances in Mathematics 346 (2019), 329–358, DOI 10.1016/j.aim.2019.02.008；该文包含 2304 模型 \(S(p-1)\equiv S((p-1)/2)\equiv p(-3/p)\pmod{p^3}\)。

## 2. 全部 p² 个指标的两位进位来源

对于 0≤a,b<p，k=ap+b，m=2,3,4，记

\[
c_m=\lfloor mb/p\rfloor,\quad
q_m=\lfloor(ma+c_m)/p\rfloor,\quad
r_m=(ma+c_m)\bmod p,\quad t_m=mb\bmod p,
\]
\[
\delta_m=q_m-\lfloor ma/p\rfloor\in\{0,1\}.
\]

有准确的跨数字赋值关系

\[
v_p(A_{ap+b})=v_p(A_a)+v_p(A_b)+\delta_2+\delta_3,\quad
v_p(B_{ap+b})=v_p(B_a)+v_p(B_b)+\delta_4.\tag{4}
\]

进一步以 U(X)=X/p^{v_p(X)} 为单位读出，完全明确：

\[
\boxed{U(A_{ap+b})\equiv(-1)^{v_p(A_{ap+b})}
\frac{t_2!r_2!q_2!\ t_3!r_3!q_3!}{(a!b!)^5}\pmod p},
\]
\[
\boxed{U(B_{ap+b})\equiv(-1)^{v_p(B_{ap+b})}
\frac{t_4!r_4!q_4!}{(a!b!)^4}\pmod p}.\tag{5}
\]

因为 p≥5 时 4(p²−1)<p³，以上分位单位公式已包含全部非零高位。原始 w,s 项再乘各自带符号权重和 216^{-k},2304^{-k}；这些方向不能在尚未证明完整有符号观察者等价前商掉。

若 p=6m+1，A 的额外进位仅出现在三行 a=2m、3m、4m，b 下限分别 2m+1、3m+1、4m+1，长度 4m,3m,2m。B 的三行满足 4a modp=p−1,p−2,p−3；与 A 仅重合在 a=h=3m、b>h。因此 p² 项被严格分为 **共同行 h=(p−1)/2 项、A-only p−1 项、B-only p−1 项、none p²−5(p−1)/2 项**。共同中廊不能代替另外三个带符号来源。

## 3. 可复现的原始有限证书

本轮实际运行 Python 标准库逐指标计算 p=13,19,37,373 的所有 k<p²，共 141028 个 k；每个 k 同时检验两个模型的阶乘 p 赋值、p-自由单位公式、完整原始权重与分母。再按四个来源分组计算 W₂−2S₂ modp⁶；中廊各项与 (1) 模 p⁵ 核对，完整 W₂/S₂ 与此前独立 p² 原始求和结果交叉一致。

| p | 共同进位项 | W-only | S-only | 共同中廊的 p⁴ 数字 | T_W | T_S |
|---:|---:|---:|---:|---:|---:|---:|
| 13 | 6 | 12 | 12 | 3 | 10 | 0 |
| 19 | 9 | 18 | 18 | 9 | 9 | 0 |
| 37 | 18 | 36 | 36 | 17 | 20 | 0 |
| **373** | **186** | **372** | **372** | **107** | **266** | **0** |

固定373：\((6/373)=-1\)，因此共同中廊的非零 p⁴ 数字 **107≡−266(mod373)** 来自原始216尾项。完整双流的 p² 尺度残差则为 \(E_2=W_2−2S_2+373²\)，实际 \(v_{373}(E_2)=5\)，\(E_2/373^5\equiv174\pmod{373}\)；它是所有来源相消的结果，不等于中廊107。

另外在 p=5,7,11,17,29,31,43,67 的全部共同中廊也逐项核对 (1)。有限测试是实现与固定值证书，不作为全素数定理的代替。

完整作者侧 proof + exact runner + check JSON + machine continuation 见 2026-11-02 同轮附件 d25_joint_two_digit_carry_20261102_author_side.zip。当前文件为 GitHub 可回读的作者侧来源；正式 Source 接纳另有 gate。

## 4. 未完项和正确接续

**最高科学目标仍开放**：原始 \(\Delta_p-R_p\equiv0\pmod p\)，p≡13,19 mod24。全尺度 Dwork 的各模型 \(W_2\equiv\chi_ppW_1,S_2\equiv\chi_ppS_1\pmod{p^6}\) 尚未由本定理推出。**下一精确动作**：在 (4) 的 W-only、S-only 行构造有符号分块望远镜或 WZ 证书，联合 none 组与当前共同中廊，检验完整 Dwork 条件后直接回归原始 Δ−R；若不存在这种抵消，保留一个确切失败项/反例而不重复辅助理论。

**原生固定373实验**：支持事项 awdawmip/enterprise-math#1559（2026-11-02 核验 OPEN、无人指派）仍需真正 H0/B0 divided-power 同原始类 [X]U mod139129、模块秩、半线性 Frobenius 方向与 eta、带符号 odd Green/Hesse、kappa 和独立复核；本轮的139129项原始加权**标量**不替代 native operator。责任路径为该支持单所列合法 Source owner/原生执行者或指定实现维护者，未验证有人接手：PENDING_OWNER / NOT_EXECUTED。

**控制与身份**：本轮 Gateway v0.6.11 是 Site static read-only，research_authority_granted=false、executor_binding_configured=false、UPSTREAM_CODE_REVIEW_REQUIRED，jobs 5/5。旧 research-onhour-20261031-0205-dispatch-r15 已在 kimi-query-bridge#6633 终局 FAILED，不重发。自身未取得可核实的 Source Researcher session/claim/run；新增是**作者侧 GitHub 保全**，非 Source checkpoint、Research Activity、review。研究 lane chatgpt-research-onhour-enterprise-math-20260923 与 maintenance chatgpt-hourly-enterprise-math-20260921 严格隔离。原定时任务不变。
