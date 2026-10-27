# PREFIX-300｜C4-BRC 秩二残差的相位共轭等变定理与固定事件标签反例

**等级：AUTHOR_SIDE_EXACT_THEOREM / UNREVIEWED / NOT_ADMITTED / NATIVE_ATTRIBUTION_PENDING_BRC_REVALIDATION。** 日期：2026-10-28。作者侧研究，不是已获得 Source CLAIM 的原生执行；本轮控制端活跃任务查询返回 CONTROL_QUOTA，未验证 Owner；禁止推断正式 Result/独立 Driver 审查。

## 1. 冻结输入和精确边界

延续 PREFIX-299 的两种秩二残差 `S₄=diag(1,0,2)`、`S₇=diag(2,0,1)` 各六个 `U(3,Z[i])` 左 Port 轨道，不重做 984 轨道等历史枚举。原始 12 个代表及完整枚举的机器证据：`research_notes/research6_prefix299_rank2_left_orbits_20261027/RESULTS_PREFIX299.json`，Blob `b6acffe158f014469235f5428d2889ff43b62810`。本轮程序逐字写入六个 S₄ 代表、六个 S₇ 代表，只对映射与原分类做精确回归。

辅助来源 `a∈Q(i)^3`，四相位 `q∈{1,i,-1,-i}`，`D_q=diag(1,q,q²)`。分子矩阵
`R=[[4,4,0],[0,-4,4]]`，
`L₄=[[1,0,0],[0,0,1+i]]`，
`L₇=[[1+i,0,0],[0,0,1]]`。
定义完整 **七输出** 的带标签 C4-BRC 仪器
`F₄,q(M)=1/8 · [diag(1,conj(q)) R D_q; M D_q; L₄ D_q]`，
`F₇,q(N)=1/8 · [diag(1,conj(q)) R D_q; N D_q; L₇ D_q]`。
前两行是**有不同事件语义的** E/Ec；后三行保留三条 Port；最后两行是泄漏 Port。二元组复有理系数通过来源标识及九个有序来源路径对计算 BRC 质量，绝不把正质量当作带符号振幅抵消。

令 `T=[[0,0,1],[0,-1,0],[1,0,0]]`，`P=[[0,1],[1,0]]`。

## 2. PREFIX300-A（对全部整数高斯保留矩阵成立的相位共轭等变恒等式）

**精确定理。** 对任意 `M∈Z[i]^{3×3}` 与任意上述四相位，有
\[
\boxed{F_{4,q}(M)T=U_q F_{7,\bar q}(MT),\qquad
U_q=\operatorname{diag}(qP,q^2 I_3,q^2P).}
\]
`U_q` 是逐行单位相位加输出行置换的矩阵。证明只需精确整数高斯关系：
\[
T^2=I,\quad RT=PR,\quad L_4T=PL_7,\quad
D_q T=q^2 T D_{\bar q}.
\]
事件块需特别处理 `diag(1,conj(q))` 因子；化简给出 **`E_q T=q P E_{conj(q)}`**。保留块为 `M D_q T=q²(MT)D_{conj(q)}`；泄漏块为 `L₄D_qT=q² P L₇D_{conj(q)}`。逐块组合即得盒中恒等式。它对每个来源路径**振幅系数**成立：原来源 `0↔2`、中间来源携带一项 `-1` 相位，而不抹去或合并原来源轨迹；相应输出的来源对乘积也逐项对应。对固定旧来源 a_old=Ta_new，七个逐 Port 的质量按事件两行互换、保留三行不换、泄漏两行互换而一致；相干内积与总质量也精确保留。

使用 PREFIX-299 的 `M*M=16H−S₄`、`(MT)*(MT)=16H−S₇` 与各泄漏 Gram，获得 `F₄,q*F₄,q=F₇,q*F₇,q=I₃`。不能从 Gram 等距进一步推断在**同一固定标签**或原生操作门集下等价。

## 3. PREFIX300-B（原生可达性和未来组合的条件判据）

声明一个允许的观测集合 `\mathcal O`：标明来源身份、q 值、七个逐 Port 标签以及后续门所能读取的内部联合路径关系。上式仅给出一个**候选带标号同构**，它实际可操作，当且仅当声明的源操作允许 `a↦Ta`（含来源 1 的变号）、相位配对 `q↔\bar q`，且结果端允许事件 E/Ec 交换与泄漏 Port 交换及对应单位相位。对某个后续门/观察器 `K,O`，必要且充分的局部相等检查是
`O_old K_old U_q y=O_new K_new y` 对所有可达 `y∈im(F₇,conj(q)(MT))` 成立，并且保留相应来源标识；逐门的这种 intertwining 在兼容组合下按归纳法保持。这是一项**条件定理/类型检查**，不是对未知原生门集的实测或许可。

**固定标签的精确反例：** 取 `q=i`、新来源 `a=(1,0,0)`，相配旧来源 `Ta=(0,0,1)`。旧 `F₄,i(M)Ta` 的 E/Ec 正质量为 `(0,16)/64`；新 `F₇,-i(MT)a` 为 `(16,0)/64`。在未允许交换事件标签的观察器中，E 与 Ec 可区分，故**形式 Gram 同构不等于保留固定 E 效应**。该反例对六个代表都成立，与 M 无关。

另有 `D_iT=-T D_{-i}`，但 `D_i T` 不等于任何单一 C4 单位数乘 `T D_i`；当 q=±1 时可在固定 q 下交换。故对 q=±i **本构造的精确源系数同构必须伴随 q 共轭**；这不排除未来发现其他不同结构的变换，但排除未经证据把本 T 看成同相位可达门。

## 4. 实际验证与局限

`verify_prefix300.js` 使用安全范围内的精确整数二元组进行 Z[i] 运算（不使用浮点运算推断、π、三角函数、普通传播指数、精度拟合），逐来源生成 BRC 9 项有序路径对。六个 S₄ 代表通过 T 映至恰好六个 S₇ 左轨道；复核 108 个 Gram 条目、四相位共 504 个逐来源系数等式，并对 5184 组配对输入核验两侧共 72,576 次直接 bin 读数、653,184 项有序来源路径对、10,368 次完整质量恒等式及标签交换。实际返回数据见 `RESULTS_PREFIX300.json`，一般定理由上述解析恒等式成立，不从样本外推。

**Native 未完成：** 尚无 Source 签发的合法 `model_law_id`、Detector 门集、完整原生 Hₙ Cell/场/来源/环境/边界/测后状态接口、三维切片在原生 X6 的实际嵌入与第三分量语义、独立时间账本。因此结论严格处于**七个辅助 BRC 结果 bin 与三个辅助来源维度**，不能把它直接提升为原生六维 Cell 空间的动力学对称或真实物理可达操作。P000 是六空间轴加独立时间、原生正角 120°、没有原生二维平面，全部保持不变。

## 5. 前沿与来源

P000、ACTIVE 世界观、项目根 AGENTS、PORTABLE_RESEARCH_PROTOCOL、HEARTBEAT_BRC_ONLY_ARITHMETIC 及现行 AUTONOMOUS_RESEARCH_OPERATIONS 约束适用；本轮唯一全局读快照 `awdawmip/chatgpt-global-knowledge@7249a71c9a5c045808b7f7a4985cdaef3d849fb2`，项目科学输入 `awdawmip/enterprise-math@281ecd321ac38064822ec4b7d28ded183373923c`。原生 em_status 读到 `CANONICAL_CONTROL_ADAPTER_TRIAL / active_jobs=5/5`，任务读取 `CONTROL_QUOTA`，无法证明当前 owner/CLAIM；本轮作者侧 GitHub 记录不替代 Research Activity 原生注册/正式 Result/Driver review。

**下一单元** 见 `NEXT_PREFIX301.md`。不得重算 PREFIX-298/299 分类或把固定 E/Ec 标签的反例隐去。
