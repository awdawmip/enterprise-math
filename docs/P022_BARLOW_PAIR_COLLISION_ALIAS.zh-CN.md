# P022 — Barlow Checkpoint Geometry 的 Pair-Collision Alias

状态：`ACTIVE RESEARCH NOTE / EXACT COUNTEREXAMPLE / PRIOR-ART SENSITIVE`  
归属：`program/p022-geometry-v2`  
依赖：P011 `J_2`；P022 checkpoint fiber convolution

## 1. 问题

最终层被观察时，segment lengths 为 `ell_1,...,ell_m`。令

\[
B_n=\binom{2n}{n}.
\]

ordered equal-observation pair moment 为

\[
M_2=\prod_jB_{\ell_j},
\]

由于 microscopic domain size 为 `2^N`，

\[
\boxed{J_2=\frac{M_2-2^N}{2}.}
\]

固定总长度 `N`、checkpoint 数 `m` 与精确 `J_2`，能否恢复 segment-length multiset？答案是否定的。

## 2. P022-PA01 — 按总长度最早出现的有限 alias

对固定 `(N,m)` 的正 segment multisets 做完整有限搜索，在

\[
N\le20
\]

没有发现 `M_2` alias。

第一次出现在

\[
N=21,\qquad m=4.
\]

两个不同 multisets

\[
\boxed{(1,5,5,10)}
\]

与

\[
\boxed{(2,2,6,11)}
\]

满足

\[
\boxed{B_1B_5^2B_{10}=B_2^2B_6B_{11}=23465490048.}
\]

故二者都有

\[
\boxed{J_2=11731696448.}
\]

`N<=20` 的陈述是该 segment-multiset class 内的 exhaustive finite result，不外推到其它 observation systems。

## 3. Product identity 的精确证明

利用

\[
\frac{B_n}{B_{n-1}}=4-\frac2n,
\]

有

\[
\frac{B_6}{B_5}=\frac{11}{3},
\qquad
\frac{B_{11}}{B_{10}}=\frac{42}{11}.
\]

因此

\[
\frac{B_2^2B_6B_{11}}{B_1B_5^2B_{10}}
=
\frac{36}{2\cdot252}\frac{11}{3}\frac{42}{11}=1.
\]

完全不需要近似。

## 4. 更高信息会分离这两个 schedules

二者完整 fiber profiles 不同。具体：

- image sizes：`792` 与 `756`；
- `J_3`：
  \[
  \boxed{64506690871040}
  \]
  与
  \[
  \boxed{70446056775360}.
  \]

所以

\[
\boxed{(N,m,J_2)\not\Rightarrow\text{segment multiset}.}
\]

## 5. 更简洁的 three-segment alias

稍晚的例子：

\[
(1,4,17)
\]

与

\[
(2,2,18),
\]

其中 `N=22,m=3`。

它们满足

\[
B_1B_4B_{17}=B_2^2B_{18}=326704870800,
\]

因为

\[
\frac{B_{18}}{B_{17}}=\frac{35}{9}
\]

且

\[
\frac{B_2^2}{B_1B_4}\frac{B_{18}}{B_{17}}
=
\frac{36}{140}\frac{35}{9}=1.
\]

二者 `J_2` 都为

\[
163350338248,
\]

但 image size 分别 `180` 与 `171`，`J_3` 也不同。

## 6. 精度含义

`J_2` 是合法的 ambiguity statistic，但只是完整 fiber geometry 的一个 projection。

这个 exact alias 证明：

> 匹配或最小化 `J_2`，并不等价于识别 quotient geometry。

当 future language 会响应 higher collision blocks、worst fibers 或完整 observation image 时，低阶统计不足。

在 Barlow specialization 中，完整 P011 collision polynomial 则可通过 fiber-convolution theorem 反推出 segment multiset 与 hidden tail，因此不存在这一低阶 alias。

## 7. 可执行资产

- `src/enterprise_math/p022_barlow_pair_collision_alias.py`；
- `tests/test_p022_barlow_pair_collision_alias.py`。

测试保留精确恒等式、higher-statistic separation，并 exhaustive 检查总长度小于 21 的固定 `(N,m)` segment multisets。