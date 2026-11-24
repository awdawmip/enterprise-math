# C90：多支联合极限所用的精确 Ratner 输入

日期：2026-11-24。此文件只核对本轮实际使用的外部标准定理；其余微平移、整数重指标化和原读数窗口仍从 C89 的准确有限模型推导。

## 1. 原始来源

Marina Ratner, **On measure rigidity of unipotent subgroups of semisimple groups**, *Acta Mathematica* **165** (1990), 229–309, DOI [10.1007/BF02391906](https://doi.org/10.1007/BF02391906)。

- 实际读取的原始期刊 PDF：[清华丘成桐数学科学中心存档](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6450-11511_2006_Article_BF02391906.pdf)。
- 核心定位：原文第 233 页 **Theorem 2** 和 **Corollary 5(1) (The Joinings Theorem)**；代数测度、joining、两个正规核的定义在第 229、232 页。Theorem 2 的证明在第 307–309 页。
- 本轮已实际读取原文定义及第 233 页的完整定理解析文本。工具来源引用：`turn328503852view0`、`turn409541134view0`。

该版本已足够：把前若干因子作为一个连通半单群，剩余一个因子作为另一个群，然后递归应用两系统的 joining 分类。因此不需要把尚未逐项核对的 1991 一般版本当作本轮前提。

## 2. 本轮采用的准确内容

在两个连通半单实李群的格商上，对各自 Haar 概率和 unipotent 元素，任一遍历 joining 是代数 joining。Theorem 2 将它表示为两个闭正规核之上的同构商，并给有限个纤维代表；投影到第二群的核记为 \(A_2\)。

这里的“格”允许非余紧格；Theorem 2 / Corollary 5(1) 并没有要求紧商。本轮使用的是带 Haar 边缘的 joining 分类，而非从任意轨道出发的均匀分布定理。

具体代入：

\[
G_1=\operatorname{SL}_2(\mathbb R)^{r-1},\quad
\Gamma_1=\operatorname{SL}_2(\mathbb Z)^{r-1},\qquad
G_2=\operatorname{SL}_2(\mathbb R),\quad
\Gamma_2=\operatorname{SL}_2(\mathbb Z).
\]

所有群连通、半单且第二可数，所列离散子群均为格。选定的时间一元素在每个因子中都是非平凡 unipotent 元素；其速度允许不同及异号。Haar horocycle 混合性使每个时间一变换及其有限乘积遍历。归纳先证明前 \(r-1\) 个因子的边缘为 Haar 乘积，随后才将完整遍历分量代入 Corollary 5(1)。

原文用左商 \(\Gamma\backslash G\) 和右平移。本文列格用 \(G/\Gamma\) 和左平移，映射 \(g\Gamma\mapsto\Gamma g^{-1}\) 将二者等价，并把各速度统一变号；所有假设及结论保持。

## 3. 混合性的继承输入

C89 已读取并使用 Ratner, **The rate of mixing for geodesic and horocycle flows**, *Ergodic Theory and Dynamical Systems* **7** (1987), 267–288, Theorem 2、Corollary 2，DOI [10.1017/S0143385700004004](https://doi.org/10.1017/S0143385700004004)。本轮仍只使用定性 Haar 混合性及其无非零频率特征函数的推论。

## 4. 此输入解决的确切缺口

本轮证明的条件性命题是：对每条实际宏观逆支，若所有分支对的主斜率映射横截几乎处处成立，则形状联合弱极限为完整 Haar 乘积。证明并不把一般概率论中的两两独立提升为共同独立；它额外使用原有限模型给出的乘积 horocycle 不变性，以及上面的代数 joining 分类。

这些外部李群格空间是原整数安排的局部读数计数模型。原三态因子路径的次序、标签和观察者仍保留，未据辅助连续空间改变项目的原生 X6 空间或原整数定义。
