# C90：横截三谱相遇弧与真实局部损失的准确倒数主项

## 1. 对象及结论

本文沿用原三态因子路径、原观察者 `H(0,1)`、原整数目录
`2≤w≤v≤c` 及 C89 的三个库存 `c,c+A,c+B`。宏观源 `X=(v/c,w/c)`、
连续谱和 Haar 格均为该路径观察者的辅助表示，不改变原安排或 X6 内部状态。

先取 C89 端点临界极限

\[
c^{1/3}\ll B\ll c,\quad D=\sqrt{c/B},\quad A/D\to\tau<\infty,
\quad L_c=2^{p-p_*(c,B)}\to L>0.
\]

本篇再研究所得真实区域极限随 `τ→∞` 的行为。库存极限在先。

新增结论如下。

1. 左折叠线上恰有一个三谱奇差商零点，且该零点简单。由它产生一条
   **简单横截**的正规三谱相遇弧：不同的正规配对
   `Y=T(X)` 共享 `(G,B₁,B₂)`，而 `f(X)=B₂(TX)−B₂(X)` 在此弧上
   的梯度处处非零。此弧可取为 C89 折叠相遇族的一个明确局部分支。
2. 在这条弧的一段紧子弧周围，完整纤维恰有六支，其余四支的 `B₂` 值
   与配对两支保持统一正距离。故固定 `L>0` 后，充分大 `τ` 的完整区域
   唯一率由 C89 的成对公式准确给出。
3. 该区域真实损失有严格正的准确主项 `C_K(L)/τ`，其中 `C_K(L)` 是
   下文明确的线积分。无需先得到全域六支 joining 定理。

## 2. 用两个有理方程定位简单折叠交点

为区分库存增量，以 `𝒜` 表示谱坐标。置

\[
\mathcal A=4x^{15/4},\quad d=4(y/x)^{9/4},\quad m=\frac7{16}\mathcal A^4d,
\quad u=\frac m{1+m},\quad v=\frac{m\mathcal A}{1+m\mathcal A}.
\]

在左负瓣 `0<𝒜,d<1`，原谱为

\[
\nu=G/C_*
=\frac{\mathcal A^{19/5}d^{14/3}(1-\mathcal A)(1-d)}
{(1+m)(1+m\mathcal A)},
\]

\[
h=\frac1{\mathcal A-1}+5-4u-5v,\quad
T=4u(1-u)+5v(1-v),
\]

\[
N=\frac{\mathcal A}{(\mathcal A-1)^2}+16u(1-u)+25v(1-v),
\quad R=\frac{14}{3}+\frac d{d-1}-u-v.
\]

已有恒等式是

\[
h_{\mathcal A}=-N/\mathcal A,\quad h_d=-T/d,
\quad \mathcal A\partial_{\mathcal A}\log\nu=h-1/5,
\quad d\partial_d\log\nu=R.
\]

沿固定 `h` 的微分算子为

\[
\mathcal D=d\partial_d-\frac{\mathcal A T}{N}\partial_{\mathcal A}.
\]

定义两个有理函数

\[
\boxed{P=NR-T(h-1/5),\qquad
K=N\,dN_d-\mathcal A T N_{\mathcal A}.}
\tag{1}
\]

于是 `𝒟 logν=P/N`，左负瓣折叠曲线恰为 `P=0`；而 `𝒟N=K/N`。
在折叠上 `K=0` 正是 C89 奇差商在 `t=0` 时为零的条件。

### 左折叠上恰有一个简单零点：解析证明

由 `dN_d=𝒜T_𝒜`，有

\[
K=\mathcal A(NT_{\mathcal A}-TN_{\mathcal A}).
\]

通分并按 `d` 的幂分组，准确得到

\[
K=\frac{-224d\mathcal A^5\,Q(\mathcal A,d)}
{(\mathcal A-1)^3(7\mathcal A^4d+16)^3(7\mathcal A^5d+16)^3},
\tag{1a}
\]

其中 `Q=q₀+dq₁+d²q₂+d³q₃+d⁴q₄`，

\[
\begin{aligned}
q_0&=393216-983040\mathcal A^2,\\
q_1&=114688\mathcal A^4(5\mathcal A^3-30\mathcal A^2+21\mathcal A-5),\\
q_2&=-225792\mathcal A^8\{5(\mathcal A-1)^4+3\mathcal A^2\},\\
q_3&=21952\mathcal A^{13}(-5\mathcal A^3+21\mathcal A^2-30\mathcal A+5),\\
q_4&=7203\mathcal A^{18}(2\mathcal A^2-5).
\end{aligned}
\]

在 `0<𝒜<1`，`q₁',q₂',q₄'` 全为负。逐项核对：

- `q₁'=573440𝒜³(7𝒜³−36𝒜²+21𝒜−4)`；括号至多
  `−29𝒜²+21𝒜−4<0`，其判别式为 `−23`。
- `q₂'=−225792𝒜⁷{20(𝒜−1)³(3𝒜−2)+30𝒜²}`。
  当 `𝒜≤2/3`，大括号显然为正；当 `𝒜>2/3`，它至少为
  `−20/27+40/3>0`。
- `q₄'=7203𝒜¹⁷(40𝒜²−90)<0`。

而

\[
q_3'=21952\mathcal A^{12}
(-80\mathcal A^3+315\mathcal A^2-420\mathcal A+65)
\le1426880\mathcal A^{12}.
\]

因此在整个 `0<𝒜,d<1` 上

\[
\boxed{Q_{\mathcal A}<-1966080\mathcal A
+1426880\mathcal A^{12}\le-539200\mathcal A<0.}
\tag{1b}
\]

式 (1a) 中 `Q` 前的因子在左瓣为正，所以在 `K=0` 处必有 `K_𝒜<0`。
另一方面，`R_𝒜=−T/𝒜`、`h_𝒜=−N/𝒜` 给

\[
P_{\mathcal A}=N_{\mathcal A}R-T_{\mathcal A}(h-1/5),
\quad
P=0\Longrightarrow
P_{\mathcal A}=-\frac{h-1/5}{\mathcal A N}K.
\tag{1c}
\]

在任一折叠 `K` 零点，遂有 `P_𝒜=0`。沿固定 `h` 的非退化峰保证
`∂_d|_h P<0`，而此时 `P_𝒜=0`，所以 `P_d<0`。
以 C82 的全局解析折叠 `(𝒜_*(h),d_*(h))` 为参数，微分 `P=0` 和 `h=h`
便得该零点处

\[
d_*'(h)=0,\quad \mathcal A_*'(h)=-\mathcal A/N,
\quad
\frac{d}{dh}K(\mathcal A_*(h),d_*(h))
=-\frac{\mathcal A}{N}K_{\mathcal A}>0.
\tag{1d}
\]

C89 已证明折叠上 `K<0` 当 `h→−∞`，`K>0` 当 `h↑4`。介值定理给
至少一个零点。(1d) 表明所有零点都简单且只能由负跨向正；若有两个零点，
其间必有反向过零，与 (1d) 矛盾。因此左折叠上恰有一个零点，且必简单。
这个唯一性与简单性结论由上述解析论证给出，不依赖下面的数值定位。

### 准确定位与其他分支所用的证书

程序 [certify_transverse_fold.py](certify_transverse_fold.py) 及其实际输出
[transverse_fold_certificate.json](transverse_fold_certificate.json) 使用
`Fraction` 与向外舍入到分母 `10^100` 的有理区间。中心是下列准确有理数：

\[
a_c=0.606768297615534074525671270774251123919356,
\]
\[
d_c=0.817439750408149842744396827269022350625456.
\]

令矩形 `Q=[a_c−10^{-12},a_c+10^{-12}]×[d_c−10^{-12},d_c+10^{-12}]`。
程序准确证明以下事实：

- `P_d<−160`，在矩形的下 `d` 面 `P>0`，上 `d` 面 `P<0`；
- 在左 `𝒜` 面 `K>0`，右 `𝒜` 面 `K<0`；
- 沿 `P=0`，
  \[
  \frac{dK}{d\mathcal A}=K_{\mathcal A}-K_dP_{\mathcal A}/P_d<-18,
  \quad
  \frac{dh}{d\mathcal A}=h_{\mathcal A}-h_dP_{\mathcal A}/P_d<0;
  \]
- 整个矩形上
  \[
  -2934<\det D(P,K)<-2933,
  \quad
  2<\frac{dK}{dh}\bigg|_{P=0}<\frac{21}{10}.
  \tag{2}
  \]

面符号使用矩形上的准确导数包围与中心值，经均值定理外包；不是把单个
中心值代替整个面的符号。由 `P_d<0` 和两面符号，对每个 `𝒜` 有唯一
`d=d(𝒜)` 使 `P=0`。再用 `K` 的两面符号和沿这条曲线的严格下降性，
得到 `Q` 内恰有一个公共零点 `(a_*,d_*)`。这是一维介值论证。

其 `h` 值的显示包围为

\[
2.12916590982216<h_*<2.12916590984091.
\]

这里显示小数只便于定位；接受条件均在 JSON 中用准确有理端点保存。

## 3. 从简单折叠交点得到简单三谱相遇弧

C82 的非退化折叠给参数 Morse 坐标

\[
X=X(h,t),\quad \nu=M(h)-t^2,\quad \partial_td>0.
\]

将 C89 的奇差商记为 `𝒦`，以区别有理函数 `K`：

\[
\mathcal K(h,t)=
\begin{cases}
\dfrac{N(X(h,t))-N(X(h,-t))}{2t},&t\ne0,\\
\partial_tN(X(h,0)),&t=0.
\end{cases}
\]

它解析且关于 `t` 偶。在折叠线上

\[
\mathcal K(h,0)=\frac{K}{Nd}\partial_td.
\]

因 `N,d,∂td` 都为正，公共零点处由 (2) 得

\[
\partial_h\mathcal K(h_*,0)
=\frac{\partial_td}{Nd}\frac{dK}{dh}\bigg|_{P=0}>0.
\tag{3}
\]

解析隐函数定理给 `ε>0` 及唯一解析偶函数 `h=H(t)`，满足
`H(0)=h_*`、`𝒦(H(t),t)=0`（`|t|<ε`），并可缩小范围使 `∂h𝒦>0`。
当 `0<t<ε` 时，`X(h,t)` 与 `X(h,-t)` 是不同正规原像。

同前两谱纤维上 C84 已有

\[
B_2(Y)-B_2(X)=-\frac{225}{16}G(X)\{N(Y)-N(X)\}.
\]

取 `X=X(h,t)`、`Y=X(h,-t)`，便有

\[
f(h,t):=B_2(Y)-B_2(X)=\frac{225}{8}G(h,t)t\mathcal K(h,t).
\tag{4}
\]

在 `h=H(t)`、`t>0` 上，

\[
\partial_hf=\frac{225}{8}G(h,t)t\partial_h\mathcal K(h,t)>0.
\tag{5}
\]

因为 `(h,t)` 到源坐标是局部解析微分同胚，(5) 就是源坐标中 `∇f≠0`。
这比只知道零集含正规解析弧更强：第三谱差在该弧横截地改变符号。

## 4. 其余四支的第三谱确实分离

同一准确程序还在目标 `(h_*,ν_*)` 上隔离了四条其他内部正规支。
以 `ν_*^{15}` 表示目标可完全使用有理区间；固定 `d` 时通过 `h_𝒜<0`
二分隔离 `𝒜`。`h_𝒜,h_d<0` 给整个目标盒和根盒的单调外包，负瓣上升、
下降根及正瓣根分别由准确 `ν^{15}` 端点符号和 `P≠0` 确认。

| 分支 | d 的准确外包 | N 的显示包围 |
|---|---|---|
| 左正瓣 | `[1.0578177,1.0578178]` | `[5.3251362056,5.3251365269]` |
| 右负瓣上升 | `[0.3787012,0.3787014]` | `[15.6248571456,15.6248897381]` |
| 右负瓣下降 | `[0.9718356,0.9718358]` | `[20.1068713103,20.1068862358]` |
| 右正瓣 | `[1.0238258,1.0238260]` | `[20.4236522197,20.4236665145]` |

相对于折叠点的 `N_*`，四个差都严格大于 `1/1000`。最紧的差包围为
`[0.0016952753573,0.0016955966490]`，因此此处没有把视觉上接近当作相等。

四支由正规隐函数定理延续到目标邻域。对足够小的 `t>0`，相遇弧上的
左负瓣两支与这四支合计已有六个不同正规可行原像；C81 的全域至多六支
结论给出完整性。取 `0<t₁<t₂<ε` 的一个紧弧段，再取其固定小管状区域
`K₀`，可使：

\[
J(X),J(TX)>0,\quad \inf_{K_0}|\nabla f|>0,
\]

以及对其余四支 `Y_j`

\[
\inf_{X\in K_0}|B_2(Y_j(X))-B_2(X)|\ge\delta_*>0.
\tag{6}
\]

这一步使用连续性缩小紧管，不声称已经算出管宽或 `δ_*` 的最优数值。

## 5. 损失核的准确积分分离

沿用 C89 的线性格函数 `F₂,F₀` 和仿射空窗概率 `E₂`。令

\[
w_a(d)=(1-|d|)F_2\!\left(\frac a{1-|d|}\right),
\]

\[
\mathcal D(a,b,z)=\int_{-1}^1w_a(d)
\left[1-E_2\!\left(\frac b{(1-|d-z|)_+}\right)\right]dd.
\tag{7}
\]

零窗口按 `E₂(∞)=1` 解释。此核连续、非负，且在 `|z|≥2` 为零；
`a,b>0`、`|z|<2` 时严格为正。窗口长度趋零时的连续性可由
`1−E₂(b/ℓ)≤ℓ/b` 得到；这一界只用基本域平移平均的期望点数。

定义

\[
\Xi(b)=2\int_0^1[1-E_2(b/\ell)]\,d\ell\in(0,2).
\tag{8}
\]

Tonelli 及 `s=d−z` 给准确分离恒等式

\[
\boxed{\int_{\mathbb R}\mathcal D(a,b,z)\,dz=F_0(a)\Xi(b).}
\tag{9}
\]

因为对每个固定 `d`，`z` 的积分都是
`∫_{−1}^1[1−E₂(b/(1−|s|))]ds=Ξ(b)`，再用 `∫w_a=F₀(a)` 即得。

## 6. 全库存真实区域损失的倒数主项

在第 4 节紧管中选一块闭管 `K`，使其可在坐标 `(s,z)` 下写成
`s∈[s₁,s₂], z=f(X)∈[−z₀,z₀]`，且 `z₀>0`。端部边界为零面积。
令 `Γ=K∩{f=0}`，只把 `K` 中原安排作为源，以全部 `N_c` 归一，仍允许
全库存竞争者。记区域 near 唯一率与 full 唯一率之差的库存极限为
`𝓛_{τ,K}(L)`。

由 (6)，固定 `L` 且 `τ>4/(Lδ_*)` 时，其余四支都满足第三谱必要差值
阈值的严格反向不等式，因此不可能产生同格竞争者。C89 的准确有限谱
排除与成对联合极限遂给对三个格原点一致的完整区域极限

\[
\mathcal L_{\tau,K}(L)
=2\int_K\mathcal D\left(L^2J(X),L^2J(TX),\frac{L\tau}2 f(X)\right)dX.
\tag{10}
\]

**定理。** 固定 `L>0`，

\[
\boxed{\mathcal L_{\tau,K}(L)\sim\frac{\mathcal C_K(L)}\tau,\qquad
\mathcal C_K(L)=\frac4L\int_\Gamma
\frac{F_0(L^2J(X))\Xi(L^2J(TX))}{|\nabla f(X)|}\,d\mathcal H^1(X)>0.}
\tag{11}
\]

**证明。** 写 `X=X(s,z)`、源面积密度 `q(s,z)=|det D_{s,z}X|`。
在 (10) 中令 `r=Lτz/2`，便得

\[
\tau\mathcal L_{\tau,K}(L)
=\frac4L\int_{s_1}^{s_2}\int_{-2}^2
\mathcal D(a(s,2r/(L\tau)),b(s,2r/(L\tau)),r)
q(s,2r/(L\tau))\,dr\,ds
\]

对充分大 `τ` 成立。所有参数位于正紧区间，故支配收敛和 (9) 给极限。
在零水平上 `q(s,0)ds=d𝓗¹/|∇f|`，这就得到 (11)。严格正性来自
非零弧长、正 `J`、非零梯度及 `F₀,Ξ>0`。证毕。

同一公式可在被积函数中加入连续紧支源权重 `χ≥0`；若它在弧上非零，
主系数严格为正。

### 有序源与反向支的计数

式 (11) 只计 `K` 中的源安排，每个源一次。若同时计 `K` 与 `T(K)`，
两片不交，两个源贡献相加。因

\[
|\det DT(X)|=J(X)/J(TX),\qquad f(TX)=-f(X),
\]

两片的系数可在同一弧 `Γ⊂K` 上写为

\[
\frac4L\int_\Gamma\frac{
F_0(a_0)\Xi(a_1)+(J_0/J_1)F_0(a_1)\Xi(a_0)
}{|\nabla f|}\,d\mathcal H^1.
\tag{12}
\]

这里没有额外把无序配对再乘二；源概率的归一化 `2dX` 已包含在 (10) 中。

## 7. 局部主系数的低、高精度行为

C83 的仿射平移平均与普通 Siegel 公式已给单位方格格点数
`EN=1/s`、`E[N(N−1)]=1/s²`。因此

\[
\frac1s-\frac1{2s^2}\le1-E_2(s)\le\frac1s.
\tag{13}
\]

左式来自整数 `N≥0` 上 `1_{N>0}≥N−N(N−1)/2`。另由
`EN²=(EN)²+EN` 和 Cauchy–Schwarz 得
`E₂(s)≤s/(1+s)`。代入 (8) 可得

\[
2-2b\log(1+1/b)\le\Xi(b)\le2,
\quad
\frac1b-\frac1{3b^2}\le\Xi(b)\le\frac1b.
\tag{14}
\]

本轮 [AFFINE_VOID_KERNEL.md](../joining/AFFINE_VOID_KERNEL.md) §§9–10
进一步证明了所需准确核式：

\[
\Xi(b)=\frac1b-\frac2{\pi^2b^2}\quad(b\ge1),\qquad
\Xi(b)=2-\frac4{\pi^2}b\log(1/b)+O(b)\quad(b\downarrow0),
\]

以及由 C82 两标记准确式和 C85 端点积分直接得到

\[
F_0(a)=1-\frac7{2\pi^2a}\quad(a\ge1),\qquad
F_0(a)=C_{\rm end}a^2-\frac2{\pi^2}a^3+O(a^4)\quad(a\downarrow0).
\]

沿固定紧弧 `J₀,J₁` 正且有界，代入 (11) 得低精度的首个对数修正：

\[
\boxed{\begin{aligned}
\mathcal C_K(L)
={}&8C_{\rm end}L^3\int_\Gamma\frac{J_0^2}{|\nabla f|}\,d\mathcal H^1\\
&-\frac{32C_{\rm end}}{\pi^2}L^5\log(1/L)
\int_\Gamma\frac{J_0^2J_1}{|\nabla f|}\,d\mathcal H^1
+O_K(L^5),\qquad L\downarrow0.
\end{aligned}}
\tag{15}
\]

高精度时令

\[
I_{ab}=\int_\Gamma\frac{J_0^{-a}J_1^{-b}}{|\nabla f|}\,d\mathcal H^1.
\]

只要 `L² min_Γ(J₀,J₁)≥1`，就有**准确三项式**

\[
\boxed{\mathcal C_K(L)=4I_{01}L^{-3}
-\frac{8I_{02}+14I_{11}}{\pi^2}L^{-5}
+\frac{28I_{12}}{\pi^4}L^{-7}.}
\tag{16}
\]

式 (15) 中 `log(1/(L²J₁))=2log(1/L)−log J₁` 的第二项统一为 `O(1)`，
故余项确为 `O_K(L⁵)`。式 (16) 则是两个准确核式的有限乘积，没有余项。

这里先取库存极限，再取大 `τ` 主系数，最后研究其 `L` 行为；没有交换这些
极限或给库存误差的联合速率。

## 8. 第二低精度尺度 R(β) 的同一局部主项

本轮 [TRUE_LOW_PRECISION_TRANSITIONS.md](../root/TRUE_LOW_PRECISION_TRANSITIONS.md)
证明第二低精度过渡函数

\[
\mathcal R(\beta)=C_{\rm end}\int_\Delta J_0^2
\bigl[\mathbf1\{\delta_+\ge4/\beta\}
+\mathbf1\{\delta_-\ge4/\beta\}\bigr]dX,
\quad \mathcal R(\infty)=2C_{\rm end}\int_\Delta J_0^2dX.
\]

在本文的同一紧管 `K` 上，当 `β>4/δ_*` 时，四条其他支均越过阈值，
故 `R(∞)−R(β)` 的此区域贡献准确为

\[
\mathcal R_K(\infty)-\mathcal R_K(\beta)
=C_{\rm end}\int_K J_0^2\mathbf1\{0<|f|<4/\beta\}\,dX.
\]

简单零水平的两侧 coarea 换元直接给

\[
\boxed{\mathcal R_K(\infty)-\mathcal R_K(\beta)
\sim\frac{8C_{\rm end}}\beta
\int_\Gamma\frac{J_0^2}{|\nabla f|}\,d\mathcal H^1
\qquad(\beta\to\infty).}
\tag{17}
\]

因为水平厚度为 `4/β`、两侧均计入，系数是 `8/β`。这是对已证明函数
`R` 自身的阈值积分推导，不通过交换 (11)、(15) 的极限获得。
它与 (15) 的 `L³/τ=L⁴/(Lτ)` 主项系数吻合。

## 9. 多支交叉与全域主项尚需的条件

在已知完整多支乘积公式的正规紧源片上，若所有差函数 `f_j=B₂(Y_j)−B₂(X)`
的零弧均简单，且不同零弧只作横截相交，则不同远支同时允许的交集面积为
`O(τ^{-2})`。因为交点附近 `(f_i,f_j)` 是局部坐标，而两窗口分别要求
`|f_i|,|f_j|<4/(Lτ)`。损失核有界，所以包含排除法表明一阶系数等于
各零弧的 (11) 系数之和。

若两条零弧重合，应保留共同法向尺度下的完整乘积核；此时不能把系数直接
相加。高阶零、折叠端点和源边界也需要各自的加权可积性估计。
本文认证的六支局部管避开这些问题，并已得到无条件的真实区域主项；
它不将此局部主项自动提升为全库存的准确主项。

## 来源和核验范围

- C89 固定 Source `6a6bb85747f6396970b1f54d999822ab710750a4`：
  `spectral/THREE_JET_EXCEPTION_ARC.md` 的 Morse 坐标与奇差商；
  `joint/PAIR_LATTICE_LIMIT.md` 的左负瓣 a.e. 双斜率横截、真实成对概率
  及原点一致极限。
- C84 `BRANCH_TRANSITION.md` §3：同纤维曲率恒等式；§4 原有完整根计数方法。
- C82 `FIBER_STRUCTURE.md`：非退化折叠和最多六支；C83 `HAAR_SMALL.md`
  §1：仿射一、二阶矩；C85 `ENDPOINT_LIMIT.md` §4：端点小余体积二次律。
- 本篇准确程序已经实际运行。其数学任务是公共零点存在、唯一性、简单性和
  四条其他支的准确隔离与谱间隔；解析延拓、coarea 和概率转移由正文证明。
  这是共享输入下的项目内研究成果，外部同行复核与形式化检查未执行。
