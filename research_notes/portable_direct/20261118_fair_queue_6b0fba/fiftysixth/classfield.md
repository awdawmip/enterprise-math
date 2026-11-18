# 矩形 CM 点的秩五选择子生成整个实坐标域

在第 5 轮固定的 Legendre 纯对称四次族中，取正虚轴上的分裂奇周期归一化。设 \(\tau=iy,\ y>0,\ \tau\) 虚二次，\(K=\mathbb Q(\tau)\)，\(\operatorname{End}(\mathbb C/(\mathbb Z+\tau\mathbb Z))=\mathcal O_f=\mathbb Z+f\mathcal O_K\)。记 \(H_g\) 为序 \(\mathcal O_g\) 的环类域，\(\iota\) 为当前复嵌入的共轭。对两个原始奇行子式比 \(\alpha=A/C,\ b=B/C\)，有
\[
 \boxed{\quad\mathbb Q(\alpha,b)=\mathbb Q(\lambda(\tau))
   =H_{2f}^{\langle\iota\rangle},\qquad K(\alpha,b)=H_{2f}.\quad} \tag{1}
\]
同一对读数定义的代数逆式一般有两个根，但其中一个绝不可能是这一矩形 CM 点的坐标共轭。式 (1) 适用于所有正虚轴 CM 点。第 5 轮的判别式 \(-12\) 是二次实例；下文另给判别式 \(-64\) 的四次实例，两条原始读数在该点各自就能生成全域。[原任务与 CP17–19](https://github.com/awdawmip/enterprise-math/blob/c0f816e2ab6be0145a3edd1a77488bddfd42a2f6/research_tasks/1195_RANK5_SELECTOR_GALOIS_CLASSFIELD_GEN2_20260909.md) · [第 5 轮奇行推导与扩张常数](../fifth/selector.md)

## 一、原读数和 CM 共轭

令 \(x=\lambda(\tau)\)，\(W=\vartheta_3(\tau)^4\)，\(e=E_2^*(\tau)/W\)，其中 \(E_2^*=E_2-3/(\pi\operatorname{Im}\tau)\)。椭圆方程 \((1-x)\theta^2F-x\theta F-xF/4=0,\ \theta=x\,d/dx\) 的对称四次有分裂基 \(W^2(\pi i\tau)^j/j!\)（\(0\le j\le4\)）。沿正虚轴取实对数 \(\pi i\tau\)。固定 \(j=1,3\) 的两奇行，取有符号最大子式比；第 5 轮已由该微分系统推出
\[
 b=\frac{1-3x-e}{1-x},\qquad
 \alpha=\frac{e^2+(4x-2)e+7x^2-7x+1}{3(1-x)^2}. \tag{2}
\]
固定的纯对称张量把第三奇周期的相对扩张常数定为零。下述推导只使用 (2)，无需偶行的 \(1/\pi^2\) 特值。

采用 \(\Delta=(E_4^3-E_6^2)/1728\) 和 \(\chi^*=E_2^*E_4E_6/\Delta\)。经典恒等式为
\[
 A_4=1-x+x^2,\quad A_6=(1+x)(1-2x)(2-x)/2,\quad
 E_4=A_4W^2,\ E_6=A_6W^3,\ \Delta=x^2(1-x)^2W^6/256 .
\]
因此
\[
 j=J(x)=256A_4^3/[x^2(1-x)^2],\qquad
 e=\frac{\chi^*x^2(1-x)^2}{256A_4A_6}. \tag{3}
\]
第二式用在 \(j\notin\{0,1728\}\)。正虚轴 \(0<x<1\)，\(j=0\) 无解；\(j=1728\) 只有 \(x=1/2,\tau=i\)，稳定子使 \(E_2^*(i)=0\)，故 \(\alpha=b=-1\)。此点的水平二环类域也满足 (1)。

Masser 的定理给 \(\chi^*(\tau)\in\mathbb Q(j(\tau))\)。所需更强的量词是，对**任意**嵌入 \(\sigma\) 和**任何**满足 \(j(\tau')=\sigma j(\tau)\) 的 CM 点，均有 \(\chi^*(\tau')=\sigma\chi^*(\tau)\)。Spence 命题 5.1–5.2 明列这两条结论，证明对 \(|D|=3k^2,\ k\) 奇的情形改用 Masser 的另一有理公式。此处矩形的本原方程为 \(A_0\tau^2+C_0=0,\ (A_0,C_0)=1\)，故 \(D=-4A_0C_0\)，本身避开上述奇判别式。Spence 后来还证明 \(\mathbb Q(\chi^*)=\mathbb Q(j)\)；本证明只用包含及其共轭相容性。各嵌入下取 \(\lambda(\tau')=\sigma x\) 的上半平面点，则 \(j(\tau')=\sigma j\)，经典奇模理论保证 \(\tau'\) 是同判别式的 CM 点。式 (3) 和 (2) 因而逐项等同于 \(\sigma\) 作用后的值。复数共轭点上的读数按这个带水平标记的模表达式搬运；在新点采用其他实对数或更换奇周期需另行分析。[Masser, *Elliptic Functions and Transcendence*, 附录 A](https://doi.org/10.1007/BFb0069432) · [Spence，命题 5.1–5.2 及特殊判别式](https://arxiv.org/abs/1607.03769) · [Spence，推论 2.4](https://arxiv.org/abs/1904.03432)

## 二、为什么二次损失从不发生

记 \(F=\mathbb Q(\alpha,b)\)。已知 \(F\subseteq\mathbb Q(x)\)。消去 \(e\)，以 \(t=(1-x)^{-1}\) 为未知数得到
\[
 t^2+(2b-5)t+b^2-2b+4-3\alpha=0 . \tag{4}
\]
给定 \(\alpha,b\) 的另一根及其对应参数是
\[
 t'=\frac{2+x+2e}{1-x},\quad
 x'=\frac{1+2x+2e}{2+x+2e},\quad
 e'=-\frac{2+2x+3e}{2+x+2e},\quad
 1+e'=-\frac{x+e}{2+x+2e}. \tag{5}
\]

这里决定两根的是一般实模不等式。对每个 \(y>0\) 有
\[
                    -x<e<1-x,\qquad x=\lambda(iy). \tag{6}
\]
当 \(y\ge1\) 时，\(E_2^*(i)=0\)，而 \(E_2(iy)=1-24\sum_{n\ge1}\sigma_1(n)e^{-2\pi n y}\) 及 \(-3/(\pi y)\) 都严格递增，故 \(e\ge0\)。设 \(q=e^{-\pi y}\)，交错 theta 级数有 \(\vartheta_4\ge1-2q>0\)。因为 \(8\pi y e^{-\pi y}<3\)，得到
\[
 E_2^*(iy)<1-3/(\pi y)<1-8q\le\vartheta_4^4=(1-x)W.
\]
当 \(0<y<1\)，模反演 \(\tau\mapsto-1/\tau\) 将 \((x,e)\) 送到 \((1-x,-e)\)，故 (6) 保持。正虚轴的 \(\lambda(iy)\) 遍历且单射到 \((0,1)\)，也可从 \(d\log x/d\log q=(1-x)W>0\)、尖点极限和反演读出。[Jacobi 的 theta 模变换](https://dlmf.nist.gov/20.7)

由 (5)–(6)，\(0<x'<1\)，但 \(e'<-1\)。故它不可能是该 \(x'\) 在正虚轴上的真实伴随 \(e\)。若 \([\mathbb Q(x):F]=2\)，二次扩张的非平凡自同构必交换 (4) 的根，使 \(x\mapsto x',e\mapsto e'\)。取唯一的 \(iy'\) 使 \(\lambda(iy')=x'\)。其 \(J(x')\) 是原奇模的共轭；第一节的 CM 协变性遂使 \(e'\) 必等于 \(E_2^*(iy')/\vartheta_3(iy')^4\)，与 (6) 矛盾。连同 (4) 的上界，得到 \(F=\mathbb Q(x)\)。对一般正虚轴点，(4) 的实逆式也完全显式，
\[
 t=\frac{5-2b-\sqrt{9-12b+12\alpha}}2,\qquad
 t'-t=\frac{1+x+2e}{1-x}>1 .
\]
因此 CM 处这里取到的正平方根已属于 \(F\)。仅知两根可以数值区分尚不足以证明域相等；上面的 CM 共轭论证排除了真实的域自同构。

## 三、环类域、单个 \(j\) 生成元与实签名

\(\lambda\) 是完整水平二模曲线 \(X(2)\) 的有理主函数，标记有序的二扭基；所需单位根 \(\zeta_2=-1\) 有理。复乘主定理在 \(K\) 上以有限 idèle 的类域作用描述这个带标记点。设格的乘子序为 \(\mathcal O_f\)。在 \(\ell\ne2\) 处稳定格的局部子群是 \(\mathcal O_{f,\ell}^{\times}\)；在 2 处，在稳定格后还须使两根标记在格模 2 上不变，即 \((u-1)\Lambda_2\subseteq2\Lambda_2\)，等价于 \(u\in1+2\mathcal O_{f,2}\)。点的同构允许的整体标量给 \(K^\times\)，也吸收额外 CM 单位。因为 \(\mathbb Z_2^\times=1+2\mathbb Z_2\)，有
\[
 1+2\mathcal O_{f,2}=(\mathbb Z_2+2\mathcal O_{f,2})^\times
                      =\mathcal O_{2f,2}^\times.
\]
其余素位 \(\mathcal O_{2f,\ell}=\mathcal O_{f,\ell}\)，因此稳定子对应 \(H_{2f}\)。这个核计算也适用于偶 \(f\)。由 \(\mathcal F_2=\mathbb Q(\lambda)\) 及 \(x\) 有限，所有在该点正则的水平二模函数值都属于 \(\mathbb Q(x)\)。于是 \(K(x)=H_{2f}\)。这里的 \(2f\) 指序的导子；单个阿贝尔扩张的最小 Artin 导子可能更小。[Streng，非极大序的水平复乘定理 2.2 与 §4.4](https://pub.math.leidenuniv.nl/~strengtc/reciprocity.pdf) · [Milne，复乘基本定理](https://www.jmilne.org/math/CourseNotes/CM.pdf)

矩形情形还能直接从经典无水平 \(j\) 提取同一域。用前述本原方程的 \(A_0,C_0>0\)，令
\[
 \tau'=\begin{cases}2\tau,&A_0\text{ 奇},\\
                       \tau/2,&A_0\text{ 偶}.
        \end{cases}
\]
第一种的本原式为 \(A_0\tau'^2+4C_0=0\)，第二种为 \(4A_0\tau'^2+C_0=0\)（此时 \(C_0\) 奇），判别式均为 \(4D\)。二倍角公式给
\[
 j(2\tau)=J_2(x)=16(16-16x+x^2)^3/[x^4(1-x)],\qquad
 j(\tau/2)=J_2(1-x).
\]
所以 \(j(\tau')\in\mathbb Q(x)\cap\mathbb R\)，普通 CM 定理给 \(K(j(\tau'))=H_{2f}\)，独立校准水平二稳定子的下界。由于 \(K\) 虚二次而 \(F\subset\mathbb R\)，\([H_{2f}:F]=2\)。综上
\[
 F=\mathbb Q(j(\tau'))=H_{2f}^{\langle\iota\rangle},\qquad [F:\mathbb Q]=h(4D),
\]
其中 \(h(4D)\) 是判别式 \(4D\) 的本原正定型类数。故通常的环类多项式给出此前两条射影读数所生成域的一个单生成元。

水平二点的域本身已有直接文献结果。Bourdon–Clark 定理 1.1(b) 在偶判别式 \(D<-4\) 给 \(\mathbb Q(P)\cong\mathbb Q(J_{4D})\)、\([\mathbb Q(P):\mathbb Q(j(\tau))]=2\)。所以对这些矩形 CM 点，原始 \(j(\tau)\) 到选择子域确实是二次扩张，而选择子域到 \(\lambda\) 域的度为一。这两个扩张分别对应加入水平与从两条奇读数恢复水平。式 (1) 于是也给出有理读数的完整分类：两读数同在 \(\mathbb Q\) 恰当 \(\tau=i\)。另一直接证明写 \(n=A_0C_0>1\)。判别式 \(-16n\) 的本原正定型在奇 \(n\) 时可取 \([4,0,n]\)，在偶 \(n\) 时取 \([4,4,n+1]\)；前者不表 1，后者的值 \((2u+v)^2+nv^2\) 也不表 1，故都不同于主类。[Bourdon–Clark 的模曲线结果，见 Clark 定理 1.1(b)](https://arxiv.org/abs/2212.13316)

若 \(G=\operatorname{Pic}(\mathcal O_{2f})\)，则 \(\operatorname{Gal}(H_{2f}/\mathbb Q)=G\rtimes\langle\iota\rangle\)，\(\iota\) 作用为取逆。\(F\) 的各个嵌入可用 \(a\in G\) 标记；复共轭交换 \(a\) 与 \(a^{-1}\)，故签名为 \((|G[2]|,(|G|-|G[2]|)/2)\)。若 \(G\) 中存在阶大于 2 的元，则 \(\langle\iota\rangle\) 的共轭核心平凡，\(F\) 的正规闭包为 \(H_{2f}\)；否则 \(F/\mathbb Q\) 已是全实 Galois 扩张。

## 四、一个可逐项复算的四次轨道

从 \((x,e)=(1/2,0)\) 出发，实根 \(v=\sqrt{1-x}\) 取正。由 theta 二倍式和 \(2E_2^*(2\tau)-E_2^*(\tau)=(\vartheta_3^4+\vartheta_4^4)/2\)，
\[
 x(2\tau)=\left(\frac{1-v}{1+v}\right)^2,\qquad
 e(2\tau)=\frac{2e+2-x}{(1+v)^2}.
\]
先得 \(x(2i)=17-12\sqrt2,\ e(2i)=9-6\sqrt2\)，\(j(2i)=66^3\)。再令 \(w=\sqrt{12\sqrt2-16}>0\)，则
\[
 w^4+32w^2-32=0,\qquad
 x(4i)=\left(\frac{1-w}{1+w}\right)^2,\qquad e(4i)=\frac3{(1+w)^2}.
\]
\(N_{\mathbb Q(\sqrt2)/\mathbb Q}(12\sqrt2-16)=-32\)，排除了它在二次域内是平方。将 (2) 化到 \(\mathbb Q[w]\) 的幂基后，有
\[
 b=2-\frac{7w}4-\frac{5w^3}{128},\qquad
 \alpha=\frac74-\frac{7w}4+\frac{w^2}{32}-\frac{5w^3}{128}.
\]
以 \((1,w,w^2,w^3)\) 为基，\((1,b,b^2,b^3)\) 的行列式为 \(9902007/134217728\)，换作 \(\alpha\) 得 \(10876599/134217728\)。所以本例任一读数即可生成四次域；\(b\) 的本原最小多项式是
\[
 8192z^4-65536z^3+228864z^2-391168z+81167.
\]
从 \(w\) 的四个根代回同一有理公式，给出各共轭的**配对**读数。\(w\) 有两实根、两非实根，\(F\) 的签名为 \((2,1)\)，且在本实嵌入 \(K=\mathbb Q(i),\ f=4,\ KF=H_8,\ F=\mathbb Q(j(8i))\)。脚本在有理多项式商环内复核 (4)、(5)、两种换根的不变量、二倍 \(j\) 及 \(x,e,\alpha,b,j(8i)\) 各自的最小多项式，无需小数识别。[复算程序](classfield_check.py) · [精确数据](classfield_checked.json)

原奇行的扩张检验亦随这一族统一。第 5 轮首奇行的射影直线斜率为 \(-2(e+2x-1)/(3(1-x))+1/[(1-x)W\pi i\tau]\)。在上述 CM 点，第一项代数，第二项是 \((\pi W)^{-1}\) 的非零代数倍。由 \(E_2=eW+3/(\pi y), E_4=A_4W^2,E_6=A_6W^3\) 和 Nesterenko 的超越次数至少三，\(\pi,W,e^{2\pi i\tau}\) 代数独立，故斜率超越。原分裂射线因此是首奇行中唯一的代数射线，第三奇周期加上任意非零常量倍的 \(w_0\) 都会移出它（原选择子对 \(w_0\) 的值为 \(3w_0/[(1-x)W\pi i\tau]^2\ne0\)）。这一结论沿用第 5 轮的秩二奇行检验，并由 (3) 推广至全矩形 CM 族。[Nesterenko 定理](https://doi.org/10.1070/SM1996v187n09ABEH000158)

式 (1) 使用 CM 处的水平标记、分裂奇周期和正虚轴分支。对于预定非零第三奇周期扩张的其他秩五族，替换归一化会改变子式，仍须证明相应的特殊值定理；第 5 轮在同一模族中已有改变扩张常数即失去代数性的见证。一般 Guillera 非分裂选择子的下降仍留给原登记问题。
