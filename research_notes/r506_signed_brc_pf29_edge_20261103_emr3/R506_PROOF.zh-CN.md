# R506 — signed BRC 辅助标量右缘29阶 Toeplitz 子式：精确全参数符号分类

日期：2026-11-03 · AUTHOR_SIDE_EXACT_COMPUTER_CERTIFICATE · DRIVER_UNREVIEWED · NOT_ADMITTED

## 冻结科学输入与精确定理

科学输入沿用 R462 immutable pin `18783e01e3646c72b7aab3b16d3f565e83e6446f`，接续 R505@5c6253b0efe74b1c161b553a629f08717d3450de；任务中的 P000 / ACTIVE 心跳世界保持原状。

定义对整数 `k>=1`：

```text
r=2k+1,  C_k=binom(2k,k)/(k+1)>0.
H_k(t)=binom(r+t,2t)*[x^r]((1-x)(1+x)^(2t)(1+x^2)^(r-t))
        for 2<=t<=r, and H_k(t)=0 otherwise.
D_m(k)=det(H_k(3+i-j))_(0<=i,j<m).
```

**定理（在冻结 R452/R462 多项式前提下的整数代数计算机辅助证明）**：

```text
D_29(k)>0    1<=k<=5;
D_29(k)<0    6<=k<=8;
D_29(k)>0    every integer k>=9.
```

负性恰好在 `r=13,15,17` 三个奇数点发生；自 `r=19` 起严格为正。R505 证明 `D_28(k)<0` 当 `6<=k<=12`，故 `D_28(k)<0<D_29(k)` 在 `9<=k<=12` 成立。

## 负载证明：有限证书推出无限参数

使用 R452/R462 已有前提：`p_t(k)=H_k(t)/C_k` 是 `Q[k]` 多项式，且 `deg p_t<=2t`。置 `f_m=D_m/C_k^m` 与 `f_0=1`。由 Hessenberg 末列展开：

```text
f_m = sum_(ell=1)^m (-1)^(ell-1)*p_(ell+2)*p_2^(ell-1)*f_(m-ell).
```

归纳可知 `deg f_m<=6m`：递推每个乘积的次数上界为
`(2ell+4)+4(ell-1)+6(m-ell)=6m`。所以 `deg f_29<=174`。

取严格正因子

```text
G_29(k)=[k(k+1)(2k+1)(2k+3)]^29*(k+2)>0  (k>=1);
deg G_29=117.
```

在 `k=1..58` 精确求值 `f_29/G_29`，用这58个有理数的既约分母最小公倍数 `L>0` 消去分母，构造整数前向差分 `delta_j`，`0<=j<=57`。定义

```text
S_29(k)=sum_(j=0)^57 delta_j*binom(k-1,j),    deg S_29<=57.
```

执行的 `R506_VERIFY.js` 精确验证了175个不同正整数点 `k=1..175` 的等式：

```text
L*D_29(k) = C_k^29*G_29(k)*S_29(k).
```

即 `L*f_29(k)=G_29(k)*S_29(k)`。左右都是次数至多174的有理多项式；175个不同点相等，故这是 **Q[k] 中的恒等式**。

证书逐一检查 `S_29(1..8)` 符号依次为 `+,+,+,+,+,-,-,-`。又对 `k=9` 平移求得58个差分 `epsilon_j=Delta^j S_29(9)`，**全部严格为正**。对每个整数 `u>=0`，

```text
S_29(9+u)=sum_(j=0)^57 epsilon_j*binom(u,j)>0
```

（所有二项式非负且常数系数严格正）。利用 `L,C_k,G_29>0`，定理得证。

全部 `L,delta_j,epsilon_j,S_29(1..8)` 十进制精确整数载于 `R506_EVIDENCE.json`；由同目录脚本运行 `node R506_VERIFY.js > R506_EVIDENCE.json` 可完整重建。

## 实际运行范围与独立交叉核对

主程序使用 JavaScript BigInt 精确整数运算，输出 `R506_EXACT_JS_PASS`：175项恒等式点检查，20项直接29×29 Bareiss整数行列式，以及580项原始 signed BRC 卷积和 ballot-Catalan 表达式一致性检查。

独立脚本 `R506_INDEPENDENT.py` 使用 Python/SymPy 直接构造原定义矩阵和系数卷积，在 `k=1,5,6,7,8,9,10,15` 八个点运行，符号为 `+,+,-,-,-,+,+,+`，结果 `R506_INDEPENDENT_PASS`。

本定理的全参数部分依赖冻结 R452/R462 的多项式前提、Hessenberg 递推、175点恒等式证书和58项全正平移差分。独立矩阵测试提供有限点交叉校验。该辅助标量结果以作者侧研究证书保存，原生 X6 模型推广与 Driver 审查是独立问题。

## 下一问题

1. 计算 `s=3,m=30` 的60项 Newton 差分和181点恒等式，判定全部整数参数符号。
2. 对固定 `k=6,8,9,12,13`，使用 Hessenberg 递推的有理阶数生成函数，对分母进行精确因式分解或伴随矩阵特征根隔离，探索29阶负性窗口缩小的结构原因。

## 真实研究身份与保存性质

本次 GitHub 认证身份 `awdawmip`。原生 `em_session_start` 返回 `STATIC_READONLY_SCOPE_DENIED` (`operation_sent=false`)；`em_control_tasks` 返回 `CONTROL_QUOTA`。未确认活跃 owner，未获得研究会话身份、CLAIM、Result 或 Driver review。文件仅写入已存在的 Draft PR 研究注记分支；不变更冻结科学输入、P000 或项目状态机。
