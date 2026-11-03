# R515 — signed BRC 辅助标量：s=3，三十八阶 Toeplitz 子式全正整数符号分类

2026-11-04。冻结科学输入：R462 @ `18783e01e3646c72b7aab3b16d3f565e83e6446f`；前沿：R514 @ `513658f3a928ee4036cf21b060b1928bdc67afb3`。

状态：**AUTHOR_SIDE_EXACT_COMPUTER_CERTIFICATE / DRIVER_UNREVIEWED / NOT_ADMITTED**。

## 定义与定理

令 k 为正整数，r=2k+1，C_k=binom(2k,k)/(k+1)>0。冻结 signed BRC 辅助标量定义：

```text
H_k(t)=binom(r+t,2t)*[x^r](1-x)(1+x)^(2t)(1+x^2)^(r-t),  2<=t<=r;
H_k(t)=0, otherwise;
D_m(k)=det(H_k(3+i-j))_(0<=i,j<m), D_0(k)=1.
```

假设冻结 R452/R462 已有的代数前提：p_t(k)=H_k(t)/C_k∈Q[k] 且 deg p_t≤2t。则对 **全部正整数 k**：

```text
D_38(k)>0  for 1<=k<=12;
D_38(k)<0  for k>=13.
```

即三十八阶在 r=3,5,...,25 均严格为正，自 r=27 起对奇数 r 永久严格为负。结合 R514：D_37(k)>0>D_38(k) 对 13<=k<=22 成立。

## 完整精确计算机辅助证明

设 f_m(k)=D_m(k)/C_k^m，f_0=1。对 s=3 的 Toeplitz–Hessenberg 矩阵展开第一行并逐项化简，得

```text
f_m(k)= Σ_(a=1..m) (-1)^(a-1) p_(a+2)(k) p_2(k)^(a-1) f_(m-a)(k).
```

已知 deg p_(a+2)≤2a+4、deg p_2≤4，归纳得 deg f_m≤6m，特别是 deg f_38≤228。

取在正整数域严格正的
```text
G_38(k)=[k(k+1)(2k+1)(2k+3)]^38*(k+2), deg G_38=153.
```

在 k=1..76 精确构造 f_38(k)/G_38(k)，令 L 为约分分母的最小公倍数。其76个整数化样本的 Newton 前向差分 δ_0,..,δ_75 与 L 保存在 `R515_EVIDENCE.json`。定义
```text
S_38(k)= Σ_(j=0..75) δ_j binom(k-1,j), deg S_38<=75.
```
本次 BigInt 程序逐点精确核对全部 229 个 **不同整数** k=1..229：
```text
L D_38(k) = C_k^38 G_38(k) S_38(k).
```
在冻结多项式前提下，除以 C_k^38 后两侧是次数至多228的 Q[k] 多项式；229个不同点相等推出全参数恒等式
```text
L f_38(k)=G_38(k) S_38(k) .
```

证书存储的 k=1..12 的 S_38(k) 精确整数值均 **严格为正**。以 k=13 平移的76项前向差分 ε_j=Δ^j S_38(13) **全部严格为负**。故每个整数 u≥0 有
```text
S_38(13+u)= Σ_(j=0..75) ε_j binom(u,j)<0,
```
因为 binom(u,j)≥0 且 ε_0<0。最后 L,C_k,G_38(k)>0，得上述无穷参数定理。

## 精确验证范围、来源、限制

`node R515_VERIFY.js > R515_EVIDENCE.json` 已实际执行：`R515_EXACT_JS_PASS`，包括229项多项式恒等式整点核验，20个原始38×38 Bareiss 精确行列式，以及760项有符号原始卷积/ballot-Catalan 恒等式（k=1..20,t=2..39）。`python R515_INDEPENDENT.py > R515_INDEPENDENT_EVIDENCE.json` 已在独立 Python 实现执行：`R515_INDEPENDENT_PASS`，通过 Python math.comb、ballot-Catalan 展开及 SymPy Berkowitz 直接构造12个38×38原始矩阵：k=1,2,5,6,7,8,11,12,13,14,22,38；另交叉验证760项原始 signed BRC 系数。两条路径全部为精确整数运算。

结论依赖上述冻结的多项式前提及确切的计算证书，属于 signed BRC 辅助标量模型内的作者侧条件性计算机辅助证明；正式 Result、独立 Driver 数学审阅及采纳仍待完成。P000、ACTIVE 世界观与冻结源保持原值。

## 下一问题

研究 s=3,m=39，先尝试78项 Newton 插值和235个整点的多项式证书，分类全部正整数参数。并在 k=12、13、22、23 研究固定 k 的有理阶数生成函数主导极点和共轭相位，寻求不同阶数的符号转折机制。
