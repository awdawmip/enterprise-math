# D25 — 原始216—2304双流的素数幂尺度残差（2026-11-02）

**状态：AUTHOR-DERIVED / PROVED CONDITIONAL LEMMA + EXACT FINITE CHECK / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_EXPERIMENT。** 本文仅作作者侧数学证据，未取得正式Source checkpoint/Result/Review。

母任务：RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT；不可变publication TP2-B6F4FC938FF94941C1B7；冻结科学pin c47e13e4aba0e006366f989d6334d443f6333ae3。母目标仍为对**全部**p≡13,19(mod24)证明原始Δ_p=(G_p h_p−1)/p≡R_p(modp)，或给出原定义反例。D24 UR已接纳，不重新证明。

## 精确原始输入与带符号观察量

对素数p>3、r≥1，使用原始加权整数二项式完整截断（0≤k<p^r）：

$$
W_r=\sum_{k=0}^{p^r-1}(6k+1)\frac{\binom{2k}{k}^2\binom{3k}{k}}{216^k},
\quad
S_r=\sum_{k=0}^{p^r-1}(8k+1)\frac{\binom{2k}{k}^2\binom{4k}{2k}}{2304^k}.
$$

χ_p=+1若p≡1(mod3)，否则χ_p=−1。定义 E_r=W_r−2S_r+χ_p^r p^r。这一BRC保真观察保留两个原始加权来源、相减的符号、χ_p^r、p进赋值以及E_r/p^{r+3}模p；仅对下一次p幂截断的演化测试，不把它认作P000原生六维空间坐标。

## 已严格证明的条件传递定理

设在每个2≤j≤r，**假设**原始模型分别满足Dwork型同余：

$$
W_j\equiv\chi_p pW_{j-1}\pmod{p^{3j}},\qquad
S_j\equiv\chi_p pS_{j-1}\pmod{p^{3j}}. \tag{D_j}
$$

保留χ_p²=1，逐项相减立即严格得到

$$
E_j-\chi_p pE_{j-1}
=(W_j-\chi_p pW_{j-1})-2(S_j-\chi_p pS_{j-1})
\equiv0\pmod{p^{3j}}.
$$

若另有基本层级E_1≡0(mod p⁴)，则归纳证明：

$$
\boxed{E_r\equiv0\pmod{p^{r+3}},\qquad
E_r/p^{r+3}\equiv\chi_p^{r-1}(E_1/p^4)\pmod p.}
$$

证明：前层赋值至少r+2，所以χ_p pE_{r−1}赋值至少r+3；D_j误差赋值至少3r≥r+4（r≥2），故不仅得到整除性，除以p^{r+3}后误差模p消失，首位乘χ_p。重复归纳即可。**此定理是全p、r的条件蕴含，不是全部D_j或E_1同余的无条件证明。**

## 新完成的原始素数幂有限证书

实际执行Python纯整数、无浮点运算。覆盖21个素数：
5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,109,139,211,373。
每个包含r=1,2；另p=5检验至r=5，p=7/11/13至r=4，p=19至r=3；**52个完整(p,r)原始求和证书及31组独立相邻尺度Dwork测试**。每组按N=max(8,3r_max+2)精确计算模p^N。所有测试点满足指定的两条D_j、基本层第四位及有符号首数字传递。p≤43且r≤2的24个完整输入，另用原始math.comb整数求和双实现独立交叉验证。

原始整数分子 A_k=(2k)!(3k)!/(k!)⁵、B_k=(4k)!/(k!)⁴；带权项分别为(6k+1)A_k/216^k、(8k+1)B_k/2304^k。二者递推比分别为

$$
a_{k+1}/a_k=(2k+1)(3k+1)(3k+2)/(36(k+1)^3),
\quad b_{k+1}/b_k=(4k+1)(2k+1)(4k+3)/(288(k+1)^3).
$$

程序逐因子剥离p进赋值、以单位模p^N取逆并跟踪整系数，不对k≥p时不可逆的(k+1)直接取模逆。由此所有p²截断均是真实原始和，而不是从小截断结果推算。

| p | χ_p | E₁/p⁴(mod p) | E₂/p⁵(mod p) | v_p(E₂) | 最大检查层级 |
|---:|---:|---:|---:|---:|---:|
| 11 | −1 | 5 | 6 | 5 | r=4，首数字6 |
| **13** | +1 | **9** | **9** | **5** | r=4，首数字9 |
| **19** | +1 | **14** | **14** | **5** | r=3，首数字14 |
| 37 | +1 | 26 | 26 | 5 | r=2 |
| 109 | +1 | 61 | 61 | 5 | r=2 |
| **373** | +1 | **174** | **174** | **5** | r=2 |

固定p=373的**完整原始**加权双流在截断p²=139129时精确满足

$$
v_{373}(W_{373^2}-2S_{373^2}+373^2)=5,\qquad
(W_{373^2}-2S_{373^2}+373^2)/373^5\equiv174\pmod{373}.
$$

对于p=13，r=1,2,3,4的E_r赋值依次4,5,6,7。这是实际跨尺度残差的来源保真信息：在这些有限例子中，原始第四位桥接沿层级增长一位而非4r位；不排除其他有修正的传输机制。p=5/7的首数字为零，其更高赋值单独保留。

复现源：本轮提供附件 d25_signed_dwork_scale_transport_20261102.py（完整程序、单位/赋值更新、原始math.comb校验）及 d25_signed_dwork_scale_transport_20261102.check.json（52个原始精确记录）。程序定义的有序证据摘要SHA256：ee55f8f6dd037a4aad594f9af98c9c48bd230546a29ca2109e240ccf33aca46c。此摘要是数据完整性标识，不替代数学审核。

## 精确接续、真实欠项和控制状态

最高母目标仍为Δ_p−R_p≡0(modp)，对全部p≡13,19(mod24)。当前新信息是可检验的带符号跨尺度传递；Dwork的全部素数层级假设和原始基本层统一同余**尚需证明**。下一精确科学动作：构造联合原始加权WZ/Dwork block或直接带符号Clausen证书，证明两个模型p²→p的p⁶误差及母目标实际要求；不可用PF端点齐次性冒充Dwork证明。复用已完成428素数r=1证书、PF端点、可逆加权连接和D24 UR，不重复其证明。

独立固定373原生H0/B0 divided-power实验仍由已有Issue #1559接续，**PENDING_OWNER / NOT_EXECUTED**：原始同类[X]U模139129、秩、半线性Frobenius方向/η、奇Green/Hesse、κ及独立复核欠缺。此次n=139129加权标量求和与原生H0/B0算子不同，不可替代。

Gateway 0.6.11在本轮显示research_authority_granted=false、executor_binding_configured=false、control jobs 5/5。exact continuation返回CONTROL_QUOTA，自身client checkpoint读取ACCESS_DENIED；没有取得合法Researcher session、claim/run或Source checkpoint。旧请求research-onhour-20261031-0205-dispatch-r15的原回执已终结FAILED/UPSTREAM_CODE_REVIEW_REQUIRED，未重复提交。正式Source仍REGISTER_PENDING/SYNC_DEBT，本GitHub文件只持久化作者侧证据。冻结pin/P000/ACTIVE世界观不变。Research lane chatgpt-research-onhour-enterprise-math-20260923与maintenance chatgpt-hourly-enterprise-math-20260921严格分离。原定时和通知未修改。

既有frontier：research_notes/portable_direct/20261102_onhour_d25_two_stream_fourth_digit_finite_certificate.md（r=1有限证书）；research_notes/portable_direct/20261102_onhour_d25_full_period_pf_endpoint_all_r.md（PF端点）；research_notes/portable_direct/20261102_onhour_d25_weighted_gauged_pf_endpoint.md（双模型加权连接）。
