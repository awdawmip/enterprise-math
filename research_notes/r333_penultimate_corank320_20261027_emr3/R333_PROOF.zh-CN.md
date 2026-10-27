# R333｜BRC Newton 差分：任意余阶的次高插值系数闭式与321条无界正性带

**级别：作者侧代数证明与计算辅助证书，UNREVIEWED / NOT_ADMITTED；不是原生 CLAIM、Source Result、Foundation 或真实六维物理模型的已接受结论。**

## 输入及严格适用域

冻结 GLOBAL_KNOWLEDGE_V1 main@e1cf9d381d32b4cd72648613189aa0ebbe0b0a2a、P000 Blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc、ACTIVE 世界观 Blob 99238c3466eb0805748bae01fd1a20868a5a351e；研究开始时 Enterprise Math main@eb2ba75469454c5b6f6b46c683b1d4ecdce897b7。原始有序六边 BRC **辅助有符号组合计数多项式**来自 R330 7c73f56263c3f0515aa28e55ced2d4c703b8e086、R331 98e7ccce13c07fa91c816314b01f0681dc7c264e、R332 16b2209bda28aa8d8082331820e0e1e62410fef3。原始12项 K/J 有符号递推全程保留域外负尾，不提前截断。

定义 N_(q,v)=2^(q-v)[t^q]B_(q+v)(t)，D_(q,k)=(Δ_v^k N_(q,v))_(v=0)。R330 作者侧精确二元有理母函数抽取引理给出次数至多 r 的有理多项式 H_r，且 D_(r+u,u)=5^u H_r(u)，r,u≥0。令 c_(r,i)=Δ^iH_r(0)。

## 定理 A：覆盖所有 r≥1 的次高 Newton 系数

对每个整数 r≥1，精确恒等式

\[
\boxed{c_{r,r}=6^r,\qquad c_{r,r-1}=6^r(6r-1)/5>0.}
\]

r=0 时 c_(0,0)=1。本结论基于 R330 的抽取引理，不是由有限整数正性外推；它也不单独证明所有其他 c_(r,i) 正。

### 作者侧全指标代数证明

令 U(x,t)=A(x,t)/(1-K(x,t))，A=1+t+Σ_(s≥1)J_s(t)x^s，K=Σ_(i=1..12)K_i(t)x^i。将 x=(1−y)/2，t=yz 代入，写

\[
\mathcal P(y,z)=yU((1-y)/2,yz)=N(y,z)/E(y,z),\quad E=(1-K((1-y)/2,yz))/y.
\]

从完整原始 K_i/J_s 精确展开所得低阶系数：

\[
E_0=1-\frac54z,\quad E_1=z,\quad E_2=\frac{z(11z^2-16z+4)}{16},
\quad N_0=1,\quad N_1=0. \tag{1}
\]

令 a=4/5，G_j(z)=[y^j]\mathcal P(y,z)=g_j(z)/E_0(z)^{j+1}。从 E G=N 得

\[
g_0=1,\qquad g_j=N_jE_0^j-\sum_{\ell=1}^j E_\ell g_{j-\ell}E_0^{\ell-1}. \tag{2}
\]

E_0(a)=0，E'_0(a)=−5/4，E_1(a)=a，E_2(a)=−11/125。对 j≥1，有 g_j(a)=(−a)^j。对 (2) 求导并在 a 代入，j≥2 时只有 ℓ=1,2 项非零，得到

\[
g'_j(a)=-g_{j-1}(a)-a g'_{j-1}(a)+\frac54E_2(a)g_{j-2}(a).
\]

以 g'_1(a)=−1 作归纳：

\[
\boxed{g'_j(a)=(-a)^{j-1}\left[-1-\frac{69}{80}(j-1)\right]}. \tag{3}
\]

R330 精确公式（**显式未独立审查的数学前提**）：

\[
H_r(q-r)=\sum_{j=0}^r\sum_m g_{j,m}5^{r-m}4^m
\binom{q-m+j}{j}\binom{2q-j}{r-j},\qquad q=r+u. \tag{4}
\]

其中 g_j(z)=Σ_m g_(j,m)z^m。固定 r 时 (4) 是次数至多 r 的有理多项式。设 q 的最高、次高项为 L_rq^r+A_rq^(r−1)。由精确下降阶乘展开，

\[
L_r=5^r\sum_{j=0}^r \frac{2^{r-j}g_j(a)}{j!(r-j)!}
=5^r(2-a)^r/r!=6^r/r!. \tag{5}
\]

两个组合式的 q^(r−1) 系数包含

\[
T_{r,j}=\frac{j(j+1)}2-\frac{j(r-j)}2-\frac{(r-j)(r-j-1)}4.
\]

应用 (3)，对形式符号 r,j 精确恒等

\[
T_{r,j}g_j(a)-ja g'_j(a)
=(-a)^j\left[-\frac{r(r-1)}4-\frac9{80}j(j-1)\right]. \tag{6}
\]

因此

\[
A_r=5^r\sum_{j=0}^r\frac{2^{r-j}}{j!(r-j)!}
\left[T_{r,j}g_j(a)-ja g'_j(a)\right].
\]

以 (2−a)^r/r! 的二项式卷积及二阶析出 j(j−1) 精确求和，得

\[
A_r=-\frac{3r(r-1)}{10}\frac{6^r}{r!}. \tag{7}
\]

设 q=u+r，H_r(u) 的 u^r 系数是 L_r，u^(r−1) 系数为
\(P_r=r^2L_r+A_r=L_r(7r^2+3r)/10\)。由下降阶乘/Newton 变换
\(\Delta^ku^n|_{u=0}=k!S(n,k)\) 及 \(S(r,r-1)=\binom r2\)，于是

\[
c_{r,r}=r!L_r=6^r,\quad
c_{r,r-1}=(r-1)![P_r+\binom r2L_r]=\frac{6^r(6r-1)}5>0.
\]

对于 r=1 公式亦直接适用（常数次高项）。这里使用的是一般符号恒等式，和下节对 r≤320 的有限证书无关。符号验证程序还从原始 K/J 独立构建 (1)，检查 (6) 的通用符号恒等及 r=1..32 的原始递推交叉样本。

## 定理 B：新增301≤r≤320二十条完整无界正性带

直接从原始 signed-tail K/J 整数递推构造 B_s(t)，对 r=301..320, v=0..r+1 精确求

\[
H_r(v)=5^{-v}\sum_{a=0}^v (-1)^{v-a}\binom va
\,2^{r+v-a}[t^{r+v}] B_{r+v+a}(t).
\]

求出 c_(r,i)=Δ^iH_r(0)，覆盖 301≤r≤320、0≤i≤r，共 **6,230 个 Fraction，全数严格正**。每个 r 都验 c_(r,r)=6^r，且额外节点 v=r+1 的 (r+1) 阶差分为0；与 R332 原始运行证据的 r=300 界面一致。由 R330 先验 deg H_r≤r 和精确 Newton 插值，全部整数 u≥0 满足

\[
\boxed{D_{r+u,u}=5^u\sum_{i=0}^r c_{r,i}\binom ui
\ge5^uc_{r,0}>0,\qquad 301\le r\le320.}
\]

因此结合 R331–R332 已证 r=0..300 的作者侧结果，共有 **321条无界整数差分带 r=0..320**。所有适用阶前向差分 Δ^jH_r(u) 也严格正。有限证书本身不独立提供无限外推，它依赖已注明的 R330 有理抽取证明。

## 实际运行的精确证据和剩余范围

执行 Python 任意精度整数/Fraction 程序 R333_VERIFY.py，参数 min-r=301,max-r=320，并在拥有先前完整 R332 evidence 时带 prior-r332 交叉比较，结果 PASS。B_s 原始 signed-tail 递推 s=0..962；三角域 **464,166项**全部严格正、域外 **194,675个负系数**保留；6,230项正有理系数、20次最高差分检查、20个额外多项式次数检查均通过。按 (r,i) 序列中每项 r,i,numerator/denominator + LF 形成完整确定性摘要：

b873ec12fd6c5f305fa962bf8244db68cdf09c7bb03af383f022f72402c31d17

执行 R333_PENULTIMATE_SYMBOLIC.py --max-r 32，SymPy 有理符号恒等及原始整数 r=1..32 交叉检验 PASS。没有浮点符号判定；上面 321 无界差分带的结论不等于原始 Newton 三角域全指标正性。先前 R327 的 s≤1280 有限域证书强于此处 s≤962，没有新扩张。

**权限**：GitHub awdawmip（admin、push）；EM gateway 0.6.11 只读 status 研究权限 false，em_control_tasks 返回 CONTROL_QUOTA，因此 owner 未权威确认；没有 native CLAIM、Source Result 或独立 Driver 审查。研究对象是外部辅助有符号组合模型，不作原生 X6 Cell 六维动力学、独立三维平面、时间因果或物理参数主张。P000/ACTIVE 世界观未修改。

下一值得推进的精确问题：利用 E_3、N_2 与 g''_j(4/5) 证明或证伪所有 r≥2 的 c_(r,r−2) 正性；随后寻找控制所有 i,r 的二维正锥不变机制。可选再计算 r=321（322 个证书）但非统一解法。在目前充分证书框架下未知的差分区域含 q≥641 且 0≤k≤q−321。此结果均为 AUTHOR_SIDE / UNREVIEWED / NOT_ADMITTED。

Researcher-ID: EM-R333-9B1FB4 (locally allocated; not service-issued).
