# P022 — 半指标 Franel defect 的素数折半支撑树

状态：`ACTIVE RESEARCH NOTE / EXACT SUPPORT SUPERSET + LOCATION BOUNDS`  
Owner：`program/p022-geometry-v2`  
依赖：central-binomial A-elimination；Franel half-index family；integer midpoint companion  
开放目标：证明或证伪 `p = 5 或 23 (mod 24)` family 的 support avoidance。

## 1. 为什么旧 support 问题尺度过大

对

\[
p\equiv5,23\pmod{24},\qquad m=(p-1)/2,
\]

半指标 witness 满足 `p|F_m`，且 `2m-1=p-2` 为合数，因此 canonical pure Franel defect `D_m` 有定义。

若希望

\[
v_p(D_m)=v_p(F_m),
\]

就必须保证 central-binomial elimination 使用的所有更早 Franel 因子都是 `p`-adic unit。

直接做法会把 support 与

\[
F_1,\ldots,F_{m-1}
\]

全部比较。central-binomial recursion 说明这远远过度。

## 2. P022-LI33 — 素数折半树

精确恒等式

\[
\frac{A_n}{A_{n-1}}=\frac{2(2n-1)}n,
\qquad A_n=\binom{2n}{n}
\]

中，一个奇素数 `q` 通过

\[
j=(q+1)/2
\]

进入 A-basis。表达 `q` 时只新增相邻指标

\[
j,\ j-1,
\]

并继续递归展开更小整数 `j`。

因此定义正整数 `v` 的**prime-halving tree**：

1. 根节点取 `v` 的奇素因子；
2. 对每个节点 `q`，继续取 `(q+1)/2` 的奇素因子；
3. 每个节点产生 A-index candidates `(q+1)/2` 与 `(q-1)/2`。

对 half defect，exact canonical support 严格包含于

\[
\boxed{
\{1,m-1\}
\cup C(p-2)
\cup C(m),
}
\]

其中 `C(v)` 是该树产生的 index set。

后续指数相消可能让 exact support 更小；这棵树是严格的 support 超集。

## 3. P022-LI34 — polylogarithmic support complexity

任何节点 `q` 的子素数 `r` 都满足

\[
r\le\frac{q+1}{2}\le\frac{2q}{3}
\qquad(q\ge3).
\]

所以任意 root-to-leaf path 只有对数深度。

在固定深度上，所有奇素数节点按重数计算的乘积不超过上一层，因而不超过起始整数；每个节点至少为 `3`，因此每层节点数量同样至多对数量级。

由此

\[
\boxed{|C(v)|=O((\log v)^2),}
\]

half-defect candidate support 的规模为

\[
\boxed{O((\log p)^2).}
\]

所以 support avoidance 本质上不是 `O(p)` 的表扫描，而是**一个 polylogarithmic arithmetic tree 与 companion-zero set 的 incidence 问题**。

## 4. P022-LI35 — 目标等差类的显式位置界

### `p = 5 (mod 24)`

`p-2` 为奇数且可被 `3` 整除，因此其任意奇素因子至多为 `(p-2)/3`。同时

\[
m=(p-1)/2
\]

为偶数，所以 `m` 的任意奇素因子至多为 `(p-1)/4`。

所有后继节点只会继续减小，于是除相邻项外的 candidate support 必满足

\[
\boxed{j\le\frac{p+1}{6}.}
\]

### `p = 23 (mod 24)`

`p-2` 同样被 `3` 整除；但此时 `m` 本身可能为素数，因此来自 `m` 一侧的最坏 A-index 是

\[
(m+1)/2=(p+1)/4.
\]

于是

\[
\boxed{j\le\frac{p+1}{4}.}
\]

特殊 support index `m-1` 永远安全，因为 `F_m=0 (mod p)`，而 Franel recurrence 禁止相邻两项同时为零。

## 5. P022-LI36 — 危险 companion offset 只能位于远尾部

令

\[
d=m-j.
\]

结合位置界与整数 companion 判据

\[
p\mid F_{m-d}\iff p\mid H_d
\]

得到：

- `p=5 (mod 24)` 时，任何非相邻 dangerous support zero 必须满足
  \[
  \boxed{d\ge(p-2)/3;}
  \]
- `p=23 (mod 24)` 时，必须满足
  \[
  \boxed{d\ge(p-3)/4.}
  \]

所以目标等差类中，所有靠近 midpoint 的 companion zeros 都自动与 canonical half-defect elimination 无关。

## 6. 精确 incidence 表述

若 candidate support index `j=m-d` 来自 halving-tree 节点 `q`，则

\[
j=(q+1)/2\quad\text{或}\quad j=(q-1)/2.
\]

因此必有

\[
\boxed{q=p-2d-2\quad\text{或}\quad q=p-2d.}
\]

一个真正危险的 cancellation 必须同时满足：

1. universal integer companion 中 `p|H_d`；
2. residual prime `p-2d` 或 `p-2d-2` 属于从 `p-2` 或 `m` 生成的 prime-halving tree；
3. 对应 candidate 在 exact coefficient cancellation 后仍然存在。

这就是当前无限问题的最窄算术表述。

## 7. 负边界

强制 midpoint 即使具有非常早的额外 zeros，也不必威胁 half defect。

例如 `p=173` 的 zero alphabet 是

\[
\{4,86,168\},
\]

但 exact A-elimination support 不含 `4`。

相反，更宽 family 中的 `p=157` 在 `16` 有 zero，而且 `16` 恰好属于 canonical elimination support，因此 midpoint valuation 被抵消。由此可见 forced midpoint 本身远远不够。

## 8. 可执行资产

- `src/enterprise_math/p022_barlow_half_defect_support_tree.py`
- `tests/test_p022_barlow_half_defect_support_tree.py`

测试把 tree superset 与 exact elimination support 逐项对照，并在较宽有限素数区间核验目标位置界。有限核验只是 regression evidence，不替代尚未完成的无限 avoidance proof。
