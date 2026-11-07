# R505 — signed BRC 辅助标量右缘 28 阶 Toeplitz 子式全参数符号分类

2026-11-03 · AUTHOR_SIDE_EXACT_COMPUTER_CERTIFICATE · DRIVER_UNREVIEWED · NOT_ADMITTED

## 冻结对象与结论

科学输入沿用 R462 immutable pin `18783e01e3646c72b7aab3b16d3f565e83e6446f`，接续已持久化的 R504 `e2535d803c6b1ab41c28b39d1f6b11914af0e40b`。本工作仅涉及 signed BRC 辅助**标量**核的整数代数，不改变 P000 / ACTIVE 心跳世界 / X6 原生观察或来源隔离。

对整数 `k>=1`，设 `r=2k+1`、`C_k=binom(2k,k)/(k+1)>0`；对 `2<=t<=r` 定义

```text
H_k(t) = binom(r+t,2t) * [x^r](1-x)(1+x)^(2t)(1+x^2)^(r-t),
H_k(t)=0 otherwise.
D_m(k) = det( H_k(3+i-j) )_(0<=i,j<m).
```

**定理（冻结 R462 多项式前提下的精确计算机辅助结论）**：对每个正整数 `k`，

```text
D_28(k)>0  for 1<=k<=5;
D_28(k)<0  for 6<=k<=12;
D_28(k)>0  for every k>=13.
```

负性参数对应 `r=13,15,17,19,21,23,25`，自 `r=27` 起恒严格为正。结合 R504 的 `D_27(k)<0` 对 `6<=k<=25`，得到 `D_27(k)<0<D_28(k)` 对 `13<=k<=25`。

## 多项式结构与无限参数证书

复用冻结 R452/R462 科学前提：`p_t(k)=H_k(t)/C_k` 是 `Q[k]` 中多项式，且 `deg p_t<=2t`。设 `f_m=D_m/C_k^m`、`f_0=1`；Hessenberg 展开为

```text
f_m(k)=sum_(ell=1)^m (-1)^(ell-1) p_(ell+2)(k) p_2(k)^(ell-1) f_(m-ell)(k).
```

归纳：任一项次数不超过 `(2ell+4)+4(ell-1)+6(m-ell)=6m`，从而 `deg f_28<=168`。

引入严格正归一化因子

```text
G_28(k)=[k(k+1)(2k+1)(2k+3)]^28 (k+2)>0,  k>=1,
deg G_28 = 113.
```

在 `k=1,...,56` 精确计算有理数 `f_28/G_28`。将其既约分母最小公倍数记为 `L>0`，令 `v_k=L f_28(k)/G_28(k)`；取全部 56 项前向差分 `delta_j=Delta^j v_1`，构造整数系数 Newton 多项式

```text
S_28(k)=sum_(j=0)^55 delta_j * binom(k-1,j).
```

`R505_VERIFY.js` 对 `k=1,...,169` 的每个点验证精确等式

```text
L*D_28(k)=C_k^28 * G_28(k) * S_28(k).
```

除以正数 `C_k^28` 后，`L*f_28` 与 `G_28*S_28` 是次数不超过 168 的有理多项式。它们在 169 个不同整数点相等，故**对所有参数恒等**。这个步骤把有限精确计算提升为整式恒等式，前提和次数界均已明确。

证书精确给出 `k=1,...,12` 的 `S_28(k)` 符号：`(+,+,+,+,+,-,-,-,-,-,-,-)`。再令 `epsilon_j=Delta^j S_28(13)` (`0<=j<=55`)。重新计算所得 **56 个整数 epsilon_j 全部严格为正**。对任意整数 `u>=0`，

```text
S_28(13+u)=sum_(j=0)^55 epsilon_j * binom(u,j)>0,
```

因为二项式基底非负且 `epsilon_0>0`。由 `L,C_k,G_28>0`，得到上述完整符号分类。所有 `L`、`delta_j`、`epsilon_j`、前 12 点值均在 `R505_EVIDENCE.json`；证书可由 `node R505_VERIFY.js > R505_EVIDENCE.json` 完整复算。

## 已执行核验及证据等级

实际以 JavaScript BigInt 整数算法进行精确运算；返回 `R505_EXACT_JS_PASS`，证书覆盖 **169 项恒等式点检查、20 项独立原始 28×28 Bareiss 行列式核验、580 项 signed BRC 原卷积与 ballot-Catalan 等价式核验**。远端发布的 `R505_VERIFY.js` 在同一 JavaScript 精确算术环境重新执行，也返回同一符号分段与全部证书计数。

另以单独的 `R505_INDEPENDENT.py` (Python + SymPy) 经另一 kernel 形式直接建立 28×28 矩阵，在 `k=1,5,6,7,12,13,14,20` 八个点计算确切行列式，符号依次 `+,+,-,-,-,+,+,+`，返回 `R505_INDEPENDENT_PASS`。此独立检查是有限点交叉验证；全参数结论使用的是整式次数界与 56 项全正 Newton 系数证书。

当前成果为作者侧计算机辅助证明；正式原生 CLAIM/Result、独立 Driver Review 与数学接纳仍按既有权威路径办理。原生会话申请实际返回 `STATIC_READONLY_SCOPE_DENIED` (`operation_sent=false`)，活跃 Owner 列表查询返回 `CONTROL_QUOTA`，故此次只在既有 Draft PR 的非规范研究注记分支持久化，并未声称获得新任务控制权限。

## 后续问题

继续 `s=3,m=29`：可尝试 58 项 Newton 差分与 175 个整数点整式恒等式证书。并比较固定 `k=6,12,13,25,26` 的有理阶数生成函数分母及主导极点，解释 27 阶与 28 阶不同的符号恢复阈值。保留跨阶数统一定理作为后续研究问题。
