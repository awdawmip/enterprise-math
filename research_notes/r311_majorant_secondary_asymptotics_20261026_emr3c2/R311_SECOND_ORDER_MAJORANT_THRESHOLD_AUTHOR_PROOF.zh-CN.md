# R311 — BRC 缺陷纤维正性**充分证书**的二阶阈值展开

日期：2026-10-26。性质：作者侧组合/渐近证明与可重放的精确整数交叉检验；未经独立 Driver 审查、不是原生 Source Result 或 Foundation 定理。

## 0. 精确来源、身份和声明范围

- 本研究读取并固定账户规范 \`awdawmip/chatgpt-global-knowledge\` 的 \`GLOBAL_KNOWLEDGE_V1 main@3c2f14ffb124902dc0fe1050a8bc11811842ed48\`，包括 \`00_BOOTSTRAP.md\`、\`OPERATING_MANUAL.md\`、Enterprise Math 当前项目与 TASK 入口、P000 V4 及启动投影、ACTIVE《我眼中的世界》、数学/代码/BRC 研究政策和研究活动规则。
- Enterprise Math 控制/方法源固定于 \`awdawmip/enterprise-math main@edbdb734e67f745a47416271b176507aaa6c8134\`：\`docs/PORTABLE_RESEARCH_PROTOCOL.md\`、\`docs/CHATGPT_ORDINARY_CONTROL.zh-CN.md\`、\`control_plane/current_control_authority.json\` 及相关精确合同。科学先行来源：R303 首返分块 \`c8079dcbb383c010196cfd7a422626f1b545bf77\`；R305 生成函数 \`fef7b1db71a9884f55de16ad24d94699412a38d1\`；R309 主项/负项界 \`fb8fa9b03d5b69bfac9c00b6ef0ce0ecb812eebd\`；最新 R310 更优统一楔形的作者侧证明 \`a7575a0a7e8e6e9177524882ac74287f03c1a4cd\`。
- 实际 GitHub 账号 \`awdawmip\` 有仓库管理员及推送权限。研究活动已在项目 main 登记 \`RA-EMR3-20261026-C2-1847\`，本地分配的 \`Researcher-ID=EM-DIRECT-C2R3\` 不冒充平台认证身份。原生查询 \`em_control_tasks\` 返回 \`CONTROL_QUOTA\`；普通 Chat 控制请求 \`status\` 成功但 \`dispatch\` 最终 \`FAILED/TimeoutExpired\`，并非 \`NO_DISPATCH\`。因此不能权威判定活跃 Owner，也未取得正式 CLAIM、Researcher run、Source Result 或独立 Driver 审查；只推进不抢占任何正式 Task 的独立辅助数学单元。
- BRC 工具状态：\`REUSE_APPLIED\`（R303/R305/R309/R310 的保序来源纤维、组合上界及精确二项式接口），\`REUSE_EXECUTED\`（下述 BigInt 完整临界点符号搜索）。没有新建普适运算族。P000 与 ACTIVE 世界观未修改。本结果仅为六边 BRC **来源数量**之差的充分证书分析，不是复振幅相消，更无原生六维 Cell／三维切片／物理心跳时间转移。

## 1. 本轮新的精确定理

沿用正权、有序六边 BRC 辅助来源词统计
\[
D_d(n)=P_n(+,2-n+2d)-P_n(-,2-n+2d).
\]
对每个整数 \(d\ge3\)、\(n\ge4d+4\)，由既有首返来源分块保留顺序、重数和后缀符号，有
\[
D_d(n)=A_d(n)+R_{+,d}(n)-R_{-,d}(n),
\quad R_{\pm,d}\ge0,\quad R_{-,d}(n)\le U_d(n),
\]
其中
\[
A_d(n)=\binom{n-2d-4}{d-1},\qquad
U_d(n)=\sum_{r=1}^{d-1}\sum_{t=1}^{\min(r,d-r)}
\binom{d-r}{t}\binom{r-1}{t-1}\binom{n}{d-r-t}.
\tag{1}
\]
记 \(B_d(n)=\binom{n}{d-2}>0\)，并定义**充分证书**的最早成功整数长度
\[
m_d:=\min\{n\in\mathbb Z:n\ge4d+4,\ A_d(n)>U_d(n)\}.
\tag{2}
\]
这与 \(D_d(n)>0\) 的真实最早长度不是同一个定义。

令 \(c>0\) 为唯一满足 \(c\,e^{-2/c}=1\) 的实数，即 \(c=2/W(2)\)。再定义
\[
\beta=\frac{4c+\frac72-2c^2}{c+2},
\qquad
\gamma=\frac{6c^6-30c^5-327c^4-283c^3-54c^2+18c+1}
{6c^2(c+2)^3}.
\tag{3}
\]
其参考十进制值为 \(c\approx2.3457507549227654\)、\(\beta\approx0.4321255214930036\)、\(\gamma\approx-5.513225335374604\)；十进制近似不参与任何符号证书。

**定理（R311，作者侧）。** 将 (1) 中的二项式视为 \(n\ge4d+4\) 的实多项式/有理函数延拓，足够大 \(d\) 存在唯一实数 \(\nu_d\ge4d+4\) 满足 \(A_d(\nu_d)=U_d(\nu_d)\)，且
\[
\boxed{\nu_d=c\,d^2+\beta d+\gamma+O(d^{-1}).}
\tag{4}
\]
证书的第一个严格成功整数恰为
\[
\boxed{m_d=\lfloor\nu_d\rfloor+1
       =c\,d^2+\beta d+\gamma+O(1).}
\tag{5}
\]
因此 R310 只给出的首阶门槛 \(2/W(2)\) 还具有明确的一阶线性漂移 \(\beta d\) 与二阶实根常数校正 \(\gamma\)。式 (5) 的整数部分不能删除；式 (4) 不等价于整数 \(m_d\) 的 \(o(1)\) 误差表达式。

## 2. 相对主项、证书单调与唯一穿越

保留 R309/R310 的精确比值恒等式
\[
\frac{A_d(n)}{B_d(n)}
=\frac{n-3d-2}{d-1}
\prod_{i=0}^{d-3}
\left(1-\frac{2d+4}{n-i}\right).
\tag{6}
\]
在 \(n\ge4d+4\) 上，右侧全部因子非负，且 \(A_d(n)/B_d(n)\) 随实数 \(n\) 严格增加。

在 (1) 的每个 \(U\) 项中记 \(j=d-r-t\le d-2\)。则
\[
\frac{\binom nj}{B_d(n)}
=\prod_{h=j+1}^{d-2}\frac{h}{n-h+1},
\tag{7}
\]
因而 \(U_d(n)/B_d(n)\) 连续且非增。于是
\[
H_d(n):=\frac{A_d(n)-U_d(n)}{B_d(n)}
\]
在这一区域连续、严格递增；它在 \(n\to\infty\) 时为正，且至多有一个零点。只需在二次尺度找到异号两端，就能确定唯一 \(\nu_d\)，并将严格整数穿越转换成 \(\lfloor\nu_d\rfloor+1\)。

## 3. 主项在 \(n=c_0d^2+bd+g\) 附近的统一展开

这一节先令固定 \(c_0>0\)，固定 \(b,g\) 落在任意紧区间。写 \(n=c_0d^2+bd+g\)，令
\[
p_1=b+c_0-3,\quad p_2=b+c_0+g-5,\quad
\ell_1=\frac{2b-3}{c_0^2},\quad
\ell_2=-\frac{6b^2-18b-24c_0^2-6c_0g+3c_0+16}{3c_0^3}.
\tag{8}
\]
二项式前因子精确长除得到
\[
\frac{n-3d-2}{d(d-1)}
=c_0+\frac{p_1}{d}+\frac{p_2}{d^2}+O(d^{-3}).
\tag{9}
\]
再置 \(a_i=(2d+4)/(n-i)\)，\(0\le i\le d-3\)，故 \(a_i=O(1/d)\)，有
\[
\begin{aligned}
\sum_{i=0}^{d-3}\log(1-a_i)
&=-\sum_i a_i-\tfrac12\sum_i a_i^2-\tfrac13\sum_i a_i^3
+O\!\left(\sum_i a_i^4\right)\\
&=-\frac2{c_0}+\frac{\ell_1}{d}
+\frac{\ell_2}{d^2}+O(d^{-3}).
\end{aligned}\tag{10}
\]
其中使用有限公式 \(\sum_{i=0}^{d-3}i=(d-3)(d-2)/2\) 和 \(\sum i^2=(d-3)(d-2)(2d-5)/6\)。因为 \(\sum_i a_i^4=O(d^{-3})\)，且这些估计对紧区间内 \(b,g\) 统一，余项真正是所写阶数。这里 \(\log\) 只是严格正有限乘积的解析辅助；没有引入任何心跳世界的连续动力学公理。

由 (6)、(9)、(10) 指数展开
\[
\frac{A_d(n)}{d B_d(n)}
=e^{-2/c_0}\left[
c_0+\frac{p_1+c_0\ell_1}{d}
+\frac{p_2+p_1\ell_1+c_0(\ell_2+\ell_1^2/2)}{d^2}
\right]+O(d^{-3}).
\tag{11}
\]

## 4. 负项界的精细前两阶：尾部确为 \(O(d^{-2})\)

令 \(Y=n-d+3\) 与 \(\theta=d/Y\)。将 \(U_d(n)/B_d(n)\) 按首返结构中的 \(r\) 分组。

- \(r=1,t=1\) 精确贡献 \(d-1\)。
- \(r=2,t=1,2\) 精确贡献
\[
\frac{(d-2)^2}{Y}
+\frac{(d-2)^2(d-3)^2}{2Y(Y+1)}.
\tag{12}
\]
- \(r=3,t=1,2,3\) 的领先贡献依次为
\[
\frac1{c_0^2d},\quad \frac1{c_0^3d},\quad
\frac1{6c_0^4d},\qquad\text{余项各 }O(d^{-2}).
\tag{13}
\]
- 对 \(r\ge4\)，将此前 R306/R309 的保留负尾位置的逐组估计直接在本模型内复证。因 \(j=d-r-t\le d-2\)，由 (7) 逐因子比较
\[
\frac{\binom n{d-r-t}}{B_d(n)}
\le\theta^{r+t-2}.
\]
另有 \(\binom{d-r}t\le d^t\)，且 \(1\le t\le r\)。故用二项式定理严格得到
\[
\begin{aligned}
0\le\frac{U_{r,d}(n)}{B_d(n)}
&\le\sum_{t=1}^r
d^t\binom{r-1}{t-1}\theta^{r+t-2}\\
&=d\,\theta^{r-1}(1+d\theta)^{r-1}
=d\,\rho^{r-1},\qquad
\rho=\theta(1+d\theta)=O(d^{-1}).
\end{aligned}\tag{14}
\]
这里当二项式下指标越界时相应项按零处理；在 \(r\ge4\) 的适用范围所有出现的 \(r+t-2\ge0\)，并且 \(\theta<1\) 对足够大 \(d\) 成立。
于是 \(\sum_{r\ge4}U_{r,d}/B_d\le d\rho^3/(1-\rho)=O(d^{-2})\)，统一适用于前述参数紧区间与足够大 \(d\)。

对 (12) 展开并加入 (13)，得严格统一渐近式
\[
\frac{U_d(n)}{B_d(n)}
=d+u_0+\frac{u_1}{d}+O(d^{-2}),
\quad
u_0=-1+\frac1{c_0}+\frac1{2c_0^2},
\quad
u_1=-\frac4{c_0}-\frac{b+3}{c_0^2}
+\frac{2-b}{c_0^3}+\frac1{6c_0^4}.
\tag{15}
\]
这里 \(\gamma\) 不会进入 \(U/B\) 的所需 \(1/d\) 项；\(g\) 只从更高阶进入。

## 5. 逐阶匹配与实根精度

先固定任意 \(c_0>0\)，令 \(d\to\infty\)。从 (11)、(15) 得
\[
\frac{A_d(n)-U_d(n)}{dB_d(n)}
\longrightarrow c_0e^{-2/c_0}-1.
\tag{16}
\]
函数 \(c_0\mapsto c_0e^{-2/c_0}\) 在正半轴严格增加、从 0 增至无穷；故恰有根 \(c=2/W(2)\)。取 \(c-\varepsilon,c+\varepsilon\) 作为二次尺度，则大 \(d\) 时 \(H_d\) 两端异号，第二节的单调性保证真实 \(\nu_d\) 存在且唯一。

在 \(c_0=c\) 时，由 \(e^{-2/c}=1/c\)，比较 (11) 的 \(d^0\) 项和 (15) 的 \(u_0\)，求得恰为 (3) 的
\[
b=\beta=\frac{4c+7/2-2c^2}{c+2}.
\]
再比较 \(1/d\) 项，求得恰为 (3) 的 \(g=\gamma\)。更明确地，对有界 \(g\)，将 \((c,\beta,g)\) 代入全部展开，直接通分化简得到
\[
H_d(c d^2+\beta d+g)
=\frac{c+2}{c^2}\frac{g-\gamma}{d}
+O(d^{-2}).
\tag{17}
\]
因此在 \(g=\gamma\pm C/d\) 时有
\[
H_d(cd^2+\beta d+\gamma\pm C/d)
=\pm\frac{c+2}{c^2}\frac{C}{d^2}+O(d^{-2}),
\tag{18}
\]
而 (10)(11)(15) 的误差在此微扰族上一致且常数与固定 \(C\) 无关。选取一个足够大的常数 \(C>0\)，使主项压过余项，严格正负夹逼得 (4)。利用第二节的单调穿越得到 (5)。证毕。

**审查注意：** 核心输入仍包含 R303/R305/R306 的准确保序分块、\(R_-\le U\) 与 (14) 的逐组 majorant；作者侧全量词结论的独立审查须核验这些输入在同一模型和同一 \(n,d\) 定义下成立。计算不会代替 (14) 的证明。

## 6. 实际 BigInt 精确阈值检验

本轮实际执行 \`R311_verify_majorant_threshold.js\`，以 JavaScript 无界 \`BigInt\` 精确实现 (1) 的二项式和、\(A-U\) 的符号与单调二分；每个样本均核实 \(A(m_d-1)-U(m_d-1)\le0\)、\(A(m_d)-U(m_d)>0\)。严格符号判断无浮点。参数检查值如下（这些是**各个固定 d 的完整整数穿越**，不是已验证无穷多 d 的计算）：

| d | 3 | 4 | 5 | 10 | 20 | 30 | 60 | 100 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| \(m_d\) | 20 | 36 | 57 | 235 | 942 | 2119 | 8466 | 23496 |

| d | 150 | 250 | 400 | 600 | 800 | 1000 | 1500 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| \(m_d\) | 52839 | 146712 | 375488 | 844725 | 1501621 | 2346178 | 5278582 |

15/15 检验通过，最大 d=1500 时 A−U 两侧实际具有约 5958–5959 个十进制位。程序中的 \`Math.exp\`、\`Math.floor\` 仅生成用于观察二阶公式的十进制预测；符号、二分和二项式系数全部由 \`BigInt\` 判定。运行汇总及每个实际整数穿越符号、位数与近似预测分别保存于 \`R311_EXACT_EVIDENCE.json\`。不能把某些样本整数恰与 \(\lfloor cd^2+\beta d+\gamma\rfloor+1\) 相同当成所有 d 的无误差恒等式。

## 7. 科学意义、硬边界及接续问题

R310 已把 \(\,c_*=2/W(2)\,\) 识别为 **\(A>U\) 充分证书**的首阶极限。R311 的新进展是证明这个特定证书的首次穿越存在可控制的次阶展开，并实际确定 \(\beta,\gamma\)。这将后续证书改进问题精确定位：继续单纯优化对 \(U\) 的同一主项估计，无法从 R310 所给 \(c_*\) 首阶屏障跨越到 \(n=O(d)\)；必须利用 \(R_+\) 的补偿、构造直接来源注入，或研究 R307 的全参数 Newton 系数 \(K_s(d)\) 同时增长区间。

**仍开放的关键问题：** 对全部整数 \(d\ge2\)、\(0\le s\le d-1\)，R307 的 \(K_s(d)\) 是否均严格正，从而推出全部 \(n\ge4d+4\) 的 \(D_d(n)>0\)？固定 s 的渐近和 d≤400 的有限证书不能自动解决此联合量词。还需独立处理 R293 28 个中央效果比较、\(N_{\rm peak}=81\) 与原生 X6 物理对应。

结论标记：\`R311_SECOND_ORDER_CERTIFICATE_THRESHOLD_AUTHOR_PROVED / EXACT_BIGINT_15_PASS / SOURCES_R303_R306_DEPENDENT / NATIVE_OWNER_UNVERIFIED / NO_CLAIM / NO_SOURCE_RESULT / DRIVER_UNREVIEWED / NOT_ADMITTED\`。
