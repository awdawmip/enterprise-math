# R267 | 有限效果视野内的精确零点解码：最小表示维数

2026-10-25 | AUTHOR_SIDE_ANALYTIC_PROOF / EXACT_FINITE_CHECKS / DRIVER_UNREVIEWED / NOT_ADMITTED

研究固定来源：
GLOBAL_KNOWLEDGE_V1 main@ba426098a3731ac30822784c7f670f2a40416493；
Enterprise Math main@5e8c16777987ab8da4afbbc90450a56f6e145945；
R266 author proof@5ab2fcd0a980c728560b2a10b3657f0413ba1dd1。

## 1. 模型、量词与 BRC 范围

形式仿射效果群 G={(epsilon,k):epsilon=±1,k∈Z}，有序复合律为
(epsilon,k) THEN (eta,b)=(eta epsilon,eta k+b)。
令 rho:G→GL_r(Q) 满足反表示等式 rho(g THEN h)=rho(h)rho(g)。
固定行向量 ell 与列向量 v，末端效果系数读出 f(g)=ell rho(g)v。

给定任意 H≥0，规定**整个效果窗口** W_H={(epsilon,k):epsilon=±1,|k|≤H}；与某个固定来源自动机仅有的可达效果集合严格区分。两个任务：

T0: f(epsilon,k)=1 当且仅当 k=0（不区分 epsilon）。
G0: f(epsilon,k)=1 当且仅当 (epsilon,k)=(+1,0)。

精确数学问题：在上述全部输入上，使用一个固定有理群反表示与一个矩阵系数，最少需要多大 r？正权 BRC 分支的正整数重数与群表示算子是不同载体；这里的表示矩阵不宣称原始物理状态的坐标。

## 2. 定理 A：r_T0(H)=H+1

下界：设 A=rho(+1,1)，它可逆并满足 rho(+1,k)=A^k。建立矩阵

  T_ij=f(+1,i-j),  0≤i,j≤H。

因为 |i-j|≤H，T 是 H+1 阶单位矩阵，rank(T)=H+1。
反表示律给出

  T_ij = ell A^(-j) A^i v。

因此 T 可分解为 (H+1)×r 与 r×(H+1) 矩阵之积，故 r≥H+1。
这是真正全部 H 的严格矩阵秩证明，不是有限数值观察。

上界：取 N=H+1 与 V=Q[Z/NZ]，基为 e_x。定义

  rho_N(epsilon,k)e_x=e_(epsilon*x+k mod N)。

此为有理置换反表示，因为先 g 后 h 正对应两次仿射映射的复合顺序。令 v=e_0、ell=e_0^T，得到

  f(epsilon,k)=1_{k≡0 (mod N)}。

|k|≤N-1 内，模 N 等于零当且仅当 k=0；r=N 达到下界。证毕。

## 3. 定理 B：r_G0(H)=2(H+1)

下界：设 N=H+1，取 2N 个不同效果组成 S={(epsilon,i):epsilon=±1,0≤i≤H}。
对 g=(epsilon,i)、h=(eta,j)，h^{-1}=(eta,-eta*j)，故

  g THEN h^{-1}=(eta*epsilon,eta*(i-j)), 且 |eta*(i-j)|≤H。

于是 B_(g,h)=f(g THEN h^{-1}) 是以 S 标记的 2N 阶单位矩阵。
但是 B_(g,h)=ell rho(h^{-1})rho(g)v，故 rank(B)≤r，必有 r≥2N。

上界：构造大小为 2N 的有限群 Gbar_N={(epsilon,k mod N)}，
使用上述半直积 THEN 律。令 V=Q[Gbar_N]，e_x 为群元素基，
rho_N(g)e_x=e_(x THEN gbar)，v=e_identity，ell=e_identity^T。
这是反表示且

  f(epsilon,k)=1_{epsilon=+1, k≡0 (mod N)}。

在 W_H 上精确等于 G0，r=2N 达到下界。
N=1 和 N=2 的抽象有限群也成立，无需依赖反射置换在残基集合上忠实。证毕。

## 4. BRC 资源边界与不应推广之处

当每条局部仿射边的平移增量绝对值≤1时，由复合律的三角界，长度≤H 的路径必有 |k|≤H。因此上述构造在该有限视野内是严格可用的零点效果读出；矩阵是0-1置换矩阵，路径正权并未转成有符号抵消。

若要在所有整数 k 上精确检查 k=0 或完整单位效果，任何单个固定有限 r 都不可能满足：定理 A/B 分别给出每个 H 上的无界线性下界。此结果定量细化 R266 的固定维数系数解码与任意非线性效果解码之间的边界。

重要：以上最小维数对**整个 W_H 接口**成立，不能自动转换成 R260 某个具体来源图的六控制态下界。特别是：
(a) 来源图可能只到达较小效果集合；
(b) 全部 H_m 的非选择完整直方图比单个解码函数包含更多数据；
(c) 允许任意非线性 D(control,m,epsilon,k) 与允许固定表示系数解码是不同模型；
(d) 聚合自动机的边、控制态与来源多重性须另行定义和验证。

因此本轮既没有构造 R260 的六控制态任意聚合实现，也没有证明这类实现不存在。没有验证 R193 真正来源/查询/时间端口；形式步数并非 P000 物理心跳时间。P000 六维 Cell 与联合关系保真要求不变。

## 5. 精确复核与接续

R267_verify_finite_window_decoder.py 使用纯 Python 整数检验 H=0..12：
全部 W_H 效果读出、两种单位矩阵证书的全部条目，并在 N≤7 时
穷举所有有限群元素对验证反表示合成律。机器证据见 EXACT_EVIDENCE.json。
通用结论来自上方解析证明；有限检查只核验代码实现/样例。

下一问题：固定 R260 的可比类——是否允许多重边、是否逐边保留真实仿射效果、
终点是否允许任意 D(control,m,epsilon,k)、是否要求逐来源词保真或仅非选择包 H_m 保真。
然后寻找真正 6 状态正权聚合构造或非商型障碍。独立的 R193 原生保真映射仍待解决。

原生会话/Owner 状态：本轮 em_control_tasks 为 CONTROL_QUOTA；
em_session_start 为 STATIC_READONLY_SCOPE_DENIED（operation_sent=false）。
无法核实活跃 Owner，也未取得原生 Researcher 会话、CLAIM、独立 Driver 审查
或正式 Result 接纳。本文件只是作者侧数学材料和持久化研究前沿。
