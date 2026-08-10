# Modular Branching Precision 与 GCD/LCM Lattice

状态：`RESEARCH BRIDGE / NONCANONICAL`

普通 modular precision lattice 在 relation branching semantics 中仍然成立，但它的 join 必须和 structural operation interface 一起解释。

对 terminal count traces，lcm 已经是 independent readout join；对 branching operations，lcm 则是 **coupled compositional join**，可能要求比 independent modular readout join 更多的 state refinement。

## 1. Divisibility 仍然是 coefficient precision order

若

`M | N`，

reduction

`Z/NZ -> Z/MZ`

是 semiring homomorphism。

由 branching semiring-morphism theorem，mod-N branching signatures 会递归投影到 mod-M branching signatures。

因此每个 horizon 都有：

`mod-N branching precision`

refine

`mod-M branching precision`。

所以 natural order 仍然不是 modulus 数值大小，而是 divisibility。

## 2. GCD 是共同 modular coefficient coarsening

对 moduli M,N，令

`G=gcd(M,N)`。

若 `G>1`，两个 coefficient semirings 都能 reduce 到 `Z/GZ`，因此两边 branching partitions 都 refine mod-G branching partition。

若 `G=1`，formal common coefficient quotient 就是 trivial mod-1 world：所有 multiplicities 都为 zero。Executable layer 把它保留成 formal bottom，不额外构造 zero-ring branching semiring。

因此 gcd 仍然对应 modular coefficient meet / coarsening 方向。

## 3. LCM inject 到 coefficient product

令

`L=lcm(M,N)`。

Residue map：

`iota: Z/LZ -> Z/MZ x Z/NZ`

`r |-> (r mod M, r mod N)`

是 semiring homomorphism。

它 injective：若两个 residues 在 mod M 与 mod N 下都相同，它们的差同时被 M、N 整除，所以被 L 整除。

其 image 是 compatible residue-pair subring；当 M,N coprime 时，就是完整 CRT product。

由于 coefficient morphism injective，recursive signature map 在每个 branching depth 也保持 injective。因此：

`mod-L branching partition`

精确等于

`(mod-M x mod-N) product-semiring branching partition`。

## 4. LCM 是 coupled compositional join

Compositional-interface theorem 已证明：product-semiring refinement 正是让两套 coefficient interfaces 在同一个 shared state space 上继续 executable 的 coarsest quotient。

结合 injective LCM map，得到：

`E_comp(M,N)=E_LCM(M,N)`。

所以 branching analogue 的 arithmetic join 可以写成：

> **mod-lcm 是唯一的 coarsest shared quotient state，使 mod-M 与 mod-N weighted relation interfaces 能继续共同 composition。**

这把静态 modular lattice 精确延拓到了 branching operation language。

## 5. Independent branching readout join 可以严格更粗

分别计算 stable mod-M 与 mod-N quotients，再取它们的 state-kernel intersection。

这个 readout join 足以分别恢复两个 final modular branching labels。

但 target blocks 被共同拆开后，它不保证任何一套 transition interface 仍然 stable。

因此：

`independent modular branching join`

可能严格粗于

`mod-lcm coupled branching join`。

二者之间的 gap 就是 parent generation 定义的 compositional closure debt。

## 6. Sharp CRT witness：mod2 与 mod3

取十个 states：

`p,q,A,B,C,D,z1,z2,z3,z4`，

observation constant。

Action b 让四个 middle states 的 successor counts 分别为：

- A: 0；
- B: 4；
- C: 3；
- D: 1。

于是 coefficient types 为：

| state | mod2 | mod3 | mod6 |
|---|---:|---:|---:|
| A | 0 | 0 | 0 |
| B | 0 | 1 | 4 |
| C | 1 | 0 | 3 |
| D | 1 | 1 | 1 |

Action a 选择：

`p -> {A,D}`，

`q -> {B,C}`。

### Separate mod2 view

p/q 都看到一个 parity-zero child type 与一个 parity-one child type。

### Separate mod3 view

p/q 都看到一个 residue-zero child type 与一个 residue-one child type。

所以 stable mod2 与 mod3 branching interfaces 都合并 p/q，它们的 independent state readout join 也继续合并 p/q。

### Mod6 / coupled view

mod6 会保留 paired residue types：

p 到达 `{0,1}`；

q 到达 `{4,3}`。

因此 mod6 branching 会拆开 p/q。

这就是 cross-capability successor correlation 的 CRT 版本。

## 7. Terminal modular count traces 的行为不同

对一个 terminal path-count entry n：

同时知道

`n mod M`

和

`n mod N`

精确等价于知道

`n mod L`。

Terminal word traces 只是按 word 与 observation label 索引的一组有限 coefficient arrays。

因此它们的 state partitions 直接满足：

`Trace_L = Trace_M join Trace_N`。

不需要额外 branch-correlation closure，因为 terminal trace semantics 已经先把 successor grouping sum 掉了。

即使在前述 ten-state witness 上、branching operations 有 positive compositional debt，这条 terminal trace law 仍然成立。

## 8. 同一个 arithmetic lcm，有两种 semantic role

公式

`join = lcm`

因此具有 interface-dependent 含义。

### Terminal count-trace interface

LCM 已经是 ordinary independent readout join。

### Branching weighted-operation interface

LCM 是恢复 shared successor-state consistency 之后的 coupled compositional join。

Arithmetic object 相同，但实现它所需要的 state precision 可能不同，因为 structural future language 不同。

## 9. Coprime CRT 给出最干净的 strict example

当 M=2,N=3：

`Z/6Z ~= Z/2Z x Z/3Z`。

Coefficient product 本身没有任何 redundancy。

但两个 stable branching interfaces 的 independent **state** join 仍然可能比 mod6 branching 更粗，因为它忘记：哪个 mod2 child behaviour 与哪个 mod3 child behaviour 属于同一个 successor type。

所以 compositional debt 不是坏 coefficient representation 造成的，而是 successor branches 上的 structural pairing 造成的。

## 10. 与之前 modular precision 路线的关系

此前 integer-action work 已建立：

- divisibility 是 modular precision order；
- `meet=gcd`, `join=lcm`；
- CRT 把不同 prime-power arithmetic precisions 并行分解。

当前 relation 结果保留这些 coefficient laws，但增加一个新的 structural distinction：

> **arithmetic CRT components 在 coefficient 层彼此 independent，但 branching future 可以要求它们在同一个 successor state 上保持 correlation。**

Terminal trace semantics 会把这种 correlation 擦掉；shared relation execution 则必须保留。

## 11. Compiler consequence

对 modular branching tasks：

1. 先利用 divisibility 删除 dominated moduli；
2. 若只需要 terminal modular count traces，remaining moduli 直接以 lcm 合并即可；
3. 若 weighted relation 必须在同一个 shared quotient state space 上直接执行，则使用 mod-lcm branching closure；
4. 把它与 independent readout join 比较，可以显式测出 compositional debt。

因此 arithmetic compression 与 structural closure 是两个不同 compiler stages。

## 12. Prior-art boundary

CRT、gcd/lcm divisibility lattice、modular semiring、weighted bisimulation 与 trace semantics 都是标准既有数学 / CS。A4 保留 relation / witness ownership；P023/A2 保留 declared future-signature 与 precision ownership。

这里的项目价值是 cross-layer theorem：

> **mod-lcm 同时是 coefficient join 与 coupled branching-operation join，而 terminal traces 则把同一个 lcm 直接实现成更简单的 independent readout join。**