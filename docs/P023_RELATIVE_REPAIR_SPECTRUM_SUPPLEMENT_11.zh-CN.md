# P023 —— 相对 repair 谱，补充 11

状态：`PROVED RESEARCH NOTE`  
归属：A2 / P023，并建立到 P011、P018 的正式桥接  
依赖：P011 collision spectrum、P018 有限 precision partitions、P023-S9 最小 repair cardinality  
纪律：集合分区、商映射、二项反演与 collision spectrum 都属于成熟数学。本补充的项目价值是统一已有 Enterprise Math 定理线的有限精度解释与精确接口。

## 1. 问题

P023-S9 对一个有限 refinement 给出一个标量：从粗 precision 升级到细 precision，最少需要多大的 repair alphabet。

P011 对一般 many-to-one map 已经给出更完整的 collision spectrum。

P018 则给出 observation fiber 内的点态 ambiguity。

这三者并不是独立结构。任意 precision refinement 自己就带有一个规范 many-to-one quotient projection，因此 P011 的完整 spectrum 可以直接施加到一次 precision 升级上。

## 2. 规范 quotient projection

令 `X` 为有限集，并设 `F` 比 `E` 更细，即

\[
F\subseteq E.
\]

则存在规范满射

\[
\boxed{
\pi_{F,E}:X/F\to X/E,
\qquad
[x]_F\mapsto[x]_E.
}
\]

对 coarse block `B in X/E`，定义

\[
\boxed{
s_B
=
\#\{C\in X/F:C\subseteq B\}.
}
\]

于是 `s_B` 就是在一个旧 coarse class 内被忘掉的 fine quotient classes 数量。

## 3. P023-S11-T01 —— projection fiber 就是局部最小 repair alphabet

状态：`PROVED`。

对每个 coarse block `B`，

\[
\boxed{
|\pi_{F,E}^{-1}(B)|=s_B.
}
\]

由 P023-S9，`s_B` 恰好就是在该 coarse block 内恢复 fine class 所需的最小 repair symbols 数量。

因此全局最小 repair alphabet 为

\[
\boxed{
R(E\leftarrow F)
=
\max_{B\in X/E}s_B.
}
\]

所以 S9 的标量正是一个规范 quotient projection 的最大 fiber size。

## 4. P023-S11-T02 —— 相对 repair spectrum

状态：`PROVED`。

定义

\[
\boxed{
\mathcal R_k(E\leftarrow F)
=
\sum_{B\in X/E}\binom{s_B}{k}.
}
\]

则

\[
\boxed{
\mathcal R_k(E\leftarrow F)
=J_k(\pi_{F,E}),
}
\]

其中 `J_k` 就是 P011 collision spectrum。

因此：

- `R(E<-F)=max_B s_B` 是最坏局部 repair alphabet；
- `R_2` 统计被 coarse precision 忘进同一 block 的 fine classes 对；
- 更高阶 `R_k` 统计被同一次 precision-forgetting projection 一起合并的 fine-class 高阶集合。

第一坐标为

\[
\mathcal R_1(E\leftarrow F)=|X/F|.
\]

## 5. P023-S11-T03 —— 二项反演恢复完整 repair-size 分布

状态：`PROVED`，是 P011-T05 的直接特化。

令

\[
a_r
=
\#\{B\in X/E:s_B=r\}.
\]

则

\[
\mathcal R_k
=
\sum_{r\ge k}a_r\binom rk.
\]

因此

\[
\boxed{
a_r
=
\sum_{k\ge r}
(-1)^{k-r}\binom kr\mathcal R_k.
}
\]

所以完整相对谱不仅决定最坏 repair block，还精确决定所有局部 repair alphabet 大小的直方分布。

## 6. P023-S11-T04 —— P011 provenance spectrum 是最细 precision 端点

令 `F` 取原始状态集上的离散相等关系，并令有限确定性映射

\[
T:X\to Y
\]

诱导

\[
E=\ker(T).
\]

此时每个 `F`-class 只有一个原始 state，因此对应输出 block 有

\[
s_B=|T^{-1}(y)|.
\]

于是

\[
\boxed{
\mathcal R_k(\ker T\leftarrow\Delta_X)
=J_k(T).
}
\]

这给 P011 一个精确 repair 解释：

> `|T^{-1}(y)|` 就是在只保留 `T(x)=y` 后恢复原始 state label 所需的局部最小 alphabet。

因此 P011 的整个 collision spectrum 同时就是 forward map 的高阶 provenance-repair spectrum。

这只是数学上的重建成本，并不主张自然界实际保存了被合并的 provenance。

## 7. P023-S11-T05 —— precision refinement 与 history merging 在同一 spectrum 上反向运动

对任意有限 partition `E`，定义其绝对状态 ambiguity spectrum

\[
\boxed{
\mathcal A_k(E)
=
\sum_{B\in X/E}\binom{|B|}{k}.
}
\]

若 `F subseteq E` 更细，则每个 `F`-block 都包含于一个 `E`-block，由二项组合计数得到

\[
\boxed{
\mathcal A_k(F)\le\mathcal A_k(E).
}
\]

定义 refinement gain

\[
\boxed{
G_k(E\to F)
=
\mathcal A_k(E)-\mathcal A_k(F).
}
\]

则 `G_k` 精确统计：在 precision `E` 下仍共同可见、但被更细 precision `F` 分开的 `k` 元原始状态集合数量。

因此：

\[
\boxed{
\text{deterministic postcomposition / history merging}
\Longrightarrow
\mathcal A_k\text{ 增大},
}
\]

而

\[
\boxed{
\text{task enrichment / precision refinement}
\Longrightarrow
\mathcal A_k\text{ 减小}.
}
\]

同一个 partition statistic 因而以相反方向同时度量 forward information loss 与 precision gain。

## 8. P023-S11-T06 —— refinement chain 的组合

状态：`PROVED`。

对

\[
G\subseteq F\subseteq E,
\]

规范 projection 复合为

\[
X/G\longrightarrow X/F\longrightarrow X/E.
\]

若一个 `E`-block 包含 `F`-blocks `C_1,...,C_m`，则它内部的 `G`-blocks 数精确为

\[
\boxed{
s^{G/E}_B
=
\sum_{j=1}^{m}s^{G/F}_{C_j}.
}
\]

因此

\[
\boxed{
R(E\leftarrow G)
\le
R(E\leftarrow F)R(F\leftarrow G),
}
\]

这把 P023-S9 的 staged repair bound 重新解释成规范 quotient-projection 组合的 maximum-fiber shadow。

当两个阶段的最大 split 出现在不同局部分支时，该乘积上界可以严格不等。

## 9. Repair 生成多项式

相对 repair spectrum 可以打包为

\[
\boxed{
K_{E\leftarrow F}(t)
=
\sum_{B\in X/E}\big((1+t)^{s_B}-1\big).
}
\]

`t^k` 的系数恰好就是 `R_k(E<-F)`。

这正是规范 precision-forgetting projection 的 P011 collision polynomial。

因此 P011 的 polynomial identities 与 fiber-merger 解释可以直接复用于 precision projections，不需要再建立一套独立多项式理论。

## 10. 基础解释

一个有限 precision state 不能只由单一 class count 描述完毕。

对相对升级 `E -> F`，至少存在三个不同的精确对象：

1. 最坏局部 repair alphabet `max s_B`；
2. 完整局部 repair-size 分布 `a_r`；
3. 高阶 spectrum `R_k` / generating polynomial。

这提供了一套不需要对数、概率、隐藏实值 entropy 或预设欧氏尺度的任务相对整数信息演算。

## 11. 可执行规范

- `src/enterprise_math/precision_projection_spectrum.py`
- `tests/test_precision_projection_spectrum.py`

测试通过二项反演重建局部 repair-size 分布，验证 quotient projection 的精确组合，把 S11 maximum 与通用 S9 minimum-repair theorem 对照，并在小型有限 partitions 上压力测试 ambiguity-spectrum refinement monotonicity。

## 12. 前人工作与新颖性纪律

等价关系商、fiber-size spectrum、二项反演与 partition lattice 都属于成熟数学。P011 已经是 Enterprise Math 内 collision-spectrum theorem family 的 owner。

本补充新增的项目级统一是显式识别

\[
\boxed{
\text{P011 collision spectrum of }\pi_{F,E}
=
\text{relative precision repair spectrum }E\leftarrow F,
}
\]

从而闭合此前分离的 P011/P018/P023 三条线。这里不主张历史首创。
