# D25 / LIFT：模 p³ 观察器的精度隔离与 p⁴ 锐性反例

- **状态**：AUTHOR_EXACT_PROJECTION_PROOF / TWO_EXACT_TARGET_CLASS_WITNESSES / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NO_FORMAL_CLAIM / NOT_NATIVE_BENCHMARK。
- **来源**：真实 TASK_RESEARCH 作者材料，Research 逻辑 lane \`chatgpt-research-onhour-enterprise-math-20260923\`（仅供溯源，非 Source 所有权凭据）；本轮已暴露 D25、LOW、B11 历史，不能作独立审阅。
- **母任务**：RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT；已发布 Task TP2-B6F4FC938FF94941C1B7；原 Taskbook blob 53a3ef039325534e3715add837f0eee332289984，当前 Source 读 head 于本轮写前为 3102dc08dcc1fe649de542367409bfb98bd77025。历史 D25 frozen Source pin 与当前控制 main 不混同，不能因此更新任何冻结输入。
- **已有且不重证的科学前沿**：来自 research_notes/directed_recovery/20260926_13C1B7/sources/hourly_new/fb9aba8a-6fb9-411b-920b-9bb376d16cd5.md 与 f48dfe9d-4144-4e56-9948-00a764fb3035.md 的 WZ/B11 first digit、two-band LOW、Beta adjoint、单一 LOW observer；研究笔记 research_notes/portable_direct/20261023_onhour_d25_B11_normal_second_jet_p3.md 中的 N/T 二阶法向公式仍是各自声明范围内的作者代数，不是终局 LIFT。
- **GLOBAL_KNOWLEDGE_V1**：本轮验证 canonical main@90248aab307c325e45690bb2bc147e483a18734b；P000 ACTIVE_LOCKED，世界观 ACTIVE。所用有理数/p-adic 算术是外部辅助证明，不是 X6 运动学或原生 benchmark。

## 1. 新的必要精度隔离定理：在实际 WZ 链中 B11 的高法向喷流不可影响 LIFT 的模 p³ 目标

已经得到的精确接续为
\[
W_p\equiv S_{4m}(2m)-p^2D_p\pmod{p^3},\qquad p=6m+1,
\]
而第一 digit 的已完成 B11/interval 链给出
\[
D_p\equiv\chi_p:=2q_p(2)-q_p(3)
=\frac{(4/3)^{p-1}-1}{p}\pmod p.
\]
因此对任意满足条件的素数，直接由 p-adic filtration 得到
\[
p^2(D_p-\chi_p)\in p^3\mathbf Z_{(p)}.
\]
这里 \(\chi_p\) 表示选定的 p-integral lift，例如最后一项的有理数。于是原问题的真正剩余目标严格等价于
\[
\boxed{S_{4m}(2m)\equiv p(4/3)^{p-1}\pmod{p^3}.}\tag{EP}
\]
这不是对 EP 的证明，而是对现有 accepted first digit + portable WZ 公式的逐步精度投影；不把 WZ 证据冒充新发现。

把 B11 的 \(S_m=C_m+(p/3)N_m+(p^2/18)T_m+O(p^3)\) 在其自身接口内展开，允许其 \(D_p\) 中出现 p 倍或 p² 倍的高 jet 校正时，乘以 WZ 的外部 \(p^2\) 后，这些项分别至少属于 \(p^3\)、\(p^4\)。**所以在当前 WZ→EP 路径下，B11 的 N/T 高 jet 不属于本轮模 p³ LIFT 的必需缺项。** 这条“零传递”结论只限于上述带外部 \(p^2\) 的接口；如其他冻结 source 证明存在独立不带该因子的 LOW 耦合，须另行审查，不能把零传递推广到所有可能的路径。

## 2. 两个目标 residue class 的完全有理精确证书：p³ 成立，但 p⁴ 均不成立

采用之前已经发表的原 endpoint 定义
\[
\mathcal A_m=\frac{(p-1)!}{3^{p-1}(2m)!^3},\quad
S_{4m}(2m)=\mathcal A_m
\sum_{n=0}^{4m}\frac{(2m+\frac12)_n(\frac13)_n(\frac23)_n}
{n!(2m+1)_n(4m+1)_n}\,\frac{6n+2p-1}{2^n}.
\]
直接在 \(\mathbf Q\) 中逐项精确构造（没有浮点近似），取得：
\[
p=13,\quad m=2,\quad
S_8(4)=\frac{12854999453611128788975}{7772129990182032113664};
\]
\[
p=19,\quad m=3,\quad
S_{12}(6)=
\frac{1274954291994799670874173419390525}
{770837094750179348605289078194176}.
\]
分母均为对应 p-单位。将目标 \(B_p=p(4/3)^{p-1}\) 单独按模 \(p^4\) 计算：

| p (class mod 24) | \(S\bmod p^4\) | \(B_p\bmod p^4\) | \(S-B_p\bmod p^4\) | \((S-B_p)/p^3\bmod p\) | \((S-p)/p^2\bmod p\) |
| --- | ---: | ---: | ---: | ---: | ---: |
| 13 (13) | 19448 | 21645 | 26364 = \(12\cdot13^3\) | 12 | 11 |
| 19 (19) | 23123 | 98572 | 54872 = \(8\cdot19^3\) | 8 | 7 |

因此 EP 在上述两个确切目标素数上模 \(p^3\) 成立，而 **普遍把 EP 无条件强化到模 \(p^4\) 是错误命题**，两个 residue class 各有一份精确反例。这个锐性结论在原模 \(p^3\) LIFT 之外，不是对 LIFT 的否证。

**独立构造核对**：一条算法使用普通 Pochhammer 有理递推（每次用 \(n-1\) 到 \(n\) 的有理项比率），另一条将每个上升阶乘拆成完全独立的整数积
\[
\frac{(2m+\frac12)_n(\frac13)_n(\frac23)_n}{2^n}
=\frac{\prod_{k=0}^{n-1}(4m+1+2k)(3k+1)(3k+2)}{36^n}
\]
并把 denominator 的 \((2m+1)_n,(4m+1)_n\) 各用整数阶乘比重建。Python Fraction 两条算法所得的完整精确分数在 p=7,13,19,31,37 全部相等；上表两目标素数的有理分数、全部模剩余和 p-赋值由第一算法逐项读出并经第二构造对照。无运行的 native benchmark、Lean、独立审阅均不得当作通过；未作全素数模 p³ 证明，五个输入仅为确定性核验。

## 3. 第二位观察器不可混同：一个模 19 的明示来源反例

前轮 B11 的二阶法向源量定义为
\[
T_m=\sum_{j=0}^{m}w_j(H_j^2+E_j),
\quad w_j=\frac{(-m)_j}{(m+\frac23)_j}\frac{-1/3}{j-1/3},
\quad H_j=\sum_{\ell=0}^{j-1}(m+\tfrac23+\ell)^{-1},
\quad E_j=\sum_{\ell=0}^{j-1}(m+\tfrac23+\ell)^{-2}.
\]
在 \(p=19,m=3\)，精确有理计算给出
\[
T_3=\frac{7242533433}{179435730320},\quad
T_3/18\equiv 9\pmod{19},\quad
\chi_{19}=7\pmod{19}.
\]
因此 **\(T_m/18\equiv\chi_p\pmod p\)** 这个未经证明的观察器等同命题已有明确反例（19），尽管在 p=13 碰巧都读成 11。反例不排除含额外 LOW 校正项的耦合，也不影响此前 B11 Taylor 定理。它恰好说明保留 BRC 的源标签（B11-normal-jet / endpoint-second-digit）、观测层与前置 \(p^2\) 因子是必要的：将两个“第二位”字样压成单个无来源数是信息损失。

## 4. 科研状态与下一最小动作

- **母问题**：冻结 D=-24 first-digit UR 后，决定 LIFT/JT2 的 \(\Delta_p-R_p\bmod p\)。
- **不可变前沿及不重做**：accepted RR-AC9B3BA5BD277CE043F5 与既有 Driver 结论，原 Task TP2-B6F4FC938FF94941C1B7，已证明的 WZ 边界、B11 一位、two-band LOW、Beta adjoint；本文件只证明精度隔离、两个 p⁴ 锐性反例和上述错误 scalar identification 的 p=19 反例。
- **真正未完成项**：对 \(p\equiv13,19\pmod{24}\) 的全素数 EP / 单 LOW binomial-Beta 数学证书；未验证 Task 需要的 native run、independent review；在 Source 上没有自己的合法 checkpoint/claim/run。
- **下一精确动作**：从 f48dfe9d... 中已消去高段的 \(X_{0,m},Z_m\) 出发，证明或否证
\[
\frac{\mathcal A_mX_{0,m}-1}{p}+\mathcal A_mZ_m\equiv\chi_p\pmod p,
\]
保留特殊 \(n=m\) 支、端点系数与所有 p-单位分母。优先对已有 Beta/contiguous 低段做有来源的全 \(m\) 恒等变形，而非再次求 B11 \(N_m,T_m\) 的更高 jet 或扩大无目的素数扫描。
- **恢复/身份**：Research logical conversation ID 仍为 chatgpt-research-onhour-enterprise-math-20260923；旧 recovery Issue #6186 回执仍只显示 ACTIVE 的未核实 session 投影 MCP-de3e5bafb24f43f4a5e6285e7601676a，CLAIM/run 均无；原 continuation #6187 是 PREREQUISITE_NOT_SUCCEEDED，原 dispatch #6188 是 FAILED/TimeoutExpired；保留其原 request_id，发生新的授权/状态变化先复核原回执，不重发。旧三份 staging 经先前 preserve manifest 中立保全，保持独立、未并入 Result。Site-only readonly 令本轮不能声称 Source-native 角色写权限。
- **本文件地位**：经 GitHub 连接中立保全的独立作者材料；不代表 TASK publication、Source checkpoint、Result、freeze、owner、native benchmark 或独立审阅。正式 Source admission 待合法会话和当前 Selector 续接。

BRC / 残差类型：保留 p 的 13/19 两支、\(n\) 与 \(j\) 支路、p-valuation、两个不同观察器及先乘 \(p^2\) 后投影的操作顺序；带符号有理数的抵消不是非负质量抵消；没有改变 P000 或 Heartbeat World 的六维原生语义。
