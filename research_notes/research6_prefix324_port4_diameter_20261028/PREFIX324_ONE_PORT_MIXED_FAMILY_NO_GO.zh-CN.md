# PREFIX-324｜单 Port 圆周直径定理：同尺度两形状 BRC 家族不可能突破 L

2026-10-28，Research6 作者侧全域解析推导；AUTHOR_SIDE_EXACT_AUXILIARY_BRC_PROOF / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING。

## 精确模型

在静态辅助 S7-3 复数三来源、五 Port 模型内，保留 source:1/2/3 和独立 reference 标签的全部有序 BRC 路径对。设
\[
U=\tfrac18\begin{pmatrix}
4&4&0\\0&-4&4\\-5+3i&0&-3+i\\-2-2i&4+4i&2+2i\\-2&0&5+2i
\end{pmatrix},\quad b_0=(-2,-2i,1),\ b_2=(2i,2,-i).
\]
状态来自同一尺度 \(r>0\) 的 \(rzb_0,rwb_2\)，单位复相位连续取值。对每个 Port，准确基础正质量 \(Q_0=|\sum_{k=1}^3U_{jk}a_k|^2\) 与十项独立有界误差参考 \(Q_1,Q_i\) 的来源保真定义为对三个 source 及 optional reference 的每个有序路径对 \(u_p\bar u_q\) 累加，其中 \(Q_\rho=|\sum_kU_{jk}a_k+\rho|^2,\rho=0,1,i\)。五项 Q0 必须完全一致；十项测量的每项误差绝对值不超过1。集合 S 非空、紧、包含至少一种 b0 与 b2 来源（任意连续纤维或其紧子集）。风险是完整输入空间 \(\mathbb C^3\simeq\mathbb R^6\) 中的最小覆盖球平方半径 \(\operatorname{MEB}^2(S)\)。

上游 PREFIX-321 的作者侧全相位尺度定理证明任一这样的混合报告满足 \(r^2\le29/98\)。以下新导出的 Port4 逐尺度界不依赖这一临界尺度结论，仅最终统一界依赖该已发表作者侧定理。

## 定理

\[
\boxed{\operatorname{MEB}^2(S)\le411/196
< L:=1062562/458329,\quad
L-411/196=19888933/89832484>0.}
\]
更具体地，\(r^2\le16/75\) 时 \(\operatorname{MEB}^2(S)\le9r^2\le48/25\)；
\(r^2>16/75\) 时
\[
\boxed{\operatorname{MEB}^2(S)\le (29/6)r^2+2/3.}
\]
这回答 PREFIX-323 留下的整个中间尺度疑问：任何自由十参考报告、连续两相位以及两形状任意多态共同纤维，都不能提供 \(R^2>L\) 的见证。结论限于这两个固定形状及**同尺度**；不能外推至单形状可变尺度、更多独立形状、异尺度同 Q0 或完整辅助模型、原生 X6。

## 引理1：圆周直径与凸包投影

设紧集 \(T\) 在实二维、半径 \(R>0\) 的圆周上，直径 \(D\)。若 \(D<\sqrt3R\)，则零点不在 \(\operatorname{conv}T\)，且
\[
\operatorname{dist}(0,\operatorname{conv}T)^2\ge R^2-D^2/4.
\]
证明：若零点在凸包，Carathéodory 定理给出最多三点的表示。两点时必须为对径点，弦长 \(2R\)。若是三点，圆上的三个循环间隙各不超过半圆（否则三点落在不含原点的开半圆），而间隙和为整圆；故至少有一个间隙不小于整圆的三分之一且不超过半圆，其弦长至少 \(\sqrt3R\)。这与直径限制矛盾。此处仅用外部欧氏圆的几何顺序及等边三角形弦长，不进行任何心跳世界 π/三角函数数值运算。设 h 为凸包到原点的最近点；因原点在凸包外，h 所在的支撑直线与圆周最多相交于两个点 u,v，且 h 是这两个实际 T 点的凸组合（紧性+支撑面上的凸组合分解）。圆周等范数给出 \(\|(u+v)/2\|^2=R^2-\|u-v\|^2/4\)，中点为该弦最近原点之点。因此 \(\|h\|^2\ge R^2-D^2/4\)。

## 引理2：同范数来源的最小覆盖球

若紧集 S 在实 Hilbert 空间的半径 \(\rho\) 球面上，\(h=\operatorname{proj}_{\operatorname{conv}S}(0)\)，则
\[
\operatorname{MEB}^2(S)=\rho^2-\|h\|^2.
\]
上界来自对每个 a∈S 的 \(\langle a,h\rangle\ge\|h\|^2\)。下界来自有限凸表示 \(h=\sum\lambda_i a_i\)：任意球心 x 的加权平方距离恰为
\(\sum\lambda_i\|a_i-x\|^2=\rho^2-\|h\|^2+\|x-h\|^2\)。上下匹配，证毕。

## 单 Port 全域证明

选择第4 Port 输出线性算子 \(\ell(a)=(Ua)_4\)，保留三个来源路径计算
\[
\ell(b_0)=(7-i)/4,\quad \ell(b_2)=(7+i)/4,\quad
|\ell(b_0)|^2=|\ell(b_2)|^2=25/8.
\]
Port4 行为 \(((-1-i)/4,(1+i)/2,(1+i)/4)\)，故 \(\|\ell\|_{\rm op}^2=3/4\)；每态完整输入范数平方 \(9r^2\)，其输出属于半径平方 \(R^2=(25/8)r^2\) 的**同一圆周**。

按来源标签执行 BRC 后，参考路径与 source 路径对严格给出：
\(Q_1=Q_0+1+2\operatorname{Re}\ell(a)\)、
\(Q_i=Q_0+1+2\operatorname{Im}\ell(a)\)。
所有状态共享准确 Q0 和同一份误差≤1报告，因此任意两状态在 Port4 的实部输出差≤1、虚部差≤1。于是 \(T=\ell(S)\) 的直径平方 \(D^2\le2\)。

对 \(r^2>16/75\)，有 \(3R^2>2\ge D^2\)，满足引理1，于是
\[
\operatorname{dist}(0,\operatorname{conv}\ell S)^2
\ge (25/8)r^2-1/2.
\]
线性映射 \(\ell(\operatorname{conv}S)=\operatorname{conv}\ell(S)\) 与 \(|\ell(x)|^2\le (3/4)\|x\|^2\) 推出
\[
\operatorname{dist}(0,\operatorname{conv}S)^2
\ge(4/3)[(25/8)r^2-1/2].
\]
结合引理2，即
\[
\operatorname{MEB}^2(S)
\le9r^2-(4/3)[(25/8)r^2-1/2]=(29/6)r^2+2/3.
\]
对小尺度 \(r^2\le16/75\)，用原点球心直接得 \(R_{\rm MEB}^2\le9r^2\le48/25\)。
最后复用 PREFIX-321 已发布的全相位临界尺度 \(r^2\le29/98\)，大尺度界最多为 \((29/6)(29/98)+2/3=411/196\)；且 \(48/25<411/196<L\)。定理证毕。

## 证据及范围

辅助静态BRC观察是 \(\ell\) 的合法输出，Port4 并未替代全部状态；Port4 压缩只用于本次 MEB 的算子范数不等式，未宣称对未来操作保真。原生六维 X6、三维切片、Detector、时间动力学的转移映射待单独证明。

在本轮作者侧本地运行 Python 标准库 Fraction 高斯有理 BRC 检查器，结果 PASS：2态×5Port×(Q0,Q1,Qi)=30项正质量，逐项展开 410 个保留 source/reference 标签的有序路径对；所有五项 Q0、十项共享测量报告、Port4 行范数、两态见证风险60/49及全部有理比较通过。程序与机器证据另存同目录；程序核验证书中的数值代数，**无限连续量词的证明是上述几何引理而非有限抽样**。上游 PREFIX-321 全域证书沿用其已发表作者侧数学强度，尚无独立 Driver 接纳。

固定 GLOBAL_KNOWLEDGE_V1 main@c5547c717135d4d54d93d79fd47daecf9a9fb138；Enterprise Math main@338de014797c76ff16a12d0509b8e41f1f30b628。2026-10-28 真实 GitHub 登录 awdawmip；原生 status 返回 research_authority_granted=false，owner 只读查询 CONTROL_QUOTA；本轮为未登记作者侧科研，非正式CLAIM/Result/Review。下一单元 PREFIX-325：研究三种及以上相同准确 Q0 的新来源形状、异尺度来源和单形状纤维，或全辅助模型恢复统一上界；对原生转移保真另行立证。
