# P023 / A2 —— 整数 Repair Metric 的 Completion 边界，v3 补充

状态：`PROVED OWNER RESEARCH / FOUNDATION-BACKFLOW CANDIDATE`  
归属：A2 future-compatible quotient  
桥接：P005 projective precision / Foundation

## 1. 整数 repair geometry 是 uniformly discrete

固定整数 alphabet base `B>=2`，A2 的对称 repair metric 为

\[
D_B(E,F)=L_B(\rho(E,F))+L_B(\rho(F,E)).
\]

只要两个 precision relations `E,F` 不同，

\[
\boxed{D_B(E,F)\ge1.}
\]

所以正 repair distance 不可能向 0 累积。

## 2. 一般定理 —— 整数值 metric 自动完备

令 `(M,d)` 为 metric space，且 `d:M x M -> N_0`。任何 Cauchy sequence 都最终常值。

### 证明

取 `epsilon=1/2`。若 `(x_n)` 为 Cauchy sequence，则存在 `N`，使 `m,n>=N` 时 `d(x_m,x_n)<1/2`。但 `d` 是非负整数，所以只能有 `d(x_m,x_n)=0`，从而 `x_m=x_n`。因此序列最终常值并收敛。∎

所以任何有限值 A2 repair-metric space 本身已经 Cauchy complete。

## 3. 不会自动产生非平凡无限精度极限点

两两不同的 A2 precision states 不可能形成 Cauchy sequence。特别地，一条 strict refinement chain 不会因为不断保留更多有限 coordinates 就自动收敛。

因此

\[
\boxed{\text{整数 repair geometry 自身不会生成无限精度 limit point}.}
\]

## 4. Projective completion 是另一种构造

对 countable primitive binary task family，有限 coordinate states 可以写成有限子集 `S subset N`。按单位 binary repair cost，

\[
\boxed{D(S,T)=|S\triangle T|.}
\]

这是整数值 metric，所以 finite-support state space 已经完备。

但同一套 finite coordinates 的 projective/product completion 是 `{0,1}^N`，其中包含 infinite-support profiles。因此

\[
\boxed{\text{projective completion}\ne\text{A2 repair-metric completion}.}
\]

只有 finite shadow compatibility 并不能自动选定哪一种 completion。

## 5. 怎样额外制造非平凡 metric completion

再引入正 coordinate weights `w_i`，并要求 `sum_i w_i<infinity`，定义

\[
d_w(S,T)=\sum_{i\in S\triangle T}w_i.
\]

这时 finite-support profiles 在完整 Boolean product 中稠密，因为任意无限 profile 都可以由 finite truncations 逼近，tail weight 趋于 0。例如 `w_i=2^{-i}` 会让越来越后的 precision coordinates 变得任意便宜。

所以非平凡 metric infinite completion 需要额外结构提供任意小的正距离。

## 6. Precision quantum 判据

更一般地，若 metric 满足

\[
x\ne y\Longrightarrow d(x,y)\ge\delta>0,
\]

则空间 uniformly discrete，任何 Cauchy sequence 最终常值。因此要出现非平凡 Cauchy completion，一个必要条件是

\[
\boxed{0\text{ 必须成为正距离的累积点}.}
\]

用 precision 语言说：无限 metric refinement limit 要求越来越后的严格 refinement 在所选 metric 中变得任意便宜。这是一条额外几何假设，不是 finite quotient data 自动推出的事实。

## 7. Foundation 边界

本定理不禁止 inverse limit、product completion 或其他形式 completion。它只说明这些对象不能与 intrinsic integer repair metric 的 Cauchy completion 混为一谈。

未来 Foundation 若吸收这一结果，必须区分 precision shadows 的 finite/projective compatibility、formal infinite compatible profiles 是否存在、这些 profiles 是否由 actual states 实现、以及在声明 precision geometry 下是否 metric convergent。没有显式定理，任何一层都不能自动推出下一层。

## 8. P017 特化

若某条数论 program 实现所有 finite binary task patterns，但每个 actual state 只有有限 support，那么 actual profiles 可以在 product completion 中稠密，同时在单位 repair/Hamming distance 下仍然离散且完备。

这给上述 distinction 一个具体 program pressure test，而不把 formal completion 升格成物理本体。
