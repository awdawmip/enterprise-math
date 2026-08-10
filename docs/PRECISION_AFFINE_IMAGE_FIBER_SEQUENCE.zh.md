# 仿射精度正合序列：先 IMAGE，再 FIBER

状态：`RESEARCH BRIDGE / NONCANONICAL`

本文从整数可达性、critical denominator、modular precision 与动态仿射模型 agreement 中提炼一条可复用架构规则。

## 1. 线性正合序列

对整数同态

`A : Z^n -> Z^m`，

关键的短正合序列是

`0 -> ker(A) -> Z^n -> im(A) -> 0`，

`0 -> im(A) -> Z^m -> coker(A) -> 0`。

这两端回答的是不同问题：

- `coker(A)` 先回答请求的 target 到底有没有被表示；
- `ker(A)` 再回答 target 已固定后，还剩多少不可见方向。

仿射 fiber 必须按这个顺序诊断。

## 2. 仿射 target 就是 cokernel 中的一个类

考虑

`A x=b`，

记 b 在 `coker(A)` 中的类为 `[b]`。

整数 exact world 有三种情况。

### 可达

`[b]=0`。

解集非空，并且是 `ker_Z(A)` 的一个 affine torsor / coset。其自由维数为

`n-rank_Q(A)`。

### 有限 torsion IMAGE 障碍

b 在有理像中，但不在整数像中。此时 `[b]` 在 saturated-image quotient 中是有限 torsion 类。

使得

`s b in im_Z(A)`

成立的最小正整数 s，就是 `[b]` 的 order。

这正是各种有限 denominator / critical-class order 现象的通用形式。

### free cokernel 障碍

b 不在有理像中。此时 `[b]` 有非零 free cokernel 分量；任意正整数倍都无法把 b 推入整数像。

这两种 IMAGE 障碍都不能靠“多存 history”修复。

## 3. modular precision 会改变 IMAGE 问题

模正整数 M 时，求解

`A x == b (mod M)`。

等价于

`b in im_Z(A) + M Z^m`，

也等价于 cokernel 中

`[b] in M coker(A)`。

因此，粗 modular world 可能存在合法 affine state，而 exact integer world 不存在。

例：

`2x=1`

在整数上无解，mod4 仍无解，但 mod3 有解。

所以“某个 modular/coarse world 存在 after-state”不能反推 exact integer target 可达。

## 4. modular IMAGE 通过以后，才进入 FIBER

若 modular target class 通过 IMAGE 检查，则所有 modular 解组成 `ker(A mod M)` 的一个 affine torsor。

若 A 的非零 Smith factors 为

`d_1|...|d_r`，

fiber 的精确状态数为

`M^(n-r) * product_i gcd(d_i,M)`。

若 IMAGE 检查失败，则解集为空，不管这个“如果可解时的 kernel size”多大。

sharp pair：

`2x == 1 (mod4)` -> 空 fiber；

`2x == 2 (mod4)` -> 两状态 fiber。

两者 linear Smith factor 都是 2。

## 5. modular solvability region 与 model equality region 不是同一种 lattice 对象

固定 affine equation，定义

`S={M>0 : A x == b (mod M) 可解}`。

S 在整除关系下向下闭合，并且对 lcm 闭合。因此它等价于某个 supernatural modulus

`product_p p^e_p`

的全部有限 divisors，其中每个 prime exponent ceiling 可以是有限值，也可以是无穷。

例 `2x=1`：S 是所有奇数模数。它不是某个有限整数的 divisor set。

而两个固定整数 observation maps 的 modular **不可辨识区域**，通常是矩阵差 content g 的有限 principal down-set `divisors(g)`。

所以 IMAGE solvability 与 MODEL equality 虽然都位于 modular divisibility precision lattice 中，但区域几何不同。

## 6. 动态 model agreement 消费同一正合序列

两个 total-affine dynamic models 经 homogeneous 编译后，future-difference rows 形如

`(a_i,c_i)`。

要求 initial state x 在所有 future words 下输出一致，就是

`A_inf x = -c_inf`。

仍然按同样顺序：

1. IMAGE：`-c_inf` 是否在 exact / modular image 中？
2. FIBER：若在，exact / modular kernel torsor 有多大？

future language 可以通过两种完全不同的方式继续收紧 agreement：

- linear kernel 变小；
- affine target 离开 image，agreement fiber 在 linear rank 完全不变的情况下直接变成空集。

一个 sharp mod4 例子就会从2个 agreement states 直接掉到0，而 linear Smith factor 始终是2。

## 7. 在五层诊断中的位置

这套 exact-sequence 视角不取代已有五层 precision-state diagnostic。

- IMAGE/COKERNEL：决定 target 是否存在/可表示；
- FIBER：在 target 已存在后决定 multiplicity；
- DOMAIN：决定产生该方程的 operation 是否合法；
- RELATION：决定是不是同时存在多个 admissible equations / successors；
- LEDGER：决定守恒内容如何在 compartments 间重新分配。

声明的 future/coefficient language 决定哪些差异未来仍可见。

架构规则可以压成一句：

> **不要拿 kernel/fiber 数据回答 image-solvability 问题；先证明 affine target 在声明的 coefficient precision 中存在。**

本文使用的正合序列、Smith/Hermite、affine torsor、cokernel、线性同余与 supernatural divisibility 都是标准既有数学。项目价值在于 precision-first 的诊断路由。