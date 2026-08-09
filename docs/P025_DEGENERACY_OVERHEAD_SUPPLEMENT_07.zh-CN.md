# P025 补充 07 —— Additive Radius 与 Non-Degenerate Witness Radius

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner：`program/p025-degeneracy-overhead`  
父依赖：`program/p025-witness-precision-bracket@44f260d7`  
前人工作状态：有限整数格 minima 属于既有数学；P025 只把它作为 task-state 压力测试

## 1. 目标

补充 06 已经把精确 non-degenerate witness precision `mu` 夹在 arithmetic demand floor `lambda_abc` 与 sparse generator ceiling `U_2` 之间。

还剩一个自然的简化猜测：

> 也许 arithmetic demand 以上的全部成本，都已经由 additive relation lattice `T=ker_Z(alpha)` 自身解释；只要知道 additive lattice 的 shortest radius，就可以删掉 degeneracy sublattice `T^circ`。

本补充给出精确反例。答案是否定的。

## 2. Additive-lattice radius

定义

\[
\boxed{
\rho(a,b,c)
=
\min\{\|x\|_\infty:x\in T,\ x\ne0\}.
}
\]

non-degenerate witness set 只是 nonzero additive lattice 的子集：

\[
T\setminus T^\circ
\subseteq
T\setminus\{0\}.
\]

所以按定义

\[
\boxed{\rho\le\mu.}
\]

结合补充 06：

\[
\boxed{
\max(\lambda_{abc},\rho)
\le
\mu
\le
U_2.
}
\]

定义 **non-degeneracy overhead**

\[
\boxed{
\eta_{nd}
=
\mu-\max(\lambda_{abc},\rho)
\ge0.
}
\]

若 `eta_nd>0`，则 arithmetic demand 与第一个 nonzero additive-lattice state 都不足以回答未来问题“当前 radius 是否已经存在 non-degenerate certificate？”。

## 3. P025-N04 —— `1+53=54` 的精确 non-degeneracy barrier

考虑

\[
1+53=54.
\]

prime-labelled coordinates 为

\[
(2,3,53).
\]

对 relation-adapted arithmetic derivative，primitive additive normal 是

\[
\boxed{
\alpha=(27,54,-1).
}
\]

因为

\[
d^\psi(54)=27x_2+54x_3,
\qquad
 d^\psi(53)=x_{53},
\]

而 relation additivity 给出

\[
\boxed{x_{53}=27x_2+54x_3=27(x_2+2x_3).}
\]

对补 pair `(1,53)`，Wronskian 就是 `d^psi(53)`，所以 primitive degeneracy normal 可以取

\[
\boxed{
\beta=(0,0,1).
}
\]

于是 non-degeneracy 恰好等价于

\[
x_{53}\ne0.
\]

### Additive radius

向量

\[
(-2,1,0)
\]

属于 `T`，故 `rho<=2`。

radius 1 内不存在 nonzero additive vector。若全部坐标都在 `{-1,0,1}`，由

\[
x_{53}=27(x_2+2x_3)
\]

及 `|x_53|<=1`，必须有 `x_2+2x_3=0`；而在 `{-1,0,1}` 内只能得到 `x_2=x_3=0`，进而 `x_53=0`。

因此

\[
\boxed{\rho=2.}
\]

### Non-degenerate witness radius

若 witness 非退化，则 `x_53` 是 27 的非零倍数。所以

\[
\|x\|_\infty\ge |x_{53}|\ge27.
\]

显式向量

\[
(1,0,27)
\]

满足 additive relation 且非退化，因此

\[
\boxed{\mu=27.}
\]

### Arithmetic demand floor 与 sparse upper certificate

这里

\[
m(54)=9,
\]

而 target `54` 的补 pair `(1,53)` 的 normalized complementary capacity 是

\[
K_{1,53}=1.
\]

因此

\[
\lambda_{54}=9,
\]

其它 orientation 均不超过它，所以

\[
\boxed{\lambda_{abc}=9.}
\]

与 `53` coordinate 相关的 nonzero generator minor 给出的 cheapest sparse witness cost 为

\[
\boxed{U_2=27.}
\]

所以完整精确 profile 是

\[
\boxed{
\lambda_{abc}=9,
\qquad
\rho=2,
\qquad
\mu=27,
\qquad
U_2=27.
}
\]

从而

\[
\boxed{\eta_{nd}=27-9=18.}
\]

这是一个严格有限反例：即使已经知道 arithmetic demand 与 additive-lattice shortest radius，也不能把完整 flag `T^circ subset T` 删除掉。

## 4. 第二个独立 barrier：`1+36=37`

在 coordinates `(2,3,37)` 上，

\[
\alpha=(36,24,-1),
\qquad
\beta=(3,2,0).
\]

additive equation 为

\[
x_{37}=36x_2+24x_3=12(3x_2+2x_3).
\]

最短 additive vector 是

\[
(-2,3,0),
\]

因此

\[
\rho=3.
\]

但该向量退化，因为 `3(-2)+2(3)=0`。non-degeneracy 要求 `3x_2+2x_3\ne0`，于是 `x_37` 必为 12 的非零倍数，给出

\[
\mu\ge12.
\]

向量 `(1,-1,12)` 取到该下界，所以

\[
\mu=12.
\]

补充 06 又给出

\[
\lambda_{abc}=6,
\qquad
U_2=24.
\]

因此

\[
\boxed{
(\lambda_{abc},\rho,\mu,U_2)=(6,3,12,24),
\qquad
\eta_{nd}=6.
}
\]

这个样本与 `1+53=54` 的结构不同：degeneracy row 位于 `(2,3)` coordinates，而不是单独落在 complementary prime coordinate 上。因此独立 barrier 不是某一种 support placement 的偶然结果。

## 5. 架构后果 —— 三种不同 future question

这些精确样本把三种未来语言严格分开：

1. **Arithmetic demand：** 仅为了承载 multiplicity load，certificate 至少要多大？由 `lambda_abc` 回答。
2. **Additive feasibility：** relation lattice `T` 在多大 radius 第一次出现任意 nonzero state？由 `rho` 回答。
3. **Non-degenerate certification：** state 在多大 radius 才真正逃出 `T^circ` 并产生可用 Wronskian certificate？由 `mu` 回答。

通用蕴含只有

\[
\lambda_{abc}\le\mu,
\qquad
\rho\le\mu.
\]

一般不存在

\[
\mu=\max(\lambda_{abc},\rho)
\]

这样的等式原则。

所以完整 witness flag 保存的 degeneracy/Pluecker information，对于 certificate language 并不是冗余信息。

这直接强化此前的架构分离：

\[
\boxed{
\text{relation lattice state}
\ne
\text{non-degenerate certificate state}.
}
\]

它正是 P023 所要求的 future-language distinction：对“有没有任意 additive state？”安全的 erasure，对“有没有可用 certificate？”可能不安全。

## 6. 这没有证明什么

这些样本没有证明 `eta_nd` 在 abc-exceptional triples 上渐近变大，也没有证明它在全部 primitive triples 上无界。

它们只严格建立必要的结构边界：

\[
\boxed{\eta_{nd}\text{ 在精确有限状态上可以严格为正且数量级不可忽略}.}
\]

任何关于 `eta_nd` 分布或增长的渐近陈述，都需要另行证明。

## 7. 可执行资产

本 generation 新增：

- `src/enterprise_math/witness_precision_layers.py`；
- `tests/test_witness_precision_layers.py`。

可执行层计算有界 exact additive radius `rho`，并把它和 `lambda_abc`、`mu`、`U_2` 放入同一个 layer profile，同时锁定上面两个显式 degeneracy-barrier 样本。

有限枚举只承担这些已声明有界样本的 oracle；第 3--4 节中的精确数值已经由整数 relation equation 直接证明。

## 8. Ownership / 前人工作边界

整数格最短向量、nested sublattices 与 relative minima 都属于既有数学。P025 不把这些一般对象作为新发明。

项目侧价值是一个精确 pressure-test 结论：当前 P025 generator flag 确实承担了未来语言义务，不能因为 additive kernel 与 arithmetic demand 已经知道，就删掉它的 degeneracy component。

因此它仍是 P025 specialization / Foundation-boundary witness，而不是新的 generic lattice-theory mother theorem。

## 9. 下一前沿

剩余高价值问题进一步收窄为：

1. 在不夸大创新性的前提下，把 `mu` 精确表达为 flag / quotient `T/T^circ` 的 relative minimum；
2. 找出仅从 generator signature 就能保证 `eta_nd=0` 的条件；
3. 检查 `eta_nd>0` 是否与补充 05 的 proof-loss shells 有关联；
4. 专门在 high-quality triples 中寻找“witness-pressure floor 的增强主要来自 non-degeneracy，而不是 arithmetic demand”的样本；
5. 把这些精确反例路由到 Foundation FQ-004，作为 relation layer 与 certificate layer 必须分离的证据。
