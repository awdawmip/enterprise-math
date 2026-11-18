# 非分裂 Weil 六维簇的 32 图像锥：每个扩张恰能沿两维环境提升

在指定特殊纤维上，设 $P,M$ 分别是下述两个带标记的 16 图像结构层直和。对 **每一个** $\xi\in\operatorname{Ext}^2(P,M)$，取三角 $M[1]\to E_\xi\to P\xrightarrow{\xi}M[2]$。在九维有极化、保 $\mathbf Q(i)$ 作用的变形空间中，$E_\xi$ 的完整一阶环境障碍有秩七，其核恰为
$$
\{\operatorname{diag}(b_1,b_2,0):b_1,b_2\in\mathbf C\}.
$$
2026-09-17 原稿只给出该平面为上界，明确留下每个扩张能否沿平面提升。本次用一个共同二维解析族及相对 Ext 基变换证明充分性。结论涵盖 1152 维参数空间的所有点，包括零扩张。[H0Q 任务](https://github.com/awdawmip/enterprise-math/blob/c0f816e2ab6be0145a3edd1a77488bddfd42a2f6/research_tasks/HODGE_H0Q_NONSPLIT_WEIL_INDEPENDENT_OBSTRUCTION_AUDIT_20260919.md) · [32 图像原稿 §§1–4](https://github.com/awdawmip/enterprise-math/blob/ecafd46d13384398f58b287389d72708626cfff4/research_notes/HODGE_MU4_PURE_SEED_LIAISON_OBSTRUCTION_EM_HODGE_E8C393_20260917.md)

## 特殊纤维上的投影和四个交数

取 $E=\mathbf C/\mathbf Z[i]$，$X_0=E_z^3\times E_w^3$，$K=\mathbf Q(i)$ 在 $z,w$ 块分别经两个共轭嵌入作用。极化权重为 $(1,1,1,1,1,3)$，Hermitian 判别式类为 $[-3]$。令 $u=1+2i,\ U=\iota(u)^*|H^6$。对中维杯积配对，$U^\dagger=5^6U^{-1}$；因为同源的度为 $5^6$，拉回将配对乘以此数。令 $S=(U+U^\dagger)/2$。在第 $p$ 个嵌入计数分量上，$U$ 作用为 $u^p\bar u^{6-p}$，故 $S$ 的特征值在四组共轭块上为 $117,-35,-75,125$。两端 Weil 块的短投影为
$$
 \Pi_W=-\frac{(S+35)(S+75)(S-125)}{233472}.
$$
对实中维类 $c$ 令 $m_j=\int c\,U^jc$。展开并使用 $UU^\dagger=15625$ 得
$$
 m_3-30m_2+2375m_1-1781250m_0=-933888\int(\Pi_W c)^2 .
$$
两个 Weil 行列式线原始且为 $(3,3)$ 型，其实形式上的中维配对负定，故这四数可判别投影非零。对对角图像 $\Gamma$，固定三个坐标的消元给 $m_j=|u^j-\bar u^j|^6$（$m_0=0$ 亦由平凡法丛得到）。四数为 $0,4096,262144,4096$，组合为 $1867776$，故 $w=\Pi_W[\Gamma]$ 满足 $\int w^2=-2$。[H0N 投影来源](https://github.com/awdawmip/enterprise-math/blob/c0f816e2ab6be0145a3edd1a77488bddfd42a2f6/research_returns/HODGE_H0N_NONSPLIT_WEIL_EXCEPTIONAL_CH3_SEED_OBJECT_RETURN_20260902.md) · [四交数冻结记录](https://github.com/awdawmip/enterprise-math/blob/8e63e1612659add4559f8dafa2074b9a67867de2/research_artifacts/HODGE_FOUR_INTERSECTION_GRAPH_EM_HODGE_E8C393_20260910.json)

## 图像的符号、交与 Ext

对 $a\in\mu_4^3$，设 $\Gamma_a=\{w_j=a_jz_j\},\,F_a=\mathcal O_{\Gamma_a}$。$P$ 取 $\prod a_j=1$ 的直和，$M$ 取 $\prod a_j=-1$ 的直和。每个 $F_a$ 的全 Chern 特征仅有图像中维类一项，源和靶皆有平凡切丛。写 $q_j=[0]_{z_j}+[0]_{w_j}$，$q=q_1q_2q_3$。单对图像的三个字符为 $1,a_j,\bar a_j$，常数项为 $q_j$。各在 16 元陪集上求和后，仅全常数、全 $a_j$、全 $\bar a_j$ 三项留下；后两项正是对角类的两个极端嵌入分量。故
$$
 \operatorname{ch}P=16(q+w),\qquad
 \operatorname{ch}M=16(q-w),\qquad \operatorname{ch}E_\xi=32w.
$$
独立地，对图像对计算 $\int[\Gamma_a][\Gamma_b]=\prod_j|a_j-b_j|^2$；有共同坐标时，可平移使之不交。32 项带符号平方为 $-2048$，和 $32^2\int w^2$ 相符。

若 $a,b$ 恰有 $s$ 个坐标不同，记 $N=\prod_{a_j\ne b_j}|a_j-b_j|^2$。在单个阿贝尔曲面中，两图像不同时横截于相应数量的点，结构层的 Ext 仅在次数一。相同时，由除子二项分解、平凡法线及椭圆曲线的 $H^*(\mathcal O_E)$，自 Ext 多项式为 $(1+t)^2$。逐因子 Künneth 因此给出
$$
 \sum_k\dim\operatorname{Ext}^k(F_a,F_b)t^k=Nt^s(1+t)^{2(3-s)} .
$$
正负两组的 $s=1,2,3$ 对数依次为 $48,96,112$，按度数 $0,\dots,6$ 合计的 Ext 维数为 $(0,192,1152,4480,1152,192,0)$。两个方向的 $\operatorname{Hom}$ 均为零。

## 核的必要性与充分性

记 $D=\operatorname{diag}(1,1,3)$。以行表示全纯切向输出、列表示反全纯输入，保 $K$ 作用强制 Beltrami 矩阵仅有非对角块，保极化强制权重乘矩阵对称，故所有九个切向具有形式
$$
 C(B)=\begin{pmatrix}0&B\\D^{-1}B^\mathsf T&0\end{pmatrix}.
$$
写 $A_a=\operatorname{diag}(a_j)$。限制到 $\Gamma_a$ 后将切向送至法丛商 $v_w-A_av_z$，得
$$
 \delta_a(B)=D^{-1}B^\mathsf T-A_aB\bar A_a.
$$
对角图像的核为 $\langle E_{11},E_{22},E_{12}+E_{21}\rangle$，秩六。若对正组所有 $a$ 同时要求 $\delta_a(B)=0$，则对 $j\ne k$，改变 $a_j\bar a_k$ 迫使 $B_{jk}=0$。对角方程再迫使 $B_{33}=0$。负组有同一结论。独立地，在外代数上对 $q$ 施以 $dz_j\mapsto\sum B_{jk}d\bar w_k,\ dw_k\mapsto\sum B_{jk}d\bar z_j/D_{kk}$ 的次数零导子，得到到 $(2,4)$ 分量的秩也为七，两条纯 Weil 线上的该导子为零。因而 $P,M$ 各自的 Chern 类与二者之差在此处确实给出不同的 Hodge 方向数。

**必要性。** 一阶完美提升的 $\epsilon$ 短正合复形给出的上同调层 Bockstein 只有一项可能非零，即 $M\to P$。由于 $\operatorname{Hom}(M,P)=0$，两上同调层各自得到平坦提升；其乘 $\epsilon$ 的核等于像。$P$ 的 Atiyah–Kodaira–Spencer 障碍在直和的每个对角块即是 $F_a$ 的障碍。每个 $F_a$ 的提升强制图像的法向障碍为零：平坦提升在各处由单个局部元生成，零化子给出平坦闭子概形，提升原图像。因此任何 $\xi$ 的提升方向都属于上述共同平面。[完整对象障碍的判据](https://arxiv.org/abs/0805.3527)

**充分性。** 在小双圆盘 $b=(b_1,b_2)$ 上，给该固定实环面引入复坐标
$$
  Z_j=z_j-b_j\bar w_j,\qquad W_j=w_j-b_j\bar z_j
  \quad(j=1,2),\qquad (Z_3,W_3)=(z_3,w_3).
$$
用变换后的格作商。格生成元随 $b$ 全纯变化，故得一族复环面。每块仍保 $K$；前两块的极化权重相等，反全纯切空间是对称 Beltrami 矩阵的图，因而对固定交替 Riemann 形式仍为迷向；正定性在原点附近保持。这样得到有极化的实际解析族，其切空间为所求平面。由于 $a_j\bar a_j=1$，每个原实子环面在新坐标中仍满足 $W_j=a_j Z_j$。于是所有 $F_a$ 同时延为相对图像结构层，它们在光滑总空间上完美。

每个纤维仍是三个阿贝尔曲面的乘积。单因子中，不同图像的有限交群由底层实格决定，切线斜率仍相异。相同图像的法线仍平凡。因此上节的因子级 Ext 计算逐纤维保持，所有次数的 $\dim\operatorname{Ext}^k(P_b,M_b)$ 恒定。令 $p$ 为这族的投影。由适当映射的上同调与基变换，$Rp_*R\mathcal Hom(P_b,M_b)$ 对应的相对 Ext 层局部自由且与取纤维交换。也可在小圆盘上将这个完美推出表示为有界有限自由复形；各度上同调维数恒定，逐度推出微分秩恒定，立即得到上述基变换。故任意给定 $\xi$ 延为局部截面。在缩小后的 Stein 双圆盘上，高阶凝聚上同调消失，局部到整体谱序列使该截面来自实际的相对态射 $P_b\to M_b[2]$。取三角并限制到任意双数切向，即得到 $E_\xi$ 的完美提升。有极化的无穷小纤维可用射影 GAGA 转回代数范畴。结合必要性，完整障碍核恰为该平面。这里建立的是特殊亚族上的实际提升，余下七个方向对指定两层锥都有障碍。

## 单侧辅助映射的独立边界

若 $a\ne b$，取图像理想 $\mathcal I_a\subset\mathcal O_{X_0}$。有
$$
\operatorname{Hom}(F_b,\mathcal I_a)=0,\qquad
\dim\operatorname{Hom}(\mathcal I_a,F_b)=
\begin{cases}
 |a_j-b_j|^2,&\text{只在第 }j\text{ 项不同},\\
 1,&\text{至少两项不同}.
\end{cases}
$$
首式由环境理想无挠得出。在 $\Gamma_b$ 上，$\mathcal I_a$ 的限制到其像（交理想）的核是挠层，所有到 $\mathcal O_{\Gamma_b}$ 的态射均杀掉它。一个坐标不同时，该像为从椭圆因子拉回的有效次数 $N$ 除子的理想，故其对偶全局截面维数为 $N$；交余维至少二时，光滑正规 $\Gamma_b$ 上该理想的对偶为结构层。这个计算确定了通道的方向和维数。要让通道消去特定障碍，还需计算实际的 Yoneda 乘积。具体地，三角 $M'[1]\to E\to P'\xrightarrow{\eta} M'[2]$ 的自然性只强制源、靶障碍分别落在 $\eta\circ\operatorname{Hom}(M',P')$ 和 $\operatorname{Hom}(M',P')[2]\circ\eta$ 的像中。非零 Hom 本身不决定那些像。

**具体的 Yoneda 零乘积。** 取正图像 $a=(1,1,1)$、负图像 $b=(-1,1,1)$，则 $N=4$。记 $\iota_a:\mathcal I_a\to\mathcal O_X$，$r_b:\mathcal O_X\to F_b$，并取自然非零映射 $v=r_b\iota_a$。这里 $\dim\operatorname{Hom}(\mathcal I_a,F_b)=4$，且 $\dim\operatorname{Ext}^2(F_b,\mathcal I_a)=4$。然而对其中每一个 $\xi:F_b\to\mathcal I_a[2]$ 同时有
$$
 v[2]\circ\xi=0,\qquad \xi\circ v=0.
$$
第一式来自余维三正则嵌入的对偶 Koszul 分解：$\operatorname{Ext}^{1,2}(F_b,\mathcal O_X)=0$。同一消失使 $\mathcal I_a\to\mathcal O_X\to F_a\xrightarrow{\partial_a}\mathcal I_a[1]$ 诱导同构 $\operatorname{Ext}^1(F_b,F_a)\simeq\operatorname{Ext}^2(F_b,\mathcal I_a)$，故 $\xi=\partial_a[1]\gamma$，左端维数由前述图像对公式为四。此时 $\gamma r_b\in H^1(\mathcal O_{\Gamma_a})$，而图像投影到 $z$ 块给出收缩，故 $H^1(\mathcal O_X)\to H^1(\mathcal O_{\Gamma_a})$ 满射。于是 $\partial_a[1](\gamma r_b)=0$，再复合 $\iota_a$ 即得第二式。该例把任意可用 Yoneda 通道进一步限制在 $\operatorname{Hom}(\mathcal I_a,F_b)/\mathbf Cv$ 的至多三维候选空间内。其余候选的乘积尚待测定。

| 待审核命题 | 数学复核 |
|---|---|
| 短投影、图像四交数、非零特殊纤维 Weil 投影 | PASS；七块谱代入及几何交数独立相符。 |
| 32 图像的纯 Weil 差、正负图像之间各次 Ext 和 Hom | PASS；逐因子 Koszul、字符与整数枚举一致。 |
| 两层锥自然性和共同环境切空间 | PASS 并加强；每个参数的完整障碍恰为秩七，剩余两维逐一可抬升。 |
| 10-15 固定对角的有限长度修改 | 对冻结族的秩六结论与本次重算相容。必要性由避开有限集后深度三的 $H^1(N)$ 限制单射；反向在已抬升支撑的含有限集光滑仿射开上局部平凡化后抬升该有限子概形。这是不同于 32 图像锥的族。[10-15 结果](https://github.com/awdawmip/enterprise-math/blob/18925b197fb3772e410b1e245b5fa84abf33d8fd/research_artifacts/mcp/RS-HODGE-H0P-NONSPLIT-WEIL-BILATERAL-DEFORMATION-OBJECT/MCP-e3eda4529333438d8ae1ae7e6983e5e5/86da7418af02a4cc365b/H0P_FINITE_MODIFICATION_RETURN.md) |
| 借辅助理想消去给定对象障碍、或向很一般纤维推广 | PARTIAL；上述四维例的自然映射在两侧均为零，剩余候选至多三维；尚无全九向的对象。本次没有推出很一般纤维上的代数性。 |

运行同目录的复算程序，依赖 Python 3 与 SymPy。程序独立构造 32 个字符标记、全部正负配对、各图像法向矩阵和外代数导子。解析族的存在与相对扩张的提升由上文论证。[复算程序](hodge_check.py)
