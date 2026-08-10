# P023 / A2 —— Precision Incidence Core v3

状态：`PROVED OWNER DISTILLATION / RESEARCH`  
归属：A2 future-compatible quotient  
压力来源：P011/P018/P023/P024 与 P017  
冻结来源：`research/p023-precision-incidence-scheduling@646530c3acd69332efe0fb937258cec888713688`

本文把此前不断扩张的应用型补充压成一个 owner-level finite theorem surface。有限分区、等价关系、二部 incidence graph、二项反演、定向 metric 等一般数学都属于成熟前人数学；这里保留的是进取数论的精确 repair 接口及跨路线综合。

## 1. Precision state 是有限分区

令 `X` 为有限非空状态集。一个 precision/task state 是 `X` 上的等价关系 `E`，等价地是分区 `X/E`。

新增任务 `F` 后保留的精度是共同细化

\[
E\cap F.
\]

真实联合状态不是形式笛卡尔积，而是恰好对应非空 block intersections：

\[
\Gamma(E,F)=\{(B,C)\in X/E\times X/F:B\cap C\ne\varnothing\}.
\]

因此

\[
\boxed{|X/(E\cap F)|=|\Gamma(E,F)|.}
\]

差值 `|X/E| |X/F|-|Gamma(E,F)|` 精确数出形式 product labels 中没有任何真实 state 实现的部分。

## 2. 最小 repair = 最大局部 split degree

假设当前已经保留 `E`，现在新增任务 `F`。对每个 `E` block `B`，定义

\[
s_B=\#\{C\in X/F:B\cap C\ne\varnothing\}.
\]

任何把 `E` 升级为 `E cap F` 的 repair coordinate，其最小 alphabet 大小精确为

\[
\boxed{\rho(E,F)=\max_{B\in X/E}s_B.}
\]

必要性是在最坏 coarse block 内用鸽巢原理；充分性则是在每个 `E` block 内局部给真实 `F` 子块编号，并跨不同 `E` blocks 重用同一 repair alphabet。

因此 one-bit repair 不是特殊现象：

\[
\boxed{\text{binary repair 足够}\iff\rho(E,F)\le2.}
\]

crossing bit、carry bit、shell-label repair、material/event repair 都只是这条局部 split law 的特化。

## 3. 完整 relative repair spectrum

最坏 local alphabet 只是最高层统计。定义

\[
\boxed{\mathcal R_k(E,F)=\sum_{B\in X/E}\binom{s_B}{k}.}
\]

这恰好是 canonical quotient projection `X/(E cap F) -> X/E` 上的 P011 collision spectrum。

因此：

- `R_1(E,F)=|X/(E cap F)|`；
- `R_2` 数出那些新 joint classes 中，原本在同一个旧 `E` block 内混在一起的 pair 数；
- 完整有限谱可通过二项反演恢复所有 local repair sizes 的分布；
- 若所有局部 split 都是 binary，则

\[
\boxed{\#\{B:s_B=2\}=\mathcal R_2(E,F)=|X/(E\cap F)|-|X/E|.}
\]

这严格区分了 local repair width、global active repair support 与 higher-order repair mass。

## 4. Incidence geometry

pairwise incidence graph 诱导定向 repair factor `rho(E,F)`。对任意第三个 precision relation `G`，

\[
\boxed{\rho(E,G)\le\rho(E,F)\rho(F,G).}
\]

证明只需：一个 `E` block 最多碰到 `rho(E,F)` 个中间 `F` blocks，而每个这样的 `F` block 最多再碰到 `rho(F,G)` 个 `G` blocks。

对整数 alphabet base `b>=2`，定义

\[
L_b(n)=\min\{\ell:n\le b^\ell\},\qquad d_b(E,F)=L_b(\rho(E,F)).
\]

则

\[
\boxed{d_b(E,G)\le d_b(E,F)+d_b(F,G).}
\]

并且 `d_b(E,F)=0 iff E subseteq F`。对称化

\[
\boxed{D_b(E,F)=d_b(E,F)+d_b(F,E)}
\]

给固定状态集上的有限 precision relations 一个整数 metric。

这是一种任务转换成本的内禀几何，不是物理空间几何。

## 5. Higher-order incidence 不能由 pairwise 数据恢复

对三个以上 task partitions，定义 realized incidence hypergraph

\[
\Gamma(E_1,\dots,E_m)=\{(B_1,\dots,B_m):B_1\cap\cdots\cap B_m\ne\varnothing\}.
\]

则

\[
\boxed{|X/(\cap_iE_i)|=|\Gamma(E_1,\dots,E_m)|.}
\]

pairwise weighted incidence 不足以确定它。

显式 8-state 反例：系统 A 只实现四个 even-parity binary triples `000,011,101,110`，每个出现两次；系统 B 实现全部八个 binary triples，各出现一次。两个系统的每个单独 partition block sizes 相同，所有 weighted pairwise incidence tables 也完全相同，但 joint class counts 分别为 `4` 与 `8`。在 A 中知道两个 tasks 后第三个已经免费，而 B 中同一条件 repair factor 为 `2`。

所以

\[
\boxed{\text{pairwise precision geometry 不决定 joint precision}.}
\]

## 6. Context monotonicity

若已知 context `C'` 比 `C` 更细，对同一个新增任务 `F`，

\[
\boxed{\rho(C',F)\le\rho(C,F).}
\]

已知上下文越丰富，增加同一任务所需的最小 repair alphabet 不会增加。这是纯有限分区定理，不是熵或概率陈述。

## 7. Realizability 与 observation 的双重单调性

更一般地，令有限 incidence relation `R subseteq I x X` 表示 label `i` 下哪些细状态真实可实现，并令 `g:X->Y` 为保留 observation。对每个 `y` 定义

\[
m_{R,g}(y)=|\{i:\exists x,\ (i,x)\in R,\ g(x)=y\}|.
\]

恢复 label 所需的精确最小 repair alphabet 为

\[
\boxed{M(R,g)=\max_y m_{R,g}(y).}
\]

立即得到：扩大可实现关系不会降低 `M`，粗化保留 observation 也不会降低 `M`。image separation 恰好就是 `M=1` 的端点。

这就是“candidate superset 会制造假 collision”原则的 owner-level 版本。

## 8. 边界

本核心不声称所有 precision 问题都是有限的；不声称 pairwise metric 可以替代 higher-order task structure；不把 task-relative predictive sufficiency 升格为物理本体；不把 informative feature 自动等同 necessary repair；也不假定 formal Cartesian task product 自动真实实现。

正确对象始终是声明 task language 下的真实 partition/incidence structure。

## 9. 可执行规范

owner-local modules：

- `src/enterprise_math/a2_precision_incidence.py`
- `tests/test_a2_precision_incidence.py`

回归覆盖：真实 tuple 计数、repair-spectrum 二项反演、binary active-support identity、pairwise-shadow no-go、四状态全部 15 个 partitions 的全部 `15^3=3375` triples 上的乘法/加法三角律，以及对称 metric triangle。

有限枚举只承担 regression / counterexample reconstruction，不替代上面的普通有限数学证明。
