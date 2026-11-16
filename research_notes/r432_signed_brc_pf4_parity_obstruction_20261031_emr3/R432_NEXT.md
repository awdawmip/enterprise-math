# R432 接续说明（UNREVIEWED / NOT_ADMITTED）

本轮新定理：原始 signed BRC 辅助标量行的连续列左端四阶子式 M_(2k)<0 对全部 k≥3，M_(2k+1)<0 恰在 k≥49；小奇行 k=2..48 的该子式严格正，但不表示全行 PF₄。所有偶数 r≥4 与所有奇数 r≥99 非 PF₄。新增完整 PF₄ 两行：r13 与 r15；完整 r12、r14 均有且仅有3个四阶负子式（有限支撑归约范围）。全部不自动推广到 X6 / 三维切片。

下一研究单元：完整分类奇数 17≤r≤97 的内部/非连续四阶 Toeplitz 子式，寻找首次出现的负例或证明剩余奇数行 PF₄。优先直接重用 R432 的奇偶 Catalan b_s 多项式、R431 的有限支撑归约、R430 的窗口扰动工具；无必要重复 R431 r7/9/11、R432 r13/15 的完整验证。若声称无界 PF₄，必须处理所有形状，不能从单个正的 M_r 外推。

复算：运行 R432_VERIFY.py 生成精确证据；C++ 源 R432_EXHAUSTIVE_PF4.cpp 对 r5..15 接受正 gcd 归一化的整行 a_h 并输出精确4阶统计；r12..15 的低阶整数 Bareiss 原始证明记录在 R432_FINITE_EVIDENCE.json。

固定来源：GLOBAL_KNOWLEDGE_V1 main@6d641db765283606da81862be0e2eb4336d27878；Enterprise Math main@bc570ffbe807936cf285d4d0584e5fb54c84bb9d；前沿 R431 commit 1914babcf902767710ebeeca9344767707dd77c2。

本轮 em_status authority=false，owner 查询 CONTROL_QUOTA，原生 CLAIM/Result/Driver review 未取得。禁止将作者侧数值证明冒充正式任务接纳。P000/ACTIVE 未修改。