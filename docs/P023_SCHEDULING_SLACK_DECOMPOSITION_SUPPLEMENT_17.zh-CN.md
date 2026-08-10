# P023 —— 调度 slack 分解与 primitive-task overhead，补充 17

状态：`PROVED RESEARCH NOTE`  
归属：A2 / P023，并桥接 P018 mixed-radix precision  
依赖：P023-S14 scheduling、S13 realized joint incidence、P018 integer radix/carry discipline  
纪律：整数 ceiling codes 与有限 incidence products 都属于成熟数学。本补充的项目作用，是把 sequential precision overhead 的两种不同数学来源严格拆开。

## 1. 一个 scalar slack 混合了两种不同 defect

对一个 task order `sigma`，S14 定义 stage repair factors

\[
\rho_1,\ldots,\rho_m
\]

以及总 base-`B` symbol depth

\[
C_B(\sigma)=\sum_j L_B(\rho_j).
\]

令

\[
P_\sigma=\prod_j\rho_j
\]

为 stagewise product capacity，令

\[
N_*=|X/E_*|
\]

为真实 final joint class count。

S14 已给出

\[
N_*\le P_\sigma.
\]

总 scheduling slack

\[
C_B(\sigma)-L_B(N_*)
\]

实际上包含两种不同来源。

## 2. P023-S17-T01 —— 精确二项 slack decomposition

状态：`PROVED`。

定义

\[
\boxed{
S_{\rm radix}(\sigma)
=
\sum_jL_B(\rho_j)-L_B(P_\sigma),
}
\]

以及

\[
\boxed{
S_{\rm inc}(\sigma)
=
L_B(P_\sigma)-L_B(N_*).
}
\]

则二者都是非负整数，并且

\[
\boxed{
C_B(\sigma)-L_B(N_*)
=
S_{\rm radix}(\sigma)
+
S_{\rm inc}(\sigma).
}
\]

### 证明

整数 symbol depth 的 submultiplicativity 给出

\[
L_B(P_\sigma)
=L_B\!\left(\prod_j\rho_j\right)
\le
\sum_jL_B(\rho_j),
\]

因此 `S_radix>=0`。

又因为 `N_*<=P_sigma`，由 `L_B` 单调性有

\[
L_B(N_*)\le L_B(P_\sigma),
\]

所以 `S_inc>=0`。

总式只是精确 telescoping。∎

## 3. 两项的含义

### Radix packing slack

即使每一步 capacity 都被完全实现，`S_radix` 仍然可能非零。

它来自：每个 stage 单独向上取整到 base-`B` alphabet depth，而不是把完整 mixed-radix product 一次性打包编码。

这是 scheduling 版的 integer radix/carry discipline：多个 local radices 分开编码时，可能比其乘积真正需要的 whole base-`B` symbols 更多。

### Incidence capacity slack

`S_inc` 比较 stagewise product capacity 与真实 joint state count。

它来自 realized incidence 没有填满每一步 worst-case branching 的形式乘积。Nonuniform branching 与 higher-order dependency 是典型来源。

这是 P017/P023 中“candidate product 与 realized states 不同”的 task-scheduling 版本。

## 4. P023-S17-T02 —— 可以只有 incidence slack 而没有 radix slack

状态：`PROVED BY EXPLICIT WITNESS`。

取 5 个 states 与两个 three-block tasks，其 realized incidence edges 为

\[
(A,X),(A,Y),(A,Z),(B,X),(C,X).
\]

两个方向的 repair factors 都是 3：

\[
\rho(E,F)=\rho(F,E)=3.
\]

所以任一顺序有

\[
P_\sigma=3\cdot3=9.
\]

但实际只实现 5 个 joint classes：

\[
N_*=5.
\]

在 base two 中，

\[
C_2=2+2=4,
\qquad
L_2(P_\sigma)=L_2(9)=4,
\qquad
L_2(N_*)=L_2(5)=3.
\]

因此

\[
\boxed{
S_{\rm radix}=0,
\qquad
S_{\rm inc}=1.
}
\]

全部 1 bit overhead 都来自结构性的 incidence overcapacity。

## 5. P023-S17-T03 —— 可以只有 radix slack 而没有 incidence slack

状态：`PROVED BY EXPLICIT WITNESS`。

取一个 3-block task 与一个 5-block task 的完整 incidence product，共 15 个 realized states。

此时

\[
\rho(E,F)=5,
\qquad
\rho(F,E)=3,
\]

而所有形式 pair 都真实存在，所以

\[
P_\sigma=N_*=15.
\]

对 base two 的顺序 `E -> F`，

\[
C_2=L_2(3)+L_2(5)=2+3=5,
\]

但

\[
L_2(P_\sigma)=L_2(15)=4.
\]

因此

\[
\boxed{
S_{\rm radix}=1,
\qquad
S_{\rm inc}=0.
}
\]

尽管 incidence 完全没有缺口，仍然存在 1 bit overhead；它纯粹来自 radix packing。

## 6. P023-S17-T04 —— 即使 optimal ordering 也未必达到 final class-count lower bound

状态：`PROVED BY THE FIVE-STATE WITNESS`。

Section 4 的 incidence-only witness 中，两个 task orders 的 binary cost 都是 4，而 final joint quotient 只有 5 classes，lower bound 为 3。

因此

\[
\boxed{
\min_\sigma C_2(\sigma)=4>3=L_2(N_*).
}
\]

所以对声明的 primitive task language，positive scheduling slack 可能是**不可避免**的。

这比“某个 order 不最优”更强：所有可用 sequential orders 都相对于 hypothetical direct joint code 存在 overhead。

## 7. Primitive-task interface overhead

定义

\[
\boxed{
H_B(\mathcal T)
=
\min_\sigma C_B(\sigma)-L_B(N_*).
}
\]

它表示：通过声明 primitive tasks 获取 final precision 时，不可避免的最小 overhead。

它依赖 task language，而不只依赖 final joint partition。

如果允许直接加入 bundled task

\[
E_*(x)=([x]_{E_1},\ldots,[x]_{E_m}),
\]

该 task 正好有 `N_*` classes，因此只需

\[
L_B(N_*)
\]

symbols，interface overhead 立刻降为 0。

所以

\[
\boxed{
\text{相同 final precision}
\not\Rightarrow
\text{不同 primitive task languages 具有相同 acquisition overhead}.
}
\]

## 8. P023-S17-T05 —— Bundling 可以消除 interface overhead，而不改变 final semantics

状态：`PROVED`。

加入一个等于 final joint observation 的 bundled task，不会改变 final joint partition；它只改变允许的 acquisition language。

因此 positive `H_B(T)` 不是 final precision state 自身的 intrinsic defect，而是通过特定 primitive task interface 表示/获取该 state 产生的 defect。

这与项目更广泛的三层区分一致：

- represented state semantics；
- allowed operations/queries；
- task-relative repair cost。

## 9. 与 P018 radix calculus 的关系

P018 已经研究 mixed-radix precision state 与 exact carry/coherence。

S17 给它一个新的 proof-state 解释：

\[
\boxed{
\text{radix slack}
=
\text{separately rounded stage alphabets 相对于 packed product capacity 的额外 cost}.
}
\]

这提示下一层优化：schedule 不仅可以选择 task order，还可能选择如何把相邻 repair alphabets 打包成 mixed-radix symbols。

这种 packing 无法消除 incidence capacity slack，因为 unrealized joint states 属于另一类结构 defect。

## 10. 研究工具规则

一个 schedule 出现 positive slack 时，不要先发明新 heuristic，应先诊断：

1. 计算 product capacity `P_sigma`；
2. 把 total slack 分成 `S_radix` 与 `S_inc`；
3. radix slack 主导时，调整 coding/packing，而不是修改 task semantics；
4. incidence slack 主导时，利用 dependency closure、realized tuples 或改 task order；
5. 如果 optimal schedule 仍有正 overhead，真正限制对象就是 primitive task interface；
6. 区分“加入 bundled primitive”与“改变 final precision state”。

这样不会把两个不同 defect 都笼统叫成 inefficiency。

## 11. 可执行规范

- `src/enterprise_math/precision_scheduling_slack.py`
- `tests/test_precision_scheduling_slack.py`

测试分别隔离纯 incidence slack 与纯 radix slack，验证精确二项 decomposition，证明五状态 family 上 unavoidable optimal interface overhead，并验证加入 direct bundled joint task 后 overhead 降为 0。

## 12. 前人工作与新颖性纪律

Mixed-radix coding、integer ceiling effects、product capacities 与 task bundling 都属于成熟思想。

本项目新增综合是：把 P023 内生 repair schedule cost 精确分解成 radix component 与 realized-incidence component，并把它用作 precision / number-theoretic proof states 的研究诊断工具。
