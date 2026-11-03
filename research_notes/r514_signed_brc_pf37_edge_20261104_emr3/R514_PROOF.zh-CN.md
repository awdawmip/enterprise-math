# R514 — signed BRC 辅助标量：s=3、三十七阶 Toeplitz 子式全整数符号分类

2026-11-04；科学冻结 pin：R462@`18783e01e3646c72b7aab3b16d3f565e83e6446f`；上轮 R513@`4cd3c076d3e4d4c988a28beeb9966080f2fbb22d`。
状态：**AUTHOR_SIDE_EXACT_COMPUTER_CERTIFICATE / DRIVER_UNREVIEWED / NOT_ADMITTED**。

## 定义和定理

对正整数 `k`，令 `r=2k+1`、`C_k=binom(2k,k)/(k+1)>0`。定义原始 signed BRC 辅助标量
```text
H_k(t)=binom(r+t,2t)*[x^r](1-x)(1+x)^(2t)(1+x^2)^(r-t),  2<=t<=r;
H_k(t)=0, otherwise;
D_m(k)=det(H_k(3+i-j))_(0<=i,j<m), D_0=1.
```
沿用 R452/R462 冻结多项式前提 `p_t(k)=H_k(t)/C_k ∈ Q[k]`、`deg p_t<=2t`。则对所有正整数 `k`，
```text
D_37(k)>0, 1<=k<=5 or 7<=k<=22;
D_37(k)<0, k=6 or k>=23.
```
即 `r=13` 为孤立负值，`r=15,17,...,45` 为正，自 `r=47` 起永久为负。由 R513 已证符号分类，`D_36(k)>0>D_37(k)` 对 `23<=k<=207` 成立。

## 证明

令 `f_m(k)=D_m(k)/C_k^m`，`f_0(k)=1`。Toeplitz–Hessenberg 递推：
```text
f_m = sum_(a=1..m) (-1)^(a-1)*p_(a+2)*p_2^(a-1)*f_(m-a).
```
对每项使用 `deg p_(a+2)<=2a+4`、`deg p_2<=4` 与归纳界 `deg f_(m-a)<=6(m-a)`，得 `deg f_m<=6m`。所以 `deg f_37<=222`。

在正整数域上取严格正的
```text
G_37(k)=[k(k+1)(2k+1)(2k+3)]^37*(k+2), deg G_37=149.
```
在 `k=1..74` 精确计算 `f_37(k)/G_37(k)` 的约分有理数，令正整数 `L` 为其分母最小公倍数。对应74个整数值的完整前向差分 `delta_0,...,delta_73` 存于 `R514_EVIDENCE.json`，并定义
```text
S_37(k) = sum_(j=0..73) delta_j * binom(k-1,j), deg S_37<=73.
```
`R514_VERIFY.js` 以精确 BigInt 验证全部 **223个不同整点 k=1..223** 的等式
```text
L*D_37(k) = C_k^37*G_37(k)*S_37(k).
```
两侧除以 `C_k^37` 后都是次数至多222的 `Q[k]` 多项式，223点一致蕴含恒等式
`L*f_37(k)=G_37(k)*S_37(k)` 对全部 `k` 成立。

证书保存 `S_37(k),k=1..22` 的精确整数值，其符号为 `1..5:+;6:-;7..22:+`。移至 `k=23` 后全部74项 `epsilon_j=Delta^j S_37(23)` **严格负**，所以每个整数 `u>=0` 满足
```text
S_37(23+u)=sum_(j=0..73) epsilon_j*binom(u,j)<0.
```
理由是所有二项式系数非负且 `epsilon_0<0`。最后结合 `L,C_k,G_37(k)>0` 得到全正整数参数符号定理。

## 可复现的精确验证

`node R514_VERIFY.js > R514_EVIDENCE.json` 实际返回 `R514_EXACT_JS_PASS`：223个恒等式点、20个直接原始37×37 Bareiss 行列式、740个 signed BRC 原始卷积与 ballot-Catalan 的逐项整数核对（k=1..20,t=2..38）。

`python R514_INDEPENDENT.py > R514_INDEPENDENT_EVIDENCE.json` 实际返回 `R514_INDEPENDENT_PASS`：独立 ballot/Catalan 构造下，SymPy Berkowitz 方法直接计算10个37×37矩阵行列式（k=1,5,6,7,9,14,22,23,24,37），另核对740个原始 signed 系数。两种实现全部使用精确整数运算。

本结论是冻结 R452/R462 多项式前提下的 signed BRC 辅助标量模型内定理；尚待独立数学审阅和正式原生 Result/Driver 接纳。P000、ACTIVE 世界观和冻结科学输入均未修改。

## 下一单元

`s=3,m=38`：先测试76项 Newton 差分和229点精确恒等式证书以分类全部正整数参数；研究固定 k=22/23/207/208 的有理阶数生成函数分母主导根与共轭相位，解释长正区间以及永久负尾。
