# P023 —— 合法性敏感的部分操作商，补充 08

状态：`CANONICAL RESULT / EXECUTABLE-CHECKED / NOT LEAN-CHECKED`  
范围：具有状态依赖动作定义域的有限确定性部分操作族  
依赖：FQ-004 functional-kernel 分层、P023 全操作族闭包  
解决来源：FQ-20260809-006，研究回报 PR #285  
纪律：部分转移系统、部分映射、带禁用动作的自动机、行为等价、sink totalization 与有限 partition refinement 均属于成熟前人数学。本文不对这些一般结构提出原创性主张。

## 1. 为什么全操作还不够

规范 P023 的 operation-family closure 原先假设有限个全定义确定性自映射

\[
F_a:X\to X.
\]

对于 guarded action，动作是否合法本身可能依赖当前状态。此时正确的一般对象是确定性部分操作

\[
\boxed{F_a:D_a\to X,\qquad D_a\subseteq X.}
\]

针对这类语言的 future-safe quotient 不仅要保留合法动作词的观测结果，还必须保留每个声明动作及其前缀是否合法。因此，禁用动作不能被悄悄解释成 identity 或直接省略。

全文中，`X` 是有限非空 typed state set，`A` 是有限非空动作名集合，每个 `F_a` 都是 `X` 上的确定性部分映射，而

\[
q_0:X\to Q_0
\]

是初始 observation / represented-precision partition。

## 2. 部分操作兼容性

一个 partition `q:X->Q` 与部分操作 `F_a:D_a->X` **兼容**，是指同一 quotient class 中的状态同时满足：

1. 定义域成员关系一致，
   \[
   x\in D_a\iff y\in D_a;
   \]
2. 当动作可执行时，目标状态落入同一 quotient class，
   \[
   x,y\in D_a\Longrightarrow q(F_a(x))=q(F_a(y)).
   \]

若对每个 `a in A` 都成立，则称 partition 与整个操作族兼容。

这正是让动作在 quotient 上**连同其定义域一起下沉**所需的条件。

## 3. 合法性敏感细化

给定当前 partition `q_t`，定义生成元行为

\[
B^t_a(x)=
\begin{cases}
(1,q_t(F_a(x))), & x\in D_a,\\
(0,\bot), & x\notin D_a,
\end{cases}
\]

其中 `bot` 只是 signature 中表示 undefinedness 的标记，并不是 `X` 的元素。

定义

\[
\boxed{
q_{t+1}(x)
=
\left(q_t(x),(B^t_a(x))_{a\in A}\right),
}
\]

具体 tuple 标签可以任意重编号，只保留其诱导的有限 partition。

## 4. P023-S4-T01 —— 单调有限稳定化

状态：有限状态空间上 `PROVED`；已有 executable 检查。

每个 `q_(t+1)` 都细化 `q_t`。若细化严格发生，class 数至少增加 1。因此，记 `N=|X|`、初始 class 数为 `c_0`，严格细化轮数至多为

\[
\boxed{N-c_0}.
\]

故该过程必在有限步到达稳定 partition `q_*`。

### 证明

`q_(t+1)` 的第一坐标就是 `q_t`，所以已经区分的状态不会重新合并。有限 partition 的每次严格细化都会增加 class 数，而 class 数至多为 `N`。∎

## 5. P023-S4-T02 —— 稳定商保留合法性与目标类

状态：`PROVED`；已有 executable 检查。

稳定后，每个声明的部分操作都能通过 `q_*` 下沉，并且其定义域得到保留。即对每个 `a`，

\[
q_*(x)=q_*(y)
\Longrightarrow
\left[
 x\in D_a\iff y\in D_a
\right],
\]

且当动作可执行时，

\[
q_*(F_a(x))=q_*(F_a(y)).
\]

### 证明

在 fixed point 上，同一 `q_*` class 的状态具有相同完整一步 signature。enabled bit 相同给出定义域一致；动作可执行时，target-class 坐标相同给出目标兼容。∎

## 6. P023-S4-T03 —— 有界合法性敏感动作词语义

状态：`PROVED`；在有限小系统上有穷尽 executable 检查。

对命名动作词

\[
w=a_1\cdots a_k,
\]

从左到右依次应用部分映射。仅当沿途每个访问到的前缀都可执行时，称该词在 `x` 上**有定义**。对长度不超过 `t` 的每个词，记录：

\[
(\mathrm{DEFINED},q_0(F_w(x)))
\]

若完整动作词有定义；否则在首个禁用前缀处记录

\[
\mathrm{UNDEFINED}.
\]

则

\[
\boxed{
q_t(x)=q_t(y)
\iff
\text{两状态对全部 }|w|\le t\text{ 的合法性敏感观测 signature 完全一致。}
}
\]

由于任一长度不超过 `t` 的动作词之所有前缀本身也属于长度不超过 `t` 的动作词集合，因此该 signature 同时保留完整的 prefix-definedness language。

### 证明

对 `t` 归纳。`t=0` 时 signature 就是 `q_0`。细化一步记录当前 class，并对每个首动作记录 disabledness，或者记录到达状态在上一深度的 class。由归纳假设，后一坐标正好编码剩余深度的动作词 signature。∎

## 7. P023-S4-T04 —— 最粗兼容细化

状态：`PROVED`；通过有限 partition 穷尽枚举进行 executable 检查。

设 `s:X->S` 是任一 partition，满足：

1. `s` 细化 `q_0`；
2. 每个部分操作都能通过 `s` 下沉，且定义域成员关系被保留。

则 `s` 细化每个 `q_t`，因而细化 `q_*`。

因此

\[
\boxed{
q_*
\text{ 是 }q_0\text{ 的、与所声明部分操作族兼容的最粗细化。}
}
\]

### 证明

对 `t` 归纳。若 `s` 细化 `q_t`，则 `s` 相等给出 `q_t` 相等、每个生成元的 enabledness 相等，并在动作可执行时给出目标属于同一 `s`-class。将归纳假设应用到这些目标，得到目标 `q_t` class 相等，于是完整 `q_(t+1)` signature 相同。∎

## 8. P023-S4-T05 —— 精确退化到全操作情形

状态：`PROVED`；reference suite 对所有纳入的两状态、双生成元全操作族做了穷尽 executable 检查。

若每个定义域都是整个 `X`，

\[
D_a=X\qquad\text{对每个 }a,
\]

则所有 enabledness bit 都是常量。去掉这些常量坐标后，恰好得到规范 P023 全操作族细化

\[
q_{t+1}(x)
=
\left(q_t(x),(q_t(F_a(x)))_{a\in A}\right).
\]

因此部分操作构造是现有全操作理论的严格接口扩展，而不是对它的替换。

## 9. Distinguished-UNDEFINED totalization 边界

为了验证，可以把部分操作族转成如下更大空间上的全操作族：

\[
X^\bot=X\sqcup\{\bot\},
\]

所有禁用转移都进入一个 absorbing `bot` 状态。

只有满足以下条件时，该验证构造在原始状态上的 stable quotient 才与真正的 partial quotient 一致：

1. `bot` 对所有动作都 absorbing；
2. `bot` 的 observation 与任何普通状态 observation 显式区分。

若新增 sink 在 observation 上与普通状态混同，totalization 可能错误地把“动作可执行的状态”和“动作禁用的状态”合并。

因此：

\[
\boxed{
\text{verification sink}\neq\text{新的 ontic/world state 假设}.
}
\]

规范语义接口仍是真正的部分映射 `F_a:D_a->X`。

## 10. Foundation 接口结论

只有当所声明未来语言包含 guarded/partial actions 时，FQ-006 才在 FQ-004 分层上增加一层：

\[
\boxed{
\text{typed state}
\to
\text{current observation kernel}
\to
\text{declared partial future language}
\to
\text{legality-sensitive future-signature kernel}.
}
\]

对于全定义语言，它精确退化为已规范化的 P023/FQ-004 接口。

Foundation 不把任何 application-specific legality law 设为原语。应用路线必须自己声明动作定义域；通用 quotient 只规定：在这些定义域已经声明之后，哪些信息必须被保留。

## 11. Prior-art 与归属边界

抽象机制属于成熟的有限 partial-transition / automata / behavioral-equivalence / partition-refinement 数学。P023 不对此提出一般原创性主张。

归属保持为：

- FQ-004 / A1–A2：通用 functional-kernel 与 declared-future 分层；
- P023：quotient compatibility 与最粗 safe refinement，现在包括部分确定性操作族；
- P024 与各应用路线：特定 action language 及其精确定义域/合法性规律；
- A4：multivalued correspondence/support，不与一个部分确定性函数族混同。

## 12. 可执行参考与验证状态

规范 executable reference：

- `src/enterprise_math/partial_operation_quotient.py`
- `tests/test_partial_operation_quotient.py`

回归测试覆盖 bounded-word equivalence、有限稳定化、最粗兼容最小性、对全操作实现的精确退化、distinguished absorbing-undefined totalization，以及未区分 sink 时的失败边界。

本补充**没有 Lean 检查**。不得仅因 Python reference 存在，或因为 P023 其他模块已经 Lean formalize，就把本文整体提升成 `LEAN_CHECKED_MAIN`。
