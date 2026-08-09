# P007 —— 对偶因子窗口传输，补充 02

状态：`PROVED RESEARCH NOTE`  
归属：A0 / P007 离散除法  
来源压力：P017 high-band root precision  
纪律：Euclidean division 与区间投影属于成熟数学。项目新增价值是把它固定成可复用有限状态传输接口，并用于后续数论路线。

## 1. 设置

令

\[
0\le A<B
\]

并考虑正整数 `d,q` 的乘法 incidence：

\[
\boxed{A<dq\le B}.
\]

P007 补充 01 固定 `d`，把这一关系投影到 quotient 坐标：

\[
W_d(A,B)
=
\{q:A<dq\le B\}
=
\left[
\left\lfloor\frac A d\right\rfloor+1,
\left\lfloor\frac B d\right\rfloor
\right].
\]

本补充固定一个 quotient bucket，把同一个 incidence 向相反方向投影。

## 2. P007-S2-T01 —— 对偶因子窗口定理

状态：`PROVED`。

固定正整数 quotient bucket

\[
J=[L,U],
\qquad
1\le L\le U.
\]

定义

\[
D_J(A,B)
=
\{d\ge1:W_d(A,B)\cap J\ne\varnothing\}.
\]

则当下式区间非空时，

\[
\boxed{
D_J(A,B)
=
\left[
\left\lfloor\frac A U\right\rfloor+1,
\left\lfloor\frac B L\right\rfloor
\right],
}
\]

否则 `D_J(A,B)` 为空。

### 证明

交集非空，当且仅当存在 `q` 满足

\[
L\le q\le U,
\qquad
A<dq\le B.
\]

由于正整数 `d` 的乘法对 `q` 单调，这样的 `q` 存在，当且仅当两个端点条件同时成立：

\[
A<dU,
\qquad
dL\le B.
\]

对整数 `d`，这等价于

\[
d\ge\left\lfloor\frac A U\right\rfloor+1,
\qquad
d\le\left\lfloor\frac B L\right\rfloor.
\]

故得到所述精确闭整数窗口。∎

## 3. P007-S2-T02 —— 精确候选基数

状态：`PROVED`。

若对偶窗口非空，则

\[
\boxed{
|D_J(A,B)|
=
\left\lfloor\frac B L\right\rfloor
-
\left\lfloor\frac A U\right\rfloor.
}
\]

### 证明

下端点为 `floor(A/U)+1`，上端点为 `floor(B/L)`；闭整数区间基数等于上端点减下端点再加一。∎

这个计数是一个精确的**整数候选资源**。如果后续要求 `d` 必须是 prime、rough、coprime 或满足其他 admissibility 条件，这些谓词必须在对偶传输之后再施加，不能暗中混入窗口定义。

## 4. P007-S2-T03 —— root-basin 因子窗口

状态：`PROVED`。

对 square-basin 源区间

\[
(k^2,k(k+2)]
\]

以及保留的平方根 index `s`，quotient bucket 为

\[
J_s=[s^2,(s+1)^2-1]=[s^2,s(s+2)].
\]

因此 raw quotient window 能够命中 root `s` 的正因子恰好是

\[
\boxed{
D_{k,s}
=
\left[
\left\lfloor\frac{k^2}{s(s+2)}\right\rfloor+1,
\left\lfloor\frac{k(k+2)}{s^2}\right\rfloor
\right].
}
\]

这就是 P017 high-band root-label 窗口的算术来源。

## 5. Incidence 对偶，而不是逆重建

P007 的两个窗口

\[
d\mapsto W_d(A,B)
\]

与

\[
J\mapsto D_J(A,B)
\]

只是同一个有限关系

\[
\mathcal R_{A,B}
=
\{(d,q):A<dq\le B\}
\]

的两个投影。

这**不**表示 quotienting 可逆。它表示：一旦声明一个 quotient bucket，就能在不枚举整个源区间的情况下，精确传输出所有相容 factor labels。

这对 future-safe precision 很重要：保留的 quotient/root bucket 会诱导一个有限、精确的隐藏 factor 候选集；另一个独立的 admissibility predicate 决定其中哪些候选真正被物理或数论状态实现。

## 6. 研究工具解释

该定理给出一个可复用的两阶段编译器：

1. 用 dual factor window **精确传输 envelope**；
2. 再施加 realizability / admissibility filter。

因此

\[
\boxed{
\text{exact envelope}
\neq
\text{realized state set（一般情形）}.
}
\]

对偶窗口不交可以推出真实 labels 不交；但对偶窗口相交本身不能推出真实 collision。

## 7. 可执行规格

- `src/enterprise_math/quotient_window.py`
- `tests/test_p007_dual_factor_window.py`

测试在小整数区间上穷举重建定理，并验证 factor-side 与 quotient-side 两种视角得到完全相同的 incidence relation。

## 8. 前人工作纪律

证明只是初等 Euclidean-division 区间算术，不主张属于新的通用数学。Enterprise Math 的作用是把它固定成 canonical finite transport primitive，用于连接 quotient precision、factor precision、root bucket 与后续 repair counting。
