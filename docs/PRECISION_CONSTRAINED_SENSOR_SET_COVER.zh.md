# 受限 Modular Sensor 设计包含 Minimum Set Cover

状态：`RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID：`R-8F3K`

对一个 finite local-law codebook，如果 modulus 完全不受限制，arithmetic design 很容易：选一个大于所有 relevant differences 的 prime 即可。真正的组合复杂度只在 **available sensor catalogue 与 cost model 受到约束** 时出现。

本文给出从 Set Cover 到 prime-only modular sensor selection 的 exact polynomial-size reduction，而且每个 contextual codebook 只需要两个 exact integers。

## 1. Set Cover instance

设

`U={i}`

为有限 universe，candidate sets 为：

`S_1,...,S_k subseteq U`。

给 candidate sensor j 分配一个不同 prime `p_j`。

对每个 universe element i 定义 contextual codebook：

`L_i={0,d_i}`，

其中

`d_i = product_(j : i notin S_j) p_j`。

若所有 candidate sets 都覆盖 i，则 empty product 给出 `d_i=1`。

## 2. 一个 prime sensor 精确编码一条 cover incidence

Sensor `p_j` 反射 context i，当且仅当：

`p_j does not divide d_i`。

根据构造，这等价于：

`i in S_j`。

所以 codebooks 的 prime-divisibility incidence matrix 与原始 Set Cover incidence matrix 完全一致，只是把“set covers element”换成“sensor separates context”。

## 3. Sensor family exactness iff set family covers

选择 sensor subset J。

Joint modular code 反射 context i，当且仅当至少一个 selected prime 能区分0与 `d_i`：

`exists j in J : p_j does not divide d_i`。

由 incidence theorem，这等价于：

`exists j in J : i in S_j`。

因此：

`selected modular sensors reflect every contextual codebook`

当且仅当

`selected candidate sets cover U`。

该 equivalence 对**每一个** subset J 都成立，而不只对 optimum 成立。

## 4. Minimum-cardinality identity

在 sensor-name identification 下，两边的 feasible subset family 完全相同。因此：

`minimum number of allowed prime sensors`

精确等于

`minimum set-cover cardinality`。

Executable owner 对 3-element / 3-sensor 的全部 incidence instances 做 exhaustively checking：

512 个 incidence matrices × 每个 instance 8 个 sensor subsets。

## 5. Infeasibility 被完整保存

若某个 universe element 不属于任何 candidate set，则它的 difference 是**所有** allowed sensor primes 的乘积。

于是每个 allowed prime 都整除该 difference，没有任何 sensor subset 可以反射这个 context。

因此 Set Cover infeasibility 与 constrained precision infeasibility 完全对应。

## 6. Reduction 的编码规模是 polynomial

第 j 个 prime 的 bit length 对 k 是 polynomial，且每个 `d_i` 最多乘 k 个这样的 primes。因此 encoded codebooks 的 binary size 对原 Set Cover instance size 也是 polynomial。

所以这是真正的 polynomial-size complexity reduction，不是靠指数长整数作弊。

因此 minimum constrained modular-sensor selection 已经包含 Minimum Set Cover，即使限制到：

- 每个 allowed sensor 都只是 prime modulus；
- 每个 contextual codebook 只有两个 exact integers；
- 没有任何 transition / future-dynamics complexity。

Hardness 来自 **precision-resource selection** 本身。

## 7. Weighted sensor costs

给 candidate sensor 任意 nonnegative cost `c_j`，并把同一 cost 赋给对应 Set Cover candidate。

由于 feasible subsets 完全一致，minimum total sensor cost 精确等于 weighted Set Cover optimum。

所以异构 sensor price、energy cost、latency cost、storage allocation 等资源都会直接继承 weighted covering problem。

## 8. 为什么 unrestricted modulus design 不因此变难

不能把 reduction 过度推广成“所有 modulus design 都 NP-hard”。

若 arbitrary moduli 可自由使用，且目标只是“找一个 exact modulus”，直接选择足够大的新 prime 就可以，不存在上述 Set Cover choice structure。

组合复杂度出现于 world 明确规定：

- 只能使用某个固定 sensor / channel catalogue；或
- 不同 sensors 带有不同固定 cost / capability；或
- 必须从 declared precision basis 中选 subset。

因此 complexity source 是 constrained capability selection，而不是 modular arithmetic 本身。

## 9. 多个 prime channels 与一个 fused composite channel arithmetic 等价

对 selected prime set J，它们的 joint residue tuple 等价于一个 modulus：

`L_J=product_(j in J) p_j`，

因为 primes 两两不同。

所以同一 exact arithmetic code 可以有两种实现：

### Parallel sensor representation

每个 prime modulus 保留为独立 channel。

资源包括：

- channel count `|J|`；
- parallel execution opportunity；
- synchronization / routing overhead；
- 较小的 per-channel arithmetic width。

### Fused scalar representation

把 selected channels 融成一个 composite modulus `L_J`。

资源包括：

- 单一 channel；
- scalar bit width 约为 `log_2 L_J`；
- 不再有独立 prime-channel scheduling。

Arithmetic exactness 完全不变。

## 10. Free fusion 会让 channel-count hardness 消失

若 arbitrary composite modulus 可以按 unit channel cost 无成本生成，那么选够 prime factors 后都能 fuse 成一个 sensor。此时只数**physical channel count**就不再表达原 Set Cover objective。

这并不否定 reduction，而是说明 precision optimization 的 objective function 本身属于 problem definition。

Set Cover theorem 作用于 declared prime-sensor catalogue / selection-cost model。

## 11. Bit-width cost 在 fusion 后仍保留

对 distinct primes：

`log L_J = sum_(j in J) log p_j`。

因此 fused composite modulus 仍保留 additive prime-factor storage-width cost。

如果 sensor cost 取 `log p_j`（或任意 additive per-prime resource），优化 fused modulus 仍然是对 selected prime factors 的 weighted covering problem。

所以 fusion 可以交换 channel count 与 scalar width，但不会抹掉所有 optimization cost。

## 12. Storage / parallelism Pareto

同一个 exact precision 可以位于多个 implementation points：

- 多条 narrow channels，parallelism 更高；
- 较少 fused channels，arithmetic word 更宽；
- 一个 fully fused modulus，channel count 最低但 scalar width 最大。

这与项目此前的 storage / execution-depth Pareto 属于同一类原则：exact law 并不唯一决定 operational representation。

## 13. 与 semantic capability join 的关系

该 reduction 虽然是 arithmetic-only，但结构上与 semantic-preorder theorem 完全一致。

每个 sensor 提供一组 semantic distinctions；declared task 要求这些 distinction 的 union 覆盖全部必要 contexts。最小 precision-resource selection 因而不必具有 matroid-like basis，也不保证存在 canonical basis；任意 set-system structure 已经可以被实现。

这是此前 action-alphabet monotone universality / Set Cover boundary 的 coefficient-sensor 对应物。

## Owner-local assets

- `src/enterprise_math/constrained_sensor_set_cover.py`；
- `tests/test_constrained_sensor_set_cover.py`；
- 本双语 theorem note。

## Prior-art / status

Minimum Set Cover、weighted Set Cover、prime-factor encoding 与 CRT 都是标准既有数学 / CS。P023/A2 保留 precision / future-signature ownership。本文只拥有 constrained modular-sensor reduction 与 precision-resource interpretation。

无 repository strict CI、无 `EXECUTABLE_CHECKED`、无 canonical claim。`CI_NOT_REQUIRED_FOR_RESEARCH`。Hard block：`NONE`。
