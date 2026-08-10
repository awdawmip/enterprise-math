# Minimal Supernatural Precision Filters

状态：`RESEARCH BRIDGE / NONCANONICAL`

Supernatural completeness theorem 不仅能判断一个 modular experiment family 是否足够，还能精确给出**所有足够 precision profiles 的序结构**。

设一个 affine IMAGE task 满足

`coker(A) ~= Z^f direct_sum T`，

其有限 torsion exponent 为

`E=product_p p^(a_p)`。

用 divisibility，也就是逐 prime 的 p-adic depth，给 supernatural precision profiles 排序。

## 1. Finite cokernel：存在唯一 least exact precision

若

`f=0`，

不存在需要消灭的 free integer direction。完备性的条件就是

`E | Q`。

因此全部 complete precision profiles 形成 principal up-set：

`{Q : E divides Q}`。

它有唯一 least element：

`Q_min=E`。

所以 finite cokernel 会产生一个 canonical least exact modular precision。

## 2. Free cokernel：完备性仍向上闭，但失去 least element

若

`f>0`，

uniform completeness 要求：

- `E|Q`；并且
- Q 是 infinite supernatural。

这个集合仍然 upward closed，但不再是 principal filter，也**不存在 least element**。

这并不是说没有 minimal precision。恰恰相反，它拥有无穷多个两两不可比的 minimal choices。

## 3. 全部 minimal complete profiles

对任意素数 p，定义 `Q_p`：

- `v_p(Q_p)=infinity`；
- 对每个 `q!=p`，`v_q(Q_p)=a_q`。

那么 `Q_p` 是 complete 且 inclusion-minimal。

反过来，每一个 minimal complete supernatural profile 必然具有这个形状。

证明可以直接按精度坐标压缩：

- 任何高于 required `a_q` 的有限 depth 都可以继续降低；
- 如果有两个不同 prime 都是 infinite depth，可以把其中一个降回它的有限 required depth，另一个仍足以分离 free part；
- 如果没有任何 infinite-depth prime，而是依靠无限多个额外 prime 形成 infinite support，那么删掉有限个额外 prime 后仍然是 infinite supernatural，因此不可能 minimal；
- 所以 minimal profile 必须恰好只有一个 prime direction 为 infinity，其余坐标都精确等于有限 torsion requirement。

因此

`minimal complete profiles = {Q_p : p prime}`。

## 4. 不同 minimal directions 的 meet 恰好掉回不完整层

对不同素数 `p!=q`：

`gcd(Q_p,Q_q)=E`。

若 `f>0`，E 是有限的，因此无法分离 free part，已经不 complete。

所以一旦存在 free cokernel，complete-profile up-set 不再对 meet 闭合。

这给出一个清晰的 precision-lattice phase change：

`finite cokernel -> unique least precision / principal filter`，

`free cokernel -> no least precision / infinitely many incomparable minimal unbounded directions`。

## 5. 一个具体的 minimal experiment family

任意 `Q_p` 都可以由

`M_e=E*p^e`，`e=0,1,2,...`

实现。

第0层 mod E 已经检测全部非零 torsion class。如果 target 继续通过，那么它的 torsion class 已经为0，剩下的 obstruction 只能来自 free part。之后只需要沿一个任选的 p-adic direction 无限加深，就一定能最终暴露任何非零 free integer coordinate。

这在 supernatural order 上比一个一般的 `R^e` ladder 更经济：后者会把 R 中所有 prime 的 depth 都推到 infinity，而其中很多 torsion prime 实际只需要有限深度。

## 6. FIBER 推论

对于非零整数 observation O，控制 exact state agreement 的 quotient 是非零 free group

`im(O)`。

这里没有有限 torsion requirement，因此 minimal complete precision profiles 直接退化为

`p^infinity`，每个素数 p 各给一条。

所以任意单一 p-adic ladder

`p,p^2,p^3,...`

都是 exact state-output equality 的一个 minimal complete precision axis；而 all-primes breadth 虽然同样 complete，却不是 minimal。

若 `O=0`，requirement 本身为 trivial，least precision 就是1。

## 7. 多任务推论

多个 IMAGE/FIBER tasks 共享一个 experiment language 时，先把它们的有限 torsion requirements 逐 prime 取 max，并把 free-separation flags 取 OR。

若 join 后不需要 free separation，则 joint least precision 就是所有 torsion exponent 的有限 lcm。

若 join 后需要 free separation，并令联合 torsion exponent 为 E，那么 joint minimal complete profiles 恰好是

`E*p^infinity`，p 任意素数。

也就是说，多任务合并并不会迫使我们维护多个彼此独立的 infinite precision directions：只要一条任选的无限 prime direction，就可以承担整个 joined free-separation requirement。

这里使用的 supernatural divisibility 与 primary decomposition 都是标准既有数学。项目价值在于明确 least/minimal precision 的精确几何，并区分“唯一的有限 least precision”与“没有 least、但存在多条不可比 minimal 无界精度方向”这两个结构状态。