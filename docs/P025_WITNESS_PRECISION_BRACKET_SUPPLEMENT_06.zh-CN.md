# P025 补充 06 —— Arithmetic Demand Floor 与 Sparse Witness Ceiling

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner：`program/p025-witness-precision-bracket`  
父依赖：`program/p025-arithmetic-witness-budget@e160fda3`（本 generation 开始时为 `PROVED WIP`、验证仍在运行）  
前人工作状态：初等整数 kernel / Pluecker 构造；有限精度整合 `NOVELTY_UNVERIFIED`

## 1. 目标

此前 P025 已经从两个方向逼近同一个 relation-conditioned witness precision `mu`：

1. 补充 05 把 multiplicity demand 转成必要的 norm budget；
2. 补充 01--02 用紧凑 generator signature `(alpha,beta)` 重建 witness lattice 及其 degeneracy hyperplane。

本补充把两者直接合起来，而不要求先完整求解 shortest-vector problem。

得到精确有限夹逼

\[
\boxed{\lambda_{abc}\le \mu\le U_2}
\]

其中下端由 arithmetic demand 强制给出，上端则由一个非零 generator minor 直接构造只占两个 prime coordinate 的非退化 witness。

若上下端相等，就无需枚举 witness lattice，直接精确确定 `mu`。

## 2. Residual-normalized derivative weight

对正整数 `n` 定义

\[
A(n)
=
\sum_{p\mid n}\frac{n}{p}v_p(n)
\]

并回忆

\[
m(n)=\frac{n}{\operatorname{rad}(n)}.
\]

`A(n)` 每一项都被 `m(n)` 整除，精确约掉以后得到

\[
\boxed{
\widehat A(n)
:=\frac{A(n)}{m(n)}
=
\sum_{p\mid n}
\frac{\operatorname{rad}(n)}{p}v_p(n)
\in\mathbb N_0.
}
\]

这个 coordinate 去掉已经由 `m(n)` 承担的 repeated-power bulk，但仍保留 arithmetic derivative coefficient 所需要的 exponent label。

## 3. P025-T19 —— normalized complementary capacity

对正整数 `x,y` 定义

\[
\boxed{
K_{x,y}
=
\operatorname{rad}(x)\widehat A(y)
+
\operatorname{rad}(y)\widehat A(x).
}
\]

等价地，

\[
K_{x,y}
=
\operatorname{rad}(x)\operatorname{rad}(y)
\left(
\sum_{p\mid x}\frac{v_p(x)}p
+
\sum_{p\mid y}\frac{v_p(y)}p
\right),
\]

但第一种写法直接显示它是整数。

补充 05 的 norm-budget coefficient mass 为

\[
H_{x,y}=xA(y)+yA(x).
\]

因为 `x=m(x)rad(x)` 且 `A(x)=m(x)\widehat A(x)`，所以精确分解为

\[
\boxed{
H_{x,y}=m(x)m(y)K_{x,y}.
}
\]

现在令 `(x,y,z)` 是 primitive abc triple 的一个 orientation。补充 05 已有

\[
m(x)m(y)m(z)\le H_{x,y}\mu.
\]

约掉正因子 `m(x)m(y)`：

\[
\boxed{m(z)\le K_{x,y}\mu.}
\]

这一步很重要：target 自己的 repeated-prime demand 被“补 pair 的 normalized coefficient capacity × 全局 minimum witness precision”控制。

## 4. P025-T20 —— triple-only arithmetic demand floor

对 target `z` 及其补 pair `(x,y)` 定义

\[
\lambda_z
=
\left\lceil\frac{m(z)}{K_{x,y}}\right\rceil.
\]

只要非退化 witness family 存在，就有 `K_(x,y)>0`，由 P025-T19：

\[
\boxed{\lambda_z\le\mu.}
\]

把三个 target orientation 合起来：

\[
\boxed{
\lambda_{abc}
=
\max\{\lambda_a,\lambda_b,\lambda_c\}
\le\mu.
}
\]

`lambda_abc` 的价值在于，它完全从 arithmetic triple 本身计算，不需要枚举或优化任何 witness vector。

### 解释

`lambda_abc` 是 **arithmetic-demand precision floor**：低于这个 norm radius 时，无论 witness lattice 的几何结构多好，都不可能有 relation-adapted non-degenerate certificate 承载全部 target multiplicity demand。

但它只是下界，不是 `mu` 的完整替代。

## 5. 负边界 —— arithmetic demand 不决定 witness precision

对

\[
1+7=8,
\]

有

\[
\lambda_{abc}=4,
\]

但精确 relation-conditioned witness lattice 给出

\[
\mu=12.
\]

在 prime coordinates `(2,7)` 上 primitive additive normal 是

\[
\alpha=(12,-1),
\]

所以 additive kernel 由 `(1,12)`（差一个整体符号）生成。arithmetic demand floor 只看到了这个 relation slope 的一部分。

因此

\[
\boxed{
\text{multiplicity demand}
\not\Rightarrow
\text{complete witness precision}.
}
\]

缺掉的成本是真正的 relation/lattice information，不是继续增加 radical support bookkeeping 就能补回的。

## 6. P025-T21 —— 显式 two-coordinate non-degenerate witness

令

\[
\alpha=(\alpha_1,\ldots,\alpha_s)
\]

为 primitive additive normal，

\[
\beta=(\beta_1,\ldots,\beta_s)
\]

为同一 prime-labelled coordinate set 上的 Wronskian degeneracy normal。

对 `i<j` 定义 two-row minor

\[
\omega_{ij}
=
\alpha_i\beta_j-\alpha_j\beta_i.
\]

假设

\[
\omega_{ij}\ne0.
\]

令

\[
g_{ij}=\gcd(|\alpha_i|,|\alpha_j|)
\]

并构造 sparse vector `x^(ij)`：

\[
x_i=\frac{\alpha_j}{g_{ij}},
\qquad
x_j=-\frac{\alpha_i}{g_{ij}},
\]

其它 coordinate 全部为零。

于是

\[
\alpha\cdot x^{(ij)}=0.
\]

同时

\[
\beta\cdot x^{(ij)}
=
\frac{\beta_i\alpha_j-\beta_j\alpha_i}{g_{ij}}
=-\frac{\omega_{ij}}{g_{ij}}
e0.
\]

因此 `x^(ij)` 是显式 non-degenerate relation-adapted witness。

其 `L_infinity` cost 为

\[
\boxed{
U_{ij}
=
\frac{\max(|\alpha_i|,|\alpha_j|)}
{\gcd(|\alpha_i|,|\alpha_j|)}.
}
\]

完整 witness flag 非退化意味着 `alpha,beta` 不成比例，所以至少有一个 `omega_ij` 非零。定义

\[
\boxed{
U_2
=
\min_{\omega_{ij}\ne0}U_{ij}.
}
\]

得到

\[
\boxed{\mu\le U_2.}
\]

这是初等 sparse kernel 构造。P025 不把二行列式/Pluecker 代数作为新发明。

## 7. P025-T22 —— 精确有限 witness-precision bracket

合并 P025-T20 与 P025-T21：

\[
\boxed{
\lambda_{abc}\le\mu\le U_2.
}
\]

区间宽度

\[
\Delta_\mu=U_2-\lambda_{abc}
\]

是在执行完整 lattice optimization 之前的一个精确有限 uncertainty budget。

尤其：

\[
\boxed{
\lambda_{abc}=U_2
\Longrightarrow
\mu=\lambda_{abc}=U_2.
}
\]

也就是说，有些 witness-precision 问题只需要一张 arithmetic lower certificate 加一张 generator-based sparse upper certificate，就可以完全关闭，无需 witness-ball enumeration。

### 例子

- `1+2=3`：`lambda_abc=1=U_2`，所以精确 `mu=1`。
- `1+8=9`：`lambda_abc=2=U_2`，所以精确 `mu=2`。
- `1+7=8`：`lambda_abc=4`，`mu=12`，`U_2=12`。
- `1+36=37`：`lambda_abc=6`，`mu=12`，`U_2=24`；上下两侧都还有真实余量。

## 8. P025-T23 —— 高 abc quality 强迫 witness-precision horizon

回忆 P025 前面的结果。固定正整数 `u>v`。若

\[
c^v>\operatorname{rad}(abc)^u,
\]

则

\[
m_{\max}^{3u}
>
c^{u-v}(c-1)^u.
\]

定义

\[
H_{u,v}(c)
=
R_{3u}\!\left(c^{u-v}(c-1)^u\right).
\]

于是

\[
m_{\max}>H_{u,v}(c).
\]

再令

\[
K_{\max}=\max\{K_{b,c},K_{c,a},K_{a,b}\}.
\]

对实现 `m_max` 的那个 target，P025-T19 给出

\[
m_{\max}\le K_i\mu\le K_{\max}\mu.
\]

所以

\[
K_{\max}\mu>H_{u,v}(c),
\]

所有量均为整数，因此

\[
\boxed{
\mu
\ge
\left\lfloor\frac{H_{u,v}(c)}{K_{\max}}\right\rfloor+1.
}
\]

这是第一次把 abc-type high-quality event 直接运输成显式 witness-precision floor。

但它并没有证明该 floor 必须趋于无穷，因为 triple-dependent complementary capacity 本身也可能增长。这个限制必须保留：这是精确 routing theorem，不是新的渐近 abc 突破。

## 9. 有界压力测试

独立精确 prototype 枚举了满足以下条件的有序 primitive triples：

- `c<80`；
- prime-support dimension 至多四；
- 能在 `mu<=12` 范围精确找到 witness precision。

共保留 1,154 个状态。

在该有限范围内：

- 全部满足 `lambda_abc<=mu<=U_2`；
- `mu-lambda_abc` 最大达到 `8`，确认 arithmetic lower bound 本身并不完整；
- 592 个状态满足 `lambda_abc=U_2`，即在这个刻意很小的样本里，略超过一半的 `mu` 不需要 shortest-vector search 就被 bracket 直接精确锁定；
- 724 个状态满足 `U_2=mu`。

这些计数只属于 executable exploration，不是分布或渐近主张。

## 10. 架构后果

P025 现在出现了三种不能混在一起的 precision：

1. **arithmetic-demand precision** `lambda_abc` —— multiplicity load 强迫到哪里；
2. **exact relation-conditioned witness precision** `mu` —— 第一个 non-degenerate certificate 出现在哪里；
3. **sparse generator ceiling** `U_2` —— compact row/Pluecker generator 不做全局 lattice search 就能明确构造到哪里。

因此 proof architecture 出现一个 certificate sandwich：

\[
\boxed{
\text{demand certificate}
\le
\text{true witness precision}
\le
\text{sparse construction certificate}.
}
\]

它比把 witness search 简单标记成 `safe/unsafe` 或 `found/not found` 保留了更多可计算结构。

但三者仍然都是 task-relative 的，只属于声明的 relation/certificate language，不应自动提升成本体或物理 state。

## 11. 前人工作与 ownership 边界

以下部件均属于既有或初等数学：

- integer linear kernels；
- two-coordinate kernel vector 的 gcd normalization；
- two-by-two minors / exterior coordinates；
- shortest-vector / Geometry-of-Numbers 视角；
- Pasten 的 arithmetic derivative witness lattice。

所以 P025 不对 sparse vector construction 或“用显式上下界夹逼 shortest certificate”作历史优先性主张。

项目侧研究候选只是把此前三个 P025 层真正接起来：

\[
\text{abc residual demand}
\to
\text{relation witness precision}
\to
\text{compact generator certificate}.
\]

历史创新性继续是 `NOVELTY_UNVERIFIED`。

本结果仍属于 P025 specialization。除非以后抽出更强的一般 theorem 并完成专门 prior-art audit，否则 generic lower/upper certificate bracketing 与 task-relative repair 不应复制 P023/A2 的母理论。

## 12. 可执行资产

本 generation 新增：

- `src/enterprise_math/witness_precision_bracket.py`；
- `tests/test_witness_precision_bracket.py`。

实现包括：

- residual-normalized derivative weights；
- normalized pair capacities `K_(x,y)`；
- orientation-specific 与 combined arithmetic demand floor；
- 从 nonzero row minor 构造显式 sparse witness；
- `U_2` 与精确 bracket；
- 可选调用有界 exact `mu` oracle 进行核验；
- high-quality witness-floor transport。

## 13. 下一前沿

这个 bracket 把剩余未知进一步拆开了。

1. 研究 `mu-lambda_abc`：其中多少来自 additive lattice 本身，多少专门来自 degeneracy sublattice `T^circ`？
2. 引入 additive lattice 的 shortest nonzero radius `rho`，测试更强下界 `max(lambda_abc,rho)<=mu`。
3. 主动寻找在 arithmetic demand 与 additive-lattice shortest radius 都计入以后，non-degeneracy 仍然额外增加成本的精确反例。
4. 检查 minimum witness 的 proof-loss vector `(g1,g2,g3)` 与 bracket gaps 是否存在关系，还是基本独立。
5. 只有这些正负边界都弄清以后，再继续对 high-quality abc triples 提出更强主张。
