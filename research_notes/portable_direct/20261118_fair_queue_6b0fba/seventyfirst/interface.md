# 两条原 PASS 路径在同一个 STAR 读出上恢复三轴位移

本题为 RS-X6-UPPER-STRUCTURE-INTEGRATION（TP2-C7F31A8D520B49E653F6）；11月17日交接要求消费真实五上游而不以裸 S6 的原始步枚举代替原生准入。该共同片段用原有 6 维整数位移、原三轴散射及观察图，不作全原生联合状态的笛卡尔积。各冻结交接及其准确遗留问题见[五项上游的冻结回执](frozen_upstreams.json)。

## 来源

以下路径均相对于 enterprise-math 提交 e7b9fb5084f93a9b2dbc16225629b667fb7bf46c；interface_checked.json 依下列顺序含每个文件的 SHA-256。

| 原文件 | 行号、实际接口 |
|---|---|
| experiments/x6_network_event_ledger_v29_20260906/check_event_order_holonomy.py | 36–54 名字/评分、56–71 PASS 前件和起始筛选、72–93 原 run 与两路具名末帧；git blob 4d3dd55915d165082ac5b856e3a8353a9ba23f21 |
| experiments/x6_nonfcc_observer_switch_v42_20260906/check_nonfcc_observer_switch.py | 8–23 固定 FCC 列和图册、47–57 mv 和16/4分裂、116–123 实际 even edge_lift；blob 2a8c8c804c6d4b0a4e0919f62235e58ccb583e4e |
| experiments/x6_triadic_atomic_scatter_v1_20260906/check_triadic_atomic_scatter.py | 43–57 有符号 Q、原 signed BRC 中间支路、60–81 同源三径共同枢纽；blob d5f6dfcfd0dedbe46feae3bc1b227185af417c2f |
| experiments/x6_triadic_rotation_v1_20260906/check_triadic_rotation.py | 44–49 同一原三元 Q，作用于具名六轴；blob c446d0327f9bf643d5796348ba46cafe96d2915d |
| experiments/x6_native_event_time_v1_20260906/check_event_time_markov.py | 5–18 $\Theta_r\to\Kappa_r\to\Theta_{r+1}$，37–39 两关系层/六个原始发生；blob df0df29327fe8c969ad9e4c758d5c7372ecd65cd |
| experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py | 20–34 有符号步长、同长路径 multiplicity；blob 300a96e3dc24bf6fff73743037a0347a8bc83176 |
| research_notes/X6_TRIADIC_INNER_C12_RELATION_CLOCK_V2_20260906.md | §1 逐令牌的有向闭合事件及原两层后继；blob e36897d0124c3987ad03ddcc6e400f2e13c6c1a7 |

额外来源包括 [11月17日交接](https://github.com/awdawmip/enterprise-math/blob/cb1651e00d35b46393ea622c51f60a586e5b23ec/research_artifacts/mcp/RS-X6-UPPER-STRUCTURE-INTEGRATION/MCP-c618a61189764f23846a391a08518a1a/0bf4c36b9aefb57d9d89/_checkpoint.json) 和 V1–V43 历史承接。每个上游的更晚原 checkpoint 已单独读取。

## 共同原输入与整数恢复

取既有 V30 参数，不动任何外场。原 run(AB) 给 $345\to134\to034$；run(BA) 给 $345\to045\to034$。逐边执行 V43 even lift（共有轴固定、离去轴换至新轴，余两轴另行对换），其在当前三轴上的限制逐步等于原 V30 slot transport。全部六轴排列分别为 $(5,2,1,3,4,0)$ 和 $(5,1,2,0,4,3)$，这里写六个依次的像。以原空间位移 $x=aE_3+bE_4+cE_5$ 为输入。支撑、起点、方向命名相同，比较两次独立准备同一个输入的运行。它们是原存在的算子对同一数学位移的作用，未声称 V30 的记账事件已经实际搬动了此物理位移。

定终点 T=034 是 STAR，固定原 FCC 列满足 $V_0=V_3+V_4$，$V_3=(1,0,-1)$、$V_4=(0,1,1)$ 是此平面像的整数基。原目标三轴槽分别读 $(c,a,b)$、$(a,c,b)$；经 $M_T$ 后，在 $(V_3,V_4)$ 下得 $(a+c,b+c)$ 和 $(a+c,a+b)$。故两路可见差是 $(c-a)V_4$（前减后）；当且仅当 $a=c$ 时等。每一路都有一维整核，合读的三个独立量 $(u,v,w)=(a+c,b+c,a+b)$ 的 Smith 因子 $1,1,2$，像是 $u+v+w$ 为偶数的子格。恢复式 $2(a,b,c)=(u+w-v,v+w-u,u+v-w)$。整数模 $q$ 的奇模无损，偶模恰剩一个公共半周平移 $(q/2,q/2,q/2)$。对规定的同一终点 STAR，任何更多只经有号轴置换再观测的操作均看不到该偶模二挠，因为半周等于自身负值，各列之和是 $2V_0$；这个量词不及追加秩三的另一终点仪器。单路不可能恢复全部整数，双路已经足够。若只问非负锥，两种核的差向量仍可同时平移成非负反例。

## 有符号三元与钟

原 $Q_S$ 将当前依序列出的 $e_{s_i}$ 送到 $-e_{s_{i+1}}$，支撑之外为恒等。AB 在三槽上是偶置换，BA 为奇置换。故在全部六轴上

$$ U_{AB}Q_{345}U_{AB}^{-1}=Q_{034},\qquad U_{BA}Q_{345}U_{BA}^{-1}=Q_{034}^{-1}.$$

两路在原散射核的 8 种具名正负号模式上分别执行了原 midpoint_options（内部调用签名 BRC）。搬运前后的每个原始选项一一对应，三径共同中点只出现于三个 INNER 选择。如果两路都用同一个约定的正向 $Q_{034}$ 作目标更新，不加手性修复则 BA 的方块失败。例取源正 $E_3$；沿 BA 先 Q 再搬运为 $-E_4$，先搬运再正向 Q 为 $-E_3$。

以各路搬运后的完整有序帧为该路零点，写 $\Theta'_k=Q_{034}^k\Theta'_0$。V2 将闭合事件定义为枢纽、入壳三元、出壳三元与逐令牌端口匹配的整体。记 $\Kappa^+_k=(c;\Theta'_k\Rightarrow\Theta'_{k+1};M^+_k)$，其中 $M^+_k$ 将各入壳令牌配至自身的出壳位置。同理 $\Kappa^-_k$ 对应 $\Theta'_k\Rightarrow\Theta'_{k-1}$，下标 $k$ 指入壳的正向相位。AB 把原事件 $\Kappa_r$ 直接送至 $\Kappa^+_r$。BA 则把它送至 $\Kappa^-_{-r}$，由入壳 $\Theta'_{-r}$ 指向出壳 $\Theta'_{-r-1}$。在目标的六个正向具名闭合事件中，没有一个保有这组入、出与匹配。[原有向闭合定义，§1](https://github.com/awdawmip/enterprise-math/blob/e7b9fb5084f93a9b2dbc16225629b667fb7bf46c/research_notes/X6_TRIADIC_INNER_C12_RELATION_CLOCK_V2_20260906.md)

令 $D$ 交换闭合事件的入壳与出壳，并将逐令牌端口双射取逆，令其在壳态上恒等。则 $D\Kappa^-_{-r}=\Kappa^+_{-r-1}$。搬运再施加 $D$ 后才得到正向目标十二态上的反向识别 $J\Theta_r=\Theta'_{-r},\ J\Kappa_r=\Kappa^+_{-r-1}$，满足 $J\tau=\tau^{-1}J$。原 $\tau$ 每次走一层，原前向入/出方向和令牌追踪均保留在未经 $D$ 的搬运里。这个额外的对偶是事件描述的变换；原固定正向钟未赋予反向演化的物理操作。

若两路都改用固定有序初帧 $(E_0,E_3,E_4)$ 标定，AB 的原三具名向量搬到 $(E_3,E_4,E_0)$，处于该标准轨道的第 4 相。BA 搬到 $(E_0,E_4,E_3)$，属于另一条具名序轨道，任何相位平移均不能补救。检查器分别对六起相追踪全部原子入/出对，共同枢纽相同也照样核对端口匹配。

## 上游各缺口

- **轴旋转**。此处实际搬运为 even edge lift，原有符号 $Q$ 是一个确定的三元端口选择。近期32图旋转商并未给物理准入或统一选择律。
- **三元闭合**。原 V1 三径、六有符号轴、共同 INNER 中点、完整原始分支选项可互核。近期 R762EI 的正终端 BRC 是不同的输入/未来；本例也未提供 TRIADIC_CLOSURE_E 的签名 Cell/Link/Port 许可。
- **时间**。关系钟 V1 的十二态与六相宏步可对照。近期多胞时间定律所需真实资源/源/目标/冲突守卫仍缺，没有把相位反转当作实际倒放。
- **非 FCC 图册**。读取给定 slice-supported 位移的有名 FCC 列，目标 STAR 合读有整数恢复。全程无需把不同行走路径上的固定 FCC 点认作同一原生位移；FACE/PATH 的实际物理三元准入仍见原交接。
- **内部通道**。源 V30 的 PASS_01、PASS_10 以实际合法评分路径产生具名切换，未推导选取 A 或 B 的原生 PF-10 物质机制，亦未将关系通道宣称为某一空间轴。

合同只含统计、代数、离散关系钟及源自约定的算子。两个完整物理实验的相同制备、原发射的独立重复性、统一原生时间及 P000 五项实际许可仍没有证书。无关联数据的另外分支不能靠给算子再乘三个形式标签而完成。

复算 `python interface_check.py --repo "$ENTERPRISE_MATH_ROOT"`。已独立检查 2,197 个有符号整数三元、模 2 至 16 的全部余数三元、两路径的所有六个有符号相位、16 个散射制备及完整 12 个关系钟状态。
