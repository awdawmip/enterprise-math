# Profinite Local-Global Precision

状态：`FOUNDATION-FACING RESEARCH BRIDGE / NONCANONICAL`

本文不新增 Foundation Question，而是把当前整数 IMAGE/FIBER 研究压缩成一套基于有限生成整数格 congruence/profinite topology 的统一 precision architecture。

## 1. Modular precision 是 congruence neighborhoods 的拓扑

在 `Z^n` 中，

`M Z^n`，`M=1,2,...`

形成0附近的标准 congruence neighborhood system。

把 exact integer data 降到 mod-M，本质上就是把一个 exact point 或 subgroup 换成该 neighborhood scale 下的 coset / thickening。

因此，提高 arithmetic precision 并不只是把某个标量数值调大，而是在 divisibility refinement 下不断缩小 congruence neighborhoods。

## 2. Closed 表示“无限 refinement 最终可识别”

设 `H<=Z^n` 为有限生成 subgroup。标准 subgroup separability 给出

`H = intersection_(M>=1) (H + M Z^n)`。

因此，每一个整数格 subgroup 在 profinite / congruence topology 中都是 closed。

Precision 解释是：

> 只要一个 exact state 不属于 H，就一定存在某个有限 modulus，最终能把它与 H 分开。

这就是整数 local-global principle 的拓扑形式。

但 closed 并不意味着存在一个预先固定的有限 modulus，可以 uniform 地分开所有不属于 H 的状态。

## 3. Open 表示“存在有限 uniform cutoff”

H 为 open，当且仅当它包含某个 congruence neighborhood：

`M Z^n subseteq H`

对某个有限 M 成立。

这等价于 H 在 ambient integer lattice 中具有 finite index。

Precision 解释是：

> 一个 exact membership property 存在一个统一有限 modular cutoff，当且仅当其定义 subgroup 是 open。

因此：

`closed -> 每一个单独的 false state 都存在某个有限 separating precision`，

而

`open -> 同一个有限 precision 对整个 unrestricted state family 都有效`。

## 4. IMAGE 可以非平凡地 clopen

对

`A:Z^n -> Z^m`，

令

`L=im_Z(A)`。

exact target reachability 就是 L 的 membership。

L 总是 closed；而 L 为 open 当且仅当

`rank_Q(A)=m`，

也就是 cokernel 没有 free part。

在 open 情形，令

`E=exp(coker(A))`

为最大 Smith factor。E 就是满足

`E Z^m subseteq L`

的唯一 least modulus。

所以：

- full row rank -> IMAGE 为 clopen，并存在一个 finite exact precision E；
- rank deficient -> IMAGE closed but not open：每个 bad target 各自都有有限 separator，但不存在一个 finite modulus 能统一决定所有 unrestricted targets。

这就是 affine local-global hierarchy 的拓扑含义。

## 5. Rational-image promise 会改变 ambient precision space

对 rank-deficient A，定义 saturation

`S = span_Q(L) intersect Z^m`。

若另有独立信息已经保证 target 属于 S，那么 free cokernel coordinate 已被排除。此时在更小的 ambient lattice S 中，L 具有 finite index。

因此 L 在 S 的 induced profinite topology 中变成 open，而同一个 finite torsion exponent E 又成为 least uniform exact certificate。

也就是说，一个先验结构约束可以通过**改变 admissible world**，把 closed/non-open 问题变成 open，而不是依靠盲目增大 modulus。

## 6. FIBER 的拓扑不同

对整数 observation

`O:Z^n -> Z^m`，

令

`K=ker_Z(O)`。

由于 codomain 无 torsion，K 是 saturated。于是

`Z^n/K ~= im(O)`

是 free abelian。

因此：

- K 总是 closed；
- K 为 open 当且仅当 `im(O)=0`，也就是 O 本身为 zero observation。

所以每一个 proper exact observation fiber 都是 closed but not open。

Precision 结论：

> 对任何非零整数 observation，都不存在一个固定 finite modular family，可以在全部无界整数 states 上 uniform 认证 exact state-output equality。

但只要某个 state difference 不属于 K，足够精细的 modular precision 最终一定能把它分开。

这是真正的 IMAGE/FIBER 不对称：nontrivial IMAGE subgroup 可以 clopen；而映向 free integer observations 的 proper kernel 不可能 open。

## 7. 独立 bound 可以 finite-ize closed/non-open 问题

closed-but-not-open 并不表示 finite precision 永远无法做出精确判定。它只表示：在一个无界 admissible family 上不存在 uniform cutoff。

一旦另有独立 height bound 限制 admissible lifts，有限 cutoff 会重新出现。

### IMAGE

设整数 left-null rows Q 张成 rational obstruction directions。若

`||Qb||_infinity <= B`，

那么任意满足

`D>B` 且 `E|D`

的 modulus，都能使 mod-D solvability 等价于这一 bounded target family 上的 exact reachability。

### FIBER

若

`|x_i|,|y_i|<=H`，

则

`|O_j(x-y)| <= 2H ||O_j||_1`。

只要 modulus 严格大于所有可能的 output difference，modular output equality 就与整个 bounded state box 上的 exact output equality 完全一致。

共同原则是：

> **closed exact property + independent finite lift-height bound -> finite exact precision certificate。**

这里的 bound 是 declared world 的一部分，不是 modulus 自己“推断”出来的信息。

## 8. Supernatural precision 描述任意无限实验族

对有限或无限 modulus family，定义 supernatural lcm

`Q_* = product_p p^(q_p)`，

`q_p=sup_M v_p(M)`。

对

`coker(A) ~= Z^f direct_sum T`，

若 torsion exponent 为

`E=product_p p^(a_p)`，

则实验族能 uniform exact certify IMAGE reachability，当且仅当：

- `f=0`，或者 `Q_*` 是 infinite supernatural；并且
- 对每个 torsion prime，都有 `q_p>=a_p`。

所以任意 modular experiment 真正拥有的精度资源只有两类：

1. **free separation** —— supernatural extent 是否足以迫使 free integer coordinate 为0；
2. **prime depth** —— 每个 p-direction 是否达到消灭有限 torsion 所需的深度。

finite families、all-prime breadth、以及一条 tailored power ladder，都只是提供这些资源坐标的不同方式。

## 9. Least precision 出现结构相变

若 cokernel 有限，complete supernatural profiles 形成 principal up-set：

`{Q : E divides Q}`，

并拥有唯一 least element E。

若仍有 free cokernel，则 completeness 还要求 Q 为 infinite supernatural。complete profiles 仍然形成 up-set，但不存在 least element。

其全部 minimal elements 恰好是

`E*p^infinity`，p 任意素数，

即：所有有限 torsion depth 都恰好取 required value，再任选一个 prime direction 无限加深。

因此：

`finite cokernel -> unique least exact precision`，

`free cokernel -> no least exact precision, but infinitely many incomparable minimal unbounded directions`。

对非零 FIBER observation，有 E=1，因此 minimal exact precision directions 就是 `p^infinity`。

## 10. Precision requirements 用 join 合成，而不是相加

一个整数 IMAGE task 可以压成 requirement：

`(free-separation flag ; required p-depths)`。

多个 tasks 共用一个 experiment language 时，requirements 按逐坐标 join 合成：

- free flag -> logical OR；
- p-depth -> maximum。

若 join 后不再有 free direction，least common finite modulus 就是各 torsion exponent 的普通 lcm。

若 join 后仍需要 free separation，则有限 torsion requirement E 仍按 lcm 合并，而整个 joined free-separation requirement 只需要一条任选的 infinite prime direction 即可承担。

所以 precision resources 的组合律是 lattice join，而不是 scalar addition。

## 11. Foundation routing consequence

当前 precision architecture 已经能区分四个不能混为一谈的问题：

1. **一个 exact object 是否存在？** —— IMAGE/COKERNEL。
2. **若存在，它的 state fiber 有多大？** —— FIBER/KERNEL。
3. **继续提高有限 precision，是否终究能识别一个 false state？** —— closedness。
4. **是否存在一个 finite uniform cutoff，对整个 admissible world 一次性有效？** —— openness；或者在加入 independent bound / 改变 ambient admissible world 后重新获得 openness-like finite certificate。

这给之前若干“有限精度”直觉一个严格数学解释：

- “当前还没有区分出来”不等于“exact 相同”；
- “总有某个有限 precision 能区分”不等于“存在一个 universal finite precision”；
- “必须无界提高 precision”也不意味着存在唯一 canonical 的提高方向。

Profinite topology、subgroup separability、finite-index lattices、Smith normal form 和 supernatural numbers 都是标准既有数学。Enterprise Math 在这里的价值是 routing 与 precision interpretation，而不是这些一般代数事实本身。