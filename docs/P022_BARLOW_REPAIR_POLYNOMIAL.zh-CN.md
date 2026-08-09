# P022 — Two-Sided Coordination-History Quotient 的 Repair Polynomial

状态：`ACTIVE RESEARCH NOTE / EXACT FINITE WEIGHTED WALK / PRIOR-ART MAPPED`  
归属：`program/p022-geometry-v2`  
依赖：two-sided event-driven repair；P011 fiber/collision spectrum

## 1. Repair dimension 作为 fiber 坐标

对长度 `N` 的 two-sided microscopic Barlow window，coordination history 丢失：

- 每个 zero-departure excursion 的 orientation bit；
- 每个 diagonal split 的 side-label bit。

令

\[
r(h)=E(h)+B(h).
\]

则精确 microscopic fiber 为

\[
\boxed{|O_N^{-1}(h)|=2^{r(h)}.}
\]

## 2. P022-RP01 — Repair polynomial

定义

\[
a_{N,r}=\#\{h:r(h)=r\}
\]

及

\[
\boxed{R_N(z)=\sum_ra_{N,r}z^r.}
\]

因为所有 fiber sizes 都是 2 的幂，故

\[
\boxed{c_{2^r}=a_{N,r}}
\]

且其它 `c_s=0`。所以 `R_N` 是完整 P011 fiber profile 的 bit-dimension re-encoding。

## 3. P022-RP02 — 有限 weighted chamber recursion

coordination state 写成

\[
0\le a\le b.
\]

一步内两 coordinate 各按 reflected ±1 变化，再排序。

对 transition `p->q` 定义 repair cost

\[
w(p,q)=\#\{p\text{ 中的 zero entries}\}+\mathbf1_{p\text{ 在 diagonal 且 }q\text{ split}}.
\]

令 `F_n(a,b;z)` 为长度 `n`、终点 `(a,b)` 的 repair polynomial，则

\[
F_0(0,0;z)=1
\]

并有

\[
\boxed{F_{n+1}(q;z)=\sum_{p\to q}z^{w(p,q)}F_n(p;z).}
\]

最终

\[
\boxed{R_N(z)=\sum_qF_N(q;z).}
\]

初值：

\[
R_0=1,
\quad
R_1=z^2,
\]

\[
R_2=2z^2+z^3,
\]

\[
R_3=2z^2+z^3+3z^4,
\]

\[
R_4=4z^2+6z^3+8z^4+2z^5.
\]

## 4. P022-RP03 — 三个精确 evaluation

### Quotient image

令 `z=1`：

\[
\boxed{R_N(1)=|\operatorname{im}O_N|.}
\]

### Microscopic domain

令 `z=2`：

\[
\boxed{R_N(2)=4^N.}
\]

### 总 repair-bit load

\[
\boxed{2R_N'(2)=\sum_{\text{microscopic windows}}r(O_N(window)).}
\]

所以 polynomial derivative 在 microscopic weighting point 上精确恢复 aggregate repair cost。

## 5. P022-RP04 — 从 `R_N` 恢复 P011 collision polynomial

repair-`r` quotient state 的 fiber size 为 `2^r`，故

\[
\boxed{J_k(N)=\sum_ra_{N,r}\binom{2^r}{k}.}
\]

以及

\[
\boxed{K_N(t)=\sum_ra_{N,r}\left((1+t)^{2^r}-1\right).}
\]

因此 repair polynomial 是完整 P011 collision state 的 bit-dimension 坐标。

## 6. Classical unweighted chamber count

`R_N(1)` 的 unweighted image count 属于已有组合数学。

平移

\[
(a,b)\mapsto(a+1,b+3)
\]

把 `0<=a<=b` 映成 strict Weyl chamber

\[
0<x_1<x_2
\]

中的 lock-step walk，从 `(1,3)` 出发。

令 Catalan 数

\[
C_m=\frac1{m+1}\binom{2m}{m}.
\]

偶数 `N=2m`：

\[
\boxed{R_{2m}(1)=(2m+1)C_m^2.}
\]

奇数 `N=2m+1`：

\[
\boxed{R_{2m+1}(1)=\frac{m+2}{2}C_{m+1}^2.}
\]

该序列的 even/odd subsequences 已出现在 Catalan/Narayana/Weyl-chamber 相关既有文献与整数序列中，按 prior art 处理。

## 7. P022-RP05 — quotient-state 平均 fiber 与最坏 fiber 强烈分离

microscopic domain 为 `4^N`，所以 quotient states 上的 arithmetic mean fiber size 为

\[
\boxed{\overline f_N=\frac{4^N}{R_N(1)}.}
\]

由 Catalan asymptotic：

\[
\boxed{R_N(1)\sim\frac{8}{\pi N^2}4^N,}
\]

故

\[
\boxed{\overline f_N\sim\frac{\pi N^2}{8}.}
\]

但最大 fiber 为

\[
\boxed{f_{\max}(N)=2^{N+1}.}
\]

因此 quotient-state 平均 ambiguity 仅二次增长，而 worst ambiguity 指数增长。平均与最大都不能替代完整 fiber profile。

## 8. Sharp repair range

对 `N>=1`：

\[
\boxed{2\le r(h)\le N+1.}
\]

最小值由只保留最初两 orientation choices、之后无新的 boundary events 的 histories 达到；最大值由 equal/split alternating histories 达到。

最低非零 coefficient `a_(N,2)` 是 one-sided one-excursion history 数；最高 coefficient 有闭式：

- `N=2m`：
  \[
  a_{N,N+1}=2^{m-1};
  \]
- `N=2m+1>=3`：
  \[
  a_{N,N+1}=3\cdot2^{m-1}.
  \]

最大 fibers 占 microscopic mass 的比例为：

- even：`2^{-m}`；
- odd：`3*2^{-m-1}`。

故最大 ambiguity 虽指数大，但极端 fibers 的 microscopic mass 比例指数衰减。

## 9. Prior-art 边界

`z=1` 的 chamber count、Catalan/Narayana 数、reflection/Weyl-chamber 技术与 asymptotics 都是 established mathematics。

本项目当前特定结果是：Barlow two-sided coordination quotient 的 fiber dimension 恰由 zero-excursion 与 diagonal-split events 生成，并由 weighted polynomial 同时协调 exact repair、P011 fibers、collision statistics 与 quotient-size observables。历史新颖性保持 `NOVELTY_UNVERIFIED`。

## 10. 可执行资产

- `src/enterprise_math/p022_barlow_repair_polynomial.py`；
- `tests/test_p022_barlow_repair_polynomial.py`；
- two-sided repair module/tests。

weighted recursion 已与短 horizon direct microscopic grouping 交叉验证；closed chamber count 在更长有限范围内与 recursion 对照。