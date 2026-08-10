# A2——操作—商对偶与 P008 的序结构核心

状态：`PROVED_WIP / EXECUTABLE_CHECKED / STACKED_ON_STAGE4 / NOT CANONICAL_MAIN`  
归属：A2 future-compatible quotient 母层  
消费：canonical P023/P024 quotient repair、canonical generic operation congruence，以及冻结于 `core/a2-safe-operation-algebra-v3@09450e3ac7a09e56895a2e6fdc6ecf0c521ba438` 的 Stage-4 safe-operation algebra。

## 1. 反向问题需要先修正一次

Stage 4 已经对 quotient

\[
q:X\to Q,
\qquad
\theta=\ker q
\]

相对于 declared ambient operation family `A` 定义 natural safe-operation spectrum：

\[
\operatorname{Spec}_{\mathcal A}(q)
=
\mathcal A\cap\operatorname{Pol}(\theta).
\]

一个很自然的想法是把箭头反过来：operation family 能不能唯一决定 natural quotient？

对 total operations 来说，若没有额外数据，答案是否定的。

正确的反向问题应改成：

> declared operation language 允许哪些 quotient geometries 成为 congruence；再加入当前 observation/context 后，其中哪一个 quotient 被唯一选中？

本笔记把这个区别精确化。

## 2. A2-OQD-T01——total operations 单独不可能唯一选出 quotient

令 `X` 至少包含两个 states，`A` 是 `X` 上任意 total finitary operations family。

等号关系

\[
\Delta_X
\]

与 universal relation

\[
\nabla_X
\]

永远都是 `A` 中每个 total operation 的 congruence。

因此

\[
\boxed{
|\operatorname{Con}(X,\mathcal A)|\ge2.
}
\]

也就是

\[
\boxed{
\text{total operation family 单独不可能选出唯一 quotient。}
}
\]

这不是理论缺陷。operation language 本来就更适合决定一个 **admissible congruence geometry/lattice**，而不是凭空制造某个 observed resolution。

这里故意只对 total operations 作结论。进入 legality-sensitive partial-operation theory 后，enabledness/domain membership 本身属于 future behavior；若同一 universal class 同时包含 enabled 与 disabled states，则 universal relation 不再兼容。因此 FQ-006 partial-operation 层是真正的扩展，而不是形式改写。

## 3. A2-OQD-T02——finitary congruence 精确归约为 unary elementary translations

设 `f:X^r->X` 为 total `r`-ary operation。固定一个 coordinate `i`，并固定其他全部 coordinates，就得到一个 unary map：

\[
T_{f,i,\mathbf a}(x)
=
f(a_1,\ldots,a_{i-1},x,a_{i+1},\ldots,a_r).
\]

它是 `f` 的 **elementary unary translation/context**。

对 equivalence relation `theta`，有

\[
\boxed{
\theta\text{ 是 }f\text{ 的 congruence}
\iff
\theta\text{ 被每一个 }T_{f,i,\mathbf a}\text{ 保持。}
}
\]

### 证明

正向显然：把其余 coordinates 固定即可。

反向假设每一个 elementary translation 都保持 `theta`。若

\[
x_j\mathrel\theta y_j
\qquad(j=1,\ldots,r),
\]

把 `(x_1,...,x_r)` 的输入逐坐标改成 `(y_1,...,y_r)`。每一步都只是某一个 elementary translation 作用在一对 `theta`-related states 上，所以 outputs 在每一步后仍 `theta`-related。最终得到

\[
f(x_1,\ldots,x_r)
\mathrel\theta
f(y_1,\ldots,y_r).
\]

证毕。

这是 classical universal algebra。对 Enterprise Math 的意义是执行层面的：**现有 unary finite-family P023 engine 在把基本 finitary operations 编译成 elementary translations 后，就已经足够处理任意 finite finitary operation language。** 不需要再造第二套 quotient-repair 母理论。

## 4. A2-OQD-T03——operation + observation 唯一选出最大兼容忘却关系

令 `A` 是 `X` 上一个 total finitary algebra，并令

\[
O:X\to Y
\]

表示当前 observation。令 `Pol_1(A)` 表示由 basic operations、identity 与 fixed parameters 生成的全部 unary polynomial/context maps。

定义

\[
\boxed{
\Theta_{\mathcal A,O}
=
\bigcap_{p\in\operatorname{Pol}_1(\mathcal A)}
\ker(O\circ p).
}
\]

等价地，

\[
x\mathrel{\Theta_{\mathcal A,O}}y
\iff
O(p(x))=O(p(y))
\quad
\text{对每一个 unary context }p.
\]

则：

1. `Theta_(A,O)` 是 equivalence relation；
2. `Theta_(A,O) subseteq ker O`，因为 identity context 在其中；
3. `Theta_(A,O)` 是 `A`-congruence；
4. 任意满足 `rho subseteq ker O` 的 `A`-congruence `rho` 都满足 `rho subseteq Theta_(A,O)`。

因此

\[
\boxed{
\Theta_{\mathcal A,O}
=
\max\{\rho\in\operatorname{Con}(X,\mathcal A):\rho\subseteq\ker O\}.
}
\]

换成 partition 语言：它就是**当前 observation 的所有 refinement 中，仍能让全部 required operations 精确下降的最粗那个 refinement**。

### 为什么 T03 是 congruence

设 basic operation `f` 的每一对输入都有 `x_i Theta y_i`。要比较任意 outer observation context `p` 下的

\[
p(f(x_1,\ldots,x_r))
\]

与对应的 `y_i` 版本，只需逐坐标替换。每一步中其他 inputs 都固定成 parameters，因此当前被改变的 coordinate 所看到的函数本身就是一个 unary polynomial context。按 `Theta` 的定义，该步不会改变最终 observation。于是最终 outputs 仍 `Theta`-equivalent。

### 为什么 T03 最大

若 `rho` 是 `ker O` 以下任意 congruence，则所有 polynomial/context operations 都保持 `rho`。所以 `x rho y` 会推出 `p(x) rho p(y)`；再由 `rho subseteq ker O` 得到对所有 `p` 都有 `O(p(x))=O(p(y))`。故 `rho subseteq Theta_(A,O)`。

这个 construction 属于标准 congruence/context 逻辑。finite unary case 下，它就是 canonical P023 已经实现的 operation-word future-distinguishability closure。

## 5. A2-OQD-C01——canonical P023 已经是一台 finitary congruence compiler

当 `X` 有限、basic finitary operations 数量有限时：

1. 把每个 basic operation 编译成全部 elementary unary translations；
2. 把这个 finite unary family 交给 canonical P023 `stable_family_partition`；
3. 从当前 observation partition 开始 refinement。

稳定结果精确等于 observation kernel 内最大的 algebra congruence，也就是与整个 finitary algebra 兼容的最粗 observation refinement。

新增 executable bridge：

- `src/enterprise_math/operation_quotient_duality.py`；
- `tests/test_operation_quotient_duality.py`。

实现明确复用 `src/enterprise_math/operation_quotient.py`，不复制 P023 refinement。

## 6. A2-OQD-T04——P008 interval quotients 精确保留 chain lattice

设

\[
V(0)=0<V(1)<V(2)<\cdots
\]

并定义 P008 quotient：

\[
q_V(n)=k
\iff
V(k)\le n<V(k+1).
\]

因为 basin classes 是按顺序排列的 intervals，`q_V` 是 monotone map。因此对任意 `x,y`：

\[
\boxed{
q_V(\min(x,y))
=
\min(q_V(x),q_V(y)),
}
\]

以及

\[
\boxed{
q_V(\max(x,y))
=
\max(q_V(x),q_V(y)).
}
\]

所以每一个 P008 complete-growth quotient 都是 lattice homomorphism：

\[
(\mathbb N_0,\min,\max)
\longrightarrow
(\mathbb N_0,\min,\max).
\]

由 `min`、`max`、projections 与 constants 生成的全部 lattice terms 都能精确下降。

这给 Stage-4 arithmetic no-go 一个正面的对照：

\[
\boxed{
\text{order lattice 在每一个 P008 interval collapse 中都存活，}
}
\]

而 ordinary addition、multiplication 与非平凡 polynomial unary arithmetic 在 nonlinear complete growth 中通常全部被摧毁。

## 7. A2-OQD-T05——convex partitions 精确等于 chain lattice congruences

令 `(C,<=)` 是一条 chain，并定义

\[
x\wedge y=\min(x,y),
\qquad
x\vee y=\max(x,y).
\]

`C` 上一个 equivalence relation `theta` 是 lattice congruence，当且仅当每个 `theta`-class 都是 convex。

### Congruence 推出 convexity

若

\[
a\le b\le c,
\qquad
a\mathrel\theta c,
\]

两侧同时 meet `b`：

\[
a\wedge b=a
\mathrel\theta
c\wedge b=b.
\]

所以 `a theta b`；类似地同时 join `b` 可得 `b theta c`。因此 related endpoints 之间整个 interval 都在同一 class 中。

### Convexity 推出 congruence

若所有 classes 都 convex，则 chain 中两个不同 classes 必然是互不交叠且全序排列的 intervals。因此 `min(x,y)` 所在 class 只依赖两个 input classes，并且就是较低的那个 class；`max` 同理落入较高 class。故 `min/max` 均可下降。

于是

\[
\boxed{
\operatorname{Con}(C,\min,\max)
=
\{\text{C 上全部 convex interval partitions}\}.
}
\]

当 `C=N_0` 时，P008 complete-growth quotients 正是其中这样一类特殊 chain-lattice congruences：successive classes 是有限 basins

\[
[V(k),V(k+1)-1]
\]

并且 quotient order type 仍为 `N_0`。

这是成熟 lattice theory，而不是 Enterprise Math novelty claim。它对项目真正重要的地方在于：**P008 basin geometry 现在可以由一个 operation algebra 生成/刻画，而不再只是人为先验规定“取 interval”。**

## 8. A2-OQD-C02——operation language 先决定 geometry class，再谈 scale

T01 与 T05 合起来给出正确的 reverse interpretation。

order language

\[
\mathcal L_{\mathrm{ord}}=\{\min,\max\}
\]

不会选出唯一 `V`。它先选出 admissible quotient geometry：

\[
\boxed{
\{\min,\max\}
\Longrightarrow
\text{convex/interval quotient classes}.
}
\]

再加入一个 fixed external translation `+t`。按照 Stage-3 P008 safe-translation hypotheses，只要某个固定正 step 能持续安全通过 quotient，basin boundary/width pattern 就被强迫进入 periodic transport。因此在 complete-growth regime 中：

\[
\boxed{
\{\min,\max,+t\}
\Longrightarrow
\text{periodically transported interval geometry}
}
\]

但 period capacity `t` 仍不能唯一决定 primitive width word。

反过来，若 language 含 ordinary internal binary addition，它的 elementary translations 自动包含全部

\[
x\mapsto x+a,
\]

特别包含 `+1`。Stage 4 随即强迫所有 basins 成为 singleton：

\[
\boxed{
\{\min,\max,+\}
\Longrightarrow
\text{identity quotient}.
}
\]

multiplication 也可由同一 elementary-translation 视角解释：internal binary multiplication 自动提供所有 scalar maps `x->ax`；Stage 4 已证明，只要 P008 boundaries 无界且存在 non-singleton basin，就总有某个 scalar 把同一 basin 内两点分开。

所以 operation signature 的差异不是纯语法差异；不同 operation languages 会真实地产生不同的 admissible quotient geometries。

## 9. A2-OQD-T06——fixed-block gcd theorem 是 restricted language 下 reverse closure 的闭式解

取当前 fixed-block observation

\[
q_d(n)=\left\lfloor\frac nd\right\rfloor
\]

并且只声明 external additive generators

\[
U=\{u_1,\ldots,u_r\}.
\]

Stage 3 已证明最粗 exact future-safe refinement 为

\[
q_g,
\qquad
\boxed{g=\gcd(d,u_1,\ldots,u_r)}.
\]

在当前语言下，这正是

\[
\boxed{
\Theta_{\langle+U\rangle,q_d}
=\ker q_g.
}
\]

所以 gcd 不是额外先验规定的 precision law。它是一般“operation + observation congruence closure”在 scalar fixed-block family 中的闭式值。

它的边界也因此很清楚：一般 causal quotient 完全可能没有任何单一 scalar `d` 可用来描述。

## 10. A2-OQD-C03——forward 与 reverse 现在闭合

causal algebra 现在可以写成两个耦合方向。

### Reverse / quotient selection

required total-operation language 首先决定 congruence lattice：

\[
\boxed{
\mathcal A_{\rm req}
\longmapsto
\operatorname{Con}(X,\mathcal A_{\rm req}).
}
\]

当前 observation/context 再在“已经可观察的区别不能被重新删除”这一条件下，选出最大的安全忘却关系：

\[
\boxed{
(\mathcal A_{\rm req},O)
\longmapsto
\Theta_{\mathcal A_{\rm req},O}
=
\max\bigl(
\operatorname{Con}(X,\mathcal A_{\rm req})
\cap\downarrow\ker O
\bigr).
}
\]

### Forward / surviving-operation audit

quotient `theta` 一旦固定，就可对更大的 candidate ambient language `B` 做 audit：

\[
\boxed{
\theta
\longmapsto
\operatorname{Spec}_{\mathcal B}(\theta)
=
\mathcal B\cap\operatorname{Pol}(\theta).
}
\]

若 `B=A_req`，required operations 按 construction 全部存活；若 `B` 更大，spectrum 则回答“还有哪些额外 operations 免费存活”。

因此得到完整闭环：

\[
\boxed{
\text{operation requirements}
\to
\text{admissible quotient geometry}
\to
\text{observation-selected natural quotient}
\to
\text{surviving operation spectrum}.
}
\]

只有当 selected quotient family 恰好允许 faithful scalar coordinate 时，才出现 scalar natural scale；fixed blocks 就是这种特殊情形。第一对象仍是 quotient，scale 只是可用时的一种 representation。

## 11. Partial-operation boundary

T01 只针对 total operations。对于 partial operation，若 compatibility 要保存 enabledness，则除了 enabled 后的 target compatibility，还必须要求

\[
x\mathrel\theta y
\Longrightarrow
(x\in D\iff y\in D).
\]

只要同时存在 enabled 与 disabled states，universal relation 就会失败。

所以 FQ-006 legality-sensitive extension 会真实改变 admissible congruence geometry，本身就是 total-operation duality 的扩展，不应被压扁回 total theory。

Equality 仍然兼容，因此 partial operations 可以减少 quotient-selection ambiguity，但并不自动保证完全消除全部 ambiguity。

## 12. Prior-art boundary

以下一般内容均属于经典数学，不作为 novelty claim：

- universal algebra 的 congruence lattices；
- elementary/fundamental unary translations 与 congruence testing；
- observation/context relation 以下最大的 operation-compatible indistinguishability；
- chain/lattice congruences 与 convex blocks；
- finite partition refinement / future distinguishability。

Enterprise Math 当前接受 pressure test 的，是把这些成熟结构与现有 P008/P018/P023/P024 complete-growth system 接成一条闭链：

1. `min/max` 精确刻画 P008 已经使用的 interval geometry；
2. Stage-3 translation rigidity 在 fixed positive step 存活后进一步把该 geometry 压到 periodic transport；
3. ordinary arithmetic 又把 admissible geometry 压到 equality；
4. fixed-block gcd refinement 是一般 observation-congruence closure 的 scalar closed form；
5. 所以 scalar precision 次于 selected causal quotient 与 surviving operation algebra。

## 13. Executable evidence

`operation_quotient_duality.py` 把 finite finitary operations 编译成 elementary unary translations，再委托 canonical P023 做 refinement。

当前 regressions 核验：

- 对 three-state set 的全部 partitions 与若干 binary algebras，direct finitary congruence test 与 elementary-translation compiler 一致；
- 编译器确实生成每一个 coordinate context；
- `min/max` 对 convex interval observation 不产生额外 refinement；
- `min` 能识别 nonconvex observation 并强迫进一步细化；
- total operation family 下 equality 与 universal relations 都是 congruence；
- irregular、square 与 cubic basin samples 上，P008 `min/max` identities 精确成立。

这些 tests 是 executable witnesses；上述定理依赖结构证明，而不是有限枚举。
