# R362｜BRC Newton 第342条正性带、有限全余阶普通严格 Turán 证书

日期：2026-10-28。分类：AUTHOR_SIDE_EXACT_FINITE / CONDITIONAL_ALL_K / DRIVER_UNREVIEWED / NOT_ADMITTED。

## 冻结来源及模型

固定知识快照：`awdawmip/chatgpt-global-knowledge@74fa0b5495e75bec892ce26cf3e76ad55bcfcb5f` / GLOBAL_KNOWLEDGE_V1；项目规范：`awdawmip/enterprise-math@737cd7689de9692617a5e2c04ef0e81a19504ed4`。沿用 R346 中保留全部十二项正负号的有序 BRC K/J 递推：

`B_0(t)=1+t`; `B_s(t)=J_s(t)+Σ_(i=1)^min(12,s) K_i(t) B_(s−i)(t)`。
`D_(q,k)=Σ_(w=0)^k (−1)^(k−w) binom(k,w) 2^(q−w)[t^q]B_(q+w)(t)`，`L_r(u)=5^r H_r(u)`，其中 `H_r` 是由样本 `D_(r+u,u)/5^u`、u=0..r，确定的次数≤r的 Newton 插值多项式。定义

`Q_r(v)=L_r(v+1)L_r(v+2)−L_(r−1)(v+2)L_(r+1)(v+1)`，

`c_(r,j)=Δ^j Q_r(0)`，`0≤j≤2r`。本轮证明对象为 BRC 辅助组合序列；不把组合指标视为 P000 原生空间坐标、真实物理时间或 X6 Cell 动力学。

## 精确有限验证：完整 r=1..342

本轮实际执行 `R362_scan.py` 和另一路 `R362_full_turan_scan.py`，均从原始保留符号 K/J 核计算 `B_0..B_1031`（t 截断次数≤687）、`H_0..H_343`，继而对每个整数 r=1..342 的所有 j 完整取差分。得到：

`∀1≤r≤342,∀0≤j≤2r: c_(r,j)>0`，总计 `342×344=117648` 项；
`∀1≤r≤342,∀1≤j≤2r−1: c_(r,j)^2>c_(r,j−1)c_(r,j+1)`，总计 `342²=116964` 项。

先前尚未系统覆盖的 r=49..336 共新增 `336²−48²=110592` 项普通严格 Turán 检查。每个 r 的最高项核验 `c_(r,2r)=30^(2r) Cat_r`，次高与第三高项核验 R353/R354 作者侧公式；每个 `H_r` 的有限插值采样核验最高 Newton 差分 `6^r`、下一阶差分0。以任意精度整数、Fraction 精确运算判号，无浮点正性推断。

规范行 `r,j,decimal_integer\n` 拼接为 117648 行的 SHA256：
`d15a75f9ab5091cc8c1f740553ee52f4473765b9930177090a6f907cb63222fd`。
r=49..336 子集行的 SHA256：
`a25b864fddb5c141c8a7923b5d4c0bf1893c3e0cd22bad6d64be85f799a8a9d4`。

## R362 新 Q342 与旧证书回归

`Q_342` 的 **685/685** 项 Newton 系数严格正，**683/683** 项普通严格 Turán 检查通过。规范685行 SHA256：

`aa4b0e6390085106420e442b79dd81ffca80f6f9e1106fb14de474e13acc2f74`。

Q342 的683项内部二项式归一化超对数凹性 ULC 测试中，626项失败、57项成立、0项等号；首个失败 j=1，最大 Newton 系数位于 j=367。Q341 683行回归 SHA256 等于 R361：`8d266933eaa17e62317fe4709a85be633f4a09726d90757ef05facd9e672d346`。独立包装的局部 `R362_verify.py` 还精确核对8个原始 D 阵列二阶子式，结果均一致。以上有限数值证书可通过此目录执行源码重现，完整685行整数与执行日志保存在本轮研究交付包。

## 量词、条件外推与剩余证明义务

R348(A1–A5) 的全指标抽取与次数界作者侧证明（Draft PR #1599）若成立，则所有 u≥0 有 `D_(r+u,u)=5^u H_r(u)`，且 `deg Q_r≤2r`，而完整正 Newton 系数推出所有整数 `v≥0` 的 `Q342(v)>0`。由精确因子化 `M_(342+k,k)=5^(2k+1−684)Q342(k−1)`，得条件性结论：

`∀k≥1: M_(342+k,k)>0`；与前序证书合并，`∀k≥1,1≤q−k≤342: M_(q,k)>0`。

有限计算不能外推成所有 r 的严格 Turán 定理、全二维 TP₂、TP₃ 或原生六维 X6 动力学定理；R348 仍须独立数学审查。**下一核心问题**：建立同时控制 r,j 的普通严格 Turán / PF₂ 保真核，或者找到精确反例；对 R348(A2–A5) 的 y-分次、极点归纳、全部边界展开进行真正独立复核。

## 执行权限与保存

本轮 GitHub 作者身份 awdawmip，仓库 push/admin；原生 Site gateway 配置只读 `research_authority_granted=false`，原生 Owner 查询返回 `CONTROL_QUOTA`。本轮只作作者侧数学研究及 GitHub Draft PR 材料保存，不宣称 Source-native CLAIM、Result、独立 Driver review 或数学接纳。P000 与 ACTIVE 世界观未改写。
