# P025 补充 14 —— Squarefree Arithmetic Floor 与大 Access Delay

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner：`program/p025-abc-support-collapse`  
依赖：P025 补充 07、13  
Hard block：`NONE`

## 1. 目的

补充 13 已证明：若未来任务只问 arithmetic absorption floor，那么 block 内部的 prime-coordinate 信息可以压成很小的 block content。自然的反证问题是：这种算术压缩是否也保留“访问这个 floor 至少需要多大 witness 半径”的几何信息？

答案是否定的。

下面给出一个非常干净的条件族：它完全没有 arithmetic absorption obstruction，但 floor-access radius 可以远大于 first witness radius。

## 2. 条件 Sophie Germain 族

设 `q` 为奇素数，且

\[
\boxed{c=2q+1}
\]

也是素数。于是

\[
\boxed{1+2q=c}
\]

是 primitive abc triple，且所有非单位项都是 squarefree。

这里不假设也不声称这类素数有无穷多个；定理只作用于实际满足条件的每一对素数。

因为整个 triple squarefree，P025-T16 立即给出

\[
\boxed{\eta_{\min}=1.}
\]

并且

\[
h(2q)=1,
\qquad
h(c)=1.
\]

所以 arithmetic-floor language 看不到任何非平凡吸收障碍。

## 3. P025-T39 —— 精确 floor-access radius

对 unit-first relation `1+b=c`，Wronskian 就是

\[
W(1,b)=d_x(b).
\]

这里 `b=2q` squarefree，在 prime coordinates `(2,q)` 上

\[
\boxed{d_x(2q)=q x_2+2x_q.}
\]

又因为 `M=1`、`eta_min=1`，absorption-floor witness 必须满足

\[
\boxed{q x_2+2x_q=\pm1.}
\]

`c`-block 是单素数 block，additivity 只要求它的单坐标等于同号 `±1`，不会把最优半径推到 1 以上的新尺度。

对奇数 `q`，方程

\[
q u+2v=1
\]

的最小 `L_infinity` 解为

\[
\boxed{u=1,
\qquad
v=\frac{1-q}{2}.}
\]

因此

\[
\boxed{
\nu
=
\frac{q-1}{2}.
}
\]

### 最优性证明

模 `2` 立即得到 `u` 必须为奇数。可选值依次为 `..., -3,-1,1,3,...`。取 `u=1` 时，

\[
v=(1-q)/2.
\]

取 `u=-1` 时，

\[
v=(q+1)/2,
\]

绝对值已经更大。再把 `u` 改变任何额外的 `2` 倍数，都会让 `v` 改变一个 `q` 的整数倍，因此最大坐标只会继续增大。故上述解为精确 `L_infinity` 最优。∎

## 4. P025-T40 —— first witness radius 保持很小

完整 additive relation 是

\[
q x_2+2x_q-x_c=0,
\]

同时

\[
W=q x_2+2x_q=x_c.
\]

对 `q>=5`，

\[
\boxed{(x_2,x_q,x_c)=(0,1,2)}
\]

就是 radius `2` 的非退化 witness，所以 `mu<=2`。

radius `1` 不可能：

- 若 `x_2=0`，则非零 `W` 为偶数，故 `|W|>=2`，不可能同时等于绝对值至多 1 的 `x_c`；
- 若 `x_2=±1`，且 `x_q in {-1,0,1}`，则
  \[
  |W|=|\pm q+2x_q|\ge q-2\ge3.
  \]

所以

\[
\boxed{\mu=2\qquad(q>=5).}
\]

最小例外 `q=3` 中，`(1,-1,1)` 已有 radius 1，因此 `mu=1`。

## 5. P025-C02 —— 精确 access delay

对每个实际存在且 `q>=5` 的族成员，

\[
\boxed{
\delta_{\rm abs}
=\nu-\mu
=\frac{q-5}{2}.
}
\]

于是

\[
\boxed{
\eta_{\min}=1,
\qquad
\mu=2,
\qquad
\nu=(q-1)/2.
}
\]

三类量完全分离。

没有任何无界/渐近结论在这里被偷偷推出；若要得到真正的无界族，还需要独立证明相应 prime family 的无穷性。

## 6. P025-T41 —— `q>=11` 时精确两点 Pareto frontier

当 `q>=11` 时，`nu>2`。

radius 2 witness `(0,1,2)` 给出

\[
\eta=|W|=2,
\]

所以 `(2,2)` 可实现。

按 `nu` 的定义，任何 radius 小于 `nu` 的 witness 都不可能达到 `eta=1`。由于 `eta` 为正整数，所有 `radius>=2, eta>=2` 的成本点都被 `(2,2)` 支配，而所有 `eta=1` 的点都被第一个 `(nu,1)` 支配。

因此

\[
\boxed{
\mathcal P
=\{(2,2),(\nu,1)\}
\qquad(q>=11).
}
\]

小例外恰好退化为：

- `q=3`：`P={(1,1)}`；
- `q=5`：`P={(2,1)}`。

## 7. 精确工作样本

- `q=5`：`1+10=11`，`eta_min=1`，`mu=nu=2`；
- `q=11`：`1+22=23`，`mu=2`，`nu=5`，`delta_abs=3`；
- `q=23`：`1+46=47`，`mu=2`，`nu=11`，`delta_abs=9`；
- `q=41`：`1+82=83`，`mu=2`，`nu=20`，`delta_abs=18`。

所有这些样本的 arithmetic floor 都恒等于 1。

## 8. Content-only geometric precision 的直接 no-go

该族每个 squarefree unit-first 成员都满足

\[
h(2q)=h(2q+1)=1,
\qquad
\eta_{\min}=1,
\]

但 `nu` 随 `q` 改变。

因此，对 absorption-floor observable 完备的 block derivative contents 并不对 access-radius observable 完备：

\[
\boxed{
\text{相同的最小 block-content 类型}
\not\Rightarrow
\text{相同的 access precision }\nu.
}
\]

甚至 perfect absorption 与 squarefree multiplicity data 同时成立，也不能保证 floor certificate 位于附近。

## 9. 与 P023 的关系

对 arithmetic-floor language，可把状态压到

\[
(h_b,h_c,g)=(1,1,1)
\]

仍然精确得到 `eta_min=1`。

但对 geometric-access language，这个压缩立即失效：至少必须保留 `(q,2)` 的 Bezout coefficient geometry，才能区分 `(q-1)/2` 的 access cost。

因此同一个 witness system 中，一个 representation 可以对某个未来查询完全精确，却对另一个未来查询严重过粗。

## 10. Prior-art 纪律

Sophie Germain primes、线性丢番图方程 `qu+2v=1`、奇偶性以及 minimum-size Bezout coefficients 都属于经典算术。P025 不主张这些对象的历史原创性。

本族只作为一个精确 pressure test，用于证明 arithmetic image content 与 geometric preimage access 是不同的 finite-precision 对象。

## 11. 可执行资产

新增：

- `src/enterprise_math/abc_absorption_sophie.py`：族条件验证、精确 `eta_min/mu/nu/access delay/Pareto frontier` 与 floor witness；
- `tests/test_abc_absorption_sophie.py`：`q=3,5` 校准、`q=11,23,29,41` 的 growing delay、floor-witness 方程与非法输入拒绝。

## 12. 下一前沿

没有 hard block。继续：

1. 求出比 block content 更丰富、但又比完整 primitive additive normal 更小的 `nu` access signature；
2. 从一个 two-prime squarefree block 推广到任意 squarefree multi-prime block；
3. 检查成熟 lattice invariant 能否压缩 minimum Bezout coefficient geometry；
4. 不在没有独立 prime-family infinitude 结果时声称无界/无穷族结论。
