# P025 补充 04 —— Mason Witness-Slack 与无穷远接触深度

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner：`program/p025-mason-witness-slack`  
父 payload：`program/p025-abc-support-collapse@6c854aeb`  
前人工作状态：经典 Mason--Stothers/Wronskian 数学；架构解释 `NOVELTY_UNVERIFIED`

## 1. 目标

P025 第一代已经把经典 Mason--Stothers 路线拆成

\[
\text{multiplicity residual}
\to
\text{common Wronskian witness}
\to
\text{witness capacity}
\to
\text{radical bound}.
\]

本补充只追问一个更窄的问题：

> 成功的多项式证明内部，是否存在一个可与 P018/P023 精度语言比较的精确有限 **proof-slack state**？

答案是肯定的，但底层多项式代数仍属于经典数学。可复用候选是 accounting interface，而不是新的 Mason 定理。

全文设 `P_0,P_1,P_2` 为特征零域上的非零两两互素多项式，满足

\[
P_0+P_1+P_2=0,
\]

并假定公共循环 Wronskian 非零。记

\[
h_i=\deg P_i,
\qquad
R=\deg\operatorname{rad}(P_0P_1P_2),
\qquad
D=h_0+h_1+h_2-R.
\]

在经典 Wronskian 证明中，multiplicity residual 的乘积整除公共 Wronskian，因此

\[
D\le w,
\qquad
w=\deg W.
\]

对任意目标指标 `i`，若 `{j,k}` 为其补对，普通导数次数界给出

\[
w\le h_j+h_k-1.
\]

这些都是既有的 Mason--Stothers 证明部件 [SRC-BAEK-LEE-2024-MASON-LEAN]。

## 2. P025-T11 —— 精确 proof-margin 分解

对目标 `i` 定义

\[
A_i=w-D
\]

以及

\[
C_i=h_j+h_k-1-w.
\]

在经典证明不等式下二者均非负。则

\[
\boxed{
R-h_i-1=A_i+C_i.
}
\]

### 证明

因为

\[
D=h_0+h_1+h_2-R,
\]

所以

\[
R-h_i-1
=h_j+h_k-1-D.
\]

加减一个 `w`：

\[
h_j+h_k-1-D
=(w-D)+(h_j+h_k-1-w)
=A_i+C_i.
\]

这里没有任何渐近论证。

### 解释

`A_i` 衡量 multiplicity residual 被公共 witness 吸收以后，witness 中还剩多少次数空间：

\[
\boxed{A_i=\text{residual absorption slack}.}
\]

`C_i` 衡量实际 Wronskian 比补对的初等次数上限低了多少：

\[
\boxed{C_i=\text{witness capacity slack}.}
\]

因此最终 Mason margin 不是一个不可再分的数，而是两个证明阶段资源的精确和。

## 3. P025-T12 —— Wronskian capacity slack 等于无穷远接触深度

令 `P,Q` 为特征零域上的非零、非成比例多项式。记

\[
p=\deg P,
\qquad
q=\deg Q,
\]

以及

\[
W(P,Q)=P'Q-PQ'.
\]

定义 Wronskian capacity slack

\[
\boxed{
\kappa_\infty(P,Q)
=p+q-1-\deg W(P,Q).
}
\]

下面给这个非负整数一个精确的系数含义。

### 次数不同

若 `p neq q`，`W(P,Q)` 的最高次项为

\[
(p-q)\operatorname{lc}(P)\operatorname{lc}(Q)x^{p+q-1},
\]

在特征零下非零。因此

\[
\deg W(P,Q)=p+q-1
\]

从而

\[
\boxed{\kappa_\infty(P,Q)=0.}
\]

两个 degree profile 在第一层最高次信息上就已经分离。

### 次数相同

现在设

\[
p=q=d.
\]

记 `a=lc(P)`、`b=lc(Q)`，作前导消元多项式

\[
E=bP-aQ.
\]

因为 `P,Q` 不成比例，

\[
E\ne0,
\qquad
 e=\deg E<d.
\]

并且

\[
W(E,Q)=bW(P,Q),
\]

因为 `Q,Q` 的 Wronskian 为零。由于 `e neq d`，把刚才的异次数情形用于 `(E,Q)`，得到

\[
\deg W(P,Q)=\deg W(E,Q)=e+d-1.
\]

所以

\[
\boxed{
\kappa_\infty(P,Q)=d-e.
}
\]

定义

\[
\boxed{
\delta_\infty(P,Q)=
\begin{cases}
0,&\deg P\ne\deg Q,\\
d-\deg(bP-aQ),&\deg P=\deg Q=d.
\end{cases}
}
\]

则精确有

\[
\boxed{
\kappa_\infty(P,Q)=\delta_\infty(P,Q).
}
\]

### 有限精度含义

当次数同为 `d` 时，可以概念上除去各自前导项，并使用局部坐标 `t=1/x`。整数 `delta_infinity` 正是两个归一化 coefficient jet 第一次出现差异的正阶深度。

因此普通 Wronskian 的次数损失就是一个精确的**无穷远碰撞深度**：

\[
\boxed{
\text{Wronskian capacity loss}
=
\text{normalized leading-jet coalescence depth}.
}
\]

其证明只使用有限系数比较；可执行解释不需要把连续极限作为原始对象。

## 4. P025-T13 —— Mason margin = absorption slack + contact depth

把 P025-T12 代入 P025-T11，对目标 `i` 及其补对 `(P_j,P_k)` 得到

\[
\boxed{
R-h_i-1
=
(w-D)+\delta_\infty(P_j,P_k).
}
\]

这是本补充最重要的校准结果。

它揭示最终 radical degree 比 target degree 多出裸 Mason 单位以上的部分，可能来自两个逻辑不同的原因：

1. 公共 witness 含有并非由 multiplicity residual 强制占用的次数容量；
2. 补多项式对在若干个归一化前导系数层仍不可区分，Wronskian 到更深层才检测到分裂。

若补对次数不同，则

\[
\delta_\infty=0,
\]

最终超过 Mason 单位的 margin 全部来自 residual absorption slack。

若补对次数相同且不成比例，则

\[
\delta_\infty\ge1,
\]

所以这个 orientation 自动多出至少一个 radical margin 单位。

这是 Wronskian 证明的初等推论，不对 Mason 极值情形作历史创新主张。

## 5. P025-N03 —— 最终 theorem margin 会抹去 proof provenance

考虑特征零上的以下两个精确多项式关系。

### 例 A

\[
P_0=x^2,
\qquad
P_1=x^2+1,
\qquad
P_2=-(2x^2+1).
\]

三个多项式两两互素，次数都是 `(2,2,2)`。其 radical degree 分别为 `(1,2,2)`，所以

\[
R=5,
\qquad
D=1.
\]

对目标 `P_2`，

\[
W(P_0,P_1)=2x,
\qquad
w=1.
\]

于是

\[
A_2=w-D=0,
\qquad
\delta_\infty(P_0,P_1)=2,
\]

并且

\[
R-h_2-1=2=0+2.
\]

### 例 B

\[
P_0=x^2,
\qquad
P_1=x^2+x+1,
\qquad
P_2=-(2x^2+x+1).
\]

degree triple 仍然是 `(2,2,2)`，三个多项式仍两两互素，并且

\[
R=5,
\qquad
D=1.
\]

但现在

\[
W(P_0,P_1)=x^2+2x,
\qquad
w=2.
\]

所以

\[
A_2=1,
\qquad
\delta_\infty(P_0,P_1)=1,
\]

而最终 theorem margin 仍然是

\[
R-h_2-1=2=1+1.
\]

因此粗数据

\[
(h_0,h_1,h_2,R,R-h_2-1)
\]

可以完全相同，但内部 proof-resource decomposition 不同。

所以若后续问题关心证明**为什么**成功、未使用的容量究竟位于哪个阶段，仅保留最终定理真值或 margin 并不是完备状态。

## 6. 架构后果 —— decision precision 与 proof-provenance precision

P023 已经说明所需精度依赖声明的未来观测。上面的两个例子在一个已经证明的数学世界里，把同一原则校准到了 proof level。

若任务只要求最终 Mason 不等式，那么内部二元组

\[
(A_i,\delta_\infty)
\]

在知道其和以后可以安全抹去。

若未来任务会问以下任何问题，最终 margin 就不够：

- residual absorption 是否恰好饱和；
- Wronskian 是否因为 leading-jet collision 而掉次；
- 有多少层归一化前导系数发生了合流；
- 多余 margin 究竟由哪个证明阶段提供。

因此出现一个区分：

\[
\boxed{\text{decision precision} \ne \text{proof-provenance precision}.}
\]

P025 并不建议把全部 proof trace 都塞进基础状态。恰恰相反：只有后续 query 真正会消费这些 proof-stage coordinate 时才保留，完全遵守 P023 的原则。

## 7. 前人工作与创新边界

Mason--Stothers 定理、多项式 radical、导数整除、循环 Wronskian 相等以及 Wronskian 次数界均属于既有数学 [SRC-BAEK-LEE-2024-MASON-LEAN]。多项式 `abc` 的等号与极值情形也已有大量前人研究，因此本补充不主张任何极值分类优先权。

恒等式

\[
U-D=(w-D)+(U-w)
\]

只是初等 accounting。同次数前导消元给出 Wronskian 掉次的证明同样属于初等多项式代数。

项目侧唯一候选是把它们组合成

\[
\text{proof residual}
\to
\text{witness absorption slack}
\to
\text{coefficient collision depth}
\to
\text{task-relative proof state}.
\]

其历史创新性保持 `NOVELTY_UNVERIFIED`。

## 8. 可执行资产与回归

本 generation 新增：

- `src/enterprise_math/mason_witness_slack.py`
  - 精确整数多项式运算；
  - Wronskian 次数与 capacity slack；
  - 精确 infinity-contact depth；
  - Mason margin 分解；
  - relation-level slack profile。
- `tests/test_mason_witness_slack.py`
  - 异次数的零接触深度；
  - 同次数 depth-one / depth-two 样本；
  - 两个 final margin 相同但 provenance 不同的 Mason 样本；
  - 非法 bound 与成比例 pair guard；
  - 小系数范围内 Wronskian capacity slack 与 infinity contact depth 的穷举对照。

独立于仓库实现的 prototype 已检查次数 `1..3`、系数 `[-2,2]` 内的 382,848 个非退化有序多项式对，没有发现不一致。这里只作为回归证据；P025-T12 已在上文证明。

## 9. 下一前沿

目前有三个高价值问题：

1. **P018 bridge：** 判断 `delta_infinity` 是否只是已有 first-separation / collision-depth coordinate 的特化，还是暴露出一个缺失的有限 coefficient-jet 母定理。
2. **P023 bridge：** 精确分类在什么 proof-query language 下，二元组 `(absorption_slack,contact_depth)` 可以只保留它们的和。
3. **返回整数 abc：** 检查 Pasten 的 arithmetic Wronskian 是否存在类似的有限 slack decomposition，并判断其分量是否携带超过最终 norm bound 的结构；不得假定多项式次数恒等式可以自动搬运。

优先顺序仍然是先在已经证明的多项式世界里解决 1、2，再回到更强的整数 abc 主张。
