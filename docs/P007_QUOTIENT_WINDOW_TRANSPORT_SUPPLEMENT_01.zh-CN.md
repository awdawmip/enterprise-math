# P007 —— 精确商窗口搬运，补充 01

状态：`PROVED`  
归属：A0 / P007 离散除法核心  
来源压力：P017 L054 first-factor cofactor windows  
纪律：这里只使用欧几里得整数除法与整数不等式；不主张发明 floor division 或区间算术。

## 1. 为什么从 P017 回灌到 P007

P017 在连续平方盆地中反复出现

\[
W_p(k)=\left[
\left\lfloor\frac{k^2}{p}\right\rfloor+1,
\left\lfloor\frac{k(k+2)}{p}\right\rfloor
\right].
\]

L054 证明不同 least-prime shells 的这些窗口从 `k>=4` 起严格分离。

但这个现象本身不需要素数，也不需要平方。它首先是一个关于**开闭整数区间经过精确商坐标以后如何搬运**的 P007 定理。

因此本补充把领域假设全部移除，再把 P017 L054 降回推论。

## 2. 设置

固定整数

\[
0\le A<B,
\qquad d\ge1.
\]

定义源区间

\[
I=(A,B]\cap\mathbb N_0
\]

以及乘法坐标

\[
M_d(q)=dq.
\]

P007 已有右伴随

\[
M_d\dashv Q_d,
\qquad
Q_d(n)=n//d.
\]

定义因子 `d` 的精确商窗口

\[
\boxed{
W_d(A,B)=\{q\in\mathbb N_0:A<dq\le B\}.
}
\]

## 3. P007-S1-T09 —— 精确 quotient-window transport

状态：`PROVED`。

有

\[
\boxed{
W_d(A,B)
=
\left[
Q_d(A)+1,
Q_d(B)
\right]\cap\mathbb N_0.
}
\]

若左端点大于右端点，则窗口为空。

### 证明

对整数 `q`，

\[
A<dq
\iff
Q_d(A)<q,
\]

因为 `Q_d(A)` 是满足 `dt<=A` 的最大整数 `t`。

另一方面由 P007-T02，

\[
dq\le B
\iff
q\le Q_d(B).
\]

所以

\[
A<dq\le B
\iff
Q_d(A)+1\le q\le Q_d(B).
\]

证毕。

### 解释

这不是把实区间 `(A/d,B/d]` 再“取整近似”。它直接给出离散乘法坐标 `M_d` 对源整数区间的**精确逆像**。

因此 factor stripping、cofactor window、quotient shell 都可以优先写成这一标准形。

## 4. P007-S1-T10 —— 两个商窗口的精确分离判据

状态：`PROVED`。

设

\[
1\le d<e.
\]

当两个窗口都非空时，以下命题等价：

1. `W_e(A,B)` 中每个状态都严格小于 `W_d(A,B)` 中每个状态；
2.
   \[
   \boxed{Q_e(B)\le Q_d(A).}
   \]

### 证明

由 T09，

\[
\max W_e=Q_e(B),
\qquad
\min W_d=Q_d(A)+1.
\]

严格分离等价于

\[
Q_e(B)<Q_d(A)+1,
\]

对整数正好等价于 `Q_e(B)<=Q_d(A)`。∎

因此 shell separation 可以被压成两个**整数端点状态**的比较，而不需要枚举窗口内部。

## 5. P007-S1-T11 —— 纯整数叉乘充分条件

状态：`PROVED`。

若

\[
\boxed{dB\le eA,}
\]

则

\[
Q_e(B)\le Q_d(A),
\]

从而两个窗口严格分离。

### 证明

由 `dB<=eA` 得

\[
\frac Be\le\frac Ad.
\]

但证明不需要把分数加入状态空间。等价地，任取满足 `eq<=B` 的整数 `q`，有

\[
dq\le \frac de B\le A,
\]

所以 `q<=Q_d(A)`。特别地取 `q=Q_e(B)` 即得。∎

这一形式只使用整数乘法与序关系。

## 6. P007-S1-T12 —— 精确间隙资源

状态：`PROVED`。

当两个非空窗口严格分离时，定义其间没有被任一窗口使用的 quotient 状态数

\[
G_{d,e}(A,B)
=
\min W_d-\max W_e-1.
\]

则

\[
\boxed{
G_{d,e}(A,B)
=Q_d(A)-Q_e(B)\ge0.
}
\]

所以窗口分离不仅是 Boolean 事实，还天然带一个整数 margin。这个 margin 可以被后续 packing/resource argument 直接消费。

## 7. 连续平方盆地的统一特化

取

\[
A=k^2,
\qquad
B=k(k+2),
\qquad
1\le d<e\le k.
\]

T11 的叉乘条件化为

\[
dk(k+2)\le ek^2,
\]

即

\[
\boxed{k(e-d)\ge2d.}
\]

### P007-S1-C01 —— 间距至少 2 自动分离

若

\[
e-d\ge2,
\qquad d\le k,
\]

则

\[
k(e-d)\ge2k\ge2d,
\]

所以

\[
\boxed{W_e(k^2,k(k+2))<W_d(k^2,k(k+2)).}
\]

这里完全没有使用素数。

## 8. P017 L054 成为直接推论

令 `p<r<=k` 为素数，`k>=4`。

- 若 `p>=3`，则 `p,r` 都是奇素数，所以 `r-p>=2`，由 C01 自动分离；
- 若 `p=2` 且 `r>=5`，同样 `r-p>=3`；
- 唯一相邻素数情形是 `(p,r)=(2,3)`，此时条件变成
  \[
  k\ge4.
  \]

因此 P017 L054 的统一阈值 `k>=4` 立刻恢复。

这说明 L054 中真正属于 prime arithmetic 的信息极少：除 `(2,3)` 外，所需 spacing 已由奇素数的最小间距自动提供；母结构是 P007 的 quotient-window transport。

## 9. 对数论研究方法的反哺

当一个整数区间按候选因子 `d` 分 shell 时，不应默认保留二维标签 `(d,q)`，也不应立即用粗密度估计代替精确窗口。更强的顺序是：

1. 先用 T09 写出 exact quotient window；
2. 用 T10/T11 检查不同 shells 是否已经按 quotient 坐标分离；
3. 用 T12 保留 separation margin；
4. 只有窗口仍相交时，才引入额外 shell label、CRT residue 或其他 repair coordinate。

这把“先估计数量”改成“先消除不必要的状态维度”。

## 10. 与 P024 的关系

P007 的 `M_d ⊣ Q_d` 已经是 P008/P024 伴随结构的实例。本补充研究的是一个双边 interval query，而不是单个 principal threshold；其两个端点分别由精确整数商搬运。

因此可以把 T09 看成：

> 两条边界分别做伴随搬运后，其间的离散原子就是 exact quotient window。

P024 负责一般未来 boundary pullback；P007 保留这里的具体整数除法闭式。

## 11. 可执行审计

- `src/enterprise_math/quotient_window.py`
- `tests/test_p007_quotient_window_transport.py`

测试穷举小整数区间核对 T09，逐例比较 T10 的 endpoint criterion，并验证 T11 的叉乘条件从不产生假分离；同时固定 P017 `k=3` 的 sharp raw-window overlap 与 `k=4` 的首次统一分离。

## 12. 前人工作与新颖性纪律

Euclidean/floor division、整数区间端点运算以及 Galois adjunction 都是成熟数学。这里不主张这些一般事实的新颖性。

项目新增价值是把它们提炼成一个可重复的**数论 shell-window 编译工具**，并明确证明 P017 L054 是该 A0 工具的特化，而不是继续在 Legendre 路线内部维护一份孤立证明。
