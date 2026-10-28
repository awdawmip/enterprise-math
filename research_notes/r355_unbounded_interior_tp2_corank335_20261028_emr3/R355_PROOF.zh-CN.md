# R355｜有符号 BRC Newton 第335条无界内区 TP₂ 差分带

**日期与来源。** 2026-10-28（Asia/Shanghai）；本轮研究身份：ChatGPT 进取数论研究3，本地作者侧可移植研究；研究者不拥有经 Source 授权的本轮 CLAIM。固定读取 GLOBAL_KNOWLEDGE_V1 `main@1c6c5743a0d20073fb74048ec9ca5b576e45990e`，Enterprise Math `main@829710b992ee1905dea5d471e7ca7806cc6521e1`。承接 R348 全指标有理抽取作者证明 `5347e506bd145028d7338e9f7993dcd2a2fed97c`、R354 第334条前沿 `b1fcc9f5e9b4b40964d0232bc08952df63963ec4`。状态：**AUTHOR_SIDE_EXACT / CONDITIONAL_ON_R348 / UNREVIEWED / NOT_ADMITTED**。

## 1. 对象与载重前提

完整十二项保留符号的有序六边 BRC 辅助组合递推为
[
B_0(t)=1+t,qquad B_s(t)=J_s(t)+sum_{i=1}^{min(12,s)}K_i(t)B_{s-i}(t);
quad
D_{q,k}=sum_{w=0}^k(-1)^{k-w}inom{k}{w}2^{q-w}[t^q]B_{q+w}(t).
]
`K_i,J_s` 的完整整数定义复用 R346_verify.py，未消去负号。定义
[
M_{q,k}=D_{q,k}D_{q+1,k+1}-D_{q,k+1}D_{q+1,k}.
]
**明确条件 A：**R348(A1–A5) 的全指标定理成立，即每个 r,u≥0 有
(D_{r+u,u}=5^uH_r(u))，其中 (H_rinmathbb Q[u])、次数≤r。R348 虽提供作者侧形式幂级数论证，本论证不声称该引理已得到独立 Driver 数学审查。

按既有记号令 (L_r(v)=5^rH_r(v))，
[
Q_r(v)=L_r(v+1)L_r(v+2)-L_{r-1}(v+2)L_{r+1}(v+1).
]
R348 的乘积分离给出 (M_{r+k,k}=5^{2k+1-2r}Q_r(k-1))。

## 2. 本轮精确整数证书

本轮真实执行 `R355_verify.py`，由原始完整 K/J 带符号递推重新计算 (B_0,ldots,B_{1010})，截取 t 的 0..673 次系数；取 `r=333,334,335,336` 的 H 行，计算各 r+1 次前向差分为零及最高差分 (6^r)；构造 Q334、Q335 并计算完整 Newton 系数。

[
oxed{Delta^jQ_{335}(0)>0quad (j=0,1,ldots,670).}
]

**671个精确整数严格为正，零项0、负项0。** 新增逐行标准格式 `335,j,decimal_integer\n` 的 SHA256：
`95e782ee91ff3b097d2af2d02106c53680b825c3290fbb3cb0365437096af943`。

回归验证 `Q_{334}` 的669个系数 SHA256：
`e92c455f5f097dcdfbce8b5f3268fe5096d0f4d3cff91a0d685993017deee26a`，与 R354 一致。Q335 最高系数精确等于 (30^{670}mathrm{Cat}_{335})。其最高两级比值精确符合 R353 与 R354 的已列公式：
[
rac{Delta^{669}Q_{335}(0)}{Delta^{670}Q_{335}(0)}=rac{17\cdot335+11}{10},quad
rac{Delta^{668}Q_{335}(0)}{Delta^{670}Q_{335}(0)}
=rac{7803\cdot335^3+2252\cdot335^2-5523\cdot335+3328}{2700(2\cdot335-1)}.
]
另外，8个 (k=1,ldots,8) 的原始 D 子式与分离表达式在 Fraction 精确算术下直接相等、且为正。没有浮点符号判断。

**计算范围声明：**上述截断只验证本次需要的有限系数，依赖全指标论证来排除未计算的更高阶项；有限实验单独不建立无界结论。

## 3. 条件无界结论

由前提 A，(deg Q_{335}le670)。对任意整数 (kge1)，(v=k-1ge0)，有限 Newton 展开严格成立：
[
Q_{335}(v)=sum_{j=0}^{670}Delta^jQ_{335}(0)inom{v}{j}>0.
]
其中 (inom{v}{j}ge0) 且 j=0 项严格正。因 (5^{2k+1-670}>0)，可得
[
oxed{M_{335+k,k}>0quad	ext{对全部整数 }kge1.}
]
结合已有相同前提下 r≤334 的证书，作者侧条件结论达到
[
oxed{M_{q,k}>0quad(kge1, 1le q-kle335).}
]
无界性仅沿固定余阶带，尚未覆盖全部二维指标。该对象是带符号 BRC **辅助组合模型**；要转至 P000 原生六维 X6 Cell 动力学，需另行建立保留联合路径/支路/残差和后续操作的原生状态—读出对应及保真定理。

## 4. 复现、范围与下一问题

在 Enterprise Math 仓库内执行 `python research_notes/r355_unbounded_interior_tp2_corank335_20261028_emr3/R355_verify.py`；依赖同仓库 `research_notes/r346_unbounded_interior_tp2_corank301_20261028_emr3/R346_verify.py` 与 Python 3 标准库。源码本轮实际执行 SHA256 为 `d0c41f747111297c584f3310a75a3dccfb1a57a89204e8a2a6b0b32e1b86f01f`，Git Blob SHA1 为 `d698ef7826373051b936ff142b3954b209e73c6f`。运行生成 `R355_EVIDENCE.json` 和含全部671行精确整数的 `R355_Q335_FULL_COEFFICIENTS.txt`；本轮保存完整本地研究 ZIP，GitHub 中源码与证据摘要可复算。实际执行约10秒（容器环境一次测量）。

**下一单元：**构造 Q336 并验算其673个完整 Newton 系数，回归锚固定 Q335 的上述 SHA256。更关键的数学审查目标是由其他真实独立贡献者复核 R348(A1–A5) 的形式换元、y/z 次数界和 q<m 的二项式边界；继续探索对任意 r、k 的全局低阶差分正性或精确反例。不得把作者检查计为独立 Driver review/正式 Source Result。

P000、ACTIVE 世界观、先前审阅/Source 字节均不变。