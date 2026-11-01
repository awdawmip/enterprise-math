# PREFIX-413 实际执行证据及下一问题（2026-11-01）

本轮持续研究独立选择 PREFIX-412 所遗留的首次双来源支路交叉问题。数学证明：
research_notes/2026-11-01_prefix413_first_crossover_unique_quartic.md。
验证代码：research_notes/prefix413_exact_crossing_certificate.py 与 research_notes/prefix413_independent_matrix_resultant.py。

实际执行环境：Python 3.13.5，SymPy 1.14.0。没有调用 GitHub Actions、远程代执行或替代性的证明认证。

程序一（标准库 Fraction / isqrt 的精确有理算术）执行：
    python research_notes/prefix413_exact_crossing_certificate.py

PASS_PREFIX413_EXACT_POSITIVE_QUARTIC_FIRST_CROSSING
global interval: [3/4000, 97/50000], first-crossing bracket: [903411/500000000, 1806823/1000000000]
certified D(L)>0 margin lower=1538892223825362547516009792430462835334371596453366491706707057123/1044839527044155171452481437696000000000000000000000000000000000000000000000
certified D(U)<0 margin lower=30644204065380477158929291556356271720198044762594232450965483631/11356951380914730124483493888000000000000000000000000000000000000000000000
P(L)<0<P(U); primitive quartic coefficients: (411370922419157000000000000000000000000, 3406648973825365305852000000000000000000, 7207920358822113492588156702000000000000, -15929217691721140762689459588000000, -23522344829723509499221428663222123)
result: strictly decreasing branch gap on analytic validity interval, exact first crossover isolated

程序二（从五 Port 原矩阵重新反演 + SymPy resultant）执行：
    python research_notes/prefix413_independent_matrix_resultant.py

PASS_PREFIX413_INDEPENDENT_ORIGINAL_MATRIX_AND_QUARTIC_RESULTANT
resultant proportionality: 74837639237
port4: (1 - I)*(u*(-2 + 5*I) + 4*v*(-1 + I) - 2 + 7*I)/2
port5: u*(22 + 15*I)/8 + v*(5 + 9*I)/4 + 11/4 + 15*I/8

证明与验证范围：给出了 η∈[3/4000,97/50000] 的两支路准确全局极值和严格单调交叉，结合 PREFIX-412 的 η∈[1/10000,3/4000] 分支优势，严格确定了首次交叉为给定整系数四次多项式的唯一正实根，根隔离宽 10^-9。程序核对代数证书和原始矩阵系数；全连续域定理由证明中的数学不等式支持，不把有限计算当普适证明。

权限实读：GitHub 登录 awdawmip，enterprise-math 的 push=true；原生 em_control_tasks 返回 CONTROL_QUOTA，em_session_start 返回 STATIC_READONLY_SCOPE_DENIED，operation_sent=false。当前活跃 Owner 不可核验。本轮没有正式 CLAIM、Result/Review 或独立数学审阅，外部辅助静态模型也没有 P000 原生转移。

固定源：GLOBAL_KNOWLEDGE_V1 main@aea254fc09586929ff4c569d9201da6131eb03bf；Enterprise Math 研究输入 main@1cce3e5a5246da8660e995cc5ea67182785504ef。所有普通 GitHub 发布均属于保存作者侧研究证据，不代表正式数学 admission。

后继 PREFIX-414：首先确定 η≥97/50000 后是否发生第二次切换；从 η≥2001/1000000 时 C_v 约束自动成立的圆盘–二次条带支撑函数入手，证明负支路继续占优或构造反例。其后再允许 I₂、C_u 的非零噪声 ε>0，研究交叉面的代数稳定性与活跃边界变化。
