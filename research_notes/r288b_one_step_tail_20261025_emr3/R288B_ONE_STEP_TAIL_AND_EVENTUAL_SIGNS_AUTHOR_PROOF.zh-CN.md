# R288B — BRC 负平移纤维的一步正核、双基底归约与渐近符号完全分类

日期：2026-10-25。地位：AUTHOR_PROVED_WITH_DEPENDENCIES / EXACT_INTEGER_CHECKED / DRIVER_UNREVIEWED / NOT_ADMITTED。

## 1. 固定模型、来源及权限

本研究仅限 R268–R287 固定的正权、有序、六边 BRC 辅助自动机。初态 (q,epsilon,k)=(0,+1,0)，转移 (q,bit) -> (q',eta,c) 是
(0,0)->(2,-1,-1)，(0,1)->(2,+1,-1)；
(1,0)->(0,-1,-1)，(1,1)->(0,+1,-1)；
(2,0)->(1,+1,+1)，(2,1)->(2,+1,-1)。
有序效果复合为 (epsilon,k)★(eta,c)=(eta epsilon,eta k+c)。clean 路径禁止来源串出现 00，末态 q=0。P_n(epsilon,k) 为原始来源串的非负整数数量，没有进行归一化或忽略重数。

规范固定读取 Global main@c92003bea71fd3e63a82e6130331dc9ab25b981f（两入口、EM 项目启动、P000 原件与 ACTIVE 世界观、数学/BRC/代码/活动规范），P000 原件 blob=770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc；Enterprise Math main 读取基准 723e55977e3b8fc0db61df3da21b5680c2994175。精确 Green 核前提来自 R283@98eb41b63bb29c9b32d79ba5d9b4ef74d0975fa0；正 h 方程来自 R286@83aaa25e0bf6e34ad65c80498a45ed8a6648f060；上轮待证四基底来自 R287@c2279fcee701cf874e7a865b86fab100137e8de0。这些是作者侧已验证来源，尚非独立 Driver 数学接纳。

真实 GitHub 用户 awdawmip，可向本仓库作者分支写入；原生 em_control_tasks 受 CONTROL_QUOTA 限制，em_session_start 返回 STATIC_READONLY_SCOPE_DENIED，operation_sent=false。故没有本轮 Source 签发 Researcher/CLAIM、没有权威当前 Owner 核定。本文只记录本轮作者侧新数学及证据，不修改 P000/ACTIVE 世界观，也不将辅助二维标签称为原生二维平面或把路径长度对应物理时间。

## 2. 全长度新定理 A：一步正核传递

令 F_m^epsilon(x)=sum_{n>=0} P_n(epsilon,-m)x^n，
Delta_m^epsilon(x)=F_m^epsilon(x)-F_{m+2}^epsilon(x)。
从 R283 的精确公式（正符号 m>=1，负符号 m>=2）：

$$
F_m^+(x)=x^2J(x)u(x)^m(1-x^2+x^4-xu(x)),
$$
$$
F_m^-(x)=x^4J(x)u(x)^{m-2}(1-xu(x)).
$$

因此对于上述合法 m，直接逐项比较得到

$$
\boxed{F_{m+1}^\epsilon=uF_m^\epsilon,\quad
\Delta_{m+1}^\epsilon=u\Delta_m^\epsilon.}
$$

R287 已给二步式 Delta_(m+2)=u^2 Delta_m；本轮发现该式可提升为跨奇偶索引的一步精确传递。

置 y=x^2，a(y)=1+2y^2-y^3，D(y)=a(y)^2-4y，
$$
u(x)=\frac{a(y)-\sqrt{D(y)}}{2x}=xv(y),\quad v=(1+y)(1+h(y)).
$$
由 yv^2-av+1=0 直接代入 v=(1+y)(1+h) 得到
$$
\boxed{h=y^4+(y+2y^2+y^3+y^4)h+y(1+y)^2h^2}.
$$
此等式唯一确定 h 属于 y^4 Z_>=0[[y]]；从 y^4 初始项及 y h 项归纳可知 [y^j]h>0 对全部 j>=4。故
$$
\boxed{u\in x\mathbb Z_{\ge0}[[x^2]],\quad
[x^{1+2j}]u>0\iff j=0,1\text{ 或 }j\ge4.}
$$
中间 j=2,3 的两个系数严格为零。于是 Delta_m 系数全非负可无损传递给任意更大的 m（不必分奇偶）：这是对全长度、全部原始来源重数的形式幂级数定理，并非有限实验外推。

## 3. 新定理 B：四待证基底严格归约为两个，并确定所有更低基底不可能全非负

R287 需分别证明 Delta_13^+、Delta_14^+、Delta_11^-、Delta_12^- 非负。本轮由一步正核严格证明：
$$
\boxed{
(\Delta_{13}^+\succeq0\ \land\ \Delta_{11}^-\succeq0)
\Longrightarrow
\begin{cases}
\Delta_m^+\succeq0&(\forall m\ge13),\\
\Delta_m^-\succeq0&(\forall m\ge11).
\end{cases}}
$$
其中「>=0」表示每个长度的整数系数都非负。这同样蕴含 R287 的 28 效果候选窗口，但该窗口仍以本节两个尚未解决的全系数正性命题为前提。

更进一步，原始来源精确反例
$$
[x^{24}]\Delta_{12}^+=-56,\qquad
[x^{20}]\Delta_{10}^-=-5
$$
说明不存在任何 1<=m<=12（正符号）或 2<=m<=10（负符号）的全长度非负基底：如果有，则重复乘以 u 的非负系数将使上列反例也非负，构成矛盾。因此 13/11 是所有「单一基底 + 正核向更大指标传递」方案的最早**可能**起点；此为必要性定理，并不声称两基底的充分正性已证明。

## 4. 新定理 C：每个固定负平移指标的最终符号分类（不依赖 R280/R281）

将 Green 核写成 y 级数，令 r(y)=sqrt(D(y)) 且 v(y)=(a-r)/(2y)。把 Delta_m=x^{m+2} d_m(y)，则严格有
$$
\boxed{d_m^+(y)=\frac{v(y)^{m+1}}{1+y}(1-y+y^2-yv(y)),\quad m\ge1,}
$$
$$
\boxed{d_m^-(y)=\frac{v(y)^{m-1}}{1+y}(1-yv(y)),\quad m\ge2.}
$$
这是直接利用 (1-u^2)/sqrt(D)=u/x=v 约去 Green 核得到的恒等式，不依赖数值拟合。

令 phi=(1+sqrt(5))/2，rho=phi^(-2)=(3-sqrt(5))/2，s=sqrt(rho)=phi^(-1)，以及 c=sqrt(-rho D'(rho))>0。D=(1-y)(1-y^3)(1-3y+y^2)，其唯一模长最小的零点是 y=rho，其余零点模长至少1。v(rho)=phi 且
$$
v(y)=\phi-\frac{c}{2\rho}\sqrt{1-y/\rho}+O(1-y/\rho).
$$
对 d_m 的 v 参数取偏导；在 y=rho，两个括号恰有
1-rho+rho^2-rho phi=rho^2，
1-rho phi=rho。
代数平方根奇点的标准系数转移给出：固定合法 m，j->infty，
$$
[y^j]d_m^+=K_m^+\rho^{-j}j^{-3/2}
 + O_m(\rho^{-j}j^{-5/2}),\quad
K_m^+=\frac{c\phi^m}{4\rho(1+\rho)\sqrt\pi}
 ((m+1)\rho^2-\sqrt\rho),
$$
$$
[y^j]d_m^-=K_m^-\rho^{-j}j^{-3/2}
 + O_m(\rho^{-j}j^{-5/2}),\quad
K_m^-=\frac{c\phi^{m-2}}{4\rho(1+\rho)\sqrt\pi}
 ((m-1)\rho-\sqrt\rho).
$$
这里近点外的潜在 y=-1 极点和单位模奇点均严格远于 rho；解析部分不改变主指数项。由于 sqrt(rho)/rho^2=phi^3=2+sqrt5，sqrt(rho)/rho=phi，两个常数均非零，符号精确分类为
$$
\boxed{
\begin{array}{c|c}
\text{指标}&[x^{m+2+2j}]\Delta_m^\epsilon\text{ 对充分大 }j\text{ 的严格符号}\\
+\;m=1,2,3&负\\
+\;m\ge4&正\\
-\;m=2&负\\
-\;m\ge3&正
\end{array}}
$$
「充分大」在每个固定 m 下成立，但本定理尚未提供统一可计算的有效 N；不能用它直接宣称 Delta_13^+、Delta_11^- 的全长度正性。

## 5. 本轮有限无界整数核对

执行的独立标准库程序 R288_verify_one_step.py 保持两个计算途径：
（甲）由 f_j=-[y^j]sqrt((1-3y+y^2)/(1+y+y^2)) 的完整精确递推直接生成两基底系数到 j=8000（对应正符号最大原始路径长度16015、负符号16013），检查均非负，并保存逐项 SHA-256；
（乙）原始六边、禁 00 的来源路径 DP 到 n=160，对四基底直接算计数差与代数核系数交叉比较；
（丙）按 h 的独立正整数递推生成 u 的前91项，逐项检查 Delta_(m+1)=u Delta_m，j=0..69。

机器输出 EXACT_EVIDENCE.json 为 PASS。有限证据只证明所列有界范围，不能越界提升两个待证基底为永久定理。数值依赖使用 Python 无界整数；没有浮点判断承担任何全系数正性证明。

## 6. 下一最小未决单元与接续

真正未完成的是两个、不是四个：
$$
\boxed{\Delta_{13}^+(x)\succeq0,\qquad\Delta_{11}^-(x)\succeq0.}
$$
优先复用 R285 比值正锥，或对 d_13^+ 与 d_11^- 构造直接组合注入／有理正锥证书，使有限前缀与严格无限尾相接。取得上述两项后才能无条件应用 28 候选窗口，并逐一建立其他有限效果在 n>=N_peak 时不超过中央效果的有效阈值；此后再审查 R274/R275/R282，尝试六通道 B_n=Lambda_n 的有效起点。

本轮不申请原生数学接受、不假冒独立 Driver、未验证当前活跃 Owner，源论文保存到独立作者分支。原生会话和数学审查仍须按现行协议恢复或由真实授权执行者接续。