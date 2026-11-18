# 双次数 $(448,24304)$ 的四阶 Honda–Tate 对应

在第四组同一条 $C=C_{46,7}$ 上，用七次 Frobenius 和原曲线自同构的图像，可以构造一对新的曲面像。两个整对应的正负有效部分各自都有双次数 $(448,24304)$。上一包的四阶对应给出的界为 $(114480,5621868)$。此处的曲面仍属于 $B$ 的同源类，七次 Frobenius 交换两条像。[前篇的曲线、投影与四阶下界](https://github.com/awdawmip/enterprise-math/blob/82555c4e618ab18f47c1ee6ad5226d7475e2a7e8/research_notes/portable_direct/20261118_fair_queue_6b0fba/fourth/honda.md)

## 1. 小整系数证书

沿用推图约定。令 $t=\pi$ 表示曲线七次幂态射在 Prym $P$ 上诱导的 Frobenius，取 $i^2=-1$ 于 $\mathbf F_{49}$。四阶曲线自同构 $\sigma(w,x,y)=(iw,x,-y)$ 满足 $z=\sigma^2$ 在 $P$ 上等于 $-1$。记 $f(t)=t^8+5t^6+245t^2+2401$，$\tau(t)=-t$，则 $\sigma a=\tau(a)\sigma$。算术在 $L=\mathbf Q[t]/(f)$ 中进行。取
$$
\begin{aligned}
a(t)&=-49-70t+35t^2-12t^3+4t^4,\\
b(t)&=196-35t+35t^2-11t^3+t^4.
\end{aligned}
$$
整系数多项式恒等式 $a\,\tau(a)+b\,\tau(b)=17f$ 给出
$$
q'=\frac{b}{\tau(a)}\in L,\qquad q'\tau(q')=-1,\qquad
Q'=q'\sigma,\qquad e'_\pm=\tfrac12(1\pm Q').
$$
于是 $Q'^2=1,\ \pi Q'\pi^{-1}=-Q'$。在 $\operatorname{End}^0_{\mathbf F_{49}}(P)=M_2(\mathbf Q(\pi^2))$ 中，这对互补投影由 Frobenius 交换，各秩一。令 $T_\pm=a\pm b\sigma$，由
$$
T_\pm=(1\pm q'\sigma)a
$$
及 $a$ 在 $L$ 中可逆，得 $\operatorname{im}T_\pm=\operatorname{im}e'_\pm$。

整曲线上的对应为 $(1-z)T_\pm$。将乘积展开为有符号图像和，按 $\Gamma_{\pi^j\sigma^k}$ 中的 $j=0,1,2,3,4$ 分组，每个有效部分的分组重数为 $245,105,70,23,5$。图像的双次数为 $(1,7^j)$，故两个投影方向的总次数分别为
$$
\sum_j (|a_j|+|b_j|)=448,\qquad
\sum_j 7^j(|a_j|+|b_j|)=24304.
$$
这给出总双次数的上界。最大 Frobenius 指数 $4$ 则已经最小，原因是 $j\le3$ 时非零秩一元的范数多项式既应被 $f$ 整除，又至多六次，而在纯虚轴上它是两个模平方之和。低双次数 $C_{46}\times C_7$ 对应和指定 $J(C_7)$ 的显式同源仍待确定。

## 2. 两种归一化与自然极化

同一个 $T=T_+$ 还满足 $T^2=dT$，其中 $d=a+\tau(a)=2(4t^4+35t^2-49)$ 是非零中心元。由此得到另一对互补幂等元 $T/d$ 与 $(\tau(a)-b\sigma)/d$。它们不由七次 Frobenius 互换，因为共轭 $T$ 给出 $a-b\sigma$，且 $a\ne\tau(a)$。为了同时取得小整分子和 Frobenius 交换性，上一节直接以 $q'=b/\tau(a)$ 定义有理投影，整分子仅用来取得它们的像。

用自然 Prym 极化的 Rosati 对合 $\pi^\dagger=7/\pi$、$\sigma^\dagger=-\sigma$ 可独立检查新选择。$Q'-Q'^\dagger$ 的 $\sigma$ 系数为 $q'(t)+q'(-7/t)$，约化成模 $f$ 的七次以下代表时，常数项为 $-389/23207$。因此 Frobenius 交换的这两个投影均非自伴，两条像不正交。迹归一化的 $T/d$ 同样非自伴，其与伴随之差的 $\sigma$ 系数的常数项为 $1075/7234$。所有投影等式均指图像诱导的有理端同态，整图像仍以带符号除子出现。[复算程序](honda_small_check.py)
