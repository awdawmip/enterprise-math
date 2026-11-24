# C90 阅读与复算

## 阅读顺序

先读 [C90_RESEARCH_NOTE.md](C90_RESEARCH_NOTE.md)，再按问题进入下列证明。

| 问题 | 完整证明 |
|---|---|
| 原整数目录上全多分支的有限分离极限 | [joining/FULL_MULTIBRANCH_LIMIT.md](joining/FULL_MULTIBRANCH_LIMIT.md) |
| 外部 joining 输入的准确假设与所用结论 | [joining/RATNER_JOINING_INPUT.md](joining/RATNER_JOINING_INPUT.md) |
| 全部六支、15 对斜率横截及谱差无原子 | [rank/GLOBAL_PAIR_TRANSVERSALITY.md](rank/GLOBAL_PAIR_TRANSVERSALITY.md) |
| 端点到内部位置的统一公式 | [root/MATCHED_POSITION_LAW.md](root/MATCHED_POSITION_LAW.md) |
| 第一低精度过渡、准确平台、第二过渡 | [root/TRUE_LOW_PRECISION_TRANSITIONS.md](root/TRUE_LOW_PRECISION_TRANSITIONS.md) |
| 仿射空窗核 E2 及 Xi 的准确式和展开 | [joining/AFFINE_VOID_KERNEL.md](joining/AFFINE_VOID_KERNEL.md) |
| 唯一简单折叠零点、正规相遇弧与局部倒数主项 | [tail/TRANSVERSE_ARC_AND_LOCAL_TAIL.md](tail/TRANSVERSE_ARC_AND_LOCAL_TAIL.md) |
| 固定边界楔区的加权 250/117 指数及准确系数 | [tail/WEIGHTED_BOUNDARY_TAIL.md](tail/WEIGHTED_BOUNDARY_TAIL.md) |

主证明的项目内核查见 [root/REVIEW_OF_MAIN_THEOREMS.md](root/REVIEW_OF_MAIN_THEOREMS.md)。joining 和 rank 目录另有对应的交叉核查记录；这些协作者共享冻结输入，不是外部独立同行评议。

## 准确计算复算

在本目录运行，Python 只需标准库：

~~~bash
python3 rank/certify_six_branch_rank.py
python3 tail/certify_transverse_fold.py
~~~

第一项隔离 h=0、U=1/250 的完整六个物理正规根，证明全部 15 个约化双斜率行列式不含零；它使用同目录的 c89_interval_kernel.py，后者字节继承 C89 准确程序内核。

第二项准确隔离简单折叠交点，认证 P/K 面符号、导数和另外四支的谱间隔。两个程序均以 Fraction 和向外舍入的有理区间承担接受判断；显示浮点数只作阅读。程序会在自身目录重写相应 JSON 证据文件。

本轮已实际执行两个程序并通过其接受条件。书面解析延拓、完整 joining、coarea、加权渐近和 Haar 核的几何证明均不由这些有限证书替代。

另有一项准确多项式核查，需要 SymPy：

~~~bash
python3 rank/verify_fold_polynomial.py
~~~

它先明确清去有理分母，再用整数系数多项式展开核对 dN_d=A T_A、K 的 Q 因子以及五个分组系数的导数恒等式。实际 7 项全部通过，输出为 rank/fold_polynomial_verification.json。导数不等式及全折叠唯一性仍由书面证明承担。

本轮运行环境为 Python 3.12.14；符号核查环境为 SymPy 1.14.0。

## 来源与归档

SOURCE_REFS.json 给出本轮规范读取快照、继承科学来源、实际外部输入和证明状态。SHA256SUMS 绑定本轮研究文件；它自身不纳入自己的摘要。

完整导出包还含 inputs/C89/，是经 SHA-256 核对后恢复的冻结 C89 证明树，连同其 inputs/ 下的 C81–C88 所需材料。原来的相对层级保持，C89_PUBLICATION.json 保留旧发布依据。C90 中对“C89 的 inputs/C82/……”之类文字引用可在该树下找到。

仓库保存本轮新增科学文件及必要程序内核，继承证明仍引用冻结提交；导出包中的额外输入副本仅为离线阅读和复算。C90_PUBLICATION.json 在发布后记录实际源提交、Activity checkpoint 和全局进展事件；保存回执不承担数学证明。

## 范围

主定理读取原 H(0,1) 的三次读数，并要求 c^(1/3)<<B<<c。低精度推导先取库存极限，再研究曲线的 L、τ 参数。局部 1/τ 系数与固定楔区 τ^(-250/117) 都明确给定源区域；全域精确尾部仍开放。未将连续三谱相遇弧宣称为原整数准确读数碰撞。
