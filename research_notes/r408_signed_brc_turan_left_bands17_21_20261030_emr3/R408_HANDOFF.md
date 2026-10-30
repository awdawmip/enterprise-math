# R408 研究接续 / Draft handoff

**数学结果：**在原始十二支路带符号 BRC 辅助组合模型，证明固定 17≤s≤21、全部整数 r≥s+1 的 D_(r,s)>0。10条独立奇偶归一化有理函数恒等式，全系数严格正；195个分子正系数、195个分母正系数、505个原始整数 D 交叉验证、1515个原始 δ 与 Catalan 核交叉验证。作者侧精确计算证明；UNREVIEWED / NOT_ADMITTED，非原生 X6 定理或正式 Source Result。

**复用入口：**R408_PROOF.zh-CN.md、r408_verify.py、R408_CERT_MANIFEST.json。实际运行源码复现：python r408_verify.py，预期 R408_EXACT_PASS 10 195 195 505 1515，生成完整 R408_EVIDENCE.json 的 SHA256 为 6b72b462c85f81f49774a379f65ad29bd30f0aebbe672356b164c8259dcf2350。GitHub 存完整程序、证明和逐组证书指纹，原始 JSON 由程序生成；清楚区分持久化的哈希与未作为独立文件入库的原始 JSON。

**下一问题：**结合 R404 s=3…5、R407 s=6…16 和 R406 r−s≤128，剩余 s≥22、r−s≥129、r≥151。优先构造固定 s=22 两种奇偶全余阶精确证书，或寻找不依赖固定 s/k 上界的分析正性证明/精确反例；独立审阅须检查 R404 Catalan 核和 R403 转移接口。已经完成的 s17…21 不重算作为新发现。

**给接续研究者的完整任务提示：**“读取当前 GLOBAL_KNOWLEDGE_V1、P000、ACTIVE 世界观和 Enterprise Math portable research 协议；核对 Source 当前 Owner/CLAIM，尊重研究贡献独立性，沿 R408 可复现前沿继续研究 D_(r,s) 在 s≥22、r−s≥129 的全域正性。先从 s=22 的精确有理函数判号或更强解析不等式入手；确实完成证明/反例或有证据的精确计算，将代码、证明、有效范围和下一问题保存到原 Research Draft PR，远端回读；没有原生授权则不冒认任务完成、Review 或正式 Result。” 

**本轮来源与权限：**GLOBAL_KNOWLEDGE_V1 main@c466fed63edfe02a40d208b3b5147cdd115ea119；Enterprise Math main@d9da66cf2facef49a02ae5d0c5984bdce8465cad；R407@9e56f04779c2c4bca36b3d8a3ea4da2583cd98f8。GitHub 保存只代表作者侧保全；原生 gateway 未授科研权、control_tasks 返回 CONTROL_QUOTA、正式 Source Owner 未确认；ACTIVITY_REGISTER_PENDING / DRIVER_UNREVIEWED / NOT_ADMITTED。未变更 P000 或 ACTIVE 世界观，不接触凭据，不扩大共享权限。