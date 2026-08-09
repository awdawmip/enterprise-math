# A3 Piecewise Affine Quotient 补充 01 —— 唯一最粗 Exact Partition 的两阶段构造

状态：`RESEARCH WIP / COARSEST EXACT PARTITION THEOREM + EXECUTABLE SOLVER`

## 1. 背景

主文已经证明：binary threshold affine map 的 exactness 对任意 partition refinement **不单调**。

这并不意味着 minimum exact partition 不存在或不能有效求出。

本补充证明：在完整整数格 `Z^k`、单个线性 threshold guard、两个整数 affine branches 的条件下，给定任意 initial partition，仍存在一个**唯一最粗 exact refinement**，并且只需两阶段 partition synthesis。

## 2. 程序

\[
T(c)=
\begin{cases}
B_+c+u_+,&w^Tc+b\ge0,\\
B_-c+u_-,&w^Tc+b<0.
\end{cases}
\]

initial partition 记为 `P_0`。

## 3. A3-PW04 —— branch-stable core partition

先完全忽略 guard identity，只要求两个 branch 的 linear parts 都能 descend。

用 A3 已有 linear-family solver 求：

\[
P_L=
\text{coarsest refinement of }P_0
\text{ on which }B_+,B_-\text{ both descend}.
\]

任何非恒定-guard 的 exact partition 都必须 refine `P_L`，因为只要某个 branch 在某 coarse fiber 中实际执行，该 fiber 内所有 hidden kernel moves 都不能改变 coarse branch output。

## 4. 情形一：`P_L` 已 exact

在 `P_L` 上检查主文 PW01/PW02：

- guard 已 coarse-readable；或
- guard hidden，但两个 descended affine branch effects 完全相同。

则：

\[
\boxed{P_*=P_L.}
\]

它显然 exact；任何其他 exact refinement 必须 refine `P_L`，所以它也是唯一最粗 exact refinement。

这包括最重要的 hidden-branch erasure 情形：branch identity 不可见，但 coarse output 不受 branch 影响，因此无需为 guard 提高精度。

## 5. 情形二：guard hidden 且 coarse branch effects 不同

设 branch difference：

\[
\Delta B=B_+-B_-,
\qquad
\Delta u=u_+-u_-.
\]

在 `P_L` 上两个 branches 已分别 descend，但 coarse effects 不同，所以至少有某个 `P_L` target block `G` 对 `Delta B` 的某列聚合不为 0，或 `Delta u` 在 `G` 上聚合不为 0。

假设存在一个更细 partition `R`，仍不暴露 guard，却试图让两个 coarse branch effects 重新相同。

`R` 把 `G` 拆成若干 child blocks。若在 `R` 上两个 branch coarse effects相同，则每个 child block 的对应 `Delta` 聚合都必须为 0。

把这些 child-block sums 相加，就得到 parent `G` 的聚合也必须为 0，与 `P_L` 上已知的非零差异矛盾。

因此：

\[
\boxed{
\text{一旦 hidden guard 在 }P_L\text{ 上看到不同 coarse effects，
任何保持 guard hidden 的 refinement 都不可能 exact。}
}
\]

所以所有 exact refinements **必须**让 guard descend。

## 6. 两阶段构造

先按 guard coefficient signature 细化 `P_L`：

\[
P_G=\operatorname{ObsRefine}(P_L,w).
\]

此时 guard 可见。

但主文已经展示 refinement 可能破坏 branch stability，所以不能直接停在 `P_G`。

再用 branch-family solver 重新稳定：

\[
P_*=\operatorname{LinearStable}(P_G;B_+,B_-).
\]

由于任何 exact partition：

1. 必须 refine `P_L`；
2. 在当前 case 中必须 expose guard，因此必须 refine `P_G`；
3. 又必须让两个 branch dynamics descend；

A3 linear solver 的 coarseness 立即推出：

\[
\boxed{
P_*=\text{unique coarsest exact refinement of }P_0.
}
\]

## 7. Globally constant guard

若 fine `w=0`，guard 在所有 state 上恒定，仅由 `b` 决定。

此时不应把 inactive branch 加入 stability obligation；minimum solver 只稳定实际 active branch：

\[
P_*=\operatorname{LinearStable}(P_0;B_{active}).
\]

这避免无意义 over-refinement。

## 8. 非单调但仍可求最小值

因此 binary threshold class 同时具有两个看似相反但并不矛盾的性质：

1. arbitrary exactness 不对 partition refinement 单调；
2. 给定 initial partition，minimum exact refinement 仍然唯一并可由上述两阶段算法求出。

这说明 general piecewise solver 不能使用“沿任意 refinement 保持 exact”的错误不变量，但可以利用**结构性 regime switch**。

## 9. 实现与压力测试

`src/enterprise_math/piecewise_relation_quotient.py` 新增：

`minimum_exact_partition_for_binary_threshold_piecewise(...)`。

测试包括：

- hidden guard 可完全擦除时保持最粗 partition；
- hidden guard coarse effects 不同后自动 expose guard；
- globally constant guard 只稳定 active branch；
- 4-coordinate 全 set-partition 暴力 oracle：所有 exact candidate partitions 都 refine solver 输出。

## 10. 下一步

下一层不直接跳到任意 program，而研究有限 guard family。

给 guard matrix `W`，真正需要分析的是：

\[
W(K_A)\subseteq\mathbb Z^r,
\]

即 hidden kernel 在 guard-score space 中生成的整数像格。

单 guard 主文只是：

- `rank W(K_A)=0`：guard visible；
- `rank W(K_A)=1`：每个 fiber 两侧 threshold 都可达。

multi-guard 情形需要区分 full-rank hidden guard lattice 与 partial hidden directions，并据此决定哪些 branch patterns 在一个 coarse fiber 中真实可达。
