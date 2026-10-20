# 进取原生 filament 零线排列：缺陷持久性与出生阶梯

Status: `FREE_RESEARCH_EXACT_COLLAPSE_PERSISTENCE_INVARIANT / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-24`

Researcher-ID: `EM-FREE-NEPS-239A6D`

## 一、窗口增长与 deletion–restriction

固定特征 \(q\)、手性 \(\chi\)，并在斜率两两不同的范围内考虑从长度
\(k\) 增长到 \(k+1\) 的零线排列。

旧排列有 \(k\) 条线，新增边界线与旧 union 相交于 \(s_k\) 个不同点。

Grothendieck deletion–restriction 给出：
\[
[X_{k+1}]=[X_k]-\mathbb L+s_k.
\]

因此排列特征常数满足
\[
b_{k+1}=b_k+s_k.
\]

而缺陷
\[
\delta_k=\binom k2-b_k
\]
满足
\[
\boxed{
\delta_{k+1}-\delta_k=k-s_k\ge0
}.
\]

这里 \(k-s_k\) 正是新增边界线上名义 \(k\) 个 pair intersections 因共点而发生的碰撞数。

## 二、原生坍缩单调性

所以：

- 向窗口中增加一个 Cell，\(\delta_k\) 只能增加或保持；
- 端点 puncturing \(k+1\to k\) 时，\(\delta\) 只能下降或保持；
- 一旦某个 \(q\)-通道在某一窗口长度出生为 exceptional，它在后续 slope-distinct 窗口中不会自行消失。

冻结：
\[
\boxed{
\delta_k^\chi(q)
\text{ 是窗口 puncturing tower 的整数 persistence invariant}
}.
\]

这比单独列出 exceptional primes 更强：它同时记录异常何时出生、之后累计了多少 boundary collisions。

## 三、\(k=3,\ldots,9\) 的精确 defect barcodes

表中 “—” 表示 \(q\le k-1\)，斜率已发生模 \(q\) 碰撞，不属于当前 distinct-slope arrangement 层。

### Plus chirality

| \(q\backslash k\) | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 5  | 0 | 1 | 2 | — | — | — | — |
| 7  | 0 | 0 | 0 | 1 | 3 | — | — |
| 11 | 0 | 0 | 0 | 1 | 2 | 4 | 7 |
| 13 | 0 | 0 | 0 | 0 | 1 | 2 | 4 |
| 23 | 0 | 0 | 0 | 1 | 2 | 3 | 4 |
| 31 | 0 | 0 | 0 | 0 | 0 | 1 | 2 |
| 53 | 0 | 0 | 0 | 0 | 0 | 1 | 2 |

### Minus chirality

| \(q\backslash k\) | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 5  | 0 | 1 | 3 | — | — | — | — |
| 7  | 0 | 0 | 0 | 1 | 3 | — | — |
| 11 | 0 | 0 | 0 | 1 | 2 | 4 | 7 |
| 13 | 0 | 0 | 0 | 0 | 0 | 2 | 3 |
| 23 | 0 | 0 | 0 | 1 | 2 | 3 | 5 |
| 31 | 0 | 0 | 0 | 0 | 0 | 1 | 2 |
| 53 | 0 | 0 | 0 | 0 | 0 | 1 | 2 |

## 四、出生长度

在长 filament 的 \(k=5,\ldots,9\) 范围内：

- \(q=5\)：进入长窗口前已经出生；
- \(q=7,11,23\)：在 \(k=6\) 出生；
- \(q=13\)：plus 在 \(k=7\) 出生，minus 延迟到 \(k=8\)；
- \(q=31,53\)：在 \(k=8\) 出生；
- 到 \(k=9\) 不再出现新 exceptional prime，只增加已有通道的 collision multiplicity。

因此 exceptional support 在 \(k=8\) 饱和，而 defect multiplicity 继续增长到 sharp cap \(k=9\)。

## 五、手性偏差的 persistence 解释

两个非平衡 sharp-nine 通道可以由 barcode 差直接读出：

### \(q=13\)

\[
\delta_7^+=1,\qquad\delta_7^-=0.
\]

plus 手性比 minus 提前一个窗口长度出生。到 \(k=9\)：
\[
\delta_9^+=4,\qquad\delta_9^-=3,
\]
因此
\[
N_+-N_-=\delta_- -\delta_+=-1.
\]

### \(q=23\)

两手性都在 \(k=6\) 出生，并一直相等到 \(k=8\)。增加第九个 Cell 时：

\[
\delta_9^+=4,\qquad\delta_9^-=5.
\]

minus 边界多产生一个 collision，因此
\[
N_+-N_-=+1.
\]

所以 sharp-nine 的两个手性 defect 具有两种不同来源：

1. \(q=13\)：**出生时间错位**；
2. \(q=23\)：**最终边界增量错位**。

## 六、当前意义

这给出一条完整的进取坍缩条形码：

\[
\boxed{
\text{prime channel}
\to
\text{exception birth length}
\to
\text{monotone defect accumulation}
\to
\text{sharp }k=9\text{ terminal charge}
}.
\]

它仍是 geometry-selected local sieve arrangement 的结构量，不等同于新的实际 prime-frequency law；但它已经是一个严格可组合、可向下投影、不会被单个 prime/composite bit 图样替代的多 Cell 原生读数。
