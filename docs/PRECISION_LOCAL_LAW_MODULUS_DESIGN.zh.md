# 基于 Difference Spectrum 的 Local-Law Modulus 设计

状态：`RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID：`R-8F3K`

一旦 bounded local law 的 finite codebook 已经确定，怎样选择 reflective modulus 就变成一个有限数论问题。真正控制 exactness 的不是 coefficient 的绝对大小，而是 codebook 中**两两差值的整除结构**。

本文把这一 arithmetic layer 从消费它的 weighted-machine semantics 中独立出来。

## 1. Difference-spectrum criterion

对 finite integer codebook S 定义

`D(S)={|u-v| : u,v in S, u!=v}`。

mod M 在 S 上 injective，当且仅当：

`M` 不整除 `D(S)` 中任何非零 difference。

因为

`u==v mod M`

当且仅当

`M | (u-v)`。

对 contextual codebooks `{L_c}`，只在每个 context 内分别应用该 criterion；cross-context differences 不参与 bad-modulus 判断。

## 2. Bad moduli 是有限 divisor down-set union

对一族 finite contextual codebooks：

`B = union_c union_(d in D(L_c)) Divisors_ge_2(d)`。

所以 bad-modulus set B 是有限的。

Reflective moduli 是所有 `M>=2` 中 B 的补集。

若 M reflective 且 `M|N`，则 N 也 reflective：若 N 整除某个 bad difference，则 M 也必整除它。

因此 exact moduli 在 divisibility order 中形成 upward-closed set。

## 3. Divisibility lattice 中没有 least reflective modulus

这个 upward-closed set 一般不是 principal up-set。

取两个都大于所有 codebook differences 的不同素数，它们都 reflective。若存在一个 divisibility-least reflective modulus，它必须同时整除这两个素数，只能等于1，但1不属于非平凡 modulus world。

因此同一个 finite codebook family 同时具有：

- 外部 numeric cost order 下的最小 modulus；
- intrinsic divisibility precision order 下**没有 least element**。

这再次说明“最小 precision”依赖所选 cost/order，而不是天然唯一对象。

Meet closure 也可能失败。例如 codebook `{0,6}`：mod4 与 mod10 都 reflective，但它们的 gcd2 不 reflective。

## 4. Numeric optimum 夹在 cardinality 与 width 两个界之间

对 contextual codebooks `{L_c}` 定义：

`K=max_c |L_c|`。

任何单一 modulus 若要反射所有 codebooks，至少需要 K 个 residue classes：

`M >= K`。

另一方面，安全上界是：

`M > max_c(max L_c - min L_c)`。

所以 least numeric reflective modulus 被 codebook-cardinality lower bound 与 interval-width upper bound 夹住。

Codebook 有空隙时可以靠近下界。例如 `{0,2,4}` 有3个值，虽然 width=4，但 mod3 已经 exact。

## 5. Exact p-adic collision depth

固定素数 p。对一个 nonzero difference d，mod `p^e` 合并它的两个端点，当且仅当：

`e <= v_p(d)`。

因此第一次同时反射全部 contextual codebooks 的 p-adic exponent 精确为：

`e_p^* = 1 + max_(c,u!=v in L_c) v_p(u-v)`。

若所有 codebooks 都是 singleton，则 e=1 已经足够。

所以 local-law codebook 自己携带一条有限的 p-adic collision-depth spectrum。

例：`S={0,2,4}`：

- p=2 时最大 valuation=2，所以 first exact level 是 mod8；
- p=3 时所有 nonzero differences 的 valuation=0，所以 mod3 第一层就 exact。

## 6. 单 primitive repetition 的闭式 capacity law

若唯一 primitive contribution 是 nonzero integer w，且一个 local aggregate 最多出现 d 份，则 codebook 为：

`{0,w,2w,...,dw}`。

w 在 mod M additive group 中的 order 是：

`ord_M(w)=M/gcd(M,|w|)`。

所以 mod M reflective 的充要条件是：

`M/gcd(M,|w|) > d`。

等价地，最大 universal local multiplicity capacity 为：

`capacity_M(w)=M/gcd(M,|w|)-1`。

这说明控制资源不是 primitive 的绝对大小。比如 w=2、d=2 时，mod3 已经能 exactize `{0,2,4}`，虽然3远小于简单 interval width+1 的5。

## 7. 单 primitive 的 p-adic closed form

写

`a=v_p(w)`。

对 d>=1，第一层满足 capacity 条件的 p-adic exponent 是：

`e_min = a + floor(log_p d) + 1`

也等价于：

`e_min = a + ceil(log_p(d+1))`。

因此 primitive 本身含有的 p-divisibility 会先消耗 a 层 p-adic precision，然后才开始提供 multiplicity resolution。

例如 `w=12`、p=2、d=3：

`v_2(12)=2`，

所以第一次 exact 是 mod16（e=4）。

## 8. Unit scaling 不改变 reflection

对 finite codebook S 与满足

`gcd(c,M)=1`

的 integer scale c，乘 c 是 `Z/MZ` 上的 permutation。因此：

`S mod M reflective`

当且仅当

`cS mod M reflective`。

所以只要 scale 是 modular unit，把所有 primitive coefficients 放大很多也不会改变该 modulus 的 precision requirement。

Scaling 只有在与 M 共享 prime factors 时才影响 reflection。

## 9. CRT sensor family 只由 lcm 决定

给定 moduli `M_1,...,M_k`，两个 integers 的完整 residue tuple 相同，当且仅当它们在

`L=lcm(M_1,...,M_k)`

下 congruent。

因此纯 modular sensor family 反射 contextual codebooks，当且仅当 mod L 反射它们。

lcm 是该 sensor family 的 exact arithmetic content。

Noncoprime 冗余 sensors 只增加 carrier / channel cost，不增加超过 lcm 的 residue distinction。

## 10. Modular sensor synergy

多个单独不够的 sensor 可以联合 exact。

对 codebook：

`S={0,1,4}`：

- mod2 合并0与4；
- mod3 合并1与4；
- `(mod2,mod3)` 的 joint code 的 lcm=6，可以区分三个 values。

所以 local-law precision 存在 CRT synergy：

`insufficient channel + insufficient channel -> exact joint code`。

这对应此前 semantic capability synergy 的纯 modular 版本。

## 11. 相同 lcm，不同 resource allocation

虽然一个 modular sensor family 与单一 mod-L channel 在 arithmetic information 上等价，但实现成本不同。

一个大 modulus 把 numeric range 集中在一条 channel；CRT family 把它拆成多条较小 channels，可以并行处理。

因此 arithmetic exactness 只看 lcm，而 storage width、channel count、parallel execution 与 synchronization cost 会形成额外 Pareto 问题。

这直接连接项目已有的 storage / execution-depth resource axis。

## 12. Precision geometry 对照

不同 exactness property 会产生不同的 modulus-lattice 几何。

此前 affine uniform certification 在 free obstruction 消失时得到 principal up-set `{M:E|M}`，存在唯一 divisibility-least modulus E。

Finite local-code reflection 则得到 finite divisor union 的补集：它 upward-closed、cofinite，但没有 divisibility-least modulus。

所以仅说“提高 modulus precision”不足以描述 exactness geometry；真正决定 admissible lattice region 的是 task property 本身。

## 13. 下一复杂度边界

如果 available modular sensors 被限制在一个 declared prime set 中，寻找最少 sensor subset，使 joint lcm 反射所有 contextual differences，会变成一个 covering problem。

每个 prime sensor 能分开的，恰好是它**不整除**的那些 differences。

因此 constrained precision design 会自然进入 finite Set Cover / Hitting Set 复杂度层。这是下一 owner-local frontier。

## Owner-local assets

- `src/enterprise_math/local_law_modulus_design.py`；
- `tests/test_local_law_modulus_design.py`；
- 本双语 theorem note。

## Prior-art / status

Modular injectivity、divisibility lattice、p-adic valuation、additive order 与 CRT 都是标准数论。P023/A2 保留 precision / future-signature ownership。本文只拥有 finite-difference modulus-design specialization。

无 repository strict CI、无 `EXECUTABLE_CHECKED`、无 canonical claim。`CI_NOT_REQUIRED_FOR_RESEARCH`。Hard block：`NONE`。
