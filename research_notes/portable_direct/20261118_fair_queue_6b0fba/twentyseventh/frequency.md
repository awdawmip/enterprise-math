# 整频率偏振核的二平方求和与首个晶格修正

在冻结的标准三维环面归一化下，令 $k\in\mathbb Z^3\setminus\{0\}$，$P_k=I-kk^T/|k|^2$。本次独立复核正算子
$$
 T(k)=\sum_{\substack{p+q=k\\p,q\ne0}}
 \frac{|p\times k|^2}{|k|\,|p|^4|q|^2}\,P_kP_qP_k.
$$
轴向 $k=Ke_3$ 的整纵坐标可显式消去，留下带正双曲函数核的一维二平方因子和。高频处，从一般方向的原算子直接得到在算子范数中一致的展开
$$
 T(k)=\left(\frac{3\pi^3}{8}+\frac{2C_{\rm cub}}{3|k|}\right)P_k
              +O(|k|^{-3}),\qquad C_{\rm cub}=-8.91363291758515\ldots .       \tag{1}
$$
源笔记给出连续积分 $3\pi^3/8$，并报告 571 个八面体类及全频上界 $6.45^2$。式 (1) 中的次主项为负，两个横向特征值在充分高频处都从下侧趋近该极限，其间距至多 $O(|k|^{-3})$。轴向有限频率用第 2 节公式计算；第 4 节另给出一个完整非轴向频率的严格谱分裂。[任务书](https://github.com/awdawmip/enterprise-math/blob/e17e50381a1ba51a2d1c8ad96e9440d08eb8ddc5/research_tasks/NS_BRC_INDEPENDENT_REPLICATION_20260917.md) · [冻结偏振核、连续积分与原常数](https://github.com/awdawmip/enterprise-math/blob/e17e50381a1ba51a2d1c8ad96e9440d08eb8ddc5/research_notes/ns-coupled-polarization-20260910.md)

## 1. 壳权及整纵向的精确求和

令 $K\ge1$ 为整数，$p=(x,y,t),\ m=x^2+y^2,\ r=m+t^2,\ s=m+(t-K)^2$。当 $m>0$，算子在横平面内的矩阵是 $Km/(r^2s)$ 乘 $I_2-(x,y)^T(x,y)/s$。每个壳对四分之一转角封闭，$\sum x^2=\sum y^2=mr_2(m)/2,\ \sum xy=0$。$m=0$ 的合法项均为零，$p=0,k$ 原本就删去。因此
$$
 T(Ke_3)=\lambda_K P_{e_3},\qquad
 \lambda_K=K\sum_{m\ge1}r_2(m)\sum_{t\in\mathbb Z}
       \left(\frac{m}{r^2s}-\frac{m^2}{2r^2s^2}\right),
 \quad r_2(m)=4\sum_{d\mid m}\chi_4(d).                                    \tag{2}
$$
这里 $\chi_4$ 在 $1,3\bmod4$ 上分别取 $1,-1$，在偶数上取零。(2) 中的整数恒等式也可从 $\mathbb Z[i]$ 唯一分解得到。$3\bmod4$ 素数须有偶赋值，$1\bmod4$ 素数的 $a$ 次幂提供 $a+1$ 种共轭分配，$2$ 的幂只有一种分配，再乘四个单位。该壳权计算有向格点，包括坐标为零或绝对值相等的情形。

令 $b=K^2,\ v=b/m,\ A(v)=(v^2+15v+28)/(2(v+4)^3),\ B(v)=(v^2+3v+4)/(2(v+4)^2)$。则
$$
 \boxed{\displaystyle\lambda_K=\sum_{m\ge1}r_2(m)\,g_K(m),\qquad
 g_K(m)=\frac{\pi K}{m^{3/2}}A(v)\coth(\pi\sqrt m)
       +\frac{\pi^2}{K}B(v)\operatorname{csch}^2(\pi\sqrt m).}               \tag{3}
$$
两个权在整个参数域内均为正。证明时先让两个横向参数 $a,c$ 独立，记 $C(a)=\sum_t(t^2+a)^{-1}=\pi\coth(\pi\sqrt a)/\sqrt a$。部分分式给出
$$
 S(a,c)=\sum_t\frac1{(t^2+a)((t-K)^2+c)}
       =\frac{(b+c-a)C(a)+(b+a-c)C(c)}{(b+a+c)^2-4ac}.
$$
例如模 $t^2+a$ 对另一因子求逆得分子 $b+c-a+2Kt$，分母即上式分母；另一边平移 $t-K$ 同算。奇分子在对称截断极限为零，整数平移也保留此极限。由局部一致收敛，(2) 的每横向点贡献是 $K[-mS_a-m^2S_{ac}/2]_{a=c=m}$。用
$-C'(m)=(C(m)+\pi^2\operatorname{csch}^2(\pi\sqrt m))/(2m)$
整理即得 (3)。整数 $K$ 是平移闭合的假设。[双曲余切的部分分式](https://dlmf.nist.gov/4.36.E3)

## 2. 有显式常数的水平尾界

记 $D_s=\sum r_2(m)m^{-s}=4\zeta(s)L(s,\chi_4)$（$s>1$），并置
$$
 L_K(M)=\pi K\!\left(\tfrac7{32}D_{3/2}-\tfrac{3K^2}{64}D_{5/2}\right)
 +\sum_{1\le m\le M}r_2(m)
 \left[g_K(m)-\frac{\pi K}{m^{3/2}}\left(\tfrac7{32}-\tfrac{3K^2}{64m}\right)\right].
$$
对实 $M\ge2$，令 $J=\lfloor\sqrt{M/2}\rfloor,\ u=e^{-2\pi},\ d_M=1-e^{-2\pi\sqrt M}$。一致有
$$
 0\le\lambda_K-L_K(M)\le
 \frac{\pi K^5}{80J^5}+
 \left(\frac{7\pi K}{16M^{3/2}d_M}+\frac{2\pi^2}{Kd_M^2}\right)
 \frac{8u^{J+1}(J+1-Ju)}{(1-u)^2}.                                        \tag{4}
$$
其中
$$
 A(v)-\frac7{32}+\frac{3v}{64}
   =v^2\frac{3v^2+22v+8}{64(v+4)^3}\ \in [0,v^2/128],\quad
 A(v)\le 7/32,\quad B(v)\le1/2.
$$
尾项余下的代数部分至多 $\pi K^5m^{-7/2}/128$，指数部分用 $\coth w-1=2e^{-2w}/(1-e^{-2w})$ 及 $\operatorname{csch}^2w=4e^{-2w}/(1-e^{-2w})^2$ 控制。若 $x^2+y^2>M$，则 $j=\max(|x|,|y|)>J$，对应方壳有 $8j$ 个点。代数和至多 $8\sum_{j>J}j^{-6}\le8/(5J^5)$，指数和是 $\sum_{j>J}8ju^j$。从而得 (4)。给定 $K$ 的有效尾误差与在 $K$ 增长时保持精度所需的水平半径都在式中显出。

## 3. 独立连续积分与全方向次主项

写 $h=1/|k|,\ e=hk$，取任意实单位 $z\perp e$。其横向二次型为 $h^3\sum_{p\ne0,k}F_{e,z}(hp)$，其中
$$
 F_{e,z}(x)=\frac{|x\times e|^2}{|x|^4}\,
             \frac{|(e-x)\times z|^2}{|e-x|^4}.
$$
连续积分可同时旋转 $e,z$。取 $e=e_3,z=e_1$，记 $m=x_1^2+x_2^2,\ r=|x|^2,\ s=|e_3-x|^2$，对水平角积分使 $x_1^2$ 换成 $m/2$，所求为 $I(2,1,1)-I(2,2,2)/2$，其中 $I(a,c,j)=\int m^j r^{-a}s^{-c}\,dx$。把两个分母用 Schwinger 参数写作拉普拉斯积分，配方后轴向平移不改 $m$。横向高斯矩
$\int m^j e^{-t|x|^2}dx=\pi^{3/2}j!t^{-j-3/2}$，再对参数和及其比例作 Gamma、Beta 积分，给出
$$
 I(a,c,j)=\frac{\pi^{3/2}j!\,\Gamma(a+c-j-3/2)
 \Gamma(j+3/2-a)\Gamma(j+3/2-c)}
 {\Gamma(a)\Gamma(c)\Gamma(2j+3-a-c)} .
$$
此次两组参数各 Gamma 自变量均正，所得分别为 $\pi^3/2,\pi^3/4$。连续积分为 $3\pi^3/8$，与源稿相合。

**两处孤立奇性。** 在 $0$ 附近，由 $e\cdot z=0$，有 $|(e-x)\times z|^2/|e-x|^4=1+2x\cdot e+O(|x|^2)$。减去
$$
 H_e(x)=e^{-|x|^2}(1+2x\cdot e)\frac{|x\times e|^2}{|x|^4},
 \qquad G=F_{e,z}-H_e .
$$
在 $a=0,e$ 的固定小邻域，$|\partial^j G|\ll_j |x-a|^{-j}$ 对 $0\le j\le4$ 成立：在零点处光滑因子余项有二阶零点；在 $e$ 处的两个叉积的平方各提供二阶零点。在远处各阶导数为 $O_j(|x|^{-4-j})$。常数对紧参数集 $|e|=|z|=1,\ e\perp z$ 一致。令奇点处的 $G,H_e$ 格点值为零；在 $x=e$ 时 $H_e$ 按原式也为零。

**求积余项。** $0,e$ 都在 $h\mathbb Z^3$。对中心为 $y$ 的边长 $h$ 立方，用 Taylor 展开取平均可得
$\int_C G=h^3G(y)+h^5\Delta G(y)/24+O(h^7\sup_C|D^4G|)$。删去距两奇点 $O(h)$ 的有限个近胞，近胞的积分和格点项为 $O(h^3)$。其余胞四阶余项合计 $O(h^3)$，因为 $\int_{h<|x-a|<1}|x-a|^{-4}dx=O(h^{-1})$，逐胞上确界有同阶上界。又 $\int_{\mathbb R^3}\Delta G=0$：挖去半径 $\epsilon$ 的小球，边界通量为 $O(\epsilon)$，无穷远通量亦趋零。相同格胞对 $\Delta G$ 作二阶中点误差，近胞质量 $O(h)$，余胞总误差 $O(h^2 h^{-1})=O(h)$。故 $h^3\sum\Delta G(y)=O(h)$（近奇点可略），乘前面的 $h^2/24$ 后仍为 $O(h^3)$。这证明 $G$ 的格和与积分相差 $O(h^3)$，亦解释了 (1) 中为何没有二次项。

**晶格常数。** $H_e$ 的奇部分因 $p\leftrightarrow-p$ 对格和和积分均贡献零；原本删去的点 $p=k$ 贡献也为零。偶部分的角张量由立方晶格的符号与置换对称给出精确因子 $2/3$：在每个完整球壳 $\sum p_i p_j=\delta_{ij}\sum |p|^2/3$，故对任意 $e$ 一致。令 $\Theta(t)=\sum_{v\in\mathbb Z^3}e^{-t|v|^2}$。偶部分的格和减积分为
$$
 \frac{2h}{3}\int_{h^2}^\infty
       \left(\Theta(t)-1-(\pi/t)^{3/2}\right)\,dt,\qquad
 C_{\rm cub}=\int_0^\infty\left(\Theta(t)-1-(\pi/t)^{3/2}\right)dt.
$$
Poisson 恒等式 $\Theta(t)=(\pi/t)^{3/2}\Theta(\pi^2/t)$ 给积分下端的被积函数为 $-1+O(t^{-3/2}e^{-\pi^2/t})$，故此差为 $2h C_{\rm cub}/3+O(h^3)$。$C_{\rm cub}$ 亦是立方 Epstein zeta $\sum_{v\ne0}|v|^{-2s}$ 在 $s=1$ 的解析延拓值（由分段 Mellin 积分）。各单位二次型误差一致，原核实对称且消去 $k$ 方向，即得算子式 (1)。这一全方向结论使用一般 $e,z$ 的原求和，并未旋转离散晶格。其 $O$ 项没有在此求得可用于逐个中频的数值常数。

在 $t=\pi$ 处分段换元得到指数收敛式
$$
 C_{\rm cub}=-3\pi+
 \sum_{v\ne0}\left(\frac{e^{-\pi |v|^2}}{|v|^2}
       +\frac{\pi\,\mathrm{erfc}(\sqrt\pi|v|)}{|v|}\right).
$$
每个 $\mathrm{erfc}$ 项至多等于其前一项。截至 $\|v\|_\infty\le H$，用方壳 $24j^2+2$ 计数，遗漏量介于 $0$ 与
$52e^{-\pi(H+1)^2}/(1-e^{-\pi(2H+3)})$ 之间。取 $H=3$ 已得 $2C_{\rm cub}/3\in[-5.94242194505677,-5.94242194505676]$。

## 4. 裸格、因子和与无穷和的交叉复核

复算按原矩阵定义在五个有限球上用有理数累计两个对角元及交叉元，再与 (2) 比对。例如 $K=1,\ |p|^2\le2$ 得 $1181/450$，$K=2,\ |p|^2\le5$ 得 $6920294483417/1595635470000$，交叉元均为零。程序对 $1\le m\le65536$ 的每个 $r_2(m)$ 用有向格点和因子筛交叉验证。另对 20 个 $(K,m)$ 取 $|t|\le36$ 作有理求和，与 (3) 的完整纵向球算术结果比对；在 $N\ge2K$ 时删去的 $|t|>N$ 部分至多 $8Km/(5N^5)$，因为 $r\ge t^2,\ s\ge t^2/4$。

下表是**完整轴向无穷和**的包含区间。计算 (4) 用 $M=65536$，Arb 128 位球算术；$L(s,\chi_4)=4^{-s}[\zeta(s,1/4)-\zeta(s,3/4)]$ 用 Hurwitz zeta 计算，最后把端点十进位向外舍入。完整七组区间在 frequency_checked.json。

| $K$ | $\lambda_K$ 的严格包含区间 |
|---:|---|
| 1 | $[5.57378208,5.57378209]$ |
| 4 | $[10.11185255,10.11185256]$ |
| 8 | $[10.88094802,10.88094803]$ |
| 32 | $[11.44159616,11.44160296]$ |
| 64 | $[11.53448814,11.53470520]$ |

**一个严格非轴向分裂。** 对 $k=(1,1,0)$ 取 $u=(1,-1,0)/\sqrt2,\ v=(0,0,1)$。坐标交换 $x\leftrightarrow y$ 或反射 $z\mapsto-z$ 使交叉元消失，因此它们是横平面上的两个特征方向。对 $p=(x,y,z),\ r=|p|^2,\ s=|k-p|^2$，$D=\sqrt2(\lambda_v-\lambda_u)$ 精确等于
$$
 \sum_{p\ne0,k}\frac{(x-y)^4-4z^4}{2r^2s^2}.
$$
在 $\|p\|_\infty\le R=128$ 的方盒内，按 $x\leftrightarrow y,\ z\leftrightarrow-z$ 合并，4276735 个合法轨道各自将加权有理数乘 $10^{12}$ 再向下取整，和为 $247466290679$；方盒和与该值除以 $10^{12}$ 的差介于 $0$ 与 $4276735/10^{12}$ 之间。盒外单项绝对值 $\le 2/|k-p|^4$：$(x-y)^4\le4r^2,\ 4z^4\le4r^2$，两者非负。在 $\|p\|_\infty>R$ 有 $|k-p|\ge(1-2/(R+1))|p|$。若 $\xi$ 在中心为 $p$ 的单位格胞，则 $|\xi|\le(1+1/(R+1))|p|$ 且 $|\xi|>R$。逐胞积分得严格绝对尾界
$$
 \frac{8\pi}{R}\left(\frac{R+2}{R-1}\right)^4
 \ <\ \frac{392713750}{1821012487}\qquad(R=128,\ \pi<22/7).
$$
合并向外舍入后 $0.03180947\le D\le0.46312739$。这为完整无穷和证明了 $\lambda_v>\lambda_u$，给出了 (1) 的一致渐近各向同性与各固定方向精确对称之间的实际界线。

运行 frequency_check.py 需 Python 3 和 python-flint 0.9.0。该程序从定义重建各样本，未导入原 571 类证书或其预计算文件。对本次切面，原核到轴向壳、整数纵向求和、连续常数及高频首修正均有独立推导。完整常数 $6.45$ 的全部有限类、因果逆和限制族的成功或障碍证书仍待全链独立复算；正核的高频展开本身不判定任意初值的 NS 正则性。[原研究程序的依赖及范围](https://github.com/awdawmip/enterprise-math/blob/e17e50381a1ba51a2d1c8ad96e9440d08eb8ddc5/research_notes/ns_brc_program_handoff_20260917.md)
