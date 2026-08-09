# P025 补充 15 —— Unit Relation 的 Ideal Intersection 与 Blockwise Access

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner：`program/p025-abc-support-collapse`  
依赖：P025 补充 13–14  
Hard block：`NONE`

## 1. `1+b=c` 的更强分解

关系

\[
\boxed{1+b=c}
\]

有一个特殊简化：单位 `1` 的 arithmetic derivative 为零，所以 relation-adapted additivity 精确等价于

\[
\boxed{d_x(b)=d_x(c).}
\]

Wronskian 也直接退化为

\[
\boxed{W_x(1,b)=d_x(b).}
\]

因此 arithmetic image 与 floor-access 都可以先在两个 block 内独立处理，而无需先建立 global Wronskian-minor lattice。

## 2. P025-D05 —— raw block derivative image generator

对 `n>1` 定义

\[
\boxed{
A(n)
=
\gcd_{p\mid n}
\frac{n v_p(n)}p.
}
\]

由 P025-T37，

\[
\boxed{A(n)=m(n)h(n).}
\]

整个 block 的 raw derivative image 精确是

\[
\boxed{
\{d_x(n):x\}
=A(n)\mathbb Z.
}
\]

因此 `A(n)` 是 raw derivative image ideal 的正生成元。

## 3. P025-T42 —— Wronskian image 是两个 principal ideals 的交

记

\[
A_b=A(b),
\qquad
A_c=A(c).
\]

unit relation 的 additive witness 必须选择一个同时落在两个 image ideals 中的 derivative value：

\[
d_x(b)=d_x(c)
\in
A_b\mathbb Z\cap A_c\mathbb Z.
\]

整数环中的 principal ideal 满足

\[
A_b\mathbb Z\cap A_c\mathbb Z
=
\operatorname{lcm}(A_b,A_c)\mathbb Z.
\]

所以正 Wronskian image generator 为

\[
\boxed{
D
=
\operatorname{lcm}(A_b,A_c).
}
\]

这给出 unit relation absorption floor 的另一条完全精确推导，不需要形成 prime-pair minors。

## 4. P025-T43 —— unit relation 的闭式 floor 公式

residual product 为

\[
M=m(b)m(c),
\]

Pasten 的 residual divisibility 保证 `M|D`，于是

\[
\boxed{
\eta_{\min}(1,b,c)
=
\frac{\operatorname{lcm}(A(b),A(c))}
{m(b)m(c)}.
}
\]

代入 `A(n)=m(n)h(n)`，得到等价形式

\[
\boxed{
\eta_{\min}(1,b,c)
=
\frac{
\operatorname{lcm}(m_b h_b,m_c h_c)
}{m_bm_c}.
}
\]

这是补充 13 一般 block formula 在 unit-block 情形的特化。

## 5. P025-D06 —— block generator access radius

`A(n)` 只回答“哪些 derivative values 可实现”，并不回答“实现某个值至少需要多大的 prime-coordinate witness”。

对任意

\[
T\in A(n)\mathbb Z
\]

定义

\[
\boxed{
\kappa_n(T)
=
\min\left\{
\|x\|_\infty:
\sum_{p\mid n}\frac{n v_p(n)}p x_p=T
\right\}.
}
\]

这是 raw derivative target `T` 的 blockwise minimum preimage access cost。

对 image generator 本身可简记

\[
\kappa(n)=\kappa_n(A(n)).
\]

于是 block 内部再次出现

\[
\boxed{
A(n)
\quad\neq\quad
\kappa_n(T).
}
\]

前者是 image content，后者是 access geometry。

## 6. P025-T44 —— `nu` 的精确 blockwise 分解

令

\[
D=\operatorname{lcm}(A_b,A_c).
\]

`1+b=c` 的 positive-floor witness 恰好由两块组成：

- b-block 坐标实现 `d_x(b)=D`；
- c-block 坐标实现 `d_x(c)=D`。

两块 prime coordinates 完全不相交，所以组合 witness 的 `L_infinity` norm 就是两块 norm 的最大值。

因此

\[
\boxed{
\nu(1,b,c)
=
\max\bigl(
\kappa_b(D),
\kappa_c(D)
\bigr).
}
\]

### 证明

任何 absorption-floor witness 都必须满足 `d_x(b)=d_x(c)=±D`；整体变号不改变 `L_infinity`。两个 block 除共同 target 外互相独立，所以分别取 minimum preimage norm，再取两者最大值，就是全局 minimum。∎

这说明 unit relation 的 global floor-access 不是一个不可分的 generic high-dimensional CVP，而是两个独立 block preimage problem 的直积。

## 7. 不用三维 solver 重获 `1+242=243`

对

\[
242=2\cdot11^2
\]

raw derivative coefficients 为

\[
121,\ 44,
\]

所以

\[
A(242)=11.
\]

对

\[
243=3^5,
\]

raw derivative coefficient 为 `405`，因此

\[
A(243)=405.
\]

故

\[
D=\operatorname{lcm}(11,405)=4455,
\]

并有

\[
\eta_{\min}
=
\frac{4455}{11\cdot81}
=5.
\]

两个独立 access equations 是

\[
121x_2+44x_{11}=4455
\]

和

\[
405x_3=4455.
\]

第一式除以 `11`：

\[
11x_2+4x_{11}=405.
\]

精确最优解可取

\[
(x_2,x_{11})=(27,27),
\]

故

\[
\kappa_{242}(4455)=27.
\]

第二块要求 `x_3=11`，所以

\[
\kappa_{243}(4455)=11.
\]

最终

\[
\boxed{\nu=\max(27,11)=27.}
\]

完全不需要 global affine-line 表达。

## 8. `1+512=513`：quality、obstruction、access 三者继续分离

对

\[
512=2^9,
\]

\[
A(512)=9\cdot2^8=2304.
\]

对

\[
513=3^3\cdot19,
\]

raw derivative coefficients 为 `513,27`，所以

\[
A(513)=27.
\]

因此

\[
D=\operatorname{lcm}(2304,27)=6912,
\]

而

\[
m(512)m(513)=256\cdot9=2304.
\]

故

\[
\boxed{\eta_{\min}=3.}
\]

`512` block 只需要坐标 `3`。`513` block 化为

\[
19x_3+x_{19}=256,
\]

最小 `L_infinity` 半径为 `13`，例如

\[
(x_3,x_{19})=(13,9).
\]

所以

\[
\boxed{\nu=13.}
\]

此前的 high-quality 反例因此具有完整独立 profile：

\[
\eta_{\min}=3,
\qquad
\nu=13,
\qquad
513^4>114^5.
\]

这里不声称三者存在任何蕴含关系。

## 9. P025-T45 —— Mersenne-prime unit family

假设

\[
\boxed{1+(2^m-1)=2^m}
\]

且 `2^m-1` 为素数。

prime block 有

\[
A(2^m-1)=1,
\]

prime-power block 只有一个坐标，且

\[
A(2^m)=m2^{m-1}.
\]

因此

\[
D=m2^{m-1},
\qquad
M=2^{m-1},
\]

故

\[
\boxed{\eta_{\min}=m.}
\]

prime block 必须用它唯一的 coefficient `1` 实现 target `D`，坐标恰为 `D`；power block 坐标为 `1`。所以

\[
\boxed{
\nu=m2^{m-1}.
}
\]

总 prime-coordinate 数只有 2，P025-T22 同时给出

\[
\boxed{\mu=\nu=m2^{m-1}.}
\]

这个族没有 norm/absorption Pareto tradeoff，但 arithmetic floor `m` 与 first witness radius `m2^(m-1)` 仍可处在完全不同的尺度。

不假设 Mersenne primes 有无穷多个。

样本：

- `m=5`：`1+31=32`，`eta_min=5`，`mu=nu=80`；
- `m=7`：`1+127=128`，`eta_min=7`，`mu=nu=448`。

## 10. 新的架构层：image content 与 generator access

unit relation 使下述区别不可回避：

\[
\boxed{
\text{image content }A(n)
\neq
\text{access cost }\kappa_n(T).
}
\]

`A(n)` 足以决定整个 block 的 derivative image ideal，所以可以参与 exact arithmetic-floor 计算。

但它无法决定实现某个 target 的 minimum coordinate radius；这一点需要更丰富的 coefficient geometry。

因此 block 内部再次重复同一结构：

\[
\boxed{
\text{generator/image state}
\to
\text{target selection}
\to
\text{minimum preimage precision}.
}
\]

这正是全局 `eta_min -> nu` 区分的局部版本。

## 11. Prior-art 纪律

principal ideal intersection、`lcm`、Bezout image generation 与 integer linear form 的 minimum-norm preimage 都属于标准数学。P025 不对这些工具作历史优先性主张。

项目侧仍处于 `NOVELTY_UNVERIFIED` 的只是反复出现的 finite-precision pattern：image generator 可以是某一算术 future language 的充分精确状态，但要访问指定 generator value，又必须保留更丰富的 precision state。

## 12. 可执行资产

新增：

- `src/enterprise_math/abc_unit_relation.py`
  - raw block derivative coefficients 与 image generator；
  - unit-relation Wronskian image 的 `lcm` ideal intersection；
  - support size 至多 2 时的 exact blockwise access；
  - Mersenne-prime 闭式族。
- `tests/test_abc_unit_relation.py`
  - `1+242=243` ideal 重建与 `nu=27`；
  - `1+512=513` 的 access radius 13；
  - squarefree Sophie 样本；
  - Mersenne `m=5,7`；
  - 明确拒绝用 brute force 悄悄隐藏 higher-rank block。

## 13. 下一前沿

没有 hard block。继续：

1. 把 `kappa_n(T)` 作为独立 precision object 研究；
2. 求其 target scaling 的精确成立/失败条件；
3. 判定何时 `kappa_n(kA(n))=|k|kappa_n(A(n))`，并系统收集严格失败反例；
4. 对 squarefree multi-prime blocks，寻找比完整 coefficient row 更小的 minimum Bezout access invariant；
5. 检验 image-content/access-cost 分层是否在其它 Enterprise Math quotient/certificate system 中重复出现。
