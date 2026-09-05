# X0(12) 上 signature 2/3/4 的二次 character、Čech cocycle 与同时线性化覆盖

Status: `FREE_RESEARCH / DERIVED_CHARACTER_COCYCLE_CLASSIFICATION / EXACT_SIMULTANEOUS_LINEARIZATION_OBSTRUCTION / NOT_AXIOM / NOT_FOUNDATION`

Date: `2026-09-04`
Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`
Parent candidate: `EM-FREE-F6D046-C1-ROTATIONAL-PERIOD-WRONSKIAN`
Research unit: `EM-FREE-F6D046-R4-X0-12-THREE-SIGNATURE-CHARACTER-COCYCLE`
Blindness status: `ANCHOR_EXPOSED / PHASE-B CONTINUATION`

## 0. 结论

将三种 Gauss 周期系统

`U_2(x)=2F1(1/2,1/2;1;x)`, `U_3(y)=2F1(1/3,2/3;1;y)`, `U_4(z)=2F1(1/4,3/4;1;z)`

放到标准同一 tau 的 congruence 共同覆盖 `Y=X0(12)` 上。项目化周期局部系统相同，但线性 lift 并非三个都相同。选 signature 3 为基准，存在两个独立二次 character `chi_2,chi_4: pi_1(Y^o)->mu_2`，使

- `L_2 ~= chi_2 tensor L`；
- `L_3 ~= L`；
- `L_4 ~= chi_4 tensor L`。

`chi_2` 在 signature-2 负中心 cusp 的两个奇分歧原像上非平凡；`chi_4` 在 signature-4 order-2 椭圆点的四个二重原像上非平凡。前者是 cusps，后者是内部点，故分支集不交。两个 character 独立并生成 `(Z/2)^2`。

两两过渡 character 为

`chi_23=chi_2`, `chi_34=chi_4`, `chi_24=chi_2 chi_4`,

且严格满足 `chi_23 chi_34 chi_42=1`。所以不存在额外 associator、Čech 2-cocycle 或 mu_2-gerbe 阻碍；剩余阻碍是秩 2 的 `H^1(Y^o,mu_2)` character 子空间。

共同 kernel cover 是次数 4 的 `(Z/2)^2`-Galois 覆盖。紧化后在 6 个点具有阶 2 inertia，Riemann--Hurwitz 给出 `g=3`。三个非平凡二次中间覆盖的 genus 为 `0,1,2`，对应分支点数 `2,4,6`。

Clausen/symmetric-square 消去中心符号：`Sym^2(chi_s tensor L)=Sym^2(L)`。因此三个 rank-3 Clausen 系统可在 X0(12) 上线性统一；但共同 monodromy 仍非平凡，不存在非零全局平坦评价协向量。平方消除中心 twist，不等于局部系统整体平凡化。

## 1. congruence 共同底面

采用 Ramanujan alternative-base 的标准 modular typing：signatures 2、3、4 的同一 tau projective period carriers 分别由 levels 4、3、2 的 genus-zero modular curves承载。于是

`Gamma0(4) intersect Gamma0(3) intersect Gamma0(2)=Gamma0(12)`。

标准指数 `mu(N)=N product_{p|N}(1+1/p)` 给出 `mu(2)=3, mu(3)=4, mu(4)=6, mu(12)=24`。所以 X0(12) 到 X0(4), X0(3), X0(2) 的覆盖次数分别是 `4,6,8`。

X0(12) 有 6 个 cusps、无 order-2/order-3 椭圆点，且 `g=1+24/12-6/2=0`。

这里的共同底面只指标准同一 tau 的 congruence 交，不排除改变 modular marking 或允许非-congruence 对应后出现更小抽象 orbifold span。

## 2. signature 4 的中心 character

signature 4 椭圆指数是 `{1/4,3/4}`。X0(2) 有一个 order-2 椭圆点，而 X0(12) torsion-free。次数 8 覆盖在该点上由四个 ramification index 2 的内部点组成。指数拉回为 `{1/2,3/2}`，两个线性本征值均为 -1：projective monodromy 消失，linear monodromy 是中心元 `-I`。

记这四个内部点为 B4。对应 character chi4 在每个小环上取 -1，故 `|B4|=4`。其 kernel double cover 紧化 genus 为 `(4-2)/2=1`。

## 3. signature 3 基准

signature 3 的椭圆指数是 `{1/3,2/3}`。X0(3) 的 order-3 椭圆点在次数 6 覆盖中有两个 index-3 原像。指数变为 `{1,2}`，线性 monodromy 为 +I。故可取 `L_3=L` 作为共同 projective system 的线性基准。

## 4. signature 2 的 cusp character

signature 2 方程局部指数型为 `0:{0,0}`, `1:{0,0}`, `infinity:{1/2,1/2}`。因此 infinity 的 projective monodromy 是抛物型，但线性 lift 带共同中心符号 -1。

在 X0(4) 的标准 cusp 标记中，该点对应 denominator 2、width 1 的 cusp。X0(12) 的六个 cusp denominators 为 `1,2,3,4,6,12`，widths 为 `12,3,4,3,1,1`。映到 X0(4) denominator-2 cusp 的恰是 denominators 2 与 6，局部次数分别为 3 与 1，均为奇数，所以中心符号仍为 -I。

记这两个 cusps 为 B2，则 `|B2|=2` 且 `B2 intersect B4=empty`。chi2 的 kernel double cover 紧化 genus 为 0。

## 5. character 独立性与 cocycle

取围绕 B2 中一点的小环 gamma2 和围绕 B4 中一点的小环 gamma4：

- `(chi2(gamma2),chi4(gamma2))=(-1,+1)`；
- `(chi2(gamma4),chi4(gamma4))=(+1,-1)`。

故 `<chi2,chi4> ~= (Z/2)^2`。令 chi3=1，定义 `chi_ij=chi_i chi_j^{-1}`。由于 mu2 交换且元素自逆，`chi_ij chi_jk=chi_ik`，特别 `chi23 chi34 chi42=1`。不能同时选择单值 gauge 的原因是两个 H1 类非零且独立，而不是 H2 associator 非平凡。

## 6. 最小同时线性化覆盖

联合 character 映射 `Phi=(chi2,chi4):pi1(Y^o)->(Z/2)^2` 满射，所以共同 kernel cover 次数为 4。任何同时平凡化二者的连通覆盖基本群都包含 ker Phi，故次数至少 4；共同 kernel cover 达到下界。

紧化分支集合 `B=B2 disjoint_union B4` 有 6 点，每点 inertia 阶 2。Riemann--Hurwitz：

`2g-2 = 4*(-2)+6*4*(1-1/2) = -8+12 = 4`，故 `g=3`。

第三个非平凡 character chi2chi4 在 6 点分支，其中间 double cover genus 2。三个中间 genera 为 `0,1,2`，总和 3。

## 7. symmetric-power parity theorem

对任意 m>=1，`Sym^m(chi tensor L) ~= chi^m tensor Sym^m(L)`。所以：

- m 偶：全部二次 twist 消失；
- m 奇：原 character 完整保留。

Clausen 平方是 m=2 的首个非平凡实例。共同 rank-2 monodromy仍包含两个非共线抛物元；一个行协向量若同时被上、下非平凡 unipotent 固定，只能为零。其正次数 symmetric powers 亦无共同非零不变量。

`TWIST_KILLED != LOCAL_SYSTEM_TRIVIAL != GLOBAL_FLAT_EVALUATION_COVECTOR`。

## 8. P000 边界

本结果是多切片粘合的严格二维局部系统模型：pairwise transition 可满足 cocycle，却仍有非零 H1 character rank；同时线性化次数由 character rank 决定；symmetric square 可抹去中心 twist。这些事实不决定 P000 六维补空间、旋转群或跨切片耦合，不得解释为现实的额外维度。

## 9. 工具复用与公理门

- T9 Holonomy/Cocycle/Gluing: `REUSE_APPLIED`；保留“holonomy 不唯一决定 repaired object”的硬边界。
- T7 Finite Symmetry/Equivariance: `COMPOSE_APPLIED`；没有从无固定点数据推导 canonical gauge。
- Tool harvest: `RESULT_ONLY / NO_NEW_TOOL_FAMILY`。

公理门：`DERIVED_CHARACTER_COCYCLE_CLASSIFICATION / NOT_NEW_AXIOM / NOT_FOUNDATION`。
