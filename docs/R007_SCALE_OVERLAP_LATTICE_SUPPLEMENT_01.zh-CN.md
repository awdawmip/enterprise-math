# R007 尺度交叠格补充 01

状态：`PROVED WIP / CROSS-ROUTE SUPPLEMENT / NOT CANONICAL`

范围：`RS-R007-SCALE-COLLAPSE-DESCENT-NOGO` 的继续研究；连接 P023/P024 与 R005A/R005B。

本说明记录 R007 的第二层结构。第一阶段 no-descent 定理研究的是一个固定 quotient 与一个固定 perfect-power collapse；这里真实状态本身是一族有限 uniform scales，而核心对象是这些尺度层的交叠几何。

## 1. 加权尺度交叠 nerve

对正整数尺度 `d`，记

\[
I_{d,i}=\left(\frac{i}{d},\frac{i+1}{d}\right),
\qquad 0\le i<d.
\]

对有限非空尺度族 `S`，定义尺度交叠 nerve `N(S)`：

- 顶点是带尺度颜色的胞元 `(d,i)`，其中 `d in S`；
- 若一组顶点对应的开区间存在共同正长度交叠，则构成 simplex；
- 每个 full-color maximal simplex 的权重取其共同交叠的有理长度。

full-color maximal simplices 恰好对应所有网格边界叠加后切出的原子区间。

同一个加权对象会以两种不同方式同时承载 gcd meet 与 lcm join。

## 2. 连通 quotient 构造 gcd meet 对象

令

\[
g=\gcd(S).
\]

在 `S` 中每个尺度上都是网格边界的点，恰好是

\[
\frac{k}{g},\qquad 1\le k<g.
\]

因此所有开放尺度胞元的并集，就是从 `(0,1)` 中去掉这些共同边界，正好有 `g` 个连通分量。任意有限个尺度胞元的非空交仍是区间。由标准 good-cover nerve theorem，

\[
\mathcal N(S)\simeq \bigsqcup_{k=0}^{g-1}(0,1).
\]

特别地，

\[
\beta_0(\mathcal N(S))=\chi(\mathcal N(S))=g,
\qquad
\beta_j(\mathcal N(S))=0\quad(j\ge1).
\]

还存在更强的对象级陈述。因为对每个 `d in S` 都有 `g | d`，每个 `d`-胞元恰好落在唯一一个 `g`-胞元中。它的分量标签为

\[
\pi_{d\to g}(i)=\left\lfloor\frac{i}{d/g}\right\rfloor.
\]

overlap edge 永远不会跨越 `g`-边界，而每个 `g`-block 内的胞元构成一个连通分量。因此按左右次序排列的分量 quotient 规范地满足

\[
\boxed{\pi_0\mathcal N(S)\cong R_g,}
\]

且每个输入尺度 `R_d` 到该 quotient 的映射，正好就是 canonical divisibility projection `R_d -> R_g`。

所以交叠几何构造出来的不是“分量数量碰巧等于 gcd”，而是真正的 gcd/meet scale object。

### 2.1 带颜色的 simplex 计数

对非空子族 `T subseteq S`，令 `A(T)` 为 `T` 中所有网格叠加后形成的原子区间数。边界集合的交仍是 gcd-grid，因此 inclusion-exclusion 给出

\[
\boxed{
A(T)=
\sum_{\varnothing\ne U\subseteq T}
(-1)^{|U|+1}\gcd(U).
}
\]

颜色集合恰为 `T` 的 simplex 数正好等于 `A(T)`。因此完整的带颜色 f-vector 由各子集的 gcd 数据决定。

例如

\[
S=\{6,10,15\}
\]

三个二尺度场的分量数分别是 `2,3,5`，但三尺度 nerve 因为 `gcd(6,10,15)=1` 而整体连通。其 f-vector 为

\[
(f_0,f_1,f_2)=(31,52,22),
\]

因此

\[
31-52+22=1.
\]

所以 pairwise disconnected 并不意味着更高层的多尺度 gluing 后仍然 disconnected。

## 3. 有理原子长度恢复 lcm join

设叠加网格产生的原子区间长度为

\[
\ell_1,\ldots,\ell_m\in\mathbb Q_{>0}.
\]

则

\[
\boxed{
\operatorname{lcm}(S)
=
\operatorname{lcm}\bigl(
\operatorname{den}(\ell_1),\ldots,
\operatorname{den}(\ell_m)
\bigr),
}
\]

其中分母均取约分后的分母。

### 证明

令

\[
L=\operatorname{lcm}(S).
\]

所有输入边界都是 `L`-grid 边界。把所有不同边界排序并写成

\[
0=\frac{b_0}{L}<\frac{b_1}{L}<\cdots<\frac{b_m}{L}=1,
\]

其中 `b_j` 为整数。于是原子长度为

\[
\ell_j=\frac{a_j}{L},
\qquad
a_j=b_j-b_{j-1}>0.
\]

整数边界坐标中，对每个 `d in S` 都包含 `L/d` 的全部整数倍。因此全部边界坐标生成的 `Z` 子群的 gcd 为

\[
\gcd_{d\in S}\frac{L}{d}=1,
\]

因为对 `L` 的每个素因子，都至少有一个输入尺度取得该素因子的最大指数。相邻 gap 与所有边界坐标生成同一个整数子群，所以

\[
\gcd_j a_j=1.
\]

`a_j/L` 约分后的分母是 `L/gcd(L,a_j)`。逐素数看，因为所有 `a_j` 的 gcd 为一，这些约分分母的 lcm 会保留 `L` 的每个完整素指数，因此等于 `L`。

### 3.1 Uniformization 是 reflector

在有限有理 interval partitions 的格中，uniform partitions 对普通 join 并不封闭。例如尺度 `2` 与 `3` 的普通共同 refinement 具有不等长原子区间，而不是 uniform `6`-partition。

但对任意有限有理 interval partition `P`，都存在唯一的最小 uniform refinement `U(P)`：取所有有理边界约分分母的 lcm 即可。因此 `U` 是“取最小 uniform majorant”的 reflector。

对 uniform 输入尺度，

\[
\boxed{
\mathsf U\!\left(\bigvee_{d\in S}\mathcal P_d\right)
=
\mathcal P_{\operatorname{lcm}(S)}.
}
\]

相反，uniform 输入 partitions 的普通 meet 仍然留在 uniform world：

\[
\boxed{
\bigwedge_{d\in S}\mathcal P_d
=
\mathcal P_{\gcd(S)}.
}
\]

因此 uniform-scale world 对 meet 闭合，而普通 join 通常会离开它，需要一次 canonical uniformization closure 才能返回。

## 4. Divisor-lattice 尺度包络

记

\[
g=\gcd(S),\qquad L=\operatorname{lcm}(S).
\]

每个输入尺度都位于 divisibility interval `[g,L]` 中。对每个素数 `p`，令

\[
m_p=\min_{d\in S}v_p(d),
\qquad
M_p=\max_{d\in S}v_p(d).
\]

则

\[
\boxed{
[g,L]_{\mid}
\cong
\prod_p[m_p,M_p].
}
\]

若某个素方向满足 `m_p=M_p`，它在整个尺度族中是锁定方向；若 `m_p<M_p`，才是真正发生变化的自由方向，其深度跨度为 `M_p-m_p`。发生变化的素方向数量就是 scale envelope 的产品维数，并且

\[
|[g,L]_{\mid}|
=
\prod_p(M_p-m_p+1)
=
\tau(L/g).
\]

这把“不同素因子对应不同坍缩维度”的口头说法修正得更精确：一个素方向只有在它的指数确实在当前尺度族中变化时，才构成当前 family 的一个真实尺度维度。

## 5. 二尺度 forest 几何与欧几里得叶编码

对两个尺度 `d,e`，令 `B(d,e)` 为正长度交叠的二部图。记

\[
g=\gcd(d,e),
\qquad
d'=d/g,
\qquad e'=e/g.
\]

则

\[
\boxed{
\#\pi_0 B(d,e)=g,
\qquad
|E(B)|=d+e-g.
}
\]

该图是由 `g` 个同型 tree components 构成的 forest。设 `d'<=e'`。在每个分量中，每个内部 `d'`-grid 边界都落在唯一一个 `e'`-胞元内部；这个细胞元 degree 为二，并跨接相邻两个粗胞元。这样的 bridge cells 恰有 `d'-1` 个。其余 `e'-d'+1` 个细胞元都是 leaves。因此每个分量都是一条交替的 subdivided path，并在 `d'` 侧顶点挂有 leaf bundles，而且

\[
\boxed{
\operatorname{diam}(\text{component})=2d'
=\frac{2\min(d,e)}{\gcd(d,e)}.
}
\]

当 `g=1` 且 `e=qd+s`、`0<s<d` 时，细尺度一侧的叶 multiplicities 满足

\[
\lambda_i(d,e)-(q-1)=\lambda_i(d,d+s).
\]

去掉强制的左端点叶后，剩余二进制装饰就是

\[
w_i=
\left\lfloor\frac{(i+1)s}{d}\right\rfloor
-
\left\lfloor\frac{is}{d}\right\rfloor,
\]

即斜率 `s/d` 的有理 lower mechanical word。其 1 的位置间距会递归编码下一步欧几里得 quotient/remainder，进而编码 continued-fraction 数据。

mechanical/Christoffel/Sturmian words 与欧几里得/连分数递归之间的联系属于经典 prior art。R007 specialization 的价值，是它们精确地作为 scale-overlap forest 的 leaf decoration 出现。

## 6. 素数分裂语义

因为

\[
\#\pi_0B(n,d)=\gcd(n,d),
\]

定义首次断裂尺度

\[
D(n)=
\min\{2\le d\le n:B(n,d)\text{ disconnected}\}.
\]

则

\[
\boxed{D(n)=\operatorname{spf}(n).}
\]

因此

\[
\boxed{
n\text{ prime}
\iff
B(n,d)\text{ 对所有 }2\le d<n\text{ 都 connected}.
}
\]

对一个素方向 `p`，

\[
\boxed{
\#\pi_0B(n,p^k)
=p^{\min(v_p(n),k)}.
}
\]

所以 `p` 是一个 split direction，而 `v_p(n)` 是该方向的 splitting saturation depth。

binary split observable

\[
\chi_d(n)=\mathbf 1\{\gcd(n,d)>1\}
\]

满足

\[
\boxed{
\chi_d=\bigvee_{p\mid d}\chi_p
=\chi_{\operatorname{rad}(d)}.
}
\]

素数幂只会加深既有方向，而不会创造新的 binary split direction。按尺度从小到大扫描，并对新的 prime scale `p` 标记所有使 `B(n,p)` 断裂的未来 `n`，就精确复现 Eratosthenes sieve 的语义。这只是结构重述，不主张算法加速。

## 7. Provenance no-descent：overlay 不能决定 meet

令真实状态是一个有限尺度族 `S`。定义

\[
Q(S)=\text{忘掉 layer identity 后的 overlay partition},
\qquad
H(S)=\gcd(S).
\]

即使可见 overlay 更细，也可能丢失 `H` 需要的 layer relation。

例如

\[
S_1=\{6\},
\qquad
S_2=\{2,6\}.
\]

`2`-grid 已经完全包含在 `6`-grid 中，因此

\[
Q(S_1)=Q(S_2),
\]

包括完全相同的 atom lengths。因此 lcm/join 仍可恢复，并且都是 `6`。但

\[
H(S_1)=6,
\qquad
H(S_2)=2.
\]

所以 meet/common-scale 无法通过“忘掉 layer 来源、只保留 overlay”的 quotient 下降。

### 7.1 固定 uniform overlay 上的精确 repair width

固定可见 overlay `P_M`。任何隐藏尺度都必须整除 `M`，而边界 `1/M` 又迫使尺度 `M` 本身出现。因此隐藏 fiber 恰好是 `Div(M)` 中所有包含 `M` 的 subsets，总共有

\[
\boxed{2^{\tau(M)-1}}
\]

个 provenance states。

可能出现的 future gcd 则恰好遍历 `M` 的所有因子：

\[
\boxed{
H(Q^{-1}(P_M))=\operatorname{Div}(M).
}
\]

因此，对 one-shot future task “回答 common scale”，最粗 repair 恰有 `tau(M)` 个类别；直接保存 gcd 即充分。最坏固定长度编码只需要

\[
\left\lceil\log_2\tau(M)\right\rceil
\]

bits，而不是恢复完整 provenance。

对 `g | M`，repair 值恰为 `g` 的隐藏 families 数量为

\[
\boxed{
C_M(g)=
\sum_{h\mid M/g}
\mu(h)\,2^{\tau(M/(gh))-1}.
}
\]

这只是 divisor lattice 上的普通 Möbius inversion。它精确量化了：即使 task-relative repair 被补回，仍有多少 provenance 继续被删除。

若 `M` 为含 `k` 个不同素因子的 squarefree 数，则 `tau(M)=2^k`：one-shot gcd repair 只需要 `k` 个固定长度 bits，而完整 provenance fiber 有 `2^{2^k-1}` 个 states。

## 8. Future language 扩张会扩大所需状态

上面的很小 repair 只对应 one-shot gcd 查询。若 layer 具有稳定 identity，而 future language 允许先删除任意指定 layer，再观察剩余 gcd，则 predictive state 会显著变细。

把其他 layers 全部删除，只留下第 `i` 层，就可以观察

\[
\gcd(\{d_i\})=d_i.
\]

因此任意两个只要某个带标签 layer 的尺度不同的真实 states，都存在有限 future word 可以把它们区分开。在这个更强 future language 下，完整 per-layer scale data 都必须保留。

这给出一个完全有限、精确的 P023/P024 例子：需要什么状态由 future operation language 决定，而不是由当前某个标量意义上的“精度”决定。

## 9. 从 gcd 到 lcm 的 deletion-horizon filtration

对带标签尺度族

\[
S=(d_1,\ldots,d_m),
\]

以及 deletion budget `0<=h<=m-1`，定义

\[
E_h(S)
=
\operatorname{lcm}_{|D|\le h}
\gcd(S\setminus D).
\]

对每个素数 `p`，把各 layer 的 valuation 排序：

\[
a_{p,(1)}\le\cdots\le a_{p,(m)}.
\]

则

\[
\boxed{
v_p(E_h)=a_{p,(h+1)}.
}
\]

因为若想把剩余 minimum 提升到第 `h+1` 小值以上，至少要删掉 `h+1` 个更低 layers；而删掉最低的 `h` 个层正好能达到第 `h+1` 个 order statistic。

因此得到一条 divisor chain：

\[
\boxed{
E_0\mid E_1\mid\cdots\mid E_{m-1},
}
\]

两个端点为

\[
\boxed{
E_0=\gcd(S),
\qquad
E_{m-1}=\operatorname{lcm}(S).
}
\]

这就是从 meet 到 join 的 deletion-horizon chain。

### 9.1 Envelope 不等于联合可达

该链只保留各 prime direction 的 marginal order statistics，并不保留不同 prime depths 在同一个 layer 中如何相关。

例如

\[
S_1=\{6,10,15\},
\qquad
S_2=\{30,2,15\}
\]

在 `2,3,5` 三个素方向上都有相同的 valuation multiset `{0,1,1}`，因此两者都满足

\[
(E_0,E_1,E_2)=(1,30,30).
\]

但删除一层后的 exact reachable gcd sets 不同。`S_1` 恰删一层得到 `{2,3,5}`，而 `S_2` 得到 `{1,2,15}`。

所以 coordinatewise capability envelope 不能和 jointly reachable future state 混为一谈。

## 10. Capability ideals 与 exact reachable closure

定义候选 common scale `c` 的 defect set：

\[
\operatorname{Def}_S(c)=\{i:c\nmid d_i\}.
\]

`c` 能整除某个“至多删除 `h` 层后”的 surviving gcd，当且仅当所有 defect layers 都能够被删掉：

\[
\boxed{
c\in\mathcal C_h(S)
\iff
|\operatorname{Def}_S(c)|\le h.
}
\]

因此

\[
\mathcal C_h(S)
=
\{c\mid\operatorname{lcm}(S):|\operatorname{Def}_S(c)|\le h\}
\]

是 divisor lattice 中的 order ideal，并满足

\[
\mathcal C_0\subseteq\cdots\subseteq\mathcal C_{m-1}.
\]

它的 join 就是 deletion envelope：

\[
\boxed{E_h=\bigvee\mathcal C_h.}
\]

当且仅当 capability ideal 是 principal 时，单个 envelope 对联合 divisibility capability 才是无损的：

\[
\boxed{
\mathcal C_h=\operatorname{Div}(E_h)
\iff
E_h\in\mathcal C_h
\iff
|\operatorname{Def}_S(E_h)|\le h.
}
\]

为了分类 exact reachable gcd outputs，定义 supporter layers：

\[
\operatorname{Supp}_S(c)=\{i:c\mid d_i\},
\]

并在 supporter 非空时定义

\[
\Gamma_S(c)
=
\gcd\{d_i:i\in\operatorname{Supp}_S(c)\}.
\]

`Gamma_S` 对 divisibility order 是 extensive、monotone、idempotent。并且

\[
\boxed{
c\text{ 是某个非空 surviving subfamily 的 exact gcd}
\iff
\Gamma_S(c)=c.
}
\]

加入 deletion budget `h` 后，exact reachable set 因而为

\[
\boxed{
R_h(S)
=
\{c:\Gamma_S(c)=c,\ |\operatorname{Def}_S(c)|\le h\}.
}
\]

三层结构为

\[
\boxed{
R_h=\text{closed exact outputs},
\qquad
\mathcal C_h=\downarrow R_h,
\qquad
E_h=\bigvee R_h.
}
\]

## 11. Formal Concept Analysis 边界

闭包 `Gamma_S` 不是新的通用 closure mechanism。它是 Formal Concept Analysis（FCA）标准 Galois-connection machinery 的一个实例。

把 layer indices 作为 objects，把 prime-power divisibility conditions `p^a` 作为 attributes；当且仅当 `p^a | d_i` 时，layer `i` 拥有属性 `p^a`。于是：

- 候选 divisor 的 extent 就是它的 supporter set；
- 再取这些 supporters 的全部共同 attributes，数论上正好产生 gcd closure `Gamma_S`；
- 条件 `|Supp_S(c)| >= m-h` 正好是 minimum-support threshold；
- support threshold 下的 `Gamma_S` fixed candidates 对应 closed frequent divisibility patterns。

FCA closure operators、concept lattices 和 frequent closed-itemset algorithms 都是成熟 prior art。大规模枚举时应直接消费已有算法，而不是在 R007 内重写。相关的一般 prior-art 基础包括 FCA/Galois-connection 文献，以及 concept-lattice / frequent closed itemset 的构造算法。

R007-specific 的项目层贡献，是把“尺度 layer deletion future + common-scale observable”精确翻译到这个 divisibility incidence context，并把它和同一个 gcd/lcm overlap geometry 接起来。

## 12. 边界陈述与下一步形式化目标

以下区分必须长期明确：

1. `gcd = component quotient` 与 `lcm = atom-denominator uniformization` 是结构重述，不是更快的算术算法。
2. mechanical/Christoffel/continued-fraction recursion 与 FCA/Galois closures 属于既有数学。
3. prime scale 的 divisor-only freedom 不等于 full all-scale naturality；非因子尺度仍可能阻塞 operation。
4. `E_h` 是 join envelope，不保证是 exact reachable common scale。
5. unlabeled overlay 可以保留 lcm，却不可逆地丢失 gcd provenance。
6. minimal repair 始终相对于声明的 future language。

建议形式化顺序：

- Lean：二尺度 overlap component/gcd theorem；
- Lean：主 R007 线的 Farey bridge-descent 与 one-step extension theorem；
- Lean 或有限序形式化：`P_M` 上的 provenance no-descent 与 exact repair width；
- reusable theorem layer：deletion-horizon capability ideal 与 `Gamma_S` closure；
- 由 R005A/R005B 跨路线消费，但不主张算法加速或通用 FCA novelty。
