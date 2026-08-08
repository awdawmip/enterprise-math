# P023 —— 精度兼容补充 01

状态：`ACTIVE RESEARCH NOTE`  
范围：P007 商 / multiple-collapse 与 P018 floor-precision 投影之间的精确兼容分类

## 1. 设置

固定正精度比 `r`，定义

\[
\pi_r(n)=Q_r(n)=n//r.
\]

对正整数 `d`，回顾

\[
Q_d(n)=n//d,
\qquad
D_d(n)=d(n//d).
\]

P023 要问的是：细粒度运算能否下沉到 `\pi_r` 给出的粗精度状态。

## 2. P023-T08 —— quotient 对任意该类精度投影都兼容

对任意正整数 `r,d` 与任意 `n in N`，

\[
\boxed{
\pi_r(Q_d(n))=Q_d(\pi_r(n)).
}
\]

等价地，

\[
Q_rQ_d=Q_dQ_r=Q_{rd}.
\]

因此精确 quotient 在这些粗精度状态上运行时，不需要额外修复 detail。

### 证明

正整数 floor division 满足

\[
(n//d)//r=n//(dr)=(n//r)//d.
\]

## 3. P023-T09 —— 同空间 multiple-collapse 的精确分类

映射

\[
\pi_r\circ D_d
\]

能够通过 `\pi_r` 下沉，当且仅当

\[
\boxed{d\mid r\quad\text{或}\quad r\mid d.}
\]

也就是说，兼容性恰好等价于两个参数在整除序下可比。

### 情形 1：`d|r`

写成 `r=ds`。若

\[
n=qr+t,
\qquad 0\le t<r,
\]

则

\[
D_d(n)=qr+d(t//d).
\]

余项满足

\[
0\le d(t//d)<r,
\]

因此

\[
\boxed{
\pi_r(D_d(n))=q=\pi_r(n).
}
\]

故诱导粗映射就是恒等映射。

### 情形 2：`r|d`

写成 `d=rs`。则

\[
\pi_r(D_d(n))
=
s(n//rs).
\]

再利用

\[
n//(rs)=(n//r)//s,
\]

得到

\[
\boxed{
\pi_r(D_d(n))
=
D_s(\pi_r(n)).
}
\]

所以诱导粗运算精确等于 `D_(d/r)`。

## 4. 参数不可比时的统一显式 witness

假设既没有 `d|r`，也没有 `r|d`。

### 若 `d<r`

取

\[
x=r,
\qquad
y=(r//d+1)d.
\]

由于 `d` 不整除 `r`，有

\[
r<y<r+d<2r,
\]

故

\[
\pi_r(x)=\pi_r(y)=1.
\]

但是

\[
D_d(x)=d(r//d)<r,
\]

而 `D_d(y)=y>=r`，于是

\[
\pi_r(D_d(x))=0,
\qquad
\pi_r(D_d(y))=1.
\]

### 若 `d>r`

写成

\[
d=kr+s,
\qquad 0<s<r.
\]

取

\[
x=d-1,
\qquad y=d.
\]

则

\[
\pi_r(x)=\pi_r(y)=k,
\]

但

\[
D_d(x)=0,
\qquad
D_d(y)=d,
\]

所以

\[
\pi_r(D_d(x))=0,
\qquad
\pi_r(D_d(y))=k>0.
\]

因此不存在诱导粗映射。

## 5. 结构结论

这是 P023 descent 判据在我们自己算术核心中的一个具体实例：

- `Q_d` 尊重任意 floor-precision quotient；
- `D_d` 尊重 `Q_r`，恰好发生在整除可比的尺度对上；
- 对不可比尺度，如果还想从粗状态预测 `D_d` 的粗输出，就必然需要补回额外 detail。

这个分类与 P007 已有的 same-space multiple-collapse 交换性整除分类形式相似，但问题并不相同：这里研究的是**通过精度商下沉**，而不是两个同空间 endomap 是否交换。

## 6. 可执行审计

- `src/enterprise_math/p023_precision_compatibility.py`
- `tests/test_p023_precision_compatibility.py`

测试覆盖 quotient 恒等式的有界验证、正参数上的整除分类、两类诱导粗映射，以及不可比参数时的显式 witness。
