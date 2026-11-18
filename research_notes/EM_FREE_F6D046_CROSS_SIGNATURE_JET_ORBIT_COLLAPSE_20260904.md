# 跨 signature 的一阶喷流轨道坍缩、方程刚化与二次模对应阻碍

Status: `FREE_RESEARCH / DERIVED_NO_GO / PRIOR_ART_METHOD_SPECIALIZATION / NOT_AXIOM / NOT_FOUNDATION`

Date: `2026-09-04`

Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`

Parent candidate: `EM-FREE-F6D046-C1-ROTATIONAL-PERIOD-WRONSKIAN`

Research unit: `EM-FREE-F6D046-R2-CROSS-SIGNATURE-JET-ORBIT`

Blindness status: `ANCHOR_EXPOSED / PHASE-B CONTINUATION`

Author/program signature: `YUAN X / Enterprise Math`

## 0. 本轮结论

前一阶段留下的最小未完成单元是：选择至少两条不在同一已知二次变换轨道中的 Ramanujan–Sato 公式，构造标准喷流协向量，并寻找对偶喷流群胚的轨道不变量。

本轮得到一个正反两面的闭合结果：

1. 选取了 signature `s=4`、level `ell=2` 的 Ramanujan degree-29 公式，以及 signature `s=3`、level `ell=3` 的 degree-23 公式；两者都写成标准的一阶喷流协向量。
2. 证明：若允许任意局部解析重参数化和任意非零标量规范，那么在固定非零标量值下，所有 `B != 0` 的一阶公式都在同一轨道。也就是说，`(A,B)`、`A/B`、底数正负、level、degree 和 signature 都不能从裸一阶喷流轨道中恢复。
3. 因此，原先设想的“从一阶系数对直接提取跨 level 轨道不变量”在不加限制时必然坍缩；这不是计算尚未完成，而是一个精确 no-go 定理。
4. 把周期微分方程及其局部单值性加入对象后，轨道重新变得非平凡。对二次方程保持型拉回，唯一椭圆局部单值的阶的奇数部分是链式轨道不变量。
5. level-2 公式的该阶为 `2`、奇数部分为 `1`；level-3 公式的该阶为 `3`、奇数部分为 `3`。故二者不可能由任何二次方程拉回链连接。
6. 该结论是链式法则、超几何局部指数与标准拉回规律的派生结果，不构成新公理。真正保留下来的新研究信息是：**Ramanujan 喷流必须与其周期局部系统共同类型化；只保留点值喷流会把 signature 信息彻底抹除。**

## 1. 两条跨 signature 公式

统一记

\[
F_a(z)={}_3F_2\!\left(\frac12,a,1-a;1,1;z\right),
\qquad
\Theta_z=z\frac{d}{dz}.
\]

前一阶段的 Wronskian 归一化为

\[
J_a=\frac{\sin(\pi a)}{\pi}.
\]

### 1.1 signature `s=4` / level `ell=2`

取

\[
a_2=\frac14,
\qquad
z_2=99^{-4}=\frac1{96059601}.
\]

标准 Wronskian 协向量为

\[
\boxed{
J_{1/4}=\left(\frac{2206}{9801}+\frac{52780}{9801}\Theta_z\right)F_{1/4}(z_2).
}
\]

其 `1/pi` 归一化为

\[
\boxed{
\frac1\pi=\left(\frac{2206\sqrt2}{9801}+\frac{52780\sqrt2}{9801}\Theta_z\right)F_{1/4}(z_2).
}
\]

记

\[
d_2=\left(\frac{2206\sqrt2}{9801},\frac{52780\sqrt2}{9801}\right).
\]

### 1.2 signature `s=3` / level `ell=3`

Guillera 证明的 degree-23 公式是

\[
\sum_{n=0}^{\infty}\frac{(\tfrac12)_n(\tfrac13)_n(\tfrac23)_n}{(1)_n^3}(14151n+827)\frac{(-1)^n}{500^{2n}}=\frac{1500\sqrt3}{\pi}.
\]

令

\[
a_3=\frac13,
\qquad
z_3=-500^{-2}=-\frac1{250000}.
\]

则其 Wronskian 归一化为

\[
\boxed{
J_{1/3}=\left(\frac{827}{3000}+\frac{14151}{3000}\Theta_z\right)F_{1/3}(z_3).
}
\]

其 `1/pi` 归一化为

\[
\boxed{
\frac1\pi=\left(\frac{827}{1500\sqrt3}+\frac{14151}{1500\sqrt3}\Theta_z\right)F_{1/3}(z_3).
}
\]

记

\[
d_3=\left(\frac{827}{1500\sqrt3},\frac{14151}{1500\sqrt3}\right).
\]

对应奇异点可取

\[
\alpha_3=\frac12-\frac{53\sqrt{89}}{1000},
\qquad
\beta_3=1-\alpha_3,
\]

且

\[
4\alpha_3\beta_3=1-\frac{4\cdot53^2\cdot89}{1000^2}=-\frac1{250000}=z_3,
\]

由 `4*53^2*89=1000004` 精确得到。

## 2. 裸一阶喷流群胚

设 `F_1`、`F_2` 分别是在非零基点 `z_1`、`w_2` 附近的非零解析函数芽，并且 `F_1(z_1)F_2(w_2) != 0`。定义

\[
j_1=\binom{F_1}{\Theta_zF_1}_{z=z_1},
\qquad
j_2=\binom{F_2}{\Theta_wF_2}_{w=w_2}.
\]

一个不受限制的局部解析箭头由局部双全纯重参数化 `z=phi(w)`、非零解析规范 `g(w)` 以及

\[
F_1(\phi(w))=g(w)F_2(w)
\]

组成。令

\[
\kappa_0=\frac{\phi(w_2)}{w_2\phi'(w_2)}.
\]

链式法则给出

\[
\boxed{
j_1=Tj_2,
\qquad
T=\begin{pmatrix}g_0&0\\ \kappa_0\Theta_wg_0&\kappa_0g_0\end{pmatrix}.
}
\]

若 `K=c_1j_1`，则协向量运输为 `c_2=c_1T`。

## 3. 一阶归一化轨道坍缩定理

### 定理 3.1 — `B != 0` 轨道的传递性

设

\[
K=c_1j_1=c_2j_2\ne0,
\qquad
c_i=(A_i,B_i),
\]

且 `F_i != 0`、`B_1B_2 != 0`。则存在一个上述局部解析箭头，使

\[
\boxed{c_2=c_1T.}
\]

**证明。** 令

\[
g_0=\frac{F_1(z_1)}{F_2(w_2)},
\qquad
\kappa_0=\frac{B_2}{B_1g_0}.
\]

选择局部双全纯芽满足

\[
\phi(w_2)=z_1,
\qquad
\phi'(w_2)=\frac{z_1}{w_2\kappa_0},
\]

再定义

\[
g(w)=\frac{F_1(\phi(w))}{F_2(w)}.
\]

由构造，`c_1T` 与 `c_2` 的第二分量相同。又有

\[
c_1Tj_2=c_1j_1=K=c_2j_2.
\]

二者之差为 `(D,0)`，故 `D F_2(w_2)=0`；由 `F_2(w_2) != 0` 得 `D=0`。证毕。

### 定理 3.2 — 轨道全集

固定 `K != 0` 时，归一化一阶公式恰分成两个轨道：

\[
\boxed{\{B=0\}\sqcup\{B\ne0\}.}
\]

`B=0` 在可逆下三角变换下保持；两个 `B=0` 公式仍可用 `g=F_1\circ\phi/F_2` 相互运输。故裸一阶喷流至多保留

\[
\boxed{(K,\mathbf 1_{B\ne0})}.
\]

于是 `A`、`B`、`A/B`、`z_0`、底数正负、degree、level、signature 都不是不受限制的一阶轨道不变量。

## 4. level-2 到 level-3 的显式人为箭头

120 位十进制验证给出

\[
T_{2\to3}\approx
\begin{pmatrix}
1.0000004454198582571&0\\
3.1883712677585530\times10^{-7}&0.7151896980349726470
\end{pmatrix},
\]

并满足

\[
\boxed{d_2T_{2\to3}=d_3}.
\]

对应 `A` 残差约为 `10^-120`，`B` 残差为十进制零。这个箭头由

\[
g(w)=F_{1/4}(\phi(w))/F_{1/3}(w)
\]

人为制造，只是函数芽等价；它不保持超几何方程、模参数化或全局单值性。其意义是证明：只要求一阶喷流相容时，箭头类别过宽，轨道分类必然失去内容。

## 5. 最小刚化：保留周期微分方程

令

\[
\mathcal H_a:\quad x(1-x)y''+(1-2x)y'-a(1-a)y=0.
\]

其正则奇点局部指数对为

\[
0:\{0,0\},\qquad 1:\{0,0\},\qquad \infty:\{a,1-a\}.
\]

故无穷远的项目化局部单值比为

\[
\rho_a=\exp(2\pi i(1-2a)).
\]

记其阶为

\[
\nu(a)=\operatorname{ord}(\rho_a).
\]

若坐标拉回在目标点的分歧指数为 `e`，局部指数差乘以 `e`；标量规范只给全部指数加同一数。因此

\[
\rho\mapsto\rho^e,
\qquad
\boxed{\nu\mapsto\frac{\nu}{\gcd(\nu,e)}}.
\]

## 6. 二次拉回链的奇数阶不变量

二次拉回只有 `e in {1,2}`。在当前“两个抛物点加一个椭圆点”的 Gauss 系统族中，非平凡椭圆点必须位于源椭圆点上方。于是沿二次箭头，`nu` 只能保持或除以 `2`；逆向遍历只可能补回一个 `2` 因子。

定义

\[
\boxed{\Omega_2(\mathcal H_a)=\operatorname{oddpart}(\nu(a)).}
\]

### 定理 6.1

`Omega_2` 在由二次方程保持型拉回、标量规范及其逆关系生成的连接分支上保持不变。

对 `a=1/4`，

\[
1-2a=\frac12,
\quad
\rho=-1,
\quad
\nu=2,
\quad
\boxed{\Omega_2=1}.
\]

对 `a=1/3`，

\[
1-2a=\frac13,
\quad
\rho=e^{2\pi i/3},
\quad
\nu=3,
\quad
\boxed{\Omega_2=3}.
\]

因此

\[
\boxed{\Omega_2(\mathcal H_{1/4})\ne\Omega_2(\mathcal H_{1/3}).}
\]

故两条公式不在同一二次方程拉回分支中。更强地，不存在任一方向的直接有限分歧拉回：阶 `2` 元素的幂只有阶 `1` 或 `2`，阶 `3` 元素的幂只有阶 `1` 或 `3`。

这不排除通过第三个局部系统形成共同覆盖 span；共同覆盖不是一个方程到另一个方程的单向标量拉回，必须另行研究双向传输与 holonomy。

## 7. Clausen 秩三方程的独立回归

`F_a` 满足

\[
\mathcal L_aF=\left[\Theta^3-z(\Theta+\tfrac12)(\Theta+a)(\Theta+1-a)\right]F=0.
\]

局部指数为

\[
0:\{0,0,0\},\qquad
1:\{0,\tfrac12,1\},\qquad
\infty:\{a,\tfrac12,1-a\}.
\]

无穷远指数两两差对应的项目化本征值比阶为

\[
a=\frac14:\ [2,4,4],
\qquad
a=\frac13:\ [3,6,6].
\]

对 `a=1/4` 的全部奇点施加 `e=1,2` 后只可能出现

\[
[1,1,1],\ [1,2,2],\ [2,4,4],
\]

不含 `[3,6,6]`。反向，对 `a=1/3` 只可能出现

\[
[1,1,1],\ [1,2,2],\ [3,3,3],\ [3,6,6],
\]

不含 `[2,4,4]`。这独立确认两个方向都不存在二次秩三方程拉回。

## 8. 三层轨道对象

必须区分：

1. 裸点值喷流
   \[
   \mathfrak J^{(1)}=(F(z_0),\Theta F(z_0),c,K);
   \]
2. 方程刚化喷流
   \[
   \mathfrak J^{\rm eq}=(\mathcal H_a,\mathcal L_a,F,z_0,c,K);
   \]
3. 模对应/共同覆盖：再保留模参数、覆盖方向、degree、乘子、分歧图和全局回路。

因此

\[
\boxed{
\text{POINTWISE JET EQUIVALENCE}
\ne
\text{DIFFERENTIAL-EQUATION EQUIVALENCE}
\ne
\text{MODULAR CORRESPONDENCE}.
}
\]

## 9. 对 P000 六维粘合的影响

本轮没有推出新的六维 P000 公理，而是收紧了输入边界：

- 孤立点 `(A,B)` 或下三角矩阵不能区分任何 `B != 0` 的归一化公式；
- 切片对象至少必须携带周期局部系统或等价的项目化单值类型；
- level 2 与 level 3 不能由二次自然变换直接粘合；
- 共同覆盖若存在，必须给出 span 两侧拉回、共同覆盖上的协向量比较与回路 holonomy；
- 前一阶段的四维补空间欠定性仍然存在。

故最小输入满足

\[
\boxed{
\text{P000 SLICE GLUING INPUT}
\supseteq
\text{JET}+\text{EQUATION/LOCAL-SYSTEM PROVENANCE}+\text{CORRESPONDENCE DIRECTION}.
}
\]

## 10. 公理门与工具复用

分类：

`DERIVED_NO_GO / PRIOR_ART_METHOD_SPECIALIZATION / NOT_NEW_AXIOM / NOT_FOUNDATION`。

父候选继续保持 `REJECT_AS_NEW_AXIOM / DERIVED_NOT_AXIOM`，不重新开启候选门。

工具审计：

- `T9_HOLONOMY_COCOYCLE_GLUING`：`REUSE_APPLIED`；保持“holonomy 不自动选择唯一修复对象”的硬边界。
- `T7_FINITE_SYMMETRY_EQUIVARIANCE`：`NOT_APPLICABLE`；本题作用对象是无限局部解析伪群/拉回范畴，不越界使用有限群枚举。
- 当前 registry、method inventory 及 `main` 可搜索执行面未命中专门的 Ramanujan/超几何喷流工具；验证器分类为 `RESULT_ONLY`，不建立新全局工具家族。

## 11. 验证与后继

运行：

```bash
python scripts/verify_em_free_f6d046_cross_signature_jet_orbits.py
```

共 `20` 项检查全部通过，包括两条公式、显式一阶箭头、秩二单值阶、二次链奇数部分和秩三双向拉回阻碍。

下一前沿是共同覆盖 span：构造或排除最小 degree 的共同覆盖，把两条 `1/pi` 协向量拉到共同局部系统，并判断它们相等、只差规范，还是形成非平凡 holonomy。

## 参考来源

1. J. Guillera, *Proof of a rational Ramanujan-type series for 1/pi. The fastest one in level 3*, arXiv:1811.01200, formula (3).
2. J. Guillera, *The fastest series for 1/pi due to Ramanujan. Proofs from modular polynomials*, arXiv:1911.03968.
3. NIST DLMF, Sections 15.10 and 16.8.
4. R. Vidunas, *Transformations of some Gauss hypergeometric functions*, arXiv:math/0310436.
