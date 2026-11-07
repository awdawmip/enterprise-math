# R342｜精确 TP₃ 反例及 R340 独立重算 — PORTABLE HANDOFF

**本轮结论**：BRC Newton 阵列的内区 TP₃ 全指标命题为假。行 (8,9,10)、列 (1,2,3) 的整数 3×3 行列式为 \`-11584498914207849250816\`，而其 9 个二阶子式全严格正。这不是逐项系数 D 变负，也没有否定 R341 的内区 TP₂。Dodgson 凝缩说明需要额外约束 LR≥UV，本例该条件严格失败。

**运行并核验过的科学证据**：\`R342_portable.py\` 从完整十二项带符号 BRC 递推独立构造 D，使用稀疏多项式与两种整数差分算法，实际运行命令 \`python R342_portable.py\`。机器原始输出 \`R342_RECEIPT.json\`。验证域 q≤320：51040 个严格正内区相邻 2×2；50721 个内区相邻 3×3（50717 正、4 负、0 零），4 个负位置为 (8,1),(9,1),(10,1),(11,1)。原始 R340 内区/边界 SHA256 两个值逐字复现，完整证据在 JSON 中。附带复杂一点的本地交叉计算稿未发布，不是本 PR 的再现依赖。

**已读先行前沿**：R340 \`b86bef3ab7b4a8f6691b50b5ef84231c06d1b3ee\`；R341 \`cad0f5e5536d7d4dc651588a7d26ebab485acf2a\`，PR #1575/#1577。R341 望远镜恒等式独立于 TP₃。GLOBAL_KNOWLEDGE_V1 固定 \`main@8c69fa749d4acd22da35a009bcfc0affc8f2424c\`；项目本轮起点 \`main@94874d58a6b7aea806c7839ca2d8a7e05ec063ff\`。

**继续单元**：首先证明或者精确反驳无界内区相邻 2×2 \(M_{q,k}≥0,\ q≥321, 1≤k<q\)，然后用 R341 的局部—全局提升。分别解无界首内列和最左边界正性；可选研究四个低阶 TP₃ 负口袋的来源，但不能用 TP₃ 当全局正性前提。不重复已有 q≤320 完整运行，除非在真实冲突的独立审计中有必要。

**真实状态**：AUTHOR_SIDE / EXACT_VERIFIED / GITHUB_DRAFT / NOT_ADMITTED。GitHub 用户 \`awdawmip\`、admin 已核验。原生 owner 查询 \`CONTROL_QUOTA\`；没有本轮 native CLAIM、Result 或独立 Driver 接纳。P000 / ACTIVE 世界观均未改变，未推导完整六维 X6 物理对应。