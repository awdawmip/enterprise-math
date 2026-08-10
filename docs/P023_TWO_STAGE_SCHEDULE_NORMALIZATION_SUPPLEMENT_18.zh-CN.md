# P023 —— Sequential precision code 的两阶段正规化，补充 18

状态：`PROVED RESEARCH NOTE`  
归属：A2 / P023，并复用 P018 mixed-radix 结构  
依赖：P023-S17 slack decomposition、P023-S14 conditional repair schedules、P018 exact mixed-radix charts  
纪律：mixed-radix packing 与有限 realized subset ranking 都属于成熟构造。本补充的项目结论，是把 P023 两类 scheduling slack 分别解释成可被精确正规化的两个 defect。

## 1. 从诊断推进到 exact normalization

S17 已证明 sequential precision schedule 的 overhead 精确分成两部分：

\[
S_{\rm total}=S_{\rm radix}+S_{\rm inc}.
\]

本补充进一步证明：这两项并不只是事后统计量。

它们各自对应一个 exact finite normalization step：

\[
\boxed{
\text{separate local repair digits}
\longrightarrow
\text{packed mixed-radix code}
\longrightarrow
\text{realized joint-rank code}.
}
\]

第一步恰好消除 `S_radix`；第二步恰好消除 `S_inc`。

## 2. 一个 schedule 上的 canonical local repair digits

固定 task order 与 S14 context chain：

\[
C_0\supseteq C_1\supseteq\cdots\supseteq C_m=E_*.
\]

第 `j` 步的最大 branching factor 为

\[
\rho_j.
\]

在每个当前 context block 内，对实际出现的 child blocks 做局部编号：

\[
d_j\in\{0,\ldots,\rho_j-1\}.
\]

不同 parent blocks 可以复用同一个 digit alphabet，因为 parent context 已经知道。

于是每个原始 state `x` 都得到一个 digit word：

\[
\boxed{
\mathbf d(x)=(d_1(x),\ldots,d_m(x)),
}
\]

其 radix vector 为

\[
\boxed{
(\rho_1,\ldots,\rho_m).
}
\]

## 3. P023-S18-T01 —— Local repair word 精确表示 final joint classes

状态：`PROVED`。

两个 states 具有相同完整 repair digit word，当且仅当它们位于同一个 final joint block `E_*`。

### 证明

对 stages 归纳。第一步 local digit 唯一标记 universal parent 内实际选择的 child block。假设 prefix digits 已经唯一决定当前 context block，则下一 local digit 又在该 parent 内唯一决定下一个 child block。

所以每个 prefix 都精确决定 `C_j`；到 `j=m` 时，完整 digit word 与 final joint block 等价。∎

因此 local digit word 是 final precision 的 exact sequential coordinate system。

## 4. P023-S18-T02 —— Mixed-radix packing 在完整 product alphabet 上是双射

令

\[
P=\prod_{j=1}^{m}\rho_j.
\]

形式上的完整 digit product 为

\[
\prod_j\{0,\ldots,\rho_j-1\}.
\]

使用标准 mixed-radix join：

\[
\boxed{
J(d_1,\ldots,d_m)
=
(((d_1\rho_2+d_2)\rho_3+d_3)\cdots)\rho_m+d_m.
}
\]

则

\[
\boxed{
J:
\prod_j[0,\rho_j)
\overset{\sim}{\longrightarrow}
[0,P)
}
\]

为双射，逆映射由连续 quotient/remainder extraction 给出。

这正是 P018 已经使用的有限 mixed-radix 结构。

## 5. P023-S18-T03 —— Packing 恰好移除 radix slack

状态：`PROVED`。

分 stage coding 需要

\[
\sum_jL_B(\rho_j)
\]

个 base-`B` symbols。

packed product code 只需要

\[
L_B(P).
\]

所以 exact saving 为

\[
\boxed{
\sum_jL_B(\rho_j)-L_B(P)
=S_{\rm radix}.
}
\]

这一步没有改变任何 state semantics，也不使用 realizability filter；完整 formal product alphabet 被双射保留。

因此 radix slack 完全是 coordinate-packing defect。

## 6. Realized product support

不是每个 mixed-radix word 都必然由真实 state 实现。

定义

\[
\mathcal C
=
\{J(\mathbf d(x)):x\in X\}
\subseteq[0,P).
\]

由 T01，

\[
\boxed{
|\mathcal C|=|X/E_*|=N_*.
}
\]

`[0,P)` 中不属于 `C` 的 code values，就是没有任何 state 实现的形式 sequential codewords。

## 7. P023-S18-T04 —— Realized-support ranking 恰好移除 incidence slack

状态：`PROVED`。

把 realized packed codes 从小到大排序，并定义 rank map

\[
\boxed{
r:\mathcal C\overset{\sim}{\longrightarrow}[0,N_*).
}
\]

这只是 actual final joint classes 的双射重编码。

其 base-`B` depth 为

\[
L_B(N_*).
\]

从 packed product code 的 `L_B(P)` depth 到该 direct joint code 的 exact saving 为

\[
\boxed{
L_B(P)-L_B(N_*)
=S_{\rm inc}.
}
\]

第二步没有删除任何真实 state，只删除 unused formal product codes。

因此 incidence slack 精确就是 unrealized-support defect。

## 8. P023-S18-T05 —— 完整 normalization 达到 final cardinality lower bound

把 T03 与 T04 合并：

\[
\boxed{
\sum_jL_B(\rho_j)
\longrightarrow
L_B(P)
\longrightarrow
L_B(N_*).
}
\]

总共移除的 depth 正好是

\[
S_{\rm radix}+S_{\rm inc}=S_{\rm total}.
\]

所以任意 finite sequential task code 都存在一个 exact normalization，最终到达由 final joint-state cardinality 给出的整数下界。

代价只在 representation：final rank code 可能不再把原始 stage coordinates 显式暴露成独立 digits。

## 9. 两种 normalization mechanism 必须分开

### Mixed-radix packing

- domain：**完整 formal product alphabet**；
- operation：双射 coordinate change；
- 消除：separate-ceiling / radix slack；
- 不能消除：unrealized product tuples。

### Realized-support ranking

- domain：product codes 中**实际实现的 subset**；
- operation：support quotient / relabeling；
- 消除：incidence capacity slack；
- 需要：actual realizability information。

因此必须保持：

\[
\boxed{
\text{coordinate normalization}
\neq
\text{state-space quotient}.
}
\]

## 10. 两个纯 witness

S17 的 radix-only `3 x 5` complete-incidence example 中

\[
P=N_*=15.
\]

packing 把 binary depth 从 `5` 降到 `4`，realized ranking 不再节省任何 bit。

S17 的 incidence-only five-state example 中

\[
P=9,
\qquad
N_*=5.
\]

packing 没有节省（`4 -> 4`），而 realized ranking 完整实现 `4 -> 3` 的 1 bit saving。

所以两种 normalization mechanism 各自独立必要。

## 11. 与 P018 的关系

P018 mixed-radix charts 已经证明：有限 detail coordinates 可以用纯整数方式 exact join/split，而无需 hidden real arithmetic。

S18 把同样的算术用于 **task-repair digits**，而不是 spatial/detail digits。

因此得到更广原则：

> 只要有限 repair coordinates 形成 product alphabet，在进行任何 realizability quotient 之前，coordinatewise representation 与 packed integer representation 可以精确互换。

后续 support quotient 仍然是另一种 A2 操作。

## 12. 研究工具后果

一个 multi-stage proof state 不能因为携带很多 local repair coordinates 就直接被宣布为 irreducibly large。

在接受 state cost 之前：

1. 先求 exact local repair radices；
2. mixed-radix pack，消除 coordinate-ceiling overhead；
3. 计算 packed code 的 realized support；
4. 只对 realized support 做 quotient/rank；
5. 在删除原 coordinate chart 前，重新检查 downstream future-task requirements。

这是 exact compiler pipeline，不是 lossy compression。

## 13. 可执行规范

- `src/enterprise_math/precision_schedule_normalization.py`
- `tests/test_precision_schedule_normalization.py`

测试穷举 `2 x 3 x 4` mixed-radix alphabet 验证 pack/unpack 双射，验证 local digit words 精确重建 final joint classes，并分别隔离 radix-only 与 incidence-only normalization step。

## 14. 基础边界

direct final rank code 对声明的 final task quotient 是最小表示，但若未来新增 tasks 需要访问原 repair coordinates，它可能成为糟糕的 intermediate state。

因此 normalization 仍必须 future-language relative：

\[
\boxed{
\text{minimal final code}
\not\Rightarrow
\text{minimal state for every future extension}.
}
\]

是否能安全删除原 coordinate chart，仍由 P023 future-safe refinement 决定。
