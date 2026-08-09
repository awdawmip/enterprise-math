# P025 补充 21 —— Compressed Block-Value Lattice 的 Determinantal Core

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-access-tail-stage18`  
依赖：P025 补充 20；此前 absorption-floor formulas  
Hard block：`NONE`

## 1. Compressed lattice 自己拥有一个精确算术核心

补充 20 把当前 norm/Wronskian witness language 降到

\[
\Lambda_{abc}
=
\{(u,v):
 u\in A\mathbb Z,
 v\in B\mathbb Z,
 u+v\in C\mathbb Z\},
\]

其中

\[
A=A(a),\qquad B=A(b),\qquad C=A(c)
\]

是三个 raw block derivative image generators；若某 block 为 unit，则对应 generator 记为 0。

Wronskian 为

\[
W(u,v)=a v-b u.
\]

下一问题纯粹是整数算术：

> `W(Lambda_abc)` 的正生成元是什么？

答案是一个三项闭式。

## 2. 提升到单个 relation row

对 non-unit blocks 写成

\[
u=A x,
\qquad
v=B y,
\qquad
u+v=C z.
\]

additive condition 变成

\[
\boxed{A x+B y-C z=0.}
\]

令

\[
\boxed{G=\gcd(A,B,C).}
\]

除掉 relation row content 后，使用 primitive row

\[
\boxed{
\alpha=\left(\frac A G,\frac B G,-\frac C G\right).
}
\]

在 `(x,y,z)` 上，Wronskian functional 为

\[
\boxed{
\beta=(-bA,aB,0).
}
\]

因为 `c=a+b`，矩阵 `[alpha;beta]` 的三个 `2x2` minors（忽略符号）正好是

\[
\boxed{
\frac{cAB}{G},
\qquad
\frac{bAC}{G},
\qquad
\frac{aBC}{G}.
}
\]

## 3. P025-T60 —— exact Wronskian image generator

primitive relation row 的标准 determinantal-divisor 恒等式给出

\[
\beta(\ker_{\mathbb Z}\alpha)
=D\mathbb Z,
\]

其中 `D` 为上述 `2x2` minors 的 gcd。因此

\[
\boxed{
D
=
\frac{\gcd(cAB,bAC,aBC)}{G}.
}
\]

等价地，

\[
\boxed{W(\Lambda_{abc})=D\mathbb Z.}
\]

这就是 additive block-value witnesses 所有可实现 arithmetic Wronskian values 的精确正生成元。

### Prior-art 边界

Determinantal-divisor 命题属于标准 integer linear algebra，补充 04 已使用。项目侧新增只是：完成 block-value quotient 后，这三个 minors 可以显式压成上述 block-ideal expressions。

## 4. P025-T61 —— compact absorption-floor formula

令

\[
M=m(a)m(b)m(c).
\]

Pasten residual divisibility 保证 `M|D`。所以

\[
\boxed{
\eta_{\min}
=
\frac{D}{M}
=
\frac{\gcd(cAB,bAC,aBC)}
{G\,m(a)m(b)m(c)}.
}
\]

因此若只关心 absorption-floor language，一旦三个 raw derivative image ideals 已知，就不再需要 full prime-coordinate rows、cross-prime minor table，甚至不必分别保留 block radicals 与 normalized contents。

当前充分算术状态缩成

\[
\boxed{(a,b,c;A,B,C)}
\]

若 relation state 仍保留实际整数，则 residual normalization 可由它们恢复。

目前不主张这是 P023 意义下的 coarsest possible state。

## 5. 恢复此前公式

### 5.1 `2+7=9`

这里

\[
(A,B,C)=(1,1,6),
\qquad G=1.
\]

三个 minor generators 为

\[
(9,42,12),
\]

gcd 为

\[
D=3.
\]

由于 `M=3`，

\[
\eta_{\min}=1.
\]

### 5.2 `5+7=12`

这里

\[
(A,B,C)=(1,1,4),
\]

minors 为

\[
(12,28,20).
\]

所以

\[
D=4,
\qquad M=2,
\qquad
\boxed{\eta_{\min}=2.}
\]

不可约 absorption overhead 在 compressed two-dimensional lattice 中已经完全可见。

### 5.3 Unit relation `1+8=9`

unit block 有 `A=0`，而

\[
(B,C)=(12,6),
\qquad G=6.
\]

只有第三个 minor 非零：

\[
\frac{aBC}{G}
=
\frac{1\cdot12\cdot6}{6}
=12.
\]

因此

\[
D=12.
\]

这正是

\[
\operatorname{lcm}(12,6),
\]

所以补充 15 的 principal-ideal intersection 是同一个 determinantal formula 的 rank-one boundary。

### 5.4 `1+242=243`

这里

\[
(A,B,C)=(0,11,405),
\qquad G=1,
\]

故

\[
D=11\cdot405=4455,
\qquad M=891,
\qquad
\boxed{\eta_{\min}=5.}
\]

不再需要 prime-pair enumeration。

## 6. P025-T62 —— non-unit compressed lattice 的 index

假设三个 blocks 都非 unit，即 `A,B,C>0`。

在 `(x,y)` 坐标中，条件

\[
A x+B y\equiv0\pmod C
\]

是映射

\[
\mathbb Z^2\to\mathbb Z/C\mathbb Z
\]

的 kernel。

`A,B` 在模 `C` 下生成的 image subgroup 大小为

\[
\frac{C}{G}.
\]

因此 kernel 在 `Z^2` 中的 index 为 `C/G`。

再从 `(x,y)` 缩放到 `(u,v)=(Ax,By)`，额外贡献 index `AB`，所以

\[
\boxed{
[\mathbb Z^2:\Lambda_{abc}]
=
\frac{ABC}{G}.
}
\]

这是紧凑的 relation-lattice density invariant；它并不决定 block access metric `K(u,v)`，因此单独不足以决定 `mu` 或 `nu`。

## 7. 与 Stage 13 的关系

补充 13 使用 block radicals `R_i`、residuals `m_i` 与 normalized derivative contents `h_i`。由于

\[
A_i=m_i h_i,
\qquad
n_i=m_iR_i,
\]

把 Stage-13 block-pair generators 乘以

\[
M=m_am_bm_c
\]

恰好得到

\[
\frac{cAB}{G},
\quad
\frac{bAC}{G},
\quad
\frac{aBC}{G}.
\]

所以补充 21 不是另一条竞争 floor theorem，而是完成 block-value quotient 后同一个 arithmetic invariant 的 compressed-lattice 形式。

## 8. 架构后果

Absorption-floor language 的信息阶梯现在缩短为

\[
\boxed{
\text{fine prime data}
\to
\text{block derivative image ideals }(A,B,C)
\to
\Lambda_{abc}
\xrightarrow{W}
D\mathbb Z
\to
\eta_{\min}.
}
\]

若未来查询还关心 geometric access，就必须继续附加三个 block access responses；若只问 arithmetic floor，则不需要它们。

这精确分开了 **image arithmetic** 与 **preimage geometry**。

## 9. 可执行资产

新增：

- `src/enterprise_math/abc_block_value_lattice.py`
  - block image generators；
  - relation content `G`；
  - 三个 compressed Wronskian minors；
  - exact Wronskian image generator；
  - exact absorption floor；
  - non-unit lattice index。
- `tests/test_abc_block_value_lattice.py`
  - prime、prime-power、unit 与 irreducible-overhead examples；
  - bounded primitive triples 与此前 block formula 的一致性。

## 10. 下一前沿

没有 hard block。继续：

1. 给 `Lambda_abc` 推导方便的 explicit basis / HNF normal form；
2. 把该 basis 与 block capacity frontiers 组合，绕过 prime-coordinate enumeration 攻击 `mu` 与 `nu`；
3. 判断选定 Wronskian-threshold language 下哪些 lattice invariants 还能继续 quotient；
4. 把 determinantal compression 推广到多个 simultaneous linear certificate observables；
5. 把更短的 floor formula Relay 给 P023/P018，作为 worked exact-image compression，而不是新的 generic theorem。
