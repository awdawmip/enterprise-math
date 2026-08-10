# Reachable Coefficient Image 与 Carrier-Minimal Semiring Precision

状态：`RESEARCH BRIDGE / NONCANONICAL`

一个 coefficient semiring 可能包含很多 declared unweighted relation world 永远无法生成的 elements。

这些 unreachable carrier states 构成一种独立于 state partition 与 successor-correlation 的 representation overprecision。

对 unweighted relations，exact reachable coefficient algebra 有一个 canonical answer：semiring unit 的 natural image。

## 1. Unweighted relations 只生成 natural image

设 K 为 coefficient semiring。

每条 raw relation edge 只贡献 `1_K`。

所以任意 local target-block weight 都是：

`n * 1_K`

其中 n 为 natural successor count。

定义：

`K_nat = { n*1_K : n in N }`。

这正是 canonical semiring homomorphism

`eta_K:N->K`

的 image。

## 2. K_nat 是 subsemiring

对 natural m,n：

`eta(m)+eta(n)=eta(m+n)`，

`eta(m)*eta(n)=eta(mn)`。

并且：

`eta(0)=0_K`，

`eta(1)=1_K`。

因此 `K_nat` 对 zero、one、addition、multiplication 全部闭合。

更强地，它是 K 中包含 `1_K` 的唯一最小 subsemiring：任何包含 one 的 subsemiring 都必须包含所有 repeated sums `n*1_K`。

所以 K_nat 不是 heuristic compression，而是 unweighted world law 的 canonical reachable coefficient algebra。

## 3. Branching 永远不会离开 K_nat

每个 local branching coefficient 都是 raw successor count 经 eta 的 image，所以从第一步就落在 K_nat。

Recursive branching refinement 以后也不会产生别的 coefficient：每一轮仍然只是“某个 current behavioural type 有多少 raw successors”，然后再次应用 eta。

因此把 K 替换成 K_nat，不会改变任何 unweighted branching signature 或 state kernel。

## 4. Terminal trace fold 也不会离开 K_nat

Terminal traces 只对 local coefficients 做加法与乘法。

由于 K_nat 是 subsemiring，所有 path-count coefficients 仍留在 K_nat。

所以相同替换也保留：

- 每个 literal word trace；
- 每个 observed trace partition；
- 所有只在 reachable image 上实际作用的 coefficient morphism semantics。

Executable branch 会对 Boolean×modular family 直接验证这一点。

## 5. Product semiring 可能有 coefficient-carrier overprecision

Categorical product K×L 包含所有 pairs `(k,l)`。

但 unweighted raw relation 进入 product 时，只会沿 diagonal natural code：

`n -> (eta_K(n),eta_L(n))`。

所以 operational coefficient carrier 是这个 natural map 的 image，而不是完整 Cartesian product。

这是第一种、纯代数的 product overprecision：

> natural image 之外的 coefficient pairs 在任何 state / branch semantics 之前就已经永远 unreachable。

对 declared unweighted world 来说，它们可以无条件删除。

## 6. Modular products 压成 compatible CRT image

取：

`K=Z/MZ x Z/NZ`。

Natural image 是：

`{(n mod M,n mod N):n in N}`。

它的大小为：

`lcm(M,N)`。

这个 image 就是 compatible-residue subring，并与

`Z/lcm(M,N)Z`

同构。

所以 full product carrier size

`M*N`

可以压成

`lcm(M,N)`。

若 M,N coprime，则 `lcm=MN`，CRT product 恰好没有 coefficient-carrier redundancy。

若它们共享 factor，categorical product 中就存在 unreachable incompatible residue pairs。

这给此前 modular lcm theorem 一个 coefficient-carrier 解释。

## 7. Boolean × modular product 压成 M+1 states

考虑：

`B x Z/MZ`。

Full product carrier 有：

`2M`

个 elements。

Natural image 只有：

- exact zero：`(0,0)`；
- positive residue classes：对每个 `r in Z/MZ` 有 `(1,r)`。

所以 reachable carrier size 为：

`M+1`。

Unreachable elements 恰好是：

`(0,r)`，其中 `r!=0`，

一共 `M-1` 个。

任何 positive / raw natural count 都不可能生成这些 states。

## 8. Zero-aware modular semiring

Boolean×mod-M 的 reachable image 可以直接表示成一个 semiring：

- 一个 true zero Z；
- M 个 positive residue classes `P_r`。

运算：

`Z+x=x`，

`P_r+P_s=P_(r+s mod M)`，

`Z*x=Z`，

`P_r*P_s=P_(rs mod M)`。

最重要的是：`P_0` **不是** true zero；它表示“positive count 但 divisible by M”。

这正是 Boolean support 把 pure modular local-count capacity 从 M-1 提升到 M 的代数原因：它区分了

`0`

与

`positive multiple of M`。

Executable `zero_aware_modular_semiring` 使用 canonical pair representation：

`(0,0)` 或 `(1,r)`。

## 9. Full product 与 zero-aware semiring 的 unweighted branching semantics 完全相同

所有 raw local coefficients 都位于 natural image。

Zero-aware operations 与 full Boolean×mod-M operations 在这个 image 上精确相同。

因此每个 branching horizon 都有：

`zero-aware branching partition`

等于

`full Boolean x mod-M product branching partition`。

Owner regression 会在 multiple moduli 下，对全部 two-state relation pairs 做 exhaustive check。

## 10. Terminal traces 同样完全一致

因为两套 semiring 在 reachable subsemiring 上相同，而且 trace folds 永远不会离开该 subsemiring，所以任意 literal terminal trace 在：

- full Boolean×mod-M product；
- zero-aware M+1-state semiring

下完全相同。

这也会对多个 words / moduli 做 executable regression。

所以这个 carrier compression 同时保留 structural 与 trace semantics；它不同于 task-dependent 的 branch-correlation removal。

## 11. 两种不同的 product overprecision

近期 branching generations 已经暴露两种彼此独立的机制。

### Coefficient-carrier overprecision

Ambient product semiring 包含 primitive world weights 永远无法到达的 coefficient elements。

Repair：

`把 ambient K 替换成 natural-image subsemiring K_nat`。

对使用该 coefficient algebra 的全部 unweighted branching / trace tasks 都安全。

### Structural correlation overprecision

即使 coefficient elements 本身 reachable，product child type 仍可能保留：哪个 K-behaviour 与哪个 L-behaviour 属于同一个 successor。

对 independent readout task，这种 pairing 可能无用。

对 shared compositional operation task，它又可能必须保留。

Repair 依赖 declared continuation semantics，不能只靠 coefficient reachability 判断。

这两种 overprecision 必须严格区分。

## 12. Carrier minimization 不降低 capacity

Zero-aware M+1-state semiring 与 full Boolean×mod-M product 拥有完全相同的 natural count code：

`0 -> Z`，

`n>0 -> P_(n mod M)`。

所以两者的 local exact-count capacity 都是 M。

因此删除 unreachable carrier states 不会损失 Boolean + modular capability join 已经获得的 reflection synergy。

一般地，natural-image subsemiring 会保留 ambient semiring 对 natural counts 做出的全部 distinctions。

## 13. Scope boundary：weighted raw relations

这个 theorem 假设 raw relation edges 只携带 unit coefficient。

如果 world law 声明了 `1_K` 之外的 primitive edge weights，那么这些 values 会扩大 reachable coefficient algebra。

正确 generalization 是：

`由 actual primitive coefficient set 生成的 subsemiring`，

而不只是由 one 生成的 subsemiring。

所以 coefficient carrier minimality 本身也是 world-law relative。

## 14. Compiler rule

对 unweighted relation coefficient interface：

1. 先选择 task 真正需要的 semantic coefficient capabilities；
2. 必要时先构造方便的 ambient semiring / product；
3. 立即 restrict 到 natural-image subsemiring；
4. 然后再运行 branching / compositional state refinement。

这样可以在支付任何 state-partition cost 之前，先清掉 algebraically unreachable state。

## 15. Prior-art boundary

Semiring homomorphism image、prime subsemiring、CRT compatible residue ring 与 subsemiring generation 都是标准既有代数。A4 保留 relation / witness ownership；P023/A2 保留 precision / interface ownership。

这里的项目价值是明确 minimization rule：

> **对 unweighted relation semantics，一个 ambient semiring 内唯一 least coefficient algebra 就是 natural image `eta_K(N)`；categorical product carriers 可以先压成这个 reachable subsemiring，再做任何 task-dependent state minimization。**