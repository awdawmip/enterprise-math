# A2——操作—商对偶补充 01：混合上下文细化

状态：`PROVED_WIP / EXECUTABLE_WITNESSED / NOT CANONICAL_MAIN`  
母文档：`docs/A2_OPERATION_QUOTIENT_DUALITY.zh-CN.md`  
范围：future language 增长、admissible congruences、mixed future contexts，以及 fixed-block gcd witness

## 1. 抽象 incidence relation

对 `X` 上一个 total operation family `A`，定义 admissible quotient family：

\[
\operatorname{Adm}(\mathcal A)
=
\operatorname{Con}(X,\mathcal A),
\]

即被 `A` 中每一个 operation 保持的 equivalence relations。

对 quotient kernel `theta`，令 `Pol(theta)` 表示全部保持 `theta` 的 finitary operations。

则最基本的 incidence relation 是

\[
\boxed{
\mathcal A\subseteq\operatorname{Pol}(\theta)
\iff
\theta\in\operatorname{Adm}(\mathcal A).
}
\]

这就是经典 operation–relation `Pol/Inv` 视角限制到 equivalence relations/congruences 后的形式。Enterprise Math 只是把它作为 causal quotient 的记账骨架；Galois machinery 本身属于 prior art。

## 2. A2-OQD-S1-T01——增加 required operations 会删除 admissible quotients

对任意 total operation families `A,B`：

\[
\boxed{
\operatorname{Adm}(\mathcal A\cup\mathcal B)
=
\operatorname{Adm}(\mathcal A)
\cap
\operatorname{Adm}(\mathcal B).
}
\]

一个 quotient 与 union 兼容，当且仅当它分别与两个 families 都兼容。

因此

\[
\mathcal A\subseteq\mathcal B
\Longrightarrow
\operatorname{Adm}(\mathcal B)
\subseteq
\operatorname{Adm}(\mathcal A).
\]

这正是 Stage-3 fixed-block 规律

\[
\mathcal D(U\cup W)=\mathcal D(U)\cap\mathcal D(W)
\]

的非标量一般化。fixed-block divisor sets 只是 general admissible-congruence family 的一个参数化切片。

## 3. A2-OQD-S1-T02——future-language 增长会单调细化 selected quotient

固定 observation `O`。令母文档中的 observation-selected natural quotient kernel 为

\[
\Theta_{\mathcal A,O}
=
\max\{\rho\in\operatorname{Adm}(\mathcal A):\rho\subseteq\ker O\}.
\]

若

\[
\mathcal A\subseteq\mathcal B,
\]

则每一个 `B`-compatible relation 都必然也是 `A`-compatible，所以

\[
\boxed{
\Theta_{\mathcal B,O}
\subseteq
\Theta_{\mathcal A,O}.
}
\]

因此 future capability 越丰富，当前 state 必须单调保留更多 detail。

这与 Stage-3 的负结果并不矛盾：两个任意 quotient refinements 的 safe-operation sets 一般不可比较。这里的 monotonicity 发生在**固定 observation、扩大 future language**这条轴上，而不是任意 partition-refinement 轴上。

所以现在可以把原来的表面矛盾拆开：

- `partition 更细 => safe operations 更多/更少`：没有一般单调律；
- `required language 更大 => selected future-safe quotient 更细`：存在严格单调方向。

## 4. A2-OQD-S1-T03——mixed contexts 可以强迫比分别 minimization 更强的 refinement

一个很自然但错误的猜想是

\[
\Theta_{\mathcal A\cup\mathcal B,O}
=
\Theta_{\mathcal A,O}
\cap
\Theta_{\mathcal B,O}.
\]

一般并不成立。

普遍只能保证

\[
\boxed{
\Theta_{\mathcal A\cup\mathcal B,O}
\subseteq
\Theta_{\mathcal A,O}
\cap
\Theta_{\mathcal B,O},
}
\]

而且可以严格小于。

原因是 causal：union language 允许在 `A` 与 `B` 的 operations 之间交替形成 **mixed contexts/compositions**。把两个分别最小化后的 quotients 做 relation intersection，并不能保证这个新 partition 对任一 family 仍保持 compatibility，因为 classes 已经被重新切细，而 operation images 没有同步改变。

因此 natural quotient 必须从**闭合后的 combined language**一次性计算，不能先对每种 capability 单独 minimize，最后再机械 intersect outputs。

## 5. A2-OQD-S1-W01——精确 fixed-block witness：`+2` 与 `+3` 合在一起产生新区别

取

\[
O=q_6,
\qquad
q_6(n)=\left\lfloor\frac n6\right\rfloor.
\]

令

\[
\mathcal A=\langle+2\rangle,
\qquad
\mathcal B=\langle+3\rangle.
\]

按 Stage-3 gcd refinement：

\[
\Theta_{\mathcal A,q_6}=\ker q_2,
\qquad
\Theta_{\mathcal B,q_6}=\ker q_3.
\]

states `0` 与 `1` 在这两个 relations 中都仍不可区分：

\[
q_2(0)=q_2(1),
\qquad
q_3(0)=q_3(1).
\]

所以

\[
(0,1)\in
\ker q_2\cap\ker q_3.
\]

但 combined language 含 mixed future word

\[
+2\ ;\ +3,
\]

实际就是 translation `+5`。于是

\[
q_6(0+5)=0,
\qquad
q_6(1+5)=1.
\]

因此 `0` 与 `1` 只有在两种 capability 同时存在以后才变成 future-distinguishable。

又因为

\[
\gcd(6,2,3)=1,
\]

Stage 3 给出

\[
\boxed{
\Theta_{\mathcal A\cup\mathcal B,q_6}
=\ker q_1
=\Delta_{\mathbb N_0}.
}
\]

所以

\[
\boxed{
\Theta_{\mathcal A\cup\mathcal B,q_6}
\subsetneq
\Theta_{\mathcal A,q_6}
\cap
\Theta_{\mathcal B,q_6}.
}
\]

这是 **mixed-context refinement synergy** 的一个精确 causal witness。

## 6. 为什么 admissible-family intersection law 与 selected-kernel failure 不矛盾

T01 与 T03 没有矛盾。

T01 说的是**所有 compatible quotients 的集合**：

\[
\operatorname{Adm}(\mathcal A\cup\mathcal B)
=
\operatorname{Adm}(\mathcal A)\cap\operatorname{Adm}(\mathcal B).
\]

T03 说的是：固定 observation 后，从 admissible set 中选出的**最大那个 element**如何变化。

relation

\[
\Theta_{\mathcal A,O}\cap\Theta_{\mathcal B,O}
\]

本身未必还属于任一 admissible family。equivalence relations 的 intersection 会让 output classes 变得更细，但 operation images 没有变化，因此 operation compatibility 可能被破坏。

在 `q_6` witness 中，`ker q_2 cap ker q_3` 仍把 `0,1` 合在一起，但它并不对 combined translation language 稳定；mixed `+5` context 立即暴露缺失的 distinction。

所以“把 valid-scale sets 取 intersection”与“把 separately selected quotient kernels 取 intersection”是两个完全不同的操作。

## 7. A2-OQD-S1-C01——composition closure 具有真实 causal 内容

这个结果精确解释了为什么 P023 必须对 future language 做 operation-word closure。

一个 state representation 不能因为每个 generator 单独 audit 时都显得无害，就被判断为安全。generated algebra/monoid 可能包含任何一个 one-generator sublanguage 中都不存在的新 contexts。

因此真正的对象是

\[
\boxed{
\langle\mathcal A\rangle_{\mathrm{context/composition}},
}
\]

而不是 primitive operations 的无序清单。

这也把 Stage-3 的用户层规则“新增 future capability 会删除不安全 scales”推进了一步：新增 generators 可能产生**新的 mixed words**，所以 union language 的 information cost 可以严格高于“分别 repair 两次以后简单取 meet”得到的 naïve 结果。

## 8. 再看 P008 operation-language hierarchy

当前 hierarchy 可以理解成对 admissible quotient geometry 的逐层限制：

\[
\{\min,\max\}
\Rightarrow
\text{convex interval congruences},
\]

在 Stage-3 fixed-translation hypotheses 下，

\[
\{\min,\max,+t\}
\Rightarrow
\text{periodically transported interval geometry},
\]

而

\[
\{\min,\max,+\}
\Rightarrow
\Delta,
\]

因为 binary addition 的 elementary translations 自动包含 `+1`。

当多个 restricted translations 被加入时，真正决定 future-safe refinement 的是它们**生成的 additive monoid**，而不是把 generators 分别观看。fixed-block regime 中的 gcd formula 正是这个 generated-language effect 的闭式解。

## 9. Prior-art boundary

`Pol/Inv` operation–relation Galois 视角、congruence lattices、semigroup/action closure 与 context minimization 都属于经典数学。

Enterprise Math 当前接受 pressure test 的，是它们在 causal/P008 体系中的具体 specialization：

- 区分 admissible-quotient-set intersection 与 selected-kernel intersection；
- 给出显式 P008/fixed-block `(+2,+3)` mixed-context witness；
- 明确 capability composition 会强迫任何一个 isolated capability 都没有单独要求的新 detail；
- 把 Stage-3 gcd law 放入一般 operation-language closure 中。

不对 generic clone/Galois/automata 理论作 novelty claim。
