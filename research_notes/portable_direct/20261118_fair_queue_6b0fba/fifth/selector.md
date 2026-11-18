# Legendre 对称四次的秩五选择子，一个精确 CM 共轭轨道与扩张常数障碍

在 Legendre 椭圆族的纯对称四次变分中，取由椭圆周期对称张量确定的分裂归一化。两个共轭 CM 点的目标无关选择子为
$$
 [A:B:C]=[0:-10+6\sqrt3:1],\qquad [0:-10-6\sqrt3:1].
$$
选择子的最小坐标域是 $\mathbb Q(\sqrt3)$。保持第一奇周期时，在同一 CM 点把第三奇周期改动任意非零常量倍的全纯周期，选择子就离开 $\mathbb P^2(\overline{\mathbb Q})$。这两条结论都只用奇周期，全程未使用 $1/\pi^2$ 级数求值。

## 模族、正规化与两条射影坐标

取 $E_x:y^2=u(1-u)(1-xu)$，令 $x=\lambda(\tau),\,z=x/16,\,q=e^{\pi i\tau},\,t=\log q$，在正虚轴取实对数。$D=q\,d/dq,\ \theta=z\,d/dz$。写 $W=\vartheta_3(\tau)^4$。椭圆周期 $F={}_2F_1(1/2,1/2;1;x)=\vartheta_3^2$ 满足 $(1-x)\theta^2F-x\theta F-xF/4=0$，另一个周期可取常数倍 $Ft$。秩五系统为上述二阶方程的 $\mathrm{Sym}^4$，局部基底取
$$
 w_j=W^2t^j/j!,\qquad 0\le j\le4 .
$$
绕 $x=0$ 的单值变换在五维空间上有一个幺幂 Jordan 块。由于 $q/z\to1$，对数坐标和 Frobenius 首项吻合。此处的第三奇周期是对称张量基给出的 $w_3$，其相对 $w_0$ 的扩张常数为零。四阶 Wronskian 也给出同一归一化。取四阶代数扭转基 $y_j=\sqrt{1-x}\,\vartheta_3^6 t^j/j!$（$0\le j\le3$），则 $y_0\theta y_1-y_1\theta y_0=y_0^2/\delta=W^2$，$\delta=D\log z$。这是秩五模子族，不涵盖具有预定非零 Gamma 扩张的 Guillera 超几何族。

按 CP19 记 $K_{\rm Yuk}$ 为 Yukawa 耦合，$T$ 为零常数项的瞬子级数，$R=P(z)^{1/4}$。本族的多项式对数基给出 $K_{\rm Yuk}=1,T=0,h=0$。用 Jacobi 导数式及 CP19 的 $w_0=\delta^2/(RK_{\rm Yuk})$、$L=\delta^3/(R^2K_{\rm Yuk})$ 收得
$$
 \delta=(1-x)W,\quad R=(1-x)^2,\quad L=W^3/(1-x),\quad
 \ell=\log|q|=t,\quad U=t^2/3,\quad V=-t .
$$
正虚轴上的 $x$ 在 $(0,1)$ 内且 $t\ne0$，所有分母均非零。写
$$
 s=E_2(\tau)/W,\qquad
 e=E_2^*(\tau)/W,\qquad E_2^*=E_2-\frac{3}{\pi\,\operatorname{Im}\tau}.
$$
其中 $W$ 有模权二，$E_2$ 是拟模形式，$E_2^*$ 的非全纯校正使它有模权二。$e=s+3/(Wt)$ 正好吸收实镜面对数，公式无需借用偶部目标尺度。则两条 CP19 项 $b=B/C,\ \alpha=A/C$ 显式化为
$$
 b=\frac{1-3x-e}{1-x},\qquad
 \alpha=\frac{e^2+(4x-2)e+7x^2-7x+1}{3(1-x)^2}.
 \tag{1}
$$

推导时先代入 $b=-3/(\delta t)-\theta\log L$ 与
$\alpha=3/(\delta t)^2-b\,\theta\log w_0-\theta^2w_0/w_0$。Jacobi 与 Ramanujan 导数恒等式给出
$$
 D\log W=\frac{W(s+2x-1)}3,\qquad
 \theta s=-\frac{s^2+2(2x-1)s+1-x+x^2}{6(1-x)} .
$$
这里 $D E_2=(E_2^2-E_4)/6$ 且 $E_4=(1-x+x^2)W^2$。将 $s+3/(Wt)$ 合并为 $e$ 即得 (1)。也可独立使用 CP18 的两个奇行。设 $S=\alpha+b\theta+\theta^2$，乘积求导给出
$$
 S(w_0t)=S(w_0t^3/6)=0,\qquad
 S(w_0)=3w_0/(\delta t)^2 .
 \tag{2}
$$
因此 (1) 确为两奇行的有符号最大子式比。

## 求值、共轭与类域

令 $\tau_+=i\sqrt3,\ \tau_-=-1/\tau_+=i/\sqrt3$。六角椭点 $\rho=(\tau_++1)/2$ 处 $E_4(\rho)=E_2^*(\rho)=0$，分别由模权四、二和三阶稳定子给出。经典二分恒等式为
$$
 E_4((\tau+1)/2)=(1-16x+16x^2)W^2,\qquad
 E_2^*((\tau+1)/2)-2E_2^*(\tau)=(2x-1)W .
$$
第一式由 theta 二倍角公式和 $E_4=(1-x+x^2)W^2$ 得到。第二式可对 $2E_2(2\tau)-E_2(\tau)=(\vartheta_3^4+\vartheta_4^4)/2$ 依次使用模变换 $S,T$ 得到。因为 $\operatorname{Im}((\tau+1)/2)=\operatorname{Im}(\tau)/2$，改用 $E_2^*$ 后这条差分恒等式保持成立。代入得
$$
 x_+=(2-\sqrt3)/4,\qquad e_+=(1-2x_+)/2=\sqrt3/4 .
$$
根的选择由 $\lambda(iy)<1/2$（$y>1$）确定。模反演给出 $x_-=1-x_+$ 和 $e_-=-e_+$，后一个负号来自 $W(-1/\tau)=-\tau^2W(\tau)$。这正是同一个二次共轭对 $x,e$ 的作用。将 $e=(1-2x)/2$ 代入 (1)，得到
$$
 \alpha=\frac{16x^2-16x+1}{12(1-x)^2}=0,\qquad
 b=\frac{1-4x}{2(1-x)}=-10\pm6\sqrt3 .
$$
由 $b^2+20b-8=0$ 的既约性即知最小实坐标域。$\alpha=0$ 是奇行给出的精确退化，$\operatorname{rank}=2$ 仍成立。

记 $K_0=\mathbb Q(\sqrt{-3})$。两点的椭圆自同态序的判别式为 $-12$，相应类数为一，未加水平结构的环类域是 $K_0$。选择子使用水平二的 $\lambda$。合成域 $K_0(\sqrt3)=K_0(i)$ 恰为导子四、判别式 $-48$ 的环类域。确实，对与 $2$ 互素的理想 $\mathfrak a$，$K_0(i)/K_0$ 在 $i$ 上的 Artin 特征为 $\chi_{-4}(N\mathfrak a)$。射线模 $4$ 的主理想条件及模 $4$ 同余于有理奇数的生成元均被其消去，因为有理奇数的范数是 $1\bmod4$。故它通过导子四的环类群。范数为 $7$ 的素理想给非平凡值，而环类数公式为 $4(1+1/2)/3=2$。这一非平凡自同构固定 $\sqrt{-3}$、交换 $\sqrt3$ 的两个符号，正好交换两条选择子。由此也区分了未标记 CM 曲线的域与水平二选择子实际所需的域。

## 唯一代数射线与扩张障碍

在上述任一 CM 点，仅保留第一奇行 $(w_0t,\theta(w_0t),\theta^2(w_0t))$ 即已限定一条射影直线。其 $C=1$ 图斜率为
$$
 m=-\frac{\theta(w_0t)}{w_0t}
   =-\frac{2(e+2x-1)}{3(1-x)}+\frac{1}{\delta t}.
 \tag{3}
$$
此数超越。用 Nesterenko 的模函数代数独立性定理，$e^{2\pi i\tau},E_2(\tau),E_4(\tau),E_6(\tau)$ 生成域的超越次数至少三。此处 $E_2=e W+3/(\pi\,\operatorname{Im}\tau)$，$E_4\in\overline{\mathbb Q}W^2$。由 $E_6^2=E_4^3-1728\Delta$ 和 $j=256(1-x+x^2)^3/[x^2(1-x)^2]$ 知 $E_6$ 也在 $\overline{\mathbb Q}W^3$。因此 $e^{2\pi i\tau},W,\pi$ 代数独立，特别是 $\pi W$ 超越。式 (3) 的第二项是 $(\pi W)^{-1}$ 的非零代数倍，第一项代数。

一条含有已知代数点且斜率超越的直线无法再含第二个代数点，其无穷远点也不是代数点。故分裂选择子是第一奇行平面方程下的**唯一代数射线**。第一奇行本身不可能等于一个周期乘以代数行，因为一阶导数与函数值之比由 (3) 给出，其值超越。本例的正面结论直接来自子式比，严格超出了 CP17 的逐行周期因子充分条件。

最后令 $d\in\mathbb C$，把第三奇周期改为 $w_0(t^3/6-d)$。第一行保持不变，原分裂选择子作用在新第三奇周期上等于 $-3d\,w_0/(\delta t)^2$。若 $d\ne0$，它已不满足第二行。两行始终独立，因为除去 $w_0$ 并以 $d/dt$ 记导数后，两行的后两列为 $(1,0)$ 与 $(t^2/2,t)$。换回 $\theta$ 和权因子只引入可逆的三角列变换。故新选择子唯一且不代数。此论断覆盖 $C=0$ 图边界及任意非零 $h\zeta(3)$，无需假定 $\zeta(3)/\pi^3$ 的任何超越性。它比较的是**同一分裂模族内改变第三行**的效果。其他秩五族的 Yukawa、第一行和规范化可同时变化。

## 适用范围与证书

冻结材料已给出 CP17 的条件下降、CP18 的子式定义和 CP19 的两条通用镜面坐标。后续 CP20–34 涉及中间 Tate 线、实现分离与 $p$ 进精度。早期同号 CP19 还排除了由单一低秩 Hadamard 因子推出高秩选择子的方案。此处使用实际的秩五对称张量系统并给出其共轭轨道。一般情形中，非退化奇行平面在给定数域上有定义、且在各算术共轭处协变，即为项目选择子下降与协变的充要条件。这个纯模例说明，CM 模参数即使完全确定，也不能单独替代对奇行扩张常数与 Gauss 平面的控制。原 Guillera 非分裂族两个特值的下降仍为独立问题。

经典输入是 Jacobi 与 Ramanujan 恒等式、椭点消失、环类群互反律及 Nesterenko 定理。本笔记推得秩五显式坐标、该水平二共轭轨道和扩张刚性。运行同目录的 selector_check.py 需 Python 和 SymPy（实测 1.14.0）。脚本独立用链式法则复算两条 CP19 坐标、两条奇行与斜率，精确检查共轭与最小多项式，并在 $q^{24}$ 以内逐项核对两条半周期恒等式。有限展开用于独立复核，域结论依靠上述恒等式与证明。

[冻结任务书](https://github.com/awdawmip/enterprise-math/blob/c0f816e2ab6be0145a3edd1a77488bddfd42a2f6/research_tasks/1195_RANK5_SELECTOR_GALOIS_CLASSFIELD_GEN2_20260909.md) · [CP17](https://github.com/awdawmip/enterprise-math/issues/1195#issuecomment-5576393018) · [CP18](https://github.com/awdawmip/enterprise-math/issues/1195#issuecomment-5576406515) · [CP19](https://github.com/awdawmip/enterprise-math/issues/1195#issuecomment-5576426514) · [CP34 后续交接](https://github.com/awdawmip/enterprise-math/issues/1195#issuecomment-5588899198) · [经典 theta 变换](https://dlmf.nist.gov/20.7) · [Almkvist–Guillera](https://doi.org/10.1007/978-1-4614-6642-0_2) · [Nesterenko 超越性定理](https://doi.org/10.1070/SM1996v187n09ABEH000158)
