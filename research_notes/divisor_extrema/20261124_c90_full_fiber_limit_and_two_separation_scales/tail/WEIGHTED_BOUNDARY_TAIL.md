# C90：左尾楔区的真实损失为 τ^(-250/117)

## 1. 精确作用范围

本文研究 C84 已定位的固定左尾楔区，仍是原三态因子路径的 `H(0,1)`、
原整数安排和 C89 的端点临界缩放。所有库存极限均先于 `τ→∞`。

使用谱坐标

\[
\mathcal A=4x^{15/4},\quad d=4(y/x)^{9/4},\qquad I=[1/4,1/2],
\]

选充分小而固定的 `𝒜₀>0`，令

\[
\Omega_I=\{0<\mathcal A<\mathcal A_0,\ d\in I\}.
\]

源概率测度是原目录极限 `μ(dX)=2dxdy`。仅计源在 `Ω_I` 的安排，仍以
全部 `N_c=binom(c,2)` 归一，且竞争者来自全库存。记 near 与 full 的
区域唯一率之差为 `D_{c,I}(α)≥0`。对每组固定 `L>0,τ<∞`，取任一符合
C89 缩放的库存序列，定义

\[
\underline D_{\tau,I}(L)=\liminf_{c\to\infty}\inf_\alpha D_{c,I}(\alpha),
\quad
\overline D_{\tau,I}(L)=\limsup_{c\to\infty}\sup_\alpha D_{c,I}(\alpha).
\tag{1}
\]

以下结论对这样的序列选择成立，且得到相同主项。

**定理。** 令 `γ=250/117`。固定 `L>0` 时，

\[
\boxed{\underline D_{\tau,I}(L)\sim
\overline D_{\tau,I}(L)\sim
\mathfrak C_I(L)\tau^{-250/117}\qquad(\tau\to\infty),}
\tag{2}
\]

其中 `𝔠_I(L)>0` 是第 5 节的明确积分。

该结论不要求先证明每个有限 `τ` 的全库存唯一率极限存在；成对真实损失
下界与全部分支相位损失上界在这个楔区有相同主项。

## 2. 原谱及两个关键幂次

置

\[
g(d)=d^{14/3}(1-d).
\]

它在 `(0,14/17)` 上严格增加，在 `(14/17,1)` 上严格下降。对 `d∈I`，
记 `d_-(d)∈(14/17,1)` 为满足 `g(d_-)=g(d)` 的另一负瓣根。

C84 `BRANCH_TRANSITION.md` §5 已证明，离源最近的第三谱来自这条左负瓣
配对支，并且对 `d∈I` 一致有

\[
\delta_2(\mathcal A,d)
=\kappa(d)\mathcal A^{39/5}(1+O(\mathcal A)),
\tag{3}
\]

\[
\kappa(d)=\frac{4725}{64}C_*g(d)[d_-(d)-d]>0.
\tag{4}
\]

这里最近差是绝对差；其符号也由同一展开确定。所有不同左支的曲率差为

\[
N(\mathcal A',d')-N(\mathcal A,d)
=\frac{21}{4}\mathcal A^4(d'-d)+O(\mathcal A^5).
\]

另一个负瓣根与正瓣根都满足 `d'>d`，而所有右支满足 `N≥4/9`、源的
`N→0`。因此可统一减小 `𝒜₀`，使楔区中**全部不同宏观逆支**都满足

\[
B_2(Y)-B_2(X)<0.
\tag{5}
\]

最近的一支正是 (3) 的配对支；至少这条支始终存在。原有至多六支计数保证
没有遗漏其他类型。

再求 near 唯一率所需的 `J=|det D_X(G,B₁)|`。在 `I` 上一致有

\[
G=C_*\mathcal A^{19/5}g(d)(1+O(\mathcal A)),\quad
h_{\mathcal A}=-1+O(\mathcal A),\quad h_d=O(\mathcal A^4).
\]

因为 `B₁=−(15/4)hG`，

\[
\left|\det\frac{\partial(G,B_1)}{\partial(\mathcal A,d)}\right|
=\frac{15}{4}C_*^2\mathcal A^{38/5}g(d)g'(d)(1+O(\mathcal A)).
\]

坐标 Jacobian 是

\[
\left|\det\frac{\partial(\mathcal A,d)}{\partial(x,y)}\right|
=\frac{135}{16}4^{44/45}\mathcal A^{7/15}d^{5/9}.
\]

故

\[
\boxed{J(\mathcal A,d)=j(d)\mathcal A^{121/15}(1+O(\mathcal A)),}
\tag{6}
\]

\[
j(d)=\frac{2025}{64}C_*^2 4^{44/45}d^{5/9}g(d)g'(d)>0.
\tag{7}
\]

对应源概率密度为

\[
d\mu=\rho_0\mathcal A^{-7/15}d^{-5/9}\,d\mathcal A\,dd,
\qquad \rho_0=\frac{32}{135}4^{-44/45}.
\tag{8}
\]

上述展开都在固定 `I` 上一致。配对支满足 `𝒜'/𝒜→1`、`d'→d_-(d)`，
所以其 `J₁` 也按正系数乘 `𝒜^{121/15}` 衰减，特别 `J₁→0`。

## 3. 近距唯一的相位集中在两个端点

沿用

\[
w_a(q)=(1-|q|)F_2\!\left(\frac a{1-|q|}\right),\quad
F_0(a)=\int_{-1}^1w_a(q)dq.
\]

定义概率测度

\[
d\pi_a(q)=\frac{w_a(q)}{F_0(a)}dq.
\]

由 C83 `F₂(s)=O(s³)` 和 C85 `F₀(a)∼C_end a²`，对每个固定 `ε>0`，

\[
\int_{|q|\le1-\varepsilon}w_a(q)dq=O_\varepsilon(a^3)=o(F_0(a)).
\]

又因 `w_a` 为偶函数，所以

\[
\boxed{\pi_a\Longrightarrow\tfrac12\delta_{-1}+\tfrac12\delta_{1}
\qquad(a\downarrow0).}
\tag{9}
\]

这一步说明为什么不能直接把 C84 的未加权几何坏集当成真实损失。

令 `b→0` 为远支格的余体积，固定 `s>0`。C89 的成对损失核为

\[
\mathcal D(a,b,-s)=\int_{-1}^1 w_a(q)
\left[1-E_2\!\left(\frac b{(1-|q+s|)_+}\right)\right]dq.
\]

仿射二阶矩给 `E₂(t)≤t/(1+t)`，故非空的固定长度窗口在 `b→0` 时命中
概率趋于一。当 `0<s<2`，端点 `q=−1` 的远支窗口有严格正长度，而
`q=1` 的窗口在一个邻域内为空。由 (9) 与这些局部一致界，

\[
\boxed{\frac{\mathcal D(a,b,-s)}{F_0(a)}\longrightarrow\frac12
\qquad(a,b\downarrow0,\ 0<s<2).}
\tag{10}
\]

`s>2` 时成对损失准确为零。`a,b` 之间不需要指定趋零速率比。

## 4. 全部远支与同一个相位半端点

在楔区中所有偏移均为负。置

\[
s_\tau(X)=\frac{L\tau}{2}\delta_2(X)>0.
\]

因为最近偏移是 `−s_τ`，其余偏移更负，全部远支的相位允许区间在
`[-1,1]` 上的并恰为

\[
[-1,1-s_\tau]\quad(0<s_\tau<2),
\]

当 `s_τ≥2` 时为空。这里使用每个负偏移 `h<0` 的允许区间
`(-1+h,1+h)∩[-1,1]=[-1,1+h)`（端点零测），它们按 `h` 嵌套。

因此全部分支的相位加权损失上界为

\[
W_\tau(X)=
\begin{cases}
\displaystyle\int_{-1}^{1-s_\tau(X)}w_{L^2J(X)}(q)dq,&0<s_\tau(X)<2,\\
0,&s_\tau(X)\ge2.
\end{cases}
\tag{11}
\]

而 C89 的真实成对损失给下界

\[
\int_{\Omega_I}\mathcal D(L^2J(X),L^2J(TX),-s_\tau(X))d\mu
\le\underline D_{\tau,I}(L)
\le\overline D_{\tau,I}(L)
\le\int_{\Omega_I}W_\tau(X)d\mu.
\tag{12}
\]

这是对三个格原点一致的夹逼。可先在 `𝒜≥ε` 的正规紧片使用 C89，
再令 `ε↓0`；被删源的面积趋零，故 (12) 对完整固定楔区成立。

在接下来的尾缩放中，(9) 也使 `W_τ/F₀(a)→1/2` 当极限 `s∈(0,2)`；
当极限 `s>2` 时上下核均为零。因而 (12) 的两端具有同一主项。

## 5. 精确积分和指数 250/117

固定 `L>0`，令 `𝒜=τ^{-5/39}r`。由 (3)，

\[
s_\tau(\mathcal A,d)\longrightarrow\frac{L\kappa(d)}2r^{39/5}.
\]

有效区间因此是

\[
0<r<\left(\frac4{L\kappa(d)}\right)^{5/39}.
\tag{13}
\]

由 (6) 和端点二次律，

\[
F_0(L^2J)=C_{\rm end}L^4j(d)^2
\mathcal A^{242/15}(1+o(1)).
\]

乘上 (8) 后，`𝒜` 的被积幂是 `242/15−7/15=47/3`，其原函数幂为
`50/3`。因此总缩放指数为

\[
\boxed{\frac5{39}\cdot\frac{50}3=\frac{250}{117}.}
\]

严格支配收敛如下：`κ` 在 `I` 上有正下界，(3) 的一致余项使所有非零
上下核均支持于 `r≤R` 的固定区间；`F₀(L²J)≤C_L𝒜^{242/15}` 给
可积上界常数乘 `r^{47/3}`。极限中的阈值等式在每个固定 `d` 上只有
一个 `r`，故为零面积；`r=0` 同样可略去。(10)–(13) 遂给两端积分
共同的极限系数

\[
\boxed{
\mathfrak C_I(L)=\frac8{1125}\,4^{-44/45}
C_{\rm end}L^4\left(\frac4L\right)^{250/117}
\int_{1/4}^{1/2}d^{-5/9}j(d)^2\kappa(d)^{-250/117}\,dd.}
\tag{14}
\]

其中因子 `1/2` 来自单个负相位端点；`ρ₀` 已是原概率密度 `2dxdy`，
没有另外补乘二。直接核对常数为

\[
\rho_0\times\frac12\times\frac3{50}
=\frac8{1125}4^{-44/45}.
\]

`j,κ` 在 `I` 上连续且严格为正，所以系数有限且严格为正。由 (12) 挤压，
定理 (2) 成立。

## 6. 与未加权慢尾和局部横截弧的关系

C84 的同一楔区几何分离坏集按 `τ^{-8/117}` 衰减；其中大量源本来就很难
通过 near 唯一检查。真实损失付回其 `F₀(L²J)` 权重后，指数变成
`250/117>2`。本篇所处理的固定楔区因而为 `o(τ^{-1})`，不能压过
`TRANSVERSE_ARC_AND_LOCAL_TAIL.md` 中正规横截弧的真实倒数主项。

这一定量结论限定于 `d∈[1/4,1/2]` 的原固定楔区。靠近其他源边界、折叠
端点或多支第三谱共同零处的完整渐近，仍需要相应的加权分析。

## 7. 第二低精度过渡 R(β) 中的对应尾部

本轮 [TRUE_LOW_PRECISION_TRANSITIONS.md](../root/TRUE_LOW_PRECISION_TRANSITIONS.md)
证明了按最近正、负谱差与 `4/β` 比较的函数 `R(β)`。在本楔区，全部
谱差均负，且最近差就是 (3)，所以其区域损失准确为

\[
\mathcal R_I(\infty)-\mathcal R_I(\beta)
=C_{\rm end}\int_{\Omega_I}J(X)^2
\mathbf1\{\delta_2(X)<4/\beta\}\,dX.
\]

用 (3)、(6)、(8) 直接做同一个单调阈值积分，得到

\[
\boxed{\begin{aligned}
\mathcal R_I(\infty)-\mathcal R_I(\beta)
\sim{}&\frac8{1125}4^{-44/45}C_{\rm end}4^{250/117}\,
\beta^{-250/117}\\
&\times\int_{1/4}^{1/2}d^{-5/9}j(d)^2
\kappa(d)^{-250/117}\,dd,
\qquad\beta\to\infty.
\end{aligned}}
\tag{15}
\]

这里 `dX=dμ/2` 已包含单端点的权重。它是函数 `R` 自身的大 `β` 尾部，
无需交换先库存、后大分离、再低精度的极限。与同一正文中的正规弧贡献
`const/β` 相比，此固定楔区是严格更快的尾部。

## 科学来源

- C84 `BRANCH_TRANSITION.md` §5：最近左负瓣配对、统一谱差展开和未加权
  `8/117` 楔区尾指数。冻结科学提交 `01f50954ee37548372464c68a311f7df2dba0632`。
- C89 `joint/PAIR_LATTICE_LIMIT.md`：整个左负瓣配对域的 a.e. 双斜率横截和
  成对真实整数极限；`phase/PHASE_CONDITIONED_BOUND.md`：全部分支的相位
  加权保证与损失夹逼。冻结科学提交 `6a6bb85747f6396970b1f54d999822ab710750a4`。
- C83 `HAAR_SMALL.md`、C85 `endpoint/ENDPOINT_LIMIT.md`：两标记立方律、仿射
  二阶矩和端点二次律。
- 新证明为 (6) 的 Jacobian 权重、(9)–(12) 的同号相位夹逼及 (14) 的准确
  真实主项。正文为分析证明，不依赖新增浮点数值实验。
