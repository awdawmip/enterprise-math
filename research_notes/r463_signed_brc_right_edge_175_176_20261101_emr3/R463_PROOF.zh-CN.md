# R463｜signed BRC 辅助标量：s=175、176 无限参数正性和 r=199 拼接

日期：2026-11-01；状态：AUTHOR_SIDE_EXACT_SYMBOLIC_AND_INTEGER / DRIVER_UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING。

## 研究输入与当前规范

规范快照：GLOBAL_KNOWLEDGE_V1 `main@34e144d7ba125c9479c3d9a0e1e0fab19c71e9b0`，Enterprise Math `main@b171147eb65e16c1bb9d4f2a2f20a3073897201f`。科学前沿沿用 R462 的不可变 pin `18783e01e3646c72b7aab3b16d3f565e83e6446f`。读取 P000、ACTIVE 世界观、项目现行 portable research 方法与当前研究协议；均未修改。执行主体 GitHub 登录为 `awdawmip`。

## 精确命题

定义奇数 `r=2k+1`，`2<=s<=r`，

`H(r,s)=binom(r+s,2s)*[t^r]((1-t)(1+t)^(2s)(1+t^2)^(r-s))`。

置 `a_j=H(r,r-j)` (`0<=j<=r-2`)，越界置零；`D2_j=a_j^2-a_(j-1)*a_(j+1)`，`D3_j=det(a_(j+v-i))_(i,v=0..2)`。

**定理 R463-A：** 对每个 `s in {175,176}`、每个整数 `k>=floor((s+2)/2)`，令 `r=2k+1`、`j=r-s`，则 `D2_j>0` 且 `D3_j>0`。

## 完整系数证书与推导

令 `C_k=binom(2k,k)/(k+1)>0`，`B_t(k)=H(2k+1,t)/C_k`。引用冻结 R452/R462 的 EOR 恒等式：

`(2t)! B_t(k)=E_t(k) O_t(k) R_t(k)`，其中

`E_t=prod_(v=0..t-1) 2(k+1-floor(t/2)+v)`；

`O_t=prod_(v=0..floor(t/2)) (2k+2v+1)`；

`R_t=sum_(q=0..floor((t-1)/2)) binom(t-1,2q)*2^q*prod_(v=q..floor((t-1)/2)-1)(2k-2v-1)*prod_(d=0..q-1)(k+1-d)`。

对每个 s，取 `k0=floor((s+2)/2)`、`u=k-k0>=0`、`F=(2s+4)!`，定义 `Q_t(u)=F B_t(k0+u)`，`t=s-2,...,s+2`。记 `A=Q_s,B=Q_(s-1),C=Q_(s+1),D=Q_(s-2),E=Q_(s+2)`。

则 `P2=A^2-BC`，`P3=A^3-2ABC+DC^2+B^2E-DAE`，并且 `D2_j=C_k^2*P2/F^2`、`D3_j=C_k^3*P3/F^3`。证明核验：在 `Z[u]` 内完整展开 `P2,P3`；对两者的每一个整数系数作严格正判号，再逐系数验证恒等式 `A P3=P2^2-(B^2-DA)(C^2-AE)`。因此 `u>=0` 时两多项式都正。

| s | k0 | deg P2 | deg P3 | 严格正系数总数 | 精确系数流 SHA256 |
|---:|---:|---:|---:|---:|---|
| 175 | 88 | 700 | 1050 | 1752 | `5a68b3d2ced114ee7744e5a75b8553717314a3d0ea1b5b497b0739ba09847239` |
| 176 | 89 | 704 | 1056 | 1762 | `418eaf75094b247defaabe4ace9fc9f435f5e8e99739827df7663fb4e4a19170` |

总计四个多项式、**3514 个整数系数全部严格为正**，完成两项 `Z[u]` Desnanot–Jacobi 恒等式。每个 s 在 `k0,k0+1`，对五个邻近 t 各与原始带符号卷积及独立 Catalan 表达式比对，合计 20 项原始、20 项正 Catalan 整数等式。以上均采用任意精度整数。

执行细节：s=175 由 `R463_VERIFY.py` 通过（`R463_EXACT_PASS`）；s=176 由 R462 已发布的同一数学内核 `R462_VERIFY.py 176 176` 通过（`R462_EXACT_PASS`）。R463 是保留该内核、仅修改输出标签及证据文件名的版本。其一轮重新执行 s=176 时工具执行超时，未将该尝试记为通过。s=177 的扩展尝试也未完成，不作为本轮证书。

## r=199 的整行交叉验证与拼接

既有作者侧 R447 左缘证明给出所有奇数 r>=99 的 `0<=j<=22`；R452—R462 的作者侧右缘证明覆盖 `2<=s<=174`。本轮升至 176。对于 r=199，`j>=23` 等价于 `s=r-j<=176`；与左缘合起来覆盖全部合法 `0<=j<=197`。在 R447、R450、R452 等既有作者侧引理与判据成立的前提下，得到 **半无限辅助 Toeplitz 矩阵 `T^(199) in PF3`**；前序链故扩展至所有奇数 `99<=r<=199`。

另用直接 Catalan 整数公式建立 r=199 的整行，逐位置核验 a_j、D2_j、D3_j 各198个，共 **594 项精确整数严格正**；并与原始带符号卷积及交替 Catalan 式各核对8项。该固定 r 的整行检查独立于上述无限参数多项式全系数判号，完整结果见 `R463_EVIDENCE.json`，源码见 `R463_ROW_VERIFY.py`。

## 复现、来源与待解问题

在同目录执行 `python R463_VERIFY.py 175 175`、`python R463_VERIFY.py 176 176` 和 `python R463_ROW_VERIFY.py`；s176 本轮已完成结果来自等价数学内核 `R462_VERIFY.py 176 176`，对应冻结 R462 文件及本轮证据摘要。首次提交前由 GitHub 导入原始 R462 代码并局部修改，远端回读核对新脚本 Git blob。

证书范围是 signed BRC **辅助标量模型**。其相对原生 X6 动力学的嵌入、声明观察算子与后续运算保真仍需单独证明。R447/R450/R452 依赖及全矩阵 PF3 拼接尚待独立 Driver 审查。当前原生控制入口报告 `research_authority_granted=false`、`CODE_REVIEW_REQUIRED`，Owner 清单返回 `CONTROL_QUOTA`，未取得 CLAIM 或正式 Result。

**下一研究单元：** s=177,178 的 `P2,P3` 全系数证书与 `r=201` 直接整行检查；若发生非正系数，再检查实际合法 k 的符号，分离证书方法边界与真反例。同时寻求 EOR/Turán 对 s,k 同时无界的统一下界。
