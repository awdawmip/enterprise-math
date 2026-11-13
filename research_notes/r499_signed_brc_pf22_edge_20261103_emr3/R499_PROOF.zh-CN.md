# R499 — signed BRC 右缘二十二阶 Toeplitz 子式的全整数符号分类

Date: 2026-11-03. Status: **AUTHOR_SIDE_EXACT_SYMBOLIC; Driver unreviewed / not admitted**.
Scientific input: frozen R462 pin `18783e01e3646c72b7aab3b16d3f565e83e6446f`.
Predecessor: R498 at `2cc1acfcdf28e0d73aa1d2d1fba2e2a13c424bf7`, Draft PR #1708.

## 模型、定理和母问题

对正整数 k，令 r=2k+1、C_k=binom(2k,k)/(k+1)，并用冻结的 signed BRC 分支保真标量

```text
H_k(t) = binom(r+t,2t)[x^r](1-x)(1+x)^(2t)(1+x^2)^(r-t)   (2<=t<=r),
H_k(t) = 0                                                   (otherwise),
D_m(k) = det[H_k(3+i-j)]_(0<=i,j<m).
```

**定理（R499）**：对每个整数 k>=1，
```text
D_22(k)>0  for 1<=k<=5 or k>=9;
D_22(k)<0  for 6<=k<=8.
```
所以二十二阶子式在 r=13、15、17 三个奇数参数处为负，自 r=19 起永久严格为正。与 R498 的二十一阶分类比较，`D_21(k)<0<D_22(k)` 对 9<=k<=14 成立。母问题是理解 signed BRC 辅助标量的 Toeplitz 必要子式随秩和奇数参数变化的符号结构及相消机制。

## 精确推导

令 `p_t(k)=H_k(t)/C_k`。冻结路线的精确多项式恒等式为：

```text
p_t(k) = sum_{q=0}^{floor((t-1)/2)}
 [4^q binom(t-1,2q)/(2t)!]
 product_{h=0}^{q-1}(k-h)(k+1-h)
 product_{e=2-t,...,t+1; e not in {1-2q,...,0}}(2k+e).
```

置 `f_0=1`、`f_m=D_m/C_k^m`。Hessenberg Toeplitz 展开给出

```text
f_m(k)=sum_{ell=1}^m (-1)^(ell-1) p_{ell+2}(k)p_2(k)^(ell-1)f_{m-ell}(k).
```

该递推在 Q[k] 精确构造 `f_22`（度132），并经零余数整除及133项有理系数恒等式得到：

```text
f_22(k) = G_22(k) P_22(k) / N_22,
G_22(k) = k^22 (k+1)^22 (k+2) (2k+1)^22 (2k+3)^22,
N_22 = 242868740292635721884684180260913391106665070338645861295435284480000000000000000000000.
```

`P_22` 是43次本原整数多项式，其全部44个升幂系数记录在 `R499_EVIDENCE.json:p22_ascending`。对 k>=1，`C_k,G_22(k),N_22` 严格正，故 D_22 的符号与 P_22 一致。

## 全域符号证书

将 `P_22(9+u)=sum_{j=0}^{43} b_j u^j`，其中
`b_j=sum_{i=j}^{43} a_i binom(i,j)9^(i-j)`。完整的44个 `b_j` 保存在 `R499_EVIDENCE.json:shifted_tail_coefficients_ascending`，且严格为正，最小系数为
`31675550280390144131438302211488283511318642688`。
故对所有实数 u>=0，P_22(9+u)>0。

对 k=1,...,8，通过精确整数 Horner 法核验全部边界值，证书列示每一项，且符号依次为 `+++++---`。由正因子归约、完整移位系数、全部边界值，定理对所有正整数 k 成立。证书亦由独立 JS BigInt 重建全部44项移位系数与8项边界值，与 Python 精确输出一致。

## 执行范围与独立核查

实际本地执行 Python 标准库 `int` / `Fraction`：返回 `R499_EXACT_PASS`；133项完整多项式系数核对、460项原始 signed BRC 卷积核验（k=1,...,20，t=2,...,24）、20项从原始整数 H 构造的22×22 Bareiss 行列式交叉核对，以及22项固定 k=2 的阶数递推校验。全程无浮点近似。无限参数结论来自完整多项式恒等式与平移系数证书，有限原始行列式是独立交叉验证。验证程序可直接重建证书，证据 JSON 保存全部决定性整数。

BRC 复用：采用现有 signed branch convolution 与 Hessenberg Toeplitz scalar observer（`REUSE_EXECUTED`），保留有符号相消；本定理作用于冻结 R462 的辅助标量必要子式，未主张 native X6 整体全正性或对其它观察层的提升。P000 和 ACTIVE 世界观未修改。

## 下一精确问题

计算 `s=3,m=23` 在全部 k>=1 上的符号；并用固定 k 的有理阶数生成函数的极点与递推解释 m=20、21、22 的符号阈值变化。检查新构造是否需保留额外的分支/相位观察量。
