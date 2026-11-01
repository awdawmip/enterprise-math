# PREFIX-415｜双基准带噪后来源支路切换依然存在：全连续观测盒的精确证书

2026-11-01 · 进取数论研究6 · **作者侧完整解析论证＋精确有理数检验；UNREVIEWED / NOT_ADMITTED / NO_NATIVE_CLAIM**。

## 来源与边界

固定 GLOBAL_KNOWLEDGE_V1 \`awdawmip/chatgpt-global-knowledge main@95be78648711bac64fc18da219c2cb328c6de142\`，原始 P000 blob \`770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc\`，Enterprise Math 科学输入 \`main@c1b3200a053883f81951d54f5d55356daec114ce\`；实际读取规范入口、P000、ACTIVE 世界观、项目角色入口、Portable Research / Autonomous Operations、BRC 约束和 PREFIX-411/413/414。GitHub 登录 \`awdawmip\` 具有仓库写权；原生科研服务 0.6.11 报 \`research_authority_granted=false\`、\`UPSTREAM_CODE_REVIEW_REQUIRED\`、active_jobs 5/5；Owner/任务读取报 \`CONTROL_QUOTA\`。所以当前活跃 Owner 未核实、未取得正式 CLAIM、Result、Review 或 admission。本次仅在 \`research_notes/\` 保全数学研究原文。

本命题属于**外部静态复振幅辅助模型**，不涉及 P000 原生 X6、三维切片第三分量、时间动力学或 typed BRC 运算。BRC 判定 \`COMPOSE_APPLIED\`：保留来源符号、复相位以及未来 η 变化所需的联合读数，不无证合并来源叶。

## 模型与精确定理

原始五 Port 复矩阵逐行为
\`(4,4,0); (0,-4,4); (-5+3i,0,-3+i); (-2-2i,4+4i,2+2i); (-2,0,5+2i)\`。
前三行可逆，取其归一化输出为 \`(1,u,v)\`，第四、第五输出：
\[
z_4=a+bu+4iv,\quad z_5=d(1+u)+ev,\quad
a=(5+9i)/2,\ b=(3+7i)/2,\ d=(22+15i)/8,\ e=(5+9i)/4.
\]
记 \(r=|u|^2,\ s=|1+u|^2,\ t=|v|^2,\ h=|1+v|^2-1,\ k=|z_5|^2-709/32,\ I_4=|z_4|^2\)。
固定 \(\beta=10^{-6}\)，令 \(0\le\varepsilon\le10^{-6}\)，约束为
\[
|r-1|\le\varepsilon,\quad |s-2|\le\varepsilon,\quad
t\le\beta,\quad |h|\le\eta,\quad |k|\le\eta.
\]
对 \(\sigma=\operatorname{sgn}(\Im u)\in\{+,-\}\) 两个真实相位来源叶，定义
\[
q_+^\varepsilon(\eta)=\max_{\sigma=+}(I_4-37),\qquad
q_-^\varepsilon(\eta)=\max_{\sigma=-}(45-I_4).
\]
合法集合均非空（\(u=\sigma i,v=0\)）、紧致；两叶的 \(I_4\) 在本范围分别严格低于、高于 41，故第四 Port 的最优误差半径为 \(4-\max(q_+^\varepsilon,q_-^\varepsilon)\)。

**定理 A（独立于 PREFIX-413 的全局最优公式）：** 对每一个 \(0\le\varepsilon\le10^{-6}\)，上述两极值在 \(\eta\in[7/4000,187/100000]\) 连续，且
\[
\boxed{q_+^\varepsilon(7/4000)-q_-^\varepsilon(7/4000)>1/12000},
\qquad
\boxed{q_-^\varepsilon(187/100000)-q_+^\varepsilon(187/100000)>1/20000}.
\]
因此至少有一个真实最优来源分支平局点满足
\[
\boxed{0.00175<\eta_\times(\varepsilon)<0.00187}.
\]
这保证 \(10^{-6}\) 以下的双基准联合误差**不能抹去来源叶最优值逆转**。不宣称 \(\varepsilon>0\) 时交叉唯一、是从零开始的第一次交叉或整个正半轴仅有一次交叉。

## 证明一：同时保留复相位与 v 的精确误差界

写 \(u=p+i\sigma q\)，有
\[
p=(s-1-r)/2,\quad q=\sqrt{r-p^2}>0,\quad
|p|\le\varepsilon,\quad |q-1|<3\varepsilon/5,
\quad |u-\sigma i|<6\varepsilon/5
\]
（\(\varepsilon=0\) 时差为零）；用到了 \(1-\varepsilon-\varepsilon^2>(999999/10^6)^2\)。
记 \(u_0=\sigma i\)，**保持同一个 \(v\)** 比较两组强度。因
\[
|d|<10/3,\ |e|<13/5,\ |d(1+u_0)+ev|<19/4,\quad
|b|<381/100,\ |a+bu_0+4iv|<27/4,
\]
用 \(|z+\Delta|^2-|z|^2=2\Re(\bar z\Delta)+|\Delta|^2\) 得
\[
\boxed{|k(u,v)-k(u_0,v)|\le40\varepsilon},\qquad
\boxed{|I_4(u,v)-I_4(u_0,v)|\le64\varepsilon}.\tag{1}
\]
\(h=2\Re(v)+t\) 完全不变。这给出保留同一来源叶的包络
\[
q_\sigma^0(\eta)\le q_\sigma^\varepsilon(\eta)
\le q_\sigma^0(\eta+40\varepsilon)+64\varepsilon.\tag{2}
\]
由 \(|v|\le10^{-3}\) 及相同上界亦得 \(|I_4(u,v)-I_4(u_0,0)|<1/10\)，而基准值分别为 37 与 45，所以两叶的第四强度在 41 两侧。

## 证明二：左端由正来源叶严格胜出

令 \(\eta_a=7/4000\)、\(B=37577/64\)、\(E=53/8\)、\(C=\eta_a-E\beta\)，\(S=\sqrt{B\beta-C^2}\)。
原矩阵对 \(u=i,v=x+iy\) 给出
\[
k=23x+(61/8)y+Et,\quad I_4-37=48x+8y+16t.
\]
构造实际来源 \(u=i\) 与
\[
x=\frac{23C+(61/8)S}{B},\qquad y=\frac{(61/8)C-23S}{B}.
\]
由两向量正交直接平方得 \(t=\beta\)、\(k=\eta_a\)；准确根包络
\(2416/100000<S<2417/100000\) 使 \(0<h=2x+\beta<\eta_a\)。
于是
\[
q_+^\varepsilon(\eta_a)\ge
\frac{1165C+182S}{B}+16\beta.\tag{3}
\]
对负来源叶，原矩阵精确恒等式
\[
45-I_4=\frac{-93h-48k+43t}{23}
\]
在 \(u=-i\) 成立；应用 (1)，对**全部扰动的负叶**有
\[
q_-^\varepsilon(\eta_a)\le
\frac{141\eta_a+48(40\varepsilon)+43\beta}{23}+64\varepsilon.\tag{4}
\]
以 \(S>2416/100000\)、\(\varepsilon\le10^{-6}\) 比较 (3)(4)，用纯有理算术严格得到
\(q_+^\varepsilon(\eta_a)-q_-^\varepsilon(\eta_a)>1/12000\)。

## 证明三：右端由负来源叶严格胜出

令 \(\eta_b=187/100000\)，取 \(u=-i\) 和 \(h=k=-\eta_b\)；消元得到
\[
x=-(\eta_b+t)/2,\quad y=45(t-\eta_b)/368,\qquad
t=(\eta_b+t)^2/4+(45/368)^2(t-\eta_b)^2.
\]
末式右边减 \(t\) 在 \(0\) 为正、在 \(t=\beta\) 为负，并在区间内严格下降，因此有唯一 \(t\in(0,\beta)\) 并给出合法真实来源，且
\[
q_-^\varepsilon(\eta_b)\ge(141\eta_b+43t)/23>141\eta_b/23.\tag{5}
\]
另一方面正叶有
\[
q_+^0=48x+8y+16t
=2k+2x-\frac{29}{4}y+\frac{11}{4}t
\le2k+\frac{\sqrt{905}}4\sqrt{t}+\frac{11}{4}t.
\]
由 (1)、\(\sqrt{905}<301/10\)，所有扰动的正叶满足
\[
q_+^\varepsilon(\eta_b)
<2(\eta_b+40\varepsilon)+301/40000+(11/4)\beta+64\varepsilon.\tag{6}
\]
(5)−(6) 在最坏 \(\varepsilon=10^{-6}\) 时有精确有理下界
\[
\frac{141\eta_b}{23}-
\left(2(\eta_b+40\cdot10^{-6})+\frac{301}{40000}
+\frac{11}{4}\beta+64\cdot10^{-6}\right)
=\frac{4799}{92000000}>\frac1{20000}.
\]
没有通过有限采样代替连续盒的全称量词。

## 证明四：两叶最大值函数连续

固定 \(u\)，取 \(v\to\lambda v\)（\(0\le\lambda<1\)），\(c(u)=|d(1+u)|^2-709/32\)。强度极化给出
\[
h(\lambda v)=\lambda h(v)-\lambda(1-\lambda)t,\quad
k(u,\lambda v)=(1-\lambda)c(u)+\lambda k(u,v)-\lambda(1-\lambda)|e|^2t.
\]
由 (1) 在 \(v=0\) 得 \(|c(u)|\le40\varepsilon\)；并且
\(40\cdot10^{-6}+(53/8)\beta<7/4000\)，\(\beta<7/4000\)。
于是对任意当前可行 \(v\) 和所有 \(\lambda<1\)，
\[
|h(\lambda v)|\le\lambda\eta+(1-\lambda)\beta<\eta,
\quad
|k(u,\lambda v)|\le\lambda\eta+(1-\lambda)(40\varepsilon+E\beta)<\eta.
\]
保持 \(u,t\) 其他约束，缩放到靠近 1 可从较小 \(\eta\) 的合法来源逼近原极值；故左连续。最大化集合紧致且约束闭，得上半连续；可行集随 \(\eta\) 嵌套，得右连续。两叶函数连续，(3)(4) 与 (5)(6) 异号，介值定理即定理 A。证毕。

## 更强定位（条件性依赖已有 PREFIX-413 作者侧结果）

若采用 PREFIX-413（UNREVIEWED）的当前两叶准确最优公式：在 \([3/4000,97/50000]\)
\[
q_+^0=(1165C+182\sqrt{B\beta-C^2})/B+16\beta,\quad
q_-^0=(141\eta+43t_\eta)/23,
\]
其中 \(t_\eta\) 是负叶二次约束唯一根，则由严格导数界 \(0<(q_+^0)'<2\) 和 \(141/23<(q_-^0)'<7\) 得
\[
m=141/23-1165/B=3583477/864271>4.
\]
设唯一基准交叉 \(\eta_0\in(0.001806822,0.001806823)\)。由 (2) 得任意扰动平局点
\(-144\varepsilon\le(q_+^0-q_-^0)(\eta)\le344\varepsilon\)，所以
\[
\boxed{\eta_0-\frac{344}{m}\varepsilon\le\eta_\times(\varepsilon)
\le\eta_0+\frac{144}{m}\varepsilon}.
\]
对 \(\varepsilon>0\)，放松为 \(\eta_0-86\varepsilon<\eta_\times<\eta_0+36\varepsilon\)。
这是**所有可能平局点**的范围，不是新求得的唯一根或导数。此节依赖 PREFIX-413 未经独立审核的定理；前四节存在性与严格端点优势不依赖之。

## 实际验证、外部背景及下一问题

作者实际执行了标准库 \`Fraction\` 精确不等式检查器，回报 \`PASS_PREFIX415_UNIFORM_CROSSING_STABILITY_EXACT_RATIONAL_CERTIFICATE\`；另运行 SymPy 检查器，从完整原始 \(5\times3\) 复矩阵反演各 Port，回报 \`PASS_PREFIX415_INDEPENDENT_ORIGINAL_FIVE_PORT_ALGEBRA\`。GitHub 代码为相同决定性证书的便携版，完整本地扩展代码、运行日志、中文扩展证明及 SHA256 校验保留于研究证据包；不主张 GitHub 便携版与本地扩展版逐字节相同。连续全称结论由上述解析推导而非测试覆盖率承担。

背景引用：Candès–Strohmer–Voroninski, *PhaseLift: Exact and Stable Signal Recovery from Magnitude Measurements via Convex Programming*, **CPAM** 66(8):1241–1274 (2013), DOI \`10.1002/cpa.21432\`。其随机恢复假设不同于本固定确定性五 Port，本研究不宣称由该文献推出当前证书或原创优先权。

**PREFIX-416：** 求 \(\varepsilon>0\) 下各观测区间活跃角点，证明/反驳平局唯一性，并仅在确立横截性后求 \(\eta_\times'(0+)\)；另研究全 \(\eta\) 半轴的二次切换。原生 X6、三维切片第三分量及 typed BRC 动力学需另证对应。
