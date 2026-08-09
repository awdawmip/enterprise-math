# P024 —— 晶格 Guard 精度与 Score-Lattice Arrangement，补充 01

状态：`ACTIVE RESEARCH NOTE`  
母文：`docs/P024_ACTION_LANGUAGE_PRECISION.zh-CN.md`  
范围：整数晶格平移 + 完整整数仿射阈值 guard 向量  
依赖：P024 可达边界精度与 P023 未来兼容商纪律

## 1. 为什么一维定理还不够

P024 第一阶段已经证明：在整数直线上，观测阈值边界经真实可达的未来平移向当前状态空间回拉后，会切出最粗的未来安全精度胞元。

最直接的高维猜测会是：

> 把一维动作集合换成向量动作集合，然后数可达向量残差或可达平移数。

E002 的向量执行器研究已经给出反例：物理向量动作即使高度相关、联合残差很少，只要未来观测仍逐坐标暴露边界相位，就可能需要大量独立精度类别。

因此正确的高维对象必须把三件事分开：

1. **动作侧可达性** —— 未来究竟能执行哪些平移；
2. **观测方向** —— 未来任务实际读取哪些整数线性 score；
3. **状态侧 score 可行性** —— 哪些 score 组合真的能由同一个晶格状态同时产生。

本补充对“完整 guard truth-vector”给出这一分解的精确形式。

## 2. 设定

细状态为

\[
x\in\mathbb Z^n.
\]

有限平移动作字母表为

\[
A=\{a_1,\ldots,a_m\}\subseteq\mathbb Z^n,
\qquad
T_a(x)=x+a.
\]

对 horizon `h`，记

\[
M_h
\]

为长度不超过 `h` 的动作词所能产生的全部累计平移向量，包括空词产生的零向量。

声明的观测是 `r` 个整数仿射阈值 guard 的**完整向量**：

\[
G_j(x)=\mathbf1_{w_j\cdot x\ge\theta_j},
\qquad
w_j\in\mathbb Z^n,
\quad
\theta_j\in\mathbb Z.
\]

状态语义中不引入欧氏范数、实值超平面距离或连续体完成。

### Guard 原始坐标

对每个非常量 guard 定义

\[
d_j=\gcd(|w_{j1}|,\ldots,|w_{jn}|),
\qquad
p_j=w_j/d_j,
\]

以及

\[
\tau_j=\left\lceil\frac{\theta_j}{d_j}\right\rceil.
\]

由于 `w_j·x` 永远是 `d_j` 的整数倍，

\[
\boxed{
G_j(x)=\mathbf1_{p_j\cdot x\ge\tau_j}.
}
\]

因此原始整数 score

\[
z_j=p_j\cdot x
\]

就是该 guard 的精确坐标。零行对应常量 guard，不产生精度区分。

定义原始 score 映射

\[
P:\mathbb Z^n\to\mathbb Z^r,
\qquad
P(x)=(p_1\cdot x,\ldots,p_r\cdot x),
\]

讨论秩时忽略常量 guard。其像

\[
\boxed{\Lambda=P(\mathbb Z^n)}
\]

称为 **guard-score lattice**。

## 3. P024-S1-T01 —— 可达 guard 回拉 arrangement

对每个非常量 guard `j`，定义 horizon-`h` 投影动作位移

\[
S_{h,j}=\{p_j\cdot m:m\in M_h\}\subseteq\mathbb Z
\]

以及回拉到当前时刻的 cut 集合

\[
\boxed{
C_{h,j}=\{\tau_j-s:s\in S_{h,j}\}.
}
\]

未来执行平移 `m` 后，

\[
G_j(x+m)=1
\iff
p_j\cdot x\ge\tau_j-p_j\cdot m.
\]

所以完整 horizon-`h` 未来 guard signature 恰好在下列仿射超平面切出的整数胞元上保持常值：

\[
\boxed{
p_j\cdot x=c,
\qquad c\in C_{h,j}.}
\]

换句话说，一维 P024 的边界轨道被沿每个原始 guard score 拉回到高维状态空间。

### 解释

高维未来安全精度不必是矩形。其胞元可以是多个整数 slab 的交，边界可自然倾斜。这里不需要引入实值距离。

## 4. P024-S1-T02 —— 最粗 guard-rank normal form

对一个原始整数 score `z`，定义

\[
\rho_{h,j}(z)
=\#\{c\in C_{h,j}:c\le z\}.
\]

对状态 `x`，定义 rank 向量

\[
\boxed{
\rho_h(x)
=
\bigl(\rho_{h,1}(p_1\cdot x),\ldots,
\rho_{h,r}(p_r\cdot x)\bigr),
}
\]

常量 guard 不贡献非平凡坐标。

则对任意 `x,y in Z^n`，

\[
\boxed{
\rho_h(x)=\rho_h(y)
\iff
G(x+m)=G(y+m)
\quad\text{对所有 }m\in M_h.
}
\]

因此 `rho_h` 就是保存完整 guard-vector horizon-`h` 未来语言的最粗确定性商。

### 证明

若 rank 相同，则对每个 guard `j`，两者原始 score 位于 `C_(h,j)` 每条 cut 的同一侧。每个未来动作词都对应其中某条实际 cut，因此所有未来 guard bit 相同。

反之，如果第 `j` 个 rank 不同，则存在一条真实可达 cut

\[
c=\tau_j-p_j\cdot m
\]

落在两个 score 之间。对应的可达平移 `m` 会让第 `j` 个 guard 输出不同，因此两状态未来可区分。∎

这就是声明的完整 guard-vector 观测下，一维可达边界定理的精确多维版本。

## 5. P024-S1-T03 —— Score-lattice 因子化与 kernel 永久不可见

rank 状态因子化为

\[
\boxed{
\mathbb Z^n
\xrightarrow{P}
\Lambda
\xrightarrow{\rho_h}
\text{未来安全类别}.
}
\]

因此

\[
P(x)=P(y)
\Longrightarrow
\rho_h(x)=\rho_h(y)
\]

对任意 horizon 和任意平移动作词都成立。

特别地，

\[
\boxed{x-y\in\ker P}
\]

对这套“纯平移 + 完整 guard-vector”语言永久不可见。

所以真正相关的维度不必等于环境维度 `n`，而只满足

\[
\boxed{
\operatorname{rank}\Lambda
\le\min(n,r).
}
\]

这只是表示/任务结论，并不声称物理状态本身只有这些维度。若未来加入更丰富观测或运算，当前 `ker P` 中的方向仍可能重新变得可见。

## 6. P024-S1-T04 —— 精确类别数由 score-lattice 可行性决定，默认不是乘积

每个非常量 guard `j` 都有

\[
|C_{h,j}|+1
\]

个形式上的标量 rank 区间。

若这些坐标完全独立，形式 rank box 的大小是

\[
\prod_j(|C_{h,j}|+1).
\]

但真实状态必须同时产生一个属于公共像格 `Lambda` 的 score 向量。因此精确未来安全类别数是

\[
\boxed{
N_h
=|\rho_h(\Lambda)|
\le
\prod_j(|C_{h,j}|+1).
}
\]

定义缺陷集

\[
\boxed{
D_h
=
\prod_j\{0,\ldots,|C_{h,j}|\}
\setminus
\rho_h(\Lambda),
}
\]

它就是**形式上允许、但晶格上不可实现的精度胞元**的有限集合。

### Score 映射满射时的充分条件

若原始 score 映射满足

\[
P(\mathbb Z^n)=\mathbb Z^r,
\]

则每个标量 rank 区间都包含整数 score，所有乘积组合都可实现，因此

\[
\boxed{
N_h=
\prod_j(|C_{h,j}|+1).
}
\]

满射是充分条件，但不是某个特定 cut 家族上乘积等式成立的必要条件。

## 7. P024-S1-T05 —— 显式 score-lattice 缺陷：16 个形式胞元只有 14 个可实现

取

\[
x=(x_1,x_2)\in\mathbb Z^2,
\]

两个 guard 为

\[
G_1(x)=\mathbf1_{x_1+x_2\ge2},
\qquad
G_2(x)=\mathbf1_{x_1-x_2\ge2},
\]

唯一平移动作为

\[
a=(1,0).
\]

horizon `2` 时，可达累计位移是

\[
(0,0),(1,0),(2,0),
\]

所以两个 guard 的回拉 cut 都是

\[
\{0,1,2\}.
\]

每个 guard 都有 4 个标量 rank 区间，形式乘积 box 因此有

\[
4\cdot4=16
\]

种 rank。

但原始 score lattice 为

\[
\Lambda
=\{(u,v)\in\mathbb Z^2:u\equiv v\pmod2\},
\]

因为

\[
u=x_1+x_2,
\qquad
v=x_1-x_2.
\]

rank `1` 强制相应 score 等于 `0`，rank `2` 强制 score 等于 `1`。因此

\[
(1,2),\qquad(2,1)
\]

违反奇偶约束，是空胞元。

其余 rank 均可实现，于是

\[
\boxed{N_2=14<16.}
\]

这严格否定了“高维类别数总等于各 guard 类数乘积”的普遍命题。

## 8. P024-S1-T06 —— Semigroup/group 性质是 observable-direction 相对的

对 guard `j`，真正控制未来 cut 轨道的只有投影动作生成元

\[
\boxed{
D_j=\{p_j\cdot a:a\in A\}\subseteq\mathbb Z.
}
\]

所以标量 P024 分类可以**逐 guard 方向独立应用**：

1. 所有投影生成元都为零：该 guard 对动作不变；
2. 所有非零投影只有一个符号：按符号/gcd 归一化后仍是一维单向 numerical semigroup；
3. 同时出现正负投影：非负词幺半群已经等于 `Z` 中的完整 gcd 子群。

因此同一套物理动作可以在一个观测方向上已经群完备，在另一个观测方向上仍然单向。

### 最小方向例子

取

\[
A=\{(1,1),(-1,1)\}.
\]

对 `x` guard，投影生成元为

\[
\{1,-1\},
\]

所以未来动作语言是完整群 `Z`。

对 `y` guard，投影生成元为

\[
\{1,1\},
\]

所以未来动作语言仍为单向半群 `N_0`。

因此不存在一个与任务无关的高维总标签，可以简单说“这个动作系统是 gcd 型”或“这个动作系统存在 semigroup holes”。分类必须相对于未来真正读取的 score 方向。

## 9. P024-S1-T07 —— 全局动作幺半群何时等于群完备化的精确判据

设

\[
M=\mathbb N_0a_1+\cdots+\mathbb N_0a_m
\]

为非负词平移幺半群，

\[
G=\mathbb Za_1+\cdots+\mathbb Za_m
\]

为其生成的阿贝尔群。

则

\[
\boxed{
M=G
\iff
\exists\lambda_1,\ldots,\lambda_m\in\mathbb Z_{>0}
\text{ 使 }
\sum_i\lambda_i a_i=0.
}
\]

### 正系数零关系推出群完备

若

\[
\sum_i\lambda_i a_i=0
\]

且每个 `lambda_i>0`，则对任一生成元

\[
\boxed{
-a_i
=(\lambda_i-1)a_i
+\sum_{j\ne i}\lambda_j a_j
\in M.
}
\]

所以 `M` 包含每个生成元的逆，故 `M=G`。

### 群完备反推正系数零关系

若 `M=G`，则每个 `-a_i` 都有非负词表示

\[
-a_i=\sum_j\mu_{ij}a_j,
\qquad\mu_{ij}\ge0.
\]

把

\[
a_i+\sum_j\mu_{ij}a_j=0
\]

对所有 `i` 相加，就得到一个每个生成元系数都至少为 1 的零关系。∎

### 与一维定理的关系

一维中，只要存在至少一个正生成元和一个负生成元，就自动可以构造正整数零关系。高维中，“向多个方向走”本身并不足够，真正精确的条件是上面的正系数零关系。

## 10. P024-S1-T08 —— 一维“有限 holes + conductor 边界层”不能整体照搬到高维

P024 第一阶段利用了一维事实：gcd-one numerical semigroup 在 `N_0` 中只有有限多个 holes，因此不均匀只存在于有限边界层，远端最终恢复规则 gcd 网格。

高维 affine semigroup 的 saturation 中却可能有无限 holes。

考虑

\[
M=
\langle(2,0),(0,1),(1,1)\rangle_{\mathbb N_0}
\subseteq\mathbb N_0^2.
\]

它生成的群是整个 `Z^2`，因为

\[
(1,0)=(1,1)-(0,1).
\]

它的有理锥是第一象限，因此在生成群中的 saturation 是 `N_0^2`。

成员关系可以精确写出：

- `x` 为偶数时，`(x,y)` 由 `(2,0)` 与 `(0,1)` 生成；
- `x` 为奇数且 `y>=1` 时，用一个 `(1,1)`，剩余横向部分为偶数，剩余纵向部分非负；
- `x` 为奇数且 `y=0` 时不可能，因为任何一次 `(1,1)` 都会增加第二坐标。

因此 holes 恰为

\[
\boxed{
(2k+1,0),
\qquad k\in\mathbb N_0,
}
\]

沿边界 face 无限延伸。

但同时又有

\[
\boxed{
(0,1)+\mathbb N_0^2\subseteq M.
}
\]

所以虽然 hole 集无限，仍存在 conductor translate。

### 对精度理论的后果

一维命题

> 所有 semigroup 不规则性都可以由有限个缺失 cut 完全表示

不能不加条件地推广到任意 affine action monoid。

不过对本补充的“完整独立线性 guard”语言，每个单独 guard 只看到一个一维投影，因此各方向仍保留标量 P024 的 conductor 结构。只有当未来观测真正依赖**多个 action-score 的联合同时可达性**时，全局 affine holes 才会直接进入精度义务。

这正是下一阶段需要攻击的边界。

## 11. P024-S1-T09 —— 完整 guard-vector 定理不能自动推广到聚合观测

T01–T06 的前提是未来输出逐个报告每个 guard bit。

若任务只观察聚合量，例如

\[
G_1(x)\wedge G_2(x),
\]

guard-rank 向量可能严格过细。

例：

\[
G_1=\mathbf1_{x_1\ge0},
\qquad
G_2=\mathbf1_{x_2\ge0},
\qquad
A=\{(1,1)\}.
\]

两个状态

\[
(-1,1)
\quad\text{与}\quad
(1,-1)
\]

具有不同的完整 guard-rank 状态，但到 horizon 1 为止，它们的 conjunction 输出完全相同：

\[
\text{False}\to\text{True}.
\]

所以

\[
\boxed{
\text{完整 guard-vector 精度}
\ne
\text{任意 guard 聚合任务的普遍精度}.
}
\]

联合/聚合观测必须回到 P023，或者由 P024 另行根据 joint action-score reachability 推导专门算术结构。

## 12. 与 E002 向量精度的关系

E002 补充 04 已证明：对矩形 centered quotient 观测，未来安全 detail 类别数由可达残差集合的**坐标投影**决定，而不是由相关联合残差向量轨道的基数直接决定。

本补充在非周期仿射 guard 语言中解释了同一类结构分离：

- **动作侧相关性** 对逐 guard 独立输出会压缩成每个 guard 的投影 cut 集；
- **状态侧相关性** 则通过公共 score lattice `Lambda` 保留下来，并可使形式乘积胞元为空。

这里不把 E002 的周期矩形 quotient 声明为有限仿射 guard 定理的字面特例；其边界族是无限周期的，需要在后续“周期晶格胞元”阶段专门搭桥。

## 13. 与 A3 guard-image lattice 路线的关系

A3 relation-quotient 路线已经研究了整数 guard-score lattice、粗 fiber 内阈值 sign pattern 的精确可达性，以及标准 hyperplane-arrangement 复杂度界。

职责刻意分开：

- **A3**：负责一个候选粗商内部的隐藏 guard-image lattice 可达性与 relation-state 保留；
- **P023**：负责一般未来安全 quotient / 最小修复母理论；
- **P024**：负责前向平移动作语言，以及这些动作如何诱导精度胞元的算术几何。

本补充吸收 score-lattice / hyperplane 视角，但不复制 A3 的 rank-two 可行性求解器或 arrangement-count 母理论。

## 14. 可执行审计

实现：

- `src/enterprise_math/lattice_guard_precision.py`

测试：

- `tests/test_p024_lattice_guard_precision.py`

提交测试覆盖：

1. 非原始整数 guard 的精确归一化；
2. 多组有限 1D/2D 系统中 direct future signature 与 guard-rank 等价关系；
3. score-map kernel 方向的永久不可见性；
4. score 坐标自由可实现时的乘积类别数；
5. 精确的 `14 < 16` 奇偶 score-lattice 缺陷；
6. 逐方向 semigroup/group 分类；
7. 由严格正系数零关系构造所有生成元逆动作词；
8. 无限 affine-hole 家族及其 conductor translate；
9. conjunction 反例，证明聚合观测可以严格比完整 guard-rank 更粗。

提交前的独立重实现还在超过五千组小型动作/guard 系统上检验了 T02 等价式，未发现不一致。有限检查只审计实现与定理陈述，不替代上面的普通证明。

## 15. 前人工作边界

Hyperplane arrangement、整数晶格、affine semigroup、saturation、holes、conductor、gcd/Bezout 与整数线性可行性均为成熟数学。P024 不主张发明这些工具。

单独的 prior-art 文档登记标准 hyperplane-arrangement 与 affine-semigroup/hole 文献，用于约束新颖性表述。

这一综合精度解释的历史新颖性继续保持 `NOVELTY_UNVERIFIED`。

## 16. 下一批压力测试

现在最有价值的后续目标已经被清楚分离：

1. **联合/聚合 guard 观测**：从 joint action-score monoid 推导最小状态，而不是继续使用独立投影；
2. **状态依赖动作字母表**：把加法幺半群替换成真实可达转移图，检验边界轨道定理还能保留多少；
3. **周期晶格胞元观测**：推导 Hermite/Smith 相容版本，在不预设矩形胞元的情况下吸收 E002 向量 quotient 精度；
4. **P022 几何桥**：只有当某个晶格几何明确声明真实观测边界与运动字母表后，才通过 P024 编译其未来安全几何精度，而不能提前导入一个万能 metric resolution。
