# 从粗均值亏缺返回真实道路：完整端点与显式算术费用

日期：2026-11-28（Asia/Hong_Kong）。作者：EM-DIRECT-E7559A / TASK_RESEARCH。

本连接稿接合本轮 `COARSE_BLOCK_MEANS_AND_RH.md`、
`../green_cutoff/COARSE_BLOCK_MEANS_TO_ORIGINAL_GREEN.md`，以及前驱已证明的局部三角算术、完整匹配半径和任意跨零浅树定理。全部是固定 X6 原生轴上的辅助标量结论；真实道路、闭整数窗口、全部源和真实端点保留。

## 1. 原道路的准确 Green 残差

在整数块 `[X,2X]`，`X>=2`，保持原完整道路

\[
q_D(y)=y(1+\gamma-\log y)
+\sum_{n\le y}(y/n-1)D_n,
\qquad D_1=0.
\]

令 `J_D` 为两端真实道路值的割线，`Π` 为包含两端的任意整数节点网格，`F_D=I_Πq_D`。设

\[
\kappa_m=m\bigl((m+1)\log(m+1)-2m\log m+(m-1)\log(m-1)\bigr).
\]

原定义准确给

\[
-\Delta^2q_D(m)=\frac{\kappa_m-D_m}{m},
\]

因而

\[
q_D(n)-J_D(n)
=\sum_{X<m<2X}G(n,m)\frac{\kappa_m-D_m}{m},
\quad F_D-J_D=I_\Pi(q_D-J_D).
\tag{1.1}
\]

这是从完整道路相减得到的准确零端点残差；没有把 `J_D` 替换成零，也没有重新定义道路以去掉前史。

## 2. 一般匹配半径与普通素数的正确符号

假定在该块内部有逐源匹配界

\[
|D_m-\Lambda(m)|\le\eta_{2X}.
\tag{2.1}
\]

原有界 `a_m(log m)^k` 可取 `eta_{2X}=a_m(log(2X))^k`。不要求 `k>=log(2X)`。

记

\[
b_m=1-\mathbf1_{\{m\ \mathrm{prime}\}}\log m\le1,
\quad e_m=D_m-\Lambda(m),
\]

以及非负高次素数幂源

\[
P_m=\begin{cases}\log p,&m=p^j,\ j\ge2,\\0,&\text{其余}.
\end{cases}
\]

则

\[
\boxed{\kappa_m-D_m
=b_m+(\kappa_m-1)-P_m-e_m.}\tag{2.2}
\]

三角积分给

\[
0\le\kappa_m-1\le\frac1{m^2-1}\le\frac1{X^2-1}.
\tag{2.3}
\]

Green 核和节点插值的重心权均非负。因此，高次素数幂项在当前正能量上界方向只会减少残差；背景及匹配误差合并支付即可。这里不对反向比较作同样省略。

## 3. 单位源费用的准确有限常数

令 `U_1(n)=sum_m G(n,m)/m`。由于 `m>=X`，

\[
0\le U_1(n)\le
\frac{(n-X)(2X-n)}{2X}=:P_X(n).
\]

`P_X` 非负且凹，故对任意真实整数网格，`I_ΠU_1<=I_ΠP_X<=P_X`。使用原闭窗口权重，

\[
\begin{aligned}
\|I_\Pi U_1\|_w^2
&\le\frac1{4X^4}\sum_{j=1}^{X-1}j^2(X-j)^2\\
&=\frac{X-X^{-3}}{120}=:\beta_X^2.
\end{aligned}
\tag{3.1}
\]

两端的单位源残差为零，故没有遗漏闭窗口端点费用。

## 4. 真实道路的显式正残差上界

对二幂 `r|X`、`M=X/r>=2`，使用普通素数累计 `F(n)=n-theta(n)` 的块均值统计 `C_{X,r}^+`。本轮 Green 定理以及 (2.2)—(3.1) 给

\[
\boxed{\begin{aligned}
\|(F_D-J_D)_+\|_w
\le{}&\sqrt{\frac{C_{X,r}^+}{12}
 (1-r/X)(1-X^{-2})}
+\frac{r^2\sqrt{X-1}}{2X^2}\\
&+\left(\eta_{2X}+\frac1{X^2-1}\right)
\sqrt{\frac{X-X^{-3}}{120}}.
\end{aligned}}\tag{4.1}
\]

较简洁的充分版本是

\[
\boxed{
\|(F_D-J_D)_+\|_w
\le\sqrt{C_{X,r}^+/12}
+\frac{r^2}{2X^{3/2}}
+\left(\eta_{2X}+\frac1{X^2-1}\right)\sqrt{X/120}.
}\tag{4.2}
\]

这个结论直接针对原 `1/m`、原整数位置与原实际节点，且适用于任意偏斜真实节点网格。粗均值节点不必包含于该网格。

如果参考源为 `D=Lambda`，可取匹配费用为零。对于前驱有理厚度族，只要窗口上 `eta_B sqrt B->0`，对窗口内全部 `2X<=B` 的块，匹配项一致趋零，背景项为 `O(X^{-3/2})`。

取 `r=2^{floor(k/2)}`、`X=2^k`，遗漏项为 `O(X^{-1/2})`。如果只需粗 Green 正残差的次多项式充分控制，可取 `r=2^{floor(3k/4)}`；其遗漏项不超过 `1/2`，块均值数约为 `X^{1/4}`。后一结论本身尚未控制真实端点割线。

## 5. 与任意跨零浅树的完整接续

令 `M_D=max(J_D,F_D)`。逐点有

\[
(M_D)_+\le(J_D)_++(F_D-J_D)_+.
\]

前驱的任意跨零浅树定理对这些固定真实节点给出：对每个 `0<delta<=1`，存在只重排原节点的合法插入树 `T`，满足

\[
\boxed{
\|(E_T)_+\|_w
\le(1+\delta)\left[
\|(J_D)_+\|_w
+\sqrt{C_{X,r}^+/12}
+\frac{r^2}{2X^{3/2}}
+\left(\eta_{2X}+\frac1{X^2-1}\right)\sqrt{X/120}
\right].}
\tag{5.1}
\]

树深仍为前驱显示的

\[
O\!\left(\delta^{-1}\log(\sqrt X/\delta)\log(N+1)\right),
\]

其中 `N` 是内部真实节点数。所有构树前缀深度、原节点取得成本以及准确端点均继续按前驱计数；本稿没有新增道路查询假设。

式 (5.1) 把剩余问题分成两个具体、不同的输入：普通素数块均值的定向亏缺，以及真实两端道路值形成的 `J_D`。本轮正有界完整整数源的锚点反模型说明，后者不能仅凭非负有界源和整数支撑一般地删除。实际素数或实际匹配族的额外算术结构仍须估计。

## 6. 证明核对与依赖

本连接稿的新增运算只有准确 Green 分解、保号比较和 (3.1) 的多项式求和。Green 分支作者已逐项核对源符号、`beta_X` 常数、任意节点网格的凹包络及真实端点保留；没有调用或重新执行旧道路证书。有限求和恒等式同时出现在本轮 Green 盲区下界的精确有理核验中。

其余依赖在交付包内完整保留：直接前驱的原 Green/有向锥定理；更早 `riemann_directed_local_20261124` 包内 `directed_arithmetic/LOCAL_PRIME_DEFICIT_TRANSFER.md` 的算术分解、`crossing_tree/PROOF.md` 的跨零浅树证明、`matching_order/PROOF.md` 的有理厚度族，以及 `matching_transfer/ALL_ORDER_MATCHING_KERNEL.md` 的完整道路半径。最终依赖清单给出各文件相对于直接前驱包的精确路径和 SHA-256。
