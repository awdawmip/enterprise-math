# C89：有限分离保证量的低精度过渡尺度

## 1. 对象与结论

本篇继续原整数安排 \(2\leq w\leq v\leq c\) 的原 \(H(0,1)\) 三库存读数，
使用 C89 [相位条件夹逼](../phase/PHASE_CONDITIONED_BOUND.md) 中的全库存唯一率下界
\(\mathcal B_\tau(L)\)。这里分析的是已经严格转移到原问题的保证函数；
先取库存极限，随后研究这个函数的 \(L,\tau\) 参数。

记 \(F=(G,B_1)\)、\(\Delta=\{0<y<x<1\}\)、
\(J=|\det dF|\)。忽略已有的零面积例外集。
\(\mathcal S\) 是完整 \(F\) 纤维只有一个原像的源集合；
\(\mathcal E\) 是完整纤维至少有两个原像，且源的 \(B_2\) 值严格最小或严格最大的源集合。
在 \(\mathcal E\) 上令 \(\delta(X)>0\) 为向纤维内部最近的 \(B_2\) 谱差。
所有分支标签与原整数竞争者仍保留；二维连续源、谱曲率与 Haar 格均为辅助读数表示。

定义

\[
\mathcal T(r)=\int_0^r tF_2(1/t)\,dt,\qquad 0\leq r<\infty,
\quad \mathcal T(\infty)=\frac{C_{\rm end}}2,
\tag{1.1}
\]

其中

\[
C_{\rm end}=2\int_0^\infty F_2(s)s^{-3}\,ds.
\tag{1.2}
\]

令

\[
M_{2,\mathcal S}=2\int_{\mathcal S}J^2\,dX,
\qquad
\mathcal A(\rho)=C_{\rm end}M_{2,\mathcal S}
  +2\int_{\mathcal E}J(X)^2\,
    \mathcal T\!\left(\frac{\rho\delta(X)}{2J(X)}\right)dX,
\quad 0\leq\rho\leq\infty.
\tag{1.3}
\]

**定理。** 若 \(L\downarrow0\)、\(\tau=\tau(L)\geq0\)，且

\[
L\tau(L)\longrightarrow0,\qquad \tau(L)/L\longrightarrow\rho\in[0,\infty],
\tag{1.4}
\]

则

\[
\boxed{\frac{\mathcal B_{\tau(L)}(L)}{L^4}\longrightarrow\mathcal A(\rho).}
\tag{1.5}
\]

所以这项全库存保证量的分离过渡发生在 \(\tau\asymp L\)。
其端值为

\[
\mathcal A(0)=C_{\rm end}M_{2,\mathcal S},\qquad
\mathcal A(\infty)=C_{\rm end}
 \left(M_{2,\mathcal S}+\int_{\mathcal E}J^2\,dX\right).
\tag{1.6}
\]

\(\mathcal A\) 在扩展区间 \([0,\infty]\) 连续，在有限 \(\rho\) 上严格增加。
在原点还有

\[
\boxed{
\mathcal A(\rho)=C_{\rm end}M_{2,\mathcal S}
 +\frac{\rho^2}{4}\int_{\mathcal E}\delta(X)^2\,dX+o(\rho^2).
}
\tag{1.7}
\]

完整多分支库存极限是否存在仍由联合整数过程决定；(1.5) 的对象明确是
已证明的下界函数，不把它改称实际唯一率的等式。

## 2. 单端相位扇区的精确换元

固定正规源点，置 \(a=L^2J(X)\)。C89 的加权近距唯一密度为

\[
w_a(d)=(1-|d|)F_2\!\left(\frac a{1-|d|}\right),\qquad -1<d<1.
\tag{2.1}
\]

当源是纤维 \(B_2\) 极小支时，最近远支偏移为
\(h=L\tau\delta/2>0\)；若 \(h\leq1\)，可排除所有远支的相位区间是
\(-1<d<h-1\)。极大支给对称的另一端。相应保证量准确为

\[
\int_0^h \ell F_2(a/\ell)\,d\ell
 =a^2\mathcal T(h/a),\qquad
\frac ha=\frac{\tau\delta}{2LJ}.
\tag{2.2}
\]

第一式只作 \(\ell=at\) 换元，因此对所有正 \(a,h\) 的积分恒等成立。
作为端支保证量使用时保留 \(h\leq1\) 的条件。

从 C82 的 \(F_2(s)=1-21/(4\pi^2s)\)（\(s\geq1\)）得到

\[
\boxed{\mathcal T(r)=\frac{r^2}{2}-\frac{7r^3}{4\pi^2}
\quad(0\leq r\leq1).}
\tag{2.3}
\]

从 C83 的 \(F_2(s)=s^3/\pi^2+O(s^4)\)（\(s\downarrow0\)）得到

\[
\boxed{\mathcal T(r)=\frac{C_{\rm end}}2-
\frac1{\pi^2r}+O(r^{-2})\quad(r\to\infty).}
\tag{2.4}
\]

\(F_2>0\) 保证 \(\mathcal T\) 严格增加，且

\[
0\leq\mathcal T(r)\leq\min\{r^2/2,C_{\rm end}/2\}.
\tag{2.5}
\]

这些性质保留格内全部向量的相关性，不使用泊松近似。

## 3. 小 \(L\tau\) 时的全源精确公式

C89 相位夹逼证明已说明 \(B_2\) 在有限个符号片上全域有界。
取 \(M>0\)，使任一正谱纤维的任意两个原像均满足
\(|B_2(Y)-B_2(X)|\leq M\)。当

\[
L\tau M/2\leq1,
\tag{3.1}
\]

每个极端支的 \(h\leq1\)。对于内部支，最近两侧偏移
\(h_+,h_-\leq1\)，因而 \(h_++h_-\leq2\)，两个允许远支的相位区间
覆盖 \((-1,1)\)，该相位必要条件不保证它有任何全库存唯一贡献。
单原像支则保留全部近距贡献。

所以 (3.1) 下有准确公式

\[
\boxed{
\mathcal B_\tau(L)=S(L)+2L^4\int_{\mathcal E}J(X)^2
 \mathcal T\!\left(\frac{\tau\delta(X)}{2LJ(X)}\right)dX,
\quad S(L)=2\int_{\mathcal S}F_0(L^2J(X))dX.
}
\tag{3.2}
\]

全域 \(J\) 有界，C85 的端点展开给

\[
S(L)=C_{\rm end}M_{2,\mathcal S}L^4+O(L^6).
\tag{3.3}
\]

在 (1.4) 下，(3.1) 最终成立。又因
\(J^2\mathcal T(\tau\delta/(2LJ))\leq C_{\rm end}J^2/2\)，
可以支配收敛。有限 \(\rho\) 给 (1.3)，\(\rho=\infty\) 则对
\(\mathcal E\) 几乎处处用 \(\delta>0,J>0\) 及 (2.4)。由此完成 (1.5)–(1.6)。

## 4. 过渡函数的严格性与原点展开

C81 的六重正规纤维开放目标区，扣除不同支 \(B_2\) 相等的零面积集合后，
提供 \(\mathcal E\) 的正面积子区域，其中 \(J,\delta>0\)。
对任意 \(0\leq\rho_1<\rho_2<\infty\)，(2.1) 的严格正性使 (1.3) 中
该区域的被积函数严格增加，因此 \(\mathcal A(\rho_2)>\mathcal A(\rho_1)\)。
由 (2.5) 和支配收敛，\(\mathcal A\) 在整个扩展区间连续。

为证 (1.7)，固定几乎处处 \(X\in\mathcal E\)。当 \(\rho\downarrow0\) 时，
\(r=\rho\delta/(2J)\to0\)，故

\[
\frac{2J^2\mathcal T(\rho\delta/(2J))}{\rho^2}
 \longrightarrow\frac{\delta^2}{4}.
\]

由 (2.5)，左边处处不超过 \(\delta^2/4\)，后者有界可积。
这给出全域展开，无需假定 \(\int J^{-1}\) 有限。

## 5. 三个可直接比较的分离区域

以下均按先取库存极限后的保证函数理解，并保持 \(L\tau\to0\)。

| 分离参数 | \(\mathcal B_\tau(L)/L^4\) 的极限 |
|---|---|
| \(\tau/L\to0\) | \(C_{\rm end}M_{2,\mathcal S}\) |
| \(\tau/L\to\rho\in(0,\infty)\) | \(\mathcal A(\rho)\) |
| \(\tau/L\to\infty\) | \(C_{\rm end}[M_{2,\mathcal S}+\int_{\mathcal E}J^2]\) |

对每个固定 \(\tau>0\)，第三行适用。每个极端支由远支排除所保证的主项，
为该支全部近距端点主项的二分之一；另半边相位仍可能受到同方向远支影响。
这是一项可证明贡献的比例，而非实际远支损失的比例。

在固定精度 \(L>0\) 下让 \(\tau\downarrow0\)，C89 已得保证量的 \(\tau^2\) 增量。
本篇说明这个小分离展开的作用尺度随 \(L\) 缩小为 \(\tau\asymp L\)，
并给其完整过渡积分。它与 C88 研究的几何位置 \(\theta\asymp L^2\) 过渡具有不同的对象与变量。

## 6. 来源与证明状态

- C89 `phase/PHASE_CONDITIONED_BOUND.md`：相位加权近距定理、全库存保证量、极端支与内部支区间。
- C82 `LATTICE_LIMIT.md`：\(F_2\) 的 Haar 定义、正性与 \(a\geq1\) 闭式。
- C83 `HAAR_SMALL.md`：\(F_2(a)=a^3/\pi^2+O(a^4)\)。
- C85 `endpoint/ENDPOINT_LIMIT.md`：\(F_0\) 的端点积分及二次小余体积展开。
- C81 `LEVEL_CURVES.md`、C82 `CROSS_PHASE.md`：完整有限纤维、正面积六重正规域与三谱几乎处处区分。

本篇为手推积分与支配收敛证明。新增结论是保证量的 \(\tau/L\) 过渡、
式 (3.2) 的全源精确公式、式 (1.5)–(1.7) 及端支主项的一半保证。
