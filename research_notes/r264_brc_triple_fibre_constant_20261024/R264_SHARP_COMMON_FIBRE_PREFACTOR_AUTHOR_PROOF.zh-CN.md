# R264 · BRC 三来源共同效果纤维：精确一阶极限常数

**2026-10-24 | 作者侧解析证明、精确整数核验；未审 / NOT_ADMITTED。** 本研究沿用 R260–R262 已固定的有限正权形式 BRC 仿射模型，不宣称 P000 原生六维 Cell 或真实心跳动力学结论。

**固定规范读取**：GLOBAL_KNOWLEDGE_V1 main@b24616f2e895a20f69635f805853ef3b157186aa，P000 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc；Enterprise Math 控制 main@238626c2bb75a51b843c3cb3e1af56c60a30e530。直接科学前驱：R262 作者证明 [不可变提交](https://github.com/awdawmip/enterprise-math/blob/be6b89f3b2b9a477f747d68919625dcd0d025a95/research_notes/r262_brc_antic_concentration_20261024/R262_BRC_FOURIER_ANTICONCENTRATION_AUTHOR_PROOF.zh-CN.md)。

## 精确定义与主定理

起点 (q,r,eps,k)=(0,0,+1,0)，q∈{0,1,2}。两个有序来源 a∈{0,1} 的 (q',eta,b) 表为

| q | a=0 | a=1 |
|---|---|---|
| 0 | (2,-1,-1) | (2,+1,-1) |
| 1 | (0,-1,-1) | (0,+1,-1) |
| 2 | (1,+1,+1) | (2,+1,-1) |

全部原始边权重严格为1。chronological BRC composition 为 eps'=eta*eps，k'=eta*k+b。来源 r=0：从未出现00且末位1；r=1：从未出现00且末位0；r=2：曾出现00。n_r(m;q,eps,k) 是相同末端 q、完整六槽仿射效果 (eps,k) 和 r 的长度 m **有序原始词整数数量**。令 M_m=max_(q,eps,k) min_(r=0,1,2) n_r(m;q,eps,k)。

设 phi=(1+sqrt(5))/2，sigma²=3/2+7sqrt(5)/10=phi^4/sqrt(5)。**定理：**

```text
lim_(m→∞) [ sqrt(m) * M_m / phi^m ]
    = 1 / [ 5*phi*sqrt(2*pi*sigma²) ]
    ≈ 0.028165641153285.
```

两条奇偶长度子序列的前导常数相同；这严格加强 R262 的 Theta(phi^m/sqrt(m))。

## 证明

**(1) 来源终态交集。** 无00的来源 r=0 末态只有 A=(q0,last1)、C=(q2,last1)；r=1 末态只有 B=(q2,last0)、D=(q1,last0)。三来源共同同一 q 时必有 q=2。因此最大值可只取 q=2；在此 r0=C_eps，r1=B_eps。

**(2) 八态精确生成函数。** 令 t=eps*k，则由原有 BRC 复合律严格得到 t'=t+eps'*b，故每个原始边增加 ±1，且 t≡m (mod2)。这一标记在固定 eps 下对 k 可逆，不丢失原始词或完整仿射效果。令 T8(z) 以目标为行、来源为列，对 A±,B±,C±,D± 的每条无00真实边赋 Laurent 单项式 z^(t'-t)。于是 [z^t](T8(z)^m)_(J,A+) 等于终态 J 的原始整数词数。

实际边为 A_e --0,+e--> B_-e；A_e --1,-e--> C_e；B_e --1,-e--> C_e；C_e --0,+e--> D_e；C_e --1,-e--> C_e；D_e --1,-e--> A_e。

R262 的形式恒等式（本轮 SymPy 严格重验）：

```text
det(xI-T8(z))=(x²+1)[x⁶-(z+z⁻¹)x⁵+2x²-1].
```

z=1 的 Perron 根 phi 简单，其右向量 R、左向量 L（态顺序 A+,A-,B+,B-,C+,C-,D+,D-）可精确取

```text
R=(1,1,1/phi,1/phi,phi²,phi²,phi,phi)^T
L=(1,1,1/phi,1/phi,1,1,1/phi,1/phi)
L*R=10.
```

逐行检查 T8(1)R=phi*R、LT8(1)=phi*L。所以主谱投影 P=RL/10：

```text
P_(B_eps,A+) = 1/(10phi);    P_(C_eps,A+) = phi²/10.
```

八态图不可约且有自环；两个 C_± 自环标记分别为 -1,+1。单位圆上，谱半径可达到 phi 的点恰为 z=±1（Perron 三角等号条件加两自环强制 z²=1）。因每条增量为奇数，T8(-z)=-T8(z)。在 z=e^(iθ) 的 z=1 邻域，由特征多项式隐微分：

```text
Lambda8(θ)=phi[1-sigma²*θ²/2+O(θ⁴)].
```

谱投影对 θ 解析，其他弧有统一谱隙。对 t_m=m mod2∈{0,1}，用 Laurent 系数积分、u=√m θ 和高斯主项，z=±1 两峰因 (-1)^(m-t_m)=+1 正向相加，得到

```text
n1(m;2,eps,eps*t_m)
    = phi^m / sqrt(m) * [1/(5phi sqrt(2pi sigma²))+o(1)],
n0(m;2,eps,eps*t_m)
    = phi^m / sqrt(m) * [phi²/(5 sqrt(2pi sigma²))+o(1)].
```

故在**同一完整效果纤维**中 n0/n1→phi³>1。

**(3) 全整数效果上的锐上界。** 对所有 eps,t 而非只在中心 t_m，应用 Laurent 积分三角不等式：

```text
0 ≤ [z^t](T8(z)^m)_(B_eps,A+)
  ≤ (1/2pi) ∫ |(T8(e^(iθ))^m)_(B_eps,A+)| dθ.
```

两个峰的正投影元均为 1/(10phi)，高斯尺度相同，其余弧指数衰减。因此 uniformly in eps,t:

```text
sup_(eps,t) n1(m;2,eps,eps*t)
 ≤ phi^m/sqrt(m) * [1/(5phi sqrt(2pi sigma²))+o(1)].
```

从 min≤n1 立即得 M_m 的同一锐上界。

**(4) 不可省略的 r=2 同效果保证。** 模式2全局总数较大不能自动证明它在目标 (q2,eps,k) 上也较大。为此另构造所有二元原始词的六态正权 Laurent 传输 T6(z)，态序 (q0,+),(q0,-),(q1,+),(q1,-),(q2,+),(q2,-)，采用完全相同的 BRC 更新。逐项展开的精确特征多项式为

```text
det(xI-T6(z)) = x²[x-(z+z⁻¹)][x³+x-(z+z⁻¹)].
```

z=1 的简单主根为2，次谱模小于2；Perron 右向量（和为1）为 (1/8,1/8,1/8,1/8,1/4,1/4)，左向量为全1。因此主投影 (q2,eps)←(q0,+) 精确等于1/4。六态图同样不可约且有两个异号增量的自环，最大谱模仅在 z=±1；主根在 z=e^(iθ) 邻域**恰等于** 2cosθ=2(1-θ²/2+O(θ⁴))。同样的双峰整数局部极限给出在上述**同一个** t_m、eps、k=eps*t_m：

```text
n0+n1+n2 = 2^m / sqrt(m) * [1/(2sqrt(2pi))+o(1)].
```

另一方面 n0+n1=O(phi^m/sqrt(m))。由于 2>phi，n2~2^m/(2sqrt(2pi m))，且 n2/n1→∞。故最终该中心效果纤维满足 n0>n1、n2>n1；M_m≥n1 的中心下界与 (3) 全局上界夹逼，主定理成立。**证毕。**

注意：θ、cos、pi 和高斯函数仅用于形式正整数路径计数的*事后解析系数读出*，不输入 P000 物理更新、残差归因或实际 BRC 心跳数值模拟。

## 验证、边界与接续

独立本地 SymPy 整式校验两套特征多项式、左右 Perron 特征向量、归一化及 sigma² 精确式；穷举长度0..13全部16383条原始二元词，与精确整数 DP 状态逐项核验；DP 到长度200。长度128和140的 M_m 重算分别是 `1426814983819745518311507` 与 `438611399828372525268845634`，符合 R261/R262 作者前沿。有限试验不是无穷极限的证明；本稿无限结论承担的是可审的谱论推导。

尚未执行原版 `enterprise_math` 包、R193 原生来源/查询/时间端口；未证明形式六槽 BRC 到 P000 六维 Cell 的保真映射。原生会话 `em_session_start` 返回 `STATIC_READONLY_SCOPE_DENIED`，控制盘查询 `CONTROL_QUOTA`；因此未核实活跃 owner、无正式 CLAIM / Source Result、未经独立 Driver 审查。

**下一严格问题**：计算主根及谱投影的四阶/二阶展开，确定全局整数最优效果的第一项 O(1/m) 相对修正与整数格点偏移是否存在更细的奇偶结构；另独立推进 R193 原生接口保真。R263 其他研究线的七状态共纤维结果不计作本轮新发现。
