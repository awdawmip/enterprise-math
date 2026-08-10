# P025 补充 85 —— Sign-Specific 指数 Hasse 图与 Cover-Edge 充分性

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-cyclotomic-stage76`  
依赖：P025 补充 84  
硬阻断：`NONE`

## 1. Cocycle 改变了应该存什么

Stage 84 已证明，沿任意 admissible same-sign divisor chain，

\[
\Lambda_{m\to r}=\Lambda_{m\to n}\Lambda_{n\to r}.
\]

所以 long-range transition `m->n` 不是独立信息。下一压缩问题变成：

> 保留哪些 exponent transitions，就足以重建所有其他 transitions？

自然答案是 Hasse diagram：只保留 prime-ratio cover edges。

## 2. 研究域

本路线研究 equal prime-power complements，指数满足

\[
\boxed{n\ge2.}
\]

指数一刻意放在这个 transport graph 外。这样 primitive nodes 有清楚含义：它们的 pressure 不能从研究域里另一个更低的 equal-exponent shell 继承而来。

## 3. P025-D30 —— difference transport graph

对 difference sign，定义

\[
m\preceq_- n\iff m\mid n.
\]

Hasse covers 恰为

\[
\boxed{m\prec_- mp}
\]

其中 `p` 为素数。

每个 composite exponent 都有 incoming cover：除掉任一素因子即可；每个 prime exponent 都没有至少为 2 的 proper divisor。

因此

\[
\boxed{
\text{difference transport graph 的 primitive roots}
=
\text{prime exponents}.
}
\]

这给 Stage 79 的 prime-exponent theorem 一个结构解释：它就是 primitive difference case。

## 4. P025-D31 —— sum transport graph

对 sum sign，same-sign divisibility 要求 quotient 为奇数。定义

\[
\boxed{
m\preceq_+ n
\iff
m\mid n
\text{ 且 }n/m\text{ 为奇数}.
}
\]

因此 Hasse cover 为

\[
\boxed{m\prec_+ mp}
\]

其中 `p` 为**奇素数**。

乘以 2 不是 same-sign sum edge。

## 5. P025-T177 —— sum components 由 `v_2(n)` 编号

`n/m` 为奇数等价于

\[
v_2(m)=v_2(n).
\]

所以 sum transport graph 按 exponent 的 exact two-adic valuation 分解成互不连通 components。

若某 component 满足

\[
v_2(n)=a\ge1,
\]

其中每个 exponent 都可写为

\[
2^a u,
\qquad u\text{ odd}.
\]

该 component 的唯一 minimal exponent 是

\[
\boxed{2^a.}
\]

对 odd component `a=0`，exponent one 不在研究域，所以剩下的 minimal nodes 恰为 odd primes。

因此

\[
\boxed{
\text{sum transport graph 的 primitive roots}
=
\{\text{odd primes}\}
\cup
\{2^a:a\ge1\}.
}
\]

这是精确的 sign-specific primitive classification。

## 6. Stage 79 与 Stage 82 现在属于同一张图

### Odd prime exponent

对任一 sign，odd prime exponent 在 `n>=2` research graph 中都没有 incoming same-sign edge，因此其 pressure 相对于这个 transport system 是 primitive 的。

这正是 Stage 79 的设置。

### Fourth-power difference

指数四有 difference cover

\[
2\prec_-4.
\]

Stage 84 已证明 `(23,41)` hard state 是沿此 edge 的 resonant lift。

所以 fourth-power difference 不是 primitive。

### Fourth-power sum

对 sum sign，quotient `4/2=2` 为偶数，因此不是 admissible same-sign edge。指数四是其 sum component 的 root `2^2`。

所以

\[
\boxed{4\text{ 对 difference 非 primitive，但对 sum primitive}.}
\]

这解释了 Stage 82 的 sign contrast，而不需要把“parity”当成模糊 heuristic。

### Ninth powers

指数九对两个 sign 都有 cover

\[
3\prec_\pm9.
\]

Stage 83 的 ninth-power counterexamples 因而都是从 cube states lift 上来的 nonprimitive states。

## 7. P025-T178 —— Hasse-cover sufficiency

设

\[
m\mid n
\]

是 `n>=2` graph 中的 admissible same-sign transition。

将

\[
\frac nm=p_1p_2\cdots p_s
\]

分解成素数；sum route 上所有 `p_i` 必为奇数。

定义 cover chain

\[
e_0=m,
\qquad e_i=e_{i-1}p_i,
\qquad e_s=n.
\]

反复应用 Stage 84 得到

\[
\boxed{
\Lambda_{m\to n}
=
\prod_{i=1}^s\Lambda_{e_{i-1}\to e_i}.
}
\]

所以所有 long-range inheritance multipliers 都由 prime-ratio cover edges 生成。

任何 non-cover transition 都不需要作为独立 transport data 存储。

这是 **Hasse-cover sufficiency**。它只是充分性结论，并不声称不存在另一种 coordinate system 能进一步压缩。

## 8. P025-T179 —— local diamond flatness

设 `r,s` 为两个不同的 admissible cover primes，则存在两条路径

\[
m\to mr\to mrs
\]

与

\[
m\to ms\to mrs.
\]

Hasse-cover sufficiency 与 exact cocycle 给出

\[
\boxed{
\Lambda_{m\to mr}\Lambda_{mr\to mrs}
=
\Lambda_{m\to ms}\Lambda_{ms\to mrs}.
}
\]

所以每个 commuting-prime diamond 都是 flat 的。

这条局部关系就是 global path independence 背后的 finite consistency law。

若定义 logarithmic pressure increment

\[
\lambda_{a\to b}:=\log\Lambda_{a\to b},
\]

则同一关系变成

\[
\boxed{
\lambda_{m\to mr}+\lambda_{mr\to mrs}
=
\lambda_{m\to ms}+\lambda_{ms\to mrs}.
}
\]

## 9. 现在什么才是真正 primitive

Stage 84 曾提出“primitive node pressure”。Hasse 分析把它进一步压清楚。

node pressure 本身是一个 potential；真正不可约的 local transport information 位于 cover edges。

因此研究分类应改成：

1. **primitive root states** —— 没有 incoming same-sign cover 的 nodes；
2. **cover-edge innovation** —— exponent 新增一个 prime factor 时产生的 attenuation/resonance/amplification；
3. **derived long-range transport** —— cover-edge multipliers 的乘积。

第三类不再是新信息，不应被独立计数或重复存储。

## 10. Precision 解释

exponent coordinate 现在是 finite transport geometry，而不再是 flat scalar axis。

若 future query 需要许多 composite exponents 上的 pressure，不需要保存所有 pairwise exponent transitions，只需：

\[
\boxed{
\text{root pressure states}
+
\text{prime-ratio cover multipliers}
+
\text{diamond consistency}.
}
\]

这把 dense transition table 压成 sparse Hasse graph。

sum graph 还给出更强的 operation-language lesson：删掉 even-ratio edges 后，连哪些 nodes 是 primitive 都会改变。

## 11. Prior-art / novelty 边界

整除偏序、Hasse diagram、素因子分解与 cocycle/path-independence language 都是标准数学。

P025 不单独主张这些结构的新颖性。

项目侧候选是：把它们精确识别为 projective-pressure inheritance law 所生成的最小-looking transport surface，并得到 sign-specific primitive-root classification。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 12. 可执行资产

新增：

- `src/enterprise_math/abc_exponent_transport_hasse.py`；
- `tests/test_abc_exponent_transport_hasse.py`。

executable layer 验证：

- difference primitive roots 恰为 primes；
- sum primitive roots 为 odd primes 加 powers of two；
- exponent four 的 primitive status 随 sign 改变；
- Hasse covers 只含 prime-ratio predecessors；
- cover products 等于 direct long-range transport；
- commuting-prime diamonds 给出 path-independent multipliers。

## 13. 下一前沿

不存在硬阻断。继续：

1. 加入 cross-sign edges：偶 quotient 会把 sum component 送进 difference component；
2. 判断两个 sign-specific Hasse graphs 是否只是一个 signed exponent transport graph 的 shadows；
3. 在允许 cross-sign transport 后重新分类 primitive roots；
4. 判断 cover-edge multipliers 是否有只依赖 newly introduced index layers 的 local cyclotomic formulas；
5. 然后才把 Hasse/cocycle transport structure Relay 给 A2/P023。
