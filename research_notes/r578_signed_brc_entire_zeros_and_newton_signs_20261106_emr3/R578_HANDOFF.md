# R578｜接续材料（2026-11-06）

冻结科学源 R462@18783e01e3646c72b7aab3b16d3f565e83e6446f，直接前沿 R576@05de5b8b08acaa53243bf91bc7a2fac70c2408a6、R577@7f0e05e6e8b27ad28725360ea06f3e2aa6220e97。对象为 signed BRC 辅助 Toeplitz–Hessenberg 标量极限函数 F，不改变 P000/X6 或十二支路的来源语义。

本轮新作者侧证明：F 全部零点均简单且超越；最近共轭对 ζ、ζ̄ 的模 r<14、辐角 θ 控制每阶 Newton 首项 L_m，精确渐近为 L_m=2r^(−m)cos(mθ)+E_m，|E_m|≤A14^(−m)，A=14Σ_{其他零点}1/|ξ|<∞。由有理周期或无理极小旋转分别证明，无须事先解决 θ/π 无理性，正负 L_m 均在充分大 m 以有界间隔无限出现。

实际核算 R578_VERIFY.py（Python Fraction，n=1..120）通过，正59、负61；stdout 见 R578_EVIDENCE.txt，终止标记 R578_EXACT_NEWTON_RECURRENCE_PASS。详细证明 R578_PROOF.zh-CN.md；外部 Hermite–Lindemann 来源见该证明。

下一步：给 A 显式可计算上界；核验 θ/π 的有理性与自然符号密度；建立原始 signed BRC 联合观察者的谱桥。作者侧成果未由独立数学 Driver 接纳；原生身份/CLAIM/Result 单独核验。