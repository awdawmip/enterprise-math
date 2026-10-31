# R423｜带符号 BRC 辅助 Turán：二次余阶阈值的统一解析定理

日期：2026-10-31。状态：AUTHOR_SIDE_ANALYTIC / EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED。对象为 R416–R422 的十二支路带符号 BRC **辅助组合读出**；保留支路符号，不将加权期望解释为正质量。原生 X6 对应仍须单独证明。

## 1. 对象与结论

令整数 m≥1、s≥3、r=s+m，并定义

\[
\delta_{r,q}=[t^r](1-t)(1+t)^{2q}(1+t^2)^{r-q},\quad
H_{r,q}=\binom{r+q}{2q}\delta_{r,q},\quad
D_{r,s}=H_{r,s}^2-H_{r,s-1}H_{r,s+1},
\]
\[
W_s=\binom{2s+m}{2s}\binom{2s}{s}>0.
\]

**R423 定理。** 对所有整数 m≥1，s≥96(m+2)^2，有

\[
\boxed{D_{s+m,s}/W_s^2 \ge 4^m/[2(m+1)s^2]>0.}
\]

它将 R422 的同一下界的充分条件 s≥72(m+2)^4 降到二次阶；常数96仅为显式充分常数。

## 2. 精确偶核与新误差引理

对整数 q≥n≥0，q≥1，令

\[
\rho_q(d)=\binom{2q}{q+d}/\binom{2q}{q}
=\prod_{j=0}^{|d|-1}(q-j)/(q+j+1),\quad |d|\le n.
\]

令随机变量 d=n−2k，Pr(k)=2^{-n}\binom nk，并记 a(q,n)=δ_{q+n,q}/\binom{2q}{q}。从原始带符号卷积的正负两项直接展开，

\[
a(q,n)/2^n=\mathbb E[\rho_q(d)-\rho_q(d-1)].
\]

利用 d 与 −d 同分布及 ρ 的偶性，并使用精确相邻比率

\[
\rho_q(d-1)=\rho_q(d)(q+d)/(q-d+1),\quad
\rho_q(d+1)=\rho_q(d)(q-d)/(q+d+1),
\]

得 **新的精确偶核恒等式**（端点由扩展二项式系数为0解释）：

\[
\boxed{a(q,n)/2^n=
\mathbb E\!\left[\rho_q(d)
\frac{q+1-2d^2}{(q+1)^2-d^2}\right].}\tag{1}
\]

若 q≥max(1,2n²)，则对所有 |d|≤n 有 u=d²≤q/2。由有限乘积不等式

\[
0\le1-\rho_q(d)
\le\sum_{j=0}^{|d|-1}\frac{2j+1}{q+j+1}\le u/q.
\]

置 B=q(q+1−2u)/[(q+1)²−u]。有 0≤B≤1，且

\[
0\le1-B=\frac{q+1+(2q-1)u}{(q+1)^2-u}
\le\frac{q+1+2qu}{q^2}\le\frac{2+2u}{q}.
\]

故 0≤1−ρ_q(d)B≤(3d²+2)/q。由于 d 是 n 个独立等概率 ±1 的和，\(\mathbb E[d^2]=n\)。将(1)乘以 q 并取期望，得到完全精确的**一阶矩误差引理**

\[
\boxed{0\le 1-\frac{q\,a(q,n)}{2^n}\le \frac{3n+2}{q},
\qquad q\ge\max(1,2n^2).}\tag{2}
\]

这是在保留原始有符号差后进行对称化所得；逐点粗绝对值估计会丢失此处的二阶差分结构。

## 3. 统一 Turán 下界

对 h∈{−1,0,1}，令 q=s+h，n=m−h，b_h=s a(q,n)/2^n。s≥96(m+2)² 保证 q≥s−1≥2(m+1)²≥2n²。应用(2)并利用 s−1≥s/2：

\[
|b_h-1|\le\left|\frac{s}{q}-1\right|
+\frac{s}{q}\left|\frac{q a(q,n)}{2^n}-1\right|
\le\frac1{s-1}+\frac{s(3m+5)}{(s-1)^2}
\le\frac{12(m+2)}s
\le\varepsilon:=\frac1{8(m+2)}<1. \tag{3}
\]

另一方面令 W_q=\binom{r+q}{2q}\binom{2q}{q}。阶乘消去给出

\[
\lambda=\frac{W_{s-1}W_{s+1}}{W_s^2}
=\frac{m s^2(2s+m+1)}{(m+1)(s+1)^2(2s+m)}
<\frac m{m+1},
\]

最后一步由 (2s+m+1)s²<(2s+m)(s+1)² 保证。因此

\[
\frac{s^2D_{s+m,s}}{4^m W_s^2}
=b_0^2-\lambda b_{-1}b_{+1}
\ge(1-\varepsilon)^2-\frac m{m+1}(1+\varepsilon)^2
=\frac{1-(4m+2)\varepsilon+\varepsilon^2}{m+1}
>\frac1{2(m+1)},
\]

因为 1−(4m+2)/[8(m+2)]=(4m+14)/[8(m+2)]>1/2。证毕。

## 4. 验证、范围、来源与接续

附带 R423_VERIFY.py 只使用 Python 标准库整数与 Fraction，从最初的 (1−t)(1+t)^{2q}(1+t²)^n 有符号系数展开交叉核验偶核恒等式，并以精确有理数核验(2)、三邻项二次阈值和原始 Turán 差。实际执行：195项原始δ与偶核对照；87项矩引理；63项阈值对照（m=1…16、20、24、32、48、64，各三个s）；100项原始Turán交叉验证，全部 PASS。有限算例只用于代码公式复核；无限域来自第2–3节解析证明。

来源：R422 作者侧研究提交 a5b298be7f3d43fd5daf849b4b45c930e1e82a33；本轮规范读取 GLOBAL_KNOWLEDGE_V1 main@d8a7f5790a674c170799731e728aa401bfe66d11 与 Enterprise Math main@1cad8a9d12ac18449b710c4fc682bd16659ef4b1。GitHub 研究作者连接 awdawmip；原生 DIRECTED_RESEARCH authority_granted=false，活跃 Source owner 查询 CONTROL_QUOTA。本证明属于作者侧研究，未经独立 Driver 审阅或正式数学接纳；P000 和 ACTIVE 世界观未修改。

下一精确问题：能否借二项分布的尾部衰减，去掉 q≥2n² 的逐点偶核正性条件，从而进一步取得 s=O(m) 或全参数正性？需验证当 q+1−2d²<0 时远尾有符号贡献的补偿机制，不能从有限采样推断全域。
