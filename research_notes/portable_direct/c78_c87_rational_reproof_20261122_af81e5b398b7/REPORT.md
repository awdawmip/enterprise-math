# C78／C87 因数库存的有理化重证：本轮结果与精确边界

日期：2026-11-22（Asia/Hong_Kong）。

用户任务：**“C78／C87 因数库存，你跑下这个的重证试试。”**

本轮从项目原始库存、原传递核与现有证书出发，实际完成数学推导和精确运算。科学输入固定于 `awdawmip/enterprise-math@63eec225728612d1df6c178b516b5ecf4687ee06`；原有理化审计见 `ecddde4b6938b067eae8049f4cef1364d315dc63` 的 `research_notes/portable_direct/rationalization_audit_20261122_af81e5b398b7/REPORT.md`。

## 1. 已经得到的结果

**C78：已闭合原全库存的高覆盖一阶库存桥；另用形式代数重证了所需的有理仿射刚性。C87：已重证辅助位置曲线的排序与定量严格凹性，并构造了有限有理、保持严格形状的计算公式。**

| 环节 | 本轮实际成果 | 仍继承或仍需处理的部分 |
| --- | --- | --- |
| 原有限三尾读数 | 正路径传递与有理分式块逐项相等的有限证明 | 原模型、原三条完整尾、原观察量均沿用 |
| Gamma 比与幂次归一化 | 对所有整数端点成立的有理四次幂乘积包络 | 不宣称极限常数本身属于有理数 |
| 相邻／近库存差商 | 任意阶离散差分、有限 Newton 余项、原读数相对差商界 | 固定极限谱的全部落点方向统一桥尚未拼接完毕 |
| 同步带 | 原有限核上的显式坏安排数量界 | 跨模板的同格碰撞仍是另一命题 |
| C78 高覆盖桥 | 同一个好集对整个允许的整数库存差范围同时有效 | 尚未由此重证原 C78 全部锐识别阈值 |
| 分支仿射刚性 | 在 \(t=1\)、有理系数仿射映射范围内，排除非恒等配对 | 证明使用有限代数扩张和形式级数；不是纯有理数枚举证书 |
| 多项式小值格点 | 由有限 Lagrange 恒等式给出显式有理密度界 | 对实际跨分支函数还须支付消元、分母与非零性连接 |
| C87 位置排序 | 不对位置求导的严格排序与 Jensen 余量 | 继承准确位置恒等式和原核正性证书 |
| C87 有理计算 | 61 段有限公式、全位置误差、指定位置差值区间 | 原有限库存到辅助 Haar 读数的统一误差尚未重证 |

这些是作者侧新推导和核对结果。本轮未申请或冒称独立 Review、Working Truth、Foundation 接纳，也未变更共享任务及权重。

## 2. 原对象保持不变

库存包含两个因子 2、两个因子 3、\(n\) 个因子 5 和一个因子 7；原三态速率为 \(1/4,1,4\)，两种准备为 \(e_u=(7,u,1-u)/8\)，\(u=0,1\)。固定基库存 \(c\)，原安排是

\[
\mathcal T_c=\{(V,W)\in\mathbb Z^2:2\le W\le V\le c\},
\qquad |\mathcal T_c|=\binom c2.
\]

在库存 \(n\ge c\) 上保留同一安排，前缀为

\[
5^{n-V}\,23\,5^{V-W}\,23\,5^{W-2},
\]

后面接完整的 \(557,575,755\) 三条尾。增加库存时，额外的 5 放在第一个 23 之前。每条尾的两准备概率之比记为 \(R_j=P_j(1)/P_j(0)\)，真实读数始终是

\[
g(n,V,W)=H(0,1)=\frac{\max_j R_j}{\min_j R_j}.
\]

定义全有理有限乘积

\[
F_k(N)=\prod_{j=1}^{N}\frac{4j+k}{4(j+k)},\quad
\rho_k(n,s)=4\frac{F_k(n)}{F_k(s-1)},
\]
\[
\tau_k(n,s)=\rho_k(n,s)
\frac{28(4s+k-1)(s+k)^{\overline{3k}}}
{(s+k-1)(n+k+1)^{\overline{3k}}},\qquad
\mathcal B_{n,s,k}(z)=\frac{\rho_k+\tau_kz}{1+\tau_kz}.
\]

其中上升阶乘是有限整数乘积。三条终尾值为

\[
z_j(W)=\frac{a_W(t_W A_j+B_j)}{1+a_Wt_WA_j},
\quad a_W=F_1(W)/F_1(2),\quad
t_W=\frac{840}{(W+2)(W+3)(W+4)},
\]
\[
(A_j,B_j)=(3/32,15/32),(3/2,15/8),(6,3).
\]

本轮从原正状态转移逐块推出

\[
\boxed{R_j=\mathcal B_{n,V,5}\bigl(\mathcal B_{V,W,3}(z_j(W))\bigr).}
\]

完整证明见 [FINITE_KERNEL_PROOF.md](FINITE_KERNEL_PROOF.md)。这一步保留三尾间的共同来源与全部相关关系；未用独立采样替代安排，也未把三尾压成一个未经证明的标量近似。

## 3. 有限乘积包络与离散差商

### 3.1 不经 Gamma 的全整数域包络

令

\[
\eta_k=\frac{5k+4}{8},\qquad
C_k=\frac{|k(16-9k^2)|}{64},\qquad k\in\{1,3,5\},
\]
\[
E_k(m,n)=\frac{C_k}{2}
\left[(m+5k/8)^{-2}-(n+5k/8)^{-2}\right],
\]
\[
Q_k(m,n)=\left[\frac{F_k(n)}{F_k(m)}\right]^4
\left[\frac{n+\eta_k}{m+\eta_k}\right]^{3k}.
\]

对任意整数 \(0\le m\le n\)，已经证明

\[
1\le Q_1\le\frac1{1-E_1},\qquad
1-E_k\le Q_k\le1\quad(k=3,5).
\]

三个误差量分别严格小于 \(7/50,13/30,209/250\)，故分母始终正。证明把单步差写成三对明确整数多项式；在 \(j=y+1\)、\(y\ge0\) 中，它们的全部系数非负。再用有限望远镜和与有限乘积不等式得到结论。完整系数已保存，因而这不是把有限采样外推到全域。

当 \(n=m+b\) 时，还有

\[
\boxed{E_k(m,m+b)\le\frac{C_kb}{(m+5k/8)^3}.}
\]

详见 [FINITE_PRODUCT_BOUND.md](FINITE_PRODUCT_BOUND.md) 及其整数系数证书。固定有限前缀后可包围任意后续库存的归一化量；这里没有宣称极限常数变成了有理数。

### 3.2 直接在整数库存上取差分

记 \(a=3k/4,\ \beta=15k/4\)。对任意有限阶 \(r\ge0\)，

\[
\Delta_n^r\rho_k=(-1)^r\frac{a^{\overline r}}{(n+k+1)^{\overline r}}\rho_k,
\qquad
\Delta_n^r\tau_k=(-1)^r\frac{\beta^{\overline r}}{(n+4k+1)^{\overline r}}\tau_k.
\]

落点方向也有下降阶乘形式的准确差分；混合差分由变量分离相乘得到。对 \(f=\rho_k,\tau_k\)，对应 \( (d,e)=(a,k+1),(\beta,4k+1)\)，有限 Newton 求和给

\[
0\le(-1)^R\left[f(n+b)-\sum_{r<R}\binom br\Delta^rf(n)\right]
\le\binom bR\frac{d^{\overline R}}{(n+e)^{\overline R}}f(n),
\quad b\ge R\ge1.
\]

特别是

\[
0\le\frac nb\left[\frac{f(n+b)}{f(n)}-1\right]+d
\le\frac{de}{n+e}+
\frac{n(b-1)d(d+1)}{2(n+e)(n+e+1)}.
\]

因此 \(b=1\) 的相邻库存也有直接误差控制，不会因先作粗误差再除以 \(b\) 而丢失精度。

对真实 \(g\)，固定内层极端值并按外层单调性排列为 \(u,v\)，有准确恒等式

\[
g-1=\frac{(v-u)\tau(1-\rho)}{(1+\tau v)(\rho+\tau u)}.
\]

内层端点差无论多小都保留在这个式子中，并在相对差商的余项界里准确约消。完整的有理余项证明和常数见 [DISCRETE_JET_PROOF.md](DISCRETE_JET_PROOF.md)。

## 4. C78 本轮的主要新定理：原全库存高覆盖一阶桥

取整数 \(h\ge16,c\ge16\)，定义

\[
\mathcal G_{c,h}=\left\{(V,W)\in\mathcal T_c:
|\rho_5(c,V)-1|>1/h,\quad
|\rho_3(V,W)-1|>1/h\right\}.
\]

**同一个集合与库存差 \(b\) 无关。** 其补集比例满足

\[
\boxed{
\frac{|\mathcal T_c\setminus\mathcal G_{c,h}|}{\binom c2}
\le\frac{41}{10h}+\frac{12}{c}.
}
\tag{4.1}
\]

在好安排上设 \(\rho=\rho_5(c,V),\tau=\tau_5(c,V)\)，内层三值的两个极端按外层单调性排列为 \(u,v\)，定义

\[
\mathcal E_{c,V,W}
=-\frac{75}{4}+\frac{15\rho}{4(1-\rho)}
+\frac{75\tau v}{4(1+\tau v)}
+\frac{15\rho+75\tau u}{4(\rho+\tau u)}\in\mathbb Q.
\]

则对所有整数 \(1\le b\le c/(30h)\)，每个好安排同时满足 \(g(c,V,W)>1,g(c+b,V,W)>1\)，且

\[
\boxed{
\left|
\frac cb\left[
\frac{g(c+b,V,W)-1}{g(c,V,W)-1}-1
\right]-\mathcal E_{c,V,W}
\right|
\le\frac{5405bh}{c}.
}
\tag{4.2}
\]

当 \(c<30h\) 时允许的正整数 \(b\) 范围为空；定理没有掩盖这个边界。常数 \(5405\) 是为完整显式控制选取的保守常数，未做最优化。

证明中的坏安排计数针对**实际有限** \(\rho_5,\rho_3\)。对于有理 \(0<\delta\le1/16\)，

\[
N_{\mathrm{out}}\le(c-1)\left[\frac{11}{10}\delta c+1+\frac4c\right],
\]
\[
N_{\mathrm{in}}\le\frac{200}{243}\delta c(c+1)+c+21+
\frac{325}{162}\sum_{j=1}^{c}\frac1j.
\]

这由第 3 节乘积包络、有限幂差恒等式和整数间距计数得到；没有先把同步带换成极限曲线。三条尾的系数点不共线，行列式为 \(-1215/256\)，保证好集上的内层非盲。允许的 \(b\) 范围保证外层不跨同步点，之后直接接入有理差商余项。

因此，若 \(h\to\infty\) 且 \(bh/c\to0\)，就在原全部安排中得到比例趋一的共同好集，且上面的相对库存响应一致受控。这里逼近的是实际有限系数 \(\mathcal E_{c,V,W}\)；继续接入固定极限谱仍需具体落点控制。

完整证明：[HIGH_COVERAGE_BRIDGE.md](HIGH_COVERAGE_BRIDGE.md)、[SYNCHRONY_COUNT_CHECK.md](SYNCHRONY_COUNT_CHECK.md)。

## 5. 跨分支问题的两个已完成部件

### 5.1 所需仿射刚性已经去掉复解析延拓

在原 \(t=1\) 谱中置 \(r^4=x,s^4=y\)，其有符号归一形式为

\[
R(r,s)=\frac{50176r^6s^{42}(r^9-4s^9)(1-4r^{15})}
{(1+448r^{51}s^9)(1+1792r^{66}s^9)}.
\]

令 \(F(x,y)=R(x^{1/4},y^{1/4})^{12}\)，正域取正根。本轮已证：若可逆**有理系数**仿射映射 \(T\) 在某个非空正域开片上保持 \(F\circ T=F\)，则 \(T=\mathrm{id}\)。

证明先在开片取代数独立点，将等式放入有限代数扩张。若某条原像轴不是坐标轴，在其一般点处原 \(x,y\) 都是单位；四次根由形式系数递推得到普通整数幂级数，任何非零分母的倒数只有整数 Laurent 阶。另一侧沿第一轴必有非零的 \(u^{81}\) 项，沿第二轴必有非零的 \(v^{513}\) 项，而基变量是 \(u^4,v^4\)，产生矛盾。两轴零阶 \(18,126\) 不同，不能互换；最后比较两个多项式系数排除非平凡正缩放。

这已替代所需范围内的复解析芽延拓及小圈分歧论证。**它属于有理基域上的代数重证，仍使用抽象代数扩张、形式级数及代数独立点；不应称为全程只操作有限个有理数的证书。** 也未扩大为任意实参数 \(t\)、任意实系数仿射变换的旧命题。

与原 C78 方向引理的接口已经逐项核对：实际矩阵的两列是整数向量除以正整数，等谱与 Hessian 非退化给 \(S(q)=M^{-1}q\)，所以没有未知实平移，且保持的第一谱确为 \(G_1\)。新定理准确替换该引理最后的仿射刚性矛盾。方向引理前面把不同开片上的梯度恒等式延拓到同一连通逆图的**实解析恒等原理**仍未被替换；不把整个方向引理记为已完成有限有理重证。

完整证明及有限系数核对：[ALGEBRAIC_AFFINE_RIGIDITY.md](ALGEBRAIC_AFFINE_RIGIDITY.md)。

### 5.2 有理多项式小值点的有限格网界

设 \(P\in\mathbb Q[X,Y]\) 非常数，\(d=\deg_XP\)，其最高 \(X\) 次项系数 \(a(Y)\) 的次数为 \(e\)、首项系数为 \(L\ne0\)。记 \(D=d+e\ge1\)，则任意正整数 \(N,h\) 有

\[
\boxed{
\#\left\{0\le i,j\le N:
\left|P\left(\frac iN,\frac jN\right)\right|
\le\frac{|L|}{h^D}\right\}
\le D(N+1)\left(\left\lfloor\frac{2N}{h}\right\rfloor+1\right).
}
\]

相应密度至多 \(2D/h+D/(N+1)\)。证明只用有限个有理节点的 Lagrange 最高系数恒等式；\(d=0,e=0\) 的各自边界已单独处理。这里 \(D\) 不要求等于总次数。

原同步曲线对应 \(1-256x^{15}\) 与 \(x^9-256y^9\)，可直接作用于原 \((V/c,W/c)\) 格点。但对真正跨逆分支的碰撞函数，仍需实际构造非零消元式或有限范数，并控制分母、分支和误差；不能把四次根坐标的均匀网格冒充原库存网格。

完整证明：[POLYNOMIAL_SMALL_VALUE_GRID_PROOF.md](POLYNOMIAL_SMALL_VALUE_GRID_PROOF.md)。

## 6. C87：位置排序的无位置微分证明与有限有理公式

### 6.1 严格凹性直接来自正部核

沿用原 C86 准确位置恒等式与 C87 全域核正性证书，记

\[
C=\frac{16000}{16359\zeta(2)},\qquad
B(x)=A(x)/x^2\ge1/200.
\]

定义

\[
f_\theta(x)=\max\{(1-\theta)x-\theta,\ \theta x-(1-\theta),\ 0\}.
\]

原辅助位置曲线满足

\[
I_{1/2}-I_\theta=C\int_0^1 B(x)f_\theta(x)\,dx.
\]

固定 \(x\)，\(f_\theta(x)\) 是三个仿射函数的最大值，所以有限 max 不等式直接给出凸性。其在有理区间 \([l,h]\) 上的面积由有限断点梯形求和准确算出：

\[
K_{l,h}(\theta)=\frac{1-m}{2}
\left[(h-q)_+^2-(l-q)_+^2\right],
\qquad m=\min(\theta,1-\theta),\quad q=\frac m{1-m}.
\]

对有理端点和有理位置，这完全是有理运算。全段面积为

\[
j_0(\theta)=\frac{(1-2\theta)^2}{2\max(\theta,1-\theta)}.
\]

通过倒数恒等式和跨中点割线斜率比较，已证 \(j_0(\theta)-\theta^2/2\) 凸。结合 \(B\ge1/200\)，任意 \(0\le a<b\le1,0<\lambda<1,z=\lambda a+(1-\lambda)b\) 有

\[
\boxed{
I_z-\lambda I_a-(1-\lambda)I_b
\ge\frac C{400}\lambda(1-\lambda)(b-a)^2
>\frac1{800}\lambda(1-\lambda)(b-a)^2.
}
\]

最后一步仅需有理尾界给 \(\zeta(2)<7/4\)，进而 \(C>1/2\)。因此中点唯一最大，左半段严格递增，右半段严格递减；两个**辅助端点**等值最小。这一位置排序论证无需对位置求导、支配收敛或微积分基本定理。

### 6.2 实际编译出的有限公式

原证书提供 \([1/8,1]\) 上 60 个有理区间界。本轮加上已有轴展开导出的 \([0,1/8]\) 界 \(1/40\le B\le1/2\)，形成 61 段。用 64 项有理和及望远镜尾界包围 \(\zeta(2)\)，得到

\[
0.59454218<C<0.59462908.
\]

对每段取有理中值 \(b_i=(L_i+U_i)/2\)，共同常数取包围区间中值 \(C_0\)，定义

\[
\boxed{\widehat I_\theta=-C_0\sum_i b_iK_i(\theta),\qquad
\widehat I_{1/2}=0.}
\]

这个有限公式在全部有理位置上保持反射对称、严格排序和定量严格凹性。原中心化曲线与它的全位置误差由保存的确切有理数控制，本轮粗分段界约为 \(0.003922306486278024\)，严格小于 \(0.003923\)。这不是原有限库存的误差界。

直接对非负差核求和，已经算出以下**有理外扩区间**：

| 原辅助曲线的差值 | 严格包含它的区间 |
| --- | --- |
| \(I_{1/2}-I_{1/10}\) | \((0.0024153,\ 0.0061936)\) |
| \(I_{1/2}-I_{1/4}\) | \((0.0010553,\ 0.0024626)\) |
| \(I_{1/4}-I_{1/10}\) | \((0.0013600,\ 0.0037310)\) |
| \(I_{1/2}-I_0\) | \((0.0035657,\ 0.0114098)\) |

这些十进端点都是有限有理数；JSON 中保存更紧的完整分数。现成证书的旧仿射求积可比本次常值段公式更窄，本轮目的在于给出简单且保持严格形状的有理接口。

完整推导：[C87_POSITION_PROOF.md](C87_POSITION_PROOF.md)。准确积分恒等式、核正性及其既有分析来源仍是输入；本轮没有把整条 Haar 模型或整段原库存极限桥宣布为纯有理重证。

## 7. 实际运行的检查

| 检查对象 | 实际覆盖与结果 |
| --- | --- |
| 正状态路径与闭式分式核 | 基库存 \(c=2,\ldots,12\) 的全部 286 个模板；706 个不同库存／模板组合；2,118 个单尾精确等式全部通过；两准备的完整三尾质量分割通过 |
| 有限乘积 | 三对整数多项式的全部系数证书通过；\(k=1,3,5\)、\(0\le m\le n\le64\) 共 6,435 项精确包络检查通过 |
| 差分与 Newton | 库存差分 5,130；落点差分 4,506；Newton 余项 10,260；真实读数 Euler 比值 60；辅助端点比值 90，共 20,046 项通过 |
| 实际有限同步带 | \(c=16,\ldots,64\)，五个有理带宽，共 245 个完整参数案例；全安排直接计数及中间包络均通过 |
| 多项式小值格网 | 六个非零多项式、三种有理阈值，共 18 个精确格网实验通过；包含达到等号的例子 |
| 形式代数刚性 | 两轴的首非整数修正系数、不同零阶、对角缩放两项系数全部精确核对通过 |
| C87 位置公式 | 61 段覆盖检查；610 次面积公式与独立断点梯形法逐分数相等；10 个位置的包围／对称检查；4 个 Jensen 余量检查通过 |

库存及位置核验使用 Python `fractions.Fraction` 和任意精度整数；代数刚性的有限系数核验使用 SymPy 的准确符号算术。浮点只用于个别输出的十进展示，不参与接受条件。全称命题由各证明文件承担；有限运行用于核对符号、端点、下标、系数和实现，未被用来替代证明。

本轮未重跑原巨量库存枚举、原 293,423 次根检查或完整径向求积，也未把旧输出计入新运行次数。

## 8. 怎样复算

在项目仓库中进入本目录，运行：

```bash
python verify_exact_inventory.py
python finite_product_bridge.py
python check_discrete_jets.py
python check_synchrony_counts.py
python verify_polynomial_grid_bound.py
python check_algebraic_affine_rigidity.py
python rational_position.py
```

前五项与位置脚本只依赖 Python 标准库；形式系数脚本需要 SymPy。两个只向标准输出报告的脚本为 `check_discrete_jets.py`、`check_synchrony_counts.py`，其本轮输出另存为同名 JSON。其他脚本在本目录保存结果。

`rational_position.py` 默认读取项目原 C87 目录中的 `integrated_kernel_certificate.json`；也接受该固定证书的路径作为第一个参数。输入 blob 为 `4269238343a4eb5815fb048ffd0dd59b9e4fc280`。单独下载本目录时，应另外提供该原证书；本轮未重复发布原证书。

位置脚本会检查输入文件的准确 Git blob。整合时以原始字节证书再次运行，输出的数学结果与前一次全部相同；前一临时副本仅多了末尾空行，解析后的内容完全一致。

## 9. 尚待闭合的具体数学问题

**C78：** 已有真实有限读数的一阶库存桥、有理基域上的仿射刚性、多项式小值格点界。要完成原锐识别结论，还需把实际不同逆分支的近碰撞函数连接到明确非零的代数消元式，控制它的分母、退化 Hessian、逆分支及有限差误差，并对全部库存格点和舍入平移保留原量词。现有三个部件并不自动合成为同格竞争者的零密度定理。

**C87：** 已有辅助曲线上的严格位置差距及其有理区间。还需要原库存识别比例到辅助函数的显式统一误差，并与高精度尾余项一起小于指定位置的差距。尤其位置接近端点、候选网格增长、精度与库存联动时，须保留原桥的具体量词。本轮已经获得可用于比较的正差距，尚未为任意指定有限库存认证最优位置。

下一处可直接接续的对象是 C78 实际跨逆分支方向函数的非零消元／范数证书，而非再做一遍原小库存读数计算。

## 10. 原始来源及工作身份

以下路径均位于固定提交 `63eec225728612d1df6c178b516b5ecf4687ee06`：

| 原来源 | Git blob |
| --- | --- |
| `research_notes/divisor_extrema/20261116_c78_nearby_stock_precision/C78_RESEARCH_NOTE.md` | `3b826830d8a1f319558d4ec4c44b5cc59634ef45` |
| 同目录 `critical_bins.py` | `b6a44aa43e9db28332be6a7b6deb3a6aac4877ca` |
| 同目录 `check_finite.py` | `e1f56a2569d7bcefab2dfc2c01cd991a87151d94` |
| 同目录 `SHARP_NEAR_STOCKS.md` | `41d996898817258383a4232262540f5629b88059` |
| 同目录 `LOCAL_ADJACENT.md` | `a2259ca801cccf447083fb4449537d354fba393e` |
| `research_notes/divisor_extrema/20261116_c77_arbitrary_stock_pairs/TWO_STOCK_PRECISION.md` | `dd67713b07026321ffc706f2c510ced697b2ba67` |
| `research_notes/divisor_extrema/20261121_c87_global_position_ordering_and_complete_triangle_integral/C87_RESEARCH_NOTE.md` | `9f8575a2d9d654f9f11068123fe02cb8e1d0441a` |
| 同目录 `positions/GLOBAL_POSITION_THEOREM.md` | `ace988b74f301e6937570dbab8b4deb727e49924` |
| 同目录 `INTEGRATED_KERNEL_PROOF.md` | `40b327ba8a5ec56544d1166c605af78ea960cabe` |
| 同目录 `integrated_kernel_certificate.json` | `4269238343a4eb5815fb048ffd0dd59b9e4fc280` |

全局入口读取快照：`awdawmip/chatgpt-global-knowledge@b07b5f1ba2257af9cada385acabbb20ecab9ce62`。本轮沿已验证 Driver 身份处理用户指定的数学依赖，普通研究保存依据项目现行自治与持久化规则。

Driver-ID: `EM-DVR-2D6C6F / CONTROL_PLANE`。
Session: `MCP-d6362c0d7d31434e82af45c5e425dc26`。
Driver Authority: `DA-F510B2698ACA7B1E8F0B`。

同上下文协作来源：`inventory_exact_model`（原有限核与小值格网核对）、`c78_rational_bridge`（离散差分、同步计数和高覆盖桥）、`c87_rational_position`（位置证明及代数刚性）；主会话完成有限乘积证书、证明整合、范围核对及保存。以上均为作者侧工作，不构成独立项目 Review。
