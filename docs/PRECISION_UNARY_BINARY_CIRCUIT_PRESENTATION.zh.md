# Unary Binary-Power Circuit Presentation

状态：`RESEARCH BRIDGE / NONCANONICAL`

literal macro-table Pareto 在自己的 representation class 内是 exact 的，但不是 global presentation frontier。只需要一个 repeated generator，就能构造 sharp counterexample：只存 powers of two，可以同时获得 logarithmic storage 与 logarithmic worst-case runtime。

## 1. Unary repeated-action language

固定一个 exact transition A 与 repetition horizon h。

任务需要执行：

`A^m`, `0<=m<=h`。

contiguous literal d-macro table 会存：

`A,A^2,...,A^d`，

worst case 需要 `ceil(m/d)` chunks。

## 2. Binary-power presentation

改为只存不超过 h 的 power-of-two transitions：

`A^(2^j)`，

也就是：

`A,A^2,A^4,A^8,...`。

stored transition matrices 数量精确为：

`P(h)=floor(log2 h)+1`，

即 h 的 bit length。

## 3. Precomputation 本身也是 logarithmic

从 A 开始，每一条下一层 macro 只需一次 exact squaring：

`A^(2^(j+1)) = A^(2^j) A^(2^j)`。

因此除 generator 本身外，完整 binary table 只需：

`P(h)-1`

次 matrix multiplications 即可预计算完成。

不增加 semantic law。

## 4. 单个 exponent 的 exact runtime

将 m 写成 binary expansion：

`m=sum_j epsilon_j 2^j`, `epsilon_j in {0,1}`。

则：

`A^m = product_(epsilon_j=1) A^(2^j)`。

runtime macro applications 数量精确等于：

`popcount(m)`。

executable layer 对 integer 与 rational matrices 都与 literal repeated multiplication 做 exact 对照。

## 5. Horizon h 内的 exact worst-case runtime

对 `1<=m<=h`，最大 popcount 恰为：

`floor(log2(h+1))`。

证明：令

`t=floor(log2(h+1))`。

则 `2^t-1<=h`，该 exponent 恰有 t 个1 bits；而最小具有 t+1 个1 bits 的整数是 `2^(t+1)-1>h`。

所以 binary presentation：

`storage = floor(log2 h)+1`，

`worst runtime = floor(log2(h+1))`。

两者都是 logarithmic。

## 6. Same-storage 下严格支配 contiguous macros

使用相同 stored-rule count P(h)，contiguous unary table 最多只能存：

`A,...,A^P(h)`，

worst runtime 为：

`ceil(h/P(h))`。

binary powers 可以严格更好。

第一个 strict horizon 是 h=13：

- 两边都存4条 rules；
- contiguous `{1,2,3,4}` worst 需要4 chunks；
- binary `{1,2,4,8}` 最多只需3。

## 7. Large-gap example

h=1024 时：

- 两个 compared presentations 都只存11条 transition rules；
- binary powers worst runtime=10；
- contiguous depth11 macros worst runtime=94。

所以在完全相同 rule storage 下，仅仅改变 presentation technology 就能把 execution depth frontier 改变近一个数量级。

## 8. Full table 仍然占据另一个 endpoint

完整 unary table：

`A,A^2,...,A^h`

存 h 条 rules，每个 requested power 只需一次 lookup/application。

binary powers 并不支配这个 full-storage endpoint。它创造的是一个新的中间 regime：

`O(log h) storage / O(log h) execution`，

而另外两个 endpoint 分别近似：

`O(h) storage / O(1) execution`

与

`O(1) storage / O(h) execution`。

## 9. 为什么能击穿 contiguous family

contiguous family 把 storage 花在每个 short exponent 上，即使其中很多 exponent 可以由少量 strategic long-scale generators composition 得到。

binary powers 存的是一种**exponent construction basis**，而不是一个 precomputed answer interval。

这是 presentation 层用 circuit / DAG 替代 flat table 的最小例子。

## 10. Representation-class minimality 是实质条件

parent literal-macro theorem 仍然 exact。binary construction 不与它矛盾，因为它离开了那个 representation class。

真正被证明的是：

`execution depth R 下的 minimal storage`

之类说法若不声明 allowed presentation technology，本身就是不完整命题。

同一个 semantic future law 在不同 class 中会有不同 Pareto fronts：

- flat contiguous macro tables；
- binary-power circuits；
- general addition chains；
- arbitrary shared DAG / circuit presentations。

## 11. Scope boundary

本代只处理一个 repeated generator。binary decomposition 使用：

`A^r A^s=A^(r+s)`。

对 multiple noncommuting generators，arbitrary word 不能压成一个 exponent，所以 binary powers 不能直接解决一般 presentation 问题。

multi-generator frontier 属于 semigroup normal form、rewriting system、automata/circuit sharing 与 grammar-like presentation。

## 12. Stage131 bridge

同一个 binary-jump idea 可以直接用于 unary implication chain。

不是只存 adjacent edges，也不是存全部 transitive edges，而是在每个 chain position 存 power-of-two jumps。

它会给出 Hasse adjacency 与 full transitive closure 之间一个新的 exact storage/depth 中间点。下一代直接推导该 chain theorem。

## Owner-local assets

- `src/enterprise_math/unary_binary_circuit_presentation.py`；
- `tests/test_unary_binary_circuit_presentation.py`；
- `docs/PRECISION_UNARY_BINARY_CIRCUIT_PRESENTATION.{en,zh}.md`。

## Prior art / status

Binary exponentiation、repeated squaring 与 addition chain 都是标准既有数学/CS。Enterprise Math 在这里得到的项目价值是：**representation class 会真实改变 presentation storage/execution frontier。**

不声明 repository strict CI、`EXECUTABLE_CHECKED` 或 canonical。Hard block: `NONE`。