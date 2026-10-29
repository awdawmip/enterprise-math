# R373｜作者侧研究结果与接续入口

研究来源：BRC 原始十二支路带符号 K/J；R370–R372 已经研究 r1..r4，接续第五余阶。GLOBAL_KNOWLEDGE_V1 在本轮固定 main@75c30a747792c0e33c7116eb01db2f77d00868da，Enterprise Math 规范基线 main@4dab5fcd7d61f67f721f21b2f6251b4eede4750c。母目标仍是独立检验 BRC 核 PF2/TP2 的准确边界，不改变 P000 与 ACTIVE 心跳世界六维 X6 残差保真约束。

数学结果：仅改 K3[t²]=-8(1+θ)，对所有 θ>-1，第五余阶 11 点有限原始 D 观察系数满足 PF2 当且仅当 -1<θ<=ρ5，ρ5 为 c0 在 (133/125,213/200) 的唯一实根。26组精确有理 Bernstein 全区间严格正性，共332个正证书系数；原始 D 与 R369 异路符号核验 11/11 一致。θ=15/8 时最高五个 c6…c10 零点阶数为 2,4,6,8,10。前五余阶 PF2 共同参数域仍 (-1,τ1]，此项合并依赖已发布 R370–R372 作者侧数学结论。

本目录研究文件：R373_PROOF.zh-CN.md 为完整论证；R373_reproduce.py 为现有 PR 源码可自行执行的无外部数据版本；R373_independent.py 为第二独立算路；R373_EVIDENCE.json 为摘要及严格有理区间证据。运行 python research_notes/r373_signed_k3_corank5_phase_20261029_emr3/R373_reproduce.py，随后运行 R373_independent.py；只需要同 PR 已存在 R346_verify.py、R369_check.py 与 SymPy。原作者另保存精确完整 JSON 十一项多项式及原始执行日志；此 GitHub 版本源代码可重算全部十一项及区间证书。实际本地原作者检查 PASS，不代表新 GitHub 版本已在远端 CI 运行。

本研究是原生 Claim/Result/Driver 数学接纳以外的作者侧 UNREVIEWED / NOT_ADMITTED 可移植材料；有限观察不自动外推为全 k 多项式、完整 PF∞ 相图、二维 TP2 或原生 X6 动力学定理。没有对另一研究员成果进行独立审查的权限。无需重算 r1..r5 的已发表有限相图。下一研究单元：r6 的13项原始 D 有限观察、完整有理参数区间 PF2 证明；先验证已有共同区间 (-1,τ1] 是否稳定，再隔离首个可能失效阈值。独立审查 R363 在 θ=15/8 的抽取与次数退化。
