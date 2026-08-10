# P025 补充 75 —— `(3,3)` Prime-Cube Shell 的 Centered Factorization

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-paired-square-tail-stage61`  
依赖：P025 补充 72–73  
Hard block：`NONE`

## 1. centered coordinate switch 对 cube shells 同样有效

设

\[
p>q
\]

为不同奇素数，并定义

\[
\boxed{
B=\frac{p+q}{2},
\qquad
A=\frac{p-q}{2}.
}
\]

仍有

\[
\gcd(A,B)=1,
\]

且 `A,B` 奇偶性相反。

对 cutoff-five `(3,3)` shell，自然有两种 active forms：

\[
p^3+q^3
\]

与

\[
p^3-q^3.
\]

二者都可以精确分解成一个 centered coordinate 与一个 odd quadratic form。

## 2. P025-T144 —— cube-sum projective formula

有

\[
\boxed{p^3+q^3=2B(B^2+3A^2).}
\]

定义

\[
E=B^2+3A^2.
\]

由于 `A,B` 奇偶相反，`E` 为奇数；并且

\[
\gcd(B,E)=\gcd(B,3A^2)=\boxed{\gcd(B,3)}=:g_B\in\{1,3\}.
\]

再定义

\[
\varepsilon_B=
\begin{cases}
2,&2\mid B,\\
1,&2\nmid B.
\end{cases}
\]

精确追踪可能共享的 prime `3`，以及 leading factor `2` 是否已经包含在 `B` 中，可得

\[
\boxed{m(p^3+q^3)=\varepsilon_Bg_Bm(B)m(E).}
\]

两个 prime-cube complements 的 cross-capacity 为

\[
3p+3q=6B.
\]

因此 c-oriented projective term 为

\[
\boxed{
\rho_{(3,3),+}
=
\frac{\varepsilon_Bg_Bm(E)}{6\operatorname{rad}(B)}.
}
\]

这把完整 cube sum 的 factorization 问题压成 center radical 与 quadratic form `E` 的 residual。

## 3. P025-C19 —— quadratic factor squarefree 时 cube-sum 必处于 subunit basin

若 `E` squarefree，则

\[
m(E)=1.
\]

同时

\[
\varepsilon_Bg_B\le6,
\]

而 `rad(B)>=2`，所以

\[
\rho_{(3,3),+}\le\frac6{12}<1.
\]

因此

\[
\boxed{
B^2+3A^2\text{ squarefree}
\Longrightarrow
\rho_{(3,3),+}<1.
}
\]

所以 cube-sum activation 必须在 centered quadratic factor 中出现 repeated-prime structure。

## 4. P025-T145 —— cube-difference projective formula

同理，

\[
\boxed{p^3-q^3=2A(3B^2+A^2).}
\]

定义

\[
D=3B^2+A^2.
\]

`D` 仍为奇数，且

\[
\gcd(A,D)=\gcd(A,3B^2)=\boxed{\gcd(A,3)}=:g_A\in\{1,3\}.
\]

定义

\[
\varepsilon_A=
\begin{cases}
2,&2\mid A,\\
1,&2\nmid A.
\end{cases}
\]

则

\[
\boxed{m(p^3-q^3)=\varepsilon_Ag_Am(A)m(D).}
\]

prime-cube complement cross-capacity 仍为 `6B`，因此 active side term 为

\[
\boxed{
\rho_{(3,3),-}
=
\frac{\varepsilon_Ag_Am(A)m(D)}{6B}.
}
\]

## 5. P025-C20 —— double squarefreeness 认证 cube-difference subunit basin

若

\[
A
\quad\text{与}\quad
D=3B^2+A^2
\]

都 squarefree，则

\[
m(A)=m(D)=1.
\]

又因为

\[
\varepsilon_Ag_A\le6
\]

且 `B>1`，所以

\[
\rho_{(3,3),-}<1.
\]

故

\[
\boxed{
A,\ 3B^2+A^2\text{ 都 squarefree}
\Longrightarrow
\rho_{(3,3),-}<1.
}
\]

这就是 Stage 74 centered squarefree guard 的 cube-difference 对应版本。

## 6. 精确样本

### Activated cube sum

取

\[
(q,p)=(5,59),
\qquad(B,A)=(32,27).
\]

则

\[
E=32^2+3\cdot27^2=3211=13^2\cdot19.
\]

并且

\[
\varepsilon_B=2,
\quad g_B=1,
\quad m(E)=13,
\quad\operatorname{rad}(B)=2.
\]

所以

\[
\boxed{\rho_{(3,3),+}=13/6>1.}
\]

### Safe cube sum

对

\[
(q,p)=(3,5),
\qquad(B,A)=(4,1),
\]

有

\[
E=19
\]

squarefree，并且

\[
\rho_{(3,3),+}=1/6.
\]

### Activated cube difference

取

\[
(q,p)=(5,101),
\qquad(B,A)=(53,48).
\]

闭式给

\[
\boxed{\rho_{(3,3),-}=56/53>1.}
\]

### Safe cube difference

对

\[
(q,p)=(3,7),
\qquad(B,A)=(5,2),
\]

有

\[
D=79,
\]

且 `A=2`,`D=79` 都 squarefree，因此

\[
\rho_{(3,3),-}=1/15.
\]

## 7. 为什么 coordinate switch 真正有用

Stage 72 已证明 exact exponent data 无法决定 surviving low-capacity shells 内的 activation。Stage 75 把完整 prime-base binomial factorization 换成更小的 centered observables：

### Cube sum

\[
(p,q)
\to
(B,A)
\to
\bigl(\operatorname{rad}(B),\ m(B^2+3A^2)\bigr).
\]

### Cube difference

\[
(p,q)
\to
(B,A)
\to
\bigl(B,\ m(A),\ m(3B^2+A^2)\bigr).
\]

因此下一种有用 precision 不再是“更多 exponent detail”，而是 classical quadratic form 的 multiplicity structure。

## 8. 经典代数边界

Sum/difference-of-cubes factorization 与上述 quadratic forms 都是经典数学；它们与 Eisenstein/cyclotomic arithmetic 的关系属于 established number theory，应当选择性导入而不是由 P025 声称。

P025 只保留 exact projective-value reductions 及其 task-relative safe guards，历史 novelty 仍为 `NOVELTY_UNVERIFIED`。

## 9. 可执行资产

新增：

- `src/enterprise_math/abc_prime_cube_centered.py`；
- `tests/test_abc_prime_cube_centered.py`。

模块将两个 closed formulas 与独立计算的 exact projective cyclic values 做交叉核验。

## 10. 下一前沿

Hard block 不存在。继续：

1. 选择性导入 classical primitive-divisor/cyclotomic results，尝试下界 `B^2+3A^2` 与 `3B^2+A^2` 的 radicals；
2. 在引入新 quadratic-form terminology 前先检查 P018/P005 是否已有合适 coordinate home；
3. 只有 quartic shell 能产生真正更小 theorem-native state 时才继续 coordinate-switch audit；
4. 冻结 exponent-only refinement，后续文献搜索集中到新的 quadratic-form coordinates。
