# CRT Sensor Factorization 的 Precision Resource Pareto

状态：`RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID：`R-8F3K`

一个 modular precision law 并不会唯一决定一种 operational representation。只要 exact arithmetic content 已固定，CRT 就允许把同一份 precision 分散到多条 narrow channels，或 fuse 成更少但更宽的 channels。

因此即使 exact law 完全不变，内部仍然存在一条 Stage131-style resource Pareto。

## 1. 一个 arithmetic law，多种 exact factorization

设所需 squarefree arithmetic content 为：

`L=p_1 ... p_k`，

其中 primes 两两不同。

把 prime factors 分成 nonempty groups：

`B_1,...,B_g`，

并定义 channel moduli：

`M_r=product_(p in B_r) p`。

这些 M_r 两两 coprime，且：

`product M_r = lcm(M_r) = L`。

CRT 因而给出：

`Z/LZ ~= product_r Z/M_rZ`。

所以任何 grouping 都拥有完全相同的 equality / reflection precision。发生变化的只有 implementation resources。

## 2. 两个 endpoint representations

### Fully fused

只用一个 mod-L channel。

- channel count：1；
- arithmetic word 最宽；
- 若 downstream 需要 scalar mod-L output，则不需要 CRT reconstruction。

### Fully split

每个 prime 一个独立 channel。

- channel count：k；
- atomic channels 最窄；
- parallelism 最大；
- 若 downstream 最终需要 fused scalar residue，可能增加 CRT recombination cost。

所有 intermediate groupings 都是同一个 arithmetic law 的 exact representations。

## 3. Peak residue width

一个 modulus M 存 residue 所需 bit 数为：

`b(M)=ceil(log2 M)`。

对一个 grouping 定义：

`b_peak=max_r b(M_r)`。

Fusion 会减少 channel count，但不可能降低 peak modulus / width。Splitting 则可以降低 peak width，直到 atomic factor 或 packing constraint 阻止继续下降。

## 4. g channels 的 information lower bound

若 g 条 channels 每条最多 b bits，则每个 channel modulus 至多 `2^b`，所以：

`L=product M_r <= 2^(bg)`。

因此：

`b_peak >= ceil(log2 L / g)`。

这是 continuous information-balance lower bound。

## 5. Atomic-factor lower bound

Prime factors 在当前 factorization family 中不可拆。至少有一条 channel 必须容纳最大 prime factor，因此：

`b_peak >= ceil(log2 p_max)`。

两者合并得到：

`b_peak >= max(ceil(log2 L/g), ceil(log2 p_max))`。

Executable compiler 会为每个 grouping 记录这个 lower bound。

## 6. Sharp 210 reference frontier

取：

`L=210=2*3*5*7`。

不同 channel count 下的 exact optimum：

- g=1：`210`，peak8 bits；
- g=2：`14 x 15`，peak4 bits；
- g=3：`6 x 5 x 7`，peak3 bits；
- g=4：`2 x 3 x 5 x 7`，peak3 bits。

四个 optima 都精确碰到 combined lower bound。

因此 fully split 的4-channel representation 被3-channel representation 支配：两者都是 peak3-bit arithmetic，但后者少一条 channel。

真正 nondominated 的 resource points 是：

`(channels,peak_bits)=(1,8),(2,4),(3,3)`。

Splitting 会在到达 atomic endpoint 之前先发生 saturation。

## 7. Discrete factorization packing gap

Information / atomic lower bounds 不一定可实现。

取：

`L=7*11*13=1001`，

g=2 channels。

Continuous information bound 是5 bits；largest-prime bound 是4 bits，所以 combined lower bound=5。

但三个不可分 prime atoms 必须塞进两条 channels。至少一条 channel 要装两个 primes，而最小 pair 已经是：

`7*11=77`，

需要7 bits。

因此 true optimum=7 bits，出现：

`factorization packing gap = 7-5 = 2 bits`。

这是一个 finite indivisibility defect：总 information budget 看起来够，但 primitive factor packing 无法实现 continuous balance。

本文只把它作为 arithmetic packing phenomenon，不自动与项目其他 packing theorem family 合并。

## 8. Rounded total storage law

Ideal information 对 grouping 不变：

`sum_r log2(M_r)=log2 L`。

若每条 channel 按 whole bits 存 residue：

`b_r=ceil(log2 M_r)`，

fused width：

`B=ceil(log2 L)`，

则：

`0 <= sum_r b_r - B <= g-1`。

所以 splitting 可以大幅降低 peak width，而单纯由 bit ceiling 引入的 total residue-storage overhead 每新增一条 channel 最多约1 bit。

该 theorem 不包含 metadata、routing、ECC、synchronization 等 physical overhead；它们是独立资源。

## 9. Conditional CRT reconstruction depth

Residue tuple 本身已经包含完整 arithmetic precision。如果 downstream 可以原生消费 tuple，则任何 grouping 的 reconstruction depth 都是0。

如果 downstream 强制要求一个 scalar mod-L residue，则 g channels 必须重组。

用 binary CRT merges：

- sequential depth：`g-1`；
- ideal balanced parallel depth：`ceil(log2 g)`。

所以 factorization 会交换：

`更窄的 peak arithmetic width`

与

`更多可选 scalar-reconstruction depth`。

这个 depth 是 **interface-dependent** 的；tuple-native consumer 不支付它。

## 10. 210 width/depth curve

对 reference optimal groupings，若 downstream 要求 scalar reconstruction：

- one channel：`(peak bits, parallel depth)=(8,0)`；
- two channels：`(4,1)`；
- three channels：`(3,2)`；
- four channels：`(3,2)`。

再次看到 fully split point 被3-channel representation 支配。

这已经是同一个 exact arithmetic law 内真正的 storage / execution-depth Pareto。

## 11. Contiguous local-count capacity

对 local codebook：

`{0,1,...,D}`，

modular sensor family exact，当且仅当其 joint lcm L 满足：

`L>D`。

所以 universal contiguous local-count capacity 精确为：

`D_max=L-1`。

同一个 L 的所有 CRT factorizations 因而拥有完全相同的 exact capacity。

Resource design 是在 semantic capacity 已经固定之后才开始的。

## 12. Width × channel-count capacity law

若 g 条 channels 的 peak width 都不超过 b bits，则：

`L<=2^(bg)`，

所以：

`D_max < 2^(bg)`。

在 ideal arithmetic bound 下，parallel channel count 可以以指数方式补偿 per-channel residue width。

但 declared prime atoms 是否能被恰好 pack 到这种理想形态，则由离散 factorization 结构决定。

## 13. Fixed-channel optimum 是 multiplicative load balancing

对 exact g channels，最小化 peak modulus 等于：

`min max_r product_(p in B_r) p`。

取 logs 后就是把不可分 jobs `log p` 分配到 g 个 bins 做 balance。

Owner compiler 只对 bounded research fixtures 做 exhaustive set-partition enumeration，不声称存在高效 generic optimizer。

Packing-gap witness 说明 continuous information bound 并不足以直接决定 exact optimum。

## 14. 与 constrained sensor selection 的关系

Parent Set Cover generation 解决的是：从 allowed catalogue 中**选哪些 prime capabilities**。

本 generation 假设 selected prime factor set 已固定，研究**怎样 operationally package 这些 factors**。

所以 precision design 至少分两层 optimization：

1. semantic / capability selection；
2. arithmetic representation factorization。

Minimum selected capability 与 minimum-cost execution representation 不是同一个问题。

## 15. Stage131 interpretation

Stage131 最初发现：同一个 closure law 可以在 rule-table storage 与 execution depth 之间交换。

CRT 结果给出了同一 broader principle 的另一个 exact instance：

> 同一个 exact precision law 可以拥有多种 semantically equivalent factorizations，而这些表示在 width、channel count、reconstruction depth 上具有不同资源成本。

因此 precision 在 mathematical exactness 已固定后，仍然存在 **representation Pareto**。

## Owner-local assets

- `src/enterprise_math/sensor_factorization_pareto.py`；
- `src/enterprise_math/sensor_factorization_execution_depth.py`；
- `src/enterprise_math/sensor_factorization_storage_law.py`；
- 对应 tests；
- 本双语 theorem note。

## Prior-art / status

CRT、factor grouping、set partitions、information-width bounds 与 load balancing 都是标准既有数学 / CS。P023/A2 保留 precision / future-signature ownership。本文只拥有 exact-precision factorization Pareto 与 Stage131 resource interpretation。

无 repository strict CI、无 `EXECUTABLE_CHECKED`、无 canonical claim。`CI_NOT_REQUIRED_FOR_RESEARCH`。Hard block：`NONE`。
