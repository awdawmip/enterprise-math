# P022 — Coordination History 恢复完整全局最短路 Multiplicity Spectrum

状态：`ACTIVE RESEARCH NOTE / EXACT FINITE SPECIALIZATION / NOVELTY UNVERIFIED`  
归属：`program/p022-geometry-v2`  
依赖：`P022_BARLOW_COORDINATION_HISTORY.*`、geodesic multiplicity、Barlow prefix normal form

## 1. 从 path total 提升到完整 witness 分布

已有结果

\[
(S_0,\ldots,S_n)\Longrightarrow T_n
\]

只恢复 radius-`n` shell 上全部最短路的总数。

定义完整全局 multiplicity spectrum

\[
\boxed{
\mathcal M_n(m)
=
\#\{v:d(0,v)=n,\ g(0,v)=m\}.
}
\]

它同时恢复

\[
S_n=\sum_m\mathcal M_n(m)
\]

和

\[
T_n=\sum_m m\mathcal M_n(m).
\]

## 2. P022-CH06 — 单层 histogram 只依赖 `(n,q,|delta|)`

固定 shell radius `n` 与 unsigned height

\[
q=|k|.
\]

Barlow prefix normal form 为

\[
P_k
=(A+3)^{(q-|\delta_k|)/2}
B_{\operatorname{sgn}\delta_k}^{|\delta_k|}.
\]

literal prefix order 已消失。改变 `delta_k` 的符号只会把 `B_+` 与 `B_-` 互换，对 axial coordinates 做反射，不改变该层 shortest-path multiplicity 的 multiset。

因此该层 histogram 只需要

\[
\boxed{(n,q,d),\qquad d=|\delta_k|.}
\]

## 3. P022-CH07 — coordination history 恢复 global spectrum

coordination history 已恢复每个 height 的无序 pair

\[
P_q=\{|\delta_q|,|\delta_{-q}|\}.
\]

对 `q>0`，正负两层分别贡献

\[
\mathcal M_{n,q,|\delta_q|}
\]

和

\[
\mathcal M_{n,q,|\delta_{-q}|}.
\]

全局 spectrum 不记录两层的 side label，因此只需把两份 histogram 做 multiset union；交换两个 drift 不改变结果。

中央层固定。因此

\[
\boxed{
(S_0,S_1,\ldots,S_n)
\Longrightarrow
\mathcal M_n.
}
\]

逐 radius 应用又得到

\[
\boxed{
\mathcal H_S(n)
\Longrightarrow
(\mathcal M_0,\ldots,\mathcal M_n).
}
\]

原先 `H_S -> H_T` 只是这个更强结果的一阶 moment shadow。

## 4. 反向在 radius 2 已失败

FCC 与 HCP 到 radius 2 的 total-path history 都是

\[
(1,12,84),
\]

但 multiplicity spectra 分别为

\[
\boxed{
\mathcal M_2^{FCC}=\{1:12,2:24,4:6\},
}
\]

和

\[
\boxed{
\mathcal M_2^{HCP}=\{1:18,2:18,3:2,4:6\}.
}
\]

故 path-total history 不能恢复 global multiplicity spectrum。

## 5. P022-CH08 — global spectrum 仍不是 coordinate-labelled geometry

取两个 one-sided prefixes

\[
w=(+,-,+,+),
\qquad
w'=(+,-,-,-).
\]

它们 signed imbalance histories 为

\[
(1,0,1,2)
\]

与

\[
(1,0,-1,-2),
\]

所以 absolute histories 完全相同：

\[
(1,0,1,2).
\]

因此在另一侧固定时，coordination history 与 global multiplicity spectrum 都相同。

但 layer 3 的 signed drifts 是 `+1` 与 `-1`，对应 support shape 为镜像；例如 horizontal coordinate `(2,0)` 可属于前者的 minimal vertical support，而不属于后者。

所以

\[
\boxed{
\mathcal H_S
\not\Rightarrow
\text{coordinate-labelled layer support/distance field}.
}
\]

coordination history 恢复的是 absolute witness distribution，不是 orientation-sensitive geometry。

## 6. 信息层级

当前 Barlow specialization 的一条严格方向是

\[
\text{coordinate-labelled geometry}
\to
\text{unsigned-height layer spectra}
\to
\text{global multiplicity spectrum}
\to
\text{path total}
\to
\text{existence}.
\]

coordination history 足够恢复 global multiplicity spectrum，但不能恢复第一层。

关键底层结论是：

> 当 hidden transition law 使缺失状态可从 observation history 递归观测时，保留历史本身可以成为更丰富 future language 的充分状态。

这一性质依赖两通道 Barlow 结构，并非任意 quadratic-history 系统的一般事实。

## 7. 验证

- `src/enterprise_math/p022_barlow_history_multiplicity.py`；
- `tests/test_p022_barlow_history_multiplicity.py`。

分支内 reconstruction 已对 period≤4、radius≤4 的全部周期 sign patterns 与直接 endpoint enumeration 做过有限交叉检查，无不一致。