# P019 补充 17 —— 单向 Coarsening 下 Internal Relation 的永久安全删除

状态：`RESEARCH WIP / EXACT FUTURE-SAFETY THEOREM PROVED`

## 1. 问题

Supplement 08 定义 future-safe quotient：只有当两个 fine states 对所有允许 future programs 永远不可区分时，才能安全合并。

Supplement 15/16 又识别：一次 block merge 删除一个 internal weighted relation `Z_ij`。

现在可以回答一个非平凡的具体问题：

> 如果未来只允许继续降维 / 继续粗化，这个已经删除的 `Z_ij` 还需要保存吗？

答案：**不需要。**

## 2. 单向 coarsening future language

固定当前 partition `Pi`。

允许的未来 operations 仅为：

\[
\Pi\preceq\Sigma_1\preceq\Sigma_2\preceq\cdots,
\]

即只允许继续把当前 coarse blocks 合并，不允许 split/refinement。

允许 observation 只读取每个未来 partition 的：

- block capacities；
- block totals；
- weighted relation field；
- 这些 coarse state 的确定性派生量。

不读取已删除的 fine internal witness identity。

## 3. P019-X55 —— 当前 weighted quotient 是 coarsening-only future-safe

设两个 fine states `x,y` 在当前 partition `Pi` 上具有相同 weighted quotient：

\[
Q_\Pi(x)=Q_\Pi(y).
\]

则对任意未来 coarse partition

\[
\Sigma\succeq\Pi
\]

都有：

\[
\boxed{
Q_\Sigma(x)=Q_\Sigma(y).
}
\]

### 证明

由 Supplement 16 X50：

\[
Q_\Sigma
=
Q_{\Sigma/\Pi}\circ Q_\Pi.
\]

因此：

\[
Q_\Pi(x)=Q_\Pi(y)
\Longrightarrow
Q_{\Sigma/\Pi}(Q_\Pi(x))
=
Q_{\Sigma/\Pi}(Q_\Pi(y)).
\]

即得。∎

所以当前 weighted quotient 对这一 future language 已经是 future-safe。

## 4. P019-X56 —— deleted internal relations 在纯 forward coarsening 中永久不可观测

若某次 merge 将 blocks `i,j` 合并，并删除 internal relation：

\[
z=Z_{ij},
\]

则以后任何只由 coarse partition quotient 构成的 operation 都只看到：

- merged capacity `m_i+m_j`；
- merged total `c_i+c_j`；
- summed external relations `Z_{ik}+Z_{jk}`。

`Z_ij` 不再出现在任何未来 cross-block cut sum 中。

所以：

\[
\boxed{
\text{在 coarsening-only future language 中，deleted internal }Z
\text{ 可永久删除。}
}
\]

不需要保存完整 oriented contraction flag，也不需要保存 `z` history。

## 5. 这不是近似删除

这里的安全删除不是：

- “影响很小”；
- “以后大概用不到”；
- “用统计量近似”。

而是严格：

\[
\boxed{
\forall\text{ future coarsening programs},
\quad O(T_w(x))=O(T_w(y)).
}
\]

因此它是 Supplement 08 future-equivalence 的一个完整可证明实例。

## 6. P019-X57 —— 只要允许 refinement，安全性立即可能失效

取三个 unit blocks。

fine state 1：

\[
(1,-1,0),
\]

fine state 2：

\[
(2,-2,0).
\]

先把前两个 unit blocks 合并。

二者 coarse capacities 都是：

\[
(2,1),
\]

coarse totals 都是：

\[
(0,0),
\]

所以当前 weighted relation field 完全相同。

但被删除的内部关系分别为：

\[
Z_{12}=2,
\qquad
Z_{12}=4.
\]

若未来允许 refinement，把 capacity-2 block 再拆回两个 unit blocks，则差异立即重现。

所以：

\[
\boxed{
\text{coarsening-safe}
\not\Rightarrow
\text{refinement-safe}.
}
\]

## 7. Operation-family 依赖的最小 relation memory

因此没有脱离 future language 的绝对“最小历史”。

### A. 纯 forward coarsening

最小候选 current state：

\[
\boxed{
\text{current partition capacities}
+
\text{current weighted relation quotient}
+
\text{grand total}
}
\]

已经足够。

所有以前 deleted internal `Z` 都可以丢弃。

### B. 允许 exact refinement

若某 coarse block 将来可能被精确拆开，就必须保留足以恢复对应 internal relation fiber 的 detail。

单步 two-child refinement 时，一个 internal `Z` 即为完整 child-total fiber coordinate。

### C. 允许 selected boundary lift

需要保留/重建 fiber endpoint；Supplement 09 的 `(z,rho)` / fiber-root detail 是候选。

### D. 查询真实 process history

即使当前 fine state 可从更小 relation object 重建，真实先后顺序仍可能需要 historical witness。

这属于 provenance，不等同 current geometry。

## 8. 与真实不可逆性的关系

数学上：

- forward merge 丢弃 `Z` 是 many-to-one；
- 若 `Z` 不保存，fine split 一般不可唯一恢复；
- 若 future language 永远只粗化，则这种不可逆性对未来 coarse dynamics 完全安全。

这说明：

> **不可逆并不等于错误；关键是被删除的 distinction 是否还属于未来允许的物理/数学问题。**

这与 P010/P011 的 history fiber 语言兼容，但不能据此自动断言自然本体真的删除了这些 relations。

## 9. 与 P021 witness composition 的统一

P021 的安全原则：

> 只有在证明 witness identity 不影响未来 composition 时，才允许降到 cardinality / coarse shadow。

P019 当前得到 relation 版：

> 只有在证明 deleted internal relation 不影响未来 allowed partition programs 时，才允许永久删除。

对 coarsening-only language，X55 已给出完整证明。

对包含 refinement/directional lift 的 language，必须更细。

因此二者可以统一为：

\[
\boxed{
\text{safe collapse}
=
\text{quotient by future operational indistinguishability}.
}
\]

## 10. precision 的新解释

在这个具体几何模型中，提高 precision 可以直接理解成：

> 重新允许访问某些此前被 coarse partition 内化的 internal relations。

所以：

- coarse precision：只看 block-to-block weighted field；
- finer precision：split 某些 blocks，暴露新的 internal `Z`；
- finest singleton precision：所有 unit slots 可区分。

这与《我眼中的世界》中的“精度是数值定义的一部分”一致，但本补充不修改 worldview 文件。

## 11. 实现与反例回归

新增：

- `tests/test_relation_erasure.py`。

验证：

1. 两个具有不同 deleted internal relations 的 fine states，在当前 weighted quotient 相同后，经过多种后续 partition coarsenings 始终相同；
2. 同一对 states 一旦允许 refinement，内部 relation 立即可区分。

## 12. 下一步

1. 扩展 X55 到“coarsening + 某类 block-local dynamics”并分类哪些 dynamics 仍不读取 deleted `Z`；
2. 对允许 refinement 的情形，寻找最小 relation-memory set，而不是默认保存全部历史；
3. 结合 Supplement 08 partition-refinement algorithm，自动计算给定 operation family 下哪些 deleted `Z` equivalence classes 可安全商掉；
4. 对 P021 direction transport 定义 relation-level future language，检验 witness joins 是否可由部分 deleted-`Z` memory 支撑；
5. 将“precision refinement = re-expose internal relations”接入 P018 正式 algebra。
