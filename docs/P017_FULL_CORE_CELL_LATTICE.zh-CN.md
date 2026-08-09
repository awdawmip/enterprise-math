# P017 全核 Cell 格

状态：`ACTIVE DISCOVERY NOTE`  
范围：partial/full smooth-core 镜像 cell、lcm 交闭包、整除偏序反演，以及 overlap-only 攻击的负边界  
依赖：规范 P017 L020 全 smooth-core 分解、L053 full-core CRT 容量、L054 精确 quotient-window 分离，以及当前 residual hard-core 路线  
新颖性：`NOVELTY_UNVERIFIED`  
纪律：整除格、中国剩余定理、zeta 变换与 Möbius 反演均为经典数学。本文**不证明 Legendre 猜想**。

## 1. 为什么研究 cell 交叠？

当前 residual P017 hard core 为每个通过 anchor 的镜像半径

\[
1\le r<k,
\qquad M=k(k+1)
\]

附上两个精确 full `k`-smooth core：

\[
S_-(r),\qquad S_+(r).
\]

规范 L053 把精确乘积 `S_-(r)S_+(r)` 作为 full-core CRT 模数。当前 hard-core discovery 路线又表明：乘积小于 `k` 的 residual exact cell，局部上会退化成一个 locally admissible 的双线性仿射素数问题。

一个自然的下一想法，是从许多**部分 core cell** 的全局交叠中寻找额外容量亏损。

本文先把这条路压力测试到底。结论非常明确：

> **partial-cell 的交叠严格就是 lcm refinement；完整的 inclusion–exclusion 则严格就是把 partial 计数反演回已经存在的 exact full-core strata。**

因此，单纯 overlap bookkeeping 不是新的全局耦合机制。

---

## 2. 有向 partial-core cell

称正奇整数 `a` 为可容许 partial core，如果 `a` 的每个素因子都不超过 `k`，并且

\[
\gcd(a,M)=1.
\]

对两个满足

\[
\gcd(a,b)=1
\]

的可容许 partial core `a,b`，定义有向 anchor-surviving cell：

\[
\boxed{
C_k(a,b)
=
\{1\le r<k:
\gcd(r,M)=1,
\ a\mid M-r,
\ b\mid M+r\}.
}
\]

由于 `M` 为偶数，而通过 anchor 的 `r` 必为奇数，所以在施加公共 anchor 筛选前，整除条件加奇偶条件恰好给出模

\[
\boxed{2ab}
\]

的唯一 CRT 余数类。anchor 条件只会从这条等差数列中删除成员。

对 full-core pair `(A,B)`，定义 exact cell：

\[
E_k(A,B)
=
\{r:S_-(r)=A,\ S_+(r)=B\}.
\]

所有 `E_k(A,B)` 精确分割全部 anchor-surviving radii。

---

## 3. CC01 —— Cell 交叠等于逐侧 lcm 提升

状态：`PROVED`。

取两个可容许 partial cell

\[
C_k(a,b),\qquad C_k(c,d),
\]

并定义

\[
A=\operatorname{lcm}(a,c),
\qquad
B=\operatorname{lcm}(b,d).
\]

则

\[
\boxed{
C_k(a,b)\cap C_k(c,d)
=
\begin{cases}
\varnothing,&\gcd(A,B)>1,\\
C_k(A,B),&\gcd(A,B)=1.
\end{cases}
}
\]

### 证明

一个半径同时属于两 cell，当且仅当

\[
a,c\mid M-r,
\qquad
b,d\mid M+r,
\]

等价于

\[
A\mid M-r,
\qquad
B\mid M+r.
\]

若某个奇素数 `p` 同时整除 `A` 和 `B`，则它同时整除两侧镜像状态，因而整除它们之和 `2M`。但所有 core 素因子都横向于 `M`，矛盾。所以这种跨侧冲突必使交集为空。

当 `gcd(A,B)=1` 时，合并后的整除条件恰好就是 `C_k(A,B)` 的定义，并且使用同一个 anchor 筛选。∎

### 严格 refinement 至少把模数放大 3 倍

按逐坐标整除定义偏序：

\[
(a,b)\preceq(A,B)
\iff a\mid A\text{ 且 }b\mid B.
\]

若 refinement 严格，则

\[
\frac{AB}{ab}
\]

是大于 1 的奇整数，因此至少为 3。于是每一次严格 refinement，原始半径模数 `2ab` 至少放大三倍。

---

## 4. CC02 —— Exact full-core pair 是唯一最大已表示标签

状态：`PROVED`。

对每个 anchor-surviving 半径 `r`，

\[
\boxed{
r\in C_k(a,b)
\iff
a\mid S_-(r)\text{ 且 }b\mid S_+(r).
}
\]

### 证明

`a,b` 的每个素因子都不超过 `k`。因此，下侧被 `a` 整除恰好等价于 `a` 整除规范 full `k`-smooth core `S_-(r)`；上侧同理。∎

所以

\[
\boxed{(S_-(r),S_+(r))}
\]

正是半径 `r` 所表示的唯一最大 partial-core 标签。

从有限精度角度看：partial cell 只记住部分整除事实；lcm refinement 累积这些事实；exact full-core pair 是终端标签。

---

## 5. CC03 —— Partial 计数是 exact strata 的二维 zeta 变换

状态：`PROVED`。

令

\[
c_k(a,b)=|C_k(a,b)|,
\qquad
e_k(A,B)=|E_k(A,B)|.
\]

由 CC02 立即得到精确有限恒等式

\[
\boxed{
c_k(a,b)
=
\sum_{\substack{A:a\mid A\\B:b\mid B}}
e_k(A,B).
}
\]

由于候选半径只有 `k-1` 个，实际出现的 exact 标签当然有限。

这就是两个整除偏序直积上的普通 zeta 变换。

分别在两个坐标上作普通 Möbius 反演，得到

\[
\boxed{
e_k(a,b)
=
\sum_{u\ge1}\sum_{v\ge1}
\mu(u)\mu(v)\,c_k(au,bv),
}
\]

其中只有有限项非零。

因此，整族 exact full-core cell 计数与整族 partial-cell 计数在信息上等价。

这里不对 zeta/Möbius 反演本身主张任何新颖性。

---

## 6. CC04 —— Residual refinement 具有对数高度

状态：`PROVED`。

在 residual hard-core 区域中只保留

\[
ab<k.
\]

对任何始终留在 residual 区域的严格 refinement 链

\[
(a_0,b_0)
\prec(a_1,b_1)
\prec\cdots\prec(a_h,b_h),
\]

CC01 给出

\[
\boxed{3^h a_0b_0<k.}
\]

所以严格 refinement 步数有限，其上界就是满足该不等式的最大整数 `h`。

这是一个有用的 precision-depth 结论，但它本身不是 Legendre 容量亏损：不可比较 partial 标签之间的分支数仍可能很大。

---

## 7. 对 proposed cross-cell-overlap 路线的负边界

以上结果封闭了一条很诱人的路线。

假设我们试图只通过以下操作获得新的全局优势：

1. 计数许多 partial candidate cells；
2. 通过两两/高阶 inclusion–exclusion 修正交叠；
3. 把“交叠损失”解释成新的 cross-cell 资源亏损。

CC01–CC03 证明，这个过程并不会产生新不变量。每一个交叠仍是一个 lcm-refined cell，而完整 inclusion–exclusion 恰好就是把 partial 计数 Möbius 反演回 L020/L053 已经存在的 exact full-core strata。

因此

\[
\boxed{
\text{candidate-cell overlap algebra}
=
\text{full-core divisibility refinement 的另一套坐标。}
}
\]

随后，当前 affine hard-core 结果会分别作用在每个 exact residual stratum 上；其局部奇素数 wheel 又是 admissible 的。因此继续在同一整除/CRT refinement 上堆层，不能消灭这个 exact cell。

这是一个**路线淘汰定理**，不是 broader hard-core program 的失败。

真正有价值的下一耦合必须发生在**最大 refinement 之后的不同 exact full-core strata 之间**，并使用二维整除 zeta transform 中没有的信息，例如：

- 不同 cell 大素数尾之间由共同中心产生的关系；
- P017/P018 hard-core bridge 暴露出的互不重叠 root-channel 几何；
- 同一个原始平方盆地中多个 exact cells 的全局不变量；
- 或一个明确的非局部解析输入。

---

## 8. 对进取数论底层的反哺

这个 P017 特化给出了一条很干净的底层模式：

\[
\text{partial observable}
\to
\text{lcm/join refinement}
\to
\text{exact terminal label}
\to
\text{coarse/exact 计数之间的 Möbius 反演}.
\]

它也再次验证一条研究纪律：更精细的坐标只有在改变“能证明什么”时才值得保留。这里看似新的 cross-cell overlap 结构，严格坍缩为已有 terminal state，因此不应再把它提升为独立解释层。

这点可以反哺 P018/P023：以后遇到 overlap correction 想被提升成新状态变量时，应先检查它是否只是某个已知最大 refinement 的 zeta transform。

---

## 9. 可执行验证

`src/enterprise_math/p017_core_cell_lattice.py` 与 `tests/test_p017_core_cell_lattice.py` 检查：

- raw partial-core cell 是模 `2ab` 的唯一奇 CRT 等差类；
- CC01 的 lcm 交闭包以及跨侧冲突为空；
- exact full-core 标签精确分割 anchor-surviving radii；
- CC02 membership 与 exact full cores 的整除关系完全一致；
- CC03 partial 计数等于 exact-stratum zeta 求和；
- 双 Möbius 反演精确恢复 exact stratum 计数；
- CC04 的 factor-three refinement depth 上界成立。

有限测试审计参考实现；数学陈述来自整除、CRT、规范 full-core 定义与普通 Möbius 反演。
