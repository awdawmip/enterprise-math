# P022 — `p=369581` 的目标 family half-defect valuation 反转

状态：`ACTIVE RESEARCH NOTE / EXACT COUNTEREXAMPLE / NEGATIVE BOUNDARY`  
Owner：`program/p022-geometry-v2`  
依赖：half-index Franel divisor；canonical A-elimination；midpoint transversality；companion/support routing  
跨路线相关：P018 defect sign/cancellation；P023 quotient-stable witnesses 与 minimal repair

## 1. 被检验的猜想

对素数

\[
p>5,
\qquad
p\equiv5\text{ 或 }23\pmod{24},
\]

令

\[
m=\frac{p-1}{2}.
\]

half-index theorem 给出

\[
p\mid F_m
\]

且 A-boundary

\[
2m-1=p-2
\]

为合数。

此前有限压力测试曾提示两个更强命题：

1. 这个剩余类 family 中，canonical A-elimination support 可能永远避开旧 Franel zeros；
2. 因而 pure defect 可能总满足
   \[
   v_p(D_m)=1.
   \]

**这两个命题现在都已被反例推翻。**

---

## 2. P022-LI38 — 目标 family 内的精确反例

取

\[
\boxed{p=369581.}
\]

它是素数，并且

\[
369581\equiv5\pmod{24}.
\]

因此

\[
\boxed{m=184790}
\]

确实属于我们声明的目标 family。

midpoint Franel 值按 half-index theorem 被 `p` 强制整除。独立的 mod-`p^2` recurrence 给出

\[
\boxed{
\frac{F_m}{p}
\equiv153310\pmod p,
}
\]

该值非零，所以

\[
\boxed{v_p(F_m)=1.}
\]

也就是说 midpoint transversality/simple-lift 机制在这个例子中**没有失败**。

失败发生在 support correction。

---

## 3. 更早的 Franel zero 极其显式

第八个 Franel 数为

\[
F_8
=\sum_{k=0}^8\binom8k^3
=739162.
\]

但

\[
\boxed{739162=2\cdot369581.}
\]

因此

\[
\boxed{v_p(F_8)=1.}
\]

这不是数值近似命中，而是旧 Franel 项**恰好等于目标 prime 的两倍**。

---

## 4. canonical A-elimination 以指数 2 使用这个旧 zero

在 `m=184790`，精确 canonical central-binomial relation 为

\[
\boxed{
\begin{aligned}
A_m={}&
A_1^3A_2^{-2}A_4A_5^{-1}A_6
A_8^2A_9^{-2}\\
&\cdot A_{543}A_{544}^{-1}
A_{8799}^{-1}A_{8800}A_{184789}.
\end{aligned}}
\]

所以

\[
\boxed{\alpha_{m,8}=2.}
\]

直接用 Franel recurrence 模 `p` 扫描整个 canonical support，发现 **只有 `j=8`** 在该 support 中再次被 `p` 整除。

因此 eliminated coordinates 的完整 p-adic correction 恰好为

\[
\boxed{
\sum_{j<m}\alpha_{m,j}v_p(F_j)
=2.}
\]

---

## 5. P022-LI39 — defect valuation 发生符号翻转

定义

\[
D_m
=
\frac{F_m}{\prod_{j<m}F_j^{\alpha_{m,j}}}.
\]

于是

\[
\begin{aligned}
v_p(D_m)
&=v_p(F_m)
-
\sum_{j<m}\alpha_{m,j}v_p(F_j)\\
&=1-2.
\end{aligned}
\]

因此

\[
\boxed{
v_{369581}(D_{184790})=-1.}
\]

forced midpoint prime 并没有消失，而是在 canonical quotient/elimination 后以**相反 valuation 方向**继续存在：

\[
\boxed{
\text{local numerator witness}
\longrightarrow
\text{defect denominator witness}.}
\]

所以目标 family 内的

\[
\boxed{v_p(D_{(p-1)/2})=+1}
\]

猜想已被推翻；全局 support avoidance 也已被推翻。

---

## 6. 为什么旧压力测试漏掉了它

旧的 direct prime scan 截止在

\[
p<50000.
\]

而这个反例位于

\[
p=369581.
\]

真正有效的搜索反转是：先固定较小 Franel index `j`，分解 `F_j`，再问某个大 prime factor `p` 是否让这个 `j` 进入**该 p 自己**的 canonical A-support。

这里

\[
2j+1=17
\]

为素数，而且

\[
17\mid m.
\]

所以 `j=8` 直接进入 `m` 的第一层 prime-halving ancestry。更进一步，`17` 还通过较大的祖先 `1087` 再次进入同一 ancestry tree，因此实际化简后的 `A_8` 指数累积为 `+2`。

这说明继续机械提高 prime cutoff 的效率很低：危险的 Franel index 可以非常小，而目标 prime 很大。

---

## 7. 与 universal companion 的一致性

旧 zero 相对 midpoint 的 offset 为

\[
d=m-8=184782.
\]

因此 universal integer companion 满足

\[
\boxed{369581\mid K_{184782}.}
\]

该 offset 正处在 support-localization theorem 允许发生风险的 far region。

所以这个反例完全符合此前所有精确 reduction：

\[
\text{Franel zero}
\leftrightarrow
p\mid K_d
\leftrightarrow
\text{companion hit}.
\]

并且此时 terminal prime

\[
2j+1=17
\]

确实存在于 `m` 的 prime-halving ancestry 中。

---

## 8. 反例之后仍然成立的较弱结构

### 8.1 forced midpoint divisibility 仍然成立

\[
p\mid F_m
\]

没有任何变化。

### 8.2 midpoint simple lifting 仍然可能全局成立

这个反例仍满足

\[
v_p(F_m)=1.
\]

因此它没有反驳 midpoint 自身的 transversality / non-Wieferich 猜想。

### 8.3 prime 仍是非零 defect witness

虽然符号翻转，

\[
v_p(D_m)=-1\ne0.
\]

所以比 `+1` 更弱的潜在目标可能是

\[
\boxed{v_p(D_m)\ne0}.
\]

但本笔记**不直接把它升级成新猜想**：更宽 forced family 已经有 `p=157` 的精确 `v_p(D_m)=0` 例子。目标 `5,23 mod24` family 内是否也存在 valuation=0，才是现在正确的下一反例问题。

---

## 9. 精度 / quotient 含义

这个负结果比普通“信息丢失”更强。

canonical coordinate change 不仅可能改变一个局部 witness 是否存在，还可能改变它的**有符号 valuation 方向**：

\[
\boxed{
\text{visible numerator information}
\not\Rightarrow
\text{same-sign quotient information}.}
\]

因此 future computation 要精确得到 defect，不能只保留“这个 prime 在原状态中出现过”的 bit；必须保留足以计算完整 valuation correction 的状态。

这是 P022 对 A2/P023 “future-safe precision 必须相对于 operation algebra 定义”的尖锐压力测试。

---

## 10. 当前状态修正

任何旧 P022 文档中“target `5,23 mod24` family 尚未观察到 support hit”的表述，现在都只能作为已被新反例超过的历史有限证据。

当前准确状态是：

- target support avoidance：**REJECTED**；
- universal `v_p(D_m)=+1`：**REJECTED**；
- midpoint `v_p(F_m)=1`：全局仍开放，本例支持；
- target-family `v_p(D_m) != 0`：开放；
- pure-defect 全局乘法独立性：开放。

---

## 11. 可执行资产

新增：

- `src/enterprise_math/p022_barlow_target_half_defect_counterexample.py`；
- `tests/test_p022_barlow_target_half_defect_counterexample.py`。

证书重建 canonical A-relation、`F_8=2p`、唯一 support zero、midpoint mod-`p^2` 非零 lift，以及最终 defect valuation `-1`，无需构造极其巨大的整数 `F_184790`。
