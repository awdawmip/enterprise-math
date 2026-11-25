# 2026-11-25 OpenAI 公开数学吸收：张量几何、复杂度与正重数割下界

状态：SOURCE_OBSERVATION / AUTHOR_CHECKED_AUXILIARY_LEMMA / UNREVIEWED / NOT_ADMITTED；本公开数学吸收对话的独立有限推导，外部论文贡献归 OpenAI。不是正式 Task、CLAIM、Result 或 Review。

## 续接与当前规范
先实读 11-24 已保存记录 73d28e20b84491700316f61f609a1eb89c655309:research_notes/public_math_intake_20261124/OPENAI_NOV24_VP_VNP_SEPARATION_INTAKE.md。其 QFT 原请求已成功闭合，不重发；VP/VNP Driver 交接尚无已验证 Task publication。账户 main@6216eab2c0f1db722bc1c0fa47934781d141c43a，EM main@7bbb1758d9f1d3d77bc441cd96523e3967fe1bd4：实读两入口、输出与数学规则、活动协议、ACTIVE 世界观、P000、续接、自主研究、研究方法、Driver/普通 Chat 合同。EM status Source 同 SHA，服务静态账户 pin 不替代当前账户 main。保留综合任务及 ETH/QFT 冻结输入 openai/math@7ef5c0cc5ca4b0e072b7a050fca09ab24bc6fa3a；本次新增公开科学 pin 单独为 3344da59991ed94f9ba711217b29c1d760badfa6。
现行精确综合任务查询 math-intake-20261125-0930-integration-task-read-r1，最后回读 RUNNING/error=null；本对话自身新 RESEARCHER 注册 math-intake-20261125-0930-own-research-registration-r1，最后回读 RUNNING/error=null，服务分配公开 SID MCP-79a19ae7c0294830b934bd158d6f2121，未确认注册终局或活动记录。沿原 ID 回读，不重复注册。未取得自身 DA、CLAIM 或任务执行授权。

## 外部来源变化
openai/math main@3344da59991ed94f9ba711217b29c1d760badfa6，PR #6 merge，compare f5702854040e97fa7675c21ba37a9608f5f92dd3...3344da59991ed94f9ba711217b29c1d760badfa6 ahead=2 behind=0。history.md blob bba84df19e8f3e5656875efd4e2a964d7d2e7767；CONTENTS.md blob 7d4a8770643439016a70f23a4524d0ebacc78900。11-24 九稿两族，原11-23 VP/VNP 由两篇更强论文涵盖但未撤回，原 Paper.tex blob 7e83dc86fb95faf3bcf8cb0b4f9eefac2e99c181 不变；10-07 三稿撤回状态不变。官方出版索引 https://openai.com/research/index/publication/ 11-24 最新可见蛋白设计报告，未见这九稿的单独数学公告；官方 GitHub 直接公开。

379 族（lean/docs/379.md blob b1a856319056d10c922672e8dda0bb924355aaa4），按公开 Lean 范围说明：
1 Euclidean geometry in the asymptotic spectrum of tensors：有限维欧氏凸图表及指定 CAT(0)/联合凸价格前提，共享标签按归一化凸包平均宽度定价；两点距离、三点半周长；无限维 Hilbert 扩展未形式化。intro.tex blob badaa033ae1b8c48848922d57a6ac5d4e6aaebac, prices.tex 408773173318cb2dc09b5d288d021c969b7fed76, width.tex 9284d3abd9a8e50a835e7fa9d5e5a363fd119dd1。原文割秩积分与原生 X6 路径成本不同，见下独立辅助命题。
2 Paths, trees and grids separate Valiant’s hierarchy：任意域 VF⊊VBP⊊VP⊊VNP，精确公式、仿射标签分支程序、算术电路和布尔见证求和；正方网格排除多项式规模 degree-component border circuits，明确 n^{Ω((log n)^{1/12})} 定量界未形式化。
3 Circuit lower bounds for Hamiltonian cycle and the permanent：任意域有向 Hamilton 环，特征非2 permanent，精确电路超多项式下界；新更强 exp(c(log N)^2/(log log N)^2) degree-N 系数近似电路界未形式化。signed path-count P_n^star 的 exact lower bound 2^{c(log_2 n)^{5/4}} 在说明中。
4 The logarithmic exponent of finite Fourier transforms：阶 n≥2 有限阿贝尔群，域含群指数阶原根且 n 可逆；正逆变换二输入加权和电路 Ω(n sqrt(log n))、O_epsilon(n(log n)^{1/2+epsilon})，J 批共享门仍有 J 倍界；正式多项式乘法上界相应成立，独立乘积的对应下界未形式化。
5 The logarithmic exponent of integer multiplication on tapes：固定确定性多带机完整 2n 位输出，n(log n)^{1/2+o(1)} 时间、O(n) tape cells；Ω(n sqrt(log_2 n)) 下界以 Weak ETH 为前提，指数 1/2 是可达指数的下确界，是否取到仍未决。除法/开方对应界未形式化。Weak ETH 排除 2^{O(v^{1-eta})} L^{O(1)} 的确定性 3-SAT；与原已冻结普通 ETH 反证不是同一陈述，不能代换。
6 The matrix multiplication exponent is nine fourths：任意域、形式多项式恒等式、division-free 算术运算，omega=9/4，dual exponent=1/2；权重排序 x≥y≥z>0 时矩形指数 x+y+[max(0,(x+y)z-xy)]²/(4xyz)。允许除法保持方阵指数；每个 n≥2 的 ceil(n^{9/4}/2) nonscalar mult/div 下界未形式化。
7 An exponential bound for sunflowers：每个固定 r≥3 有 C_r，超过 C_r^k 个不同 k 元集合含 r-petal sunflower；显式 B_r 的 log B_r=O((log r)^4(log log(2r))^{5/2}) 未形式化。

380 族（lean/docs/380.md blob 4bd8791266871ad39435b68b96551bddd43dde5d）：
8 Strongly polynomial linear programming：有理 RAM 上固定程序，m+d 的多项式指令数，存储有理数位长为输入位长的多项式。可行性/Farkas 证书（至多 rank(A)+1 非零项），最优原对偶证书或可行点和单位目标增量射线。Smale 第九问题。
9 Superpolynomial graph diameter of simple polytopes：简单有理多面体 n facets，维数 subpolynomial，边图直径超任意 n 的固定多项式；允许跨低维面及规定目标间隔仍有超多项式距离。与强多项式 LP 不矛盾，因为任意算法不必按边行走。

## Lean 实读边界
固定 commit 读取九个 Comparator 配置与实际 solution 入口：
ArithmeticHierarchy 826e1a5af6e25a458cfb26c09580479b23b7cccf / OAI.Hierarchy.Strict 113ff541d3664db36bc20f3c477835f387ff785f；
VPVNP b55ae410b72d0d0f6d1f223cd638cb3dbb2845f5 / ClassSeparation 513ce5b4c02108143cadee0e1e612156349d2202；
ExactFourier 83f801efdbf58ff989ab49e2ba21de1cbaf244b1 / FiniteFourier.Main ad2790bb43c948c0d7c4509bc32aef0d49412f08；
NearSquareRootMultiplication bc5fe8db7ab24aaf98100442d697935c92e39e66 / NearSquareRoot.Main 1934cd4d58920bfd90aca66fca114b87df5482f5；
MultitapeWeakETH 2ba7da9edcf8b8bada83a02462b600296e00e0d3 / MultitapeWeakETH.NearRoot ca93737e6952e7d1f9923d819acf461e3d26dbfb；
MatrixExponent 49267c30c0d7acad2931cb79a4521f790caa10e8 / SpectralBooks.ExactExponent c0a1bc6519c86e87e9672b3cdf7b8e766acd3a37；
Sunflower 00994b5aa966112699706eb34df343afdb06625e / Sunflower.FixedBase 59eaae86c7b8a74cab4a4b5680880fa1b0fd7773；
LinearProgramming 83c189fa30a5b8dfd3159a49caee3aee6cc8fc3f / LinearProgramming.Optimization 88b4d7d15964f05fcdb2e3b11545e1bc6fe213cf；
Hirsch fe688f7de9b278c9a088ed1857aa1450f8f50dd6 / Hirsch.Main 10538735102ffec032ddb896df8b50de9a0b0251。
九配置均仅允许 propext, Quot.sound, Classical.choice。入口行级静态扫描未命中行首 axiom/admit/sorry 或 := sorry，非完整词法/依赖闭包审计。GitHub combined statuses=[]。当前执行环境 command -v lean/lake 无输出；没有独立运行 Lean、Comparator、依赖闭包/axiom audit。禁止将仓库说明或静态扫描写为独立 PASS。MatrixMultiplication 旧挑战文件移除且 MatrixExponent 新挑战加入，不等于撤回；11-24 history 亦未报告撤回。

## 有限研究增量：正重数的多割共同约束
续 11-24 fixed-cut rank 基线。下面为外部有限坐标关系网络的独立、可手工核验辅助引理，不是已执行的原生 BRC 算子或完整心跳动力学。P000 的六轴、120°原生正角、三元稳定及时间独立不变。

对象：有限个端口 p_i（至少2），坐标 z_i∈Z^d，d≤6；以同一选定参考 Cell 表达相对坐标。每个网络分支 t 有有限内部图，边 e 连接坐标只沿一个坐标轴移动，长度 ℓ_e 为该轴整数步数（同坐标的局部连接可计零）；边内部指标的状态数≤2^{b_e}，b_e 为非负整数。每个节点局部张量取非负整数，按独立边指标求和乘积；分支相加是自然数正重数。各端口外部标签来自 {0,1}^m。目标是逐项相等张量 Δ：全端口标签一致时为1，否则0。定义
S=Σ_{a=1}^d(max_i z_{i,a}−min_i z_{i,a})>0；
W_t=Σ_e ℓ_e b_e（bit-step 成本）。
任何有限 A 分支的精确表示满足
    Σ_{t=1}^A 2^{floor(W_t/S)} ≥ 2^m.
若 W_t≤w，则 floor(w/S)+log_2 A≥m，且 selector 为 A=2^s 时 w≥S max(0,m−s)。

证明：正整数相加精确等于 Δ，所以每支张量在非对角元全为0，在对角元为0或1；各支支持 K_t 为共同标签集合的互不相交分割，Σ k_t=2^m（k_t=|K_t|）。忽略空支。每个切割 a,h（min≤h<max，坐标≤h 与≥h+1 分隔）两侧至少各有一个外部端口。把该支张量在此切割展平为矩阵，在 Q 上恰有 k_t 个独立非零行列配对，秩 k_t。固定所有跨割边指标后剩余张量按两侧因式分解，展开至多 2^{Σ_cross b_e} 个秩一项，故每个割的 Σ_cross b_e≥ceil(log_2 k_t)。沿全部 S 个整数坐标割求和：每条轴边被计恰 ℓ_e 次（只统计端口坐标范围内切割时至多 ℓ_e 次），于是 W_t≥S ceil(log_2 k_t)，推出 k_t≤2^{floor(W_t/S)}，相加得证。允许每个分支不同拓扑或不同实际最小割位置，仍共同受同一坐标割族约束。

锐例：外部完整整数网格中，2端口沿最短坐标轴路径连接，长度 S；3端口可取逐坐标中位点，三个单调坐标路径边互不重叠（各轴的非零带向支持至多两个端口且方向相反），总长恰 S。分 A=2^{m-b} 个固定前缀组，每支只经树传 b 位共同后缀，端口校验同一固定前缀，树节点等值复制，W_t=S b。自然数每个合法标签有唯一内部延拓。m=1,2,3 的 (A,b) 锐例为 (1,m),(2,m−1),…,(2^m,0)；参数可任意 m。该锐例还需全局选择/分支描述、局部表、构造、恢复的真实成本，不把 bit-step 锐界误称总复杂度改进。原生 Cell 合法性可能排除该树，故原生只在给定合法轴路径图、明确六坐标嵌入且实现相关合同的条件下引用下界；不将外部网格、欧氏平均宽度或二力平衡当作 P000 事实。

代数类型障碍：F2 与 F3 的同一二端口 m=1 相等矩阵 I=J−X（J 全1，X 反对角置换矩阵）。每支有非对角支持却合成精确 I，F2 的减法即加法；正整数分支分割步骤失效。不能把上述多割分支界直接传到可抵消域；它为下一项选择共同割证书/显式 signed residual 的区分实验提供了具体失败点。仅二端口 fixed-cut 的一般域秩界仍沿原条件成立。

## 去重、正式交接与下一单元
当前 Source research_tasks 目录895项；匹配 OpenAI/complexity/tensor/Valiant/Fourier 等名称，已有 RS-BRC-FUTURE-FAITHFUL-INTEGRATION-20261028、三项 OpenAI ETH/QFT、RS-BRC-UNKNOWN-ORDER-BITWISE-FOURIER-SAMPLING-20261005。内容检索 VPVNP、Euclidean tensor、MatrixExponent、sunflower、strongly polynomial、Hirsch、Fourier、strict shortening 未返回结果（不能证明全库无同类研究）。实读综合任务书及其 ACTUAL_TYPED_BRC_ONLY 范围，原 ETH/QFT pin 保持不变。上述引理不冒充综合任务的原生计算或新正式输入。
优先交接同一 11-24 VP/VNP 研究方向：正重数多割资源约束、signed/finite-field 反例与 selector/分支成本；在真正 typed BRC 路径载体上，以三端口/六轴合法路径及明确未来观察，检查能否达到条件锐例并核算总成本。若原综合任务范围允许，由其当前合法 owner/Driver 增量绑定新外部输入，否则由合法 Driver 发布独立有限新方向。不要重复发泛化压缩或 Shor 任务。矩形矩阵指数与精确有限 Fourier 适合作为独立外部对照，强多项式 LP/Hirsch 作为优化模型与路径几何分离的边界，暂不抢发多个并行任务。
正式发布 PENDING_DRIVER_DECISION；本轮现行 native followup_materialize 只接真实 Result/read、review/synthesis 及自身 DA，本次是外部吸收，不制造 Result 或假 DA，也不借旧身份。原任务查询与 own registration 回读原 ID；若成功，按合同补 Activity 关联并核验。正式任务及独立 Lean 尚待执行。