# T6 p17 加入精确矩后的七个锐界

2026-11-27 · 知情作者证明与复算 · 待项目独立评审

p17 的 \(q=0\) 载体有分母 \(17j\)、\(1\le j\le16\)，权 \(w_j=17j-1\)。对有符号整数向量 \(u\)，定义正负质量 \(P(u)=\sum_j w_j(u_j)_+\)、\(N(u)=P(-u)\)，及精确矩 \(M_k(u)=\sum_j u_j/(17j)^k\)。原 T6 的 \(H_0,\ldots,H_6\) 与 \(M_0,\ldots,M_6\) 经二项式三角变换等价。固定格外项时，逐个补入这些精确矩，每次都严格提高仿射补全首次可能碰撞的预算。

| 在六同余外固定的精确矩 | 差格秩 | 首个可碰撞总预算 | 首个可碰撞对称每侧预算 | 增广椭球格点数 |
| --- | ---: | ---: | ---: | ---: |
| 无 | 16 | 9,152 | 4,576 | 616,483 |
| \(M_0\) | 15 | 13,055 | 6,528 | 266,009 |
| 至 \(M_1\) | 14 | 35,121 | 17,561 | 33,355 |
| 至 \(M_2\) | 13 | 120,168 | 60,084 | 1,411 |
| 至 \(M_3\) | 12 | 740,792 | 370,396 | 11,353 |
| 至 \(M_4\) | 11 | 2,579,053 | 1,289,527 | 905 |
| 至 \(M_5\) | 10 | 9,499,607 | 4,749,804 | 691 |
| 至 \(M_6\) | 9 | 12,056,149 | 6,028,075 | 7 |

每行恰有一对互为相反数的最短非零差。此前总预算 9,152 的具名两解，\(M_0\) 分别为 13 和 0，差的第一矩为 \(122197/144144\)。固定格外项时，\(H_0=M_0\) 已排除这对两解及首界的全部碰撞。 [六同余基线](https://github.com/awdawmip/enterprise-math/blob/e2d854c14040c40e779d6f4370434f01f9cf4fe0/research_notes/portable_direct/2026-11-27_t6_p17_sharp_affine_uniqueness/REPORT.md) · [原矩定义与 p17 格](https://github.com/awdawmip/enterprise-math/blob/996ddf75043e981b87ff8b34ca9f6d4e456dbc3b/research_artifacts/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260920_01A079FC/PROOF.md)

## 差格、完整枚举及达界

设 \(L\subset\mathbb Z^{16}\) 为原六同余的全核，\(L_s=L\cap\bigcap_{k=0}^s\ker M_k\)，并记 \(\gamma_s=\min_{0\ne v\in L_s}\max(P(v),N(v))\)。若两解都满足正负预算 \(A,B\)，其非零差在 \(L_s\) 内，且 \(P,N\le A+B\)。反之，达界向量的正负部分提供同一新右端的两解，可取 \(A=\gamma_s,B=0\)。对称预算另用有界子集和逐行构造达界拆分。

取 \(J=\operatorname{lcm}(1,\ldots,16)\)。第 \(k\) 条精确矩可清分母为整数行 \(((J/j)^k)_j\)。若当前两基行在该泛函上取值 \(a,b\)，取 \(sa+tb=g=\gcd(a,b)\)，用整数行列式为 1 的矩阵 \(\left(\begin{smallmatrix}s&t\\-b/g&a/g\end{smallmatrix}\right)\) 更新该对。归并后删去唯一非零的枢轴行，得到精确整数核。复算检查秩、原同余、各个矩及 LLL 变换的整数幺模性。

令 \(z_j=w_jv_j\)。若 \(\max(P,N)\le T\)，则 \(z\in T(\Delta-\Delta)\)。差体顶点在 \(Q(z)=\sum z_j^2+(\sum z_j)^2\) 上至多取 2，所以 \(Q(z)\le2T^2\)。对每行所报的 \(T\) 用清分母的精确三角递推完成枚举，并检查有符号质量。另用不增广的欧氏二次型重算七行，最短向量与质量一致。

七矩的极小向量有直接表达式。令 \(S=\{2,3,4,5,6,8,9,10,12\}\)，取
\[
 v_j=\frac{420(11-j)j^6}{\prod_{i\in S,\ i\ne j}(j-i)}\quad(j\in S),\qquad v_j=0\quad(j\notin S).
\]
这是整数向量，正负质量为 \((12{,}049{,}009,12{,}056{,}149)\)。在 Lagrange 插值中取次数 8 的系数可知，\(\sum_{j\in S}P(j)/\prod_{i\ne j}(j-i)=0\) 对 \(\deg P<8\) 成立。应用于 \(P(j)=(11-j)j^{6-k}\) 即得七矩为零。\(M_7(v)=77/42543913616640\) 区分了该对形状。

## 允许素于 17 的格外项变化

设两个完整的有符号候选具有相同七矩，除本 \(q=0\) 载体外，所有分母能被 17 整除的原子在两候选中相同。其余分母 \(a\ge2,\ 17\nmid a\) 的原子可以任意变化。先扣除固定项所占正负质量。**当剩余正负总预算 \(A+B\le9{,}600\) 时，两候选的 \(q=0\) 部分必相同。**

记 \(q=0\) 差为 \(u\)，其余差为 \(h\)。将精确第 \(k\) 矩乘 \(17^k\) 再模 \(17^k\)，由于 \(h\) 的分母为单位，有 \(u\in L\)。枚举至 9,600 只留下质量为 9,152 和 9,569 的两对非零差。择一个定向，有 \(\sum_a h_a/a^k=b_k=-M_k(u)\)。在总差的每侧质量上界 \(T\) 下，格外正负质量分别至多 \(A'=T-P(u)\) 和 \(B'=T-N(u)\)。

对固定多项式 \(F\)，令 \(U_+\) 为可付正原子的 \(F(2/a)/(a-1)\) 与 0 的最大值，\(U_-\) 同理以 \(-F(2/a)/(a-1)\) 定义。每枚有符号原子的罚值 \((a-1)U_\pm\mp F(2/a)\) 非负，总罚值至多 \(A'U_++B'U_--\sum_k F_k2^kb_k\)。固定证书的二次多项式使 9,569 差的右式为负。六次多项式使 9,152 差只余少量罚值额度。

\(b_6\) 分母的素数幂迫使格外原子集合至少覆盖分母倍数 \(16,9,5,7\)。对 \(q=11,13\)，或者有 \(q^2\mid a\) 的原子，或者将第六矩乘 \(q^6\) 后模 \(q^2\)，得到格外原子的模约束。用六位覆盖状态和两个模余数做带非负有理边权的最短路径穷举。每枚可付原子是一步，剪枝只使用罚值上界。对于总预算 9,600 无达标路径。9,601 时这项放宽已出现达标路径，能否补齐全部七矩仍待证。

## 复算与接续

从[上一轮复算包](https://github.com/awdawmip/enterprise-math/blob/e2d854c14040c40e779d6f4370434f01f9cf4fe0/research_notes/portable_direct/2026-11-27_t6_p17_sharp_affine_uniqueness/reproduction.json)的 <code>files</code> 提取 <code>exact.py</code> 和 <code>balanced-replay.json</code>，从[原证书](https://github.com/awdawmip/enterprise-math/blob/996ddf75043e981b87ff8b34ca9f6d4e456dbc3b/research_artifacts/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260920_01A079FC/p17_q0_certificate.json)保存 <code>basis.json</code>。同目录运行下列命令，对照 <code>results.json</code> 和 <code>euclidean.json</code>。版本为 Python 3.12、SymPy 1.14.0、python-flint 0.9.0。证书校验全用整数或有理数。

~~~sh
python replay.py basis.json balanced-replay.json
python replay.py basis.json balanced-replay.json --metric euclidean --skip-tail
~~~

七个锐界适用于固定格外项。放开素于 17 的原子时，9,600 是已证唯一性下界。不同的 17 倍数配置、低素数层和全局 \(T_6\) 仍依各自证据。下一步可把多项式和素数幂罚值检验接到项目实际保留的 p17 非空模类上，测量它能缩去多少低素数补全搜索。
