# P018 —— 有限精度证明演算：补充 26

状态：`ACTIVE RESEARCH NOTE`  
范围：one-shot transport 与 self-contained reusable interface、不同 access model 下的精确最小值，以及 Q119 的边界分类  
依赖：P018-T175/T176、T198–T212  
前人工作边界：communication complexity、coding for computing、quotient algebra 与 syntactic congruence 都属于成熟数学。本文不创造新的通信模型，而是确定在两种不同信息访问合同下，哪个已经定义的 Enterprise Math invariant 才是正确的最小量。

---

## 1. 没有 access contract，就不存在唯一 transport minimum

“完成一个 operation 最少需要多少信息”这句话本身是不完整的，除非至少说明：

1. 谁能看见 hidden fine state；
2. receiver 已经知道哪些 side information；
3. 传输对象只用于当前一次 operation，还是之后还必须作为 reusable state 继续参加后续 operations。

Supplements 19、24、25 已经给出了两个不同的 exact minimum；它们回答的是不同合同。

### One-shot centralized correction model

encoder 能看到当前 fine input tuple；decoder 已知 raw coarse input tuple，只要求恢复这一次调用的 exact raw coarse output。

T200 给出：

\[
\boxed{|\mathcal C|_{\min}=B_E(\mu).}
\]

### Self-contained reusable interface model

一个 subsystem/subtree 输出 state label `I(x)` 后，future caller 不再能访问 hidden fine state `x`；interface state 自身必须保存原 observation，并保证所有声明的 future operations 继续 exact。

这已经不是一步 correction problem，而是 state-sufficiency problem。

---

## 2. P018-T213 —— Exact reusable-interface 判据

状态：`PROVED / EXECUTABLE`

令

\[
I:X\to Z
\]

为候选 reusable interface，并记

\[
R_I=\ker(I).
\]

对于 operation language `Sigma`，`I` 是保持 raw observation `O` 的 exact reusable interface，当且仅当：

1. raw observation 能从 interface factor 出来，即

   \[
   \boxed{R_I\subseteq\ker(O),}
   \]

   所以 `I` 不能把 `O` 已经区分的 states 再合并；
2. `R_I` 是 `Sigma`-congruence，因此每个 declared operation 都能 exact descent 到 interface state space。

所以 reusable interface 恰好就是一个 observation-respecting、对 declared language 精确闭合的 quotient/refinement state。

---

## 3. P018-T214 —— Contextual closure 就是最小 reusable exact interface

状态：`PROVED STRUCTURAL CONSEQUENCE / EXECUTABLE`

令

\[
R_*=\operatorname{Syn}_\Sigma(\ker O)
\]

为 T171–T175 的 contextual closure。

若 `I` 是任意 exact reusable interface，T213 说明 `R_I` 是包含在 `ker(O)` 内的 `Sigma`-congruence。由 `R_*` 的最大性：

\[
\boxed{R_I\subseteq R_*.}
\]

所以任何 exact reusable interface 至少都必须区分全部 contextual-closure classes，从而

\[
\boxed{|I(X)|\ge |X/R_*|.}
\]

反过来，规范 quotient map

\[
X\to X/R_*
\]

本身就是 exact reusable interface。

因此

\[
\boxed{
\min\#\text{ reusable interface states}=|X/R_*|.
}
\]

T175 也因此可以理解为 exact reusable-interface minimum theorem。

---

## 4. P018-T215 —— Future operation language 参数化最小 reusable state

状态：`PROVED STRUCTURAL CONSEQUENCE / EXECUTABLE`

设

\[
\Gamma\subseteq\Sigma.
\]

如果模块只承诺在较小 future language `Gamma` 下 exact reusable，那么最小规范 interface 为

\[
X/\operatorname{Syn}_\Gamma(E).
\]

若必须支持更大的 `Sigma`，由 T179：

\[
\operatorname{Syn}_\Sigma(E)
\subseteq
\operatorname{Syn}_\Gamma(E).
\]

所以

\[
\boxed{
|X/\operatorname{Syn}_\Sigma(E)|
\ge
|X/\operatorname{Syn}_\Gamma(E)|.
}
\]

因此 reusable precision 不只取决于“现在看得见什么”，还取决于**未来允许哪些 operations**。

---

## 5. P018-T216 —— One-shot token 与 reusable state 的差距可以任意大

状态：`PROVED / EXECUTABLE FAMILY`

对任意 `r>=2`，考虑有限 cyclic state space

\[
X_r=\mathbb Z/(2r)\mathbb Z
\]

用

\[
\{0,1,\ldots,2r-1\}
\]

表示，并采用 modulo `2r` addition。

只观察高位 radix block：

\[
O_r(x)=\left\lfloor\frac xr\right\rfloor\in\{0,1\}.
\]

### One-shot transport

固定 raw coarse inputs 后，modular addition 的 exact raw coarse output 只有两种可能，对应 residue carry/wrap bit，因此

\[
\boxed{B_{E_r}(+)=2.}
\]

所以对任意 `r`，minimum one-shot correction token 都只要两个 symbols。

### Reusable exact state

取同一 raw block 内任意两个不同 states：

\[
x=qr+u,
\qquad y=qr+v,
\qquad0\le u<v<r.
\]

选择加法 context 常数

\[
t=r-1-u
\]

并按 modulo `2r` 运算。

若 `q=0`，则

\[
O_r(x+t)=0,
\qquad O_r(y+t)=1.
\]

若 `q=1`，modular wrap 会把两个 block 反转：

\[
O_r(x+t)=1,
\qquad O_r(y+t)=0.
\]

所以同一 raw block 内任意两个不同 residues 都能被某个允许 addition context 区分。于是

\[
\boxed{
\operatorname{Syn}_{+}(E_r)=\Delta,
}
\]

最小 self-contained reusable interface 必须保留全部

\[
\boxed{2r}
\]

个 states。

因此

\[
\boxed{
\frac{\text{minimum reusable states}}
     {\text{minimum one-shot token symbols}}
=r
}
\]

可随 `r` 任意增长。

一个极小的 transient correction message 可以与任意大的 persistent reusable state complexity 同时存在。

---

## 6. P018-C25 —— Small transient token 不推出 small reusable module state

状态：`COUNTERWEIGHT / ACCESS-MODEL BOUNDARY`

T216 否定以下推理：

\[
B_E(\mu)\text{ 很小}
\quad\Longrightarrow\quad
\text{exact reusable state 也很小}.
\]

one-shot encoder 可以为当前调用直接读取 hidden fine operands；reusable subtree/module state 则不可以——一旦 interface 发出，未来 operations 只能看到 interface state 本身。

这两个信息访问合同不同。

因此 binary carry 不是 operand remainder state 的替代品。carry 之所以能很小，是因为当前 encoder 仍然有权限访问 operands 的 fine detail，并据此只发送本次 coarse output 所需的 correction。

---

## 7. P018-T217 —— Q119 的 access-model 分类

状态：`RESOLVED AT THE TWO CANONICAL ACCESS EXTREMES`

对有限 state spaces 与有限 finitary operation signatures，现在有两个规范极端模型的 exact minimum：

### Model A —— one-shot centralized correction

- encoder 看见 fine input tuple；
- decoder 已知 raw coarse input tuple；
- message 只使用一次，用于恢复 raw coarse output。

minimum token alphabet：

\[
\boxed{B_E(\mu).}
\]

### Model B —— self-contained reusable exact interface

- interface 发出后 hidden fine state 不再可用；
- interface 必须能恢复 raw observation；
- 所有 declared future operations 都必须保持 exact。

minimum reusable state space：

\[
\boxed{X/\operatorname{Syn}_\Sigma(E).}
\]

由 T216，两者可以相差任意大。

所以在没有明确**access/lifetime model** 之前，Q119 不存在唯一 scalar answer。

---

## 8. P018-T218 —— Structured transport 位于两个 minimum 之间，而不是替代其中之一

状态：`STRUCTURAL SYNTHESIS / EXECUTABLE EXEMPLAR`

Supplement 25 的 radix-addition `(carry,remainder)` law 现在位置非常清楚：

- persistent remainder 属于 Model B 所要求的 reusable exact state；
- carry 是 Model A 的 operation-specific one-shot transport coordinate；
- 两者的 associative composition 形成 reusable structured protocol，但没有混淆两类信息角色。

因此 structured transport algebra 应当被建模为：**作用在已经充分的 reusable state detail 之上的组合律**，并可能在 operation boundary 暴露更小的 transient token。

它不是 contextual closure 的替代品。

---

## 9. P018-C26 —— 没有 access/lifetime metadata，“transport complexity”没有唯一含义

状态：`FOUNDATIONAL GUARDRAIL`

任何“某 operation 的 transport complexity 是多少”的陈述，至少必须明确：

1. encoder 可以读取哪些 fine information；
2. decoder 已经拥有哪些 coarse/contextual state；
3. message 是 transient 还是必须成为下一步 reusable state；
4. 必须保持 exact 的 future operation language；
5. 是否允许 composition、interaction、variable-length coding 等协议能力。

若这些 metadata 不固定，不同合法模型会产生不同 exact minima。

因此 P018 后续不能在不说明 access contract 的情况下报告单一 transport-complexity 数值。

---

## 10. 分类之后仍开放的问题

两个规范端点已经 exact，但中间仍有大量真正开放结构：

- 已知有限 future operation tree 时的最小 composable interface；
- multi-stage computation 的 fusion gain；
- legitimate precision chart change 下 representation-stable token law；
- interactive / distributed encoder model；
- variable-length / average-cost model；
- `B_E(mu)` 相同但 composability 明显不同的 operation families。

这些都应作为 transport protocol 问题研究，不应重新塞回 state ontology。

---

## 11. Executable validation

新增：

- `src/enterprise_math/reusable_interface.py`
- `tests/test_reusable_interface.py`

测试验证：

1. exhaustive two-state reusable interfaces 都 refine canonical contextual closure；
2. raw observation 虽然当然能保存自身，却可能根本不是 reusable exact interface；
3. full-state identity 总是 reusable exact interface；
4. cyclic radix-addition family 中 one-shot `B=2`，而 canonical reusable state 有 `2r` 个 classes；
5. one-shot/reusable gap 随 `r` 线性增长且无上界。
