# R501 — signed BRC 辅助标量：二十四阶右缘 Toeplitz 子式精确符号分类

Date: 2026-11-03. Status: AUTHOR_SIDE_EXACT_COMPUTER_CERTIFICATE / DRIVER_UNREVIEWED / NOT_ADMITTED.
Scientific pin: R462 at `18783e01e3646c72b7aab3b16d3f565e83e6446f`; predecessor R500 at `0e54475ed4443f6c6f0da06ed70a43b5d02f12cf`. Normative context freshly read from Global Knowledge and Enterprise Math main; no change to frozen science.

## 命题与定义

令 k 为正整数，r=2k+1，C_k=binom(2k,k)/(k+1)>0，令
`H_k(t)=binom(r+t,2t)[x^r](1-x)(1+x)^(2t)(1+x^2)^(r-t)`
当 2<=t<=r；其他整数 t 取 H_k(t)=0。右缘位置 s=3 的 m 阶 Toeplitz 子式定义为
`D_m(k)=det[H_k(3+i-j)]_(0<=i,j<m)`。

**定理 R501：**
`D_24(k)>0` 对全部整数 `1<=k<=18` 成立；`D_24(k)<0` 对全部整数 `k>=19` 成立。
首次负值 r=39，之后每个奇数 r>=39 均负。

结合 R500 已验证的 m=23 全整数正性，此处对任意整数 k>=19 有 `D_23(k)>0>D_24(k)`。该结构针对冻结 signed BRC 辅助标量及所定义观察子式。

## Hessenberg 递推与次数界

使用 R452/R462 已验证的 EOR 整数多项式恒等式：固定 t 的 `p_t(k)=H_k(t)/C_k` 属于 Q[k] 且 `deg p_t<=2t`。该前提的独立来源是 R462 的 E_t O_t R_t 因子公式。

令 `f_m(k)=D_m(k)/C_k^m`。归一化 Hessenberg 递推为

`f_0=1;quad f_m=sum_(ell=1)^m (-1)^(ell-1) p_(ell+2)(k) p_2(k)^(ell-1) f_(m-ell)(k)`.

由 `deg p_(ell+2)<=2ell+4`、`deg p_2<=4`，对递推项的次数上界是
`(2ell+4)+4(ell-1)+6(m-ell)=6m`，所以 `deg f_24<=144`。

取严格正因子 `G_24(k)=k^24(k+1)^24(k+2)(2k+1)^24(2k+3)^24`，次数97，在 k>=1 严格为正。对 k=1,...,48 计算精确有理数 `f_24(k)/G_24(k)`，把既约分母的最小公倍数记为 L>0。设 `delta_j` 为 `L*f_24(k)/G_24(k)` 在 k=1 的 j 阶前向差分，j=0,...,47。定义次数至多47的 Newton 多项式 `S(k)=sum_(j=0)^47 delta_j binom(k-1,j)`。

## 完整整数证书

实际使用 BigInt 计算并检验：

`L*D_24(k)=C_k^24*G_24(k)*S(k)` 对整数 k=1,...,145 逐项严格相等。

等价地，两个次数均不超过144的有理系数多项式 `L*f_24(k)` 和 `G_24(k)*S(k)` 在145个不同点完全一致，故作为 Q[k] 恒等。这里 k=49,...,145 是独立于48点插值的97个恒等式检查点。

对 k=1,...,18，所有18项 `S(k)` 精确计算均严格正。将 S 改写成 k=19 起的 Newton 形式：
`S(19+u)=sum_(j=0)^47 epsilon_j binom(u,j)`，
其中 `epsilon_j=Delta^j S(19)`。**全部48项 epsilon_j 严格为负**（最大的、最接近零的一项为
`-99780065090301640474338632973210760888085674407803437013733279268708324351946089481894011052357534078348322`）。对每个整数 k>=19，取 u=k-19>=0，则 binom(u,j)>=0，且 epsilon_0<0，故 S(k)<0。与 C_k>0、G_24(k)>0、L>0 联立即得定理。

## 独立交叉核验、来源及范围

运行 `node R501_VERIFY.js > R501_EVIDENCE.json`，预期状态 `R501_EXACT_JS_PASS`。完整证书包括 L、48项初始 Newton 差分、18项边界精确值、48项 k=19 平移差分以及145点多项式恒等式检查。另检查20项独立24×24 Bareiss 原始行列式（k=1..20），500项由原始有符号二项卷积与 Catalan/ballot 公式得到的 H 值（k=1..20,t=2..26）。这些交叉验证沿用 signed BRC 支路相消的精确运算。

R500 的 m=23 正性与本轮 m=24 k>=19 负性形成跨阶数无限符号分岔。未执行 X6 原生时间更新或残差实验。P000、ACTIVE 世界观及 R462 冻结科学输入保持原样。未获得原生 CLAIM 或独立 Driver 接纳。

## 下一步

研究 `s=3,m=25` 的完整整数符号分类，优先测试同一 2m 项 Newton 差分及 `6m+1` 点恒等式证书。并对固定 k 的阶数生成函数分析主导极点，解释 m=20..24 的正负阈值与交错恢复。
