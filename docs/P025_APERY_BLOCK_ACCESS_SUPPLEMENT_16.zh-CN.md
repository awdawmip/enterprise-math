# P025 补充 16 —— 高维 Block Access 的 Apéry 缺陷半群

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner：`program/p025-abc-support-collapse`  
依赖：P025 补充 13–15  
Hard block：`NONE`

## 1. 下一层对象不是另造一个 ABC 专用格

补充 15 抽出了 block access 函数

\[
\kappa_n(T)
=
\min\left\{
\|x\|_\infty:
\sum_{p\mid n}\frac{n v_p(n)}p x_p=T
\right\}.
\]

同一个问题可以对任意正整数系数行提出。把行 gcd 除掉，记 primitive row 为

\[
\boxed{b=(b_1,\ldots,b_d),\qquad \gcd(b_1,\ldots,b_d)=1.}
\]

对 `N>=0` 定义

\[
\boxed{
\kappa_b(N)
=
\min\{\|x\|_\infty:x\in\mathbb Z^d,\ b\cdot x=N\}.
}
\]

并令

\[
\boxed{P=b_1+\cdots+b_d.}
\]

补充 10–11 的二变量 modular solver 只是这个问题的一种特化。本补充去掉维数限制。

## 2. P025-T46 —— signed access 到非负 defect 的精确变换

固定候选半径 `r>=0`。下述条件

\[
\boxed{
\exists x\in\mathbb Z^d:
\|x\|_\infty\le r,
\ b\cdot x=N
}
\]

当且仅当存在

\[
y\in\mathbb N^d
\]

使

\[
\boxed{
 b\cdot y=rP-N,
\qquad
0\le y_i\le2r.
}
\]

### 证明

由 `x` 定义

\[
\boxed{y_i=r-x_i.}
\]

因 `-r<=x_i<=r`，所以 `0<=y_i<=2r`。同时

\[
b\cdot y
=
\sum_i b_i(r-x_i)
=rP-b\cdot x
=rP-N.
\]

反过来，从这样的非负 `y` 定义

\[
x_i=r-y_i.
\]

则 `-r<=x_i<=r`，同一恒等式反向给出 `b·x=N`。∎

### 推论

signed minimum-preimage 问题由数值半群

\[
\boxed{
S_b=\langle b_1,\ldots,b_d\rangle
\subseteq\mathbb N_0
}
\]

控制。

半径 `r` 下的 defect 是

\[
\boxed{\delta=rP-N.}
\]

除了 `delta in S_b` 以外，只多一个条件：所选 `delta` 的非负分解必须装进坐标上界 `2r`。

## 3. P025-D07 —— Apéry access profile

因为 `P=sum b_i` 本身属于 `S_b`，定义

\[
\operatorname{Ap}(S_b;P)
=
\{a_0,\ldots,a_{P-1}\},
\]

其中

\[
\boxed{
a_j
=
\min\{s\in S_b:s\equiv j\pmod P\}.
}
\]

对每个 Apéry 元素定义其最小非负 `L_infinity` 分解半径

\[
\boxed{
L_j
=
\min\left\{
\|y\|_\infty:
 y\in\mathbb N^d,
\ b\cdot y=a_j
\right\}.
}
\]

有限数据

\[
\boxed{
\Sigma_{\rm Ap}(b)
=
\bigl(P,(a_j,L_j)_{j=0}^{P-1}\bigr)
}
\]

称为 **Apéry access profile**。

## 4. P025-T47 —— 每个剩余类的精确第一稳定目标

固定 `N>=0`，令

\[
j\equiv-N\pmod P.
\]

任何实现 `N` 的半径 `r` 都有

\[
\delta=rP-N\equiv j\pmod P.
\]

由 Apéry 元素定义，

\[
\delta\ge a_j.
\]

因此所有 access radius 都满足

\[
\boxed{
 r
\ge
 r_0(N)
:=
\frac{N+a_j}{P}.
}
\]

这个下界何时恰好可达？答案完全精确：

\[
\boxed{
\kappa_b(N)=r_0(N)
\iff
L_j\le2r_0(N).
}
\]

### 证明

若 `r<r_0`，则

\[
rP-N<a_j
\]

但仍和 `a_j` 属于同一剩余类，所以该 defect 不可能属于 `S_b`。因此 `r_0` 是绝对下界。

在 `r=r_0` 时，defect 正好等于 `a_j`。由 P025-T46，该半径可行当且仅当 `a_j` 存在每个坐标都不超过 `2r_0` 的非负分解，即 `L_j<=2r_0`。∎

令

\[
q_j=\left\lceil\frac{L_j}{2}\right\rceil.
\]

那么在目标剩余类 `N congruent -j mod P` 内，Apéry 闭式精确成立当且仅当

\[
\boxed{
N\ge Pq_j-a_j.
}
\]

所以该剩余类的**第一稳定目标**是满足

\[
\boxed{
N_j^*\equiv-j\pmod P,
\qquad
N_j^*\ge Pq_j-a_j
}
\]

的最小非负整数。

这不是一个粗充分界，而是精确起点。

## 5. P025-T48 —— 最终仿射周期 access law

对任意

\[
N\equiv-j\pmod P,
\qquad
N\ge N_j^*,
\]

都有

\[
\boxed{
\kappa_b(N)
=
\frac{N+a_j}{P}.
}
\]

因此

\[
\boxed{
\kappa_b(N+P)=\kappa_b(N)+1
}
\]

在该剩余类进入稳定尾部以后精确成立。

### 证明

一旦 `N>=N_j^*`，P025-T47 的 Apéry 下界已经可行，因此就是最优值。把 `N` 增加 `P` 不改变 defect 剩余类和 Apéry 元素，只会让 `(N+a_j)/P` 增加一；坐标容量条件也只会更宽松。∎

因此 access response 具有一个有限非规则 preperiod，随后进入周期为 `P` 的精确仿射规律。

## 6. P025-T49 —— 完整异常目标集合有限且可精确列出

对目标剩余类

\[
\rho=(-j)\bmod P,
\]

稳定尾部之前的目标恰好是

\[
\boxed{
\rho,
\rho+P,
\rho+2P,
\ldots,
<N_j^*.
}
\]

对全部 `j` 取并，得到有限集合

\[
\boxed{\mathcal E_b}
\]

满足

\[
N\notin\mathcal E_b
\Longrightarrow
\kappa_b(N)
=
\frac{N+a_{-N}}P.
\]

而每个 `N in E_b` 都是真正的 Apéry 闭式失败点，因为此时最小 defect `a_j` 尚无法装入当前 `2r_0` 的坐标容量。

所以 preperiod 不只是“存在一个有限上界”，而是可以由有限 profile `Sigma_Ap` 精确枚举。

## 7. 示例：`(5,2)` 与旧的粗稳定界

取

\[
b=(5,2),
\qquad
P=7.
\]

按 defect 剩余类排列的 Apéry 元素为

\[
\boxed{
(a_0,\ldots,a_6)
=(0,8,2,10,4,5,6).
}
\]

对应的最小非负 `L_infinity` 分解半径为

\[
\boxed{
(L_0,\ldots,L_6)
=(0,4,1,2,2,1,3).
}
\]

精确异常目标集合竟然只有

\[
\boxed{\mathcal E_{(5,2)}=\{1\}.}
\]

确实有

\[
\kappa(1)=2,
\qquad
\kappa(2)=1,
\]

所以 access 在局部并不单调；但除了这一个异常目标以外，Apéry 仿射公式已经全部精确。

这显著强于 `abc_access_response.py` 中较早为了工程安全使用的 `N>=max(A,B)^2` 充分区域。旧界仍然正确，但已经不是最好的结构描述。

## 8. 示例：`1+242=243` 的 block

补充 15 的非平凡 block 方程化为

\[
11x_2+4x_{11}=405.
\]

因此

\[
b=(11,4),
\qquad
P=15,
\qquad
N=405\equiv0\pmod{15}.
\]

零剩余类中

\[
a_0=0,
\qquad
L_0=0.
\]

所以稳定公式立即给出

\[
\boxed{
\kappa_{(11,4)}(405)
=
405/15
=27.
}
\]

无需再解一次二变量 Bezout 最优化。

## 9. 示例：真正三坐标 block

对 primitive 三坐标行

\[
\boxed{b=(15,10,6),\qquad P=31,}
\]

当前提交的 reference regression 中，在 `70` 以下只有三个异常非负目标：

\[
\boxed{3,7,13.}
\]

其余被测试目标都已经落在自己的精确 Apéry 仿射分支上。可执行测试用独立 finite exact oracle 与 profile 公式互相核对；有限样本本身不替代证明。

定理本身与维数无关。

## 10. 与数值半群前人工作的关系

这一阶段非常接近成熟 factorization theory，必须主动收窄创新边界。

数值半群、Apéry sets 与 extremal factorization length 都是经典对象。尤其 Chapman、Dugan、Gaskari、Lycan、Mendoza De La Cruz、O'Neill、Ponomarenko 已研究数值半群中包含 `p=infinity` 的 `p`-length，并证明最终准多项式行为；他们对 minimum `L_infinity` 的分析显式使用 Apéry set [SRC-CHAPMAN-ETAL-2024-P-LENGTHS]。

因此 P025 不把以下内容据为新发现：

- Apéry 剩余类压缩；
- 数值半群 factorization invariant 的最终准多项式/仿射周期行为；
- `L_infinity` factorization length 本身。

当前项目侧仅保留更窄的候选桥：

\[
\boxed{
\text{signed certificate preimage access}
\xrightarrow{y=r\mathbf1-x}
\text{Apéry-controlled numerical-semigroup defect}
}
\]

以及它作为 arithmetic-derivative witness access 的精确有限精度接口。

该精确桥的历史优先性仍为 `NOVELTY_UNVERIFIED`。

## 11. 架构后果

补充 13–16 现在在一个 arithmetic block 内形成严格的信息阶梯：

\[
\boxed{
\text{完整 prime-coordinate row}
\to
A(n)=\gcd(\text{row})
\to
\text{primitive row }b
\to
\Sigma_{\rm Ap}(b)
\to
\text{eventual access response}.
}
\]

不同未来语言在不同层停止：

- 只问 image membership，`A(n)` 就足够；
- 精确 absorption floor 可能只需 block image generators 与 ideal intersection；
- 只问某一个目标，需要局部 access 计算；
- 只问所有充分大的 target-access，有限 Apéry access profile 已足够；
- 精确小 preperiod access 仍可能需要更细信息。

因此“精度”再次表现为未来查询索引下的最小充分状态，而不是 block 自带的一个万能标量。

## 12. 可执行资产

新增：

- `src/enterprise_math/abc_block_access_apery.py`
  - primitive 正系数行规范化；
  - signed-access / nonnegative-defect 精确变换；
  - 模 `P=sum b_i` 的 Apéry values；
  - 每个 Apéry 元素的最小非负 `L_infinity` 分解半径；
  - 精确的 residue-specific 第一稳定目标；
  - 精确异常目标集合；
  - eventual access 闭式与周期移位检查；
  - 独立 finite exact access oracle。
- `tests/test_abc_block_access_apery.py`
  - `(5,2)` 的精确 profile 与唯一异常目标 `1`；
  - 小型互素二变量行上与 closed modular solver 穷举交叉验证；
  - 三坐标回归；
  - 恢复 block 示例中的 `nu=27` 与 `nu=13`；
  - target/row gcd 缩放兼容性。

## 13. 下一前沿

没有 hard block。继续：

1. 将 exact Apéry access profile 与 P024 的 boundary/semigroup precision 对照，决定母层归属；
2. 研究 `Sigma_Ap` 在底层整数 block 的乘法、幂运算下怎样变化；
3. 判断 finite exceptional set 是否还能压成比完整 Apéry pair list 更小的 task-specific signature；
4. 在不隐藏 exact profile 的前提下，给 first stable targets 推导只依赖 block 系数的直接上界；
5. 检验同一个 signed-preimage / defect-semigroup 变换是否出现在非 ABC 的 relation-conditioned certificate system 中；
6. 始终区分成熟 numerical-semigroup theory 与 P025 的架构特化。
