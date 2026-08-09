# P025 补充 11 —— Two-Variable Certificates 的 Sharp Integrality-Access Defect

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner：`program/p025-abc-support-collapse`  
依赖：P025 补充 10  
Hard block：`NONE`

## 1. 从 abc 特化中抽出的 generic problem

补充 10 把一个结构化 floor-access problem 化成

\[
A u+B v=N,
\qquad
A,B,N\in\mathbb N_{>0}.
\]

假设该方程存在整数解。定义

\[
\nu(A,B;N)
=
\min_{Au+Bv=N}
\max(|u|,|v|)
\]

以及 continuous triangle lower bound

\[
\boxed{
L(A,B;N)
=
\left\lceil\frac{N}{A+B}\right\rceil.
}
\]

定义**integrality-access defect**

\[
\boxed{
\Gamma(A,B;N)=\nu(A,B;N)-L(A,B;N)\ge0.
}
\]

本补充给出 `Gamma=0` 的 exact modular criterion，以及一个只依赖系数的 sharp universal upper bound。

## 2. P025-T31 —— `Gamma=0` 的 exact modular criterion

令

\[
g=\gcd(A,B),
\qquad
A'=A/g,
\quad
B'=B/g,
\quad
N'=N/g.
\]

则 `gcd(A',B')=1`。记

\[
L=\left\lceil\frac{N'}{A'+B'}\right\rceil.
\]

若存在解满足

\[
|u|,|v|\le L,
\]

首先必须有

\[
-L\le u\le L.
\]

而由 `|v|<=L` 又有

\[
N'-B'L
\le A'u\le
N'+B'L.
\]

所以 `u` 的允许整数区间精确是

\[
\boxed{
I_L
=
\left[
\max\left(-L,
\left\lceil\frac{N'-B'L}{A'}\right\rceil\right),
\min\left(L,
\left\lfloor\frac{N'+B'L}{A'}\right\rfloor\right)
\right]\cap\mathbb Z.
}
\]

同时原方程要求

\[
\boxed{
A'u\equiv N'\pmod{B'}.
}
\]

因此

\[
\boxed{
\Gamma=0
\iff
I_L\text{ 中包含模 }B'\text{ 的所需 residue class。}
}
\]

这是只用一个 modular inverse 和一个有界整数区间的 exact finite test。

## 3. P025-T32 —— Sharp universal defect bound

定义 reduced maximum coefficient

\[
\boxed{
M=\max(A',B').
}
\]

则

\[
\boxed{
0\le\Gamma(A,B;N)
\le
\left\lfloor\frac{M-1}{2}\right\rfloor.
}
\]

而且这个 coefficient-only upper bound 在全部 positive solvable two-variable integer equations 组成的类上是 sharp 的。

### Upper bound 证明

reduced equation 为

\[
A'u+B'v=N'.
\]

在实数上，minimum `L_infinity` norm 在 balanced point

\[
(u,v)=(t,t),
\qquad
 t=\frac{N'}{A'+B'}
\]

处达到。因为任何满足 `max(|u|,|v|)<=B` 的实数 pair 都有

\[
N'\le(A'+B')B,
\]

而 `B=t` 时由 `(t,t)` 取等。

全部整数解位于 primitive direction

\[
(B',-A')
\]

上的一条 affine parameter lattice。令 `k_*` 为 balanced point 对应的实参数，选择整数 `k` 满足

\[
|k-k_*|\le1/2.
\]

所得整数解相对于 `(t,t)` 的第一坐标偏移不超过

\[
B'/2,
\]

第二坐标偏移不超过

\[
A'/2.
\]

所以

\[
\nu\le t+M/2.
\]

又因为 `nu` 是整数：

- 若 `t` 本身为整数，则 `(t,t)` 已是整数解，故 `Gamma=0`；
- 若 `t` 非整数，则
  \[
  \nu\le\lfloor t+M/2\rfloor.
  \]

把 `M` 写成 `2h` 或 `2h+1`，对 fractional part 直接分类得到

\[
\lfloor t+M/2\rfloor-\lceil t\rceil
\le
\begin{cases}
h-1,&M=2h,\\
h,&M=2h+1,
\end{cases}
\]

正好等于

\[
\left\lfloor\frac{M-1}{2}\right\rfloor.
\]

因此结论成立。∎

## 4. P025-T33 —— Sharpness families

对每个 reduced maximum coefficient `M>=2`，P025-T32 的 bound 都可以达到。

### 偶数 `M=2h`

取

\[
A=M,
\qquad
B=1,
\qquad
N=h.
\]

则

\[
L=1.
\]

由 congruence

\[
v\equiv h\pmod{2h}
\]

必有 `|v|>=h`，而 `(u,v)=(0,h)` 是一个解。所以

\[
\nu=h
\]

并且

\[
\boxed{
\Gamma=h-1
=
\left\lfloor\frac{M-1}{2}\right\rfloor.
}
\]

### 奇数 `M=2h+1`

取

\[
A=2h,
\qquad
B=2h+1,
\qquad
N=3h+1.
\]

同样有

\[
L=1.
\]

模 `2h` 有

\[
v\equiv h+1\pmod{2h}.
\]

两个最近 residue representatives 分别会强制 `|v|=h+1` 或 `|u|=h+1`；显式解

\[
(u,v)=(-h,h+1)
\]

给出

\[
\nu=h+1.
\]

所以

\[
\boxed{
\Gamma=h
=
\left\lfloor\frac{M-1}{2}\right\rfloor.
}
\]

因此，在只允许使用 reduced maximum coefficient 的情况下，不可能存在更小的 universal bound。

## 5. 对 `1+qr=p^m` 的后果

补充 10 中

\[
A=r,
\qquad
B=q,
\qquad
N=m p^{m-1},
\]

而 `q,r` 是互素素数，所以

\[
M=\max(q,r).
\]

因此 family 的 exact defect

\[
\Gamma_{\rm int}
=\nu-
\left\lceil\frac{m p^{m-1}}{q+r}\right\rceil
\]

满足

\[
\boxed{
0\le\Gamma_{\rm int}
\le
\left\lfloor
\frac{\max(q,r)-1}{2}
\right\rfloor.
}
\]

这里不主张 P025-T33 的 generic sharpness families 本身也满足 prime-power relation；该公式只是对每个真正落在 P025 family 中的 triple 给出严格 universal upper bound。

## 6. 例子

### `1+15=16`

modular interval 在 triangle lower bound 就包含所需 residue，因此

\[
\Gamma_{\rm int}=0.
\]

### `1+511=512`

这里

\[
q=7,
\qquad
r=73,
\qquad
L=29,
\qquad
\nu=33,
\]

所以

\[
\Gamma_{\rm int}=4.
\]

只依赖系数的 universal bound 是

\[
\left\lfloor\frac{73-1}{2}\right\rfloor=36.
\]

因此实际 defect 远小于 generic coefficient size 所允许的 worst case。

这也说明，若利用特殊 prime-power 结构，仍有空间得到比 generic Diophantine geometry 更强的 bound。

## 7. 架构含义

这个新 defect 可以精确解释成：

\[
\boxed{
\text{continuous resource bound}
+
\text{finite integrality correction}
=
\text{exact certificate access precision}.
}
\]

这个 correction 不是任意误差。在 two-variable setting 下，它永远被一个有限 coefficient-scale term 控制，而且恰好在一个 residue class 穿过一个显式 interval 时消失。

这给进取数论提供了一个很具体的离散处理范式：

> 不要把 discrete problem 用 continuous estimate 替代以后，把剩余 gap 叫作“噪声”；应当把 continuous bound 之后剩下的有限 arithmetic obstruction 精确抽出来。

## 8. Prior-art discipline

本定理只使用初等/标准工具：

- linear Diophantine equations 的 affine parameterization；
- nearest-integer rounding；
- modular inverses；
- floor/ceiling arithmetic。

P025 不主张这个 generic optimization inequality 的历史优先权。它在这里的作用，是作为 certificate-access precision 的 exact calibration theorem。

## 9. 可执行资产

`src/enterprise_math/abc_absorption_two_variable.py` 现在还包含：

- exact modular sharpness criterion；
- exact integrality defect；
- universal bound `floor((M-1)/2)`；
- 对每个 `M>=2` 的显式 sharpness examples。

测试穷举全部 positive `A,B<16`、`N<40` 验证该 bound，并覆盖奇偶两种 sharpness family。

## 10. 下一前沿

不存在 hard block，继续：

1. 利用实际 relation `1+qr=p^m` 改进 generic coefficient bound；
2. 研究 prime-power congruence 是否强制 unusually small 或 large modular access defects；
3. 寻找 structured families 中 constructive-versus-optimal witness ratio 的 exact asymptotics；
4. 在 higher-dimensional witness slices 中测试同一个 continuous-bound-plus-integrality-defect decomposition；
5. 始终把 generic Diophantine optimization 与任何最终 abc-specific claim 分开。
