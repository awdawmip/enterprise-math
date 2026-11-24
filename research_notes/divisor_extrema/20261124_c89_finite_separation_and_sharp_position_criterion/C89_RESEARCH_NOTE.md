# C89　有限分离的真实损失与三库存位置的锐门槛

日期：2026-11-24。延续原三态因子路径及原观察者 \(H(0,1)\)。

## 本轮结果

**C89 把 C88 的三库存移动位置充分条件提升为充要条件。**
在临界倍率保持于固定正紧区间、外端间距满足
\(c^{1/3}\ll B\ll c\) 时，原全库存唯一率能追踪单支 Haar 曲线，当且仅当

\[
\boxed{\frac{A(B-A)}{\sqrt{cB}}\longrightarrow\infty,}
\qquad\text{等价于}\qquad
\boxed{\frac{\min(A,B-A)}{\sqrt{c/B}}\longrightarrow\infty.}
\]

关键的新步骤是证明一对实际远隔分支的联合整数格极限。
当中间库存靠近外端，且距离只相当于 \(\tau\sqrt{c/B}\)、\(\tau<\infty\) 时，
真实的远支整数竞争者留下严格正比例损失。这个结论对全部舍入格原点一致，
并能利用一条新发现的三谱相同正规弧，把损失下界量化到至少倒数级。

本轮还证明了更强的全库存下界、小分离二次增益、低精度下的 \(\tau/L\) 过渡，
以及三个准确库存读数在 Gamma 实落点延拓中的不同原像。
详细证明、准确有理核验与项目内交叉核查随本报告保存。

## 1. 共同模型和符号

原整数目录与全部竞争安排为

\[
2\leq w\leq v\leq c,\qquad N_c=\binom c2.
\]

读取库存 \(c,c+A,c+B\)，其中 \(1\leq A<B\)。增加的因子 5 都在第一次
23 更新之前。每次读取保留 \(p\) 个二进制小数位，三个舍入格原点
\(\alpha\in\mathbb T^3\) 可以各自平移并随库存改变。
原整数安排、路径更新次序和观察者均保持；连续源坐标及 Haar 格是辅助计数表示。

记

\[
D=\sqrt{c/B},\quad \theta=A/B,\quad
p_*(c,B)=\frac74\log_2c+\frac12\log_2(c/B),\quad
L_c=2^{p-p_*(c,B)}.
\tag{1}
\]

主判据的精度范围为 \(0<L_-\leq L_c\leq L_+<\infty\)。
它不要求位数取整后 \(L_c\) 收敛。

沿用原有限谱的极限

\[
F=(G,B_1),\qquad B_1=-(E+3/4)G,\qquad
B_2=-(E+7/4)B_1,
\]

其中 \(E=X\cdot\nabla\)、\(X=(v/c,w/c)\)，
\(\Delta=\{0<y<x<1\}\)、\(J(X)=|\det DF(X)|\)。
几乎处处的完整 \(F\) 纤维有至多六个正规原像；连续宏观原像相同与原整数
读数碰撞始终分别处理。

对余体积为 \(a\) 的 Haar 格和三个独立均匀相位，使用标记
\((u,(1-\theta)u+\theta v,v)\) 的唯一概率记作 \(F_\theta(a)\)。
单支曲线是

\[
\Phi_\theta(L)=2\int_\Delta F_\theta(L^2J(X))\,dX.
\tag{2}
\]

端点处保留三个独立相位，已有

\[
F_0(a)=2\int_0^1\ell F_2(a/\ell)\,d\ell,\qquad \Phi_1=\Phi_0.
\tag{3}
\]

这里 \(F_2\) 为两标记 Haar 格函数。固定有限正 \(L\) 的 \(\Phi_\theta(L)\)
通常小于一；本轮判据判断达到这条临界曲线的条件。

## 2. 三库存移动位置的完整充要判据

**定理 1。** 假设

\[
c^{1/3}\ll B\ll c,\qquad 1\leq A<B,
\qquad 0<L_-\leq L_c\leq L_+<\infty.
\]

则

\[
\boxed{
\sup_{\alpha\in\mathbb T^3}
|V_c^{\rm full}(\alpha)-\Phi_{A/B}(L_c)|\to0
\iff
R_c:=\frac{A(B-A)}{\sqrt{cB}}\to\infty.
}
\tag{4}
\]

若 \(R_c\) 不趋于无穷，必有一条子列及 \(\varepsilon>0\)，使全部格原点
上的唯一率都至少比相应曲线低 \(\varepsilon\)。

充分性继承 C88。必要性的归约很短：
\(\ell=D^3/c\to0\)，而 \(R_c=\theta(1-\theta)/\ell\)。
有界 \(R_c\) 子列只能趋近 \(\theta=0\) 或 \(1\)，此时最近端点的间距除以
\(D\) 有界。第 3 节证明每个这种有限分离都保留真实正损失，因而排除追踪。
完整论证见 [锐门槛证明](root/SHARP_MOVING_POSITION_CRITERION.md)。

一个同精度例子：取 \(B=\lceil\sqrt c\rceil\)，于是
\(D\sim c^{1/4}\)、\(p_*=2\log_2c+o(1)\)。

| 中间增量 \(A\) | 分离尺度 | 临界窗口结论 |
|---|---|---|
| \(1\) | \(A/D\to0\) | 与端点曲线保持正距离 |
| \(\lceil\kappa c^{1/4}\rceil\)，固定 \(\kappa>0\) | \(A/D\to\kappa\) | 仍与端点曲线保持正距离 |
| \(\lceil c^{1/4}\log\log c\rceil\) | \(A/D\to\infty\) | 原点一致追踪 \(\Phi_0(L_c)\) |

三行使用相同的原目录、外端库存和精度。改变的是中间库存与最近外端的距离。

## 3. 从远支允许窗口到真实整数竞争者

### 3.1 一对分支的联合极限

设 \(\theta\to0\)、\(A/D\to\tau<\infty\)、\(L_c\to L>0\)。
在固定正规源片上选一个不同的宏观逆支 \(Y=T(X)\)，使 \(F(Y)=F(X)\)。
源支与远支的准确有限格为

\[
\Lambda_{0,c}=M_c(X)\mathbb Z^2,
\qquad
\mathcal A_{1,c}=M_c(T_cX)(\mathbb Z^2-cT_cX),
\]

\[
M_c(Y)=L_c S\operatorname{diag}(D,D^{-1})\mathsf B_c(Y),
\quad S=\begin{pmatrix}1&0\\1&1\end{pmatrix},
\quad \mathsf B_c=\begin{pmatrix}\nabla U_c\\\nabla P_c\end{pmatrix}.
\tag{5}
\]

当两支的主谱梯度斜率对源坐标横截时，本轮证明：源支线性 Haar 格、远支
仿射 Haar 格及三个均匀源相位具有乘积联合极限。
这个独立性是从准确有限模型证明出来的。

证明分四步。

1. 两个斜率作局部坐标，两个扩张 horocycle 均值给格形状的 Haar 乘积。
2. 在源坐标的 \(D^{-2}\) 尺度上微移，得到两条 horocycle 与相位差圆周的
   联合不变性；Haar horocycle 的混合性消去非零圆周特征函数。
3. 在原整数源标签中作 Gaussian 加权的短格平移，准确重指标化给远支平移与
   首末相位的环面平稳核。这一步使用 \(D^3/c\to0\)。
4. 对两个独立 Haar 格，环面上的非零整数共振几乎处处不存在，平稳测度因而
   唯一为均匀乘积测度。

新增的外部动力系统输入为 Ratner 1987 的 Haar horocycle 混合性；本轮只用其
定性结论。[原论文](https://doi.org/10.1017/S0143385700004004)。
完整证明见 [双支联合格](joint/PAIR_LATTICE_LIMIT.md)。

### 3.2 原谱上确实满足横截性

两处负载核验使用原有理谱及准确 Fraction 区间：

| 正规目标，\(u=G/C_*\) | 已证的约化双斜率行列式区间 |
|---|---|
| \(h=0,u=1/10\)：完整纤维恰有两个正瓣原像 | \(9/1000<\det_{\rm red}<1/100\) |
| \(h=0,u=1/250\)：左负瓣折叠两支 | \(-20<\det_{\rm red}<-19\) |

被约去的两个行因子都严格为正，所以这两个区间证明行列式非零。
左负瓣两支在连通解析目标域 \(h<4,0<u<M_-(h)\) 上延续，故其横截性在
整个该域几乎处处成立。核验方法与实际程序见
[证书说明](joint/DOUBLE_SLOPE_CERTIFICATE.md)及
[准确程序](joint/certify_double_slope.py)。

### 3.3 成对唯一率的完整公式

令 \(E_2(s)\) 为余体积 \(s\) 的仿射 Haar 格避开单位方格的概率。
定义

\[
a_0=L^2J(X),\qquad a_1=L^2J(TX),\qquad
h=\frac{L\tau}{2}[B_2(TX)-B_2(X)],
\]

\[
w_a(d)=(1-|d|)F_2\!\left(\frac a{1-|d|}\right),\qquad
\ell_h(d)=(1-|d-h|)_+.
\tag{6}
\]

仅保留源支与该远支时，准确极限唯一概率为

\[
\boxed{\mathcal U_\tau(X)=
\int_{-1}^1 w_{a_0}(d)
E_2\!\left(\frac{a_1}{\ell_h(d)}\right)dd.}
\tag{7}
\]

\(\ell_h=0\) 时第二因子取一。真实远支造成的成对损失满足

\[
\boxed{F_0(a_0)-\mathcal U_\tau(X)>0\iff |h|<2.}
\tag{8}
\]

在 \((h,u)=(0,1/10)\) 附近的开放目标区，完整纤维恰好只有两支，(7)
就是允许全库存竞争者的完整区域极限，并且与三个格原点无关。
在更多分支的区域，保留一条真实远支已足以证明全库存唯一率的严格损失。

## 4. 有限分离留下的缺口：正性与速率

**定理 2。** 在端点条件 \(\theta\to0\)、\(A/D\to\tau<\infty\)、
\(L_c\to L>0\) 下，存在 \(c_L>0\)，使

\[
\boxed{
\Phi_0(L)-\limsup_{c\to\infty}\sup_\alpha V_c^{\rm full}(\alpha)
\geq c_L\min\{1,\tau^{-1}\}.}
\tag{9}
\]

\(\tau=0\) 时右侧解释为 \(c_L\)。该常数与 \(\tau\) 无关；在 \(L\) 的固定
正紧区间可以统一取正。末端的对应结论用 \((B-A)/D\) 代替 \(A/D\)。

第 6 节构造一条正规三谱相同弧。在它的一条固定紧子弧附近，源支与配对支的
\(J\) 有正下界，且 \(|\Delta B_2|\leq C\times\text{到该弧的距离}\)。
宽度为 \(1/\tau\) 量级的管中，(7) 的远支碰撞概率有统一正下界。
积分这一管状区域，便得到 (9)。这一步将谱几何真正转移到了原整数碰撞。

另一方面，最近非零跨支 \(B_2\) 差是正几乎处处的半代数函数。本轮证明其
小值集合具有某个幂次面积界，因此存在只依赖原谱的 \(C,\eta>0\)，使

\[
\boxed{
\Phi_0(L)-C\min\{1,(L\tau)^{-\eta}\}
\leq\liminf_c\inf_\alpha V_c^{\rm full}(\alpha).}
\tag{10}
\]

这里尚未计算 \(\eta\) 的具体值。(9)–(10) 都先对每个固定有限 \(L,\tau\)
取库存极限；没有给 \(c\) 与 \(\tau\) 同时发散时的误差率。
证明见 [代数误差界](spectral/CURVATURE_AND_ALGEBRAIC_TAIL.md)及
[双支联合格第 8 节](joint/PAIR_LATTICE_LIMIT.md)。

## 5. 保留源相位后，更强的全库存下界

这一部分对所有宏观分支同时成立，而无需假定它们彼此独立。

对源 \(X\)，把其他纤维点的 \(B_2\) 值与源比较，记最近的上方、下方谱差为
\(\delta_+,\delta_-\)；缺失的一侧取 \(+\infty\)。置
\(h_\pm=L\tau\delta_\pm/2\)，缺失侧仍取无穷。
能排除全部远支的相位差区间为

\[
\mathcal C_X=[\max(-1,1-h_-),\ \min(1,h_+-1)].
\tag{11}
\]

若下端不小于上端，积分取零。定义

\[
\boxed{\mathcal B_\tau(L)=
2\int_\Delta\int_{\mathcal C_X}w_{L^2J(X)}(d)\,dd\,dX.}
\tag{12}
\]

则原点一致地

\[
\mathcal B_\tau(L)
\leq\liminf_c\inf_\alpha V_c^{\rm full}(\alpha)
\leq\limsup_c\sup_\alpha V_c^{\rm full}(\alpha)
\leq\Phi_0(L).
\tag{13}
\]

式 (6) 的 \(w_a\) 是**近距唯一安排**的相位差密度；把近距唯一与远支允许
事件放在同一真实相位中平均，严格强化 C88 只分别控制两事件的界。

### 小分离立刻产生正二次增益

令 \(\mathcal S\) 为单宏观原像源集合，\(\mathcal E\) 为多原像纤维中
\(B_2\) 严格最低或最高的源集合；在 \(\mathcal E\) 上令 \(\delta\) 为向内
最近谱差，并置 \(S(L)=2\int_{\mathcal S}F_0(L^2J)\)。
对固定 \(L>0\)，

\[
\boxed{\mathcal B_\tau(L)=S(L)
+\frac{L^2\tau^2}{4}\int_{\mathcal E}\delta(X)^2dX+o(\tau^2),
\qquad \tau\downarrow0.}
\tag{14}
\]

积分系数有限且严格为正。C88 旧下界在一个小正 \(\tau\) 区间恒等于
\(S(L)\)；新下界在同一区间已有严格正的二次增量。

同一纤维中，最低与最高两支对每个 \(\tau>0\) 都有正的保证贡献。
内部第 \(k\) 支按 \(b_1<\cdots<b_m\) 排序后，其相位保证量为正的准确条件是

\[
\tau>\frac4{L(b_{k+1}-b_{k-1})}.
\tag{15}
\]

这些是保证函数的性质；实际唯一事件还可出现在相位必要条件允许远支的地方。
完整证明见 [相位条件夹逼](phase/PHASE_CONDITIONED_BOUND.md)。

### 低精度的分离过渡为 \(\tau\asymp L\)

定义

\[
\mathcal T(r)=\int_0^r tF_2(1/t)dt,\qquad
\mathcal T(\infty)=C_{\rm end}/2.
\]

它在 \(0\leq r\leq1\) 上有准确公式
\(\mathcal T(r)=r^2/2-7r^3/(4\pi^2)\)。
当 \(L\tau\) 足够小时，全源下界准确等于

\[
\mathcal B_\tau(L)=S(L)+2L^4\int_{\mathcal E}J^2
\mathcal T\!\left(\frac{\tau\delta}{2LJ}\right)dX.
\tag{16}
\]

所以先取得库存极限后，若 \(L\downarrow0\)、\(L\tau\to0\)、
\(\tau/L\to\rho\in[0,\infty]\)，则

\[
\frac{\mathcal B_\tau(L)}{L^4}\to
C_{\rm end}\,2\int_{\mathcal S}J^2
+2\int_{\mathcal E}J^2\mathcal T\!\left(\frac{\rho\delta}{2J}\right)dX.
\tag{17}
\]

这是一个连续、严格增加的过渡函数。固定任意 \(\tau>0\) 时，低 \(L\) 极限
已能保证每条极端支全部近距主项的一半。详见
[低精度分离过渡](root/LOW_PRECISION_SEPARATION_TRANSITION.md)。

## 6. 三项连续库存谱确有一维真碰撞族

C82 证明 \((G,B_1,B_2)\) 几乎处处单原像。本轮进一步证明，其低维例外
确实包含一条正规解析弧：

\[
\boxed{X\ne Y,\quad J(X)J(Y)>0,\quad
(G,B_1,B_2)(X)=(G,B_1,B_2)(Y).}
\tag{18}
\]

证明重用 C84 已有的同纤维曲率恒等式。以谱坐标
\(\mathcal A=4x^{15/4}\)、\(d=4(y/x)^{9/4}\)、\(m=(7/16)\mathcal A^4d\)，记

\[
N=\frac{\mathcal A}{(\mathcal A-1)^2}
+16\frac m{(1+m)^2}+25\frac{m\mathcal A}{(1+m\mathcal A)^2}.
\]

同一 \((G,B_1)\) 纤维上，已有

\[
\Delta B_2=-\frac{225}{16}G\,\Delta N.
\tag{19}
\]

新的步骤发生在左侧折叠曲线上：沿固定 \(h=-4B_1/(15G)\) 水平线的曲率
导数，在 \(h\uparrow4\) 与 \(h\to-\infty\) 两端符号相反。
参数 Morse 坐标把同前两谱的两支写成 \((h,t)\)、\((h,-t)\)。
对每个足够小的 \(t>0\)，介值定理使两支曲率在某个中间 \(h\) 完全相等。
半代数有限分层给出一条真正的一维正规弧。

这项相遇还有稳定的有限版本：对任意整数序列
\(1\leq A_c<B_c=o(c)\)，充分大 \(c\) 时，Gamma **实落点连续延拓**中有两对
不同落点，在三个真实库存 \(c,c+A_c,c+B_c\) 的准确原读数分别完全相等。
其中包括库存 \(c,c+1,c+2\)。两对归一落点可保持固定正距离。

该结论的落点是实变量；原整数安排的准确碰撞问题仍保留整数条件。
证明见 [三谱例外弧与有限连续延拓](spectral/THREE_JET_EXCEPTION_ARC.md)。

## 7. 证据与研究状态

本轮以手推分析证明为主体。两项双斜率非零核验使用 Python 标准库 Fraction，
所有根隔离、分母不含零及最终行列式接受条件都用准确有理端点判断。
显示用小数不承担证明。程序已实际运行通过，根代理核对了有理化公式与区间
实现；其作用限于这两处横截性输入。

相位夹逼、低精度过渡、三谱例外弧、双支联合格及锐判据已作本项目共享输入下
的交叉核查。核查记录见 [阅读与复核路线](READING_GUIDE.md)。
本轮没有报告外部同行审查或形式化检查，也没有新增单库存整数全枚举范围。

曲率公式 (19) 已在 C84 发表，本轮将其作为继承工具；新增成果是它的例外弧
构造、与联合整数格的结合、全局误差界及锐门槛等上述结论。

## 8. 下一研究入口

一般有限 \(\tau\) 时，整个目录的唯一率是否收敛、其全局公式是否与格原点
无关，仍需要同时控制全部宏观逆支。本轮已在真正的两支开放区域给出完整
公式，并用其中一对支解决全域锐门槛的必要性。

一个具体的下一步是核查全部分支对的斜率横截性，并确定可适用的多重
horocycle joining 定理能否将成对结论提升为完整联合分布；随后可沿用本轮
整数平移核处理所有远支平移。成对独立本身不自动给出全部分支独立。

另一个定量问题是 (9)–(10) 之间的真实大 \(\tau\) 缺口主项，特别是正规
三谱相遇弧能否决定准确的 \(1/\tau\) 系数。原整数单次准确读数的全域单射性
仍是独立未决问题。

## 来源

项目冻结来源和各输入文件的精确提交见 [SOURCE_REFS.json](SOURCE_REFS.json)。
主继承为 C81 全纤维与水平线、C82 格极限与折叠、C83 小余体积、C84 曲率和
分支慢尾、C85 端点函数、C88 移动位置与有限分离模型。

外部标准输入分别用于明确的一步：

- Ratner, *The rate of mixing for geodesic and horocycle flows* (1987), Theorem 2、Corollary 2：
  [DOI](https://doi.org/10.1017/S0143385700004004)。
- Basu, *Algorithms in Real Algebraic Geometry: A Survey*, Theorem 2.1：
  [作者稿](https://www.math.purdue.edu/~sbasu/raag_survey2011_final-sep4-2014.pdf)。
- Aizenbud–Gourevitch, *De-Rham theorem and Shapiro lemma for Schwartz functions on Nash manifolds*,
  Theorem A.2.2、Remark 2.3.20：
  [作者稿](https://www.wisdom.weizmann.ac.il/~dimagur/RhamShap.pdf)。
