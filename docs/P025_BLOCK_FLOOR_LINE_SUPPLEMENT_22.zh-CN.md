# P025 补充 22 —— Arbitrary-Support Absorption Access 的一维 Floor Line

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-access-tail-stage18`  
依赖：P025 补充 20–21 与补充 16–18 的 finite block access  
Hard block：`NONE`

## 1. `eta_min` 是二维问题，但 floor access 只剩一维

补充 20 把 fine additive witness family 压成

\[
\Lambda_{abc}
=
\{(u,v):u\in A\mathbb Z,\ v\in B\mathbb Z,\ u+v\in C\mathbb Z\}
\subseteq\mathbb Z^2.
\]

补充 21 证明 Wronskian image 为

\[
W(\Lambda_{abc})=D\mathbb Z,
\qquad
W(u,v)=av-bu.
\]

Absorption floor 恰好在

\[
\boxed{
\mathcal F_D
=
\{(u,v)\in\Lambda_{abc}:W(u,v)=\pm D\}
}
\]

上取得。

当三个 blocks 都非 unit 时，`Lambda_abc` rank 为 2，而 `W=D` 再施加一个独立整数线性条件，所以每个符号的 floor set 都是 affine rank-one lattice。

因此，一旦 block access responses 已知，任意 support 的 `nu` 都降为一个整数参数。

## 2. P025-T63 —— `Lambda_abc` 的显式 HNF-like basis

假设 `A,B,C>0`，令

\[
G=\gcd(A,B,C),
\qquad d=\gcd(A,C).
\]

取

\[
\boxed{y_0=d/G.}
\]

因为

\[
\gcd(A/d,C/d)=1,
\]

存在唯一 residue

\[
0\le x_0<C/d
\]

满足

\[
\boxed{
\frac Ad x_0
\equiv
-\frac BG
\pmod{C/d}.
}
\]

则

\[
\boxed{g_1=(AC/d,0),\qquad g_2=(Ax_0,Bd/G)}
\]

构成 `Lambda_abc` 的 basis。

### 证明

两向量按构造都满足 `u in AZ`、`v in BZ`、`u+v in CZ`。其 determinant 为

\[
|\det(g_1,g_2)|
=
\frac{AC}{d}\frac{Bd}{G}
=
\frac{ABC}{G},
\]

正好等于补充 21 已证明的 lattice index。因此这两个已在 lattice 内的向量生成整个 `Lambda_abc`。∎

限定 `x_0` 的 residue 范围后，它是相对当前坐标顺序的 HNF-like 规范 basis。

## 3. P025-T64 —— 显式 affine floor line

令

\[
w_i=W(g_i).
\]

补充 21 保证

\[
\gcd(w_1,w_2)=D.
\]

取 Bezout coefficients `r,s` 满足

\[
rw_1+sw_2=D.
\]

定义

\[
\boxed{p_0=r g_1+s g_2.}
\]

则

\[
W(p_0)=D.
\]

再定义

\[
\boxed{
h
=
\frac{w_2}{D}g_1
-
\frac{w_1}{D}g_2.}
\]

因为 `gcd(w_1/D,w_2/D)=1`，`h` 是 `W` 在 `Lambda_abc` 内 kernel 的 primitive lattice direction。

因此

\[
\boxed{
\{(u,v)\in\Lambda_{abc}:W(u,v)=D\}
=
p_0+\mathbb Z h.
}
\]

`W=-D` 的直线就是其相反数；block access 对符号对称，所以 access cost 相同。

## 4. P025-T65 —— arbitrary-support `nu` 是一参数优化

记

\[
K(u,v)
=
\max\bigl(
\kappa_a(u),
\kappa_b(v),
\kappa_c(u+v)
\bigr).
\]

那么

\[
\boxed{
\nu
=
\min_{k\in\mathbb Z}
K(p_0+k h).
}
\]

完全不需要限制总 prime-coordinate 数量。所有 block 内高维几何已经被三条 exact access functions 编译掉。

这严格推广了补充 09 的 affine-line solver：补充 09 要求整个 fine witness ambient space 只有三个 prime coordinates，而这里对任意 support 都成立。

## 5. P025-T66 —— 一维搜索具有 exact finite bound

令

\[
R_0=K(p_0)
\]

为构造出的 Bezout floor point 成本。

对一个 block `n`，设其 raw derivative coefficient row 为 `(c_{n,p})`。任意半径不超过 `R_0` 的 prime-coordinate vector 都满足

\[
|d_x(n)|
\le
R_0\sum_{p\mid n}|c_{n,p}|.
\]

因此任何能改进或持平 `R_0` 的 floor point 必须满足

\[
\begin{aligned}
|u_0+k h_u|&\le R_0 S_a,\\
|v_0+k h_v|&\le R_0 S_b,\\
|u_0+v_0+k(h_u+h_v)|&\le R_0 S_c,
\end{aligned}
\]

其中

\[
S_n=\sum_{p\mid n}\frac{n v_p(n)}p,
\]

unit block 取 `S_1=0`。

每个不等式都是关于 `k` 的精确整数区间。在 rank-two 情形，因为 Wronskian-kernel direction 非零，三者交集有限。

因此 exact algorithm 为：

1. 构造 `p_0` 与 `h`；
2. 计算 `R_0`；
3. 交三个 integer parameter intervals；
4. 只在这个有限区间内计算 `K`；
5. 取最小值。

枚举的是 floor-line parameter，不是 prime-coordinate witness cube。

## 6. Rank-one unit boundary

若 `a=1`，则 `u=0`，并且

\[
v\in B\mathbb Z\cap C\mathbb Z
=\operatorname{lcm}(B,C)\mathbb Z.
\]

正 floor point 唯一为

\[
\boxed{(u,v)=(0,D)}
\]

且

\[
D=\operatorname{lcm}(B,C).
\]

若 `b=1` 同理，floor point 位于 `u` 轴并只差整体符号。

因此补充 15 的 unit-relation blockwise access 正是本构造的 rank-one boundary。

## 7. Exact examples

### `2+3=5`

basis 为

\[
((1,0),(0,1)),
\]

Wronskian values 为 `(-3,2)`，所以 `D=1`。一个 Bezout floor point 是 `(1,2)`，kernel direction 为 `(2,3)`。

exact floor-line optimization 在同一条线上找到更低成本代表，例如 `(-1,-1)`，最终

\[
\boxed{\nu=2.}
\]

### `2+7=9`

这里

\[
(A,B,C)=(1,1,6),
\]

HNF-like basis 为

\[
\boxed{((6,0),(5,1)).}
\]

basis Wronskians 为 `(-42,-33)`，gcd 为 `D=3`。正 floor point 可取

\[
(1,5),
\]

kernel direction 为

\[
(4,14).
\]

exact solver 得到

\[
\boxed{\nu=5,}
\]

与此前 fine-lattice 结果一致。

### `5+7=12`

basis 为

\[
((4,0),(3,1)),
\]

`D=4`，floor point `(-2,-2)`，kernel direction `(5,7)`。exact result 为

\[
\boxed{\eta_{\min}=2,\qquad\nu=2.}
\]

### `25+704=729`

该样本在 fine level 横跨四个 prime coordinates。Compressed exact solver 找到

\[
\boxed{(t_a,t_b,t_c)=(-20,8768,8748),}
\]

并得到

\[
\boxed{\eta_{\min}=6,\qquad\nu=6.}
\]

搜索只发生在一维 block-value floor line，而不是四维 prime-coordinate cube。

## 8. 架构后果

Arbitrary-support floor-access chain 现在变成

\[
\boxed{
\text{fine prime witness}
\to
\text{三条 block access functions}
+
\Lambda_{abc}
\to
\text{一条 affine floor line}
\to
\nu.
}
\]

两类复杂度被精确分开：

- block 内 preimage geometry，被编译成 `kappa_n`；
- block 之间 relation geometry，被压成一条一维 floor line。

这比“存在一个足够短的 witness”更强：它给出 minimum floor-access precision 的 exact finite search domain。

## 9. Prior-art 边界

HNF-style lattice basis、linear Diophantine level set 的 Bezout parameterization 与 affine-lattice 一参数优化都属于标准数学。

P025 不对这些 generic tools 作创新主张。项目侧继续检验的是：通过此前 block-value quotient 与 finite block access responses，把 arbitrary-support arithmetic-derivative floor access 精确降到这一结构。

该 integrated interface 的历史创新状态仍为 `NOVELTY_UNVERIFIED`。

## 10. 可执行资产

新增：

- `src/enterprise_math/abc_block_floor_line.py`
  - HNF-like compressed-lattice basis；
  - Wronskian Bezout floor point；
  - primitive floor-line direction；
  - exact finite parameter bound；
  - arbitrary-support exact `nu` solver。
- `tests/test_abc_block_floor_line.py`
  - `2+3=5`、`2+7=9`、`5+7=12` line data；
  - rank-one unit relations；
  - `1+242=243`、`1+512=513` access；
  - four-coordinate `25+704=729`；
  - 更多 small exact values。

## 11. 下一前沿

没有 hard block。继续：

1. 攻击仍在完整二维 compressed lattice 上最小化的 `mu`；
2. 用 finite block capacity frontiers 推导 `K(u,v)` 的 exact/bounded sublevel sets；
3. 判断 Wronskian-threshold queries 是否也有类似 Stage 18 的 finite two-dimensional antichain boundaries；
4. 将 exact floor-line algorithm 与 Pasten Geometry-of-Numbers sufficient norm bounds 比较；
5. 把 block-value quotient 推广到多个 simultaneous linear certificate forms。
