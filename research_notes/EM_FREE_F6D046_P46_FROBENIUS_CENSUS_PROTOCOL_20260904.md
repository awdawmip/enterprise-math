# mixed Prym P46 的完整局部 Frobenius 普查协议与证据边界

Status: `FREE_RESEARCH / COMPUTATIONAL_ARITHMETIC_EVIDENCE / FULL_DEGREE8_LOCAL_POLYNOMIALS / NO_ABSOLUTE_SIMPLICITY_CLAIM`
Date: `2026-09-04`
Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`
Parent candidate: `EM-FREE-F6D046-C1-ROTATIONAL-PERIOD-WRONSKIAN`
Research unit: `EM-FREE-F6D046-R13-P46-FROBENIUS-CENSUS`

## 0. 目标

R12 证明 symmetry/character/Hodge data 单独不足以决定 mixed Prym `P46` 的 isogeny decomposition。本轮进入所需的新算术层。

采用

\[
E:\quad v^2=A(t),
\]

\[
C_{46}:\quad m^2=-\frac{vD(t)}{288},
\]

其中

\[
A(t)=t^4+24t^3+192t^2+528t+144,
\qquad
D(t)=t^2+12t+24.
\]

`P46=Prym(C46/E)` 维数为4。

## 1. 计算对象

对好素数

\[
p\in\{5,7,11,13\}
\]

及

\[
n=1,2,3,4,
\]

直接在 `F_{p^n}` 中计算 smooth projective point counts

\[
N_n(E),\qquad N_n(C_{46}).
\]

Prym Frobenius power sums 为

\[
\boxed{
s_n(P_{46})
=(p^n+1-N_n(C_{46}))-(p^n+1-N_n(E))
=N_n(E)-N_n(C_{46}).
}
\]

由前四个 power sums 使用 Newton identities 恢复

\[
P_{46,p}(T)=\prod_{i=1}^{8}(1-\alpha_iT)
\]

的前半系数，再用 weight-one functional equation 完成：

\[
P_{46,p}(T)=
1+c_1T+c_2T^2+c_3T^3+c_4T^4
+pc_3T^5+p^2c_2T^6+p^3c_1T^7+p^4T^8.
\]

每个多项式随后在 `Z[T]` 上精确分解。

## 2. 计数细节

`E` 的 quartic 模型在每个有限 `t` 上按 `v^2=A(t)` 枚举，并加入两个无穷远点。

对 `C46->E`，有限点 fiber 按

\[
1+\chi\!\left(-vD/288\right)
\]

计数；在 `E` 的两个无穷远点，函数 `-vD/288` 的 pole order 为4，故 cover 不分歧，rational fiber 数由其 leading residue 的 quadratic character 决定。实现显式加入

\[
2+\chi(c)+\chi(-c),\qquad c=-1/288.
\]

有限域由不可约多项式商直接构造；不依赖浮点数或随机采样。

## 3. 已完成资产

可执行 verifier 输出：

- 所用不可约多项式；
- 每个 `(p,n)` 的 `N_E,N_C46,s_n(P46)`；
- 每个 `p` 的 degree-8 系数；
- functional-equation checks；
- `Z[T]` factorization。

本轮本地运行覆盖四个素数、十六个扩域点数与四个完整局部多项式。

## 4. 证据边界

完整 local polynomials 明显强于只看第一 Frobenius trace，可用于：

- 排除与某一好素数多项式不相容的候选稳定分解；
- 搜索跨素数反复出现的 degree-2/4 factors；
- 为 Tate-module endomorphism 与 explicit-correspondence 搜索提供目标。

但四个素数的 factorization pattern 本身不自动构成“P46 绝对简单”或“P46 已分裂”的证明。几何结论仍需：

1. 可认证的共同 endomorphism/correspondence；或
2. 满足相应绝对简单性判据的 Frobenius prime 与证明；或
3. 更多素数及排除 exceptional specialization 的论证。

因此本轮分类是

`COMPUTATIONAL_EVIDENCE / FULL_LOCAL_POLYNOMIALS / NO_ABSOLUTE_SIMPLICITY_CLAIM / NOT_NEW_AXIOM / NOT_FOUNDATION`。
