# P025 补充 03 —— Witness Threshold 的最粗精度链

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner：`program/p025-abc-support-collapse`  
性质：P023 minimal-repair 的直接推论；不依赖 ABC 特有数学

## 1. 只问有限阈值时，不需要恢复完整 witness cost

设状态空间为 `X`，已有 coarse quotient

\[
q:X\to Q,
\]

并设每个状态有 witness cost

\[
\mu:X\to\mathbb N\cup\{\infty\}.
\]

固定任务半径 `K>=0`。若未来只关心

\[
h_j(x)=1_{\mu(x)\le j},
\qquad 0\le j\le K,
\]

则定义截断 cost

\[
\boxed{
\tau_K(x)=\min\{\mu(x),K+1\},
}
\]

其中 `infinity` 统一映到 `K+1`。

## 2. P025-T08 —— 截断 cost 与全部阈值观察完全等价

对任意 `x,y in X`，

\[
\boxed{
\tau_K(x)=\tau_K(y)
\iff
h_j(x)=h_j(y)\quad\forall\,0\le j\le K.
}
\]

证明：若截断值相同，则每个 `j<=K` 下“截断值是否 <=j”相同，而这恰好等价于 `mu<=j`。反之若全部阈值判断相同，若某一真实 cost 不超过 `K`，其第一次由 `False` 变 `True` 的位置就是 cost 本身；若始终 `False`，截断值就是 `K+1`。故截断值相同。

因此 `tau_K` 不是经验压缩，而是这组有限 future observables 的**完备最小标签**。

## 3. P025-T09 —— 相对于已有 q 的最粗 P023 修复

定义

\[
\boxed{
r_K(x)=\bigl(q(x),\tau_K(x)\bigr).}
\]

则：

1. `r_K` 细化 `q`；
2. 每个 `h_j, j<=K` 都通过 `r_K` 下沉；
3. 若另一个 quotient `s` 细化 `q`，并且全部 `h_j, j<=K` 都通过 `s` 下沉，则 `s` 必然细化 `r_K`。

第三点由 P025-T08 立即得到：`s(x)=s(y)` 时，`q(x)=q(y)` 且全部阈值观察相同，因此 `tau_K(x)=tau_K(y)`，故 `r_K(x)=r_K(y)`。

所以

\[
\boxed{r_K=(q,\tau_K)}
\]

就是对有限 witness-threshold 任务族的最粗修复。

这正是 P023-T02“只补回未来真正需要区分的信息”在 witness precision 上的精确实例。

## 4. P025-T10 —— 阈值精度形成投影链

若 `0<=K<L`，则

\[
\boxed{
\tau_K(x)=\min\{\tau_L(x),K+1\}.
}
\]

因此高阈值精度可以精确投影到低阈值精度，并且

\[
r_L\text{ 细化 }r_K.
\]

所以得到一个真正的 task-horizon precision chain：

\[
r_0\preceq r_1\preceq r_2\preceq\cdots.
\]

提高 `K` 的含义不是“数值更精确”这一泛泛说法，而是：未来任务要求区分更高 witness cost，于是 quotient 只在必要处继续分裂。

## 5. P025-N02 的最小修复现在可以精确计算

对

\[
A:1+2=3,\qquad \mu(A)=1,
\]

\[
B:1+8=9,\qquad \mu(B)=2,
\]

且二者 radical coarse state 相同。

若任务只问 `mu<=0`，则二者仍可坍缩在一起：

\[
\tau_0(A)=\tau_0(B)=1.
\]

若任务升级为问 `mu<=1`，则

\[
\tau_1(A)=1,
\qquad
\tau_1(B)=2,
\]

二者恰好在这个任务精度上第一次必须分裂。

这给出一个非常具体的进取数论式结论：

\[
\boxed{
\text{状态是否需要分开，不由状态本身永久决定，而由未来任务阈值决定。}
}
\]

## 6. 反哺底层的意义

P025 前两阶段曾需要 `Sigma_add` 或 `Sigma_flag` 才能恢复整个 witness 生成结构。P025-T09 说明，如果任务更弱，仅要求判断有限 witness threshold，那么恢复完整生成器可能严重过细。

因此基础架构应明确区分：

- **generator precision**：足以恢复完整 witness lattice/flag；
- **decision precision**：只足以回答给定 horizon 内的 certificate predicates。

后者由 `tau_K` 给出一个严格的最粗实例。

这不是新的 ABC 定理，而是 ABC 压力测试反推出的一个可复用 P023 精度定理。

## 7. 可执行资产

- `src/enterprise_math/witness_threshold_precision.py`
  - `tau_K` 截断 cost；
  - threshold profile；
  - 高低 horizon 精确投影；
  - `(q,tau_K)` 修复；
  - finite state 上的最粗性审计。
- `tests/test_witness_threshold_precision.py`
  - profile/truncation 等价；
  - infinity 与高 cost 在有限 horizon 合流；
  - projection chain；
  - `mu=1` 与 `mu=2` 在 `K=1` 首次分裂；
  - finite coarsest-repair 回归。

## 8. 当前最短架构链

经过 P025 三轮压缩，当前得到：

\[
\boxed{
\text{fine relation-state}
\to
\text{coarse state}
\to
\begin{cases}
\text{generator signature},&\text{需要恢复证书空间};\\
\tau_K,&\text{只需要回答有限证书阈值}.
\end{cases}
}
\]

这比“所有粗化都必须精确保持未来运算”更灵活，也比“粗化失败就把全部细节补回来”更节省信息。

下一步应把这一 threshold-repair theorem 从 P025 Relay 给 P023/A2，由母层判断是否抽成一般 canonical 工具；P025 本身继续用 ABC/Mason/Pasten 作为压力测试，而不抢占母层所有权。
