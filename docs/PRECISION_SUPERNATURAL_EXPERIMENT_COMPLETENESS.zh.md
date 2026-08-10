# Supernatural LCM 下的 Modular Precision 完备性

状态：`RESEARCH BRIDGE / NONCANONICAL`

有限 modular family、全部素数模、以及一条 `R,R^2,...` 的幂精度 ladder，并不是三种彼此无关的精度机制。它们都是同一个对象的不同形状：已声明模数族的 **supernatural least common multiple**。

## 1. Supernatural precision profile

设 `M_family` 是任意非空正整数模数族，可以有限，也可以无限。对每个素数 `p` 定义

`q_p = sup_{M in M_family} v_p(M)`，

其中取值属于 `N union {infinity}`。

定义 supernatural lcm

`Q = product_p p^(q_p)`。

当且仅当只有有限多个 `q_p` 非零，且每个非零 `q_p` 都有限时，Q 才是一个普通有限整数。否则称 Q 为 **infinite supernatural**。

对整数 affine IMAGE 的 exact certification 来说，这个模数族真正提供的精度资源只有两类：

1. Q 是否为 infinite supernatural —— 它决定能否消灭一个无界的 free integer coordinate；
2. 每个素数方向的深度 `q_p` —— 它决定能否消灭有限的 p-primary torsion。

## 2. 有限生成阿贝尔群上的交定理

设

`G ~= Z^f direct_sum T`

为有限生成阿贝尔群，并设 T 的 p-primary exponent 为 `p^(a_p)`。

对已声明模数族：

`intersection_{M in M_family} M G`

可以按 free 部分和各素数部分精确分解。

### Free 部分

若 supernatural lcm 实际是有限整数 D，则

`intersection_M M Z = D Z`。

若 Q 是 infinite supernatural，则

`intersection_M M Z = {0}`。

换言之，一个非零整数能被所有已声明 modulus 同时整除，当且仅当这些 modulus 存在一个有限普通 lcm，并且该整数是它的倍数。

### p-primary torsion 部分

在有限 p-primary group `T_p` 上，与 p 互素的因子都是可逆的，因此只有 `v_p(M)` 有效。于是

`intersection_M M T_p = p^(q_p) T_p`，

并约定：若 `q_p>=a_p` 或 `q_p=infinity`，结果就是0。

因此

`intersection_M M G = {0}`

当且仅当：

- `f=0`，或者 Q 是 infinite supernatural；并且
- 对每个 torsion prime p，都有 `q_p>=a_p`。

这就是 modular experiment resource 的完整充要条件。

## 3. Exact affine IMAGE 的完备性

对

`A:Z^n -> Z^m`，`G=coker(A)`，

modular solvability 正是：

`A x == b (mod M)` 可解

当且仅当

`[b] in M G`。

因此，实验族能够对**所有整数 target**正确判定 exact reachability，当且仅当

`intersection_M M coker(A) = {0}`。

写成

`coker(A) ~= Z^f direct_sum T`，

并令

`E=exp(T)=product_p p^(a_p)`。

那么 all-target exact criterion 就是：

`f=0 or Q is infinite supernatural`，

并且

`a_p<=q_p for every p|E`。

如果 target 已经被独立知道是 rationally reachable，那么它的 free cokernel coordinate 已经为0，因此只剩 torsion-depth 条件。

## 4. 有限模数族只是一个特例

对有限 family：

`Q=D=lcm(M_family)`

是普通有限整数，所以它永远无法 uniform 分离一个 unrestricted free cokernel coordinate。

因此 all-target criterion 退化为

`f=0 and E|D`。

若只考虑 rationally reachable targets，则退化为

`E|D`。

这正好恢复 finite-family theorem，也解释了为什么实验个数本身没有意义：一旦 lcm D 固定，所有 equality precision 已经固定。

## 5. “所有素数只测一次”是第二个特例

取全部素数 modulus：

`Q = product_p p`。

由于它含有无限多个不同素数，Q 是 infinite supernatural，因此 free integer coordinate 会被完全分离。

但每个素数方向只有

`q_p=1`。

所以 all-prime tests 能 uniform exact certify，当且仅当每个 torsion depth 都满足 `a_p<=1`，也就是 torsion exponent E 为 squarefree。

这正是 prime breadth / p-adic depth theorem。

## 6. 一条幂 ladder 是第三个特例

对

`M_family={R,R^2,R^3,...}`，`R>1`，

有：

`q_p=infinity` 对所有 `p|R`，

而

`q_p=0` 对所有 `p not| R`。

其 supernatural lcm 是 infinite，因此能分离 free part。它能杀掉全部 torsion，当且仅当每个 torsion prime 都出现在 R 中：

`rad(E)|R`。

这说明：为什么对一个固定 cokernel obstruction spectrum，一条 tailor-made 的无界 ladder 就可以替代完整 modulus lattice。

这里必须明确：这条 ladder **并不**在完整 divisibility lattice 中 cofinal；它之所以足够，是因为它的 supernatural precision 已经支配了当前 cokernel 真正含有的全部 prime/depth obstruction。

## 7. FIBER 特例没有 torsion-depth 坐标

对整数 observation map

`O:Z^n -> Z^m`，

exact state agreement 由

`Z^n / ker(O) ~= im(O)`

控制。

而 `im(O)` 是 free abelian，因此 modular experiment family 能 uniform 判定 exact state-output equality，当且仅当：

- `O=0`；或者
- 它的 supernatural lcm Q 是 infinite。

FIBER quotient 上没有 p-primary torsion-depth requirement。这就是 IMAGE 与 FIBER precision profile 不对称的代数原因。

## 8. 多任务 precision 的 join

多个 affine IMAGE tasks 共用一个 experiment language 时，每个 task 都贡献：

- 一个是否需要 free-separation 的 flag；
- 一组有限的 required p-depth `a_p`。

共享实验族必须支配它们的逐坐标 join：

- free requirement 取 OR；
- p-depth 取各 task 的最大值。

用 supernatural 语言说，torsion 部分的最小共同 requirement 就是各 torsion exponent 的 supernatural / ordinary lcm。

如果所有 task 都 full row rank，这个 requirement 仍是普通有限整数：

`lcm(E_1,...,E_k)`。

如果任意一个 unrestricted task 保留 free cokernel，则共享 experiment profile 还必须拥有 infinite supernatural lcm。

## 9. Precision 解释

这给出了 **finite precision、unbounded precision 与 exact integer structure** 之间的一条精确分界。

Modular experiment family 并不需要包含所有 modulus；它只需要支配当前 declared task 真正可能重新激活的 obstruction spectrum：

- 若要排除 free integer direction，需要 infinite supernatural extent；
- 若要排除有限 torsion，需要在每个相关 prime 方向达到足够 p-adic depth。

有限 modular no-go，恰好发生在 experiment profile 缺少其中某个资源坐标时。

反过来，local-global 正面 theorem，恰好发生在 experiment profile 已经逐坐标支配全部 obstruction requirement 时。

这里使用的 supernatural numbers、primary decomposition、有限生成阿贝尔群和 profinite topology 都是标准既有数学。项目价值在于把此前分散的 modular experiment 形状统一成同一个 precision-resource 判据。