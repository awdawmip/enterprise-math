# PREFIX-290｜从最小五坐标C4-BRC测后载体到真实H_n Detector

来源与强度：PREFIX-289作者侧证明 https://github.com/awdawmip/enterprise-math/blob/e01f0785cdd1ed3b9882704cc0556361b60b404d/research_notes/research6_prefix289_minimal_brc_poststate_20261027/PREFIX289_MINIMAL_POSTSTATE_AND_RESET_LOSS.zh-CN.md ；代码、结果在同目录。状态 UNREVIEWED / NOT_ADMITTED / NATIVE_H_N_BRIDGE_PENDING。

## 母问题
在真实六维原生空间及独立时间的心跳状态 H_n 上，是否存在有原始Source与合法 model_law_id 支撑的二值Detector，其已准备输入、全部测后结果、材料/动量/场更新、来源/Port历史与边界/损耗/时间规则，可与此前C4-BRC双Port仪器形成保持未来操作的类型化对应？不要将来源寄存器的复线性五维数误认为X6空间轴。

## 固定精确输入
三来源C4振幅 a=(a0,a1,a2)∈Q(i)^3；q∈{1,i,-1,-i}；八个标签 (σ,j),σ=±,j=0..3；V_q(a)_(σ,j)=(q a_j+σ a_(j-1))/2，越界0。事件 E={(+,1),(-,2)}；二bin J_q(a)=((a0+q a1)/2,(q a2-a1)/2)，A_q=J_q*J_q 的效应本征值为0,1/4,3/4。

已证明最小“等距输入+正交二结果+全部测后分支”抽象载体是 C²_E⊕C³_Ec 共5个复坐标，Ec必须保留带来源交叉BRC的Gram G_q(x,y)=<x,y>−<J_q x,J_q y>。若强行将八bin测后状态正交回收到旧三来源输入像，E/Ec的每分支质量损失都恰为 (3Z−|<a,(-q,1,conj q)>|²)/16。q=i、a=(1,i,1)、b=(1,-i,1)：P_E分别0、2/3；b的每分支旧像回收质量损失1/2。

## 下一可执行研究单元
1. 查当前原生Source真正合法的 model_law_id、已完成准备的 H_n 对象、Detector接口与真实输出字段（六维Cell、材料标签与动量、完整场、branch/来源、边界、时序）；明确区别于 Stage50 的重新准备输入/离线来源统计。
2. 若真实合法Detector存在，逐字段给出从 BRC 的8bin或5坐标带权载体至 H'_n 的映射与后态律，明确各Port概率、来源相位/历史、损耗到何处、未来操作是否保持映射，使用真正Source执行一组最小见证，保存model_law_id和回执。
3. 若合法Detector或再准备接口不足，先精确列出缺少的状态字段/操作类型，在实际允许的操作代数内构造严格“不可表示/未闭合”证书；不要将形式模型的不能封闭误写为自然界绝对不可能。
4. 若某个Source声称旧三来源重置保质量，使用上述非负、普适锋利缺口直接测试它：必须给出未丢失的正交结果载体或声明额外环境/资源账本，不能把旧像投影之后的质量当成完整后态。

## 不重做与返回标准
前序PREFIX-287、288、289的形式定理与各自已执行有限枚举不重复当作新原生实验。本次成功是：实际有来源的合法 H_n Detector/模型操作及真实最小实验；或严格基于原生Source操作合同的禁止/类型不闭合论证和精确后续接口条件。仅GitHub保存、纯形式BRC后续计算、身份登记或任务回执不是 H_n 原生桥证明。保留 P000、ACTIVE 世界观和真正 owner/CLAIM、独立Driver数学准入边界。

需要真实授权的原生会话/CLAIM当前未验证；不能占用其他owner。
