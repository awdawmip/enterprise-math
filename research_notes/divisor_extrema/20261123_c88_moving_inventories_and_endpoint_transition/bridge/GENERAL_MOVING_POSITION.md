# C88　任意移动中间位置的一致跟踪

本篇补足 MOVING_ENDPOINT_BRIDGE.md 中未直接处理的移动内点近共振。它沿用该文的原 H(0,1)、整数安排、准确有限谱、\(A,B,D,\ell,\theta,L_c\) 等全部记号，并继续保留全库存竞争者。

## 1. 统一定理

令 \(F_\theta(a)\) 为 C84 的独立三相位 Haar 唯一函数，位移为

\[
l_\theta(u,v)=(u,(1-\theta)u+\theta v,v),\qquad 0\le\theta\le1,
\]

端点取连续延拓 \(F_0=F_1\)。令

\[
\Phi_\theta(L)=2\int_\Delta F_\theta(L^2J(X))\,dX,
\qquad \Delta=\{0<y<x<1\}.
\]

**定理（任意移动位置的全库存跟踪）。** 对整数序列 \(1\le A<B\)，若

\[
B=o(c),\qquad
R_c:=\frac{A(B-A)}{\sqrt{cB}}
=\frac{\theta(1-\theta)}\ell\longrightarrow\infty,
\qquad 0<L_-\le L_c\le L_+<\infty,
\tag{1}
\]

则

\[
\boxed{
\sup_{\alpha\in\mathbb T^3}
\left|V_c^{(3)}(\alpha)-\Phi_{\theta_c}(L_c)\right|
\longrightarrow0.
}
\tag{2}
\]

不要求 \(\theta_c\) 收敛、有理极限、固定分母或远离两个端点。条件 (1) 自动推出 \(B/c^{1/3}\to\infty\)，因为 \(R_c\le1/(4\ell)\)。

**近距版本。** 若只要求 \(B=o(c)\)、\(B/c^{1/3}\to\infty\)，则对任意 \(1\le A<B\)，同一式 (2) 对近距唯一率成立。近距半径的条件仍为 \(r_c\to0\)、\(cr_c/D\to\infty\)。在已知 \((G,B_1)\) 全宏观单原像的固定源区域，可允许全库存竞争者。

本定理是充分条件；未证明 \(R_c\to\infty\) 必要。它也不把紧倍率跟踪扩充为任意 \(L_c\to0\) 或 \(L_c\to\infty\) 的联动渐近。

## 2. 已有桥接步骤全部对位置统一

MOVING_ENDPOINT_BRIDGE.md 中以下步骤不需要 \(\theta\to0\)：

1. 准确二差积分表达、\(Q_c\to B_2\)、同格误差 \(4/(L_cR_c)\)。因此 (1) 排除全部宏观远支。
2. 用外端 \((U_c,P_{z,c})\) 反演得到全部局部有效整数位移 \(O(D)\)。
3. 首末空间线性化误差 \(O(\ell)\)，中间插值误差 \(O(\theta(1-\theta)B/c)\)。
4. 八角盒稳定性及权重沿适配流的统一 Lipschitz 界；两端坐标一直保留，常数不依赖位置。
5. 强总和 Fourier 模式的整数源步消去与原点等度连续性。

对辅助概率，所有格统一有

\[
|q_\theta(\Lambda)-q_{\theta'}(\Lambda)|\le C|\theta-\theta'|,
\tag{3}
\]

因为可能进入窗口的格向量首末坐标绝对值均不超过一，中间标记变化至多 \(2|\theta-\theta'|\)。因此 \(F_\theta(a)\) 对位置统一 Lipschitz，对 \((\theta,a)\in[0,1]\times(0,\infty)\) 联合连续，\(\Phi_\theta(L)\) 亦联合连续。

在任意子列选取 \(\theta_c\to\theta_*\)、\(L_c\to L\)，原点平均的 Haar 论证遂给 \(\Phi_{\theta_*}(L)\)。唯一新增问题是总和为零的固定 Fourier 模式在 \(0<\theta_*<1\) 时可能接近一阶共振。

## 3. 任意非零 \(B_1,B_2\) 组合的适配流导数非退化

置

\[
\mathcal V=(\operatorname{Hess}G)^{-1}\nabla G.
\]

**引理。** 对任意实数 \((a,b)\ne(0,0)\)，函数

\[
\mathcal V(aB_1+bB_2)
\tag{4}
\]

在每一个正规符号片上都不恒为零；其零集面积为零。

证明直接使用 C82 原谱，而非一般位置假设。其径向谱表达为

\[
G(X)=C\frac{A_0^{19/5}d^{14/3}|1-A_0||1-d|}
{(1+m)(1+mA_0)},
\]

\[
A_0=4x^{15/4},\qquad d=4(y/x)^{9/4},\qquad
m=\frac7{16}A_0^4d.
\tag{5}
\]

这里 \(A_0\) 是谱变量，区别于整数内间距 \(A\)。沿小正径向尺度，取一片固定的 \(d\ne1\)，原谱的前两个齐次项为

\[
G=f+h+\text{更高阶项},\qquad
\deg f=\kappa=\frac{57}4,\qquad
h=-4x^{15/4}f,\quad\deg h=18.
\tag{6}
\]

分母的首个更正相对阶数为 15，晚于第二项的相对阶数 \(15/4\)。在 \(d<1\) 的小比值锥内，除去正的共同常数，

\[
f=x^{15/4}y^{21/2}-4x^{3/2}y^{51/4}.
\tag{7}
\]

C82 已核实 \(\operatorname{Hess}f\) 在充分小而固定的 \(y/x>0\) 上可逆。齐次恒等式给

\[
(\operatorname{Hess}f)X=(\kappa-1)\nabla f,
\qquad
(\operatorname{Hess}f)^{-1}\nabla f=X/(\kappa-1).
\tag{8}
\]

由 \(B_1=-(E+3/4)G\)、\(B_2=(E+7/4)(E+3/4)G\)，前两项分别是

\[
B_1=-15f-\frac{75}4h+\cdots,
\qquad
B_2=240f+\frac{5925}{16}h+\cdots.
\tag{9}
\]

若 \(-15a+240b\ne0\)，则 (4) 的首齐次项为

\[
\frac{\kappa}{\kappa-1}(-15a+240b)f\ne0.
\]

若首项消失，则 \(a=16b\)，且 \(b\ne0\)。此时组合函数本身的 \(f\) 项完全消失，其 \(h\) 系数为

\[
-\frac{75}4(16b)+\frac{5925}{16}b
=\frac{1125}{16}b\ne0.
\]

利用 (8)，(4) 的首项变为 \((1125b/16)\,18h/(\kappa-1)\ne0\)。适配流更高阶项不能作用于已经精确取消的 \(f\) 项产生补偿。

最后，将绝对值符号固定后，\(G\) 与一个共同的正象限代数有理谱仅差整体符号；\(\mathcal V\) 不随整体符号改变，\(B_j\) 随之整体变号。清除 \(\det\operatorname{Hess}G\) 及正分母，再采用正根坐标，(4) 恒零于任一开片会迫使同一个代数表达式恒零，与刚得到的小径向非零首项矛盾。因此它在每个正规符号片均不恒零；解析零集的面积为零。证毕。

## 4. 内点近共振的固定模式消去

取非零整数模式 \(k=(k_0,k_1,k_2)\)，并设 \(k_0+k_1+k_2=0\)。准确相位为

\[
\phi_{k,c}
=W_{1,c}(k_1\theta_c+k_2)P_{z,c}
-\frac{W_{2,c}}2k_1\theta_c(1-\theta_c)Q_c,
\tag{10}
\]

其中

\[
W_{1,c}=\lambda_cz=L_cc/D,\qquad
W_{2,c}=\lambda_cz^2=L_c/\ell.
\tag{11}
\]

若 \(\theta_*\in\{0,1\}\)，MOVING_ENDPOINT_BRIDGE.md 已以尺度 \(L_cAD\) 或 \(L_c(B-A)D\) 消去靠端相位，以 \(W_1\) 消去其余模式。

现在设 \(0<\theta_*<1\)。如果 \(k_1=0\)，则 \(k_2\ne0\)，(10) 的主尺度为 \(W_1\to\infty\)，归一主函数为 \(k_2B_1\)。如果 \(k_1\ne0\)，定义

\[
T_c=\max\left\{
|W_{1,c}(k_1\theta_c+k_2)|,
\frac{W_{2,c}}2|k_1\theta_c(1-\theta_c)|
\right\}.
\tag{12}
\]

第二项趋于无穷，所以 \(T_c\to\infty\)。再取子列，使两个有号系数除以 \(T_c\) 分别趋于 \(a,b\)，且 \(\max(|a|,|b|)=1\)。由准确差商的固定阶导数收敛，

\[
\phi_{k,c}/T_c\longrightarrow aB_1+bB_2
\tag{13}
\]

于所需的 \(C^2\) 意义成立。第 3 节引理保证它沿适配流的导数几乎处处非零。在避开其零集的紧流片上，Fourier 权重仍有不依赖 \(\theta_c\) 的流 Lipschitz 界，分部积分使模式积分为 \(O(T_c^{-1})\)。源和到积分误差为 \(O(1/B+1/D)\)，因为 \(T_c=O_k(W_1)\)。所以该模式趋零。

这处理了 \(\theta_c\) 以任意速度趋近有理共振的情况，也包括混合比 \(W_1(k_1\theta_c+k_2)/W_2\) 有有限非零极限的情况。它没有把有限共振直接替换为独立相位假设。

## 5. 完成统一跟踪

每个固定非零模式均被消去，原点平均有 Haar 极限，原点渐近等度连续。故每一满足 \(\theta_c\to\theta_*\)、\(L_c\to L\) 的子列都在全部格原点上一致趋于 \(\Phi_{\theta_*}(L)\)。再由 \(\Phi\) 的联合连续性和紧性，得到原序列的跟踪式 (2)。

定理 A 的移动端点结果是本定理的特例。对于首末距离固定在外层渐近区间的设计，\(R_c\) 是真实三次读数所提供的二阶宏观分辨率；它趋于无穷即可使同一个辅助三相位函数跟踪任意移动中间位置。

## 来源与新增内容

直接输入同 MOVING_ENDPOINT_BRIDGE.md。谱 (5) 来自 C82 CROSS_PHASE.md；齐次项 (7) 及其 Hessian 非退化亦在 C82 已核对。本篇新增的是两项库存谱任意非零线性组合的流导数引理、内点近共振分流以及任意移动位置统一跟踪定理。全部证明为解析推导，不依赖抽样观察。
