# R347 | BRC Newton 内区 TP2：第302条无界余阶带

2026-10-28（Asia/Shanghai）。状态：AUTHOR_SIDE_EXACT / CONDITIONAL_ON_R330 / UNREVIEWED / NOT_ADMITTED。

## 1. 来源与数学对象

本轮固定同一私有 GLOBAL_KNOWLEDGE_V1 canonical main 快照 fa7202d5e3a897cc6e295d9da5c1341a06c3bb16，已读 00_BOOTSTRAP、OPERATING_MANUAL、P000_STARTUP（原始 P000 Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc）及 ACTIVE 世界观。项目 main 来源为 178b13bf780c92917be8eb49b414df3743f30886。旧研究 R346 不可变提交为 37516cc5bb8d72098ce25f2d64881ec5da4279cd、Draft PR #1592。

只研究完整十二项有符号 K/J 有序六边 BRC 辅助组合递推，B_0(t)=1+t；具体 K、J 与递推函数沿用 R346 已发表 R346_verify.py。保留原始乘积及所有正负项；本轮的输出观察仅限精确代数系数、Newton 差分和二阶行列式，未建立到心跳世界原生六维 X6 Cell 动力学的映射。P000 和 ACTIVE 世界观不变。

定义

D_{q,k}=sum_{v=0}^k (-1)^(k-v) C(k,v) 2^(q-v) [t^q]B_{q+v}(t),

M_{q,k}=D_{q,k} D_{q+1,k+1}-D_{q,k+1} D_{q+1,k}.

**R330 载重前提（尚未独立审查）：** 对所有 r,u>=0，D_{r+u,u}=5^u H_r(u)，其中 H_r 为有理系数多项式，deg H_r<=r。仅凭有限插值点不能证明此前提。

定义 L_r(v)=5^r H_r(v)，Q_r(v)=L_r(v+1)L_r(v+2)-L_{r-1}(v+2)L_{r+1}(v+1)。将 q=r+k 代入定义，精确得到

M_{r+k,k}=5^(2k+1-2r) Q_r(k-1), r>=1, k>=1.

## 2. 新的有限精确证书

用 Python 任意精度整数和 Fraction 从原始十二项带符号递推构建 B_0,...,B_911；截断保留系数次数 0,...,607 足以覆盖全部所需抽取。只重新计算必要的 H_300,H_301,H_302,H_303（不假称重算此前全部301条带）；每个 H 的 r+2 个节点中末级有限差分为0，r+1个 Newton 系数全严格正、最高系数为 6^r，5^r H_r 的 Newton 系数皆为整数。额外节点属于有限核验，不证明全指标次数界。

对 Q_301 的603个完整 Newton 差分，规范序列 SHA256 = 242f508cdf355e238c7052d3e7bb66b71754d5e474c85e617328210f951c4484，与 R346 不可变证据完全一致。

新计算 Q_302(0),...,Q_302(604)，求 c_{302,i}=Delta^i Q_302(0), 0<=i<=604，**605项严格正，零/负均0**，最小值为 i=0。按整数文本 302,i,decimal_coefficient 和换行依次串联，SHA256 = b7a222c6840358ba7d92943a376e58dc6a3dfe08e14a9acf3eaf8f3a404069df。

另验证最高差分：c_{302,604}=30^604 Catalan(302)=30^604 C(604,302)/303。该恒等式与来自旧 R330 次数界的最高阶系数关系一致；本轮对其做了精确整数核对。

本轮实际执行的程序为 R347_verify.py，Git Blob SHA1 = 710296e71176ff6c694a1ccc592cf3d5fa890952。程序复用同一 PR 分支的 R346_verify.py，生成完整605行 R347_Q302_COEFFICIENTS.txt 和 R347_EVIDENCE.json。证据摘要见本目录 R347_EVIDENCE.json，完整系数和执行日志另在本轮研究附件保存。

## 3. 条件无界定理与其边界

**如果 R330 全指标恒等式和次数界均成立**，则 deg Q_302<=604。对任意非负整数 v，Newton 恒等式给出

Q_302(v)=sum_{i=0}^{604} c_{302,i} C(v,i)>0，

因为 c_{302,0}>0，其余 c_{302,i}>0，且整数二项系数 C(v,i)>=0。代回 M 的抽取关系，再继承 R346 的前301条带，得到

M_{q,k}>0，对所有整数 k>=1、1<=q-k<=302。

这里“无界”仅表示固定余阶带上 k 可以无限增长；所有余阶同时无界的 TP2 仍待解决。结合 R341 的正比值望远镜及内区 D 正性证书，在合法 1<=k<l<=q<p、p-k<=303 的区域内相应二阶子式也严格为正，条件同样依赖 R330 和既有证书。

**未证明** R330 原始载重引理、整个二维内区 TP2、心跳世界 X6 动力学对应，亦未取得独立数学审查或项目 Source admission。

## 4. 可复现与接续

在同一 PR #1592 分支执行：python research_notes/r347_unbounded_interior_tp2_corank302_20261028_emr3/R347_verify.py。仅使用整数和有理数确定系数符号，无浮点符号判定。校验前301带中第301带的原 SHA256；运行后输出605行完整系数及摘要。

下一最小研究单元：构造 H_304 与 Q_303 并检验607项完整 Newton 差分；同时真正独立审查 R330 的全指标有理抽取与次数界（找证明或反例），寻找 r 与 k 同时增长的正锥机制。若某 Newton 系数非正，区分充分条件失败与实际 M 变负。

本轮原生 em_control_tasks 返回 CONTROL_QUOTA，未权威确认活跃 Owner，也无原生 CLAIM、Source Result、Driver 接纳；GitHub 存储不授予上述权限。研究员标识仅为本轮本地作者来源 LOCAL_R347_4147DCF1CA。
