# P022 — Terminal Shell Stratification 对 Coordination History 的重新编码

状态：`ACTIVE RESEARCH NOTE / EXACT FINITE EQUIVALENCE / NOVELTY UNVERIFIED`  
归属：`program/p022-geometry-v2`  
依赖：coordination-history reconstruction；layer path-total 与 extreme-layer cardinality formulas

## 1. History 不必以时间序列形式保存

完整 coordination history

\[
\mathcal H_S(n)=(S_0,S_1,\ldots,S_n)
\]

恢复每个 height 的无序 absolute drift pair

\[
P_q=\{|\delta_q|,|\delta_{-q}|\}.
\]

这里问：如果 terminal radius-`n` shell 保留 height stratification，同一信息能否完全编码在**一个终端空间切片结构**中？答案是肯定的。

## 2. Non-extreme layer path total 对 absolute drift 可逆

固定 terminal radius `n` 与

\[
0<q<n.
\]

合法 drift `d=|delta|` 下 shortest-path total 为

\[
\boxed{
L_{n,q}(d)
=
\binom nq
\left[
3\,2^{n-q+(q-d)/2}(1+2^d)-6
\right].
}
\]

它随 `d` 严格增加，因此正负 `q` 两层 path totals 的无序 pair 能恢复

\[
\boxed{\{|\delta_q|,|\delta_{-q}|\}.}
\]

## 3. P022-HS01 — Non-extreme layers 的闭式 2-adic inversion

定义

\[
Y=
\frac{L_{n,q}(d)/\binom nq+6}{3\cdot2^{n-q}}.
\]

则

\[
\boxed{Y=2^{(q-d)/2}+2^{(q+d)/2}.}
\]

若 `Y` 是一个 2 的幂，两项指数相同，故 `d=0`。

若 `d>0`，令

\[
a=v_2(Y),
\]

则

\[
\boxed{Y/2^a-1=2^d.}
\]

所以可直接从二进制 exponent 恢复 `d`，全过程 integer-only。

## 4. Extreme layer 边界

在

\[
q=n
\]

时，所有 shortest paths 都纯 vertical，path total 永远是

\[
\boxed{3^n,}
\]

完全看不到 drift。

但 extreme layer vertex count 为

\[
\boxed{A_{n,n}(d)=\frac{3n^2+6n+4-d^2}{4},}
\]

故

\[
\boxed{d^2=3n^2+6n+4-4A_{n,n}.}
\]

一个 integer `isqrt` 即恢复 `d`。

## 5. P022-HS02 — Terminal stratified profile

定义 terminal profile `P_n`：

- `q=0`：保留固定中央层 path total；
- `1<=q<n`：保留 `+q/-q` 两层 shortest-path totals 的无序 pair；
- `q=n`：改为保留正负 extreme-layer vertex counts 的无序 pair。

HS01 与 extreme inversion 给出

\[
\mathcal P_n\Longrightarrow(P_0,P_1,\ldots,P_n).
\]

coordination formula 再恢复所有 `S_q`。

反过来，coordination history 恢复全部 `P_q`，因此构造 `\mathcal P_n`。

所以

\[
\boxed{\mathcal P_n\Longleftrightarrow\mathcal H_S(n).}
\]

等价只丢正负两侧的交换，这本来就不在 whole-shell coordination observation 中。

## 6. History–stratification duality

在这一有限系统中，得到字面意义的

\[
\boxed{
\text{radius history}
\Longleftrightarrow
\text{terminal height stratification}.
}
\]

不需要连续嵌入或外部时间坐标。过去的 observation 信息被终端 shell 不同 height 上的整数 witness observables 重新编码。

该结论严格限于已证明的 Barlow structure，不外推成任意系统的一般“历史空间化”原则。

## 7. 信息丢失边界

height labels 不可省略。若把 layer totals 聚合成单个 global `T_n`，不同 stratifications 会碰撞。

terminal profile 也只恢复 absolute drift pairs，不恢复 signed orientation 或 labelled side assignment；这些需要 two-sided event-driven repair 中的 boundary bits。

当前链条为

\[
\boxed{
\text{labelled signed stacking window}
\to
\mathcal P_n\simeq\mathcal H_S(n)
\to
\text{global shell aggregates}.
}
\]

每个箭头都有明确的 repair boundary。

## 8. 可执行资产

- `src/enterprise_math/p022_barlow_history_stratification.py`；
- `tests/test_p022_barlow_history_stratification.py`。

inverse 只使用整数运算、`v_2`、bit length 与 `isqrt`；测试对短范围全部 reachable drift histories 做 profile/history round-trip，并验证 extreme layer 的特殊性。