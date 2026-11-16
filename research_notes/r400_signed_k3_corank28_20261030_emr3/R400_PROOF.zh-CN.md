# R400｜第28余阶十二支路有符号 BRC 有限 PF₂ 全实参数精确分类

日期：2026-10-30。作者侧已计算复现，DRIVER_UNREVIEWED / NOT_ADMITTED / ACTIVITY_REGISTER_PENDING。该结论为固定有限辅助模型，不是原生 X6 动力学或原生任务 Result。

## 对象、冻结来源与精确目标

复用 R346_verify.py 原始十二支路带符号 K/J 递推（Git blob 1579ceb717ab1945227eca4f7a1878bf4ffa73e1）和 R399 已发布递推源码（commit a603caa19583be512ec623dac9618fd2d22054b3）。只改变 K3[t²]=-8(1+theta)，其他 signed branches 不动，theta>-1。
令 B0=1+t，Bs=Js+sum_{i=1}^{min(s,12)} Ki B_{s-i}，b_{s,q}=[t^q]Bs，
D(q,k)=sum_{w=0}^{k}(-1)^(k-w) binom(k,w) 2^(q-w) b_{q+w,q}，
Hr(k)=5^(-k)D(r+k,k)，Lr(v)=5^r Hr(v)，
Qr(v)=Lr(v+1)Lr(v+2)-L(r-1)(v+2)L(r+1)(v+1)，
c_j=Delta^j Qr(0)，T_j=c_j²-c_(j-1)c_(j+1)。
固定 r=28，57项 c0...c56，55项 Turán T1...T55。PF₂ 只指此有限 Newton 序列 Toeplitz 二阶全非负，严禁自动推广到全 D 阵列 TP₂、无限 Q 或 X6 三维切片。

## 定理、全参数证明

取 a=1869789/1000000，b=1869790/1000000，令 eta28 为 T29 在 (a,b) 中唯一实根。则 C28(theta) 属于 PF₂ 当且仅当 -1<theta<=eta28；十进制显示 eta28≈1.8697893957305505，不用于判号。

整数 theta 多项式递推生成全部 c_j、T_j。使用有理 Bernstein 恒等式 p(l+(h-l)t)=sum_{k=0}^n beta_k binom(n,k)t^k(1-t)^(n-k) (0<=t<=1)，检查所有 beta_k>0 即得闭区间严格正性。逐个对 c0...c56、除 T29 外的 T1...T55 在 [-1,b] 严格认证，对 T29 在 [-1,a] 严格认证。T29(a)>0>T29(b)，且 -T29' 在 [a,b] 的 Bernstein 系数严格正，所以 T29 在该区间单调降、只有一个简单零点；临界点其余 c、T 仍严格正。有限正序列相邻对数凹性（全部 T>=0）推出所有 Toeplitz 二阶子式非负。

在 [b,4]，11段无缝闭有理区间各由一个 c_j<0 或 T_j<0 的 Bernstein 证书排除。在 theta=4+u (u>=0) 上，-c0(4+u) 的每一非零幂系数严格正，故无界尾部均排除。四部分覆盖全部 theta>-1，不是采样外推。总计116个判号证书对象、126段无缝叶区间、133次 Bernstein 检查、8865个严格正的有理 Bernstein 系数，最大细分深度10。两个独立算术路径在7组有理 theta 上完成784项逐项精确一致，脚本输出 R400_SYMBOLIC_PASS、R400_EXACT_PASS。

## 退化和局部再入的精确事实

在 theta*=15/8，ord c29=3，ord c(28+s)=2s (2<=s<=28)，ord T(28+s)=4s (1<=s<=27)。c29..c56 在该参数全为零，而 T26、T27 严格负，因此 PF₂ 不恢复。这再次支持奇余阶首个系数二阶、偶余阶三阶的有限证据，仍没有证明全余阶结论。

精确全 theta 多项式恒等式 c56=263747951750360(30-16theta)^56，系数等于 Catalan(28)；尚未得到对一切 r 的统一证明。

T29 在 (1880172/1000000,1880173/1000000) 有第二简单零点（约 1.8801729536759273），导数在该闭区间严格正，且 c29 在该闭区间严格负。因此单一 Turán 缺陷重新转正并不能恢复 PF₂。

## 证据、复现和范围

实际运行源码 r400_exact.py、r400_symbolic.py、r400_certify.py 作为原始十二支路和机器证书重建入口；执行 python r400_symbolic.py && python r400_certify.py 生成完整 R400_POLYNOMIALS.json / R400_EVIDENCE.json；它们的 SHA256 和运行计数记在 R400_EVIDENCE_INDEX.md。压缩包另保存生成数据、日志和完整 SHA256SUMS。有限组合/BRC 载体保留原始 signed branch provenance；观察与未来操作只覆盖 Newton、Turán 和有限 Toeplitz，不转译物理时间、原生六轴或残差归因。

下一问是解释 ord c(r+1) 奇偶分岔的 K/J 代数机制，并证明或推翻通用最高系数 Catalan 恒等式；备选第29余阶59项 PF₂。正式 Source owner/CLAIM/Result/Review 仍待权威确认。P000 与 ACTIVE 世界观未改。
GLOBAL_KNOWLEDGE_V1 固定 main@33178c632bc6256e5f1fef5f016622dd99149d72；Enterprise Math main@cd8eb5074a45543846518bfa132851e53b9eb97d。