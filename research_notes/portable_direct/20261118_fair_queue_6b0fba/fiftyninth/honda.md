# 七次 Frobenius 能交换任意接近正交的两个 Prym 因子，却不能交换一对正交因子

取特征七曲线 $C_{46}$ 的四维 Prym $P$，以曲线 Jacobian 诱导的极化 $\lambda$ 定义 Rosati 对合 $\dagger$。在几何有理端同态代数 $\operatorname{End}^0(P)=M_2(F)$ 中，**不存在被七次 Frobenius $\pi$ 保持的无标记、互补且 $\lambda$-正交的两个秩一因子**。逐个保持被中心化子排除，交换两因子的障碍来自 $K=F^+=\mathbf Q(\sqrt{417})$ 上恰好两个二进素位。与此同时，原有理图像对应可以在 $K$ 的两个实嵌入同时逼近正交，第 3 节给出收敛阶为三的精确迭代。

## 1. 从曲线对称到二元范数方程

冻结的 $\mathbf F_7$ 模型为 $y^2=x^3-6x^2+36$，$w^2=y(x^2-12)$。在 $\mathbf F_{49}$ 取 $i^2=-1$，自同构 $\sigma(w,x,y)=(iw,x,-y)$ 满足 $\sigma^2=-1$ 于 Prym 上。因 $i^7=-i$，曲线上的态射关系是 $\pi\sigma=\sigma^{-1}\pi$，限制到 Prym 得 $\pi\sigma=-\sigma\pi$。记 $s=\pi^2$，$F=\mathbf Q(s)$，$L=F(\pi)$。四次 $h(s)=s^4+5s^3+245s+2401$ 和八次 $h(t^2)$ 均不可约。在 $\mathbf F_{49}$ 已有 $P\sim B^2$，$B$ 是绝对单纯的 $7$-秩一曲面，$\operatorname{End}^0_{\overline{\mathbf F}_7}(P)=\operatorname{End}^0_{\mathbf F_{49}}(P)=M_2(F)$。早期伴随矩阵稿 §3 展示的正交坐标对应辅助 Hermitian 矩阵 $H_0=\operatorname{diag}(1,7)$，同节还保留可变的非对角项。本题指定的是曲线诱导的实际 Rosati 对合。[原任务 R108](https://github.com/awdawmip/enterprise-math/blob/c0f816e2ab6be0145a3edd1a77488bddfd42a2f6/research_tasks/EMF6D046_R108_HONDA_TATE_CORRESPONDENCE_REDUCTION_GEN2_20260909.md) · [Honda–Tate 及几何端代数，§§4–7](https://github.com/awdawmip/enterprise-math/blob/574f53c7b37ae6703ade390df851d8822af6364c/research_notes/EM_FREE_F6D046_P46_P7_HONDA_TATE_20260904.md) · [原 Frobenius 交换矩阵](https://github.com/awdawmip/enterprise-math/blob/574f53c7b37ae6703ade390df851d8822af6364c/research_notes/EM_FREE_F6D046_P46_P7_MATRIX_IDEMPOTENT_DESCENT_20260904.md)

$L/F$ 的非平凡自同构为 $\tau(\pi)=-\pi$。它由 $\sigma$ 在 $L$ 上共轭实现。$\pi^\dagger=7/\pi$，$\sigma^\dagger=\sigma^{-1}=-\sigma$。记 $\rho=\dagger|_L$，则 $\rho(\pi)=7/\pi$，$\rho\tau=\tau\rho$。整体端代数中的 $\dagger$ 反转乘积次序。$\pi$ 在 $F$ 上线性，满足 $\pi^\dagger\pi=7$，所以它作为相似变换把正交补送到正交补。$L$ 与 $L\sigma$ 线性无交，维数给出 $M_2(F)=L\oplus L\sigma$。因此 $\pi$ 的中心化子恰为域 $L$，无秩一幂等元，而与 $\pi$ 反对易的元素恰为 $q\sigma$。

若 $e$ 是无序正交分解中一个像上的正交投影，则其余投影唯一等于 $1-e$。若 $\pi$ 交换两条像，则 $\pi e\pi^{-1}=1-e$。令 $T=2e-1=q\sigma$。由 $(q\sigma)^2=-q\tau(q)$ 和 $(q\sigma)^\dagger=-\tau\rho(q)\sigma$，可得所求交换正交对存在的充要条件
$$
 q\tau(q)=-1,\qquad \tau\rho(q)=-q . \tag{1}
$$
其中第一式单独就有实际解，第四、第五轮分别已得到具体的有理图像对应。也可用 $-\pi$ 或 $7/\pi$ 表示同一共轭作用，因为 $\pi^2$ 在中心。这些算子的来源与 Rosati 对乘积反序的作用各有明确位置。[第四轮的对应与次数下界](../fourth/honda.md) · [第五轮较小的四阶整对应](../fifth/honda_small.md)

令
$$
 y=s+49/s,\qquad d=y+14,\qquad
 \delta=\pi+7/\pi,\qquad \eta=\pi-7/\pi .
$$
有 $y^2+5y-98=0$、$d^2-23d+28=0$、$\delta^2=d$、$\eta^2=d-28$。实二次域 $K=\mathbf Q(d)$ 的两个实嵌入均有 $0<d<28$。$L=K(\delta,\eta)$ 在 $K$ 上为双二次扩张，$\rho$ 固定 $\delta$、反转 $\eta$，$\tau$ 同时反转两者。于是 $E=L^{\tau\rho}=K(\eta)$，(1) 的第二式等价于 $q=\delta z$、$z\in E$。代入第一式给出
$$
 N_{E/K}(z)=1/d
 \quad\Longleftrightarrow\quad
 d\in N_{E/K}(E^\times)
 \quad\Longleftrightarrow\quad
 (d,d-28)_K\text{ 为分裂四元数代数}. \tag{2}
$$
最后一步使用二次扩张范数和四元数分裂的经典等价，后一节也给出具体的整同余障碍。[Voight，《Quaternion Algebras》](https://doi.org/10.1007/978-3-030-56694-4)

## 2. 恰好两个坏素位，及实际的最小定义域

$417\equiv1\pmod8$，故 $2$ 在 $K$ 分裂，两处完备化均为 $\mathbf Q_2$。方程 $d^2-23d+28=0$ 的两根模 $256$ 为 $227,52$。逐处检验范数方程可用齐次锥 $X^2-(d-28)Y^2=d Z^2$。有理局部解必可缩放为整数本原三元组。

| $K$ 的位置 | 局部范数判定 |
|---|---|
| $2$，$d$ 奇 | $d\equiv3$、$d-28\equiv7\pmod8$。模 $4$ 要求 $X^2+Y^2=3Z^2$，迫使三坐标全偶。局部符号 $-1$。 |
| $2$，$d$ 偶 | 抽出平方因子 $4$ 后，锥写成 $X'^2-2wY^2=vZ^2$，$v=d/4\equiv5\pmod8$，$2w=(d-28)/4\equiv6\pmod8$。若 $X',Z$ 均奇，平方差模 $8$ 为 $4$，右侧 $2wY^2$ 只能为 $0,6$；若两者均偶，模 $4$ 又迫使 $Y$ 偶。两者异奇偶亦不合。局部符号 $-1$。 |
| $3$ | $d\equiv1$ 于余域，Hensel 引理给出单位平方。 |
| $7$ | $d\equiv0$ 的地方有 $d-28=-d(22-d)$，$22-d\equiv1\pmod7$ 为平方，$(d,-d)=+1$。另一处两参数为单位。 |
| 其余有限处及实处 | $N(d)=28$、$N(d-28)=168$；其余奇位上两参数皆为单位。实处 $d>0$。 |

两处二进否定任一处已足，表中也算齐所有局部符号。这里的除代数是控制 (2) 的辅助四元数代数；实际几何端代数仍是 $M_2(F)$。

**系数扩张的精确门槛。** 对有限全实扩张 $k/K$，在 $M_2(F)\otimes_K k$ 中使用延拓的 Rosati 对合。存在所求交换正交对，当且仅当在上述两个二进处的每个上方素位 $w$ 都有偶数局部度 $[k_w:\mathbf Q_2]$。理由是 (2) 在扩标量后仍成立，$E\otimes_K k$ 是由全负 $d-28$ 定义的二次域；$L\otimes_K k$ 可为 étale 代数，其 $\tau\rho$ 负特征部分仍是 $\delta(E\otimes_K k)$。四元数代数的局部不变量随标量扩张乘局部度，整体分裂等价于所有局部不变量为零。最小全局次数恰为二。一个可写出投影的选择是 $k=K(\sqrt d)$，其确为全实二次域，因为奇二进位的 $d\equiv3\pmod8$ 不是平方。在该系数代数中
$$
 T_0=\frac{(\pi+7/\pi)\sigma}{\sqrt d},\qquad
 T_0^\dagger=T_0,\quad T_0^2=1,\quad T_0\pi=-\pi T_0 . \tag{3}
$$
于是取 $(1\pm T_0)/2$。这只扩大中心的对应系数。把实际 Prym 改写在更大有限域上，其几何有理端同态代数始终是上述同一个 $M_2(F)$。

**有限域下降。** 每一对实际的有理正交互补因子都已在 $\mathbf F_{49}$ 定义。这样的对确实存在，对任意有理秩一像取其极化正交补即可。七次 Frobenius 若保持无标记二元集合，作用只能逐个固定或互换，前者已被中心化子排除，后者被表中障碍排除。由于 $\pi^{2}$ 是中心元，任意奇次扩域仍没有如此稳定的对，任意偶次扩域则逐个定义。此处考察指定几何子对象或其投影。对极化核三条直线之一 $H$，固定商 $q_H:P\to A_H=P/H$ 在 $\mathbf F_{7^3}$ 上定义，$q_H^*\lambda_H=\lambda$。有理同源共轭运输 Rosati 以及第三次 Frobenius，而 $\operatorname{Ad}(\pi^3)=\operatorname{Ad}(\pi)$。因此已标记的 $H$ 加上 $A_H$ 的一对无标记正交同源因子，首个共同定义域恰是 $\mathbf F_{7^6}$。这里的因子按有理同源计，主极化的整乘积分解另有条件。特征零模型的几何端域为 $\mathbf Q(i)$，连通 Sato–Tate 群为 $U(4)$，其分量群 $C_2$ 与此特纤维的二进局部符号具有各自的定义。[R105 分层输入](https://github.com/awdawmip/enterprise-math/blob/c0f816e2ab6be0145a3edd1a77488bddfd42a2f6/research_notes/EM_FREE_F6D046_R105_STATE_MACHINE_HANDOFF_20260909.md) · [三个实际主极化商](../thirteenth/theta.md)

## 3. 用原有理对应同时逼近两个实位的正交线

设 $q\in L$ 满足 $q\tau(q)=-1$，取已交换的斜投影 $e_\pm=(1\pm q\sigma)/2$。在每条像上重新取唯一自伴投影
$$
 P_\pm=\frac{e_\pm e_\pm^\dagger}{\operatorname{Trd}(e_\pm e_\pm^\dagger)} .
$$
分母是正的中心元，分子秩一，由二阶 Cayley–Hamilton 公式归一化即得幂等与相同像。$\pi$ 交换 $P_+,P_-$，但 $P_++P_-\ne1$。令 $w=q\rho(q)$，则 $\tau(w)=w^{-1}$、$\rho(w)=w$，在所有复嵌入上 $w>0$。两个迹分母同为 $k=(2+w+w^{-1})/4$，从 $(q\sigma)(q\sigma)^\dagger=w$ 即得。写
$$
 c=\operatorname{Trd}(P_+P_-)=1-1/k
   =\left(\frac{w-1}{w+1}\right)^2\in K . \tag{4}
$$
为验证中间等式，在任一实位的正定 Hermitian 空间中取正交归一基使 $e_+=\left(\begin{smallmatrix}1&a\\0&0\end{smallmatrix}\right)$。两条像为 $(1,0)$ 和 $(-a,1)$ 的线，$k=1+|a|^2$，故 $c$ 正是这两条线的夹角余弦平方。每个实位均有 $0<c<1$。某一嵌入若 $c=0$，则 $c$ 在数域中就是零，与 (2) 冲突。

**有理三次迭代。** 从任一这样的 $q$ 构造
$$
 q'=q\frac{w+3}{3w+1},\qquad
 c'=\frac{c^3}{(4-3c)^2}. \tag{5}
$$
代 $w\mapsto1/w$，分式因子取逆，故 $q'\tau(q')=-1$，仍给两条由 Frobenius 交换的实际有理曲面像。其 $w'=w(w+3)^2/(3w+1)^2$。相减分子为 $(w-1)^3$，相加分子为 $(w+1)(w^2+14w+1)$，代回 (4) 即得 (5)。对两个实嵌入各有 $0<c_n\le c_0^{3^n}$，所以障碍禁止达到正交，仍允许同时任意逼近，所有步骤都在实际的有理对应代数中。逐个实嵌入取正平方根，记 $\ell=(\sqrt w-1)/(\sqrt w+1)$。经典 Cayley 分式的三次恒等式给 $\ell\mapsto\ell^3$，因为 $\sqrt{w'}=\sqrt w(w+3)/(3w+1)$；从而有精确值 $c_n=4\ell^{2\cdot3^n}/(1+\ell^{2\cdot3^n})^2$。每个 $q_n$ 可模 $h(t^2)$ 化为七次以下有理多项式，故 $(1-\sigma^2)(1\pm q_n(\pi)\sigma)/4$ 是原曲线图像的有理组合。清分母会改变有效分量的重数，此式不提供统一双次数界。

取第五轮较小四阶载体的
$$
 a=-49-70t+35t^2-12t^3+4t^4,\qquad b=196-35t+35t^2-11t^3+t^4,\qquad q=b/\tau(a).
$$
这两条像原有带符号图像的正负有效部分双次数各为 $(448,24304)$。实际计算得
$$
 c_0=\frac{10752+5217d}{175561},\qquad
 175561c_0^2-141495c_0+12348=0 .
$$
按 $d$ 从小到大的两个实位，$c_0$ 分别落在 $(0.099568,0.099569)$、$(0.706390,0.706391)$。第 3 次迭代的两值约为 $7.99\times10^{-43}$ 和 $2.35\times10^{-14}$；此时 $c_3$ 在基 $1,d$ 中两有理系数的分子或分母最长达 499 个二进位（位长按复算程序的整数 bit_length 计）。迭代给出 $C_{46}\times C_{46}$ 内可取像的有理对应。与指定二属模型 $C_7$ 之间的小双次数除子仍待构造。[原小系数证书](../fifth/honda_small.md) · [二属曲面代表](https://github.com/awdawmip/enterprise-math/blob/574f53c7b37ae6703ade390df851d8822af6364c/research_notes/EM_FREE_F6D046_B_GENUS2_WEIL_RESTRICTION_20260904.md)

## 4. 复算

运行 `python honda_check.py`，使用 Python 3、SymPy 1.14。脚本直接在 $\mathbf Q[t]/(h(t^2))$ 中实现 $\tau,\rho$ 与交叉乘法。对有理代数的 16 个基元逐一检查 $\dagger^2=1$，对全部 256 个有序基元对检查 $(XY)^\dagger=Y^\dagger X^\dagger$。脚本逐三元组核验两处本原锥模 4、8 的空集，以实际秩一投影乘积复算 (4) 和 (5) 的前三步。浮点近似只用于显示最后的两个实位，判等均在数域内完成。[程序](honda_check.py) · [完整结果](honda_checked.json)
