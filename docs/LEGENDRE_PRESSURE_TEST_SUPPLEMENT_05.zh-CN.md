# Legendre 压力测试 —— 补充 05

状态：`ACTIVE RESEARCH NOTE`  
范围：首因子壳层的精确 cofactor window 与正的 rough-window 归约  
依赖：P017 L001–L019 与 canonical P018 精度/因子工具  
纪律：**本文不证明 Legendre 猜想。**

## 1. 为什么这一部分值得从探索稿中保留

记连续平方之间的开放盆地

\[
B_k=\{n\in\mathbb N:k^2<n<(k+1)^2\}.
\]

对每个素数 \(p\le k\)，令 \(L_p(k)\) 表示 \(B_k\) 中最小素因子恰好为 \(p\) 的状态。

本补充真正保留的不是一个“新素性判据”，而是每个最小因子壳层的精确有限坐标：

\[
\boxed{\text{平方盆地几何}\longrightarrow\text{短 cofactor 区间}\longrightarrow\text{p-rough 幸存者}.}
\]

rough number、最小素因子分拆、smooth part、整数除法与 trial division 都属于成熟数论。项目问题只在于：把这些结构精确组织到连续平方盆地后，是否能产生新的证明杠杆。

---

## 2. L020 —— 平方盆地 smooth-tail 二分

状态：`PROVED`。

对 \(n\in B_k\)，定义完整的 \(k\)-smooth core

\[
S_k(n)=\prod_{p\le k}p^{v_p(n)}
\]

和剩余 tail

\[
Q_k(n)=n/S_k(n).
\]

则

\[
\boxed{Q_k(n)=1\quad\text{或}\quad Q_k(n)\text{ 是一个 }>k\text{ 的素数}.}
\]

### 证明

\(Q_k(n)\) 的每个素因子都大于 \(k\)。若 \(Q_k(n)>1\) 且为合数，则按重数至少含两个素因子，因此

\[
Q_k(n)\ge(k+1)^2.
\]

但 \(Q_k(n)\le n<(k+1)^2\)，矛盾。证毕。

于是

\[
\boxed{n\text{ 为素数}\iff S_k(n)=1.}
\]

---

## 3. L021 —— 精确 cofactor window

状态：`PROVED`。

固定素数 \(p\le k\)，令

\[
c=k+1,\qquad r=c-p,
\]

并把壳层候选写成 \(n=pq\)。

条件

\[
(c-1)^2<pq<c^2
\]

等价于

\[
\boxed{
q_{\min}=c+r-1+\left\lfloor\frac{(r-1)^2}{p}\right\rfloor
}
\]

与

\[
\boxed{
q_{\max}=c+r+\left\lfloor\frac{r^2-1}{p}\right\rfloor.
}
\]

### 证明

下端点方面，

\[
(c-1)^2=(p+r-1)^2=p(p+2r-2)+(r-1)^2,
\]

所以

\[
q\ge\left\lfloor\frac{(c-1)^2}{p}\right\rfloor+1
=c+r-1+\left\lfloor\frac{(r-1)^2}{p}\right\rfloor.
\]

上端点方面，

\[
c^2-1=p(p+2r)+(r^2-1),
\]

所以

\[
q\le\left\lfloor\frac{c^2-1}{p}\right\rfloor
=c+r+\left\lfloor\frac{r^2-1}{p}\right\rfloor.
\]

两端都是精确整数界。证毕。

---

## 4. L022 —— 首因子壳层等于 p-rough window

状态：`PROVED`。

若 \(q\) 不含任何严格小于 \(p\) 的素因子，称 \(q\) 为 **p-rough**。则

\[
\boxed{
L_p(k)=
\left\{
pq:q_{\min}\le q\le q_{\max},\ q\text{ 为 p-rough}
\right\}.
}
\]

### 证明

若 \(pq\in L_p(k)\)，L021 已把 \(q\) 限制在精确区间。若 \(q\) 含小于 \(p\) 的素因子，该因子也会整除 \(pq\)，与 \(p\) 是最小素因子矛盾。

反过来，区间候选 \(pq\) 由 L021 保证位于 \(B_k\)；若 \(q\) 为 p-rough，则没有小于 \(p\) 的素数能整除两个因子的乘积，因此 \(pq\) 的最小素因子恰好是 \(p\)。证毕。

所以平方几何被压缩后，剩余的算术障碍精确地变成了一个有限显式区间里的 roughness。

---

## 5. L023 —— 中心修正坐标与精确平方边界距离

状态：`PROVED`。

写成

\[
q=c+r+j.
\]

则

\[
-1+\left\lfloor\frac{(r-1)^2}{p}\right\rfloor
\le j\le
\left\lfloor\frac{r^2-1}{p}\right\rfloor.
\]

因为 \(p=c-r\)，

\[
pq=(c-r)(c+r+j)=c^2-r^2+jp.
\]

所以距两个平方边界的精确整数偏移为

\[
\boxed{c^2-pq=r^2-jp}
\]

以及

\[
\boxed{pq-(c-1)^2=p(j+2)-(r-1)^2.}
\]

对称乘积 \(c^2-r^2\) 只是特殊坐标 \(j=0\)，不是一般壳层。

---

## 6. L024 —— window 增长 = bulk + 一个 carry

状态：`PROVED`。

未经过 p-rough 筛选的整数 cofactor 数量为

\[
N_{\mathrm{raw}}=q_{\max}-q_{\min}+1,
\]

因此

\[
\boxed{
N_{\mathrm{raw}}
=2+
\left\lfloor\frac{r^2-1}{p}\right\rfloor
-
\left\lfloor\frac{(r-1)^2}{p}\right\rfloor.
}
\]

令

\[
a=(r-1)^2,\qquad h=2r-2.
\]

因为 \(a+h=r^2-1\)，window 宽度修正正是精确商状态输运

\[
\left\lfloor\frac{a+h}{p}\right\rfloor-\left\lfloor\frac a p\right\rfloor.
\]

再写

\[
a=pA+u,\qquad h=pH+v,
\qquad 0\le u,v<p,
\]

得到

\[
\boxed{
N_{\mathrm{raw}}
=2+
\left\lfloor\frac{2r-2}{p}\right\rfloor
+
\left\lfloor\frac{u+v}{p}\right\rfloor,
}
\]

最后一项只能取 \(0\) 或 \(1\)。

所以有限 window 具有精确分解

\[
\boxed{\text{两个基础候选}+\text{整块增长}+\text{一个边界 carry}.}
\]

这是 canonical P018 中精确 quotient-defect transport 的一个算术实例，不构成任何新的物理解释证据。

---

## 7. L025 —— 两/三候选区间与修正后的近对角退化

状态：`PROVED`。

### 两个或三个 raw candidates

若

\[
p>2(r-1),
\]

则 L024 中的整块增长项为 0，因此

\[
\boxed{N_{\mathrm{raw}}\in\{2,3\}.}
\]

取 2 还是 3，完全由最后一个边界 carry 决定。

### 强近对角定理

要把一般 cofactor window 退化为对称素数条件，正确的充分条件是

\[
\boxed{p\ge3\qquad\text{且}\qquad p>r^2.}
\]

条件 \(p>r^2\) 让 L021 中两个 floor 项都归零，所以

\[
q\in\{c+r-1,c+r\}.
\]

由于 \(p\ge3\) 是奇素数，且 \(c+r=p+2r\) 为奇数，第一个候选 \(c+r-1\) 是大于 \(p\) 的偶数，因此不可能 p-rough。

第二个候选满足

\[
p<c+r<p^2.
\]

任何大于 \(p\) 的 p-rough 合数至少为 \(p^2\)，故在该区间内 p-rough 与素数等价。因此

\[
\boxed{
L_p(k)\ne\varnothing
\iff
c+r\text{ 为素数},
}
\]

并且非空时

\[
\boxed{L_p(k)=\{(c-r)(c+r)\}=\{c^2-r^2\}.}
\]

### 为什么必须要求 \(p\ge3\)

不能只保留 \(p>r^2\)。取

\[
k=2,\quad c=3,\quad p=2,\quad r=1.
\]

此时确有 \(p>r^2\)，但 raw cofactor window 为

\[
\{3,4\}.
\]

当 \(p=2\) 时，不存在更小的素数可被 p-rough 条件排除，因此两个候选都幸存：

\[
L_2(2)=\{6,8\},
\]

而 \(c+r=4\) 是合数。这就是修正历史性过强表述所需的显式边界反例。

### 三候选边界例

取 \(k=10\)、\(c=11\)、\(p=7\)、\(r=4\)，L021 给出

\[
q\in\{15,16,17\}.
\]

其中只有 \(17\) 为 7-rough，所以

\[
L_7(10)=\{119\}.
\]

强近对角条件不成立，但一般 window 公式仍保持精确。

---

## 8. L026 —— 整数根深度约束因子重数

状态：`PROVED`。

记

\[
U=(k+1)^2-1.
\]

若

\[
\boxed{p^{m+1}>U,}
\]

则每个 \(n\in L_p(k)\) 都满足

\[
\boxed{\Omega(n)\le m,}
\]

其中 \(\Omega\) 按重数统计素因子个数。

### 证明

若 \(\Omega(n)\ge m+1\)，而 \(p\) 是最小素因子，则每个素因子都至少为 \(p\)，从而

\[
n\ge p^{m+1}>U,
\]

与 \(n\le U\) 矛盾。证毕。

等价地，可用整数根阈值写成 \(p>R_{m+1}(U)\)。若 \(n=pq\)，同一论证给出 \(\Omega(q)\le m-1\)。

---

## 9. L027 —— 正的 rough-window prime-count 恒等式

状态：`PROVED REINDEXING`。

开放平方盆地恰有 \(2k\) 个状态。每个合数状态都唯一属于某个最小素因子 \(p\le k\) 的壳层 \(L_p(k)\)。所以

\[
\Pi(k)=2k-\sum_{p\le k}|L_p(k)|.
\]

由 L022，

\[
\boxed{
\Pi(k)
=
2k-
\sum_{p\le k}
\#\{q\in[q_{\min}(k,p),q_{\max}(k,p)]:q\text{ 为 p-rough}\}.
}
\]

于是 Legendre 猜想等价于

\[
\boxed{
\sum_{p\le k}
\#\{q\in W_p(k):q\text{ 为 p-rough}\}
\le2k-1.
}
\]

这是正的最小因子重排恒等式，不是对该不等式的证明。

---

## 10. 真正剩下的开放困难

平方几何与壳层坐标现在已经显式化。尚未解决的证明内容被集中到一个位置：

> **控制所有相关短 window \(W_p(k)\) 中 p-rough 幸存者的总数。**

精确 window 公式把最小因子阈值 \(p\)、平方中心 \(c=k+1\) 和偏移 \(r=c-p\) 绑定在一起，这可能提供进一步杠杆；但本文目前没有任何已证明估计能够推出所有 \(k\) 都有

\[
\Pi(k)>0.
\]

所以当前状态仍然是：

- L020–L026：`PROVED` 结构归约；
- L027：`PROVED REINDEXING`；
- Legendre 猜想：仍然开放；
- 这一精确组织方式的历史创新性：`NOVELTY_UNVERIFIED`。

实现 `src/enterprise_math/p017_cofactor_window.py` 与其回归测试会审计这些精确恒等式，并显式锁定 \(p=2\) 边界反例。
