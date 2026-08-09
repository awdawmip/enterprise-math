# P025 补充 06 —— Prime-Local Absorption Obstruction Spectrum

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner：`program/p025-abc-support-collapse`  
依赖：P025 补充 04–05  
Hard block：`NONE`

## 1. 从一个 gcd 拆成局部 obstruction spectrum

补充 05 已证明

\[
\eta_{\min}
=
\gcd_{\text{cross-block }p,q}
K_{p,q},
\qquad
K_{p,q}
=
\frac{R e_p e_q}{g p q},
\]

其中

\[
R=\operatorname{rad}(abc),
\qquad
e_p=v_p(abc),
\]

而 `g` 是 raw additive-relation row 的 content。

一个 gcd 只是若干互相独立的局部素数障碍的全局写法。本补充把 `eta_min` 进一步分解到这些 local coordinates。

## 2. P025-T19 —— 精确 local valuation 公式

对任意素数 `ell`，定义 cross-block pair `p,q` 的 local load：

\[
\boxed{
A_\ell(p,q)
=
v_\ell(R)
+v_\ell(e_p)
+v_\ell(e_q)
-v_\ell(g)
-\mathbf 1_{p=\ell}
-\mathbf 1_{q=\ell}.
}
\]

则每个 `A_ell(p,q)` 都是非负整数，并且

\[
\boxed{
 v_\ell(\eta_{\min})
=
\min_{\text{cross-block }p,q}
A_\ell(p,q).
}
\]

### 证明

由 P025-T15，

\[
K_{p,q}=\frac{R e_p e_q}{g p q}
\]

是正整数。对它取普通 `ell`-adic valuation，正好得到上面的 `A_ell(p,q)`。又因为 gcd 的 valuation 等于各项 valuation 的最小值，所以

\[
v_\ell(\eta_{\min})
=
\min v_\ell(K_{p,q}),
\]

即得结论。∎

## 3. P025-D03 —— Absorption obstruction spectrum

定义

\[
\boxed{
\mathcal O_{\rm abs}(a,b,c)
=
\{(\ell,v_\ell(\eta_{\min})):
 v_\ell(\eta_{\min})>0\}.
}
\]

则

\[
\boxed{
\eta_{\min}
=
\prod_{(\ell,r)\in\mathcal O_{\rm abs}}
\ell^r.
}
\]

Perfect absorption 等价于 obstruction spectrum 为空。

等价地，

\[
\boxed{
\eta_{\min}=1
\iff
\text{对每个素数 }\ell,
\text{都存在某个 cross pair }p,q\text{ 使 }A_\ell(p,q)=0.
}
\]

所以 perfect absorption 的失败在精确意义上是 local 的：存在某个素数 `ell`，它在**所有** normalized cross-support minors 中都无法被消掉。

## 4. 两种不同来源的 local obstruction

该公式把机制分成两类。

### 4.1 First-order support obstruction

若 `ell|R`，则 `v_ell(R)=1` 提供一个 support-level 单位。若某个 cross pair 本身包含 `ell`，分母 indicator 可以消掉这一单位。

但能否彻底消掉，还受 valuation exponents 与 additive-row content 影响。

### 4.2 Second-order valuation obstruction

即使

\[
\ell\nmid R,
\]

仍可能出现

\[
v_\ell(\eta_{\min})>0,
\]

因为 `ell` 可能整除 valuation integers `e_p`，并且在全部相关 cross pairs 上都强到足以穿过 `g` 的 normalization。

因此 obstruction spectrum 可能包含完全不是 `abc` 素因子的素数。

这促使 P025 暂时采用如下 diagnostic language：

\[
\boxed{
\text{first-order support }\{p:p\mid abc\}
\quad\text{与}\quad
\text{valuation exponents 的 second-order support }\{\ell:\ell\mid v_p(abc)\}.
}
\]

valuation exponents 的素因子当然是普通算术数据；P025 不主张研究 exponent patterns 本身是新数学。这里真正接受压力测试的是：这种 second-order support 恰好成为一个精确 certificate-precision obstruction coordinate。

## 5. P025-N05 —— High abc quality 不会强制 perfect absorption

前几个 high-quality examples 一度给出一个很诱人的猜想：异常/高 quality 的 abc triples 会不会自动具有 `eta_min=1`。这个猜想是错的。

### 反例 A —— support-local obstruction

\[
1+512=513.
\]

这里

\[
512=2^9,
\qquad
513=3^3\cdot19,
\qquad
R=114.
\]

精确 support formula 给出

\[
\eta_{\min}=3,
\qquad
\mathcal O_{\rm abs}=\{(3,1)\}.
\]

同时

\[
\boxed{513^4>114^5,}
\]

所以标准 abc quality 大于 `5/4`。

因此即使 rational-exponent 意义上的 high-quality event 也不会强制 perfect absorption。

### 反例 B —— obstruction prime 位于 radical support 之外

更有信息量的是

\[
1+242=243,
\]

其中

\[
242=2\cdot11^2,
\qquad
243=3^5,
\qquad
R=66.
\]

additive row content 为 `g=1`，两个 normalized cross terms 为

\[
K_{2,3}=55,
\qquad
K_{11,3}=20.
\]

所以

\[
\boxed{\eta_{\min}=5.}
\]

obstruction prime `5` 并不属于

\[
\operatorname{supp}(R)=\{2,3,11\};
\]

它来自 valuation exponent

\[
v_3(243)=5.
\]

而且

\[
\boxed{243^{10}>66^{13},}
\]

所以 quality 大于 `13/10`。

这同时否掉两个 naive reduction：

1. high abc quality 不推出 `eta_min=1`；
2. absorption obstruction 不能由 radical prime support 单独决定。

## 6. P025-T20 —— One-plus-squarefree prime-power 的 obstruction spectrum

在 P025-T17 条件下，

\[
1+b=p^m,
\]

且 `b>1` squarefree 时，

\[
\eta_{\min}=m.
\]

因此 local obstruction spectrum 恰好就是**valuation exponent** `m` 的普通素因子分解：

\[
\boxed{
\mathcal O_{\rm abs}(1,b,p^m)
=
\{(\ell,v_\ell(m)):\ell\mid m\}.
}
\]

这是最干净的 second-order support 单独出现的 family。

例如

\[
1+31=2^5
\]

满足

\[
R=62,
\qquad
\eta_{\min}=5,
\qquad
\mathcal O_{\rm abs}=\{(5,1)\},
\]

虽然 `5` 既不整除 `31`，也不整除 `2`。

## 7. 与 P018 factor precision 的关系

P018 canonical factor-precision 路线观察的是**state integer** `n` 的被测试素因子，例如

\[
D_y(n)=\{p\le y:p\text{ prime},\ p\mid n\}.
\]

这是 first-order factor-witness precision system。

本补充的 obstruction spectrum 不是同一个对象。它可能要求观察整数

\[
v_p(n)
\]

本身的素因子；这些是 multiplicity metadata，而不是 `n` 自己的 prime divisors。

因此 P025 为一种 potential higher-order factor descriptor 提供了证据，但它**不会**因此直接修改 P018，也不主张这种 hierarchy 已经应当进入 foundation。正确下一步是测试这种 higher-order support 是否在当前 Wronskian certificate language 之外仍有复用价值。

## 8. 与 P023 task-relative precision 的关系

这一差异再次完全依赖 future language。

- 若 future 只询问 radical support，exponent-prime factors 可以丢掉；
- 若询问 `eta_min`，normalized local loads 已足够；
- 若询问完整 Pareto witness frontier，local obstruction data 又不够，因为 search radius 仍依赖 witness geometry。

因此

\[
\boxed{
\text{同一个 fine integer state}
\to
\text{面对不同 certificate language 需要保留不同最小 arithmetic features}.
}
\]

这仍属于 P023 generic query-generated precision calculus 的特化。

## 9. 可执行资产

新增：

- `src/enterprise_math/abc_absorption_local.py`
  - 精确 `ell`-local load formula；
  - absorption obstruction spectrum；
  - perfect-absorption local criterion；
  - 精确 high-quality counterexample helper。
- `tests/test_abc_absorption_local.py`
  - support-local 与 exponent-only obstruction examples；
  - 精确 spectrum reconstruction；
  - high-quality counterexample regression；
  - 有界扫描恢复多个 `quality>1` / `eta_min>1` triples。

有限扫描只作为 falsification/regression 工具。

## 10. 当前结论

P025 witness 路线现在形成清晰分层：

\[
\boxed{
\text{radical support}
\to
\text{valuation structure}
\to
\text{local absorption obstruction spectrum}
\to
\eta_{\min}
\to
\text{full norm/absorption Pareto frontier}.
}
\]

前三级都是针对逐步丰富 future certificate languages 的精确算术 summary。没有任何一级能普遍替代下一级。

## 11. 下一前沿

不存在 hard block，继续：

1. 按 support-block sizes 与 valuation vectors 分类 local obstruction patterns；
2. 在任何 witness search 之前，从 exponent vector 推出 `eta_min` 的 sharp bounds；
3. 比较 obstruction spectrum 与第一次达到 absorption floor 的 Pareto radius；
4. 测试递归取“valuation exponents 的 prime support”是否真的形成有用 higher-order structure，还是只是一种冗余算术编码；
5. 用该 local spectrum 重读 Pasten lattice determinant / Geometry-of-Numbers proof，把任何已被前人包含的部分降格为 prior art；
6. 后续只在**另有独立 norm control** 时研究 small `eta_min` 的后果，避免再次把 absorption tightness 与 abc 猜想本身混为一谈。
