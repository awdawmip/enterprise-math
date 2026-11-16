# R532 331×56 原始系数全网格核验补充

日期：2026-11-04；冻结科学输入 R462@18783e01e3646c72b7aab3b16d3f565e83e6446f。

主证书 R532_VERIFY.js 的 D55(k) 采用 ballot–Catalan 系数 B_k(t) 递推，而原始 Toeplitz 定义采用 H_k(t)。为将主证书的331点多项式检查直接落实到**原始 signed BRC 行列式**，本补充程序逐项验证：

`H_k(t)=binom(r+t,2t) sum_{q=0}^{r-t} binom(r-t,q)[binom(2t,r-2q)-binom(2t,r-2q-1)]`

以及

`B_k(t)=binom(r+t,2t) sum_{q=0}^{min(floor((t-1)/2),k)} binom(t-1,2q)4^q Cat(k-q)`，

其中 r=2k+1，t 不在 2..r 范围时两边按定义为零。

对所有 `k=1,...,331` 与 `t=2,...,57`，共18536组，使用 JS BigInt 精确比较上述两式，结果为 `R532_FULL_COEFFICIENT_GRID_PASS`。t=2 是行列式递推首超对角线因子，t=3,...,57 是 m=55 的其余所需系数。

因此主证书在全部331个点上计算的 D55(k) 与原始 signed BRC Toeplitz 行列式精确一致。在共同前提 P（冻结 R452/R462 的 `H_k(t)/Cat(k)` 为次数不超过2t的有理多项式）下，主证明的331点插值论证合法，并由 k=13 的110个严格正 Newton 差分得到整数无限尾部。全网格核验是**有限点等价证明**，不在此断言已取得全部 k 的 ballot–Catalan 恒等式。

复现：`node R532_FULL_COEFFICIENT_GRID.js > R532_FULL_COEFFICIENT_GRID_EVIDENCE.json`。两份附件为本补充的完整程序与实际输出；主证书及跨语言审计见 R532 原有六文件。
