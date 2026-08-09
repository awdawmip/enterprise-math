# P022 — Barlow Absolute History 的 Excursion 方向修复

状态：`ACTIVE RESEARCH NOTE / EXACT FINITE FIBER SPECTRUM / PRIOR-ART SENSITIVE`  
归属：`program/p022-geometry-v2`  
依赖：Barlow signed prefix drift；P011 fiber/collision spectrum

## 1. Absolute history 丢失的信息远少于每层一个 sign bit

对 one-sided microscopic stacking word

\[
\sigma=(\sigma_1,\ldots,\sigma_N)\in\{-1,+1\}^N,
\]

定义

\[
\delta_k=\sum_{j=1}^k\sigma_j,
\qquad
\boxed{d_k=|\delta_k|.}
\]

`d` 是从 0 出发的非负 nearest-neighbor walk。绝对值操作丢掉方向，但丢失自由度并不是每个 layer 独立产生。

## 2. Excursions

定义 nonzero excursion 为一次

\[
0\to1
\]

出发后，到下一次回到 0，或一直持续到 horizon 结束的最大区间。

令

\[
\boxed{
e(d)=\#\{k:d_{k-1}=0,\ d_k=1\},
}
\]

其中 `d_0=0`。

## 3. P022-ER01 — 一个 excursion 内 sign 完全刚性

一旦某个 excursion 选择 `+` 或 `−` 方向，在回到 0 之前 signed drift 不可能改变符号；否则必须先穿过 0，excursion 已经结束。

反之，每次回到 0 以后，下一个 excursion 的方向可重新独立选择。

因此 hidden sign degrees of freedom 由 excursions 编号，而不是由 layers 编号。

## 4. P022-ER02 — 精确 microscopic fiber 大小

对固定 absolute history `d`，给每个 excursion 独立选择

\[
\epsilon_j\in\{-1,+1\}.
\]

这唯一恢复 signed drift，进而恢复

\[
\sigma_k=\delta_k-\delta_{k-1}\in\{-1,+1\}.
\]

不同 orientation assignments 产生不同 microscopic words，故

\[
\boxed{|O^{-1}(d)|=2^{e(d)}.}
\]

最小 exact repair 为

\[
\boxed{\text{每个 excursion 一个 orientation bit}.}
\]

## 5. Event-driven precision

新的方向自由度只在 absolute state 离开 zero boundary 时产生。因此精确 repair schedule 是 boundary-event driven，而不是固定每层写一个 bit。

这与 P023 的 boundary-bit repair 有结构相似性，但这里是从 Barlow excursion dynamics 独立推得的 specialization。

## 6. P022-ER03 — 固定 excursion 数的 absolute history 数量

令

\[
A_{N,e}=\#\{\text{长度 }N\text{ 且有 }e\text{ 个 excursions 的 absolute histories}\}.
\]

若

\[
N=2m+1,
\]

则

\[
\boxed{A_{2m+1,e}=\binom{2m+1-e}{m+1-e}.}
\]

若

\[
N=2m>0,
\]

则

\[
\boxed{A_{2m,e}=2\binom{2m-e-1}{m-e}.}
\]

`N=0` 时只有一条空 history，excursion 数为 0。

## 7. ER03 的 Catalan 分解证明

令 Catalan generating function 为

\[
C(z)=1+zC(z)^2.
\]

完整正 excursion 的 half-length generating function 为

\[
I(z)=zC(z).
\]

奇数总长度时，最后一个 excursion 未闭合，使用

\[
\frac1{\sqrt{1-4z}}.
\]

偶数总长度时，最后一个 complete/incomplete excursion 的组合化简为

\[
\frac{2z}{\sqrt{1-4z}}.
\]

再用经典系数恒等式

\[
\boxed{[z^n]\frac{C(z)^k}{\sqrt{1-4z}}=\binom{2n+k}{n}}
\]

得到上述闭式。Catalan/ballot/reflection ingredients 属于既有组合数学。

## 8. P022-ER04 — absolute-history quotient 的完整 fiber profile

ER02 与 ER03 合并得到

\[
\boxed{c_{2^e}=A_{N,e},}
\]

其余非 2 的幂的 fiber sizes 全为 0。

并有两个一致性恒等式：

\[
\boxed{\sum_eA_{N,e}=\binom{N}{\lfloor N/2\rfloor}}
\]

以及

\[
\boxed{\sum_e2^eA_{N,e}=2^N.}
\]

最大 excursion 数为

\[
\left\lceil\frac N2\right\rceil,
\]

故最大 orientation fiber 为

\[
\boxed{2^{\lceil N/2\rceil}.}
\]

## 9. P022-ER05 — 完整 P011 collision spectrum

P011 的

\[
J_k=\sum_y\binom{|O^{-1}(y)|}{k}
\]

在此 specialization 中变成

\[
\boxed{J_k(N)=\sum_eA_{N,e}\binom{2^e}{k}.}
\]

collision polynomial 为

\[
\boxed{K_N(t)=\sum_eA_{N,e}\bigl((1+t)^{2^e}-1\bigr).}
\]

## 10. 精度结论

状态链为

\[
\text{literal stacking word}
\to
\text{signed drift history}
\to
\text{absolute drift history}
\to
\text{更粗 shell statistics}.
\]

signed→absolute 的 exact repair dimension 是 realized path 的 excursion 数：

\[
\boxed{\text{repair dimension}=e(d).}
\]

同一 horizon 的不同 histories 因而可需要完全不同的 repair 大小。

## 11. 可执行验证

- `src/enterprise_math/p022_barlow_excursion_repair.py`；
- `tests/test_p022_barlow_excursion_repair.py`。

测试对短 horizon 全部 microscopic words 按 absolute history 分组，验证 `2^e` fiber、excursion orientation reconstruction、闭式 excursion spectrum 与 P011 collision formulas。