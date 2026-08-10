# P025 补充 84 —— 指数整除偏序上的精确 Projective-Pressure 继承

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-cyclotomic-stage76`  
依赖：P025 补充 82–83  
硬阻断：`NONE`

## 1. Composite-exponent pressure 本质上是 transport 问题

Stage 83 证明 composite exponent 可以从 proper cyclotomic divisor layers 继承 projective pressure。四次幂与九次幂反例进一步提示：这不只是定性上的“继承”。

沿 exponent divisibility 存在一个精确的乘法 transport law。

## 2. Same-sign divisibility

设

\[
2\le m<n,
\qquad
m\mid n,
\qquad
k:=\frac nm.
\]

对 difference sign，任意 `k` 都有

\[
p^m-q^m\mid p^n-q^n.
\]

对 sum sign，在本补充讨论的 same-sign route 中，当 `k` 为奇数时有

\[
p^m+q^m\mid p^n+q^n.
\]

记

\[
A_m:=p^m\pm q^m,
\qquad
A_n:=p^n\pm q^n,
\]

并定义

\[
\boxed{Q_{m\to n}:=\frac{A_n}{A_m}.}
\]

在 cyclotomic-index 层面，low index set 包含于 high index set，而 `Q` 正是新增 layers 的乘积。

## 3. P025-D28 —— inheritance overlap 与 multiplier

定义 support-overlap factor

\[
\boxed{
\Gamma_{m\to n}
:=
\frac{\operatorname{rad}(A_m)\operatorname{rad}(Q_{m\to n})}
{\operatorname{rad}(A_n)}.
}
\]

它是整数，并且正是 inherited active component 与新 quotient 两块之间的 overlap correction。

定义 pressure inheritance multiplier

\[
\boxed{
\Lambda_{m\to n}
:=
\frac{\Gamma_{m\to n}\,m(Q_{m\to n})}{k}.
}
\]

分子有两个完全不同的来源：

1. quotient 内的新 multiplicity `m(Q)`；
2. old component 与 quotient 之间复用 support 的 `Gamma`。

分母 `k=n/m` 则是指数提升带来的 projective normalization cost。

## 4. P025-T174 —— exact projective-pressure inheritance law

两块 residual 恒等式给出

\[
\boxed{m(A_n)=\Gamma_{m\to n}\,m(A_m)m(Q_{m\to n}).}
\]

对应 equal-exponent projective ratios 为

\[
\rho_{m,\pm}=\frac{m(A_m)}{m(p+q)},
\]

和

\[
\rho_{n,\pm}=\frac{m(A_n)}{n(p+q)}.
\]

代入 residual identity 与 `n=km` 得到

\[
\boxed{\rho_{n,\pm}=\rho_{m,\pm}\Lambda_{m\to n}.}
\]

等价地，

\[
\boxed{
\frac{\rho_{n,\pm}}{\rho_{m,\pm}}
=
\frac{\Gamma_{m\to n}m(Q_{m\to n})}{n/m}.
}
\]

这是 exact formula，不含 asymptotic estimate，也不依赖近似 coprimality。

## 5. P025-D29 —— 三种 transport classes

multiplier 给出自然三分：

\[
\boxed{
\Lambda<1:\ \text{attenuated},
\qquad
\Lambda=1:\ \text{resonant},
\qquad
\Lambda>1:\ \text{amplified}.
}
\]

因此 composite exponent 可以：

- 压低 lower hard state；
- 精确保留它；
- 放大 lower state，甚至把一个 subunit state 推过 activation threshold。

这远比“proper divisors 会有影响”更强。

## 6. P025-C26 —— 四次幂反例是 exact resonant square lift

对

\[
(q,p)=(23,41),
\]

比较指数

\[
2\to4.
\]

quotient 为

\[
Q_{2\to4}=p^2+q^2=\Phi_4(p,q),
\]

在该例中完全 squarefree，所以

\[
m(Q)=1.
\]

inherited square-difference component 与 quotient 只共享素数 2，因此

\[
\Gamma_{2\to4}=2.
\]

又有

\[
k=2,
\]

所以

\[
\boxed{\Lambda_{2\to4}=1.}
\]

从而

\[
\boxed{
\rho_{4,-}(41,23)=\rho_{2,-}(41,23)=\frac32.
}
\]

Stage 82 的 squarefree-top fourth-power activation 不是新生成的 pressure，而是 prime-square centered hard state 的 exact resonant lift。

## 7. P025-C27 —— 九次幂反例是 resonant cube lift

### Difference

对

\[
(q,p)=(23,71),
\]

比较

\[
3\to9.
\]

新增 quotient 即 top `Phi_9`，它 squarefree，所以 `m(Q)=1`；同时与 inherited cube component 共享素数 3，故

\[
\Gamma_{3\to9}=3.
\]

又 `k=3`，因此

\[
\Lambda=1
\]

且

\[
\boxed{\rho_{9,-}=\rho_{3,-}=\frac{1372}{47}.}
\]

### Sum

对

\[
(q,p)=(11,13),
\]

`3->9` sum quotient `Phi_18` 同样 squarefree，并只通过 exponent prime 3 与 inherited component 重叠。再次有

\[
\Gamma=3,
\qquad
k=3,
\qquad
\Lambda=1,
\]

因此

\[
\boxed{\rho_{9,+}=\rho_{3,+}=\frac76.}
\]

这些都是 exact resonant lifts。

## 8. P025-T175 —— attenuation、resonance、amplification 三态全部真实存在

同一条

\[
3\to9
\]

route 已经实现全部三类 transport。

### Attenuation

对

\[
(q,p)=(5,59)
\]

的 sum branch，quotient squarefree 且与 inherited component 没有 support overlap：

\[
\Gamma=1,
\qquad
m(Q)=1.
\]

因此

\[
\Lambda=\frac13.
\]

activated cube state

\[
\rho_{3,+}=\frac{13}{6}>1
\]

下降为

\[
\boxed{\rho_{9,+}=\frac{13}{18}<1.}
\]

### Resonance

对 `(q,p)=(11,13)`，

\[
\boxed{\Lambda=1.}
\]

### Amplification

对

\[
(q,p)=(7,29),
\]

new quotient residual 为

\[
m(Q)=19
\]

且 overlap 为

\[
\Gamma=3.
\]

所以

\[
\Lambda=19.
\]

subunit cube state

\[
\rho_{3,+}=\frac16
\]

被放大为

\[
\boxed{\rho_{9,+}=\frac{19}{6}>1.}
\]

因此 high-exponent activation 可以被继承、被消灭，也可以由 quotient transport 新生成。

## 9. P025-T176 —— inheritance multipliers 构成 multiplicative cocycle

考虑 admissible same-sign chain

\[
m\mid n\mid r.
\]

两次应用 P025-T174，

\[
\rho_r
=\rho_n\Lambda_{n\to r}
=\rho_m\Lambda_{m\to n}\Lambda_{n\to r}.
\]

而直接 transport 给出

\[
\rho_r=\rho_m\Lambda_{m\to r}.
\]

由于 projective ratios 均为正，得到

\[
\boxed{
\Lambda_{m\to r}
=
\Lambda_{m\to n}\Lambda_{n\to r}.
}
\]

所以 `Lambda` 是 admissible exponent-divisibility poset 上的 multiplicative pressure cocycle。

取对数后，transport 变为 additive pressure increments。

## 10. Primitive 与 inherited hard states

Stage 84 提示一个更精确的研究分类。

exponent `n` 上的 hard state 不应自动被当作新的 arithmetic complexity。第一步应该先问：是否存在 proper admissible divisor `m|n`，其

\[
\rho_m
\]

已经包含显著 pressure，并且 `Lambda_{m->n}` 保持或放大它。

于是可以区分：

1. **inherited pressure** —— proper exponent 已存在；
2. **quotient-generated pressure** —— 由新 layers 的 `m(Q)` 或 overlap 产生；
3. **primitive exponent pressure** —— 不能由任何 proper-divisor transport 解释。

第三类才是真正新的 exponent-level frontier。

## 11. 架构含义

Exponent 不再只是 scalar shell label；它是 divisibility poset 上的节点，并承载一个 multiplicative transport cocycle。

因此 composite exponent 的 future-safe precision state 至少应包含：

\[
\boxed{
\text{ancestor pressure}
+
\text{new quotient residual}
+
\text{support overlap}
-
\text{exponent normalization cost}.
}
\]

这给出一个具体例子：一个 scale 上的 state 并不独立于 lower-scale history。正确 abstraction 是 refinement/divisibility structure 上的 transport，而不是彼此无关的 flat exponent shells。

## 12. Prior-art / novelty 边界

`x^m±y^m` 的 divisibility、radical identities 与 quotient factorizations 都是经典数学。

P025 不单独主张这些组成部分的新颖性。

项目侧候选是 exact projective-pressure multiplier、其 attenuation/resonance/amplification 分类，以及 exponent divisibility 上的 cocycle interpretation。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 13. 可执行资产

新增：

- `src/enterprise_math/abc_exponent_pressure_inheritance.py`；
- `tests/test_abc_exponent_pressure_inheritance.py`。

executable layer 验证 exact ratio transport、cyclotomic index inclusion、三种 transport class、Stage 82/83 resonant counterexamples，以及 exponent chain 上的 cocycle law。

## 14. 下一前沿

不存在硬阻断。继续：

1. 不把“primitive pressure”定义成含糊的 node residual，而是寻找 cover-edge 最小 transport state；
2. 判断 maximal ancestor pressure 是否只需一个小 antichain 而非全部 divisors；
3. 检验 logarithmic cocycle 是否在 exponent lattice 上形成可 telescope 的 minimal path；
4. 用 primitive/inherited split 避免未来 exceptional-set argument 重复计数 lifted hard states；
5. minimal-state theorem 证明后再把 cocycle/transport abstraction Relay 给 A2/P023。
