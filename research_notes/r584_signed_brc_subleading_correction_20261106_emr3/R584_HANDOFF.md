# R584｜研究交接与恢复前沿

冻结科学输入：R462 signed BRC @ 18783e01e3646c72b7aab3b16d3f565e83e6446f；R582 @ 832b1bb9a094f91454b46170150332727c79fff6；R583 @ 1622f5fd51e6359a5cd39de5185e5165db2e74b7。

新结论：对全部整数 m>=1，修正系数 b_m 精确分解成 -(3/2)(8/3)^m + 2^(m-2) + E_m；E_m>0，有显式中央二项式下界，且 E_m=(2^m/sqrt(pi*m))*(2-5/(2m)+O(m^-2))。完整演算在 R584_PROOF.zh-CN.md。R584_VERIFY.py 与 R584_EVIDENCE.txt 记录 m=1..96 的精确交叉核对。

此结论仅关于冻结 signed BRC 经过辅助标量倒谱观察者得到的形式系数 b_m。有限 k 的谱最小零点/复环域计数与原生联合分支保真桥仍是开放单元。

当前需要的下一项：在固定复域内对 P_k(t) 建立可读回零点计数或 k,m 联合余项，并与已证明的 b_m 双尺度结构区分；不重复 R582/R583/R584 已完成的系数恒等式。

交付位置：Draft PR #1708 的作者侧研究文件；是否取得原生 CLAIM、Researcher-ID、Owner 回执及 PR Head，以本轮实际控制查询为准。GitHub 作者身份由连接认证，GitHub 署名不替代 Source session 或权限。独立 Driver 审阅待完成。
