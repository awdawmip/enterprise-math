# R331｜BRC Newton 差分 257 条无界余阶带：精确正 Newton 插值证书

数学状态：作者侧计算辅助代数证明；独立 Driver 审查、原生 CLAIM/Result 与正式数学接纳均未取得。本结果只关于正权有序六边 BRC 辅助组合模型，不是 P000 原生 X6 动力学、三维切片或物理模型的结论。

## 来源与权威

本轮固定账户级 GLOBAL_KNOWLEDGE_V1 main@1115410aa5e5d94c4b5ff10c5df77379ca1f5825；P000 canonical blob 为 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc，ACTIVE 世界观不修改。数学来源 R330 commit 7c73f56263c3f0515aa28e55ced2d4c703b8e086，继承原始 12 项带符号域外尾项的 K/J 递推以及严格的有理母函数抽取恒等式 (3),(4)；另参 R327 commit 8332494a0aea16df27beb9828edfb41b3f234e09。开始时 Enterprise Math 主干 main@f3b1cff2be50a4c77576894d71562eb7fd78068f。

## 定义及主定理

由 R330 的原始多项式递推定义 B_s(t)，绝不提前截去三角域外的有符号尾项。设

\[
N_{q,v}=2^{q-v}[t^q]B_{q+v}(t),\qquad D_{q,k}=\left.\Delta_v^k N_{q,v}\right|_{v=0}\quad(0\le k\le q).
\]

令 r=q-k、u=k，即 q=r+u。继承 R330 的精确生成函数公式，可定义有理多项式 H_r(u)，次数不超过 r，满足 D_{r+u,u}=5^uH_r(u)。

**主定理：对全部整数 0≤r≤256 和 u≥0，有**

\[
\boxed{D_{r+u,u}=5^u\sum_{i=0}^{r}c_{r,i}\binom ui>0,\qquad
c_{r,i}=\Delta^iH_r(0)>0.}
\]

进一步任意 0≤j≤r，u≥0 都有 \(\Delta^jH_r(u)>0\)；并有
\[
D_{r+u,u}\ge 5^uD_{r,0}>0.
\]
r≥1 时仅 u=0 等号成立；r=0 时 H_0=1，对所有 u 等号成立。由 r=0,…,17 原已证明，加上 r=18,…,256 新增239条，得到 **257 条无界整数余阶带** 的精确正性证书，等价于 q≥k≥0 且 q−k≤256 处的 D_{q,k}>0。

## 精确的有限到无界证明

由 R330 精确的原始 K/J 有理母函数代数，存在 deg_z(g_j)≤2j 的有理系数多项式 g_j(z)=∑_m g_{j,m}z^m，满足

\[
H_r(q-r)=\sum_{j=0}^{r}\sum_m g_{j,m}5^{r-m}4^m
\binom{q-m+j}{j}\binom{2q-j}{r-j},\quad q\ge r.\tag{★}
\]

各项是 q 的有理多项式，次数至多 j+(r−j)=r。对 m≤2j 和 q≥r≥j，所需的组合数抽取与下降阶乘多项式在非负整数域一致。因此先验地 deg H_r≤r；这项约束 **不是** 由数值插值猜测得到，而是依赖 R330 已声明的作者侧公式 (★)。

对于每个 0≤r≤256、0≤v≤r，R331_VERIFY.py 独立用全部原始 signed-tail 12 项整数递推计算：

\[
H_r(v)=5^{-v}\sum_{a=0}^{v}(-1)^{v-a}\binom va
\,2^{r+v-a}[t^{r+v}]B_{r+v+a}.\tag{†}
\]

由于 deg H_r≤r，Newton 插值恒等式作为多项式恒等式给出
\[
H_r(u)=\sum_{i=0}^{r}(\Delta^iH_r)(0)\binom ui\qquad\text{对所有 }u.
\]

从 (†) 的 r+1 个精确值出发，对全部 r=0,…,256 形成逐阶前向差分，实际精确检验 33153 个系数 c_{r,i} 全部严格为正；另外 c_{r,r}=6^r 对全部257条逐项成立，与公式 (★) 的最高项 6^r/r! 一致。对任意 u≥0，每个二项式 \(\binom ui\ge0\) 且 c_{r,0}>0，因此 H_r(u)>0。应用 \(\Delta\binom ui=\binom u{i-1}\) 再推出全部阶次的严格正性及下界。这是有效的有限计算辅助无界证明（在原 R330 母函数引理的作者侧正确性前提下），不是凭 s 的有限正样本外推。

## 实际执行证据及复现

实际命令：

    python R331_VERIFY.py --max-r 256 --out R331_EXACT_EVIDENCE.json

结果 PASS：原始 B_s 完整构造 s=0,…,768；三角域 296065 项逐项正，保留域外负系数 124191 项；全部 33153 个有理 Newton 系数严格正；257 个 c_{r,r}=6^r 一致。未使用浮点判断。

逐项 SHA256 输入严格定义为按 r 升序、i 升序依次追加 ASCII/UTF-8 字符串 {r},{i},{numerator}/{denominator} 和一个换行符。全量 33153 系数摘要：

81c190fa50e22dc8479cb337a374706ae300a877fc9c74aa7a9033c49d96cf09

哈希仅用于识别结果；完整原始有符号递推与所有系数通过项目保存的 Python 标准库源码再生。GitHub 证据 JSON 为精简可重算摘要；作者本轮另生成完整有理系数运行物料，不把摘要当成独立证明。

独立符号交叉：原 R330 SymPy 有理母函数计算延伸到 r=18；对 r=0,…,18 的 H_r 在每个 r+1 个整数位置，独立符号公式与原始整数递推/差分完全一致。新增 r=18 的全部19个普通幂系数严格正，边界为

\[
H_{18}(0)=398361925444173824,\quad
\Delta H_{18}(0)=9646617325339672576/5,\quad
\Delta^{18}H_{18}(0)=6^{18}=101559956668416.
\]

所以 D_{18+u,u}≥398361925444173824·5^u，对 u>0 严格大于。第二套符号交叉仅覆盖 r≤18，不声称对 r19..256 全部重做有理母函数展开。

## 边界及后继

R327 的 q≤640 无界整行差分正性继续有效；本轮新增 q−k≤256 的无界斜带。**差分阵列**剩余未覆盖区域包括 q≥641、0≤k≤q−257。本轮不能把部分 D 的正性不加条件提升为原始 Newton 三角域全部正性；R327 的 s≤1280 原域有限证书也保留其原强度。P000、ACTIVE 世界观、完整缺陷纤维正性与 N_peak=81 不变。

下一数学单元：对 r=257 构造全258项有理 Newton 差分证书，优先采用按需/流式原始递推以控制大整数耗时；如果 c_{257,i} 非正，必须独立判断只是充分的 Newton 正锥失效、确切 D 负项、还是原 B_s 规定域内反例。随后研究 r 与 q 同时增大的统一正锥规律。

当前 GitHub 身份 awdawmip，可写仓库；原生 em_status 版本0.6.11，但 em_control_tasks 返回 CONTROL_QUOTA，活跃 owner 不能权威核实。旧原生 session_start 的 STATIC_READONLY_SCOPE_DENIED 没有被本轮改用其他身份重复，故正式 CLAIM/Source Result 均未取得。本成果为 AUTHOR_SIDE / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING。
