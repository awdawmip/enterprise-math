# R415｜研究交接（作者侧 UNREVIEWED / NOT_ADMITTED）

问题：原始带符号 BRC 辅助组合对象 H_(r,s)=binom(r+s,2s)[t^r](1-t)(1+t)^(2s)(1+t²)^(r-s)，D_(r,s)=H_(r,s)²-H_(r,s-1)H_(r,s+1)。

本轮已完成：固定 s=28 的全部整数 r≥29 均有 D>0。奇偶余阶产生两套完整精确有理正系数证书，57个分子系数和57个分母系数严格正。生成器 r415_verify.py、独立标准库验证器 r415_independent_verify.py、三角递推扫描 r415_recurrence_check.py、加权递推验证 r415_weighted_recurrence.py 和原始系数证据 R415_EVIDENCE.json 均位于本目录。证明与适用域见 R415_PROOF.zh-CN.md。证据 JSON SHA256：7cf60bf4d463546ea381d5b33437c0a1526006e64dd438cbc354ba8bb78fc6bc。

新增解析引理：对 r≥1,0≤s<r，(2s+2)(2s+1)H_(r,s+1)=(r+s+1)[(r-s)H_(r,s)+2(r+s)H_(r-1,s)]；从 R414 的 δ 三角递推按二项式权重清分母推出，独立于正系数有限网格。全三角表不自动为正，δ_(1,0)=-1。

下一单元：固定 s=29 以全余阶有理系数证书或精确反例判定；双参数总目标需在 s≥29, r-s≥129 区域获得解析证明（首个 (158,29)），并寻找无需逐带证明的加权递推机制。有限网格扫描 r≤320 的13,366点不证明全域。

冻结来源 GLOBAL_KNOWLEDGE_V1 main@4458ae7b7f0c3f1645083f0d64fd7d5e77f112e8，Enterprise Math main@93aed370045bcd8a1cc8685c3f593f0d4e375577，R414@9290f8145defff77a7a389ff7e6635d60d9ae70f。原生 gateway research_authority_granted=false；control_tasks CONTROL_QUOTA，Source Owner 未确认，没有正式 CLAIM/Result/Driver Review/数学接纳。P000/ACTIVE 不变；上游十二支路传递未独立复核。