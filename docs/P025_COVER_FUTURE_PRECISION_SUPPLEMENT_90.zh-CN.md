# P025 补充 90 —— Future-Query-Relative Cover Precision 与自适应 Observation Order

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-cyclotomic-stage76`  
依赖：P025 补充 87–89  
硬阻断：`NONE`

## 1. 同一个 fine state 对应多个不同的 precision 问题

Stage 89 已把 odd-prime exponent cover 的 qualitative transport 压成两个 natural bits：

\[
R:=\mathbf 1_{\{r\mid A_m\}},
\]

即 ancestor support-resonance bit；以及

\[
S:=\mathbf 1_{\{Q\text{ squarefree}\}},
\]

即 quotient-squarefree bit。

若要 exact transport，还需要

\[
\boxed{d:=m(Q).}
\]

同一 arithmetic edge 至少可以面对三种不同 future language：

1. edge 是否 non-attenuating，即 `Lambda>=1`？
2. edge 属于 attenuated、resonant 还是 amplified？
3. exact multiplier `Lambda` 是多少？

这些 future queries **并不要求同一种 precision state**。

## 2. P025-T200 —— binary non-attenuation quotient

Stage 89 给出四种情形：

\[
(R,S)=(0,1)\Rightarrow\Lambda=1/r<1,
\]

\[
(R,S)=(1,1)\Rightarrow\Lambda=1,
\]

而只要

\[
S=0,
\]

无论 `R` 如何，都有

\[
\Lambda>1.
\]

因此

\[
\boxed{
\Lambda\ge1
\iff
R\lor\neg S.
}
\]

所以 binary future output 是 natural two-bit state 的一个 one-bit semantic quotient。

但这**不**意味着有某一个固定 natural input bit 永远足够。future Boolean output 本身当然是最粗 semantic quotient；从 available arithmetic observations 计算它时，仍可能需要先观察 `R` 或 `S`，并随观察结果 short-circuit。

## 3. P025-T201 —— ternary transport-class quotient

exact qualitative class 为

\[
\boxed{
\operatorname{class}(R,S)=
\begin{cases}
\text{amplified},&S=0,\\
\text{resonant},&S=1,\ R=1,\\
\text{attenuated},&S=1,\ R=0.
\end{cases}}
\]

因此 natural sufficient observation state 是

\[
\boxed{(R,S).}
\]

两个 natural bits 各自单独都不够。

- 同样 `R=1`，future output 不同：
  - `(q,p)=(11,13)` 的 `3->9` sum：quotient squarefree，resonant；
  - `(q,p)=(7,29)`：quotient repeated，amplified。
- 同样 `S=1`，future output 也不同：
  - `(q,p)=(5,59)`：nonresonant，attenuated；
  - `(q,p)=(11,13)`：resonant。

所以 ternary future language 确实需要两个 natural coordinates。

## 4. P025-T202 —— exact multiplier state

Stage 87 给出

\[
\boxed{
\Lambda
=
\begin{cases}d/r,&R=0,\\d,&R=1.
\end{cases}}
\]

因此 exact multiplier 由

\[
\boxed{(R,d)}
\]

决定。

此时 squarefree bit 反而是冗余的，因为

\[
\boxed{S\iff d=1.}
\]

但反向 collapse 会丢失 exact 信息：当 `S=0` 时，ternary state 只记住 “amplified”，而 `d` 可以取多个不同的 allowed values。

所以 natural precision hierarchy 为

\[
\boxed{
(R,d)
\longrightarrow
(R,S)
\longrightarrow
\mathbf1_{\{\Lambda\ge1\}}.
}
\]

每一次向下 collapse 只对相应更粗的 declared future language 安全，而不是对所有 future language 普遍安全。

## 5. Semantic quotient 不等于 observation state

这里必须区分三种对象。

### Semantic quotient

future output 本身，例如

\[
\mathbf1_{\{\Lambda\ge1\}}
\]

或 ternary class。

如果答案已经被算出，它当然是最粗 possible state。

### Natural sufficient observation state

不必恢复 full fine state，就能计算 future output 的 arithmetic observables，例如 `(R,S)`、`(R,d)`。

### Adaptive observation tree

决定下一步揭示哪个 natural observable，并允许在某些 states 上不观察完整 sufficient tuple 就提前停止的 decision procedure。

这三者不能混成一个概念。

## 6. P025-T203 —— binary query 有互补的 short-circuit 顺序

对 binary query

\[
\Lambda\ge1?
\]

可以 resonance-first：

1. 若 `R=1`，立即停止并返回 `TRUE`；
2. 若 `R=0`，再观察 `S`，返回 `not S`。

也可以 squarefree-first：

1. 若 `S=0`，立即停止并返回 `TRUE`；
2. 若 `S=1`，再观察 `R`，返回 `R`。

两种顺序在 observation count 上互不全局支配。

exact fixtures 给出两个方向：

- resonant-squarefree `(11,13)`：resonance-first 只需一次观察，squarefree-first 需要两次；
- nonresonant-repeated `(3,13)` difference：squarefree-first 只需一次，resonance-first 需要两次。

因此对 binary query，不存在仅由逻辑决定的统一最佳 first observation。最佳顺序还取决于 observation cost 和/或 state distribution。

## 7. P025-T204 —— ternary query 上 squarefree-first 弱支配 resonance-first

对 ternary future query，若先观察 `R`，无论得到什么都不能直接结束：

- `R=0` 可能是 attenuated，也可能 amplified；
- `R=1` 可能是 resonant，也可能 amplified。

所以 resonance-first 永远还要第二步观察 `S`。

反过来先看 `S`：

- 若 `S=0`，立即知道 amplified；
- 若 `S=1`，再观察 `R`，区分 attenuated / resonant。

因此在单纯 observation-count 模型下，

\[
\boxed{
\text{squarefree-first 弱支配 resonance-first}
}
\]

并且在所有 nonsquarefree states 上严格更省观察。

更一般地，只要第二次 observation cost 非负，并且 `S` 自身的成本没有大到压倒全部 alternative path，这种 logical dominance 仍有意义。Stage 90 不在未声明 cost model 的情况下声称 universal computational-cost optimum。

## 8. P025-T205 —— exact query 改变 observation vocabulary

若 future query 要 exact multiplier，仅知道 squarefreeness 在 repeated branch 上完全不够，必须恢复 numerical residual `d`。

所以 exact natural observation state 为

\[
\boxed{(R,d),}
\]

而不是 `(R,S)`。

这不仅是“精度更多一点”，而是 observation vocabulary 本身发生了变化：

\[
\boxed{
\text{qualitative future}:\ S=(d=1),
\qquad
\text{quantitative future}:\ d.
}
\]

precision compiler 不应在 future operation 根本不需要 multiplier magnitude 时，把 `S` 盲目细化成 numerical `d`。

## 9. Exact 四状态校准

下面四个 covers 实现了全部 logical combinations：

\[
\begin{array}{c|c|c|c|c}
(q,p),\text{route}&R&S&\text{class}&\Lambda\\ \hline
(5,59),\ 3\to9,+&0&1&\text{attenuated}&1/3\\
(11,13),\ 3\to9,+&1&1&\text{resonant}&1\\
(7,29),\ 3\to9,+&1&0&\text{amplified}&19\\
(3,13),\ 3\to9,-&0&0&\text{amplified}&19/3
\end{array}
\]

这些 fixtures 证明上面的 decision trees 不是建立在 unreachable Boolean states 上的形式游戏。

## 10. P025-D33 —— future-relative natural precision ladder

对该 exact arithmetic edge，定义三种 future languages：

\[
\mathcal F_{\rm bin}:\ \Lambda\mapsto\mathbf1_{\{\Lambda\ge1\}},
\]

\[
\mathcal F_{\rm cls}:\ \Lambda\mapsto
\{\text{attenuated,resonant,amplified}\},
\]

以及

\[
\mathcal F_{\rm exact}:\ \Lambda\mapsto\Lambda.
\]

得到 theorem-backed natural state ladder：

\[
\boxed{
(R,d)
\succ
(R,S)
\succ
\mathcal F_{\rm bin}.
}
\]

每个更粗 level 只对对应 declared future language sufficient。

因此这里的 ordering 是 **future-relative** 的，不是在声称某一种 representation 永远比另一种更好。

## 11. 架构后果

Stage 90 给出一个有限算术例子，严格区分四条原则：

1. **future-relative sufficiency** —— future query 一变，需要的 state 也变；
2. **semantic 与 observational precision 不同** —— future output 可以远粗于计算它所需的 natural observables；
3. **short-circuit refinement** —— sufficient tuple 并不需要在每个 state 上全部观察；
4. **query-dependent observation order** —— 最优 logical observation 顺序会随 future language 改变。

这比简单说“只保留 future-compatible quotients”更强：runtime acquisition policy 本身也是 future-relative 的。

## 12. 与 P023 / A2 / E002 的关系

P023 的 exact fiber-constancy theorem 回答：一个固定 coarse state 是否足以支持 declared future map。

Stage 90 在它上方提出一个新的 research-level 问题：

> 当多个 observable coordinates 都可获得，且某些 coordinates 只在条件分支中需要时，怎样用最少 refinement 自适应计算 declared future quotient？

E002 已经研究 predictive / task-relative observation 与 horizon saturation。Stage 90 提供一个完全 number-theoretic 的 exact fixture，其中 saturation、short-circuiting 与 query-dependent observation order 都无需概率或工程假设就真实发生。

这里不主张任何 canonical cross-route theorem；它只是 Relay / Foundation-feedback candidate。

## 13. Prior-art / novelty 边界

Boolean decision trees、sufficient statistics / states 与 short-circuit evaluation 在数学和计算机科学中都有广泛 prior art。

P025 不单独主张这些概念的新颖性。

项目侧结果只是：arithmetical spectral gap 精确地把该 cover 编译成上述 future-relative natural states 与 observation trees。任何更广泛架构抽象仍需 prior-art audit 与 Foundation Steward review。

## 14. 可执行资产

新增：

- `src/enterprise_math/abc_cover_future_precision.py`；
- `tests/test_abc_cover_future_precision.py`。

executable layer 验证：

- 四个 reachable `(R,S)` states 与 exact multipliers；
- binary Boolean quotient；
- binary query 的互补 short-circuit orders；
- ternary class 上 squarefree-first 的 logical dominance；
- 任一 natural bit 单独对 ternary class 都不充分；
- `(R,d)` 对 exact multiplier 的重建；
- exact fixtures 上的严格 natural precision hierarchy。

## 15. Generation checkpoint

Stage 76–90 已经从 cube-specific cyclotomic support 推进到一整套 transport architecture：

\[
\text{cyclotomic support}
\to
\text{congruence precision}
\to
\text{precision horizon}
\to
\text{value-coordinate switch}
\to
\text{divisor-lattice carrier}
\to
\text{exponent transport cocycle}
\to
\text{Hasse covers}
\to
\text{signed/dyadic transport}
\to
\text{cover resonance}
\to
\text{future-query-relative observation trees}.
\]

这是一个自然 generation boundary。后续数学应从新的 owner generation 开始，而不是继续无限延长当前 frozen payload。
