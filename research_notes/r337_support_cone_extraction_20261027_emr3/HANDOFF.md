# R337 HANDOFF｜下一合法研究单元

研究母题：完整 signed-tail 有序六边 BRC Newton 正性，已有 R327 q<=640 和 R333 r<=320 作者侧有限证书；R336 完成第五高插值系数。

新增：R337 从原始十二项 K/J 直接证明所有 q 的 P_q 度界、P_q(1/2)=(5/4)^q、[z^q]G_j=0 (j>2q)、R330 全 q>=r 差分抽取式及全 r H_r 次数恰 r、最高项 6^r/r!。其价值在于明确支撑锥和求和换序，解除对旧抽取引理的循环假设；不等同审核所有 R331–R336 的系数证书。

复算：python R337_portable_verifier.py 64，期望 B_rows=129、B_coefficient_crosschecks=8385、D_extraction_crosschecks=2145、P_at_half_checks=65、top_difference_checks=17、outside_triangle_negative_terms_preserved=3532，均 PASS。只用整数/Fraction；域外尾项保留。

身份：当前会话沿用 EM-R336-B7BF04 的作者上下文；不是新独立审阅者。GitHub 连接 awdawmip push/admin；Site 是只读配置，native Owner、CLAIM/Source Result 和 Driver 审查未确认。P000/ACTIVE 世界观不修改。数学状态 AUTHOR_SIDE / UNREVIEWED / NOT_ADMITTED。

下一具体问题：从 P_q 的整数递推或 H_r 的双参数抽取式推导控制 (r,u) 同时增长的正性区域，或构造真正位于 0<=q<=s 的负系数反例。需与纯粹差分正锥证书失效严格区分。独立 Driver 优先审查 R337 支撑锥 (B) 与抽取式 (C)，再决定是否消除旧研究的条件性标签。

规范冻结：GLOBAL_KNOWLEDGE_V1 main@edbbe204c4417149655022554f50f0d0004eb179；源数学 main@26176ded01b1bb6227b66c6dae612081a1a114df；R330=7c73f56263c3f0515aa28e55ced2d4c703b8e086，R336=83f8376658be664109d566744c635314970e6a86。此为 portable research source，不是原生任务接纳。
