# R406 — 所有固定右边界距离的最终严格正性与前128条无界 Turán 证书

日期：2026-10-30。角色：本轮自动研究会话的作者侧可移植研究（实际 GitHub 连接主体 `awdawmip`）；**UNREVIEWED / NOT_ADMITTED**。研究对象是 R402–R405 中原始十二支路 K/J→B→D 的**带符号 BRC 辅助组合模型**，其可变项仅为 `K₃[t²]=−8(1+θ)`，`θ>−1`；`a=30−16θ`。以下成果是模型内的代数命题，不改变 P000 或 ACTIVE 世界观，不能自动推出原生 X6 物理命题。

## 1. 前沿与准确问题

采用 R405 的确切符号：对整数 `r≥2`、`1≤s≤r`，

\[
\delta_{r,s}=[t^r](1-t)(1+t)^{2s}(1+t^2)^{r-s},\quad
H_{r,s}=\binom{r+s}{2s}\delta_{r,s},\quad
D_{r,s}=H_{r,s}^2-H_{r,s-1}H_{r,s+1}.
\]

令 `k=r-s`，`Cat_r=binom(2r,r)/(r+1)`，\((z)_{\underline m}=z(z-1)\cdots(z-m+1)\)。R405 给出整数多项式

\[
Q_k(r)=(r+1)\sum_{j=0}^{k-1}\binom{k}{j}(4j-2k+1)
(r)_{\underline{2j}}(r)_{\underline{2k-2j-1}}+(2k+1)(r)_{\underline{2k}},\quad Q_0=1,
\]

\[
N_k(r)=(k+1)(2r-k)Q_k(r)^2-k(2r-k+1)Q_{k-1}(r)Q_{k+1}(r)
\]

及对于 `r≥k+3` 的严格有理恒等式

\[
\tag{R406.1}
\frac{D_{r,r-k}}{\mathrm{Cat}_r^2}
=\frac{N_k(r)}{(k+1)(2r-k)(k!)^2\big((2r)_{\underline k}\big)^2}.
\]

其中分母为正。R405 的精确计算机辅助证明仅处理 `1≤k≤24`；R404 证明固定 `3≤s≤5` 的全部余阶严格正。我们的两个目标分别是证明**全部 k 的最终正性（固定 k、r→∞）**，以及向右边界扩展可执行的严格正系数证书。

## 2. R406-A：任意 k 的精确两项渐近式（人工代数证明）

**定理 R406-A。** 对任意固定整数 `k≥1`，沿着整数 `r→∞` 且 `r≥k+3`，成立

\[
\boxed{
\frac{D_{r,r-k}}{\mathrm{Cat}_r^2}
=\frac{r^{2k}}{(k+1)(k!)^2}
\left(1-\frac{k(3k+2)}{2r}+O_k(r^{-2})\right).
}
\tag{R406.2}
\]

因此，对**每一个**整数 `k≥1`，存在有限整数 `R(k)≥k+3`，使 `r≥R(k)` 时 `D_{r,r-k}>0`。量词顺序是 `∀k ∃R(k) ∀r≥R(k)`，不宣称对所有 `k` 可统一取 `R(k)=k+3`。

**证明。** 下降阶乘最高两项满足

\[(r)_{\underline n}=r^n-\binom n2r^{n-1}+O_n(r^{n-2}).\]

在 `Q_k` 的定义中，对于 `j<k`，`(r+1)(r)_{2j}(r)_{2k-2j-1}` 的最高项为 `r^{2k}`，次高项系数为

\[
U_{j,k}=1-\binom{2j}{2}-\binom{2k-2j-1}{2}
=-4j^2+4kj-2j-2k^2+3k.
\]

最后一项 `j=k` 单独为 `(2k+1)(r)_{2k}`；把上面的 `U_{j,k}` 多项式形式代入 `j=k`，得到 `U_{k,k}=−binom(2k,2)`，因此两个最高阶系数均可用同一和式 `j=0,...,k` 计算。令 `A_{j,k}=4j−2k+1`，由二项式矩

\[
\sum_j\binom kj=2^k,\quad
\sum_jj\binom kj=k2^{k-1},\quad
\sum_jj^2\binom kj=k(k+1)2^{k-2},\quad
\sum_jj^3\binom kj=k^2(k+3)2^{k-3}
\]

直接代入，得

\[
\sum_{j=0}^k\binom kj A_{j,k}=2^k,
\qquad
\sum_{j=0}^k\binom kj A_{j,k}U_{j,k}=-2^kk(k+1).
\]

故每个 `k≥1` 有多项式最高两项的**精确**公式

\[
\tag{R406.3}
Q_k(r)=2^k r^{2k}-2^kk(k+1)r^{2k-1}+O_k(r^{2k-2}).
\]

`Q_0=1` 也与本式的零阶最高项及形式次项兼容。将 `k−1,k,k+1` 的式 (R406.3) 代入 `N_k`，严格合并高两次项，得到

\[
\tag{R406.4}
N_k(r)=2^{2k+1}r^{4k+1}
-2^{2k+1}k(2k+1)r^{4k}+O_k(r^{4k-1}).
\]

同时

\[
(2r)_{\underline k}=(2r)^k
\left(1-\frac{k(k-1)}{4r}+O_k(r^{-2})\right),
\]

所以 (R406.1) 分母中的 `(2r−k) ((2r)_k)^2` 展开为

\[
2^{2k+1}r^{2k+1}\left(1-\frac{k^2}{2r}+O_k(r^{-2})\right).
\]

由 (R406.1)、(R406.4) 约分，线性项是

\[-k(2k+1)+\frac{k^2}{2}=-\frac{k(3k+2)}2,\]

即 (R406.2)。主系数 `1/((k+1)(k!)²)` 为严格正数，因此每个固定 k 的有理函数在足够大的实数 r 上为正，在整数子域中也为正。证毕。

**含义。** 即使尚无法证明所有 `r≥k+3` 一律严格正，任何固定右边界距离上的负性/零性也不可能无限延伸到 `r→∞`；如果存在全域反例，它必须发生在该 k 对应的有限起始段。这是跨所有 `k` 的全称结构结论，而不是有限 `k` 计算外推。

## 3. R406-B：前128条右边界带的无界-r严格正性（有限代数证书）

**定理 R406-B（计算机辅助，给定源码与整数证据）。** 在 R405 的同一辅助模型中，全部整数

\[
\boxed{1\le k\le128,\quad r\ge k+3,\quad s=r-k\ge3}
\]

满足

\[
\boxed{D_{r,r-k}>0.}
\]

若采用 R403 作者侧的严格 Turán 首项传递恒等式，则同时得到

\[
\operatorname{ord}_{a=0}T_{2r-k}^{(r)}=4(r-k).
\]

后一结论依赖 R402/R403 模型系数表达与传递式的独立审阅。

**可验证证书。** 对每一个整数 `1≤k≤128`，以 `Z[x]` 中的准确运算构造 (R405.1)、(R405.3)，进行平移 `r=k+3+x`。实际验证了

\[
\tag{R406.5}
[x^j]N_k(k+3+x)>0\quad(0\le j\le4k+1).
\]

每个 `N_k` 是次数严格等于 `4k+1` 的整数多项式，最高系数 `2^(2k+1)`。本轮验证了全部 `Σ_(k=1)^128 (4k+2)=33,280` 个严格正整数系数，比 R405 的24条扩展**104条无限余阶带、32,032个新证书系数**。因 `x≥0` 时多项式严格正，(R406.1) 分母严格正，立即得到 `r≥k+3` 的全部整数正性，*不是*仅在有限 r 点采样。

结合 R404 的 `s=3,4,5`，这还覆盖了**所有 `4≤r≤134`、`3≤s<r`** 的对应 Turán 首项严格正性。尚待解决的区域可精确写为 `r≥135, s≥6, k=r−s≥129`。

## 4. 执行、交叉验证和可重建证据

2026-10-30，实际在 Python 3 本地环境执行：

```text
python r406_verify.py --max-k 128 --out R406_EVIDENCE_128.json
R406_EXACT_PASS k= 128 positive_coefficients= 33280 point_checks= 771
```

程序使用 Python 标准库、整数多项式 Horner 平移和有理式交叉乘法，不使用浮点数判号。按每条 k 的整列正系数计算 SHA256。对 771 组整数点采用两种独立的 δ 表示（R405 二项式差与 R404 正 Catalan 核）以及 R405.2/R405.4 原式交叉检查；并验证全部 k 的 Q/N 最高两次系数与 (R406.3)/(R406.4) 一致。只要某一系数不是严格正数或交叉核验不符，程序抛出断言并不返回 PASS。

完整证据 `R406_EVIDENCE_128.json` 的大小为 **13,718,661 字节**，SHA256：`f3af2a75c59f01b3648f4691c08baef5b1f9bca9efbfb563080edf4893ac89a3`。远端提交的源码和逐 k 摘要可以重新构造全部列和原始证据；本轮提供的 ZIP 还包括完整原始 JSON。远端源码/证明作为**作者侧**验证与交接，并不代表 Lean 定理检查、Driver 独立审阅或原生 Result 接纳。

## 5. 依赖、证据强度、下一问题

不可变来源：R405 proof/code `enterprise-math@32818e88b2c377460dc8cbada8957239cc837d30` 下 `research_notes/r405_signed_brc_turan_right_tail24_20261030_emr3/`；R404 `enterprise-math@89cba1614fe75643ffb61e3e715169e2de103528`；R402/R403 用于带符号 BRC 模型到 Turán 首项的传递。研究基线为 Enterprise Math `main@1a63ddbe5fdc213e916cd328edbd61094933974c`，本轮 GLOBAL_KNOWLEDGE_V1 固定在 `main@cbaa938a795f8844f4ab9e22b4e90c06aa2a0b01`。与基线分开保存研究分支 head 和最后提交。

本轮实际原生身份/活跃任务核验：`em_status` 为版本 0.6.11，`research_authority_granted=false`、`executor_binding_configured=false`，控制面 `CODE_REVIEW_REQUIRED`；`em_control_tasks(request_id=r406owner20261030T0616Z,limit=5)` 返回 `CONTROL_QUOTA`。因此当前工作仅有作者侧推导与 GitHub Research Note 权限；不主张已获得任何正式 Source owner、CLAIM、run、review 或 admission。与既有 R402–R405 的共享研究脉络完整披露，不能以相同上下文做独立审阅。

最小后继问题：能否用 R405 的 `Q_k,N_k` 或 Catalan 正核推导对所有 `k≥1`、`r≥k+3` 的统一正性（尤其排除剩余 `k≥129,s≥6` 中的精确整数反例）？本轮通用的 `∀k∃R(k)` 只能说明每条 k 的最终正性，尚不能统一断言所有起始 r。下一轮可先建立强于系数扫描的解析比值不等式或构造一个符合 R405.1 的反例。
