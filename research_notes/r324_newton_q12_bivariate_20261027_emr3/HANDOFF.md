# R324 研究接续｜BRC q=12 与统一二元母函数

研究身份：本地逻辑 Researcher-ID EM-DIRECT-R324-0734；GitHub 实际登录 awdawmip；活动 RA-EMR3-20261027-R324-Q12-0734。原生 session_start 被只读 Scope 拒绝，session 未创建；没有正式 CLAIM、Driver 审查、数学接纳。
全局快照：awdawmip/chatgpt-global-knowledge main@f105f4be6d05e87fb4b8c3e1737db6426a21a23d / GLOBAL_KNOWLEDGE_V1。
P000 原件 blob：770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc。ACTIVE 世界观只读，项目最初规范源 main@f169fc0bfc099474c86c9c4cb18205d85f0ba8f4。研究实际来源 R323 commit 19fd0ae7810ed93768c2295791fa4e3a27ff4f0a。
科学对象为有序正权六边 BRC 的辅助整数计数 M_s，非原生 X6、非复相位模型。

## 已完成并得到精确证据
对所有整数 s≥12：
a_(s,s-12) = 2^s Q12(s)/321452532301824 ≥ (53288801/4096)2^s >0，
等号当且仅当 s=12；Q12、P12、Q12(12+u) 正系数完整列于 R324_Q12_AND_BIVARIATE_AUTHOR_PROOF.zh-CN.md。以原始递推双重归纳证明而非插值；SymPy 有理多项式递推、独立原始整数递推 s=0..192 全部通过。各 181 个 q12 检查通过；样本 a_(12,0)=53288801、a_(13,1)=401236309。

新统一母函数：
U(x,z)=Σ M_s(z)x^s=N(x(1-z),z)/(1+𝔇(x(1-z),z)/(1-z))，
F(x,t)=(1+t)U(x(1+t)^2,(1+t)^(-1))；
a_(s,s-q)=[x^s t^q]F (0≤q≤s)。N、𝔇 均给出有限二项式闭式。全 F 系数并非都非负：B3(t)=8+32t+46t²+20t³−7t⁴−6t⁵，因此 [t⁴]B3=−7 在 q>s 的域外。这阻止直接用整个有理函数的非负系数证明三角区正性。

文件：完整数学证明、R324_symbolic_certificate.py、R324_integer_verify.py、R324_bivariate_certificate.py、R324_EXACT_EVIDENCE.json、HANDOFF.md。状态 DIRECT_AUTHOR_PROVED / EXACT_PASS / NOT_ADMITTED。
BRC 现有 T0 计数与 Newton 观察复用 REUSE_EXECUTED；T1 有理母函数/精确差分 COMPOSE_APPLIED。

## 下一项具体问题
**优先中央阵列**：证明或精确否定 [x^s t^q]F≥0 对所有 s≥0、0≤q≤s。寻找合法斜三角正系数表达、可复用有限状态正锥证书或对角截取化简。必须保留 q≤s 的限制，不能用全 F 系数非负（已有域外负例）。分母因子分解是否允许有界正状态递推是可测试的下一点。
次要窄任务：用 r=13 阶矩递推求 a_(s,s-13) 全指标符号；这不应代替中央问题。
原已证有限证书 R313 s≤128 加 R314—R324 q≤12 作者侧证明共同留下（定义保持一致时）s≥129、0≤k≤s-13。整体缺陷纤维正性与 N_peak=81 未解。
出版和科研接纳应分开：GitHub blob/branch 保存只是论文证据；不得自称正式 Source Result/Working Truth。
