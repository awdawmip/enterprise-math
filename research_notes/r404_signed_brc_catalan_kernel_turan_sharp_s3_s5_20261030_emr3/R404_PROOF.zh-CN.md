# R404 — 全余阶 Catalan 正展开与前五条 Turán 缺陷的精确退化阶数

2026-10-30 · Researcher-ID: EM-R404-3C89B8 / TASK_RESEARCH · 作者侧数学证明；独立审阅未完成、未进入原生 Result 或 Working Truth。

## 1. 精确对象及前沿

延续 R402、R403 的**原始带符号十二支路 BRC K/J→B→D 辅助组合模型**，仅替换 K₃[t²]=−8(1+θ)，θ>−1。令 a=30−16θ，θ*=15/8；研究固定余阶 r 下的 Newton 系数 c_j^(r) 与 Turán 缺陷 T_j^(r)=(c_j^(r))²−c_(j−1)^(r)c_(j+1)^(r)。**不将辅助系数认作 X6 原生状态或正质量**。

对 0≤s≤r 记

\[
\delta_{r,s}=[t^r](1-t)(1+t)^{2s}(1+t^2)^{r-s},\quad
B_{r,s}=\binom{r+s}{2s},\quad H_{r,s}=B_{r,s}\delta_{r,s},
\]
\[
D_{r,s}=H_{r,s}^{2}-H_{r,s-1}H_{r,s+1}\quad(1\le s<r),
\qquad\mathrm{Cat}_n=\frac1{n+1}\binom{2n}{n}.
\]

R403 已在 R402 形式系数结论基础上证明：

\[
[a^{4s}]T_{r+s}^{(r)}=180^{2r-2s}D_{r,s},\qquad
\operatorname{ord}_{a=0}T_{r+s}^{(r)}\ge4s.
\tag{R403.1}
\]

本轮证明以下两个**跨全部整数余阶、非有限枚举**的结果。对 R402 的形式外根分解、系数模型及 R403 的上述传递公式，仍保留独立审核依赖。

## 2. 定理 A：δ 的有限 Catalan 正展开

对于所有整数 r≥1 和 1≤s≤r，有精确恒等式

\[
\boxed{\displaystyle
\delta_{r,s}=\sum_{\substack{0\le j\le s-1\\r-s+j\ \mathrm{even}}}
\binom{s-1}{j}2^{s-1-j}\mathrm{Cat}_{(r-s+j)/2}.}
\tag{R404.1}
\]

每项是非负整数，且当 s≥2 时严格有正项；当 s=1 时，r 为奇数给 Cat_(r−1)/2>0，r 为偶数给零。这独立地给出 R402 中 δ 的全部正性及奇偶例外，不使用数值采样、概率积分或物理近似。

**证明。** 令形式 Laurent 变量 v=t+t^(−1)，对 v 的多项式 f 定义线性泛函

\[
\Lambda(f)=[t^0]f(t+t^{-1})-[t^1]f(t+t^{-1}).
\]

由于

\[
t^{-r}(1+t)^{2s}(1+t^2)^{r-s}=(v+2)^s v^{r-s},
\]

且右侧是 t↔t^(−1) 对称的 Laurent 多项式，所以 δ_(r,s)=Λ((v+2)^s v^(r−s))。对 k≥0，直接展开二项式：

\[
\Lambda(v^{2k})=\binom{2k}{k},\qquad
\Lambda(v^{2k+1})=-\binom{2k+1}{k}.
\]

因此

\[
\Lambda((v+2)v^{2k})=2\binom{2k}{k}-\binom{2k+1}{k}=\mathrm{Cat}_k,
\]
\[
\Lambda((v+2)v^{2k+1})=\binom{2k+2}{k+1}-2\binom{2k+1}{k}=0.
\]

展开剩余 (v+2)^(s−1)，逐项应用这两个等式即得 (R404.1)。s≥2 时 j∈{0,1} 已包含所需的两种奇偶之一，故严格正。证毕。

## 3. 定理 B：s=3、4、5 的全余阶 Turán 首项严格正

对每个整数 r≥4 及 3≤s≤min(5,r−1)，均有

\[
\boxed{D_{r,s}>0,
\qquad \operatorname{ord}_{a=0}T_{r+s}^{(r)}=4s.}
\tag{R404.2}
\]

结合 R403 已证明的 s=1、2 精确非零性，得到全部 r≥2、1≤s≤min(5,r−1) 的 **4s 阶严格取等号**。这并未解决 s≥6 的无限族。

**证明：可复算的有限代数消元。** (R404.1) 给出下列全部需要的有限系数，其中仅在 s≤r 且 Catalan 下标非负时使用相应单元：

| s | δ_(2m,s)；C=Cat_(m−1) | δ_(2m+1,s)；C=Cat_m |
|---|---|---|
| 2 | 2C | C |
| 3 | 4C | 4Cat_(m−1)+C |
| 4 | 8Cat_(m−2)+6C | 12Cat_(m−1)+C |
| 5 | 32Cat_(m−2)+8C | 16Cat_(m−2)+24Cat_(m−1)+C |
| 6 | 32Cat_(m−3)+80Cat_(m−2)+10C | 80Cat_(m−2)+40Cat_(m−1)+C |

只需代入两个通用整数比值

\[
\frac{\mathrm{Cat}_{m-1}}{\mathrm{Cat}_m}=\frac{m+1}{2(2m-1)},\qquad
\frac{\mathrm{Cat}_{m-2}}{\mathrm{Cat}_{m-1}}=\frac{m}{2(2m-3)}
\]

及二项式比值

\[
\frac{B_{r,s}}{B_{r,s-1}}=\frac{(r+s)(r-s+1)}{2s(2s-1)},\qquad
\frac{B_{r,s+1}}{B_{r,s}}=\frac{(r+s+1)(r-s)}{(2s+2)(2s+1)}.
\]

对于 r=2m，定义 C=Cat_(m−1)；对于 r=2m+1，定义 C=Cat_m。化简恒等式 D_(r,s)/(B_(r,s) C)²，可**精确**得到（各分母在所列有效整数域严格正）：

偶数余阶 r=2m：

\[
\begin{aligned}
\frac{D_{2m,3}}{(B_{2m,3}C)^2}
 &=\frac{104m^2+7m-66}{7(m-1)(2m+3)}\quad(m\ge2),\\
\frac{D_{2m,4}}{(B_{2m,4}C)^2}
 &=\frac{4(8m+5)(136m^2-119m+114)}{45(m+2)(2m-3)^2}\quad(m\ge3),\\
\frac{D_{2m,5}}{(B_{2m,5}C)^2}
 &=\frac{2(3584m^4-3584m^3-112m^2-3747m-1305)}{11(m-2)(2m-3)^2(2m+5)}\quad(m\ge3).
\end{aligned}
\tag{R404.3}
\]

奇数余阶 r=2m+1：

\[
\begin{aligned}
\frac{D_{2m+1,3}}{(B_{2m+1,3}C)^2}
 &=\frac{208m^3+610m^2+851m+431}{28(m+2)(2m-1)^2}\quad(m\ge2),\\
\frac{D_{2m+1,4}}{(B_{2m+1,4}C)^2}
 &=\frac{2176m^4+5984m^3+5482m^2-1269m-2853}{45(m-1)(2m-1)^2(2m+5)}\quad(m\ge2),\\
\frac{D_{2m+1,5}}{(B_{2m+1,5}C)^2}
 &=\frac{7168m^5+14336m^4+2464m^3-14634m^2+2319m+12024}{22(m+3)(2m-3)^2(2m-1)^2}\quad(m\ge3).
\end{aligned}
\tag{R404.4}
\]

这六个有理恒等式仅需有限项的二项式展开及 Catalan 比值；任一式可两边乘以所示分母和 (B C)²，直接验算为零多项式，不借助对 m 的有限枚举。

**全范围严格正性证书。** 为避免对带负系数的分子直接作外推，作 n≥0 的代换：

- R404.3 第一行 m=n+2，分子变为 104n²+423n+364；第二行 m=n+3，其二次因子变为 136n²+697n+981；第三行 m=n+3，括号内的分子变为 3584n⁴+39424n³+161168n²+285885n+179982。
- R404.4 第一行分子所有系数本来严格正；第二行 m=n+2，分子变为 2176n⁴+23392n³+93610n²+162099n+99225；第三行 m=n+3，分子变为 7168n⁵+121856n⁴+819616n³+2717046n²+4432371n+2856843。

因每个正性证书的系数严格正，全部有效整数 m 的六个 D 均严格正。由 (R403.1) 的 180^(2r−2s)>0，Turán 的 a^(4s) 首项非零且为正，所以阶数恰为 4s。证毕。

## 4. 精确核验范围、证据和非主张

实际执行：python verify_r404.py 512，返回 R404_EXACT_PASS。用标准库纯整数/有理数计算执行：

- r=2..32 的 527 组 δ，经直接多项式卷积、(R404.1) 和独立 Pascal 三路径完全一致；r=2..512 对共 131327 个 (r,s) 的 Pascal 与 Catalan 恒等式逐一核对。
- r≤512、s≥3 的 129795 组 D 均严格正；s∈{3,4,5} 的全部 1524 组精确匹配 (R404.3)/(R404.4)。
- r≤512、s≤2 的负值仅出现于偶数 r 的 s=1，以及 (r,s)=(3,2)、(5,2)，没有零值。这部分是 R403 结论的非独立复现，非新的无限证明。

验证源代码 SHA256：9b52fca5973bb488a052f8a40a633ea54a0b4e8f7530b25f4c97c4174ac712ea。实际生成证据 JSON SHA256：d9577d96d83d84a0c2f1907356da821a4e57b9248a8c81e2b8824caf1b28f4dd。二者将以无损 gzip/base64 保存于本研究目录，恢复方式在 R404_EVIDENCE_INDEX.md。有限运行不代替上述跨所有 r 的证明，精确模型来源仍依赖 R402/R403 的作者侧形式代数，尚未由独立研究者复核。

**下一数学单元：** 对无限域 r≥7、6≤s<r，证明 D_(r,s)>0 或给出最小精确反例。优先研究 (R404.1) 的 Catalan 非负核能否诱导 H_(r,s) 的统一比值不等式；不能直接从 δ 正性推出 H 的 log-concavity。保留 R403 已发现的 s≤2 的负值例外，不重做已有固定余阶 PF₂ 参数分类。

**来源冻结与权限：** GLOBAL_KNOWLEDGE_V1 main@b8632f1fb3f57d217415c7580f24bc79db6dce0c；Enterprise Math main@2fdba2f4e10aea0c41c4178535edcdf69bc92fbf；上轮作者侧 R403 PR HEAD@dabf55feaa5bf9f72abff704a307a76f1e5dd139。P000 与 ACTIVE 世界观未改。GitHub 当前 writer 为 awdawmip；原生服务 0.6.11 当前 research_authority_granted=false、executor_binding_configured=false、control quota 5/5 且 CODE_REVIEW_REQUIRED；活跃 Source Owner 未得到肯定性核验。本轮限定为 AUTHOR_SIDE_PROOF / LOCAL_EXACT_PASS / DRIVER_UNREVIEWED / NOT_ADMITTED / ACTIVITY_REGISTER_PENDING，不声称原生 Claim/Result/Review/接纳。
