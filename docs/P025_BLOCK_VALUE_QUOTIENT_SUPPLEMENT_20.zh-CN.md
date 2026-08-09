# P025 补充 20 —— Witness Cost Language 的 Exact Block Derivative-Value Quotient

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-access-tail-stage18`  
依赖：P025 补充 13–19；P023 future-compatible quotient semantics  
Hard block：`NONE`

## 1. 第二种压缩

补充 19 已证明，每个 arithmetic block 内部都能实现任意 primitive positive coefficient row，因此不能靠“真实 block row 更特殊”来普遍简化**单 block access function**。

但是 abc relation 并不直接读取每一个 prime coordinate。对当前 Wronskian certificate future language，它只通过每个 block 的 arithmetic derivative value 读取该 block。

对 fine witness 写成

\[
\boxed{
t_a=d_x(a),
\qquad t_b=d_x(b),
\qquad t_c=d_x(c).}
\]

Additivity 精确等价于

\[
\boxed{t_a+t_b=t_c,}
\]

而 arithmetic Wronskian 精确是

\[
\boxed{W=a t_b-b t_a.}
\]

因此可以把高维 prime-coordinate witness 按这三个 block derivative values 取商，同时保留每个 block 的 exact minimum access response。

## 2. Block derivative image ideals 与 access functions

对 `n>1`，令

\[
\boxed{A(n)=\gcd_{p\mid n}\frac{n v_p(n)}p}
\]

为补充 15 的 raw derivative image generator。于是

\[
d_x(n)\in A(n)\mathbb Z.
\]

单位 block 的 image 定义为 `{0}`。

再定义 exact block access function

\[
\boxed{
\kappa_n(t)
=
\min\{\|x^{(n)}\|_\infty:d_{x^{(n)}}(n)=t\}.
}
\]

它恰好在 block derivative image 上有限。把 raw coefficient row 除以 image generator 后，补充 16–18 已给出这类 response 的有限 exact representation。

## 3. P025-D12 —— compressed derivative-value lattice

定义

\[
\boxed{
\Lambda_{abc}
=
\{(u,v)\in\mathbb Z^2:
 u\in A(a)\mathbb Z,
 v\in A(b)\mathbb Z,
 u+v\in A(c)\mathbb Z
\}.
}
\]

若某 block 是 unit，则对应 derivative value 必须精确为零。

每个 additive fine witness 都映到

\[
(u,v)=(t_a,t_b)\in\Lambda_{abc}.
\]

反过来，`Lambda_abc` 中每个点都能在三个互不重叠的 prime-support blocks 内独立选择 prime-coordinate preimages；因为 `t_c=u+v`，合并后自动满足 additive relation。

所以 fine additive witness family 满射到这个至多 rank-two 的整数格。

## 4. P025-T57 —— 固定一个 block-value state 的 exact minimum fine norm

对 `(u,v) in Lambda_abc` 定义

\[
\boxed{
K(u,v)
=
\max\bigl(
\kappa_a(u),
\kappa_b(v),
\kappa_c(u+v)
\bigr).
}
\]

则

\[
\boxed{
K(u,v)
=
\min\{\|x\|_\infty:
 x\text{ 为 additive fine witness，且 }
(d_x(a),d_x(b))=(u,v)\}.
}
\]

### 证明

任意拥有这些 block derivative values 的 fine representative，在每个 disjoint prime-support block 上都必须是相应 target 的 preimage，所以其 norm 至少等于每个 block minimum，因而至少为 `K(u,v)`。

反过来，在三个 block 中独立选择达到各自 block minimum 的 prime-coordinate preimage。由于 blocks 坐标互不重叠，合并后因 derivative values 满足 `u+v=t_c` 而成为 additive fine witness；其全局 `L_infinity` norm 正好等于三个 block norms 的最大值。∎

所以 block-value state 虽然丢掉了 block 内的 prime-coordinate identity，却对当前 future language 保留了 exact optimal geometric cost。

## 5. P025-T58 —— Wronskian 与 absorption 精确下沉

对任意 compressed point `(u,v) in Lambda_abc`，

\[
\boxed{W(u,v)=a v-b u.}
\]

令

\[
M=m(a)m(b)m(c).
\]

Pasten 的 residual divisibility 保证每个非零 additive compressed witness 满足

\[
M\mid W(u,v).
\]

因此对 nondegenerate point 定义

\[
\boxed{
\eta(u,v)=\frac{|a v-b u|}{M}.
}
\]

Wronskian magnitude 与 absorption redundancy 都只依赖 block-value quotient，不读取 block 内部 prime identity。

## 6. P025-T59 —— fine 与 block-value Pareto frontiers 完全一致

Fine witness cost pair 为

\[
C(x)=(\|x\|_\infty,\eta(x)).
\]

那么

\[
\boxed{
\operatorname{Min}
\{C(x):x\text{ 为 nondegenerate additive fine witness}\}
=
\operatorname{Min}
\left\{
\left(K(u,v),\frac{|av-bu|}{M}\right):
(u,v)\in\Lambda_{abc},\ av-bu\ne0
\right\}.
}
\]

### 证明

每个 fine witness 都映到一个 compressed point；`eta` 完全相同，而 fine norm 至少为 `K(u,v)`，所以它被该 compressed state 的 minimum-norm representative 支配。

反过来，P025-T57 对每个 compressed point 构造 fine representative，使 norm 精确等于 `K(u,v)`。因此 nondominated cost pairs 双向一致。∎

这就是当前 norm/Wronskian certificate language 的 exact quotient theorem。

## 7. 对 `mu`、`eta_min`、`nu` 的后果

Scalar witness radius 变成

\[
\boxed{
\mu
=
\min_{(u,v)\in\Lambda_{abc},\ av-bu\ne0}
K(u,v).
}
\]

Arithmetic absorption floor 变成

\[
\boxed{
\eta_{\min}
=
\frac1M
\min_{(u,v)\in\Lambda_{abc},\ av-bu\ne0}
|av-bu|.
}
\]

而第一次访问 floor 的半径为

\[
\boxed{
\nu
=
\min_{(u,v)\in\Lambda_{abc},\ |av-bu|=M\eta_{\min}}
K(u,v).
}
\]

因此当前三类 precision coordinates 全部可以定义在一个二维 derivative-value lattice 加三条 block access responses 上。

这**不意味着**优化问题从此自动简单；补充 19 已证明每条 block access response 本身可以承载任意 primitive-row complexity。

## 8. 示例

### `2+3=5`

三个 blocks 都是素数，所以 derivative image generator 都是 1，且

\[
\kappa_n(t)=|t|.
\]

于是

\[
K(u,v)=\max(|u|,|v|,|u+v|),
\qquad
W=2v-3u.
\]

点 `(0,1)` 给出

\[
(K,\eta)=(1,2),
\]

点 `(1,1)` 给出

\[
(K,\eta)=(2,1).
\]

所以 compressed lattice 直接重建

\[
\boxed{\mathcal P(2,3,5)=\{(1,2),(2,1)\}.}
\]

### `1+8=9`

unit block 强制 `t_a=0`。Derivative images 为

\[
t_8\in12\mathbb Z,
\qquad
t_9\in6\mathbb Z,
\]

而 additivity 要求 `t_8=t_9`。因此最小非零 compressed state 是

\[
(0,12,12).
\]

对应 block access radii 为 `(0,1,2)`，所以

\[
\mu=2.
\]

Wronskian 为 `12`，恰好等于 residual product，因此 `eta=1`。

无需保留单独的 prime coordinate 即可重获此前 fine-lattice 结果。

### `1+242=243`

Floor compressed state 为

\[
(t_1,t_{242},t_{243})=(0,4455,4455).
\]

exact block radii 为

\[
(0,27,11),
\]

故

\[
\boxed{\nu=27,\qquad\eta=5.}
\]

这把补充 15 的 unit-relation decomposition 恢复为一般 block-value quotient 的 rank-one boundary。

## 9. 这个 quotient 对什么不安全

映射

\[
\text{fine prime-coordinate witness}
\mapsto
(t_a,t_b,t_c)
\]

**没有**主张保留：

- 哪些 prime coordinates 承担证书；
- witness multiplicity/counts；
- block 内 exact decomposition identity；
- 任何会对两个拥有相同 derivative value 的 prime-coordinate representatives 作不同处理的后续运算。

若这些 observables 被加入 future language，P023 要求使用更细状态。

因此这只是 future-language-specific exact quotient，而不是“prime-factor coordinates 不真实或永远可以丢掉”的本体论主张。

## 10. 架构后果

补充 13–20 现在暴露出一条嵌套 decomposition：

\[
\boxed{
\text{fine prime coordinates}
\to
\text{block access response}
\to
\text{block derivative values }(t_a,t_b,t_c)
\to
\text{rank-two relation lattice }\Lambda_{abc}
\to
\text{norm/Wronskian certificate queries}.
}
\]

Block 内部复杂度可以 universal，但 relation coupling 仍然把**全局 certificate interaction** 压到两个 derivative-value coordinates。

这正是 P023 所要求表达的区别：minimum sufficient state 必须由 future language 索引。

## 11. Prior-art 边界

Integer linear-form images、disjoint coordinate blocks 的 product decomposition、congruence lattices 与 quotient-fiber optimization 都是标准数学。P025 不对这些一般事实主张创新。

项目侧继续检验的是以下对象的 exact integration：

- Pasten arithmetic derivative blocks；
- 补充 16–18 的 finite block access precision；
- derivative-value relation lattice；
- norm/absorption Pareto certificate language。

该 packaged interface 的历史创新状态仍为 `NOVELTY_UNVERIFIED`。

## 12. 可执行资产

新增：

- `src/enterprise_math/abc_block_value_quotient.py`
  - exact block target membership 与 access cost；
  - compressed derivative-value lattice membership；
  - Wronskian/absorption evaluation；
  - bounded block-value Pareto oracle；
  - fine-vs-block Pareto cross-checks。
- `tests/test_abc_block_value_quotient.py`
  - `2+3=5` frontier reconstruction；
  - `1+8=9` compressed witness；
  - `1+242=243` floor access；
  - 当前 small reference examples 上 fine/block frontier equality。

## 13. 下一前沿

没有 hard block。继续：

1. 由三个 block image generators 推导 `Lambda_abc` 的 compact basis / Smith 描述；
2. 直接把此前 `eta_min` block formula 恢复为 `W` 在 `Lambda_abc` 上的 image generator；
3. 检验 relation-lattice geometry + finite block capacity frontiers 是否能给 `mu` 或 `nu` 更强界；
4. 从一个 Wronskian observable 推广到多个 simultaneous certificate linear forms；
5. 对每个 enriched block-value future language 确定 P023-minimal state。
