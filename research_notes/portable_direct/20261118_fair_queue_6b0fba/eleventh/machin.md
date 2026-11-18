# 固定支撑 Gregory–Machin 对角端点的最优渐近成本

固定整数 $s\ge2$。取恰好 $s$ 个互异本原原子 $z_j=[b_j+i a_j]$，其中 $0<a_j<b_j$。要求非零整数系数满足 $\prod_j z_j^{c_j}=\tau=[1+i]$，等式在 $\mathbf Q(i)^\times/\mathbf Q_{>0}^\times$ 内理解。使用冻结任务的两个资源
$$
 B_{\log}=\sum_j\log_2 b_j,\qquad
 \mu=\sum_j\frac{\ln10}{\ln(b_j/a_j)}.
$$
令 $m_s(B)$ 是所有 $B_{\log}\le B$ 的可行式中最小的 $\mu$，空集取 $+\infty$。有限预算内原子集有限。

**定理。** 对每个固定的 $s\ge2$，
$$
 \boxed{\displaystyle \lim_{B\to\infty}m_s(B)\ln B=\frac{\ln10}{s-1}.}\tag{1}
$$
若只允许零整圈、全正系数的公式，极限仍然相同。以分母的实际二进制位长总和代替 $B_{\log}$ 也给出同一极限，两种预算相差至多 $s$。特别地，固定支撑的任何精确对角公式序列若 $B_{\log}\to\infty$，则 $\mu B_{\log}\to\infty$。原下界 $s^2\log_2 10$ 在此域渐近不可达。这个极限定理描述整条预算包络。

[冻结任务书](https://github.com/awdawmip/enterprise-math/blob/c0f816e2ab6be0145a3edd1a77488bddfd42a2f6/research_tasks/RS-R1160C-GREGORY-MACHIN-RESOURCE-TRADEOFF.md) · [原双资源下界](https://github.com/awdawmip/enterprise-math/blob/93df1f4261265f910e48365ddca559a1ca202f2f/research_notes/GREGORY_MACHIN_GENERALIZED_BIT_PARETO_BOUND_20260904.md) · [端点体系与前沿](https://github.com/awdawmip/enterprise-math/blob/c0f816e2ab6be0145a3edd1a77488bddfd42a2f6/research_handoffs/GREGORY_MACHIN_1160_DURABLE_HANDOFF_20260909.md)

## 一、从模八端点提取短的奇数扭转关系

写端点签名为 $(\epsilon_j,v_j)$，其中 $\epsilon_j\in\mathbf Z/8$，列向量 $v_j$ 为有向高斯分裂素赋值。$\tau$ 的签名为 $(1,0)$。令 $V=(v_j)$、$r=\operatorname{rank}_{\mathbf Q}V$。严格正斜率的原子不可能是八阶扭转元素，故 $r\ge1$；可行公式给出 $Vc=0$，故 $r\le s-1$。每个本原原子满足
$$
 \|v_j\|_1\le \frac{\ln(a_j^2+b_j^2)}{\ln5}
       <\frac{(1+2B)\ln2}{\ln5}=:H_B .
$$
这是因为每个非零自由坐标对范数贡献至少一个 5，素数幂按绝对赋值计数。基础取自已有高斯赋值分解。[赋值与范数预算](https://github.com/awdawmip/enterprise-math/blob/c0f816e2ab6be0145a3edd1a77488bddfd42a2f6/research_notes/GREGORY_MACHIN_WEIGHTED_PLUCKER_BUDGET_20260904.md)

任选 $V$ 的 $r$ 个独立行。将这 $r$ 行的所有 $r$ 阶列子式除以其正的共同最大公因数，所得有符号整数记为 $P_J$；令 $\Delta=\max_J|P_J|$。至少有一项 $P_I$ 为奇数。对每个 $j\notin I$，克拉默法则给出整核向量 $u^{(j)}$，其 $j$ 分量取 $P_I$，在 $I$ 上取有符号的换列子式 $P_{I-i+j}$，其余位置为零。于是 $\|u^{(j)}\|_\infty\le\Delta$，每个至多有 $r+1$ 个非零分量。对任一整数核向量 $c$ 有精确恒等式
$$
 P_I c=\sum_{j\notin I}c_j u^{(j)}. \tag{2}
$$
两边具有相同的非主列分量，其差支撑于独立列 $I$，又在核内，所以差为零。把 (2) 与 $\epsilon$ 模 2 配对，因 $P_I$ 和 $\epsilon\cdot c$ 均为奇数，至少一个 $u^{(j)}$ 的扭转坐标也是奇数。此处允许原公式有冗余支撑，或所有原始子式均为偶数。选取独立行后，消去这些行等价于消去全部自由坐标。

将高斯类送至复单位圆 $z\mapsto z/|z|$，这是正比例商上的群同态。任一奇次 $\tau$ 到单位元的弦长至少为 $\eta=\sqrt{2-\sqrt2}>1/2$。若单原子斜率为 $t=a/b$，其弦长平方为 $2(1-1/\sqrt{1+t^2})\le t^2$。乘积弦长至多为各因子弦长之和，负指数与其绝对值具有同一上界。将它用于刚提取的奇关系，得到可直接剪枝的不等式
$$
 \eta\ \le\ \sum_i |u_i^{(j)}|\,a_i/b_i
 \ \le\ (r+1)\Delta\max_i(a_i/b_i). \tag{3}
$$
按 Hadamard 不等式，$\Delta\le(\max_i\|v_i\|_1)^r\le H_B^r$。从而对每个可行公式
$$
 \mu\ \ge\ \frac{\ln 10}{\ln(2s)+(s-1)\ln H_B}. \tag{4}
$$
的确，取最大斜率对应的原子，(3) 给出其倒数至多 $2sH_B^{s-1}$，仅计这一项的成本即可。固定 $s$ 时 $\ln H_B=\ln B+O(1)$，故得 (1) 的下极限。有限搜索可直接使用有理判据 $2(r+1)\Delta\max_i(a_i/b_i)\le1$ 排除整个原子组。若实际已知某个奇关系，(3) 的逐项形式保留了更多信息。

## 二、逐层取有理近根，得到精确的上界

令 $k=2^n$，网格分母 $G=2^{n^2}$。从辅助方向 $U_0=\tau$ 开始。设 $\theta_{j-1}=\arg U_{j-1}$，在第 $j=1,\ldots,s-1$ 层取
$$
 h_j=\left\lfloor G\tan(\theta_{j-1}/k)\right\rfloor,\qquad
 U_j=[G+(h_j-4^j)i],\qquad R_j=U_{j-1}U_j^{-k}. \tag{5}
$$
角记号便于估计。构造 $h_j$ 用整数即可：在 $0\le h\le G/k$ 中二分，取使 $\det((G+hi)^k,U_{j-1})\ge0$ 的最大整数。区间内幂的辐角最多 $k\arctan(1/k)<1$ 弧度，且当 $k>1$ 时 $k\arctan(1/k)>\arg(1+i)$，故单调判断落在同一象限。$U_j,R_j$ 均以最大公因数约去正比例。$R_j$ 的整数代表可通过 $U_{j-1}\overline{U_j}^{\,k}$ 直接得到。

对固定 $s$ 及充分大的 $n$，所有 $h_j-4^j$ 均正。为验证这一点，归纳设 $\theta_{j-1}=\theta_0/k^{j-1}+O_s(1/G)$。则 $h_j$ 的量级为 $G/k^j$，超过 $4^j$。设 $\theta_j=\arg U_j$，$\delta_j=\arg R_j=\theta_{j-1}-k\theta_j$。由斜率 $[0,1]$ 上 $\arctan$ 的导数位于 $[1/2,1]$，
$$
 \frac{4^j k}{2G}\ \le\ \delta_j\ \le\ \frac{(4^j+1)k}{G},
 \qquad
 \theta_j=\frac{\theta_{j-1}}{k}+O_s(1/G)
         =\frac{\theta_0}{k^j}+O_s(1/G). \tag{6}
$$
这些微小余角的区间彼此不交。又有 $\theta_{s-1}\asymp_s k^{-(s-1)}\gg_s k/G$，故最终使用的 $s$ 个原子互异，且全是严格正斜率。本原化不改变斜率或区间。

核心的高斯端点恒等式是
$$
 \boxed{\tau=
 R_1 R_2^{\,k}\cdots R_{s-1}^{\,k^{s-2}}\,
 U_{s-1}^{\,k^{s-1}}.} \tag{7}
$$
它是逐层 $R_jU_j^k=U_{j-1}$ 的消去式，因而所有自由估值严格相消、模八扭转为 1。将 (6) 中的角度恒等式逐层代入，正角的带权总和恰为 $\theta_0$，整圈数为零。

每个余角原子的 $\ln(b/a)=\ln(G/k)+O_s(1)$，其完成成本为 $O_s(n^{-2})$。末项 $\ln(b/a)=(s-1)\ln k+O_s(1)$。另一方面，$|U_j|\le\sqrt2G$ 可对所取整代表成立；每个 $R_j$ 在约分后的分母不超过 $(\sqrt2G)^{k+1}$。故存在只依赖于 $s$ 的常数 $A_s$ 使
$$
 B_{\log}\le A_s\,2^n n^2,\qquad
 \mu=\frac{\ln10}{(s-1)\ln k}+O_s(n^{-2}). \tag{8}
$$
给任意充分大的预算 $B$，取满足 $A_s2^n n^2\le B$ 的最大 $n$。由于相邻预算上界之比趋于 2，$\ln B=n\ln2+O_s(\ln n)$。这给出 (1) 的上极限。以上是预算内可行族的构造，未假定每个预算值都恰是一组原子分母的对数高度。

## 三、系数、整圈和变化的支撑

对给定的任意精确目标系数 $c$，同样的弦长估计给出 $\sum|c_j|a_j/b_j\ge\eta$。每项对 $\mu$ 的贡献至多为 $\mu$，故 $a_j/b_j\le10^{-1/\mu}$。因此
$$
 \max_j|c_j|\ \ge\ \frac{\eta}{s}\,10^{1/\mu}.
$$
系数的最大二进制位长因而至少为 $\log_2(10)/\mu-O_s(1)$。在 (7) 中最大系数恰为 $k^{s-1}$，结合 (8) 达到这一位长界的首项，且整圈为零。反过来，将该族的全部系数乘以 $1+8t$，任意整数 $t\ge0$ 都保持相同的 $s,\mu,B_{\log}$ 和相同目标，整圈数成为 $t$。这分别给出了必需的系数规模和固定两项资源时可追加的系数、绕行成本。

达到锐常数的任一序列还必须最终满足 $r=s-1$。若 $s\ge3$ 且反复出现 $r\le s-2$，在 (3) 中保留实际的秩，便在该子列得到下极限至少 $\ln10/(s-2)$；$s=2$ 时 $r=0$ 已排除。在秩 $s-1$ 的情形，整核由互素子式组成的单个本原向量 $u$ 生成。它的扭转坐标必奇，乘以绝对值至多 3 的整数即可得到精确目标。由子式界 $\|u\|_\infty\le H_B^{s-1}$ 以及前述弦长下界，最短可行系数的最大二进制位长必为 $(s-1+o(1))\log_2 B$。该推论适用于全部达到 (1) 首项的公式序列。

固定 $s$ 是取极限 (1) 的条件。若支撑随预算增长，原 Cauchy 界与 (4) 仍可联用。取实际高度 $B=B_{\log}$，用 $\ln(2s)\le s\ln2$，得到对所有 $s\ge2$ 的统一下界
$$
 \mu B\ \ge\
 \max\left(s^2\log_2 10,\frac{B\ln10}{s\ln(2H_B)}\right)
 \ \ge\ (\log_2 10)^{1/3}
         \left(\frac{B\ln10}{\ln(2H_B)}\right)^{2/3}.
$$
因此即便改变支撑，$\mu B$ 也随高度无界增长。支撑随 $B$ 增长时最佳 $\mu$ 的数量级和首项常数仍待确定。

## 四、既有两族与复算

- 首越族的精确关系为 $[q+i]^{k(q)}R_q^{-1}=\tau$，其中 $k(q)=\Theta(q)$ 且 $0<\operatorname{slope}(R_q)<1/q$。已知残余原子的比较下界与未约分幂的直接上界合给 $B_{\log}=\Theta(q\ln q)$。因此其 $\mu\ln B_{\log}$ 的下、上极限均落在 $[\ln10,2\ln10]$。式 (7) 在 $s=2$ 将最优常数确定在左端。[首越族](https://github.com/awdawmip/enterprise-math/blob/b0b99008beead9a22a6857bea9c3316cca0f00fe/research_notes/GREGORY_MACHIN_UNRESTRICTED_RATIONAL_ALPHABET_NO_GO_20260904.md)
- Pell 互补族以 $(b+ai)((b+a)+(b-a)i)=(a^2+b^2)(1+i)$ 给出正系数 $(1,1)$。两原子斜率都趋于 $\sqrt2-1$，故 $\mu\to2/\log_{10}(1+\sqrt2)>0$，同时 $B_{\log}\to\infty$。于是这一族的归一化成本 $\mu\ln B_{\log}$ 发散。[Pell 校准](https://github.com/awdawmip/enterprise-math/blob/4f08d1afb0a6b90ce7bb80593721584cf9b9190e/research_notes/GREGORY_MACHIN_RATIONAL_COMPLEMENT_PELL_CHAIN_20260904.md)
- $H=1000$ 的七点双支撑前沿采用分母位长总和。其最小 $\mu$ 点 $[79+3i]^7[278+29i]^5=\tau$ 由附带程序直接复乘。该小预算前沿及 21 位的三原子改善描述有限区间；式 (1) 描述每种固定支撑的大预算端点包络。[已有七点前沿](https://github.com/awdawmip/enterprise-math/blob/79e3349ccbb16ebd3bf7d40cb3e88bb994ea2b90/research_notes/GREGORY_MACHIN_RATIONAL_SUPPORT2_H1000_PARETO_20260904.md)

用标准库运行 <code>python machin_check.py &gt; reproduced.json</code>。程序对 $s=2,3,4,5$ 的十组参数，以整数行列式选网格点，逐层重建和验证精确端点；两组小例额外完整展开了末端乘积。例取 $s=3,n=10$，三原子的 $\lfloor\log_2(b/a)\rfloor$ 分别为 87、85、20，分母位长为 102401、102501、101，最大系数为 $2^{20}$。另核验五组首越、十四组 Pell、一个原始子式全偶的非极小秩二样例。JSON 中的归一化成本区间来自整数移位和有理界，极限常数由证明确定。高斯整数乘法和正比例约分决定端点，实对数与角度只用于资源分析。
