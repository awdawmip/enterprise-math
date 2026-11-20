# R5 | 偶数故障门槛的四周期 N^21 精确系数

研究日期：2026-11-21（Asia/Shanghai）。
状态：AUTHOR_SYMBOLIC_PROOF / EXACT_FINITE_CHECKED / NOT_REVIEWED。

## 冻结对象与可复算来源

沿用 R5 非自适应标量查询计数：256 个具名假设、价格集合 P={214,...,314}、可重复查询及 m=2f+e+1。原始输入 \`EXACT_R5_ALL_101_BUDGETS.json\` 的前驱 SHA-256 为 \`50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b\`。本轮只继承极小分离集合的原证书，未重新核验原始 JSON 字节或重做 32,640 对假设枚举。

不可变前驱：
- \`awdawmip/enterprise-math@00fc3f2d975c2ab02bf90cc27f015500d47b1b13:research_notes/portable_direct/r5_rare_failure_n78_20261120/HIGH_DEGREE_48_THEOREM.md\`；
- \`awdawmip/enterprise-math@1754824da022dda63a16cb9c6faaf092b1201b21:research_notes/portable_direct/r5_even_fourth_root_20261121/RESEARCH.md\`；
- \`awdawmip/enterprise-math@3f299cfbc2b36137d43d15ce9007d79ac21a4b0f:research_notes/portable_direct/r5_odd_fourth_root_second_20261121/RESEARCH.md\`。

本研究仅指该冻结计数模型的离散结构残差，不作心跳原生物理、X6 或 BRC 同构归因。

## 定理：所有固定偶数 m 的 N^21 四周期系数

设 S0={214,215,216,217,218}，S1={214,216,217,218,219,220,221}，
S2={215,216,217,218,219,220,221}，U={214,...,221}。对 j=0,1,2 定义有限多项式

\[
H_{j,m}(q)=\sum_{\mathbf n\ge0,\ \sum_{p\in S_j}n_p<m}q^{\sum pn_p}.
\]

在 U 上令 a_j=1{sum_{p∈S_j}n_p<m}、h=max(a0+a1+a2-1,0)，并置
\(H_{h,m}(q)=\sum_{\mathbf n\in\mathbb N^U}h(\mathbf n)q^{\sum pn_p}\)。
对 j=0,1,2,h，记

\[
u_j=H_{j,m}(i),\qquad d_j=-iH'_{j,m}(i)=-\sum_{\mathbf n}w_j(\mathbf n)\,C(\mathbf n)\,i^{C(\mathbf n)},
\]
\[
v_0=-H''_{0,m}(i)=\sum_{\mathbf n}C(\mathbf n)(C(\mathbf n)-1)i^{C(\mathbf n)},\quad C(\mathbf n)=\sum pn_p,
\]
其中 w0,w1,w2=1，wh=h。

令 \(Q_4=\prod_{p=220,224,\ldots,312}p\)、\(A=(2^{48}Q_4)^{-1}\) 和

\[
b_0=12780-24i,\quad b_1=12558+\tfrac{169}{2}i,\quad
b_2=\tfrac{25115}{2}-23i,\quad b_h=\tfrac{24901}{2}-23i.
\]

前驱首项为
\[
D_m=d_0+220(1-i)u_1+220u_2-440u_h.
\]
本轮新的**全门槛有限精确系数**为
\[
\boxed{\begin{aligned}
E_m={}&\frac{v_0}{2}+(b_0+\tfrac{23}{2})d_0\\
&+220(1-i)[(b_1+\tfrac{23}{2})u_1+d_1]\\
&+220[(b_2+\tfrac{23}{2})u_2+d_2]\\
&-440[(b_h+\tfrac{23}{2})u_h+d_h].
\end{aligned}}
\]

**定理。** 对每个固定偶数 m≥2，仅取 q=±i 两个单位根对失败方案成本计数的贡献，有
\[
\boxed{
\frac{2A}{22!}\operatorname{Re}(D_mi^{-N})N^{22}
+\frac{2A}{21!}\operatorname{Re}(E_mi^{-N})N^{21}
+O_m(N^{20}).}
\]
余项只对该单位根对成立。全部定义都是有限整数/高斯整数加权求和，不依赖样本拟合。

## 证明

写 s=1-q/i。对自由价格集合 E，若 4|p，则
\((1-q^p)^{-1}=(ps)^{-1}(1+(p-1)s/2+O(s^2))\)；
其余价格因子为
\((1-i^p)^{-1}(1-pi^p s/(1-i^p)+O(s^2))\)。
于是自由乘积首个相对修正为
\[
b(E)=\sum_{p\in E,\ 4\mid p}\frac{p-1}{2}
-\sum_{p\in E,\ 4\nmid p}\frac{pi^p}{1-i^p}.
\]
四个相关自由集依次是 E0=219..314，E1={215}∪222..314，
E2={214}∪222..314，Eh=222..314；可直接求得上列 b0,b1,b2,bh。
它们在 q=i 的极点阶数为 24,23,23,23，首阶常数与 A 的比值分别是
1、220(1-i)、220、440。

每个局部有限多项式在 q=i(1-s) 处有
\(H_{j,m}=u_j+d_js+(v_j/2)s^2+O_m(s^3)\)。
偶数 m 时原已证 \(u_0=0\)，故 s^{-24} 项消失。严格沿用
\(G_0+G_1+G_2-G_h\) 的重叠容斥，得到
\[
G_m(i(1-s))=A D_m s^{-23}+A L_m s^{-22}+O_m(s^{-21}),
\]
其中
\[
L_m=v_0/2+b_0d_0+220(1-i)(b_1u_1+d_1)
+220(b_2u_2+d_2)-440(b_hu_h+d_h).
\]
含 S4 的其余事件及 S3 在 q=i 的自由4倍数不超过20，故不能影响上述两项。
抽系数时
\([q^N](1-q/i)^{-23}
=i^{-N}\binom{N+22}{22}
=i^{-N}[N^{22}/22!+(23/2)N^{21}/21!+O(N^{20})]\)，
\([q^N](1-q/i)^{-22}
=i^{-N}[N^{21}/21!+O(N^{20})]\)。
加共轭项，得到 E_m=L_m+(23/2)D_m，证毕。

## 新的结构性推论：门槛的准多项式周期界

偶数 m 序列 E_m **最终是准多项式，准周期整除8**；本轮不主张最小周期恰为8。证明不依赖有限外推。设 z 为门槛计数变量，定义

\[
M(a,b;z)=\frac{1-abz^2}{(1-az)(1-bz)(1-abz)},
\quad T(a,b,c;z)=\frac{1-abcz^3}{(1-abcz^2)(1-az)(1-bz)(1-cz)},
\]
\[
S(a,b,c;z)=\frac{M(b,c;z)}{1-az}+\frac{M(a,c;z)}{1-bz}+\frac{M(a,b;z)}{1-cz}-T(a,b,c;z).
\]
令 \(c_r(q)=\prod_{s\in\{219,220,221\}\setminus\{r\}}(1-q^{s-r})^{-1}\)，
则在 q=i 的邻域（q^219、q^220、q^221 互异）有精确恒等式
\[
\sum_{m\ge1}H_{h,m}(q)z^m
=\frac{z}{1-z}\prod_{p=216}^{218}(1-zq^p)^{-1}
\sum_{r=219}^{221}c_r(q)S(q^{214},q^{215},q^r;z).
\]
这由三项两两交集减去三重交集、对三个价格219–221的完整齐次多项式作部分分式分解直接获得。
对其施加 q∂q，及对
\(\sum_{m\ge1}H_{j,m}(q)z^m=\frac{z}{1-z}\prod_{p\in S_j}(1-zq^p)^{-1}\)
施加一次或两次 q∂q，得到 E_m 的有理 z-母式。代 q=i 后所有可能的 z 极点均满足 z^8=1（分母只有 1-ζz 与 1-ζz²，ζ⁴=1），其偶数项亦然。部分分式定理推出最终准多项式及上述周期上界。

## 精确复算与未审范围

本轮本地使用整数对 (real,imag) 的 Z[i] 计算，Python 标准库 Fraction 保持精确性：
- m=2,4,...,20 的十组 D_m 与不可变前驱公式逐项一致；
- 十组 E_m 精确求值；
- m=2、4 使用独立八变量直接穷举及三类短事件直接枚举，对 H、d、v 全部核对一致；
- 未在本轮重新跑全体假设对、形式证明或独立外部同行审查。

完整表格及计算程序见同目录 RESULT.json、VERIFY.py。下一步：化简 E_m 有理母式、确定最小准周期，并计算更高阶单位根分量；自适应八错误原界限 8335≤C8*≤8343 保持为独立未决问题。科研 Source、Activity、正式 CLAIM/Result/Review 分别记录，当前保存不自动构成任何一项审查接纳。