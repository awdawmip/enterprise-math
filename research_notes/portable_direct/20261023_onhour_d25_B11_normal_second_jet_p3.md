# D25 B11 法向二阶喷流：模 \(p^3\) 的精确缺陷端口

- 证据状态：**AUTHOR_EXACT_DERIVATION / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NO_FORMAL_CLAIM**。
- 作者来源：本轮 `TASK_RESEARCH` 数学推演；逻辑 lane 标签 `chatgpt-research-onhour-enterprise-math-20260923` 仅用于溯源，**不声明拥有 Source session/CLAIM/run 权限**。共享已暴露 D25/B11 上下文，不主张审阅独立性。
- 母任务：`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`；已公布任务版本 `TP2-B6F4FC938FF94941C1B7`。本文不是新任务、Task checkpoint、Result 或既有冻结证据的改写。
- 复用的前沿：`research_notes/directed_recovery/20260926_13C1B7/math/D25_LOCAL_PROGRESS.md`（旧结果证明模 \(p^2\) 第一法向修正），及旧 B11 有限 contiguous-Dixon 载体；Source 控制读 pin `6df6ca9470bdfbce5cabd4d3a6b5e460a5737072`，本轮 GLOBAL_KNOWLEDGE_V1 读 pin `7a56e3a5a31c6af97f47a09befb54ae4443c9b41`。冻结任务的原 pin 不因本说明而更改。
- 数学范围：外部辅助有理数/模素数算术；不作为心跳世界原生六维状态运算、不引入原生几何平面、不声称真实 native BRC benchmark 已执行。

## 1. 精确问题与新公式

令 \(p=6m+1\) 为素数，\(m\ge1\)，\(a=-1/3\)，\(d=m+2/3\)，\(x=p/3\)，并沿用旧 B11 有限和
\[
F_m(a,d)=\sum_{j=0}^{m}\frac{(-m)_j}{(d)_j}\frac{a}{a+j},\qquad
S_m=F_m(a,d+x),\qquad C_m=F_m(a,d).
\]
前任精确结果已给出 \(C_m=1+a\sum_{r=0}^{m-1}[(a+2r+2)^{-1}-(a+2r+1)^{-1}]\) 及
\(S_m-C_m\equiv(p/3)N_m\pmod{p^2}\)。本单元**不重证**此 B11 闭式。

保留每一支 \(j\) 的精确权重、法向信息和赋值：
\[
w_j=\frac{(-m)_j}{(d)_j}\frac{a}{a+j},\quad
H_j=\sum_{\ell=0}^{j-1}\frac1{d+\ell},\quad
E_j=\sum_{\ell=0}^{j-1}\frac1{(d+\ell)^2},\quad
N_m=-\sum_{j=0}^m w_j H_j,
\quad
T_m=\sum_{j=0}^m w_j(H_j^2+E_j).
\]
空和为零。**新增模 \(p^3\) 二阶法向端口**：
\[
\boxed{S_m\equiv C_m+\frac p3N_m+\frac{p^2}{18}T_m\pmod{p^3}.}\tag{A}
\]
因此，旧一阶修正后尚存的第二个精确 p-adic digit 是
\[
\boxed{\frac{S_m-C_m-(p/3)N_m}{p^2}\equiv\frac{T_m}{18}\pmod p.}\tag{B}
\]
\(N_m\) 是旧法向双极矩端口；\(T_m\) 是**新的带支路来源的法向二阶矩**，绝非已审定的 LOW/Beta → B11 全局拼接结果。

## 2. 全 \(m\) 代数证明与合法赋值

在 \(j\le m\) 时，\(d+\ell=(3m+2+3\ell)/3\) 的分子范围为 \(3m+2,3m+5,\dots,6m-1=p-2\)，无项被 \(p\) 整除；\(a+j=(3j-1)/3\) 也为 \(p\)-单位，\(j!\) 为 \(p\)-单位。因此 \(w_j,H_j,E_j\in\mathbf Z_{(p)}\)。

对单支保持原分母因子，不先压成总量：
\[
\frac{(d)_j}{(d+x)_j}
=\prod_{\ell=0}^{j-1}\left(1+\frac{x}{d+\ell}\right)^{-1}
\equiv 1-xH_j+\frac{x^2}{2}(H_j^2+E_j)\pmod{x^3\mathbf Z_{(p)}}.
\]
系数来自有限乘积的逐支展开；所有分母均是 \(p\)-单位。乘 \(w_j\) 并对固定有限支集合 \(j=0,\dots,m\) 求和即得到 (A)，取 \(x=p/3\) 后 (B) 也成立。此论证对**每一个满足条件的素数**成立，而非九素数回归拟合；它没有证明 \(T_m\) 会被完整 LOW 残差抵消。

## 3. 显式反例：不能只用一阶法向修正声称模 \(p^3\) 闭合

在 \(p=13,m=2\)：
\[
S_2=159/140,\quad C_2=587/440,\quad
N_2=-4419/38720,\quad T_2=135459/1703680.
\]
直接化简得
\[
\frac{S_2-C_2-(13/3)N_2}{13^2}=\frac{95}{54208}
\equiv 11\pmod{13};
\qquad T_2/18\equiv11\pmod{13}.
\]
因此原一阶 port **模 \(13^2\) 足够、模 \(13^3\) 不足**。模 \(13^3\) 读数 \(S_2\equiv519\)；加二阶 \(T_2\) 的 (A) 也给 \(519\)，只加一阶项给 \(857\)。这是针对“在下一位忽略法向二阶喷流”的**精确否证**，不是针对 D25 或 Dixon 恒等式的否证。

## 4. 实际验证、BRC 信息保留及残余

本轮以 Python `fractions.Fraction` 逐支独立构造原始移位和 \(F_m(a,d+p/3)\) 与右式；在 \(p=7,13,19,31,37,43,61,67,73\) 全部核验 (A) 的差为 \(p^3\mathbf Z_{(p)}\)，并核对前任 \(C_m\) 闭式。九个 `PASS` 只核对所列有限输入，**全素数结论由上面的有理恒等式证明，不由数值回归推出**。尚未运行原 Task native benchmark、Lean checker、独立审阅，未产生 canonical checkpoint/Result。

BRC 的精确类型复用（`REUSE_APPLIED`）：population 为 \(j=0,\dots,m\) 的带标号 finite branches；载体为 \((w_j,H_j,E_j,v_p)\) 与参数方向 \(d\mapsto d+p/3\)；观察器为模 \(p^3\) 的 B11 读数；允许操作为逐支乘积、Taylor 二阶及带支路求和。若只保存 \(C_m\) 或一阶 \(N_m\)，就抹去决定第二 p-digit 的 \(T_m\)；带符号有理求和不能误称正 BRC 质量。源定义位于原生 X6 项目中并不使这段外部辅助分式成为 X6 动力学证明。

**下一最小科学单元**：从已冻结 D25/LOW 的确切输入构造带 \(j\) 标号的参数方向映射，逐项提取 \(T_m/18\) 与 LOW 高带、\(b_1J_m\)、Dixon 双极项之间的对应系数，证明所需抵消或把一个具体非零余项留在第二位。必须保留特殊 \(k=m\) 支、I1/I2 源和原生 benchmark/证书欠项。不能把 (A) 当作完整 SECOND-DIGIT-LIFT、已接纳结果或原实验已执行。

**控制接续（只读事实）**：Research lane 的 recovery/status 以桥接 Issue #6186 为准：旧 Source 未验证 ACTIVE 投影、无自身合法 claim/run；精确 D25 continuation 请求 #6187 被桥拒绝 `PREREQUISITE_NOT_SUCCEEDED`；派发请求 #6188 当前可能仍在排队，须按原 `request_id` 回读其最新 receipt。相关身份缺陷已有控制支持 Issue #1539。本文件独立保全数学证据，不尝试替这些请求授权、close、CLAIM 或 freeze。
