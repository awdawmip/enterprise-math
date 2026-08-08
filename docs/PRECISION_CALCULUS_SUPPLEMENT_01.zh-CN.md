# P018 —— 有限精度证明演算：补充 01

状态：`ACTIVE RESEARCH NOTE`  
范围：尺度次数、分级搬运、齐次非线性精度缺陷  
依赖：`docs/PRECISION_CALCULUS.zh-CN.md`  
纪律：graded algebra 是成熟数学；本文研究的是它与有限多对一精度投影的结合。

## 1. 为什么精度必须带次数

第一阶段把普通数值状态、根状态都视为尺度次数 `1` 的量。当精度比为

\[
r=e/d,
\]

粗状态的规范搬运是

\[
a\mapsto ra.
\]

但不是所有数学量都按一次尺度增长。

- 普通状态或根状态：尺度次数 `1`；
- 两个一次状态的乘积：尺度次数 `2`；
- `p` 次幂：尺度次数 `p`；
- degree `q` 与 degree `s` 两个量的乘积：degree `q+s`。

因此，对所有对象都固定使用 `//r` 并不类型正确。degree `q` 的量应当按 `r^q` 搬运，也按 `r^q` 做整数投影。

这只是成熟 graded 思想在精度坐标上的应用。graded ring 中乘法使次数相加是已有数学；P018 不把这个概念据为原创。

## 2. P018-T13 —— degree-q 精度纤维

状态：`PROVED`

对非负尺度次数 `q` 定义

\[
\tau^{(q)}_{d\to e}(a)=r^q a,
\qquad
\pi^{(q)}_{e\to d}(x)=x\operatorname{//}r^q,
\]

以及

\[
\delta^{(q)}_{e:d}(x)=x\bmod r^q.
\]

则任意 degree `q` 的细精度量都有唯一分解

\[
\boxed{
x
=r^q\pi^{(q)}_{e\to d}(x)
+
\delta^{(q)}_{e:d}(x),
\qquad
0\le\delta^{(q)}_{e:d}(x)<r^q.
}
\]

`q=1` 时回到 P018-T01；`q=p` 时，正好得到第一阶段 collapse/refinement recovery 所需的输出投影。

因此“degree”应被视作尺度相关数学量的类型信息：同一个细整数，若代表不同尺度次数的对象，其粗精度意义可以完全不同。

## 3. P018-T14 —— 分级搬运律

状态：`PROVED / ESTABLISHED GRADED PATTERN`

同次数量的和满足

\[
\boxed{
\tau^{(q)}(a+b)
=
\tau^{(q)}(a)+\tau^{(q)}(b).
}
\]

若两个量的次数分别为 `q` 与 `s`，则

\[
\boxed{
\tau^{(q+s)}(ab)
=
\tau^{(q)}(a)\tau^{(s)}(b).
}
\]

证明只是 `r` 的幂律。

真正困难的不是精化搬运，而是多对一粗投影：floor projection 一般不保持非线性乘法，因此会产生有限的 defect/carry。

## 4. P018-T15 —— degree-q 搬运 Möbius 精度壳层

状态：`PROVED`

对尺度次数为 `q` 的整数值量 `A(c)`，定义

\[
\boxed{
\widehat A_q(d)
=
\sum_{c\mid d}
\mu(d/c)
\left(\frac dc\right)^q A(c).
}
\]

则

\[
\boxed{
A(d)
=
\sum_{c\mid d}
\left(\frac dc\right)^q
\widehat A_q(c).
}
\]

证明与 P018-T07 的除数格 Möbius 反演相同，只是把一次搬运替换为 degree `q` 搬运。

### 齐次 bulk 消去

若

\[
A(c)=c^q A(1),
\]

则任意 `d>1` 都有

\[
\boxed{
\widehat A_q(d)=0.
}
\]

所以第一阶段的 shell 只是分级 shell 家族中的 degree-1 成员。只要某个量严格服从正确次数的齐次尺度律，它在所有非平凡 precision shell 中都会完全消失；壳层只保留偏离齐次搬运的真正精度结构。

## 5. 齐次单项式

设

\[
M(x_1,\ldots,x_m)
=
\prod_{i=1}^m x_i^{\alpha_i},
\]

每个输入都是 degree 1，并令

\[
q=\sum_i\alpha_i>0.
\]

把每个细状态写成

\[
x_i=ra_i+u_i,
\qquad
0\le u_i<r.
\]

规范搬运的粗单项式是

\[
r^q M(a_1,\ldots,a_m).
\]

由于 detail 之间发生非线性交互，真实细单项式一般会更大。

## 6. P018-T16 —— 单项式精度缺陷界

状态：`PROVED`

定义恢复到粗层的单项式

\[
\mathcal R_M
=
\left\lfloor
\frac{M(x_1,\ldots,x_m)}{r^q}
\right\rfloor
\]

以及**精度自然性缺陷**

\[
D_M
=
\mathcal R_M-M(a_1,\ldots,a_m).
\]

则

\[
\boxed{D_M\ge0.}
\]

并且

\[
\boxed{
D_M
\le
M(a_1+1,\ldots,a_m+1)
-
M(a_1,\ldots,a_m)
-1.
}
\]

证明：因为

\[
ra_i\le x_i<r(a_i+1),
\]

由齐次性得

\[
r^qM(a)
\le
M(x)
<
r^qM(a+\mathbf 1).
\]

再按 `r^q` 做整数投影即可。∎

同时存在唯一输出 detail `rho`：

\[
\boxed{
M(x)
=
r^q\bigl(M(a)+D_M\bigr)+\rho,
\qquad
0\le\rho<r^q.
}
\]

所以 `D_M` 不是近似误差，而是细节的非线性交互让结果穿过了多少个 degree-`q` 粗单元的精确整数。

## 7. P018-T17 —— 乘法精度 carry

状态：`PROVED`

对两个 degree-1 状态

\[
x=rA+u,
\qquad
y=rB+v,
\]

乘积是 degree 2。投回粗层得到

\[
\left\lfloor\frac{xy}{r^2}\right\rfloor
=AB+C_\times,
\]

其中

\[
\boxed{
C_\times
=
\left\lfloor
\frac{rAv+rBu+uv}{r^2}
\right\rfloor.
}
\]

并且

\[
\boxed{
0\le C_\times\le A+B.
}
\]

因为 T16 的一般上界在此恰为

\[
(A+1)(B+1)-AB-1=A+B.
\]

还存在唯一 product detail

\[
0\le\rho_\times<r^2
\]

使得

\[
\boxed{
xy=r^2(AB+C_\times)+\rho_\times.
}
\]

它是 P018-T04 二值加法 carry 的乘法版本；但乘法输出次数为 2，一个细节交互可以穿越多个粗乘积单元，所以 carry 不再要求只有 0/1。

## 8. P018-T18 —— 幂精度 carry

状态：`PROVED`

设

\[
x=rk+u,
\qquad0\le u<r.
\]

映射 `x -> x^p` 的尺度次数为 `p`。定义

\[
C_p^{\mathrm{prec}}
=
\left\lfloor\frac{x^p}{r^p}\right\rfloor-k^p.
\]

则

\[
\boxed{
0\le C_p^{\mathrm{prec}}
\le
(k+1)^p-k^p-1.
}
\]

也就是说，控制 perfect-power collapse 盆地宽度的同一个表达式，也精确控制普通 `p` 次幂映射的 precision carry。

这不是偶然：在一个根纤维内部改变 degree-1 detail 后，经 `p` 次幂映射能够触及的 degree-`p` 粗单元范围，正是相应 perfect-power basin 的宽度。

## 9. P018-T19 —— 单项式精化恢复单调性

状态：`PROVED`

设

\[
d\mid e\mid f
\]

并令精度 `f` 上一组 degree-1 状态相容地投影到 `e` 与 `d`。

对总次数为 `q` 的齐次单项式 `M`，定义从中间精度 `e` 恢复到基础精度 `d`：

\[
\mathcal R_{M;e\to d}
=
\pi^{(q)}_{e\to d}
\bigl(M(x_e)\bigr).
\]

则

\[
\boxed{
\mathcal R_{M;e\to d}
\le
\mathcal R_{M;f\to d}.
}
\]

证明：写 `s=f/e`，每个分量都有

\[
x_f=sx_e+u_i\ge sx_e.
\]

由非负指数与齐次性，

\[
M(x_f)\ge s^qM(x_e).
\]

再做 degree-`q` 投影即得。∎

因此，第一阶段的 collapse recovery 单调性属于更一般的原则：**非负齐次单项式在有限输入精度提高时，恢复出的粗层结构单调增加。**

## 10. P018-T20 —— collapse defect 就是根的幂 carry

状态：`PROVED`

第一阶段定义

\[
S_{p,d}(n)=R_p(nd^p)
\]

以及 collapse/refinement defect

\[
\chi_{p;e:d}(n)
=
\left\lfloor
\frac{S_{p,e}(n)^p}{(e/d)^p}
\right\rfloor
-
S_{p,d}(n)^p.
\]

P018-T09 给出

\[
S_{p,e}(n)
=rS_{p,d}(n)+\eta,
\qquad0\le\eta<r.
\]

代入 P018-T18 立刻得到

\[
\boxed{
\chi_{p;e:d}(n)
=
C_p^{\mathrm{prec}}
\bigl(S_{p,e}(n);d,e\bigr).
}
\]

也就是说：

> 原本看似“collapse 与精度精化不交换”的特殊现象，其实就是根状态的 detail 经过 `p` 次幂映射时产生的普通 degree-`p` precision carry。

这使理论少了一个特例对象。第一阶段的 collapse recovery 已经成为 graded nonlinear precision-defect calculus 的直接实例。

## 11. 结构解释

第二阶段必须严格区分两种映射。

### 精确精化搬运

\[
\tau^{(q)}_{d\to e}(a)=r^qa
\]

是完全精确的，并且遵守 grading。

### 多对一粗投影

\[
\pi^{(q)}_{e\to d}(x)=x//r^q
\]

会丢失有界 degree-`q` detail。

同次数线性加法在搬运层完全兼容；输入 detail 仍可能按第一阶段的规则产生加法 carry。非线性齐次映射会产生更大的 naturality defect，但它仍然是有限整数，并被一个粗输入 cell 的像宽严格控制。

于是 P018 的一般结构开始呈现为：

\[
\boxed{
\text{精确 graded transport}
+
\text{多对一 projection}
+
\text{有界 naturality defect}.
}
\]

这里的 defect 不是外部误差估计，而是内部有限对象，用来量化提高精度以后究竟显现了多少新的非线性结构。

## 12. 反例/边界：projection 不是 graded homomorphism

不能因为 transport 严格遵守 grading，就误以为 coarse floor projection 也保持乘法：

\[
\pi^{(2)}(xy)
\stackrel{?}{=}
\pi^{(1)}(x)\pi^{(1)}(y).
\]

只要 `C_x` 非零，这通常就是假的。

例如 ratio `r=10`，取

\[
x=y=19.
\]

则

\[
\pi^{(1)}(19)=1,
\qquad
\pi^{(2)}(19^2)=361//100=3.
\]

乘法 precision carry 等于 `2`。

因此真正的 graded 结构属于**搬运**；projection 是多对一的，并带有受控有限缺陷。

## 13. 前人边界

graded ring/algebra 以及“齐次乘法使次数相加”都是成熟数学。P018 只复用该语言，不声称发明 grading。

第二阶段真正的项目问题是：把 scale degree 赋给有限精度状态以后，能否形成一套有用演算，使得：

- 不同 degree 的量使用不同粗投影；
- 齐次 bulk 被 degree-aware transported Möbius shell 消去；
- 非线性运算产生精确有限的 cell-crossing defect；
- defect 在相容精化下单调恢复；
- root/collapse 精度动力学成为一般齐次映射定理的实例。

这一组合的历史创新状态仍为 `NOVELTY_UNVERIFIED`。

## 14. 第二阶段状态

- P018-T13 degree-q precision fiber：`PROVED`
- P018-T14 graded transport laws：`PROVED`
- P018-T15 degree-q transported shell + homogeneous bulk annihilation：`PROVED`
- P018-T16 monomial precision-defect bound：`PROVED`
- P018-T17 multiplication precision carry：`PROVED`
- P018-T18 power precision carry：`PROVED`
- P018-T19 monomial recovery monotonicity：`PROVED`
- P018-T20 collapse defect = root power carry：`PROVED`
- 任意齐次多项式 defect calculus：`OPEN`
- 一般 operation/predicate naturality formalism：`OPEN`
- P017 的严格 precision reinterpretation：`OPEN`

可执行检查位于 `src/enterprise_math/graded_precision.py` 与 `tests/test_graded_precision.py`。
