# P022 — Coordination History 的 Two-Sided Event-Driven Repair

状态：`ACTIVE RESEARCH NOTE / EXACT FINITE REPAIR / NOVELTY UNVERIFIED`  
归属：`program/p022-geometry-v2`  
依赖：coordination-history drift reconstruction；excursion orientation repair

## 1. Coordination history 仍丢失什么

whole-shell coordination history 在每个 radius 恢复无序 absolute drift pair

\[
P_q=\{|\delta_q^+|,|\delta_q^-|\}.
\]

要恢复两条**带侧标签、带符号**的 microscopic stacking windows，还差两类独立自由度：

1. 每个 absolute channel 的 nonzero excursion orientation；
2. 两个相等 absolute channels 分叉时，哪一侧走向较大 successor。

这些自由度只在事件发生时产生。

## 2. Zero-departure events

每当某个 absolute channel 位于 0，下一步离开 0，就开始一个新的 signed excursion，需要新的 orientation bit。

定义

\[
E(P)=\sum_{q=1}^{N}\#\{P_{q-1}\text{ 中的 zero entries}\},
\]

其中

\[
P_0=\{0,0\}.
\]

这是两条 labelled channels 总 excursion 数，而且不依赖 side labels 如何恢复。

## 3. Diagonal-split events

若

\[
P_{q-1}=\{d,d\}
\]

而

\[
P_q=\{d-1,d+1\},
\]

无序 observation 无法判断哪一侧向内、哪一侧向外，需要一个 side-label bit。

定义

\[
\boxed{B(P)=\#\{q:P_{q-1}=\{d,d\},\ P_q\text{ unequal}\}.}
\]

一旦两侧不相等，其 labels 会被 nearest-neighbor continuity 强制保持，直到再次相遇。因此两个 diagonal meetings 之间不需要额外 side bits。

## 4. P022-TR01 — Ordered absolute histories 构成 `2^B` fiber

给每个 diagonal split 选择一个 bit，指定哪一侧取较大 successor。split 之间的 labelled continuation 唯一。

所以

\[
\boxed{\#\{\text{ordered absolute realizations of }P\}=2^{B(P)}.}
\]

## 5. P022-TR02 — 精确 microscopic fiber 大小

固定 labelled absolute realization 后，one-sided excursion theorem 给每个 excursion 一个 orientation bit。总 excursion 数是无序 history invariant `E(P)`。

故

\[
\boxed{|O^{-1}(P)|=2^{E(P)+B(P)}.}
\]

exact repair-bit dimension 为

\[
\boxed{r(P)=E(P)+B(P).}
\]

最小 repair 不是每层一个 bit，而是：

- 每个 zero-departure excursion 一个 orientation bit；
- 每个 diagonal split 一个 side-label bit。

## 6. P022-TR03 — Sharp repair range

对任意非空 horizon `N`：

\[
\boxed{2\le r(P)\le N+1.}
\]

### 下界

第一步两条 zero channels 都离开 0，因此至少产生两个 orientation bits。若之后两条 channels 一直重合向外且不回零，不再出现新的 repair events，可达到下界。

### 上界

单步 repair cost 只有在前态为

\[
\{0,0\}
\]

时才可能达到 2。每次后续再次到达 `{0,0}`，前一步必须是 `{1,1}->{0,0}`，该步 repair cost 为 0。因此后续每个额外 `+1` 都与一个之前的 `-1` 抵消，只有初始 step 的额外 bit 无法抵消。

故总量至多 `N+1`。交替 history

\[
\{1,1\},\{0,2\},\{1,1\},\{0,2\},\ldots
\]

达到上界。

## 7. Aggregate split load

对全部 `4^N` 个 ordered microscopic windows，diagonal split 也可精确计数。

prefix time `t>=1` 时，split 要求两条 signed walks 的 absolute magnitudes 相等且非零。这样的 ordered prefix pairs 数为

\[
2\binom{2t}{t}
-2\mathbf1_{2\mid t}\binom{t}{t/2}^2.
\]

四种下一步组合中恰有两种会 split absolute magnitudes，suffix 任意。因此总 diagonal-split bit load 为

\[
\boxed{
D_N
=
\sum_{t=1}^{N-1}
\left[
\binom{2t}{t}
-\mathbf1_{2\mid t}\binom{t}{t/2}^2
\right]4^{N-t}.
}
\]

与两侧 excursion repair load 合并即可得到 exact aggregate two-sided repair load。

## 8. 精度含义

coordination history 的 hidden information 只在两个几何边界重新产生：

- **zero boundary**：重新产生 orientation freedom；
- **diagonal symmetry boundary**：重新产生 side identity ambiguity。

因此 repair 由 symmetry-breaking events 决定，而不是由 elapsed horizon 均匀决定。

## 9. 可执行资产

- `src/enterprise_math/p022_barlow_two_sided_repair.py`；
- `tests/test_p022_barlow_two_sided_repair.py`；
- `src/enterprise_math/p022_barlow_repair_polynomial.py`。

短 horizon direct grouping 已验证 `2^(E+B)` 与事件 bit reconstruction 精确一致。