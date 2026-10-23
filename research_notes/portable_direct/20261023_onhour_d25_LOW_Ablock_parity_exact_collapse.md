# D25/LIFT — LOW 二阶纯 A 分量的全 m 精确消去与目标素数类别分裂

**日期 / 研究交付**：2026-10-23。作者在 TASK_RESEARCH 所用独立可移植数学证据；**AUTHOR-PROVED EXACT IDENTITY / EXACT FRACTION CROSSCHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT / NO_FORMAL_CLAIM / NOT_NATIVE_BENCHMARK**。数学证明仅使用通常整数、有限二项式与形式幂级数，并非 Enterprise Math P000 的证明或新公理。

**母目标**：D25/SECOND-DIGIT-LIFT；已知 Task publication TP2-B6F4FC938FF94941C1B7，原生冻结 Source pin c47e13e4aba0e006366f989d6334d443f6333ae3。当前项目 main 在写前核验为 437c23344107b562abc0df00aed580c269eb15d3，不能覆盖该冻结 pin。Research ordinary-control 逻辑 lane 为 chatgpt-research-onhour-enterprise-math-20260923；与 maintenance lane 完全分离。作者已读 LOW/B11/WZ 既有材料，并非独立审阅者。

**继承而不重做**：已有 WZ/B11 boundary 和 D24 frozen；已证 LOW/Beta 中的线性 L_n 消去、二阶高段 Beta adjoint 与端点 611 素数的有限精确检验。来源：
- research_notes/portable_direct/20261023_onhour_d25_LOW_linear_harmonic_beta_shift.md
- research_notes/portable_direct/20261023_onhour_d25_endpoint_padic_stream_611.md
- research_notes/directed_recovery/20260926_13C1B7/sources/hourly_new/fb9aba8a-6fb9-411b-920b-9bb376d16cd5.md

## 1. 精确要消去的对象

令 m≥1、p=6m+1，b_n=(-1)^n binom(m,n)/2^n，w_n=6n−1，且

\[
A_n=H_m-H_{m-n},\quad A_n^{(2)}=H_m^{(2)}-H_{m-n}^{(2)},\qquad
B_n=H_{2m}-H_{2m-n},\quad C_n=H_{4m}-H_{4m-n}.
\]

以 B_n^{(2)}, C_n^{(2)} 表示对应的二次调和差。LOW 先前已明确得到

\[
L_n=-\frac12 A_n+\frac23B_n+\frac13 C_n,\quad
K_n=-\frac18 A_n^{(2)}+\frac49B_n^{(2)}+\frac5{18}C_n^{(2)},\quad
M_n=K_n+\frac12L_n^2.
\]

原先仍未完成的二阶项是
\[
\mathsf M_m=\sum_{n=0}^m b_nw_n M_n.
\]

将纯粹来自负整数锚 -m 的二阶对角项**精确**剥离：

\[
M_n=\frac18\bigl(A_n^2-A_n^{(2)}\bigr)+\widetilde M_n,
\]

\[
\boxed{\begin{aligned}
\widetilde M_n={}&\frac29 B_n^2+\frac49B_n^{(2)}
+\frac1{18}C_n^2+\frac5{18}C_n^{(2)}
-\frac13A_nB_n-\frac16A_nC_n+\frac29B_nC_n.
\end{aligned}}
\]

这不是将二阶相关性置零；A–B、A–C、B–C 的交叉信息完整留在 \widetilde M_n 中。定义

\[
\mathsf A_m:=\frac18\sum_{n=0}^m b_nw_n\bigl(A_n^2-A_n^{(2)}\bigr).
\]

则 \(\mathsf M_m=\mathsf A_m+\sum b_nw_n\widetilde M_n\) 是完全精确恒等式。

## 2. 全体正整数 m 的证明：有限 binomial 二次参数导数

考虑形式多项式
\[
F_m(z,\varepsilon)=\sum_{n=0}^{m}(-1)^n\binom{m+\varepsilon}{n}z^n.
\]
对每个 n≤m，二阶参数导数恰为
\[
\left.\partial_\varepsilon^2\binom{m+\varepsilon}{n}\right|_{\varepsilon=0}
=\binom mn \left(A_n^2-A_n^{(2)}\right).
\]
因此
\[
\left.\partial_\varepsilon^2 F_m(z,\varepsilon)\right|_0
=[z^{\le m}]\bigl((1-z)^m\log^2(1-z)\bigr),
\]
其中方括号明确表示在 z=0 的形式幂级数中仅保留次数不高于 m 的项。并不把有限和错当无截断的 \((1-z)^{m+\varepsilon}\)。

通过 \(\log(1-z)=-\log(1+z/(1-z))\) 及形式幂级数恒等式
\[
\log^2(1+u)=2\sum_{j\ge2}\frac{(-1)^jH_{j-1}}j u^j,
\]
得到
\[
\boxed{\left.\partial_\varepsilon^2F_m(z,\varepsilon)\right|_0
=2\sum_{j=2}^m\frac{(-z)^j(1-z)^{m-j}}j H_{j-1}
\quad\pmod {z^{m+1}}.}
\]
取权重算子 D=6z\,\partial_z−1，在 z=1/2 时每个非零 j 支路满足
\[
\left.D\!\left((-z)^j(1-z)^{m-j}\right)\right|_{1/2}
=2^{-m}(-1)^j(12j-p).
\]
所以获得严格有限有理恒等式：

\[
\boxed{\displaystyle
\mathsf A_m=
\frac1{2^m}
\left[
3\sum_{j=2}^{m}(-1)^jH_{j-1}
-\frac{p}{4}\sum_{j=2}^{m}\frac{(-1)^jH_{j-1}}j
\right],\qquad p=6m+1.
}\tag{A-COLLAPSE}
\]

这里没有剩余的 \(A_n^2\)、\(A_n^{(2)}\) 或双重 n–k 求和。形式恒等式对所有整数 m≥1 都成立，不要求 p 是素数。

## 3. 模 p 的**类别差异**，直接对应 D25 frozen prime classes

当 p=6m+1 是素数时，所有出现的 j≤m、2^m、4 都是 p-单位；故 A-COLLAPSE 的第二项属于 \(p\mathbb Z_{(p)}\)。LOW 的第二位只需要 \(\mathsf A_m\bmod p\)：

\[
\mathsf A_m\equiv\frac3{2^m}T_m\pmod p,
\quad T_m:=\sum_{j=2}^m(-1)^jH_{j-1}.
\]

改变有限求和顺序并使用交错调和式
\[
T_m=\frac12\left((-1)^mH_{m-1}
+\sum_{k=1}^{m-1}\frac{(-1)^{k+1}}k\right),\quad
\sum_{k=1}^{m-1}\frac{(-1)^{k+1}}k=H_{m-1}-H_{\lfloor(m-1)/2\rfloor},
\]
严格得到

\[
\boxed{
\mathsf A_m\equiv
\begin{cases}
\dfrac3{2^m}\left(H_{m-1}-\dfrac12H_{m/2-1}\right),&m\ {\rm even},\\[2mm]
-\dfrac3{2^{m+1}}H_{(m-1)/2},&m\ {\rm odd}
\end{cases}
\pmod p.}\tag{PARITY}
\]

这两个分支恰好精确覆盖冻结任务的目标类别：
- p≡13 (mod24) ⇒ m≡2 (mod4) ⇒ 使用 even 支；
- p≡19 (mod24) ⇒ m≡3 (mod4) ⇒ 使用 odd 支。

即便纯 A 二阶块看似包含平方与二次调和数，在最终第二位观察器下它已经**严格压缩成单阶调和数，且两个真实目标素数类别的读出不同**。这个 parity 不能从同一个未经证明的“二阶相消”假设消掉。

## 4. 与尚未闭合的 LOW/Beta 单残差的精确组合

沿用既有 LOW 结果的定义 \(C_m,V_m,J_m^{(2)},\Theta_m,\mathcal A_m,\chi_p\)，已有

\[
\mathscr D_m^{\rm beta}=
\frac{\mathcal A_m\Theta_m-1}{p}
+\mathcal A_m\bigl(2^{-m}C_m-2V_m+\mathsf M_m+J_m^{(2)}\bigr)-\chi_p.
\]

本轮无损替换为
\[
\boxed{\begin{aligned}
\mathscr D_m^{\rm beta}\equiv&
\frac{\mathcal A_m\Theta_m-1}{p}
+\mathcal A_m\Bigl(2^{-m}C_m-2V_m+J_m^{(2)}
+\sum_{n=0}^{m}b_nw_n\widetilde M_n
+\mathsf A_m^{\rm parity}\Bigr)-\chi_p\pmod p,
\end{aligned}}\tag{LOW-A}
\]
其中 \(\mathsf A_m^{\rm parity}\) 是 PARITY 右端。原 first-digit 可除性和各分母 p-unit 仍是引用的已证前提；本证明未声称自行重证它们。

**真正尚未完成**：\(\widetilde M_n\) 的 B/C 纯块与三类混合项、反射 \(J_m^{(2)}\)、全区间 \(V_m\)、以及 divided first digit 的**联合**抵消。PARITY 不是该联合同余的证明，也不是 Source Result。下一精确动作应以这个更短 LOW-A 与已证 contiguous-Dixon/B11 的同一 harmonic observer 逐项匹配，优先消除 B/C–reflected 的共有部分；禁止把只消去 A 块说成完整 LIFT 证明。

## 5. 精确核验（作者自检，非独立审阅）

使用 Python 3 标准库 Fraction，以两套构造分别计算 \(\mathsf A_m\)：
(1) 直接对每个 n 计算二项式、\(A_n,A_n^{(2)}\)；
(2) A-COLLAPSE 的 j 单和。不使用浮点，m=1,...,16 **逐个作为有理数严格相等**。
另对下述 11 个素数检查 PARITY；表中为纯 A 块模 p 的值，而**非**完整二阶 residual：

| p | m | 纯 A 块 mod p |
|---:|---:|---:|
| 7 | 1 | 0 |
| 13 | 2 | 4 |
| 19 | 3 | 1 |
| 31 | 5 | 21 |
| 37 | 6 | 21 |
| 43 | 7 | 35 |
| 61 | 10 | 10 |
| 67 | 11 | 48 |
| 73 | 12 | 2 |
| 79 | 13 | 32 |
| 97 | 16 | 92 |

独立的有理见证：m=1 时 \(\mathsf A_1=0\)，m=2 时 \(\mathsf A_2=11/32\)，m=3 时 \(\mathsf A_3=-3/16\)，m=5 时 \(\mathsf A_5=-247/3072\)。其中 p=13、19 的目标类别 \(\mathsf A_m\) **均非零 mod p**；这给出了“二阶 A 块可以直接忽略”捷径的精确反例。全 m 的证明在第 2、3 节，有限测试不是全素数论证。

可最小重演的标准库代码：

    from fractions import Fraction as Q
    from math import comb

    def H(n, s=1):
        return sum((Q(1, k**s) for k in range(1,n+1)), Q(0))

    def direct(m):
        return sum((
            Q((-1)**n*comb(m,n), 2**n)*(6*n-1)
            *((H(m)-H(m-n))**2-(H(m,2)-H(m-n,2)))/8
            for n in range(m+1)), Q(0))

    def closed(m):
        p=6*m+1
        t=sum(((-1)**j*H(j-1) for j in range(2,m+1)),Q(0))
        u=sum((Q((-1)**j,j)*H(j-1) for j in range(2,m+1)),Q(0))
        return Q(1,2**m)*(3*t-Q(p,4)*u)

    for m in range(1,17):
        assert direct(m)==closed(m)
    print("exact m=1..16 PASS")

## 6. BRC/精度与接续纪律

实际复用的 carrier 是固定 \(0\le n\le m\) 的带符号二项式支路；observable 为 \(D=6z\partial_z-1\) 之后的 p-adic 第二位。保留 n、j 两种展开的来源、权重与界面，不把有符号抵消描述为非负 BRC 质量。**REUSE_APPLIED + COMPOSE_APPLIED**：将既有 LOW 二阶 jet 的纯锚点，与有限截断二项式参数 Hessian 和目标素数奇偶类配对，完成证明范围内的无损 port 投影。第二阶参数信息 \(\mathsf A_m\) 不被置零，只用 p-unit 和前置 p² 的真实目标精度削去 \(pU_m\) 项；其它混合矩保留为独立未完端口。

本材料在实际可授权的普通 GitHub research_notes 路径保存，不属于 canonical Source checkpoint，也未发 native benchmark 或 Result/freeze。原 Research conversation 的旧 recovery #6186 显示 local ACTIVE but source_authority_verified=false、无 open run/claim；精确 continuation #6187 前提拒绝；dispatch #6188 terminal FAILED/TimeoutExpired。历史中立 staging 不属于本证明，也不合并到旧 accepted Result。现有 Sites 客户端为只读且无 Researcher execution scope；没有借 maintenance 身份或通过别的身份重发被拒的 mutation。

**下一高优先级**：在本证明的 LOW-A 残余基础上，将 \(\widetilde M_n\) 的 B/C 二阶、A–B/A–C/B–C 交叉分支与 J^{(2)} 的 reflected split 精确配对，争取模 p 的真实联合消去；native benchmark 仍按原对象/验证条件执行。下轮正式续接仍先取 own Source recovery/原请求及 canonical continuation，取回合法 claim/run 后再进行原生 checkpoint/Result，绝不把本中立数学笔记冒充已准入科学成果。

**控制状态**：LIFT/JT2 OPEN；UNREVIEWED/NOT_ADMITTED；不要求更改原 scheduler、相位、启用或通知设置。
