# P025 补充 83 —— 分圆因子格 Carrier 与精确重叠修正

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-cyclotomic-stage76`  
依赖：P025 补充 79、82  
硬阻断：`NONE`

## 1. Stage 82 改变了我们需要的 state object

Stage 79 证明，对奇素数指数，单个 nonlinear cyclotomic factor 足以回答 future query：

> threshold-one projective activation 是否强迫 nonlinear support 出现重复？

Stage 82 证明这个 state 对 composite exponent 不够。指数四 difference 可以在 top `Phi_4` 完全 squarefree 时仍然激活。

因此正确的下一对象必须保留 **sign-specific cyclotomic divisor lattice**，而不是只保留一个被选中的 top factor。

## 2. P025-D26 —— sign-specific cyclotomic index sets

对整数指数

\[
n\ge2,
\]

定义

\[
\boxed{I_-(n):=\{d:d\mid n\},}
\]

以及

\[
\boxed{I_+(n):=\{d:d\mid2n,\ d\nmid n\}.}
\]

则标准 homogeneous cyclotomic factorizations 为

\[
\boxed{p^n-q^n=\prod_{d\in I_-(n)}\Phi_d(p,q),}
\]

和

\[
\boxed{p^n+q^n=\prod_{d\in I_+(n)}\Phi_d(p,q).}
\]

例如

\[
I_-(3)=\{1,3\},\quad I_+(3)=\{2,6\},
\]

\[
I_-(4)=\{1,2,4\},\quad I_+(4)=\{8\},
\]

以及

\[
I_-(9)=\{1,3,9\},\quad I_+(9)=\{2,6,18\}.
\]

这些 index sets 就是 carrier state 的 combinatorial skeleton。

## 3. 不同 layer values 不一定互素

记

\[
F_d:=\Phi_d(p,q).
\]

一个错误的简化会是

\[
m\!\left(\prod_dF_d\right)\stackrel{?}{=}\prod_dm(F_d).
\]

当某个素数同时出现在多个 cyclotomic layers 时，这个等式会失败。

这种 overlap 不应被当作噪声丢掉；它本身就是精确 carrier。

对每个至少出现在一个 selected layer 中的素数 `r`，令

\[
t_r:=\#\{d\in I_\pm(n):r\mid F_d\}.
\]

定义

\[
\boxed{\Delta_\pm(n;p,q):=\prod_r r^{t_r-1}.}
\]

等价地，

\[
\boxed{
\Delta_\pm
=
\frac{\prod_{d\in I_\pm(n)}\operatorname{rad}(F_d)}
{\operatorname{rad}(p^n\pm q^n)}.
}
\]

这就是 **cyclotomic overlap correction**。

## 4. P025-T172 —— 精确 residual carrier 分解

因为

\[
p^n\pm q^n=\prod_dF_d,
\]

所以

\[
\begin{aligned}
m(p^n\pm q^n)
&=\frac{\prod_dF_d}{\operatorname{rad}(p^n\pm q^n)}\\
&=\frac{\prod_d\operatorname{rad}(F_d)}{\operatorname{rad}(p^n\pm q^n)}
\prod_d\frac{F_d}{\operatorname{rad}(F_d)}.
\end{aligned}
\]

于是

\[
\boxed{
m(p^n\pm q^n)=\Delta_\pm(n;p,q)\prod_{d\in I_\pm(n)}m(F_d).}
\]

这是完全精确的恒等式，不需要任何 pairwise-coprimality 假设。

对应 equal-exponent projective atom 为

\[
\boxed{
\rho_{n,\pm}=
\frac{\Delta_\pm\prod_dm(F_d)}{n(p+q)}.
}
\]

因此 projective pressure 同时存在于两种资源中：

1. within-layer multiplicity `m(F_d)`；
2. cross-layer support reuse `Delta`。

## 5. 早期公式全部变成特例

### 奇素数指数

对 prime `ell`，carrier 只有两层。overlap correction 正好就是 Stage 79 已出现的 exceptional exponent-prime factor。

例如 cube sum

\[
11^3+13^3
\]

的 layers 为

\[
\Phi_2=24,
\qquad
\Phi_6=147=3\cdot7^2.
\]

素数 3 同时出现在两层，所以

\[
\Delta=3.
\]

于是

\[
m(11^3+13^3)=3m(24)m(147)=3\cdot4\cdot7=84.
\]

### 四次幂 difference

对

\[
23^4<41^4,
\]

layers 为

\[
\Phi_1=18,\quad\Phi_2=64,\quad\Phi_4=2210.
\]

素数 2 同时出现在三层，因此

\[
\boxed{\Delta=2^{3-1}=4.}
\]

top layer squarefree，但

\[
\Delta m(\Phi_1)m(\Phi_2)=4\cdot3\cdot32=384
\]

已经超过 projective denominator

\[
4(41+23)=256.
\]

这正是 top forcing 失效的精确原因。

## 6. P025-D27 —— selected carrier 与 outside carrier

设

\[
U\subseteq I_\pm(n)
\]

为希望判断“是否被强迫出现重复”的非空 layer 集合。

定义 selected residual product

\[
\boxed{R_U:=\prod_{d\in U}m(F_d),}
\]

以及 outside carrier

\[
\boxed{K_U:=\Delta_\pm\prod_{d\notin U}m(F_d).}
\]

则 P025-T172 变为

\[
\boxed{m(p^n\pm q^n)=K_UR_U.}
\]

这把完整 divisor-lattice carrier 精确压成两个 blocks。

## 7. P025-T173 —— exact forcing-margin criterion

固定 projective threshold

\[
T>0.
\]

若

\[
\rho_{n,\pm}\ge T,
\]

则

\[
K_UR_U\ge Tn(p+q).
\]

因此只要

\[
\boxed{K_U<Tn(p+q),}
\]

就必有

\[
R_U>1.
\]

也就是

\[
\boxed{
\rho_{n,\pm}\ge T
\quad\text{且}\quad
K_U<Tn(p+q)
\Longrightarrow
\exists d\in U:\ F_d\text{ nonsquarefree}.
}
\]

这就是 exact **forcing-margin criterion**。

它并不声称 `K_U` 总是小；它精确指出，要让“只保留 selected layers”的 future-safe collapse 成立，真正必须控制的是哪一块 outside resource。

## 8. Prime exponent 与 composite exponent

取 `U` 为 maximal cyclotomic index。

对奇素数 exponent `ell`，Stage 79 已普遍证明 outside carrier 不足以单独达到 threshold one，因此 top repetition 被强迫。

对 composite exponent，proper divisor layers 可能已经带着足够 pressure。

真正结构区别是

\[
\boxed{
\text{prime exponent: shallow divisor carrier}
\qquad\text{vs.}\qquad
\text{composite exponent: inheritable lower-layer carrier}.
}
\]

## 9. P025-C25 —— odd composite exponent 同样破坏 top forcing

指数九证明 Stage 82 的现象绝不是偶指数偶发。

### 九次幂 difference

取

\[
(q,p)=(23,71).
\]

则

\[
I_-(9)=\{1,3,9\}.
\]

layers 为

\[
\Phi_1=48,
\]

\[
\Phi_3=3\cdot7^4,
\]

以及

\[
\Phi_9=3\cdot811\cdot54501859.
\]

top `Phi_9` 完全 squarefree。

素数 3 同时出现在三层，所以

\[
\Delta=3^2.
\]

但仍有

\[
\boxed{\rho_{9,-}=\frac{1372}{47}>1.}
\]

top residual 完全为 1；pressure 来自 proper-divisor layers `Phi_1,Phi_3` 与 overlap correction。

### 九次幂 sum

同理，对

\[
(q,p)=(11,13),
\]

有

\[
I_+(9)=\{2,6,18\},
\]

且

\[
\Phi_{18}=3\cdot19\cdot73\cdot883
\]

squarefree，但

\[
\boxed{\rho_{9,+}=\frac76>1.}
\]

repeated pressure 已经留在 lower cube layer `Phi_6`，并且素数 3 在三层之间共享。

因此

\[
\boxed{
\text{oddness 不会恢复 top forcing；真正 shallow 的情况是 exponent 为 prime。}
}
\]

## 10. Precision 解释

现在 carrier state 至少有三层 precision：

\[
\boxed{
\text{index precision}
\to
\text{within-layer residual precision}
\to
\text{cross-layer overlap precision}.
}
\]

top-factor-only quotient 在 proper divisor layers 能继承 pressure 时，会把后两种信息一起擦掉。

forcing-margin criterion 精确回答了 future query“selected layer 是否必重复”何时可以安全 collapse：只有先证明 outside carrier 低于 threshold budget 才行。

这比原来的 top-factor heuristic 更接近 task-relative quotient safety 的底层形式。

## 11. Prior-art / novelty 边界

cyclotomic factorization 与 radical identities 都是经典数学；`Delta` 公式本身也是 elementary exact re-accounting。

P025 不单独主张这些组成部分的新颖性。

项目侧候选是：把 overlap-corrected divisor-lattice residual 作为 exact pressure carrier、selected/outside carrier split，以及它对 projective precision routing 给出的 forcing-margin semantics。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 12. 可执行资产

新增：

- `src/enterprise_math/abc_cyclotomic_divisor_carrier.py`；
- `tests/test_abc_cyclotomic_divisor_carrier.py`。

executable layer 递归计算 homogeneous cyclotomic values，验证 sign-specific factorization，从 support counts 与 radical quotient 两条路径重建 `Delta`，检查 exact residual decomposition，并复现 prime exponent、fourth-power 与 ninth-power 的 forcing / counterforcing fixtures。

## 13. 下一前沿

不存在硬阻断。继续：

1. 单独研究 overlap correction `Delta`：区分哪些部分仅由 exponent divisor lattice 强迫，哪些部分依赖 prime values；
2. 递归压缩 proper-divisor inheritance —— composite-exponent hard state 可能只是 proper exponent hard state 的 lift；
3. 定义 minimal carrier antichain，丢掉对当前 future query 已证明不可能起作用的 cyclotomic layers；
4. 测试 `rho_{n,sign}` 沿 exponent divisibility `m|n` 是否存在 exact inheritance law；
5. 只有 inheritance law 固定后，才把 forcing-margin semantics Relay 给 P023/A2。
