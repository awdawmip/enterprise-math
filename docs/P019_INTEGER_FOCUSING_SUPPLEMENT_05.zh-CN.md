# P019 —— 整数聚焦补充 05：有限聚焦、相对 expansion 与 branch-clock 候选

状态：`ACTIVE RESEARCH NOTE / EXTERNAL-COMPARISON GATE OPEN`  
依赖：P011 collision spectrum、P019 Directed Expansion Supplement 03  
范围：从 `Xi=B-C` 推导纯整数有限聚焦定理与无分数的 relative-expansion ordering  
纪律：本文不是 Raychaudhuri 方程的离散化证明；只构造可与其做结构比较的整数定理。

## 1. 起点

对有限 directed primitive graph 的非空截面 `A`，P019-D 已证明

\[
\Xi(A)=|F(A)|-|A|=B(A)-C(A),
\]

其中：

- `B(A)` 是 outgoing branching surplus；
- `C(A)` 是 multiple outgoing incidences 合流到相同 future target 所产生的 collision/focusing excess。

定义 **focusing margin**：

\[
\boxed{M(A)=C(A)-B(A)=-\Xi(A).}
\]

于是：

\[
M<0 \iff \Xi>0,
\qquad
M=0 \iff \Xi=0,
\qquad
M>0 \iff \Xi<0.
\]

## 2. P019-F-T01 —— 严格 collision domination 等价于严格截面收缩

状态：`PROVED`

对任意正整数 `q`：

\[
\boxed{C(A)\ge B(A)+q}
\]

当且仅当

\[
\boxed{\Xi(A)\le-q.}
\]

因此下一截面满足

\[
\boxed{|F(A)|\le |A|-q.}
\]

这是 `Xi=B-C` 的直接整数推论，但它把“聚焦条件”从符号语言提升成精确 cardinality 降幅。

## 3. P019-F-T02 —— 有限聚焦定理

状态：`PROVED`

令

\[
A_{t+1}=F(A_t)
\]

并假设：只要 `A_t` 非空，就存在固定正整数 `q` 使

\[
C(A_t)\ge B(A_t)+q.
\]

由 T01：

\[
|A_{t+1}|\le|A_t|-q.
\]

迭代得到

\[
|A_t|\le |A_0|-tq.
\]

由于 cardinality 不能为负，未来截面最迟在

\[
\boxed{
T_*
\le
\left\lceil\frac{|A_0|}{q}\right\rceil
}
\]

步内变为空集。

内部不需要有理数 ceiling；可写成纯整数：

\[
\boxed{
T_*
\le
(|A_0|+q-1)//q.
}
\]

特别当

\[
C(A_t)\ge B(A_t)+1
\]

在所有非空步持续成立时：

\[
\boxed{T_*\le|A_0|.}
\]

这是一条真正的 finite focusing theorem：持续的 collision domination 强迫有限步 extinction，而不是只说“趋向收敛”。

它是有限组合定理，不需要 affine parameter、微分方程或连续极限。

## 4. 与外部 focusing theorem 的边界

经典 GR 中，Raychaudhuri equation 描述 geodesic congruence expansion 的演化；在适当条件下可导出有限 affine/proper-time 内的 focusing/conjugate-point 结论。

P019-F-T02 只在**逻辑形状**上相似：

`持续的负 expansion/focusing condition -> finite focusing`。

它没有推导：

- continuum expansion scalar；
- shear/vorticity；
- Ricci tensor；
- energy condition；
- conjugate point；
- Einstein dynamics。

因此当前可称为 **integer finite-focusing theorem**，不得称为“离散 Raychaudhuri theorem 已完成”。

## 5. P019-F-T03 —— 无分数 relative-expansion change numerator

状态：`PROVED`

令

\[
N_t=|A_t|>0,
\qquad
\Xi_t=N_{t+1}-N_t.
\]

若站在外部比较层使用归一化 expansion

\[
\theta_t=\Xi_t/N_t,
\]

Enterprise Math 核心不必存储该有理数。

定义纯整数 cross-multiplied numerator：

\[
\boxed{
\mathcal R_t
=
N_t\Xi_{t+1}-N_{t+1}\Xi_t.
}
\]

由于

\[
\theta_{t+1}-\theta_t
=
\frac{\mathcal R_t}{N_tN_{t+1}},
\]

且分母严格为正，所以：

\[
\boxed{
\operatorname{sgn}(\mathcal R_t)
=
\operatorname{sgn}(\theta_{t+1}-\theta_t).
}
\]

于是：

- `R_t<0`：relative expansion 严格下降；
- `R_t=0`：relative expansion 保持；
- `R_t>0`：relative expansion 上升。

整个内部判断只需要整数乘法、减法和次序。

这与“用 cross multiplication 比较比例而不把分数变成基本状态”的 P007/P018 方法一致。

## 6. P019-F-T04 —— Relative expansion change 的 branching/collision 分解

状态：`PROVED`

由

\[
\Xi_t=B_t-C_t
\]

代入 T03：

\[
\mathcal R_t
=
N_t(B_{t+1}-C_{t+1})
-N_{t+1}(B_t-C_t).
\]

定义

\[
\boxed{
\mathcal R^B_t
=N_tB_{t+1}-N_{t+1}B_t,
}
\]

\[
\boxed{
\mathcal R^C_t
=N_tC_{t+1}-N_{t+1}C_t.
}
\]

于是：

\[
\boxed{
\mathcal R_t
=
\mathcal R^B_t-\mathcal R^C_t.
}
\]

所以一个完全整数的 sufficient focusing condition 是：

\[
\mathcal R^B_t\le0
\quad\text{且}\quad
\mathcal R^C_t\ge0.
\]

则必有

\[
\boxed{\mathcal R_t\le0.}
\]

其语义是：

- 相对于截面规模，branching pressure 不增加；
- 相对于截面规模，collision/focusing pressure 不减少；

则 relative expansion 不会增加。

这比直接要求 `Xi<0` 更接近传统 focusing dynamics 所问的问题：不是只判断当前收缩，而是判断 expansion 本身是否继续向更负方向演化。

## 7. P019-F-T05 —— 一个 intrinsic branch-clock 候选可以从 causal graph 反向定义

状态：`DEFINITION + EXACT IDENTITY / PHYSICAL INTERPRETATION OPEN`

Correction 04 已证明：把外部 Schwarzschild clock label 直接当作 causal graph 的生成原因是 underdetermined。

一个更稳健的研究方向是**反过来**：先从 primitive causal graph 得到一个 intrinsic causal-rate 候选，而不是用 clock 去制造 graph。

若截面 `A` 中每个状态至少有一个 future successor，定义：

\[
\boxed{
K_{\rm branch}(A)
=
\sum_{v\in A}(\deg^+(v)-1).
}
\]

这正好等于 branching surplus：

\[
\boxed{K_{\rm branch}(A)=B(A).}
\]

于是中心恒等式变成：

\[
\boxed{
\Xi(A)
=K_{\rm branch}(A)-C(A).
}
\]

这个公式本身是精确整数恒等式。

但把 `K_branch` 解释成物理 proper-time rate、gravitational clock rate 或 Schwarzschild `K_sigma`，目前**没有证明**。

因此目前只能称为：

**intrinsic causal branching-clock candidate**。

它的价值在于把研究方向改成：

\[
\text{primitive causal graph}
\to
(K_{branch},C,\Xi),
\]

再研究外部钟速是否是 `K_branch` 的某种 finite observation，而不是预设

\[
\text{clock}\to\text{graph}.
\]

## 8. P019-F-C01 —— 零 branch-clock budget 仍不足以单独定义 horizon

状态：`COUNTEREXAMPLE / NECESSITY RESULT`

若

\[
K_{branch}=B=0,
\]

则

\[
\Xi=-C\le0.
\]

但存在两种完全不同情况：

### 无 collision

若 successor map 在 `A` 上单射：

\[
C=0,
\qquad
\Xi=0.
\]

得到 marginal section。

### 有 collision

若两个当前状态合流到同一个 future state：

\[
C>0,
\qquad
\Xi<0.
\]

得到 contracting section。

所以即使把 intrinsic causal clock 定义为 branching budget：

\[
\boxed{
K_{branch}=0
\not\Rightarrow
\Xi=0.
}
\]

仍然需要 collision/focusing channel。

这再次支持当前 common-structure 模型：时间/branch capacity 与 spatial convergence 不是一个单变量能够完成的描述。

## 9. 一个更接近 Raychaudhuri 的整数研究模板

到本阶段，可以把后续问题压缩为：

\[
\boxed{
N_t,
\quad B_t,
\quad C_t,
\quad \Xi_t=B_t-C_t,
\quad
\mathcal R_t=N_t\Xi_{t+1}-N_{t+1}\Xi_t.
}
\]

传统 Raychaudhuri 的外部比较对象是 congruence expansion 的导数及 shear/curvature 等 source terms。

我们的当前整数问题则是：

1. 哪些 local combinatorial structures 控制 `R^B_t`；
2. 哪些 local collision-spectrum / curvature-like structures控制 `R^C_t`；
3. 是否存在整数 energy/focusing condition，能强迫

\[
\mathcal R^B_t\le0,
\qquad
\mathcal R^C_t\ge0;
\]

4. P011 的完整 `J_k^out` 是否比粗量 `C` 足以区分 shear-like 与 Ricci-like focusing；
5. causal-set / discrete Ricci prior art 中哪些工具可以作为对照，但不把概率/实数运输距离变成我们的 primitive。

## 10. 外部 prior-art 初筛

本阶段外部检索得到两个重要参照方向：

1. causal set theory 以 locally finite causal order 为基本结构，并在 continuum approximation 中用 cardinality 表示 volume；这与 P019 的“causal relation + finite cardinality”在方法上相邻，但 causal set 有自己完整的定义、随机 sprinkling 与 covariance 文献，必须明确引用，不能改名据为原创；
2. 2026 年已有 `Ollivier-Ricci Curvature for Causal Sets` 工作，用 Lorentzian optimal transport / probability measures 在 causal diamonds 上构造 mesoscopic Ricci curvature。它说明“从 order-theoretic discrete data 恢复 curvature-like information”已有直接前人工作，但其概率测度/optimal-transport primitive 与当前 Enterprise Math integer-only 核心不同。

因此后续 novelty claim 必须特别谨慎：P019 的潜在新点只能放在**特定整数 branch/collision calculus 与现有 Enterprise Math precision/fiber machinery 的组合**上，而不能声称“首次用离散因果结构研究曲率/黑洞”。

## 11. 本阶段 ledger

- `P019-F-T01`：collision domination iff bounded integer contraction —— `PROVED`
- `P019-F-T02`：finite focusing under persistent positive margin —— `PROVED`
- `P019-F-T03`：cross-multiplied relative-expansion change numerator —— `PROVED`
- `P019-F-T04`：branching/collision decomposition of relative-expansion change —— `PROVED`
- `P019-F-T05`：no-sink intrinsic branch-clock candidate equals branching surplus —— `DEFINITION + EXACT IDENTITY`
- `P019-F-C01`：zero branch-clock budget does not by itself imply marginality —— `COUNTEREXAMPLE / NECESSITY`

Executable checks：

- `src/enterprise_math/focusing.py`
- `tests/test_focusing.py`

## 12. 下一阶段

优先推进两个方向：

1. **local source decomposition**：尝试把 `C` 或 `R^C` 分成可与 shear-like / curvature-like effects 对比的纯整数局部项；
2. **clock calibration no-go / bridge**：研究 Schwarzschild/RN finite clock observation 是否可能作为 `K_branch` 的合法 P018 observation。若不能，正式把“clock”从基础变量降格为 derived observable。

在这两个方向完成前，不进入黑洞熵系数、Hawking radiation 或 Kerr 细节。
