# Causal Operation Closure Core —— 由未来操作生成最小状态，再由状态生成零成本操作包络

状态：`ACTIVE CROSS-ROUTE RESEARCH WIP / EXACT FINITE THEOREMS + EXECUTABLE REFERENCE`

归属：A2/P023 应消费一般 quotient / congruence 母理论；A3 保留 finite compiler、LEGO/precision specialization。P008/P018/P011/P019 分别消费 completion、precision、collision spectrum 与 geometry bridge。

## 1. 核心顺序

本路线不再把 `precision` 当成先验标量。给：

- raw finite state set `X`；
- 当前离散 observation `O:X->Y`；
- 实际允许的 causal operation generators `G`。

先问：为了保证任意有限 future operation word 后 observation 仍 exact，哪些 raw states 真的可以合并？

定义：

\[
\boxed{
x\equiv_G y
\iff
O(w(x))=O(w(y))
\quad\forall w\in\langle G\rangle.}
\]

这里 `⟨G⟩` 是由 generators 经有限 composition 生成的 operation monoid；identity 对应空 future。

于是：

\[
\boxed{
E_G=\equiv_G
}
\]

是任务 `G` 的最小 exact causal state。

## 2. OC-01 —— 最粗 future-safe quotient

`E_G` 有三条立即性质：

1. `E_G` refinement 当前 observation kernel：
   \[
   xE_Gy\Rightarrow O(x)=O(y);
   \]
2. 每个 `g in G` 保持 `E_G`：
   \[
   xE_Gy\Rightarrow g(x)E_Gg(y);
   \]
3. 若任意另一个 equivalence `Q` 同时满足 observation-safe 且所有 `g in G` 都能下降，则：
   \[
   \boxed{Q\subseteq E_G.}
   \]

所以 `E_G` 是所有 exact deterministic future-state summaries 中最粗的一个。

等价写法：

\[
\boxed{
E_G
=
\bigcap_{w\in\langle G\rangle}
\ker(O\circ w).
}
\]

## 3. OC-02 —— finite partition refinement compiler

有限 `X` 上从：

\[
P_0=\ker O
\]

开始，递归：

\[
P_{t+1}(x)
=
\Bigl(
O(x),
(P_t(g(x)))_{g\in G}
\Bigr).
\]

只要 partition 仍发生 strict split 就继续。

稳定 partition `P_*` 精确等于 `E_G`。

这是 `CAUSAL_SIGNATURE_CORE` 的 finite operation-language specialization：`P_t` 表示所有长度不超过 `t` 的 future words 所能看到的 distinction。

实现：

- `causal_operation_language.py`
- `tests/test_causal_operation_language.py`

## 4. OC-03 —— future language inclusion 单调细化 state

若：

\[
G\subseteq H,
\]

则：

\[
\boxed{E_H\subseteq E_G.}
\]

解释：允许的未来能力越多，能够永久安全忘掉的 distinction 只能减少。

这与“任意两个现成 quotient 的 safe-operation sets 一般不可比较”不矛盾：这里比较的是**从同一个 observation 出发，由 future closure 自动生成的 minimum states**。

## 5. OC-04 —— zero-cost operation extension

当前任务为 `G`，最小 state 为 `E_G`。新增 operation family `H`。

则：

\[
\boxed{
E_{G\cup H}=E_G
\iff
h\text{ 保持 }E_G\quad\forall h\in H.
}
\]

因此判断新增能力是否需要“提高精度”不需要猜数值尺度：

> 直接检查新增 operation 是否能在当前 quotient 上 well-defined。

若能，新增能力对 state 是 `ZERO_COST`；若不能，自动 refinement 到 `E_(G∪H)`。

实现：

- `causal_operation_extension.py`
- `tests/test_causal_operation_extension.py`

## 6. OC-05 —— operation-language coupling defect

两个任务分别最小化：

\[
E_G,\qquad E_H.
\]

只把两个结果静态叠加会得到 common refinement：

\[
E_G\wedge E_H.
\]

但联合任务允许 `G/H` operations 交错 composition，因此一般只有：

\[
\boxed{
E_{G\cup H}
\subseteq
E_G\wedge E_H,
}
\]

且可以严格。

### 最小 4-state 反例

`X={0,1,2,3}`，只有 state `3` 当前可见：

\[
O(0)=O(1)=O(2)=0,
\qquad O(3)=1.
\]

定义：

\[
g:0\mapsto0,\ 1\mapsto0,\ 2\mapsto1,\ 3\mapsto0,
\]

\[
h:0\mapsto0,\ 1\mapsto3,\ 2\mapsto0,\ 3\mapsto0.
\]

单独 `g` 无法区分 `0,2`；单独 `h` 也无法区分 `0,2`。

但联合 future：

\[
2\xrightarrow{g}1\xrightarrow{h}3,
\]

而：

\[
0\xrightarrow{g}0\xrightarrow{h}0.
\]

所以 mixed word `(g,h)` 在 depth 2 首次暴露新 distinction。

定义 class defect：

\[
\boxed{
\Xi_0(G,H)
=|X/E_{G\cup H}|-|X/(E_G\wedge E_H)|.
}
\]

并用 P011 collision spectrum 定义：

\[
\boxed{
\Xi_k(G,H)
=J_k(E_G\wedge E_H)-J_k(E_{G\cup H}),
\qquad k\ge1.
}
\]

所有坐标非负；`J_0=#classes` 不属于 collision coordinates，单独用 `Xi_0` 记录。

还可定义最短 mixed witness depth。

## 7. OC-06 —— 任意有限元 operation 不需要新 compiler

对 `r` 元 operation：

\[
\omega(x_1,\ldots,x_r),
\]

冻结除第 `i` 个 argument 外所有伙伴，得到 elementary one-hole context：

\[
\boxed{
T_{\omega,i,\mathbf a}(x)
=
\omega(a_1,\ldots,x,\ldots,a_r).
}
\]

所有 finite one-hole term contexts 都由这些 elementary contexts 经 composition 生成。

因此：

\[
\boxed{
\text{finitary contextual congruence}
=
\text{elementary-context unary future closure}.
}
\]

这一步的 algebraic 形式属于成熟 universal algebra：translation / elementary translation / congruence compatibility 均有标准前人工作。本项目不主张该一般代数事实原创。

项目性意义在于：

\[
\text{unary dynamics}
+\text{binary LEGO join}
+\text{higher-arity operation}
\]

现在全部共享同一个 causal future-state compiler。

实现：

- `causal_term_context.py`
- `tests/test_causal_term_context.py`

## 8. OC-07 —— state collapse 同时诱导 operation collapse

固定 finite state quotient `E`，classes：

\[
B_1,\ldots,B_c.
\]

定义 full zero-cost semantic envelope：

\[
\boxed{
\mathrm{Safe}(E)
=
\{f:X\to X:\ xEy\Rightarrow f(x)Ef(y)\}.
}
\]

每个 `f in Safe(E)` 唯一诱导 coarse endomap：

\[
\bar f:X/E\to X/E.
\]

故有满射：

\[
\boxed{
\Pi_E:
\mathrm{Safe}(E)
\twoheadrightarrow
\mathrm{End}(X/E).
}
\]

### 固定 coarse operation 的 raw lift multiplicity

若 coarse map：

\[
\phi:\{1,\ldots,c\}\to\{1,\ldots,c\},
\]

则：

\[
\boxed{
m(\phi)
=
\prod_{i=1}^{c}|B_{\phi(i)}|^{|B_i|}.}
\]

总 safe raw operation 数：

\[
\boxed{
|\mathrm{Safe}(E)|
=
\prod_i
\left(
\sum_j |B_j|^{|B_i|}
\right).
}
\]

因此一次 state collapse 同时产生：

- hidden microstate fibers；
- hidden microdynamics fibers。

后者同样可定义 P011 spectrum：

\[
\boxed{
J_k^{op}(E)
=
\sum_{\phi}
\binom{m(\phi)}k.
}
\]

### uniform classes

若有 `c` 个等大 classes，每个 size `b`，raw state 数：

\[
n=bc,
\]

则每个 coarse endomap 都恰有：

\[
\boxed{b^n}
\]

个 raw lifts；共有：

\[
\boxed{c^c}
\]

个 coarse endomaps，因此：

\[
\boxed{
|\mathrm{Safe}(E)|=c^c b^n.
}
\]

实现：

- `causal_operation_projection.py`
- `tests/test_causal_operation_projection.py`

## 9. OC-08 —— full safe-operation envelope 几乎唯一确定 quotient

对同一个 raw set `X` 的 equivalences `E,F`，除两个极端外：

\[
\boxed{
E\ne F
\Longrightarrow
\mathrm{Safe}(E)\ne\mathrm{Safe}(F).
}
\]

唯一退化对是：

- discrete equality partition；
- indiscrete total-collapse partition。

二者都允许所有 raw endomaps，所以 full safe monoid 相同。

### 非恒定 observation 消除退化

若当前 observation `O` 非恒定，任何合法 causal state 必须满足：

\[
E\subseteq\ker O.
\]

indiscrete total collapse 不再允许。因此对所有 `O`-refining partitions：

\[
\boxed{
\mathrm{Safe}(E)=\mathrm{Safe}(F)
\Longrightarrow E=F.
}
\]

所以有限离散 regime 中：

> 完整 zero-cost operation envelope + 非恒定 current observation 可以唯一反推出 state quotient。

注意：一个实际物理/工程 operation language `G` 通常只是 `Safe(E)` 的很小子集，因此**少量 observed operations 不能反推出唯一 state ontology**。

实现：

- `causal_operation_state_duality.py`
- `tests/test_causal_operation_state_duality.py`

## 10. Canonical state-operation pair

由必需 operation language `G` 先生成 minimum state：

\[
E_G.
\]

再取它的 maximal zero-cost envelope：

\[
\mathrm{Safe}(E_G).
\]

得到：

\[
\boxed{
\mathfrak C(O,G)
=
(E_G,\mathrm{Safe}(E_G)).
}
\]

含义：

1. `E_G`：为了执行 `G`，系统至少必须保留的 distinction；
2. `Safe(E_G)`：在不新增 state distinction 的前提下，可以无损下降到该 quotient 的全部数学 operations。

并且：

\[
\boxed{
E_{\mathrm{Safe}(E_G)}=E_G.
}
\]

因此这是一对互相闭合的 state/operation 语义。

但 `Safe(E_G)` 不是物理 law：它包含可能非常非局域、现实中不可实现的 raw maps。Primitive causal law 仍然是 `G`；full envelope 只是 compatibility bound。

## 11. 与 P008/P018 的统一

P008 complete-growth quotient：

\[
q_V(n)=R_V(n)
\]

只是这里的一类 observation/collapse。

若只允许 additive translations，则研究的是 full `Safe(E)` 中一个特定 typed operation family：

\[
n\mapsto n+t.
\]

此前得到的 safe-translation monoid、periodic basin rigidity、polynomial no-go 都是 OC-01/OC-04 在该 operation family 中的闭式 specialization。

固定 block `d` 中：

\[
q_d(n)=\lfloor n/d\rfloor,
\]

future generators `U` 导出的 minimum refinement：

\[
\boxed{
g=\gcd(d,U),\qquad q_g}
\]

正是 `E_G` 在 additive-block regime 的闭式解。

所以 P018 `precision refinement` 可进一步解释为：

\[
\boxed{
\text{operation language expansion}
\to
\text{minimum congruent state refinement}.
}
\]

## 12. 当前研究边界

尚未完成：

- infinite-state operation-language compiler；
- locality-constrained safe envelope，而不是全部 set endomaps；
- stochastic / quantum channels；
- operation-fiber 与 physical microdynamics 的实验 bridge；
- Lean formalization；
- full clean-integration CI。

本文件中的 universal-algebra congruence/translation 事实属于成熟数学；项目当前真正需要审查的新主张集中在：causal interpretation、operation-language coupling spectrum、P011 operation fibers、与 P008/P018/P023/P019 的统一，以及 physical falsification contract。
