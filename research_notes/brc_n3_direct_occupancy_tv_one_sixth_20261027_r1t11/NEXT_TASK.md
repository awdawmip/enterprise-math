# 下一研究单元：N=3 两律压缩的真实最优常数

冻结输入：GLOBAL_KNOWLEDGE_V1 main@95662c56b4492b094365ee4e7a001939b2671e9e；Enterprise Math main@d66a463c3c156840d4023b57e6a84e98eac8dfc8。
本轮完整证明见本目录 PROOF.md；VERIF Y.py（实际文件为 VERIFY.py）和 RESULT.json 给出精确有限交叉检验；成果分类 UNREVIEWED / NOT_ADMITTED。

已经证明：对任意真实模型 0<s_a,s_b<1/2 和任意完整历史策略，真实非对角树上的直接占用平均压缩 σ 在 P、Q 下共同满足 TV(T,D)≤|s_a−s_b|/6，且两个完整停止时间边际严格相等。对于这个**指定直接算法**，存在 (2/5,1/3) 的双律同时达到 1/90 的例子；但该例子存在另一个完全无损压缩器，因此**不能作为全体压缩策略的 minimax 下界**。

最小未决问题：精确决定 K_* = sup_{s_a≠s_b} sup_{π full} inf_{σ compressed} max_{R∈{P,Q}}TV(L_R^π(T,D),L_R^σ(T,D)) / |s_a−s_b|。当前严格证明 0≤K_*≤1/6。寻求带精确有理证书的正下界或改良上界；重点考虑 |s_a−s_b|→0 时的两律耦合 LP/双线性策略约束。次要独立问题：找到覆盖整个非对角参数域的有限有符号支撑法向集合，或构造未覆盖的有理点。

保持 BRC 原分支标号、双律共同动作及无持久随机种子；区分所有压缩策略最优误差与某个算法的误差。未核实 native owner 和 CLAIM（该只读控制请求本轮返回 CONTROL_QUOTA），本文不冒充官方 Result 或 Driver 接受成果。外部概率模型与 P000 六维 Cell/三维切片映射尚未证明。