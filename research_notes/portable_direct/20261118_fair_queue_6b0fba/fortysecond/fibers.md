# 勾股参数二次交的有限域一阶矩与跨素数分布

取奇素幂 $q=p^n$ 和 $\mathbf F_q$ 的二次特征 $\chi$，规定 $\chi(0)=0$。对 $[r:s]\in\mathbf P^1(\mathbf F_q)$ 写
$$
 A=r^2-s^2,\quad B=2rs,\quad C=r^2+s^2,\quad P=A+B,\quad Q=A-B.
$$
令 $\mathcal U$ 为 $AB(A^2-B^2)\ne0$ 的参数开集。对其中的每一点，计射影二次交
$$
 \mathcal C_{P,Q}:\quad D^2+U^2=P^2Z^2,\qquad D^2+V^2=Q^2Z^2,
 \qquad a_q(P,Q)=q+1-\#\mathcal C_{P,Q}(\mathbf F_q).
$$
有理原件取 $Q=|A-B|$，方程只用到 $Q^2$。同一射影参数的不同代表给出同构的纤维。$\mathcal U$ 保留了约化后斜边 $C=0$ 而二次交仍光滑的参数。本文另给强制 $C\ne0$ 时的修正。

**一阶矩。** 记 $S_q=\sum_{\mathcal U(\mathbf F_q)}a_q(P,Q)$，并定义固定 CM 曲线 $F:y^2=(x-1)(x^2-1/2)$ 的迹 $c_q=q+1-\#F(\mathbf F_q)$。则
$$
 |\mathcal U(\mathbf F_q)|=q-5-2\chi(2),\qquad
 S_q=-4-2\chi(-1)-2\chi(-2)-\chi(2)c_q^2.                     \tag{1}
$$
因此总纤维点数是 $(q+1)|\mathcal U|-S_q$；参数集非空时再除以 $|\mathcal U|$ 即得平均点数。素数域有下表。前两列取唯一的正整数对 $p=x^2+2y^2$。

| $p\bmod8$ | 1 | 3 | 5 | 7 |
|---|---:|---:|---:|---:|
| $S_p$ | $-8-4x^2$ | $4x^2-4$ | $-4$ | $0$ |

研究对象来自 P11 对角固定轨迹的 Euclidean 参数与两二次交。先前材料已给出 genus 1 模型、有理挠点、奇偶局部 Kummer 像及固定 $(233,119)$ 上的下降问题。这里按有限域射影参数逐点等权，计整个射影纤维，包括 $D=0$ 与有理无穷点。对素数域，每个好参数都能由整数原始勾股参数得到，因 $s\ne0$ 可写为 $[r_0:1]$，再取大于 1 的偶整数 $r\equiv r_0\bmod p$、$s=1$。按整数斜边高度抽样、原题的严格不等式及恢复根的本原性均不在这里的计数条件中。[原二次交与严格条件 §§3–6](https://github.com/awdawmip/enterprise-math/blob/6bd2b264318a283e4a815473999ae72a409d1cb0/research_returns/P000_SIX_AXIS_P11_DIAGONAL_SHARED_LEG_PYTHAGOREAN_TRIPLE_RETURN_20260904.md) · [已有有理挠点与二同源](https://github.com/awdawmip/enterprise-math/blob/a68132d8f8155e94723533417e04fa45f7ea3d81/research_notes/owner_goal_20261016/p11_uniform_torsion/P11_UNIFORM_TORSION_AND_EMPTY_OR_INFINITE_STRICT_FIBER_PAPER.md) · [已有局部 Kummer 像](https://github.com/awdawmip/enterprise-math/blob/e7b9fb5084f93a9b2dbc16225629b667fb7bf46c/research_notes/owner_goal_20261016/p11_parametric_local_images/P11_PARAMETRIC_LOCAL_IMAGE_AND_DYADIC_OBSTRUCTION_PAPER.md)

## 一、从原始纤维到完备字符和

令 $t=B/A$，好斜率恰为 $G=\mathbf F_q\setminus\{0,1,-1\}$。在 $s=1$ 图内，参数方程 $tr^2-2r-t=0$ 有 $1+\chi(1+t^2)$ 个根。因此
$$
 |\mathcal U|=\sum_{t\in G}(1+\chi(1+t^2))=q-5-2\chi(2).
$$
末等式用 $\sum_t\chi(1+t^2)=-1$。这里保留映射 $[r:s]\mapsto t$ 的实际重数。

原件的四次模型 $Y^2=((P+Q)^2-T^2)(T^2-(P-Q)^2)$，经 $x=T/(2A),\ y=Y/(4A^2)$ 化为 $y^2=(1-x^2)(x^2-t^2)$。曲线有有理分支点，且 $(x,y)\mapsto(u,v)=(x^2,xy)$ 给出至椭圆曲线
$$
 E_t:\quad v^2=u(1-u)(u-t^2)
$$
的可分二次映射。选取有理原点并平移像点即为同源，故两条光滑射影曲线的 Frobenius 迹相同。记 $a(t)=-\sum_u\chi(u(1-u)(u-t^2))$，对 $t\in G$ 即为原迹。下文也在三个退化斜率使用同一字符和，那里只把它视作补项。

先在全部 $t$ 上求和。对 $u\ne0$ 有 $\sum_t\chi(u-t^2)=-\chi(-1)$，而 $\sum_u\chi(u(1-u))=-\chi(-1)$，故 $\sum_ta(t)=-1$。退化项为 $a(0)=1$ 与 $a(1)=a(-1)=\chi(-1)$。因此无权好斜率和
$$
 B_q=\sum_{t\in G}a(t)=-2(1+\chi(-1)).
$$
总矩由 $S_q=B_q+W_q$ 组成，$W_q=\sum_{t\in G}\chi(1+t^2)a(t)$ 是 Euclidean 映射引入的加权部分。

补全 $W_q$ 的 $t$，令 $v=t^2$，按原像数 $1+\chi(v)$ 拆为两项。第一项为
$$
 -\sum_u\chi(u(1-u))\sum_v\chi((u-v)(1+v))=-1-q\chi(2).
$$
内和在 $u\ne-1$ 时为 $-\chi(-1)$，在 $u=-1$ 时为 $(q-1)\chi(-1)$。第二项令 $X=-u,\ Y=v$，恰为 $-I_q$，其中
$$
 I_q=\sum_{X,Y}\chi\big(XY(X+1)(Y+1)(X+Y)\big).
$$
Ahlgren、Ono 与 Penniston 的定理 2.1 在 $\lambda=1$ 时给 $I_q=\chi(2)(c_q^2-q)$，适用所有奇素幂。在素数域，Greene–Stanton 已求出这个经典五因子和；Ono 推论 8(iv) 以 $p=x^2+2y^2$ 明列其值。本文使用这项先行定理，额外推导在于把原始 Euclidean 纤维计数化成这个和并算准光滑开集的边界。[Ahlgren–Ono–Penniston，定理 2.1](https://doi.org/10.1353/ajm.2002.0007) · [Ono，推论 8(iv) 及其历史归属](https://uva.theopenscholar.com/files/ken-ono/files/027.pdf#page=16)

由此 $\sum_{t\in\mathbf F_q}\chi(1+t^2)a(t)=-1-\chi(2)c_q^2$。三个退化斜率贡献 $1+2\chi(-2)$，给出
$$
 W_q=-2-2\chi(-2)-\chi(2)c_q^2.                                      \tag{2}
$$
加回 $B_q$ 即为 (1)。在 $p\equiv5,7\bmod8$ 时 $c_p=0$；在 $p\equiv1,3\bmod8$ 时 $c_p^2=4x^2$。首表即由此得出，尤其 $p\equiv5\bmod8$ 时加权部分为零而全和为 $-4$。

另有对 (2) 消去现象的初等检验。$t\mapsto h=(1-t)/(1+t)$ 置换 $G$。在 Legendre 形式 $v^2=u(u-1)(u-t^2)$ 上取 $(0,0)$ 为核点的二同源，商曲线为 $v^2=u(u+(1+t)^2)(u+(1-t)^2)$。尺度变换给出参数 $h$ 的 Legendre 曲线的 $-1$ 二次扭曲；转回 $E_t$ 仍有 $a(h)=\chi(-1)a(t)$。又 $1+h^2=2(1+t^2)/(1+t)^2$，故 $\chi(-2)=-1$ 时 $W_q=-W_q=0$。

## 二、斜边为零的边界及逐层提升

$C=0$ 等价于 $t^2=-1$。此时 $AB(A^2-B^2)\ne0$，每个这样的斜率对应唯一参数，曲线 $E_t$ 化为 $F_0:v^2=u-u^3$。设 $b_q=q+1-\#F_0(\mathbf F_q)$，若再限 $C\ne0$，须从 $|\mathcal U|$ 扣去 $1+\chi(-1)$，从 $S_q$ 扣去 $(1+\chi(-1))b_q$。例如 $p=13,29$ 的 $S_p$ 均为 $-4$，扣掉边界后分别为 $-16,+16$。在 $p=5$ 仅有两个 $C=0$ 的好参数，扣后参数集为空，故不取平均。

对环 $\mathbf Z/p^k$，只计约化在 $\mathcal U(\mathbf F_p)$ 的参数与点。固定任一好参数的任一提升，其射影纤维点数恰为 $p^{k-1}\#\mathcal C_{P,Q}(\mathbf F_p)$。因好斜率下两个二次式在射影仿射图中的雅可比秩为 2，每步三个局部坐标有一个自由的 $\mathbf F_p$ 方向；而基底点每步另有一个自由方向。故所有含参数的点对总数为
$$
 p^{2(k-1)}\big((p+1)|\mathcal U(\mathbf F_p)|-S_p\big).
$$
这里高次同余环中的抬升与 $\mathbf F_{p^k}$ 上新增的参数是两类不同计数。

对后者还可从 (1) 写出整个开曲面 $\mathscr X=\{([r:s],z):[r:s]\in\mathcal U,\ z\in\mathcal C_{P,Q}\}$ 的局部 zeta 函数。记 $\epsilon_j=(j/p)$，令 $T$ 为形式变量，则
$$
 Z(\mathscr X_{\mathbf F_p},T)=
 \frac{(1-pT)^4(1-T)(1-\epsilon_2 T)^2}
 {(1-p^2T)(1-\epsilon_{-1}T)^2(1-\epsilon_{-2}T)^2
  (1-\epsilon_2(c_p^2-2p)T+p^2T^2)}.                               \tag{3}
$$
按定义 $\log Z=\sum_{n\ge1}\#\mathscr X(\mathbf F_{p^n})T^n/n$。若 $\alpha+\beta=c_p,\ \alpha\beta=p$，则 $c_{p^n}^2=\alpha^{2n}+2p^n+\beta^{2n}$。将这一式代入 $(p^n+1)|\mathcal U|-S_{p^n}$，其中两项 $\pm2p^n\epsilon_2^n$ 相消，余下的幂和逐项产生 (3)。该式对应保留 $C=0$、排除四个退化斜率的开集。

## 三、让素数变化时，真零与趋零的区别

按大小均匀抽取奇素数，$S_p/p$ 的极限分布为
$$
 \tfrac12\delta_0+\tfrac14\operatorname{Law}(U)+\tfrac14\operatorname{Law}(-U),
 \qquad
 \Pr(U\in du)=\frac{du}{\pi\sqrt{u(4-u)}},\quad 0<u<4.
$$
其奇次矩均为零，第 $2m$ 次矩是 $\tfrac12\binom{4m}{2m}$（$m\ge1$），特别地二阶矩为 3。这是各素数上的**整族一阶迹和**的分布。

在分裂的两类 $p=x^2+2y^2$ 中，取 $x,y>0$，令 $\theta=\arg(x+i\sqrt2\,y)$。环 $\mathbf Z[\sqrt{-2}]$ 为范数 Euclidean 环，单位为 $\pm1$，每个这样的素数恰对应第一象限一个素元。$x$ 总为奇数，$y$ 偶与奇分别对应 $p\equiv1,3\bmod8$，即模理想 $(2)$ 的两个可逆剩余类 $1,1+\sqrt{-2}$。Mitsui 的素元定理适用于指定可逆类和开凸区域；在第一象限半径 $\sqrt X$ 的任一固定扇区内，主项正比面积，偏和去除对数权即得这两个类内分别角均匀分布。除 2 外的惰性有理素数在该环的素元都在实轴。表中的 $S_p/p$ 因而分别趋近 $-4\cos^2\theta,+4\cos^2\theta$。另外两个素数类的值均趋零，四个模 8 素数类各有密度 $1/4$。这证明所给混合分布；各阶矩由有界性与反正弦密度直接积分。[Mitsui 定理的可逆剩余类与凸区域表述，Kai 定理 1.2.1](https://arxiv.org/pdf/2209.11816v3#page=2)

真有 $S_p=0$ 的素数自然密度仅为 $1/4$。$p\equiv7\bmod8$ 全部命中；$p\equiv3\bmod8$ 中还要求 $x=1$，这种形如 $1+2y^2$ 的素数在 $X$ 内至多 $O(\sqrt X)$ 个。另一份 $1/4$ 的零原子来自 $p\equiv5\bmod8$ 时恒为 $-4$ 的全和经 $p$ 归一化后趋于零。

## 四、复算

同目录 <code>python fibers_check.py</code> 输出 <code>fibers_checked.json</code>，仅依赖标准库。程序对 3 至 251 的 53 个奇素数及六个真正的扩域（$3^2,3^3,5^2,7^2,11^2,13^2$），按原二次交逐斜率计射影点，另行枚举 Euclidean 参数、辅助三次曲线、五因子双和与斜边为零的边界。枚举仿射 $Z=1$ 图时直接乘两个平方的根数，再加 $Z=0,D=1$ 图的 $(1+\chi(-1))^2$ 个点。六个扩域另核对 (3) 的幂和。七个高次同余环直接计好参数以及两个射影图中的点，模 $5^3$ 计得 10000 对，模 $17^2$ 计得 64736 对。
