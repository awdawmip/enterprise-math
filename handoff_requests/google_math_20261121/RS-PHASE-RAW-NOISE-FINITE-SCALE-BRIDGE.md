<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PHASE-RAW-NOISE-FINITE-SCALE-BRIDGE",
  "title": "相位解码：从理想原始噪声锐半径到有限整数计数的可认证桥梁",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "DRAFT",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "理想六相位、未知平移与增益模型的任意连续窗口原始噪声锐半径已获作者侧证明和90份精确原对偶证书。原非线性整数计数模型仍缺少有效有限尺度误差界；其合法增益、平移、共同整数误差彼此耦合。",
  "next_action": "在明确的隐藏相位与已知粗尺度观察实验中，研究精确计数残差在第四差分诱导商范数下的有效控制，并据此形成有限尺度解码保证或合法整数反例。方法与研究顺序由执行者据证据选择。",
  "research_value": "把已证明的理想鲁棒性变成可实际核验的有限整数读数保证，区分足够条件、真模型锐值和观察者额外信息的作用。",
  "dependencies": [],
  "source_refs": [
    "https://github.com/awdawmip/enterprise-math/blob/ab4699ad2a80b0e040c5a5f287cd34a537d75e6f/research_notes/portable_direct/2026-11-16_google_math_continuation/joint/joint-seven-proof.md",
    "https://github.com/awdawmip/enterprise-math/blob/ab4699ad2a80b0e040c5a5f287cd34a537d75e6f/research_notes/portable_direct/2026-11-16_google_math_continuation/joint/shape-seven.md",
    "https://github.com/awdawmip/enterprise-math/blob/7ad53ff4d8168f4800fc49270b197f14defd0b4c/research_notes/portable_direct/google_clue_deepening_20261121/raw_noise/THEOREM.md",
    "https://github.com/awdawmip/enterprise-math/blob/7ad53ff4d8168f4800fc49270b197f14defd0b4c/research_notes/portable_direct/google_clue_deepening_20261121/raw_noise/verify.py",
    "https://github.com/awdawmip/enterprise-math/blob/7ad53ff4d8168f4800fc49270b197f14defd0b4c/research_notes/portable_direct/google_clue_deepening_20261121/raw_noise/certificates.json",
    "https://github.com/awdawmip/enterprise-math/blob/7ad53ff4d8168f4800fc49270b197f14defd0b4c/research_notes/portable_direct/google_clue_deepening_20261121/raw_noise/saturation_certificates.json",
    "https://github.com/awdawmip/enterprise-math/blob/7ad53ff4d8168f4800fc49270b197f14defd0b4c/research_notes/portable_direct/google_clue_deepening_20261121/raw_noise/verification.json"
  ],
  "evidence_status": "TASKBOOK_DRAFT_V2",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": ["phase-observer", "raw-noise", "finite-scale", "integer-counts"],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCHER",
  "task_authority": "PENDING_PUBLICATION",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PHASE-RAW-NOISE-FINITE-SCALE-BRIDGE",
  "parent_objective_id": "OBJ-GOOGLE-20261116-ERDOS1063-SEVEN-PHASE",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null
}
-->

# 相位解码：有限整数计数与原始噪声的有效桥梁

## 已有结果与本题问题

本轮已证明：对理想观测 `A S_a+B·1+H_n w`，`B` 任意、`g>0`，原始逐位置误差满足 `||w||∞≤ε` 时，正增益 `A≥g` 的锐半径在七点为 `3g`、八点及以后为 `15g/4`；符号未知 `|A|≥g` 的锐半径在七点为 `15g/8`、八点为 `3g`、九点及以后为 `10g/3`。严格小于相应半径时统一唯一解码；等号处存在精确的原始噪声碰撞。原始七/八点常数问题及其任意连续窗口扩展已经完成。

本题研究：原五来源非线性整数计数在有限尺度上，何时能以可计算的误差裕度使用这些结果？精确模型将增益、平移及整数共同误差联系在一起，应保留这种联系来判断实际可分性。研究对象为现有心跳世界X6下的有序采样辅助观察器；当前观察任务是识别窗口相位，保留共同误差、相位与采样次序的类型。

## 冻结的观察实验与合法候选

采用以下明确实验，使相位确实未知而粗尺度可用。

给解码器一个已知的正六倍数 `R=6m≥6`、窗口长度 `n≥7`、有序偏移 `j=0,…,n−1`、误差预算及下述模型。真实起点是六个候选之一 `r_a=R+a`，`a∈{0,…,5}`。解码器收到本节定义的差分读数；实际起点 `r_a`、逐位置绝对索引 `r_a+j` 及相位标签不作为额外数据提供。读数生成端按真实内部索引实施规定的预处理；这是明确指定的测量映射，不赋予解码器该索引。研究者如采用其他信息条件，应单独命名观察实验并证明与本题的对应关系。

原计数的精确定义为

\[
\sum_{q\ge0}C(q)z^q=\frac{z}{(1-z)^3(1-z^2)(1-z^3)(1-z^6)},\qquad
\sum_{q\ge0}T(q)z^q=\frac{z^2}{(1-z)^4(1-z^2)(1-z^3)(1-z^6)}.
\]

置

\[
Q(q)=q^4/6+q^3/2-115q^2/36+115q/6-16315/108,
\]

对候选起点 `r_a` 和候选共同整数误差 `(e,d)`，定义

\[
Y_{a,e,d,j}=\frac{(r_a+j)^3[T(r_a+j)+e]}{C(r_a+j)+d}-Q(r_a+j).
\]

`H_n` 为 `n−4` 行、`n` 列的相邻四阶差分矩阵，非零行模板为 `(1,−4,6,−4,1)`。实际收到

\[
z=H_n(Y_{a,e,d}+w),\qquad |w_j|\le\varepsilon.
\]

这里的 `w` 是施加在差分前各个 `Y` 读数上的任意加性误差，没有概率分布假设；它不同于作用在计数 `C,T` 中、在窗口内共同使用的整数 `d,e`。各相位候选可有自己的合法 `(e,d,w)`；不能要求两个竞争解释共享未知误差。

给定精确声明的有理参数 `L≥0`、`0≤δ<1`、`η>0`。候选共同误差域由

\[
E=25920e/r_a^6,\quad D=4320d/r_a^5,\quad |E|\le L,\quad |D|\le\delta
\]

以及正增益域 `1+E≥η` 或符号未知域 `|1+E|≥η` 决定。所有候选均须满足窗口内实际分母 `C(r_a+j)+d>0`。每个有限 `R` 下这些是有界整数候选集；空候选集据实处理。上述远离消去面的条件服务于当前有限尺度桥梁；`E≈−1` 的消去层由另一研究问题处理。

## 残差、范数及可用桥梁

保留六周期模板 `G=(20,20,20,−100,140,−100)`，并令

`S_a=(G_a,…,G_(a+n−5))`，下标模六。

已有渐近模型给出

\[
A(E,D)=\frac{1+E}{(1+D)^2},
\]

\[
B(E,D)=-\frac{4[D^5-121D^4+70D^3E+381D^3-365D^2E-121D^2+185DE+D-5E]}{(1+D)^5}.
\]

在合法候选上定义精确差分残差

\[
\mathcal R_{a,e,d}=H_nY_{a,e,d}-A(E,D)S_a-B(E,D)\mathbf1.
\]

`H_n` 满行秩，可使用原始误差在输出空间诱导的范数

\[
\kappa_n(v)=\min\{\|h\|_\infty:H_nh=v\},
\]

以及共同平移商上的范数

\[
\bar\kappa_n([v])=\min_{b\in\mathbb R}\kappa_n(v-b\mathbf1).
\]

后一个商的使用范围是向任意平移的理想相位族转移**充分解码保证**；原始完整差分读数仍保留。精确计数模型的 `B` 与其他参数存在关系，判断实际锐值或信息损失时应使用相应完整观测，或明确声明另一个确实丢弃平移的读数通道。

一个有意义的桥梁结果是给出可计算的统一上界

\[
\bar\kappa_n([\mathcal R_{a,e,d}])\le\rho_n(R;L,\delta,\eta)
\]

及其成立的显式尺度条件。可采用有效的 `C/R` 界、可核验的精确区间界、带合法参数覆盖证书的有限尺度算法，或其他等价证据。仅重述没有常数的 `O(1/r)` 不能完成本题。

例如，取 `g=η/(1+δ)^2`，若上述统一界成立，则

\[
\varepsilon+\rho_n(R;L,\delta,\eta)<g\,r_n
\]

是一个应验证的充分解码条件；`r_n` 取已有定理中对应模式的单位增益半径。允许使用相位对各自的更强界。此不等式是理想族包络导出的保证，不能直接作为精确整数模型的必要条件或锐值。

## 目标与验收

交付应回答一个有实际增量的有限尺度问题，并保留完整假设和可复算证据。可接受的成果包括：

- 在明确非空参数域、窗口长度及尺度范围内，给出显式残差界和可执行的认证解码条件；说明候选覆盖、整数计算及误差范数，展示合法整数起点的复算。
- 对精确整数模型给出比理想族包络更强的可分条件，并明确利用了何种增益、平移或整数耦合信息。
- 对一个具体拟议保证给出精确反例或有证明的障碍。原始读数碰撞应列出同一已知粗块 `R` 下两个不同的合法整数起点、各自的整数 `(e,d)`，以及使读数相同的噪声见证和其最大范数；不能用同一整数起点的两个虚构余数分支代替。
- 若给出真模型锐半径，应同时证明相应全部合法候选的分离下界与达到边界的合法碰撞。仅有部分范围或上下界时，明确剩余差距及哪些结论已经可用于解码。

交回模型、论证、有效参数/尺度条件、计算或代数证书及复算入口。七、八、九点分别对应已有理想定理的结构转折，可据实际问题选取或扩展；改变窗口长度时写明常数对 `n` 的依赖。研究者自主选择推导、估计、精确计算和反例构造的方法，无预设思维步骤或规定工具顺序。

完成状态据本题实际目标判定；理想模型的作者侧证明、当前有限尺度成果、独立审查和项目接纳分别记录。新结果保留原作者 EM-DIRECT-3DCA45 的计数模型贡献，并引用本轮原始噪声定理的实际发布版本。本草案已绑定实际保存和回读的固定科研来源；本文件不生成父目标代次或正式任务记录。
