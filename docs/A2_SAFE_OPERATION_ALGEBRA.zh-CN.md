# A2——安全操作代数与完整增长操作谱

状态：`PROVED_WIP / EXECUTABLE_CHECKED / NOT CANONICAL_MAIN`  
归属：A2 future-compatible quotient 母层  
消费：当前 canonical `EnterpriseMath/Quotient/OperationCongruence.lean`、P023 operation-family closure、P024 action-language precision，以及冻结于 `checkpoint/causal-absorption-20260809-stage3@d6944dad829c95c8e38022ab091c2d5c91087dfa` 的 stage-3 P008 complete-growth basin 结果。

## 1. 为什么“精度”不再适合作为第一原语

设

\[
q:X\to Q,
\qquad
\theta=\ker q.
\]

canonical A2 已经给出：一个 `k` 元操作 `mu:X^k->X` 能穿过这次 collapse，当且仅当逐坐标的 `theta`-等价必然推出输出仍 `theta`-等价。等价地说，`mu` 唯一诱导一个 `Q` 上的操作。

stage-3 的 P008 结果因此指向一个更直接的对象：与其把系统描述成一个 scalar precision，不如描述成

\[
\boxed{
(\text{causal quotient }\theta,
\text{surviving operation algebra}).
}
\]

本笔记把这件事精确化，同时明确区分：经典数学已经完整覆盖的“绝对安全操作全集”，与项目真正需要研究的“自然操作谱”。

## 2. A2-SOA-T01——绝对 unary safe monoid

对 quotient `q:X->Q`，定义

\[
\operatorname{Safe}_1(q)
=
\{f:X\to X:q(x)=q(y)\Rightarrow q(f(x))=q(f(y))\}.
\]

`Safe_1(q)` 包含 identity，并对 composition 闭合。

更强地，每个 safe `f` 唯一等价于以下数据：

\[
\boxed{
\bar f:Q\to Q,
\qquad
f_a:q^{-1}(a)\to q^{-1}(\bar f(a))
\quad(a\in Q).
}
\]

也就是先决定 coarse class 如何运动，再在每一个源 fiber 内任意选择进入目标 fiber 的具体 fine map。反过来，任何这样的 coarse map 加 fiber maps 都定义一个 safe endomap。

这正是经典的“保持/稳定某个 partition 的 transformation semigroup”，通常写成 `T(X,P)`。Enterprise Math 不把这个一般 semigroup 本身作为新数学主张。

## 3. A2-SOA-T02——全部有限元 safe operations 构成 equivalence polymorphism clone

对每个 arity `r>=1`，令 `Safe_r(q)` 为所有满足

\[
x_i\mathrel\theta y_i\ \forall i
\Longrightarrow
\mu(x_1,\ldots,x_r)\mathrel\theta\mu(y_1,\ldots,y_r)
\]

的操作

\[
\mu:X^r\to X.
\]

按 arity 分层的全集

\[
\boxed{
\operatorname{Safe}(q)=\bigcup_{r\ge1}\operatorname{Safe}_r(q)
}
\]

包含所有 projections，并对 superposition 闭合。它正是 equivalence relation `theta` 的经典 polymorphism clone：`Pol(theta)`。

因此，“绝对意义下完整的 safe-operation algebra”本身已经属于成熟 universal algebra。Enterprise Math 的研究前沿不应是重新命名这个 clone，而应是把它与 causal model 真正宣称为自然的操作族相交。

## 4. A2-SOA-T03——精确 fiber decomposition 与有限计数

设 `X` 有限，quotient fibers 的大小为

\[
m_a=|q^{-1}(a)|,
\qquad a\in Q.
\]

固定一个 coarse input tuple

\[
\mathbf a=(a_1,\ldots,a_r)\in Q^r,
\]

其上共有

\[
D_{\mathbf a}=\prod_i m_{a_i}
\]

个 fine input tuples。一个 safe fine operation 必须先为这个 coarse tuple 选择单一 output coarse class `b`，随后可以把这 `D_a` 个 fine inputs 任意映入 `b` 对应的 fiber。

因此

\[
\boxed{
|\operatorname{Safe}_r(q)|
=
\prod_{\mathbf a\in Q^r}
\left(
\sum_{b\in Q}m_b^{D_{\mathbf a}}
\right).
}
\]

若 `k=|Q|` 个 fibers 全都具有同一大小 `m`，则

\[
\boxed{
|\operatorname{Safe}_r(q)|
=
k^{k^r}m^{k^r m^r}.
}
\]

新增 executable reference 已在小型非均匀 partition 上，对 unary 与 binary operation 进行全枚举并与闭式计数逐项吻合。

这个计数属于 elementary/classical partition-preserving algebra；这里记录它的目的，是明确“绝对安全操作全集”到底有多大，而不是提出 priority claim。

## 5. A2-SOA-D01——natural operation spectrum

令 `A` 是 fine world 中被明确声明的 ambient operation family：它可以是 arithmetic operations、causal updates、物理允许的 transitions，或其他 typed operation algebra。

定义 **natural safe-operation spectrum**：

\[
\boxed{
\operatorname{Spec}_{\mathcal A}(q)
=
\mathcal A\cap\operatorname{Pol}(\ker q).
}
\]

对每一个 surviving operation，canonical A2 descent 都给出唯一的 coarse operation。因此一个 coarse causal state 更准确的对象不是“quotient + 外加 scalar precision”，而是“quotient + 它真正诱导出的 surviving algebra”。

这个定义也解释了 stage-3 的重要负结果：partition 更细，并不意味着 safe-operation set 单调增大或减小。equality relation 与 universal relation 都被所有操作保持，而中间的 equivalence 反而可能施加真实限制。因此 refinement order 与 safe-operation inclusion 根本不是同一个序。

## 6. A2-SOA-T04——safe translations 不能唯一识别 complete-growth quotient

translation spectrum 可以恢复一个 natural period capacity，却未必能恢复 basin word。

考虑 `N_0` 上两个 P008 growth laws：

\[
V_1(k)=3k,
\]

其 basin width 恒为 `3`；以及

\[
V_2(2m)=3m,
\qquad
V_2(2m+1)=3m+1,
\]

其 primitive width word 为

\[
(1,2,1,2,\ldots).
\]

这两个 quotients 的完整 global safe-translation monoid 都是

\[
\boxed{3\mathbb N_0.}
\]

但 quotient 显然不同：前者每个 period 只有一个 width-3 basin；后者每个 period 有 width `1,2` 两个 basins。因此

\[
\boxed{
\text{translation-safe monoid}\not\Rightarrow\text{unique quotient geometry}.
}
\]

最小正 generator `3` 是真实的 **period capacity**，但不是 causal partition 的完整描述。

这也修正并加强 stage-3 的 gcd 结论：若事先把候选 quotient 限定为 uniform blocks，则 `gcd(U)` 确实是由 supplied translations 强制出的最大 exact block scale；一旦离开 uniform-block candidate family，同一个 translation spectrum 可以对应不同的 periodic basin geometries。

## 7. A2-SOA-T05——完整 concrete safe unary monoid 可反推一切非退化 partition

令 `theta` 是 `X` 上一个 nontrivial proper equivalence：既不是 equality，也不是 universal relation。令

\[
M=\operatorname{Safe}_1(q)=T(X,P)
\]

为作用在 `X` 上的**完整 concrete** partition-preserving transformation monoid。

那么，被 `M` 中每一个 map 同时保持的 equivalence relations 只有

\[
\boxed{\Delta_X,\ \theta,\ \nabla_X.}
\]

### 证明

若某个 invariant equivalence `E` 把同一个 `theta`-block 中两个不同点关联起来，那么 partition-preserving map 可以把这两个点送到任意一个目标 block 内的任意两个点。因此 `E` 必须包含所有 within-block pairs，即 `theta subseteq E`。

若 `E` 关联了来自两个不同 `theta`-blocks 的点，则 partition-preserving maps 可以把这两个 source blocks 分别送到任意 target blocks，并把选定的两个点送到任意 target points。于是任意两点都必须 `E`-related，因此 `E=nabla_X`。

如果上述两种情况都没有发生，则只能有 `E=Delta_X`。所以唯一剩下的 nontrivial proper invariant equivalence 就是 `theta`。∎

因此，除 `theta=Delta_X` 与 `theta=nabla_X` 这两个退化端点外（两者的 full safe unary monoid 都等于 full transformation monoid），**完整 concrete safe unary monoid 确实唯一确定 quotient kernel**。

对 ordered P008 interval quotient，一旦 kernel 被恢复，ordered basin partition 也随之恢复；固定 level origin 后，complete-growth boundary sequence 即可恢复。

这是一个 full partition-preserving monoid 的 reverse-identifiability 结果；在完成更细 prior-art 对照前，不对其历史原创性作 priority claim。

## 8. A2-SOA-T06——P008 complete-growth 的 successor rigidity

设

\[
V(0)=0<V(1)<V(2)<\cdots
\]

且 `q_V` 为 P008 level quotient，其 basin 为

\[
I_k=[V(k),V(k+1)-1].
\]

则 unary successor

\[
s(n)=n+1
\]

安全当且仅当每个 basin 都是 singleton：

\[
\boxed{
+1\text{ safe}
\iff
V(k+1)-V(k)=1\ \forall k.
}
\]

若某个 basin width 大于 `1`，取其第一点 `x=V(k)` 与最后一点 `y=V(k+1)-1`。二者当前满足 `q_V(x)=q_V(y)=k`，但

\[
q_V(x+1)=k,
\qquad
q_V(y+1)=k+1.
\]

反向则显然，因为此时 quotient 就是 exact equality。

所以，最小的普通正 additive step 已经足以强迫全部 basin detail 成为因果必需状态。

## 9. A2-SOA-T07——普通 binary addition 不允许任何非平凡 P008 quotient

令

\[
\mu_+(x,y)=x+y.
\]

则

\[
\boxed{
\mu_+\text{ descends through }q_V
\iff
q_V\text{ is the identity quotient}.
}
\]

如果 binary addition 能下降到 quotient，固定第二输入为 `1`，逐坐标 compatibility 立即推出 `x->x+1` 必须安全；T06 随即强迫每个 basin 为 singleton。反过来，equality quotient 显然支持 exact addition。

这严格区分了两个很容易混淆的概念：

- quotient 可以允许一个**外部 unary translation submonoid**，例如 `q_d(n)=floor(n/d)` 的 `d N_0`；
- 同一个 quotient 却未必允许 coarse state 自己拥有**任意 represented states 之间的内部 binary addition**。

对每个非平凡 fixed block `d>1`，前者成立，后者失败。

## 10. A2-SOA-T08——普通 binary multiplication 同样不允许非平凡的 unbounded P008 quotient

假设 boundary sequence `V(k)` 无界，令

\[
\mu_\times(x,y)=xy.
\]

则

\[
\boxed{
\mu_\times\text{ descends through }q_V
\iff
q_V\text{ is the identity quotient}.
}
\]

假设某个 basin 含有不同的 `x<y`。

若 `x=0`，选任意正 boundary `B`，再取 multiplier `a` 使 `ay>=B`；则 `ax=0` 仍在该 boundary 以下，而 `ay` 已经越过它。

若 `x>0`，选择一个 boundary 满足

\[
B>\frac{xy}{y-x},
\]

并令

\[
a=\left\lceil\frac By\right\rceil.
\]

则 `ay>=B`，而上述不等式保证 `ax<B`。于是 scalar map `n->an` 会区分 `x,y`。但若 binary multiplication 能下降，那么固定任意 scalar 后得到的 unary map 都必须安全，矛盾。

所以不存在 non-singleton basin。

因此，只要一个 complete-growth coarse world 坚持保留普通内部 semiring operations `(+ , ×)`，它就不可能同时保留任何非平凡的信息丢失型 P008 quotient。

## 11. 反向重建存在三个强度层级

上面的结果给出一个很清楚的 hierarchy。

### Restricted natural language

一个很小的 operation language 可能只能确定某个 scale invariant。stage-3 periodic translations 能确定 primitive period capacity，但不能确定完整 basin word。

### Full concrete safe algebra

完整 concrete partition-preserving unary monoid 可以恢复所有非退化 quotient kernels。这个对象数学上是完整的，但通常远大于任何真正自然的物理或算术 dynamics。

### Declared operations + observation/context

给定 declared future language 与 current observation 后，P023/P024 通过 future distinguishability / boundary pullback 构造 coarsest compatible refinement。这才是 operational 意义下产生 **natural quotient** 的路径：不是问“哪个 partition 恰好有很多 safe maps”，而是问“真实 future tasks 与 observations 到底强迫当前保留哪些区别”。

因此，当前 causal 主链更适合写成

\[
\boxed{
\text{causal law}
\to
\text{declared future/context language}
\to
\text{future-safe quotient}
\to
\text{complete-growth basin geometry}
\to
\text{surviving natural operation spectrum}.
}
\]

“precision”由此成为这个结构上的 coordinate / complexity measure，而不再是第一原语。

## 12. Prior-art boundary

以下一般结构均属于成熟数学，不作为 Enterprise Math novelty claim：

- partition-preserving / stabilizing full transformation semigroups `T(X,P)`；
- 保持 equivalence relation 的 operations 与 clone `Pol(theta)`；
- congruences、quotient algebras、clone superposition 与 partition refinement；
- Myhill–Nerode / future distinguishability 及其邻近的 finite-state minimization 思想。

直接相关文献包括：

- J. Araújo, W. Bentz, J. D. Mitchell, C. Schneider, *The rank of the semigroup of transformations stabilising a partition of a finite set*, arXiv:1404.1598；
- M. Sarkar, S. N. Singh, *On certain Semigroups of Transformations that preserve a partition*, arXiv:2006.04242；
- L. E. F. Diekouam, E. R. A. Temgoua, M. Tonga, *Meet-reducible submaximal clones determined by nontrivial equivalence relations*, arXiv:1611.06574，作为一个直接使用 `Pol(theta)` 的参考。

本项目当前真正处于 pressure-test 中的内容，是 P008 complete-growth specialization、translation-spectrum non-identifiability、addition/multiplication no-go，以及把 natural operation spectrum 作为“外加 scalar precision”替代物的 causal layering interpretation。

## 13. Executable evidence

新增 exact reference layer：

- `src/enterprise_math/safe_operation_algebra.py`；
- `tests/test_safe_operation_algebra.py`。

当前 bounded regressions 已核验：

1. unary finite census 与非均匀 `(2,1)` partition 上的全枚举一致；
2. binary finite census 与同一 partition 上全部 `3^9` 个 binary operation tables 的全枚举一致；
3. fixed-width complete growth 上的局部 `+1` obstruction；
4. `width 3` 与 periodic `widths (1,2)` 的 translation-spectrum non-identifiability；
5. full-safe-monoid reconstruction theorem 的若干小型 finite instances。

这些 tests 是 executable evidence，不替代上述证明。

## 14. 下一研究前沿

下一步真正值得分类的已经不再是“full safe clone 是什么”——这个答案属于经典数学。

真正的问题是

\[
\boxed{
\text{给定 complete-growth law }V
\text{ 与 natural ambient operation class }\mathcal A,
\text{分类 }\operatorname{Spec}_{\mathcal A}(q_V).
}
\]

优先级最高的 ambient classes 是：

1. 满足精确 P008 boundary-pullback constraint 的 monotone integer endomaps；
2. affine / polynomial integer maps，其中 growth degree 很可能产生更强的 no-go regime；
3. 不等同于普通 semiring operation 的 typed multi-input causal operations；
4. 由 LEGO redistribution / fiber composition 生成的 operations——这里 hidden relation rank 可能在普通算术已经不能下降时仍然存活。

只有走到这一层，“数、维、quotient、scale、operation”才开始可能闭成同一个系统，同时又不会把 classical universal algebra 误包装成新数学。
