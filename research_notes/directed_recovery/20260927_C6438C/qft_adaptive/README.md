# QFT：可认证的自适应门简化与活动窗口计数

状态：作者实际有界执行与符号成果，SHARED_CONTEXT / NOT_ADMITTED。活动 RA-CAAAC604CB513AEA8BBC1DFC；一般 QFT/Shor 去量子化目标继续进行，尚无一般分解复杂度突破。

本轮把“可以降低精度”推进为一个可执行的充分条件：使用实际低策略前缀的完整 Gram 协方差，认证下一步简化门的作用误差；只在逐路径总误差预算允许时采用，否则使用原门。过去实际采用的门序列保持不变，并可从公开历史和证书重演续接。该方法不需要枚举全部历史来执行预算策略，但目前计算协方差仍可能很贵。

原型在既有实际 direct-word bank 上省略一个完整反馈词，保留所有符号和残差；它不是其他对话 RP1 的 b8/b64 精度实验。4 个 t=4 输入的完整历史—工作标签联合分布均通过检查，共 448 个前缀检查。N=21,a=4 的实际 TV 约为 0.02563，低于预设 1/3 预算；其他三个输入为零。零值有末步陪集分离的适用解释，不代表一般门省略精确。10 个拒绝控制、序列化重演及预算中断后同一步重试均通过。

另一条数学路线扩展了前轮零前缀计数：当所有非恒等的实际算子集中在宽 ell 的窗口内时，窗口两侧的长恒等区间可以压缩为 10 个固定次数的 floor moments。证明给出 O(2^ell ell) 个矩阵层，加 O(2^ell log(R+1)) 个整数阶段，另计周期/地址发现、原生词、整数位宽和证书费用。实际算术模块通过 80 个 moment 等式与 4 个窗口权重检查。尚未完成全矩阵集成，也没有证明一般或典型历史具有短窗口。

成本结果需要与正确性分开：完整 Gram 认证会增加工作量；floor-moment 的这组小例总算术成本也高于短枚举。当前成果是有严格条件和实际证据的优化工具，不能据此声称端到端加速。费用见 adaptive_execution/COST_NOTE.md 与 nonzero_structure/TYPED_FLOOR_EXECUTION_NOTE.md。

阅读 EXECUTION_NOTE.md、precision_theory/ADAPTIVE_NATIVE_PRECISION_INTERFACE.md、nonzero_structure/ACTIVE_WINDOW_FLOOR_MOMENTS.md，然后由 CONTINUE.md 选择下一项数学工作。完整证据可从 readable_evidence/INDEX.json 无损恢复；原始修订前验证也保留。任何对话可据此继续证明、审查、对比或实现，不依赖某个驾驶员的私有记忆。

Global-Knowledge-Sync: main@06788df / GLOBAL_KNOWLEDGE_V1
