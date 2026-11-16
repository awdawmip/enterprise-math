# R517 — signed BRC 辅助标量：s=3、40阶 Toeplitz 子式全正整数参数符号分类

日期：2026-11-04。科学输入冻结：R462 @ `18783e01e3646c72b7aab3b16d3f565e83e6446f`；最近直接前沿：R516 @ `78a568ed73fd8372631c58dd665e810e3903b665`。

证明状态：**AUTHOR_SIDE_EXACT_COMPUTER_CERTIFICATE / DRIVER_UNREVIEWED / NOT_ADMITTED**。适用冻结 R452/R462 的固定 `t` 多项式恒等式及次数界，结论针对 signed BRC 辅助标量模型。

## 精确定义与定理

令 `k>=1` 为整数、`r=2k+1`，`C_k=binom(2k,k)/(k+1)`。定义

```text
H_k(t) = binom(r+t,2t) [x^r](1-x)(1+x)^(2t)(1+x^2)^(r-t),  2<=t<=r;
H_k(t) = 0, t<2 or t>r;
D_m(k) = det(H_k(3+i-j)) (0<=i,j<m), D_0(k)=1.
```

**定理（在上述冻结多项式前提下，对所有正整数 k）：**

```text
D_40(k)>0   (1<=k<=7);
D_40(k)<0   (8<=k<=28);
D_40(k)>0   (k>=29).
```

因此，奇数 `r=3,5,...,15` 时正，`r=17,19,...,57` 时负，`r>=59`（奇数）时严格正。结合 R516 得到 `D_39(k)<0<D_40(k)` 对所有 `k>=29`。

## 精确计算机辅助证明

假设冻结 R452/R462 已证明：对每个固定整数 `t>=2`，`p_t(k)=H_k(t)/C_k` 属于 `Q[k]`，且 `deg p_t<=2t`。设 `f_m(k)=D_m(k)/C_k^m`，Toeplitz–Hessenberg 展开给出：

```text
f_0(k)=1;
f_m(k)=sum_{a=1..m} (-1)^(a-1) p_(a+2)(k) p_2(k)^(a-1) f_(m-a)(k).
```

每项次数至多 `2(a+2)+4(a-1)+6(m-a)=6m`，故归纳得 `deg f_40<=240`。

选取对 `k>=1` 严格为正的因子：

```text
G_40(k)=[k(k+1)(2k+1)(2k+3)]^40*(k+2),  deg G_40=161.
```

对 `k=1,...,80` 精确计算有理数 `f_40(k)/G_40(k)`，取其约分分母的最小公倍数 `L>0`，构造整数 Newton 差分 `delta_j`（`0<=j<=79`）及次数至多79的整数值多项式

```text
S_40(k)=sum_{j=0..79} delta_j*binom(k-1,j).
```

`R517_EVIDENCE.json` 保存完整 `L`、80个 `delta_j`、各点检查及尾部差分。用 BigInt 逐点精确核验 `k=1,...,241`：

```text
L*D_40(k) == C_k^40*G_40(k)*S_40(k).
```

除以 `C_k^40` 后，此式两边为次数至多240的有理多项式；241个互异整点全部满足，故恒等式对全部 `k` 成立。再以 `k=1,...,28` 的完整整数值检验 `S_40` 的正负；以 `k_0=29` 平移，计算80个整数 `epsilon_j=Delta^j S_40(29)`，证书中每个 `epsilon_j>0`。对任意整数 `u>=0`，

```text
S_40(29+u)=sum_{j=0..79} epsilon_j*binom(u,j)>0,
```

因 `epsilon_0>0` 且每个 `binom(u,j)>=0`。由 `L,C_k,G_40(k)` 的正性得到上述全参数符号结论。

## 复现及证据范围

`node R517_VERIFY.js > R517_EVIDENCE.json`：本轮实际执行 `R517_EXACT_JS_PASS`。包含241个独立参数点上的精确多项式恒等式核验、20个原始40×40 Toeplitz 整数矩阵 Bareiss 行列式核验、800个原始 signed BRC 卷积与 ballot–Catalan 整数恒等式核验；80个尾部差分严格为正。全程 BigInt 精确算术。

`python R517_INDEPENDENT.py > R517_INDEPENDENT_EVIDENCE.json`：本轮用 Python 3 / SymPy 1.14 的 Berkowitz 法从 ballot–Catalan 整数公式独立构造并核验17个40×40矩阵行列式（含 `k=7/8`、`k=28/29` 两处转换边界）；另完成800组原始卷积与 ballot–Catalan 公式相等检查，返回 `R517_INDEPENDENT_PASS`。以上证据严格适用于上述定义和冻结多项式前提。

作者侧证明尚待独立数学审阅。原生研究服务未发放本次 Researcher-ID / CLAIM / Result；活跃 Owner 只读查询返回 `CONTROL_QUOTA`。P000、ACTIVE 世界观和冻结科学输入未改动。

## 下一研究问题

独立接续 `s=3,m=41` 的全正整数参数符号分类：次数界 `246`、82个 Newton 差分和247点恒等式证书。并研究固定 `k=7,8,28,29` 的有理阶数生成函数 `sum_m D_m(k)z^m=1/Q_k(z)` 的极点和共轭相位，尝试解释跨阶数变号机制。
