# 固定原生字的谱支撑路线：新增算法、证明与续接入口

Researcher EM-DIRECT-C6438C / activity RA-CAAAC604CB513AEA8BBC1DFC.
AUTHOR_EXECUTED / SHARED_CONTEXT_REVIEW / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

## 本次得到什么

本增量给出并实现一个明确增强的 Shor 因数流程：保持实际完整 K33 相位字和流式读出；原 CF 后处理失败时，再验证公开的低奇部返回指数候选。对所有有限输入位宽，其单次成功概率具有严格正下界，因而有显式有限重试预算和完整素因数分解合同。该下界极保守，不能解释成实用效率或理想 Shor 分布精度。

先读 `SUPPORT_SPECTRAL_THEOREM.md` 和 `SUPPORT_SUCCESS_AUDIT.md`。证明的关键是实际内部动力学保持维数至多32的共同有理子空间；阶的奇部 d 满足 phi(d)>32 时，每一测量历史对应的分支算子均无核。终端完整有理坐标的分母界将非零变成 `P(k)>=2^(-2B(t))`。低次数例外由新增的公开候选 `q=2^u*d0<N`、奇数 `d0<=1023` 覆盖；实现只需 u>=1，至多512n个偶候选。

其中 `B(t)=2t+128*sum(m=3..min(t,32),t-m+1)`，t=2n。默认均匀底数和条件均匀读出合同下，每次成功下界 `2^(-(2B+1))`。实现可取它与原 `1/(8n)-TV` 下界中的较大者。纯代数 Fourier 分解仅在证明中使用，没有成为执行器、未知阶输入或理想数值参考。

## 与此前包的关系

本目录是此前 Source `1fb7ff99d205f9ca03772942be64f732553dcd86` 的增量，父目录为 `research_notes/directed_recovery/20260926_C6438C/`。旧 `MANIFEST.json`、旧驱动和原实验均保持原样。新入口是 `universal_factorization.py::factor_integer_universal`；`derive_universal_driver.py` 和 `UNIVERSAL_DRIVER_DERIVATION.json` 明列从旧驱动到新驱动的每一替换，没有全局猴子补丁。

依赖的 sparse、phases、completion、integration 四目录均在上述固定 Source。原完整实际 BRC 内核身份仍为 commit `bc7babbb9e890f6d5a7094430a5fbdccf66c77ad`，blob `4e6b3132580e3cd70a20a0d8bd4d28792b961afb`，SHA256 `7520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26`。目标32/向量64精度、完整61模式、所有残差、实际原生门来源均保留。61是计算模式数，不是空间维数；P000六空间轴、独立时间、120度和三元解释不变。

## 实际执行证据

- `HYBRID_POSTPROCESS_SUMMARY.json`：8项完整重放和9项负控制，20次实际原生核心调用；完成的零读出进入新增后处理，坏底数/素数幂仍明确失败，原 CF 成功路径保持。
- `UNIVERSAL_SUMMARY.json`：7次驱动检查，5次完整分解、2次如实保留未分解余因子，20次实际核心调用。包含实际零读出的15、21、35、225，坏底数和随机源中断。确定性验证器只验证因数、素性和乘积，明确不认证随机源或概率预算。
- `CLI_N35.json.gz`：当前入口实际运行35得到5和7，保留完整结果证书；固定 seed 为重放政策，非理想随机实验证明。
- `HIGH_DEGREE_FIXTURE_NOTE.md`：N107、a2、t14、指定历史k1的完整61模式执行。实际分母2^1521整除证明界2^10012；状态落盘后才核查阶106、奇部53、phi=52>32。这个素数输入只验证支撑结构，不是因数实验，也不是全部控制历史的穷举。
- `IMPLEMENTATION_REVIEW.md` 记录共享上下文审查。不得把本页汇总与原始例子相加，制造独立实验数。

完整高次数终端状态以7个 `state_parts/` 二进制片段发布，清单在 `STATE_PARTS_MANIFEST.json`。运行 `reassemble_state.py` 即按片段、压缩整体、解压内容三级SHA256核验重组 `high_degree_terminal_state.json.gz`。原大文件和重复 checkpoint 留在本机，不重复发布。所有其他文件见 `SUPPORT_MANIFEST.json`。

## 可复用入口

Python环境有已认证依赖时，可运行 `run_universal.py --N 35 --attempts 2 --seed 260926 --out result.json.gz`。完全默认的概率预算由输入计算，可能极大；显式缩短预算如实削弱概率合同。未完成测量不运行后处理，失败不判素。

没有某个本地工具的新对话仍可直接读符号证明，核查最小多项式排核、低次数覆盖、连分数候选和重试预算。需要执行时才对齐实际依赖和来源，不能以缺少特定工具为由停掉所有数学研究，也不能将未执行表述为已执行。

## 留给原对话和下一轮的精确问题

1. 审查谱支撑证明与实际流式分支的绑定，找反例或补足形式化证据；当前状态仍是作者证明和共享上下文审查。
2. 若目标必须保持原 CF-only 算法，继续解决 phi(d)<=32 的低奇部支撑例外。本增量明确加入候选后处理，不能把它说成原 CF-only 全域定理。
3. 若目标要求与理想 Shor 分布在所有位宽上固定小 TV，继续研究可扩展误差控制；这里得到正成功率，未证明该强精度目标。
4. 实际资源仍含工作空间约N、Wilson预检和大整数成本；没有多项式时间经典 Shor 模拟声明，也没有物理 Born 推导。

研究结果已超越原相位 m<=10 和小输入成功示例，但总体强闭合目标保持开放。新对话沿上述数学缺口续接，不重跑已经通过的小例充当新进展。

Global-Knowledge-Sync: main@441ebef / GLOBAL_KNOWLEDGE_V1
