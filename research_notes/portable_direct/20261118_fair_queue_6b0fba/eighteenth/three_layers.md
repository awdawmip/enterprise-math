# 真实二项权的三层干涉：三个二层子和均未穿零，三层已经穿零

在原 Perfect Prime AP 模型中取 $m=6$，保留首三个 Cauchy 层及其实际权重 $1,-5t,10t^2$。**在 $57/100<t<4/7$ 有唯一一个简单的规余因子零点。** 在从零到 $4/7$ 的整个开闭区间内，三个二层子和都只有常数规核。三层和在该零点另有一个独立固定向量。它的原始矩矩阵在该处仍严格全正。另有 $m=8$ 的两次穿零与 $m=10$ 的三次穿零。下面给出适用于所有 $m$ 的三层对偶判据与精确根数证书。

行政任务于 8 月 31 日修复上一份文件的 Git 对象标识，登记的数学增量为零。原数学结论控制单个相邻二层铅笔，完整 AP 是全部 $m$ 层的交替和。本节研究一个会直接影响证明路线的问题：固定原来的节点、有限差分、层号与二项系数，只截取连续三层，是否保留无穿零性质。[再冻结交接](https://github.com/awdawmip/enterprise-math/blob/cf352564a8f985fbc3151783fa0ee74f1a0b2a7f/research_returns/PERFECT_PRIME_AP_FIXED_POINT_COMPOUND_RESULT_REFREEZE_V2_RETURN_20260831.md) · [原二层定理及插值模型](https://github.com/awdawmip/enterprise-math/blob/eb90904dc7fa3abbb95fa58b32c656ec315a8c9a/research_returns/PERFECT_PRIME_AP_FIXED_POINT_COMPOUND_NO_RECROSSING_RETURN_20260830.md)

## 原规余因子与三层切片

取 $n=m-1,\ b=m^2,\ x_i=1+i,\ y_j=mj,\ w_i=(-1)^i\binom ni,\ W=\operatorname{diag}w$，指标均从 0 开始。原第 $v$ 层为 $H_v(i,j)=(x_i+y_j+bv)^{-1}$。对任意矩阵 $H$，定义
$$
 M(H)=\begin{pmatrix}
 W\operatorname{diag}(Hw)&-WHW\\
 -WH^\top W&W\operatorname{diag}(H^\top w)
 \end{pmatrix},\qquad M_v=M(H_v).
$$
设 $m\ge3,\ 0\le s\le n-2$，写 $(A,B,C)=(\binom ns,\binom n{s+1},\binom n{s+2})$。连续三层的标准化和是
$$
 L_{[s]}(t)=A M_s-Bt M_{s+1}+Ct^2 M_{s+2}.
$$
原始连续三项还带公因子 $(-t)^s$，在 $t>0$ 时不影响其核。记 $\tau_{[s]}(t)$ 为删掉最后一行一列的主子式。$M(H)$ 对称且各行和为零，所以此删行列恰取常数规方向的补空间；零点等价于出现额外零向量。

三个连续二项系数满足
$$
 \frac{B^2}{AC}=\left(1+\frac1{s+1}\right)
                  \left(1+\frac1{n-s-1}\right)\le4 ,
$$
等号仅在 $n=2$。因此 $H=AH_s-BtH_{s+1}+Ct^2H_{s+2}$ 的密度
$u^{bs}(A-Btu^b+Ct^2u^{2b})$ 在 $0<u<1$ 几乎处处严格正。任一按行列递增的子式由 Andréief 公式给出两个广义 Vandermonde 行列式乘此正密度的积分；在有序节点单纯形内两者均严格正。于是 **每个这样的三层 $H$ 都严格全正**。$Hw$ 和 $H^\top w$ 的各项也严格正，分别在积分中再乘 $(1-u^m)^n$ 和 $(1-u)^n$ 即得。故两侧的归一化算子始终有定义，$\ker M(H)$ 与 $\operatorname{diag}(Hw)^{-1}HW\operatorname{diag}(H^\top w)^{-1}H^\top W$ 的固定向量空间同维。

## 全参数三层对偶判据

令 $e_v=H_v w,\ R_v=W\operatorname{diag}(e_v),\ A_v=\operatorname{diag}(e_v)^{-1}H_vW$。原插值模型给出
$M_v=(I,-A_v)^\top R_v(I,-A_v)$。若 $q_j=f(y_j)$ 且 $\deg f\le n$，则 $(A_vq)_i=f(-x_i-bv)$。故 $A_{v+1}=TA_v$，其中
$$
 T_{ij}=\prod_{k\ne j}\frac{i+b-k}{j-k}.
$$
在节点上取平移差使次数至多为 $n$ 的多项式满射到次数至多 $n-1$ 的多项式，故 $\ker(T^\top-I)=\langle w\rangle$。

将 $v=s,s+1,s+2$ 的三个 $(I,-A_v)$ 叠成 $X$，并删掉最后一个右坐标以固定规。$X$ 有 $2m-1$ 个独立列，因为两层共同为零已迫使 $f$ 平移不变，从而 $f$ 为常数。删列不改变左零空间，原被删列是其余列之和的负数。对 $h\in\mathbb R^m,\gamma\in\mathbb R$ 定义
$$
 Z(h,\gamma)=\left(T^\top h-\gamma w,\; -(I+T^\top)h+\gamma w,\;h\right).
$$
则 $Z$ 的 $m+1$ 个列给出 $\ker X^\top$ 的全基。事实上三块向量之和须为零；由 $A_s$ 可逆，剩下的条件化为 $(T^\top-I)[h_1+(I+T^\top)h_2]=0$，恰得上式。

**三层判据。** 取 $D(t)=\operatorname{diag}(A R_s,-BtR_{s+1},Ct^2 R_{s+2})$，构造 $(m+1)\times(m+1)$ 对称二次矩阵多项式
$$
 Q_s(t)=t^2 Z^\top D(t)^{-1}Z .
$$
只需检验这个多项式的行列式。在 $t>0$，有
$$
 \dim\ker L_{[s]}(t)-1=\dim\ker Q_s(t),\qquad
 \tau_{[s]}(t)=\frac{\det(X^\top X)}{\det(Z^\top Z)}
                  \det D(t)\,t^{-2(m+1)}\det Q_s(t).
$$
为看第一式，把 $v\in\ker(X^\top DX)$ 映到 $DXv=Zh'$。反向可解 $Xv=D^{-1}Zh'$ 的充要条件为 $Z^\top D^{-1}Zh'=0$。第二式在互补的正交标准基上使用逆矩阵互补主子式公式，再恢复两个 Gram 行列式即可。$\det D(t)$ 正比于 $t^{3m}$。

**两端次数。** 每个删规后的单层秩恰为 $m$。所以三变量规余因子齐次次数 $2m-1$，每一层的次数至多 $m$。对相邻二层，它仅可写为 $U^{m-1}V^{m-1}(aU+b'V)$，且 $a,b'$ 均非零。理由是原相邻证明的兼容条件在此也充分：取其公共通量为 $w$，平移差像空间的唯一约束为 $w$ 正交，恰在 $\theta^\ast=(\alpha+b(v+1))/(\alpha+bv)$ 满足，$\alpha=(m^2+1)/2$；此时解出 $q$ 再由第一层解出左变量，即得非规向量。又因 $\theta=1$ 处规余因子非零，这个线性因子有且仅有上述非零根。代入 $(U,V,W')=(A,-Bt,Ct^2)$，最低 $t$ 次只来自层次数 $(m,m-1,0)$，最高次只来自 $(0,m-1,m)$。两项均继承相邻二层的非零系数。因此
$$
 \tau_{[s]}(t)=t^{m-1}P_{m,s}(t),\qquad
 P_{m,s}(0)\ne0,\qquad \deg P_{m,s}=2m .
$$

## 穿零次数与尾层修复

以有理插值从定义重建 $P_{m,s}$，只除正公因子，故整数多项式保留规余因子的符号。下表给出 Sturm 序列在 0 和 1 的符号变号数。各行的多项式均无重根，端点不为根。

| $m$ | 起层 $s$ | $V(0),V(1)$ | $(0,1)$ 的根数 |
|---:|---:|---:|---:|
| 3 | 0 | 5, 5 | 0 |
| 4 | 0、1 | 两者均为 6, 6 | 0 |
| 5 | 0 | 7, 6 | 1 |
| 5 | 1、2 | 两者均为 7, 7 | 0 |
| 6 | 0 | 9, 8 | 1 |
| 8 | 0 | 13, 11 | 2 |
| 10 | 0 | 17, 14 | 3 |

用正半轴的变量 $x=t/(1-t)$ 也能核对根数。按低到高次，将 $(1+x)^{2m}P_{m,0}(x/(1+x))$ 的系数符号写成连续段。$m=5,6,8,10$ 依次为 $+^8-^3$、$+^7-^6$、$+^6-^8+^3$、$+^6-^6+^6-^3$。Descartes 符号法则分别给出 1、1、2、3 的上界，各条隔离区间两端异号，故全部取到。这也直接比较了同一模型在截断前后的 Bernstein 系数变化。

故 $m=5$ 是任一连续真实三层首次出现穿零的最小维数；其根在 $(25215/32768,197/256)$。此例第一对的原权阈值 $19/26$ 已先经过。更能区分机制的是 $m=6$。其三层根在 $(18713/32768,9357/16384)\subset(57/100,4/7)$，两端 $57/100,4/7$ 的规余因子符号分别为正、负。在这一小区间及此前：

- 第一对为 $M_0-5tM_1$，首个非规阈值 $109/185>4/7$。
- 中后两层除去 $-5t$ 后为 $M_1-2tM_2$，首个阈值 $181/218>4/7$。
- 前后两层为 $M_0+10t^2M_2$，对应平移步长 $2b$ 时的负参数。二层唯一非规阈值为正，故对任意 $t>0$ 无非规核。

因此这次穿零需要三层同时出现。由于根简单，规补矩阵的秩恰减一，固定空间由一维增为二维。对 $m=8,10$ 不把有限根数随 $m$ 的变化外推为增长率。

恢复后续原始层会真实改变符号。固定 $t$，令 $L(u)=L_{[0]}(t)+u\sum_{v=3}^n(-1)^v\binom nv t^vM_v$。当 $(m,t)=(5,1)$ 或 $(6,4/7)$ 时，$u=0$ 的余因子为负，恢复到 $u=1$ 后为正。两条恢复路径各有且仅有一个简单根，分别在 $(16951/32768,2119/4096)$ 和 $(3/2048,49/32768)$。$0<u<1$ 是用来量化尾层影响的辅助变形。独立从全部真实层计算，完整 $m=3,4,5,6$ 在 $0<t\le1$ 的残余 Möbius 多项式分别有 7、16、29、46 个系数，全为正。这与后续冻结工作的有限回归相符；全 $m$ 的完整余因子是否不穿零仍待解。[全层外协方差与有限正性](https://github.com/awdawmip/enterprise-math/blob/251ed06be5fe036df4da4506d3d9bc6ec68ceb7b/research_returns/PERFECT_PRIME_AP_BINOMIAL_CAUCHY_LAYER_COFACTOR_POSITIVITY_RETURN_20260901.md) · [外旗标反例](https://github.com/awdawmip/enterprise-math/blob/688e516b85e2eb99a13e0fbe04b1507788c4a6de/research_returns/PERFECT_PRIME_AP_OUTER_CONDITIONAL_COVARIANCE_DETERMINANT_RETURN_20260901.md)

用标准 Python 3 执行 `python three_layers_check.py`。程序从原 Cauchy 条目直接组装有符号规余因子，作整数无分式消元、保号本原 Sturm 序列及有理根隔离；独立按插值平移重建 $X,Z$，在 12 个点逐分数核对两侧行列式。证书保存约去正公因子后的多项式全部整数系数，按次数递增排列。[复算程序](three_layers_check.py) · [精确证书](three_layers_checked.json)
