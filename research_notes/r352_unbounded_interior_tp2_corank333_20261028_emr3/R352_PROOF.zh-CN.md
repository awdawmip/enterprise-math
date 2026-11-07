# R352 | BRC Newton 第333条无界内区 TP₂ 正性带

日期：2026-10-28。类型：AUTHOR_SIDE_EXACT_COMPUTATION_AND_CONDITIONAL_PROOF / UNREVIEWED / NOT_ADMITTED。

## 1. 固定来源与模型

全局规范读快照 `awdawmip/chatgpt-global-knowledge@528875d07cb0dd4cdac66626f455f09ee712f1da`（`GLOBAL_KNOWLEDGE_V1`）；项目控制与 P000 读快照 `awdawmip/enterprise-math@382e6d3005559d808b8ed49cded36d2b01b299b2`。沿用 R348 的 A1–A5 有理抽取作者侧证明（Draft PR #1599，提交 `5347e506bd145028d7338e9f7993dcd2a2fed97c`）和 R351 第332条证书（Draft PR #1592，提交 `3062723fa7d568d06419b9878bcddb870c98a016`）。本轮没有正式 claim，当前活跃 owner 的原生查询返回 CONTROL_QUOTA。

原始对象为十二项**保留符号**的 BRC 辅助组合递推：

[
B_0(t)=1+t,qquad B_s(t)=J_s(t)+sum_{i=1}^{min(12,s)}K_i(t)B_{s-i}(t).
]

[
D_{q,k}=sum_{w=0}^k(-1)^{k-w}inom{k}{w},2^{q-w}[t^q]B_{q+w}(t),quad M_{q,k}=D_{q,k}D_{q+1,k+1}-D_{q,k+1}D_{q+1,k}.
]

这里的 q,k 是辅助组合索引，不是原生六维空间坐标。未构造从此观察量到 P000 心跳世界原生 X6 联合状态及后续操作的保真桥，故本文件不作原生动力学结论。

## 2. 精确计算

令 R348 的 `D_{r+u,u}=5^uH_r(u)`，`L_r(v)=5^rH_r(v)`，

[
Q_r(v)=L_r(v+1)L_r(v+2)-L_{r-1}(v+2)L_{r+1}(v+1).
]

从原始递推以任意精度整数重建 `B_0,ldots,B_{1004}`，保留 t 系数次数 `0..669`。由 `u=0..r+1` 的精确有理数值及前向差分构造 `H_{331},ldots,H_{334}`，逐行核验 `Delta^{r+1}H_r(0)=0` 和 `Delta^rH_r(0)=6^r`。在 Q 的计算中：

- 对 r=332 的665项重新计算，十进制 `r,i,integer\n` 逐行 SHA256 与 R351 完全一致：`2c718b864b329b386227c5d3ccff50dc7f9c6ab5b428a65492f34a9e4736b9c2`。
- **新增 r=333 的667项完整 Newton 差分全部为严格正整数**；0个零值、0个负值，最小值位于 i=0。逐行规范序列 SHA256：`80d7047d63ad845cc1c7f81b8c45f9537bbe7fc2475fd36a7111428113be2e60`。
- 最高差分逐整数核验 `Delta^{666}Q_{333}(0)=30^{666}mathrm{Cat}_{333}`；并逐项对照 8 个 k=1..8 的原始 D 子式与 Q 分离公式，精确一致。
- 使用 Python 大整数与 `Fraction`；无浮点判号。程序和完整输出文件及本轮日志随本地研究包保留，仓库程序可从当前 PR 内的 R346 依赖重建所有667项。

## 3. 无界条件证明

R348(A1–A5) 若成立，则 `H_r` 对每一固定 r 都是次数至多 r 的多项式，故 `deg Q_{333}le666`。对所有整数 `vge0`：

[
Q_{333}(v)=sum_{i=0}^{666}Delta^iQ_{333}(0)inom vi.
]

已精确验证所有 667 个系数均严格正，且 `inom vige0`、常数项严格正，因此 `Q_{333}(v)>0`。直接代数替换有

[
M_{r+k,k}=5^{2k+1-2r}Q_r(k-1).
]

故在上述未独立审查的 R348 抽取和次数结论成立的前提下，

[
oxed{M_{333+k,k}>0quadorall kge1.}
]

加上历史证书，作者侧条件结论累计为 `kge1,1le q-kle333` 的 333 条无界余阶正性带。**不是** `q-k` 无界的整体二维 TP₂ 证明，也不覆盖 k=0 负子式或全局 TP₃，更不提升为原生 X6 定律。R348 尚待独立审查；上述有限验证本身不能代替次数定理。

## 4. 复现、边界与下一问题

在该 PR checkout 的根目录执行 `python research_notes/r352_unbounded_interior_tp2_corank333_20261028_emr3/R352_verify.py`。它调用同一 PR 分支已经保存的 `r346_.../R346_verify.py`，写出 `R352_Q333_FULL_COEFFICIENTS.txt` 与 `R352_EVIDENCE.json`；后者是本轮实际执行证据的可复现生成方式。SHA256 定义为 **UTF-8 连续行** `333,i,<base10 integer>\n`，`i=0,...,666`。

下一问题：在不默认全系数正性的前提下分析 `Q_{334}` 的669项；更优先安排与本作者独立的 R348(A1–A5) 语义与形式化核验，尤其分次次数界、抽取替换边界与 `q<m` 处理。所有结果保留 AUTHOR_SIDE / NOT_ADMITTED，P000 与 ACTIVE 世界观未修改。
