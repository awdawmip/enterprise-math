两个提案均只整理已接受的 Task 结果，挂在现有工具之下；不注册新 Tool、不提升 Foundation/Working Truth、不创建 Task 或 Native 评审票。own RA 的真实 Source readback 已通过 startup 活动门，明确不授 CLAIM/执行权。T6 原6077保持 FAILED，无 own run。本轮未运行 comparator、旧检查器、BRC传播或任何枚举。

1. Public129：保留完整 flagged first-exit / acceptance 关系和路径＋successor-closed cut 证书，作为既有 T8 关系观察、T12 Boolean有限闭包接口及 compose_relations 的精确使用合同。对 s 个状态，入口数4s，出口及接受通道4s+2，完整 mask 为 K=16s²+8s 位。任意有限 seam reentry 的 Join 与原始串接关系精确相等；空 segment、带两 marker 的空普通输入、接受后继续、零步/正步和停留转移分别保留。固定 mask fold 可在同一抽象字母表上纸面编译为至多2^K+1状态的只读单头 DMachine；完整表格至多(2^K+1)(|Σ|+2)项，预计算 O(2^K(|Σ|+2)s³)，没有免费 closure 或把位数当状态数。此指数表未物化。

   证书检查只需验证正路径和边闭切集，不要求重跑 reachability。原图 V=2ns+8s+2、E≤4s+4ns；全入口构造 O(4s(V+E))，紧凑简单路径证书 O(KV log V)位。现成 checker 接受有限非简单路径，实际费用必须按输入证书长度计算，不能把“存在紧凑证书”偷换为任意 JSON 都有该大小。check_certificate 单独只信任给定图，必须先以 expected_raw_edges/validate_shape 绑定机器和 word；原脚本的 assertions 必须开启。它不是一个已注册的泛型生产服务。Boolean摘要不保存未来的重数、来源、幅值或时间；offline(machine,word,certificate)谓词也不是 word-language recognizer。已有反例精确说明 forward-only 摘要及遗忘可写 bit 的模型桥为何失败，没有推出新的 EM 下界。

2. U2：在既有 t0.weighted_brc_cwm 下引用 conditional incidence 正则性及源标记两边 TOTAL 返回公式。给定一个 coherent、无重复、每端口正 degree 的3-uniform H，均匀选 incident triple 再均匀选三腿，destination-row/source-column 的 K(q,p)=n(p,q)/(3d(p))。Kd=d 且 reciprocity 成立；等12通道输入保持等通道，恰当且仅当每个 incidence-connected component 内 degree 恒定。分量之间无需同 degree。三异轴是排除 opposite port、赋予 turning 2/3 解释的额外 Task 前提，不能省掉。

   固定位置、等12通道源注入、共同ρ=12λ、无门/存储延迟并正确采用入射反向 -q 时，R_a^(2)=λ²[12+3∑_{q∈B_a}r_a(q)]。旧邻居计数式在一个布局只要求该集合的 row-sum 平衡；对所有单邻居朝向逐源成立才要求每行1。仅合并两源返回的条件 r(q)+r(-q)=2 更弱。该公式是 TOTAL，不是完整 count/total/dominant CWM 或联合源-端口/路径载体。结构 degree 检查可按 O(p+3m) incidence 计数；显式核有p²项和至多9m次共关联计数，精确算术、标签和原H保留费用另计，typed JSON给出参数化位成本，未把它说成已经实现的 all-H checker。

   现有 control_mass_matrix 接受真正的 ControlPacket/六轴 EffectHistogram，输出 SOURCE-row W，不能直接把 H 或 K 喂进去；若以后建立桥，须证明 W=K转置并满足其 observer/未来闭包前提。常 degree 不等于可安全合并 control states。原 field_prefix/transport_tables 仍没有自定义 H 参数。原生 G1/G2 action-lift/第三作用、G3反作用存储、G4边界时间、G5占位后继均未解决；静态固定算子唯一性不选择占位，也不覆盖动态算子变化。

详尽输入、输出、构造/检查器依赖、成本、失败域、已接受边界与贡献者见 TYPED_HARVEST_PROPOSAL.json。Public 原作者 EM-HODGE-7936BF、EM-PARITYSUP-9840AA及旧身份/上游贡献，新增环境执行者 EM-PUBLIC-7CDA51、R2支持及接受 Driver F73673均保留；U2原作者 CDFEA3、FA0C27/E1F2B6、协作者及接受 Driver653942均保留。本提取者EM-T6-BFF294的CONTROL/U2包装/T6非盲历史亦保留，不冒充新的独立终审。

精确来源：Public accepted DR9B722991/DFUCF33在Source4d514416…，实际TaskDONE读取在bfdeab630…；原证明16members在Source1f4a3b25…全部byte/SHA/Gitblob复核。U2 accepted DR74101518/DFUD517在Source6ee607a8…并有TaskDONE原回执；原INCIDENCE_REGULARITY及INTERFACE_CERTIFICATE在Source5877887e…复核。两个母目标均OPEN。25件输入的逐件locator和完整hash见 EXACT_ACCEPTED_INPUT_CUSTODY.json，两个有限catalog覆盖查询原件一并保留。建议保持 RESULT_ONLY，先供未来调用者引用；如要实现新的通用适配器，仍需独立冻结其类型、输出预算和真实审查。
