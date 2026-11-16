# R589 接续交接
母问题：R462 frozen signed BRC 联合十二支路结构保真；本轮仅分析 R576–R588 辅助极限谱，不提升标量辅助观察者为原生动力学。

已证：F 全部零点简单；远零点模长 r→∞ 时 Re ζ=r−¼log²(8r)+O(log r/r)，|Im ζ|=√(8r)log(8r)/4+O(log³r/√r)，|F'(ζ)|~(3/√2)r^(−3/2)；固定简单零点可通过 ε_k 和 m_δ 给出 |ζ_k−ζ|≤ε_k/m_δ。

实际核验：R589_VERIFY.py 的精确 Groebner 单位理想、导数分支不变性及渐近常数检查成功；R589_EVIDENCE.txt 为执行 stdout。R589_PROOF.zh-CN.md 是完整作者侧证明。独立数学 Driver 评审待完成。

科学输入冻结于 R462@18783e01e3646c72b7aab3b16d3f565e83e6446f，前沿 R588@0395d0169a57594054a40a893ca0345ee8fd2f2f。下一问题：建立联合 k/R(k) 的整函数系数逼近与局部根隔离，构造移动窗口 V_k 正型能量证书并检验 V_k=O(k^(−1/2))。

本轮 GitHub 作者身份 awdawmip；Native session_start FAILED/OSError；Owner WAITING_RESOURCE/EVENT_COLLECTION_IO；未取得 CLAIM 或独立评审。作者侧 Draft PR 保存不改变正式状态机。
