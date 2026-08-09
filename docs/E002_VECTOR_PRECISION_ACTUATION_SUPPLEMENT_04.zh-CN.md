# E002 — 向量精度与相关执行，补充 04

状态：`ACTIVE ENGINEERING RESEARCH NOTE`  
范围：矩形向量精度、有限视野向量动作、坐标投影修复与相关性扩张  
父文档：`docs/E002_PRECISION_HORIZON_SATURATION_SUPPLEMENT_03.zh-CN.md`  
依赖：E002 中心化精度/执行理论与 P023 任务相关未来兼容理论

## 1. 为什么多维是真正的压力测试

第三阶段的一维定理表明，对单一中心化宽度 `w`，长度不超过 `h` 的全部动作 word 所要求的胞元内精度类别数为

\[
c_h=|S_h|,
\]

其中 `S_h` 是模 `w` 的可达总动作余数集合。

一个很自然的多维猜想，是把 `S_h` 换成可达余数**向量**集合，然后继续使用同样的基数公式。

这个猜想是错误的。

向量粗观测会分别输出每个坐标的商。一个可达余数向量可以同时在多个坐标细节轴上引入独立边界。物理动作轨迹中的坐标相关性，并不意味着这些被观测到的坐标相位也可以一起坍缩。

本补充推导精确的矩形替代公式，并给出对“直接使用子群大小”这一朴素推广的最小反例。

## 2. 矩形中心化精度

令状态为

\[
x=(x_1,\ldots,x_n)\in\mathbb Z^n
\]

并给定中心化奇数胞元宽度

\[
w=(w_1,\ldots,w_n),
\qquad w_i\in2\mathbb N+1.
\]

每个坐标唯一写成

\[
\boxed{
x_i=w_iq_i+r_i-c_i,
\qquad
c_i=\frac{w_i-1}{2},
\qquad
0\le r_i<w_i.}
\]

矩形商/细节状态为

\[
Q_w^c(x)=(q_1,\ldots,q_n),
\qquad
R_w^c(x)=(r_1,\ldots,r_n).
\]

这只是多个一维中心化 Euclidean chart 的笛卡尔积，不引入 Euclidean norm 或隐藏实数坐标。

## 3. E002-T24 — 向量平移兼容性

令一次物理向量动作是

\[
a=(a_1,\ldots,a_n)\in\mathbb Z^n.
\]

每个坐标写成

\[
a_i=k_iw_i+s_i,
\qquad0\le s_i<w_i.
\]

则精确向量运输为

\[
\boxed{
q_i'=q_i+k_i+\gamma_i,
\qquad
r_i'=(r_i+s_i)\bmod w_i,
}
\]

其中

\[
\boxed{
\gamma_i=\mathbf1_{r_i+s_i\ge w_i}.}
\]

因此，一个向量平移能够下降为完整矩形粗商上的确定操作，当且仅当

\[
\boxed{w_i\mid a_i\quad\text{对每个坐标 }i.}
\]

### 证明

运输公式就是第二阶段一维 Euclidean carry 恒等式逐坐标应用。若每个 `s_i=0`，全部 carry 都消失，粗商更新确定。

反过来，只要某个 `s_j` 非零，固定其余细节坐标，并在阈值 `w_j-s_j` 两侧选择两个 `r_j`。两个细向量状态在动作前具有同一个矩形粗商，但动作后的第 `j` 个粗商坐标不同。∎

## 4. 可达向量余数

令 `A` 为有限向量动作 alphabet，`W_h` 为长度不超过 `h` 的所有 word。

对一个 word `v`，令总向量增量为

\[
\Sigma(v)=(\Sigma_1(v),\ldots,\Sigma_n(v)).
\]

定义可达余数向量集合

\[
\boxed{
S_h=
\{(\Sigma_1(v)\bmod w_1,\ldots,\Sigma_n(v)\bmod w_n):v\in W_h\}.
}
\]

对每个坐标定义投影

\[
\boxed{S_{h,i}=\pi_i(S_h)\subseteq\mathbb Z/w_i\mathbb Z.}
\]

## 5. E002-T25 — 精确向量有限视野类别数

对于**完整向量粗商输出**，同一个原矩形胞元中的两个细节向量 `r,r'`，在 horizon `h` 内 future-equivalent，当且仅当对每个坐标 `i` 都有

\[
\boxed{
\mathbf1_{r_i+s\ge w_i}
=
\mathbf1_{r_i'+s\ge w_i}
\quad
\text{对每个 }s\in S_{h,i}.}
\]

因此第 `i` 个坐标恰好被分成

\[
|S_{h,i}|
\]

个未来可区分细节区间，而完整矩形细节胞元恰好被分成

\[
\boxed{
C_h=\prod_{i=1}^n|S_{h,i}|.}
\]

### 证明

对固定未来 word，同一输入胞元内两个状态的第 `i` 个输出粗商，只可能因为该 word 第 `i` 个 residue 对应的 coordinate carry 不同而不同。因此，完整向量输出对所有 word 都相同，等价于对每个坐标、每个实际出现于该坐标投影中的 residue，其 carry bit 都相同。

第三阶段的一维阈值定理给出坐标 `i` 上恰好 `|S_(h,i)|` 个类别。因为输出明确暴露每个粗商坐标，不同细节坐标上的条件相互独立，完整等价关系就是这些坐标等价关系的笛卡尔积，所以类别数为乘积。∎

## 6. E002-T25a — 向量修复 rank

对每个坐标定义一个标量阈值 rank：

\[
\boxed{
\rho_{h,i}(r_i)
=
\#\{s\in S_{h,i}\setminus\{0\}:r_i+s\ge w_i\}.}
\]

则修复状态

\[
\boxed{
(Q_w^c(x),\rho_{h,1}(r_1),\ldots,\rho_{h,n}(r_n))
}
\]

就是保存 horizon `h` 内全部完整向量粗商输出所需的最粗状态。

每个原矩形胞元内部的修复类别数恰好为 `C_h`。

## 7. 对朴素余数向量基数公式的最小反例

取

\[
w_1=w_2=3
\]

以及唯一重复动作

\[
a=(1,1).
\]

到 horizon `2` 时，可达余数向量只有

\[
S_2=\{(0,0),(1,1),(2,2)\},
\]

所以

\[
|S_2|=3.
\]

但是两个坐标投影都是

\[
S_{2,1}=S_{2,2}=\{0,1,2\}.
\]

因此 T25 给出

\[
\boxed{C_2=3\cdot3=9.}
\]

直接枚举也确认，原 `3x3` 胞元中的九个细相位具有九种不同的 horizon-2 完整向量粗商 signature。

所以

\[
\boxed{|S_h|\text{ 不是多维精度类别数}.}
\]

这是对一维定理直接推广的严格负边界。

## 8. E002-T26 — 任意未来坐标 gcd 修复

对动作族

\[
A=\{a^{(1)},\ldots,a^{(m)}\}
\]

逐坐标定义

\[
\boxed{
g_i=\gcd(w_i,|a_i^{(1)}|,\ldots,|a_i^{(m)}|).}
\]

在任意有限未来下，生成 residue 子群在第 `i` 坐标的投影正好是

\[
\boxed{
H_i=\{0,g_i,2g_i,\ldots,w_i-g_i\},
}
\]

并且

\[
|H_i|=w_i/g_i.
\]

因此任意未来下最粗 future-safe 矩形细化的坐标宽度为

\[
\boxed{(g_1,\ldots,g_n)}
\]

每个原矩形胞元内恰好需要

\[
\boxed{
C_\infty=\prod_{i=1}^n\frac{w_i}{g_i}
}
\]

个类别。

### 为什么动作相关性不能降低这个类别数

若两个细节向量在第 `i` 坐标属于不同的修复类别，一维 gcd 定理保证存在某个 `H_i` 中的 residue 能区分它们。由于 `H_i` 是完整生成向量子群的投影，一定存在一个真实有限动作 word，其 residue 向量的第 `i` 坐标就是该值。于是完整向量输出至少在第 `i` 坐标上不同，而其他坐标如何并不重要。

所以完整未来等价关系就是各坐标 gcd 修复的乘积。

## 9. 完整动作子群与被观测精度状态

令

\[
H\subseteq\prod_i\mathbb Z/w_i\mathbb Z
\]

表示向量动作生成的完整 residue 子群。

存在自然包含

\[
\boxed{H\hookrightarrow\prod_iH_i.}
\]

但是 `|H|` 一般并不是精度类别数。

定义整数

\[
\boxed{
\Delta_A
=
\frac{\prod_i|H_i|}{|H|}.}
\]

因为 `H` 是各坐标投影乘积中的有限子群，所以

\[
\boxed{\Delta_A\in\mathbb N_{\ge1}.}
\]

## 10. E002-T27 — 相关性扩张因子

对完整向量粗商观测，有

\[
\boxed{C_\infty=\Delta_A|H|.}
\]

并且

\[
\boxed{\Delta_A=1}
\]

当且仅当

\[
\boxed{H=\prod_iH_i.}
\]

### 证明

第一式直接来自定义与 T26。由于 `H` 是坐标投影乘积的有限子集/子群，二者基数相同恰好等价于包含映射为满射，也就是 `H` 等于完整直积。∎

### 解释

`Delta_A` 不是新的物理力或熵。它只记录：完整坐标精度观测相较于相关物理动作 residue 子群的基数，需要扩张多少状态。

若动作能够沿各坐标投影独立变化，则 `Delta_A=1`。

若动作坐标高度相关，则即使实际动作轨道很小，完整输出仍会分别读取每个坐标相位，因此 `Delta_A` 可以很大。

## 11. E002-T28 — 单一向量动作闭式

对唯一重复向量动作

\[
a=(a_1,\ldots,a_n),
\]

定义各坐标周期

\[
\boxed{
P_i=\frac{w_i}{\gcd(w_i,|a_i|)}.}
\]

这个 residue 向量本身在直积群中的阶为

\[
\boxed{
|H|=\operatorname{lcm}(P_1,\ldots,P_n).}
\]

但完整向量任意未来精度状态需要

\[
\boxed{
C_\infty=\prod_iP_i.
}
\]

因此

\[
\boxed{
\Delta_A=
\frac{\prod_iP_i}{\operatorname{lcm}(P_1,\ldots,P_n)}.
}
\]

在有限 horizon 下，

\[
\boxed{
C_h=\prod_i\min(h+1,P_i).
}
\]

### 证明

horizon `h` 时唯一可能的 word 总量为 `ka`，其中 `0<=k<=h`。因此第 `i` 坐标在周期闭合前恰好访问 `min(h+1,P_i)` 个不同 residue。应用 T25 即得有限 horizon 公式。所有坐标投影稳定后得到任意未来公式。单一 residue 向量在直积群中的阶就是各坐标阶的 lcm。∎

## 12. 一个无分支执行器产生维数幂精度增长

若全部 `n` 个坐标具有相同周期 `P`，则一个唯一重复的相关动作就有

\[
\boxed{
C_h=\min(h+1,P)^n.
}
\]

其物理 residue 轨道只有 `P` 个向量状态，但完整向量粗商最终需要

\[
\boxed{P^n}
\]

个胞元内类别，并且

\[
\boxed{\Delta_A=P^{n-1}.}
\]

例如

\[
w=(5,5,5),
\qquad a=(1,1,1).
\]

有限 horizon 类别数依次为

\[
\boxed{1,8,27,64,125,125,\ldots}
\]

对应 horizon `0,1,2,3,4,5,...`。动作子群的阶只有 `5`，而完整向量精度划分有 `125` 类，`Delta_A=25`。

这说明：精度义务快速增长并不需要**控制策略分支**；沿着一条确定动作轨道，多维被观测坐标就足以分别暴露各自的边界相位。

## 13. 任务相关的负边界

T25 至 T28 假设未来观测是**完整中心化粗商坐标向量**。

如果任务只观察：

- 某一个坐标；
- 一个 Boolean 条件；
- 类似 norm 的 shell；
- 某个聚合 relation；
- 或者粗商向量的其他 many-to-one 函数，

那么 P023 可能允许更粗的修复。

因此

\[
\prod_i|S_{h,i}|
\]

不是脱离未来语言的普适多维精度定律，而是已声明“完整矩形向量粗商语言”的精确规律。

这个边界必须保留，否则 E002 只会从“过强的统一标量精度”滑向另一个“过强的统一矩形精度”。

## 14. 与可能的 lattice/SNF 推广的关系

一维 gcd 定理很容易诱导出“多维立即换成 Smith normal form”的直觉。T27 说明为什么这个跳跃过早。

Smith/module 不变量描述的是生成动作子群及其 quotient 结构，但完整矩形观测可能需要比子群基数更多的类别，因为它逐坐标读取边界相位。

对于真正的 lattice-shaped 精度胞元或 mixed linear observable，module normal form 仍可能成为正确语言；但必须从已声明 observation map 推导出来，不能靠类比直接导入。

## 15. 可执行审计

实现：

- `src/enterprise_math/precision_vector_actuation.py`

测试：

- `tests/test_precision_vector_actuation.py`

确定性探针：

- `experiments/e002_vector_actuation_probe.py`

仓库 CI 之外的独立有界重建，在一千余组小型 2D/3D 宽度、动作与 horizon 组合上检查了：直接 operation-word signature 类别数与坐标投影乘积公式完全一致。已提交测试还检查：

- 精确矩形重构与向量 carry 运输；
- 单步粗商闭包的逐坐标整除条件；
- coordinate repair rank 与直接未来 signature 的等价；
- `3x3` 对角动作反例 `|S_2|=3` 而 `C_2=9`；
- 逐坐标 gcd 稳定宽度；
- 整数 `Delta_A` 以及独立坐标动作下 `Delta_A=1`；
- 单一向量动作的有限 horizon 与子群阶闭式；
- 三维 `1,8,27,64,125` 精度增长例子。

## 16. 前人工作与新颖性边界

有限循环群直积、坐标投影、子群指数、gcd/lcm 阶公式、矩形量化与乘积 partition 都是成熟数学或工程结构。E002 不把这些工具声称为原创。

当前真正测试的是：在已声明的完整向量有限精度未来语言下，为什么安全修复由“各坐标投影的乘积”决定，而不是由相关动作 residue 集合自身的基数决定。

历史新颖性继续保持 `NOVELTY_UNVERIFIED`。

## 17. 下一批压力测试

下一步高价值目标：

1. 把完整矩形输出替换为 mixed linear/lattice observation，判断何时 subgroup/module 不变量才真正充分；
2. 推导状态相关向量动作 alphabet 与 controller-policy 对可达 residue 图的限制；
3. 把向量 horizon 公式应用到 E001 空间运动/碰撞坐标；
4. 比较精度增长复杂度 `C_h` 与直接 fine-state 模拟成本；
5. 在对物理空间作任何几何声称之前，先测试非矩形有限胞元。
