# all20 相对首返的 common-depth 双侧逐点尾律

状态：`ANCHOR_EXPOSED / LOCAL_PROOF_COMPLETED / OWNER_REVIEW_PENDING / NOT_FORMAL_V2`。

辅助工作包 `/root/stability_research`，2026-09-07；不领取正式 claim，不宣称 CLEAN FREE、全局新颖性或新 Foundation。Global Knowledge 沿用有效读取租约 `main@4fa7d7d0c19a5e80a681b33c8ee2ab643ce97563`。

**本单元结论。** 对声明的十二个 signed primitive 步各权 `1/12` 的研究步行，令 τ 为二十个 can3 观察同时相对回零的首次正时间，`Z_τ=HD`、`D=(1,1,1,1,1,1)`，则

\[
\boxed{\mathbb P(\tau<\infty,H=h)
\sim \frac{1}{12\pi^3 S^2}|h|^{-4}\quad(|h|\to\infty),
\qquad S=\sum_{h\in\mathbb Z}G_{\mathbb Z^6}(hD).}
\]

这里 `1<S<∞`，概率没有以首返发生事件重新归一化。证明直接处理双侧整数卷积，使用 Green 的 `O(|h|^{-6})` 余项和一个自足的 Fourier 倒数引理。没有倒用半线更新定理，也没有以大规模步行枚举或拟合替代渐近证明。

## 1. 原生对象、首次事件与质量投影

固定当前 signed X6 affine Cell torsor 的共同 anchor 和 primitive 坐标 chart。`Z_0=0` 表示所选 anchor。每步在 `±E_i,1≤i≤6` 中独立选择，十二条正 BRC 分支各给权 `1/12`。概率解释来自这一额外声明的归一化步律，不是从 P000 推导物理随机性。

对三轴集合 I，观察是 `can3((Z_n)_I)`。所有二十个观察同时为零，当且仅当六坐标全相等，即 `Z_n∈ZD`。只需注意任何轴对都落在一个三轴集合内即可证明此条件。因此定义

\[
\tau=\inf\{n\ge1:Z_n\in\mathbb ZD\},\qquad
f_n(h)=\mathbb P(\tau=n,Z_n=hD),\quad
F(h)=\sum_{n\ge1}f_n(h).
\]

H 只在 `τ<∞` 上定义。`hD` 是真实原生位移，不能因为所有 can3 回零就把它当作原生零位移。这里保留了终点 common-depth h；该标量是已有六坐标中的复合方向，不是第七空间轴。

每个固定 n,h 的原词观察为 `a_n(h)[12^{-n}]`：`a_n(h)` 是满足首次条件的具体 signed word 数。降为 `f_n(h)=a_n(h)12^{-n}`、再对 n 求和为 F(h)，是明确声明的质量观察。不同长度的词权和词身份没有因此被保留在 F 中；尤其不能把 F(h) 当作一条原词权或有限 WeightHistogram 的完整替代。

## 2. 先验覆盖与来源选择

本题直接复用 `OWNER_NEXT_FRONTIER_SCOUT_20260907.md` 已有 signed BRC / finite-port coverage，再有界读取：

- `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py` 的 `endpoint_multiplicity`、`endpoint_weight`；它们给有限长度端点核。
- 同目录 `x6_signed.py` 的 `relative_class`、`from_residual_depth`、`joint_slice_equal`；它们提供原生 Cell 与观察的类型边界。
- `brc_weighted_recurrent.py` 开头明确限于有限状态，`brc_recurrent_ports.py` 需要稳定的有限 hidden block；现有 path monitor 又带有限图/horizon 条件，不能直接认证本题无限相对格的尾。

冻结 Fourier 反演候选后运行

```text
python -X utf8 tools/enterprise_toolbox.py --json coverage Fourier Green reciprocal derivative jump renewal
```

结构化结果保存为 `experiments/owner_common_depth_first_return_coverage_20260907.json`。词面命中的是 multiplier jump、Pell 导数和有限 critical-orbit 等接口；检查其声明范围后，没有将它们误当本题双侧 Green 倒数定理。首次输出夹有现有文件的转义 SyntaxWarning，已按 JSON 起始位置保存有效对象；这不是数学失败，也未为此修改控制面工具。

外部主依赖只用 [Lawler–Limic, Random Walk: A Modern Introduction，作者 PDF](https://www.math.uchicago.edu/~lawler/srwbook.pdf)，Theorem 4.3.1，pp.81–83。实际读过定理、简单步行特例及二分周期处理段。Fourier 反演所需引理在第 5 节完整证明。

[Asmussen–Foss–Korshunov 作者论文](https://arxiv.org/pdf/1303.4709) §6 Proposition 12 已核对：该节从 `(0,∞)` 上的非负测度出发，局部结论另有长尾/次指数前提。本题 F 在 Z 两侧有质量，且出发已知 U 的尾；该结果没有被作为反向推理依据。检索到其他卷积尾文献不等于其条件已覆盖本题，因此没有把未经逐条核验的定理列为依赖。

## 3. 真正双侧的缺陷更新恒等式

定义访问核

\[
u_n(h)=\mathbb P(Z_n=hD),\quad U(h)=\sum_{n\ge0}u_n(h).
\]

按首次访问相对零 fiber 的时刻和该时刻的完整 h 分解，并在 `kD` 处重新开始步行。平移不变性给出

\[
u_n(h)=\mathbf1_{n=0,h=0}
 +\sum_{t=1}^n\sum_{k\in\mathbb Z} f_t(k)u_{n-t}(h-k). \tag{R_n}
\]

这是真正的双侧卷积：k 与 h−k 可以为负，也可以异号。每个固定 n 的内层只有有限项，零长 excursion 被 `t≥1` 排除。分解不把相对返回与原生返回混为一谈。

第 4 节给出 `U∈ℓ¹(Z)`，所以 `S=Σ_h U(h)<∞`。先按非负项用 Tonelli 对 n 求和，再对 h 求和，得到

\[
U=\delta_0+F*U,\qquad S=1+pS,
\qquad p:=\sum_h F(h)=\mathbb P(\tau<\infty)=1-S^{-1}<1. \tag{R}
\]

`p>0`，因为最短反向两步已给 `f_2(0)=1/12`；于是 `S>1`。此外，重复展开 (R) 并用 `\|F^{*m}*U\|_1=p^mS→0`，严格有

\[
U=\sum_{m\ge0}F^{*m}\quad\hbox{在 }\ell^1(\mathbb Z)\hbox{ 中成立}. \tag{G}
\]

这一步包含首返核在 h=0 的正原子，没有假设每次首返都产生非零深度增量。

采用 Fourier 约定 `\widehat a(θ)=Σ_h a(h)e^{ihθ}`。由 ℓ¹ 卷积，

\[
\widehat U(θ)=\frac1{1-\widehat F(θ)},\qquad
\frac1{1+p}\le|\widehat U(θ)|\le\frac1{1-p}. \tag{W}
\]

所以 `\widehat U` 在整个圆周上无零，且 `\widehat U(0)=S`。符号反转整个 signed word 还给 `F(h)=F(-h)`、`U(h)=U(-h)`。因而此处 `\widehat U` 实且为正；没有任何分母零点被略去。

## 4. Green 常数、余项与周期性

Lawler–Limic Theorem 4.3.1 的简单步行特例为

\[
G_{\mathbb Z^d}(x)
=\frac{d\,\Gamma(d/2)}{(d-2)\pi^{d/2}}|x|^{2-d}
+O(|x|^{-d}).
\]

在 d=6，系数为 `3/π³`。对 `x=hD`，分量平方和为 `|hD|²=6h²`，故

\[
U(h)=\frac{1}{12\pi^3}|h|^{-4}+O(|h|^{-6})\quad(h\ne0,\ |h|\to\infty). \tag{A}
\]

这是标准六分量步律及其协方差的数学表示；没有把概率分析用的协方差度量升级为新的原生正角或空间定义。有限个 h 的 U(h) 也都有限，所以 (A) 给 `S<∞`。

本步行在时间上周期为 2：每步使坐标总和的奇偶翻转，而 `Σ_i(hD)_i=6h` 总为偶数，所以 `f_n(h)=u_n(h)=0` 于奇数 n。引用的 Green 核已经对所有 n 求和；作者 p.82 明确将二分周期情形纳入证明。因此不能再额外乘上时间周期 2。

深度 h 没有二倍子格限制。对任意 h>0，依次走 `E_1^h E_2^h ... E_6^h`；其所有真前缀不在 ZD，终点是 hD。h<0 取反向词。因此 `F(h)>0` 对每个 h≠0 成立，而 `F(0)>0` 已知。其空间格距为 1，没有额外周期因子。

无需数值 S，也可给其完全确定的积分表达。仅作为相对观察的辅助编码，设

`Y=(Z_1−Z_6,...,Z_5−Z_6)`。

则 Y=0 正好对应 Z∈ZD，步特征函数为

\[
\phi_Y(\theta)=\frac16\left[\sum_{i=1}^5\cos\theta_i+
\cos\left(\sum_{i=1}^5\theta_i\right)\right].
\]

于是

\[
S=\frac1{(2\pi)^5}\int_{[-\pi,\pi]^5}\frac{d\theta}{1-\phi_Y(\theta)}. \tag{S}
\]

此式可先在几何参数 0<r<1 下积分 `1/(1-rφ_Y)`，再取 r↑1。唯一 `φ_Y=1` 点是原点模 2π，非退化二次项使被积函数局部为 `O(|θ|^{-2})`，在该五变量辅助积分中可积。该五变量是相对观察编码，不宣称原生空间是五维；完整终点 H 仍在本题中保留。本文不将此积分作浮点求值或声称数值包围。

## 5. 自足的双侧 Fourier 倒数尾引理

**引理。** 令 `a∈ℓ¹(Z)` 是实偶数组，其 Fourier 函数在圆周上无零。设对 h≠0

\[
a(h)=c|h|^{-4}+e(h),\qquad
\sum_{h\ne0}|h|^4|e(h)|<\infty,
\qquad A=\sum_h a(h)\ne0.
\]

记 `v(h)` 为 `1/\widehat a` 的 Fourier 系数，则

\[
v(h)=-\frac{c}{A^2}|h|^{-4}+o(|h|^{-4})\quad(|h|\to\infty). \tag{I}
\]

该引理适用于本题的双侧 ℓ¹ 卷积逆。它要求明确的加权可求和余项；本文没有声称只知道 `a(h)∼c|h|^{-4}` 就足以进行下面的四阶光滑性推理。

**证明第 1 步：构造准确的 cusp 模板。** 在 `[-π,π]` 上取周期函数

\[
K(\theta)=\frac{\pi^4}{45}-\frac{\pi^2\theta^2}{6}
+\frac{\pi|\theta|^3}{6}-\frac{\theta^4}{24}. \tag{K}
\]

K 的圆周平均为 0，在 ±π 的各阶导数直到四阶均匹配。它在原点 C²，三阶导的跳跃为

`K'''(0+)−K'''(0−)=2π`，

且每侧普通四阶导数为 −1。对 h≠0 分成两段四次分部积分，只有这个三阶跳跃留下边界项，常数 −1 的非零 Fourier 系数为零，因此

\[
\frac1{2\pi}\int_{-\pi}^{\pi}K(\theta)e^{-ih\theta}d\theta=h^{-4}.
\]

这也直接证明 `K=2Σ_{h≥1} cos(hθ)/h⁴`，而不是假设级数可无条件逐项四次微分。原点跳跃与圆周接缝的角色已经分别核对。

**第 2 步：余项四阶光滑。** 设

`E(θ)=a(0)+Σ_{h≠0}e(h)e^{ihθ}`。

加权绝对可求和保证 E 的零至四阶导数级数一致收敛，故 `E∈C⁴` 且周期。因此 `\widehat a=cK+E` 在圆周上 C²、在原点两侧 C⁴，其三阶导的唯一跳跃是 `2πc`。

**第 3 步：倒数跳跃。** 无零性和圆周紧致性保证 `V=1/\widehat a` 同样 C²、分段 C⁴。在三阶导的链式公式中，除 `-\widehat a'''/\widehat a²` 外的各项只含零至二阶连续导数。因此

\[
J:=V'''(0+)-V'''(0-)=-\frac{2\pi c}{A^2}. \tag{J}
\]

V 及其导数在 ±π 匹配；没有接缝上的第二个跳跃。两侧普通四阶导数构成一个有界、分段连续的函数 g，因而 `g∈L¹[-π,π]`。

**第 4 步：直接取 Fourier 系数。** 对 V 分段四次分部积分得，对任意非零整数 h，

\[
h^4v(h)=\frac{J}{2\pi}
+\frac1{2\pi}\int_{-\pi}^{\pi}g(\theta)e^{-ih\theta}d\theta. \tag{C}
\]

等价地，分布四阶导数为 `g+Jδ_0`。Riemann–Lebesgue 引理使第二项在 h→+∞ 和 h→−∞ 都趋零。代入 (J) 得 (I)。这里 Fourier 系数衰减本身也给 v∈ℓ¹，不需要先假定一个半线更新核或调用 Wiener 逆定理来得到尾。证毕。

## 6. 应用、准确常数与已知矩阈值

对 a=U，(A) 给 `e(h)=O(|h|^{-6})`，因此

`Σ_{h≠0}|h|⁴|e(h)|<∞`。

(W) 给全圆周无零、A=S；引理适用。由 (W)，`V=1/\widehat U=1-\widehat F`。故当 h≠0 时 `v(h)=−F(h)`。取 `c=1/(12π³)`，得到

\[
F(h)=\frac{1}{12\pi^3S^2}|h|^{-4}+o(|h|^{-4}).
\]

这给全部整数两端的同一个逐点极限，没有保留未解释的奇偶子列。若另行研究条件律 `H | τ<∞`，其质量要再除以 `p=1−1/S`，渐近常数相应为 `1/(12π³pS²)`；不能混用条件与非条件版本。

三阶绝对矩阈值在 scout 中已经由 Green 加非负更新展开证明：`Σ_h |h|^aF(h)<∞` 当 `0<a<3`，在 `a≥3` 发散。本单元的逐点结果与其一致，但不把阈值重新标为未知或新贡献。S、p 的有限性和缺陷更新也属于复用前置结论。

## 7. 小解析检查、消费接口与停止边界

仅新增一个标准库 Fraction 小检查：

```text
python experiments/owner_common_depth_first_return_check_20260907.py
```

结果 `PASS`。它核对 K 两侧有理多项式的平均零、±π 接缝的零至四阶导数匹配、原点三阶跳跃 `2π`、倒数三阶跳跃的负号和 `−A^{-2}` 因子，并以既有 `endpoint_multiplicity` 只读取两类最小系数：

`f_2(0)=1/12`，`f_6(1)=f_6(-1)=6!/12⁶=5/20736`。

两步相对返回必是反向两步；到 ±D 的六步都是各正/负轴恰一次，真前缀不能相对回零，所以这些端点系数确是首次系数。没有运行旧步行枚举脚本、Monte Carlo、大 horizon DP、Fourier 数值拟合或 S 的数值求值。

本结果可被新 consumer 调用的数学接口是：声明上述 signed 步律与首次事件，使用完整 U 的主项、足够强余项和双侧更新，得到 F 的非条件质量尾常数。它没有提供自动验证任意输入尾假设的程序，也不能把仅有有限访问表的调用者标成“尾已认证”。有限 port/recurrent/Histogram 接口仍按各自有限合同使用。

本候选 B 的指定逐点目标在这些完整条件下闭合。改变步律、改变被命中的子格、只有较弱 Green 余项、要求有效数值误差界或完整 word-weight 观察，都需要重新核对条件。没有在本轮自动派生新的正式研究任务，也未将标准 Fourier 奇性分析包装为新的顶层 BRC family。

## 8. 字节来源与证据冻结

| 文件 | SHA256 |
| --- | --- |
| `research_notes/OWNER_NEXT_FRONTIER_SCOUT_20260907.md` | `81ca246abbfcb91e677e6b653eac6d35d4359d828b1764bef911c167b8c6cd1e` |
| `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md` | `519a16725156be5461c6e28a0dcef664e267cff4e85120cfb257d5d540ec459e` |
| `experiments/x6_signed_native_spatial_v16_20260905/x6_signed.py` | `e48b6f2133edc588fde98b1b0f02ce27fecda915b152b7901300898920d52b8e` |
| 同目录 `signed_brc.py` | `6f0d79a519c53fed1300b3fabf500c34e30aa46cdd63b409fa6ecc115071ecb4` |
| `src/enterprise_math/brc_weighted_recurrent.py` | `7520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26` |
| `src/enterprise_math/brc_recurrent_ports.py` | `7cda953e1f01c537f0747becc666b3c5e2255c20006b9e948c570623250f02b9` |
| 本次小检查脚本 | `ca169914e24600a1f2ee1f004f0db6ba14f205faeebe53e310edb2a140f7b56b` |
| 本次小检查 JSON | `c23f3119d26660322f4a652757216117e41bf793a189e1f0bd651c8181d383a4` |
| 本次 coverage JSON | `29bf078e10df0cc664418df1694c366ff1a34c7ad40b2ad69171a3fd73fd71b2` |

作者 PDF 第 81–83 页在网络文本读取超时时，以同一作者 URL 下载到本地临时目录后直接读取；没有把读取超时当数学证据。本任务未修改任何 canonical 工具、旧定理、taskbook 或 claim，未提交或推送。
