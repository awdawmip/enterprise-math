# Bounded Local Law Reflection：先反射局部法则，再做无界精确组合

状态：`RESEARCH BRIDGE / NONCANONICAL`

structure-first path-count 路线暴露出一个更一般的原则：有限精度 observation 不需要直接表示未来多轮 composition 后可能出现的所有大数；它只需要精确反射**生成这些 future values 的 bounded local law**。

本文先在有限整数 weighted transition system 上把该原则做成可执行 theorem，再把可复用架构与 weighted-relation 特例分开。

## 1. Primitive weighted local law

设 X 是有限 state set。每个 named action 携带有限 integer-weighted relation：

`w_a(x,y) in Z`，

省略的 edge 视为 weight0。

对当前 target partition E、source x 与 target block C，local coefficient 定义为：

`A_a^E(x,C)=sum_(y in C) w_a(x,y)`。

Weighted transition stability 要求 equivalent sources 对每个 action、每个 target block 都具有相同的 exact local aggregate vector。

## 2. Local aggregate alphabet 是有限的

固定一个 source/action。当前 target block 与该 source 的有限 outgoing edge set 相交后只会得到某个 subset，所以任何 block aggregate 都是这些 primitive weights 的 subset sum。

对全体 sources/actions 取并，得到有限集合：

`L_local subset Z`。

无论 future horizon 多深，weighted partition-refinement step 真正读取的 coefficient 都只来自这个 finite alphabet。

若声明一个 world class，其 primitive weights 来自 W，每个 source/action 最多有 Delta 条 outgoing edges，则一个统一安全 alphabet 是：

`L(W,Delta)={至多 Delta 个 W 元素之和}`。

允许 primitive value 重复，因为不同 edges 可以携带相同 weight。

## 3. Generic finite-code theorem

设

`c:L_local -> C`

是任意 hashable code。

只要 c 在 `L_local` 上 injective，把每个 exact local aggregate 换成它的 code，就会在任何 current partition 上产生与 exact integer 完全相同的一轮 refinement。归纳可得完整 refinement sequence 与 stable state quotient 全部相同。

关键点：C **不必是 semiring**，甚至不需要定义加法与乘法。

对 **reflection-before-compose** 来说，只需要：

- local code 在 finite alphabet 上 injective；
- 能从 code 唯一 decode 回 exact local value。

## 4. Modular quotient 只是一个 specialization

对

`c_M(z)=z mod M`，

只要 mod-M 在 `L_local` 上 injective，就会精确复现整个 weighted refinement。

一个简单 sufficient bound 是：

`M > max(L_local)-min(L_local)`。

因为两个不同 local values 的差绝对值小于 M，不可能是非零 M 倍数。

branch 还搜索一个 finite alphabet 的最小 reflective modulus。它可能远小于 width bound，因为真正相关的是 residue pattern。

例如：

`L={0,2,4}`

宽度为4，mod5 是显然 guarantee，但 mod3 已经 injective。

## 5. Bounded primitive world class 上的 universal necessity

对“primitive set=W、outdegree<=Delta”的整个 world class，injective-code 条件也是 universal theorem 的必要条件。

若存在两个不同 bounded sums

`r != s`

被 code 合并，就把 r/s 各自实现成 primitive edge weights 之和，并让两个 same-observation source 的全部 targets 落进同一个 observation block。

exact weighted refinement 第一轮会拆开两个 sources；coded refinement 会合并它们。

owner 提供 collision→relation compiler 自动构造这类 sharp witness。

因此对声明的 world class：

`universal exact local reflection`

当且仅当

`local code 在 L(W,Delta) 上 injective`。

## 6. Exact local decode 可以恢复整个 weighted machine

令 E 为 reflected 后的 stable partition。因为 E exact-weight stable，对每个 action、source block D、target block C：

`B_a[C,D]=A_a^E(x,C)`, `x in D`

与 representative 无关。

若 local code injective，则每个 encoded block weight 都能在 `L_local` 中唯一 lift 回 exact integer aggregate。因此可以从 finite local code 重建 exact integer quotient matrices `B_a`。

implementation 会把 reconstructed matrices 与直接 exact-integer quotient matrices 交叉比较。

## 7. Raw weighted future semantics 精确 factor through quotient

对 literal word w，raw weighted execution 会沿每条 path 乘 primitive edge weights，再对 paths 求和。

exact weighted quotient 通过 ordinary integer matrix multiplication 精确再现这些 word values。

branch 另有独立 raw-vs-quotient oracle 逐 word 核对，因此 future factorization 不是由 local reflection code 自证。

这一步把 bounded local reflection 接到了可能无界增长的 future values。

## 8. Reflect before compose 与 compose then quotient

使用 primitive weights 1、2，local alphabet 为：

`{0,1,2}`。

mod3 在整个 local law 上完全 injective。

构造两个两步 paths：

- p 先 weight2，再 weight2，exact derived value=4；
- q 先 weight1，再 weight1，exact derived value=1。

若直接在 mod3 world 里 composition：

`4 == 1 mod3`，

terminal coarse values 被合并。

若先反射并 decode local weights 1、2，恢复 exact weighted machine，再在 Z 中 composition，则正确得到4与1。

因此：

`local quotient exactness`

并不推出

`same quotient 会反射所有 derived large values`。

但它**足以**让 exact derived semantics 在 local decode 后被精确生成。

## 9. Observation code 与 execution algebra 是两个资源

上面的 local code 甚至可以完全没有 algebra：

`0 -> "zero"`, `1 -> "one"`, `2 -> "two"`。

decode 以后再在 Z 中执行 recovered machine 即可。

所以 architecture 应拆成三层：

1. **local observation code**：区分 bounded local law；
2. **reflection / decoder theorem**：恢复 exact local coefficients；
3. **execution algebra**：对 recovered law 做 composition 并生成 future values。

只有当 coarse coefficient world 自己必须在 decode 之前执行 composition 时，才额外要求 semiring homomorphism 等 algebraic laws。

## 10. Capability synergy 再次表现为 local coding synergy

在 local alphabet `{0,1,2}` 上：

- parity 单独把0与2合并；
- Boolean support 单独把1与2合并；
- pair code `(nonzero, parity)` 却能区分全部三个 values。

所以两个单独 insufficient 的 local channels，联合后可以 exactize primitive law。

这是 earlier semantic capability-join synergy 在 bounded-local-law 层的对应物。

## 11. Fixed-world split-content spectrum 更尖锐

对整个 `L_local` injective 是稳健的 world-level condition；但一个 fixed state/observation system 可能需要更少。

沿 exact weighted refinement sequence 前进。每次 x/y 位于同一 current block、但下一轮被拆开时，把它们完整 integer local signature 的坐标差取 gcd：

`g_(h,x,y)=gcd(abs(coordinate differences)) > 0`。

modulus M 会错误地把这一 exact split 合并，当且仅当：

`M | g_(h,x,y)`。

因此 fixed world 的 exact bad-modulus set 精确为：

`B = union_(split events) divisors(g_event), M>=2`。

完整 mod-M sequence 等于 exact sequence，当且仅当 `M notin B`。

## 12. Realized exact moduli 的 lattice geometry

bad set 是有限个 divisibility down-sets 的并。

它的补集——exact moduli——在 divisibility order 下 upward closed。

这又形成一种与此前不同的 modulus-region geometry：

- static model indistinguishability：principal divisor down-set；
- uniform affine exact certification：由 cokernel exponent/free structure 控制的 up-set；
- fixed weighted refinement：有限 split-content divisor unions 的补集。

branch 在 complete two-state sparse weighted family、primitive choices `{-1,1,2}` 与多个 moduli 上，把 split-content criterion 与 literal modular refinement 完整对照。

## 13. Potential alphabet 与 realized precision 必须分开

quotient 可以在一些 mathematically possible local subset sums 上发生 collision，但如果这些 values 从来不会在同一个 current state class 内竞争，state refinement 仍然可能完全 exact。

最极端例子：initial observation 已经 discrete，此时 transition refinement 本身已经完成，即使 local coefficient code 在潜在 alphabet 上不 injective，也不会再损失 state precision。split-content events 为空，所有 M>=2 都 reproduces exact state sequence。

因此要区分：

- **class-uniform local-law precision**：对声明的可能 local alphabet injective；
- **one-world realized precision**：只需保留真正发生的 strict split distinctions。

## 14. 通用架构：reflect before compose

可复用原则并不限于 path counting。

若某个 world 满足：

- local law alphabet finite / bounded；
- finite code 能精确反射该 local law；
- recovered local law 在某 exact algebra 中 compositionally 决定 future evolution；

那么 finite local observation 可以支持 unbounded exact derived semantics，而不需要直接表示每个 future value。

安全 workflow 是：

`bounded local world`

`-> finite code`

`-> exact local reflection / decode`

`-> exact compositional machine`

`-> unbounded derived semantics`。

不安全 shortcut 是：

`bounded local world`

`-> coarse code`

`-> 一直在 coarse code 内 compose`

`-> 没有 reflection theorem 就反推 exact large values`。

## 15. 与 material / ledger route 的关系

本文**不自动证明**任何 E001 material law。它提供的是一个可消费的 precision pattern。

material/ledger route 若要使用，必须自行证明对应的：

- bounded local update alphabet；
- chosen coarse code 对这些 local updates 的 exact reflection；
- compositional state 已保留所有 future-relevant remainder/history channels。

若 ledger provenance、expiry、branch identity 或 DOMAIN data 将来可能重新被读取，就必须在应用本 theorem 前保留进 local law state。

## Owner-local assets

- `bounded_local_law_reflection.py` / tests；
- `bounded_local_law_code.py` / tests；
- `weighted_refinement_modulus_spectrum.py` / tests；
- `PRECISION_BOUNDED_LOCAL_LAW_REFLECTION.{en,zh}.md`。

## Prior art / status

Bounded modular reconstruction、subset-sum alphabet、weighted lumping、GCD content 与 exact machine quotient 都是标准既有数学/CS。P023/A2 保留 generic future-signature/precision ownership。本 Draft 只拥有 bounded-local-law reflection-before-compose 架构及其 weighted transition pressure test。

不声明 repository strict CI、`EXECUTABLE_CHECKED` 或 canonical。Hard block: `NONE`。