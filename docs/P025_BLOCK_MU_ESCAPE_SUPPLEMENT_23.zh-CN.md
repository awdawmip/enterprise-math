# P025 补充 23 —— `mu` 作为 Block Scaling Line 的第一次逃逸

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-access-tail-stage18`  
依赖：P025 补充 20–22  
Hard block：`NONE`

## 1. `nu` 已经降到一维，但 `mu` 仍读取二维 sublevel set

补充 22 因为 floor condition 固定了 `W=±D`，把 absorption-floor access radius `nu` 降成一条 affine line。

第一 nondegenerate witness radius

\[
\mu
\]

不同：它只要求 `W!=0`，所以仍需在整个 compressed additive lattice 中寻找。

不过 block-value quotient 已经消除了 fine prime-coordinate cube。每个半径下只需保留每个 block 的有限**scalar derivative values**。

## 2. P025-D13 —— reachable block derivative values

对 block `n` 与半径 `r>=0` 定义

\[
\boxed{
V_n(r)
=
\{d_x(n):\|x\|_\infty\le r\}.
}
\]

对 unit block，

\[
V_1(r)=\{0\}.
\]

对 `n>1`，把 raw derivative row 写成

\[
A(n)b,
\]

其中 `b` 为 primitive positive row，并令

\[
P_n=\sum_i b_i.
\]

则所有 reduced derivative values 都落在

\[
[-rP_n,rP_n]\cap\mathbb Z,
\]

所以

\[
\boxed{|V_n(r)|\le2rP_n+1.}
\]

exact set 可以通过 scalar coordinate ranges 的反复 Minkowski/set addition 构造，无需枚举 prime-coordinate Cartesian cube。

因此潜在的 `(2r+1)^omega(n)` fine-state 枚举，被压成每个 block 内的一维 reachable-value calculation。

## 3. P025-D14 —— compressed additive reachable set

定义

\[
\boxed{
\mathcal R_r
=
\{(u,v,u+v):
 u\in V_a(r),
 v\in V_b(r),
 u+v\in V_c(r)\}.
}
\]

这恰好是 norm 不超过 `r` 的 fine additive witnesses 在 block derivative-value quotient 下的像。

并且

\[
\mathcal R_r\subseteq\mathcal R_{r+1}.
\]

## 4. P025-T67 —— Wronskian degeneracy 恰好是整数 scaling line

对 compressed additive state `(u,v,u+v)`，

\[
W=av-bu.
\]

由于

\[
\gcd(a,b)=1,
\]

精确有

\[
\boxed{
W=0
\iff
(u,v,u+v)=t(a,b,c)
\text{ 对某个 }t\in\mathbb Z.
}
\]

### 证明

若 `W=0`，则

\[
av=bu.
\]

因为 `gcd(a,b)=1`，有 `a|u`、`b|v`。写

\[
u=at,
\qquad
v=bs.
\]

代回得到 `ab s=ab t`，故 `s=t`。Additivity 再给出

\[
u+v=(a+b)t=ct.
\]

反向显然。∎

定义 **degenerate scaling line**

\[
\boxed{
\Delta_{abc}
=
\{t(a,b,c):t\in\mathbb Z\}.
}
\]

## 5. P025-T68 —— `mu` 的 exact first-escape characterization

第一 nondegenerate witness radius 精确是

\[
\boxed{
\mu
=
\min\{r\ge1:
\mathcal R_r\not\subseteq\Delta_{abc}\}.
}
\]

### 证明

按构造，`R_r` 正好是所有 norm 不超过 `r` 的 fine additive witnesses 的 compressed image。由 P025-T67，compressed state Wronskian-degenerate 当且仅当落在 `Delta_abc` 上。因此半径 `r` 存在 nondegenerate fine witness，当且仅当 `R_r` 有点离开 scaling line。取第一次出现即为 `mu`。∎

所以这是一个 exact relation-state escape problem，而不是 heuristic witness search。

## 6. P025-T69 —— arbitrary-support exact finite solver

补充 22 已给 exact floor witness，因此

\[
\mu\le\nu
\]

提供有限上界。

Exact algorithm：

1. 用 block floor-line solver 算 `nu`；
2. 对 `r=1,...,nu` 构造 `V_a(r),V_b(r),V_c(r)`；
3. 只组合满足 `u+v in V_c(r)` 的 additive pairs；
4. 第一次出现 `av-bu!=0` 时停止。

对任意 support size 都精确成立，而且 `mu` 计算从不枚举 fine prime-coordinate witness cube。

## 7. 示例

### `2+3=5`

半径 1 时，三个 prime blocks 都已可实现 `-1,0,1`。Compressed additive set 中例如有

\[
(-1,0,-1),
\]

不在 scaling line 上，因此

\[
\boxed{\mu=1.}
\]

Floor access 仍为 `nu=2`，恢复已知 Pareto tradeoff。

### `1+8=9`

半径 1 时

\[
V_8(1)=\{-12,0,12\},
\qquad
V_9(1)=\{-6,0,6\},
\]

但 additivity `t_8=t_9` 只留下零。因此

\[
\mathcal R_1=\{(0,0,0)\}
\]

没有 nondegenerate witness。

半径 2 时共同 value `12` 出现，得到

\[
\boxed{\mu=2.}
\]

### `1+22=23`

Absorption floor 有 `D=1`，但 block `22` 实现 floor target 需要

\[
\nu=5.
\]

可是共同 derivative value `2` 在全局半径 2 已经可达，其 Wronskian absorption redundancy 为 `2`，所以

\[
\boxed{\mu=2<\nu=5.}
\]

这只用 block-value reachability 就恢复了 squarefree access-delay/Pareto phenomenon。

### `25+704=729`

该 relation 横跨四个 fine prime coordinates。Compressed solver 给出

\[
\boxed{\mu=6=\nu,}
\]

而 `mu` 计算过程中不需要 prime-coordinate cube enumeration。

## 8. 架构后果

两个主要 access coordinates 现在有互补的 compressed 表达：

\[
\boxed{
\begin{array}{ll}
\mu &: \mathcal R_r\text{ 第一次逃离 }\Delta_{abc},\\
\nu &: K\text{ 在一维 floor line }W=D\text{ 上的最小值}.
\end{array}
}
\]

前者是增长的二维 reachable-set 问题，后者是一维 level-set 问题；二者共享同样的三条 finite block access systems。

## 9. 还剩什么难点

Stage 23 已给 exact finite solver，但还没有 `mu` 的 universal closed formula。

补充 19 解释了为什么不应期待从 block coefficients 直接猜出一个普适简单公式：任意 primitive positive row 都能出现在真实 arithmetic block 中，radius-one reachability 本身已经包含 bounded signed subset-sum/factorization 结构。

因此下一目标不应是硬猜一个 universal scalar，而应寻找特定 relation classes 下，哪些更小 summaries 已足以判定 scaling-line escape。

## 10. Prior-art 边界

Linear image sets、dynamic set addition、coprimality 下的整数比例关系与 first-exit formulations 都属于 elementary/standard mathematics。

P025 不对这些 generic tools 作创新主张。项目侧新增候选是 Pasten-style nondegeneracy 的 exact block-value compression 及其与 finite precision/access architecture 的结合。

历史创新状态仍为 `NOVELTY_UNVERIFIED`。

## 11. 可执行资产

新增：

- `src/enterprise_math/abc_block_mu.py`
  - exact block reachable derivative values；
  - compressed additive reachable sets；
  - exact scaling-line degeneracy test；
  - 用 `nu` 作 finite upper bound 的 arbitrary-support exact `mu` solver。
- `tests/test_abc_block_mu.py`
  - scaling-line characterization；
  - `2+3=5`、`1+8=9`、tradeoff examples；
  - `1+22=23` 的 strict `mu<nu`；
  - four-coordinate `25+704=729`；
  - selected small cases 与此前 fine exact oracle 对照。

## 12. 下一前沿

没有 hard block。继续：

1. 寻找只为 scaling-line escape 服务的 task-minimal `V_n(r)` summaries；
2. 给 structured block families 推导 exact `mu=1` 与 low-radius criteria；
3. 检验 selected relation classes 下 reachable-value MAY/MUST 或 interval/hole summaries 能否替代 full sets；
4. 把 `mu` escape 与 `nu` floor-line 组合成 compressed exact Pareto-frontier solver；
5. 从一个 Wronskian nondegeneracy condition 推广到多个 simultaneous certificate forms。
