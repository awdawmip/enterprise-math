# P024 —— 伴随稳定化对偶，补充 03

状态：`ACTIVE RESEARCH NOTE`  
母文：`docs/P024_ADJOINT_BOUNDARY_PULLBACK_SUPPLEMENT_02.zh-CN.md`  
桥接：P008 序伴随语义、P019 坍缩词稳定化、P020 良基稳定化  
纪律：Galois connection、closure/interior operator、伴随复合与不动点选择均为成熟序理论。本说明只提炼 Enterprise Math 的未来精度后果，以及与坍缩词的精确桥。

## 1. 动机

补充 02 已经指出：前向右伴随动作的左伴随，恰好给出 principal 未来边界的精确反向搬运律。

P020 另一方面已经证明：`WellFoundedLT` 偏序上的单调、向下自映射，会有限稳定到初态下方最大的原始不动点。

因此自然的对偶问题是：

> 如果前向动作向下收缩且存在左伴随，反复做 boundary pullback 会稳定到什么位置？稳定后的边界映射是否仍与稳定后的前向映射互为伴随？

答案是精确的，但终止机制必须严格分开：

- **全局**向上稳定定理需要 `WellFoundedGT` 一类上向良基条件；
- `N_0` 并不满足这一全局条件；
- `N_0` 上的坍缩词之所以仍能向上有限稳定，是因为每条具体轨道都被一个显式公共不动点上界夹在有限整数区间内。

下面不会把这两种机制混在一起。

## 2. 设定

设 `X` 为偏序，并记

\[
\lambda \dashv F
\]

表示

\[
\boxed{
\lambda(a)\le b
\iff
a\le F(b).
}
\]

假设前向动作向下收缩：

\[
\boxed{F(x)\le x.}
\]

伴随映射自动单调，因此 `lambda` 与 `F` 都是单调映射。

## 3. P024-S3-T01 —— 向下的右伴随迫使左伴随向上

状态：已在 `EnterpriseMath/Order/AdjointReductiveDuality.lean` 中 `LEAN-CHECKED`。

对任意 `x`，对自反不等式

\[
\lambda(x)\le\lambda(x)
\]

使用伴随律可得

\[
x\le F(\lambda(x)).
\]

而向下性给出

\[
F(\lambda(x))\le\lambda(x).
\]

故

\[
\boxed{x\le\lambda(x).}
\]

因此，一个向下的前向右伴随动作，其边界侧左伴随必然向上扩张。

这就是补充 02 中方向反转现象的抽象形式。

## 4. P024-S3-T02 —— 左右伴随具有完全相同的不动点

状态：`LEAN-CHECKED`。

在相同假设下，

\[
\boxed{
\lambda(x)=x
\iff
F(x)=x.
}
\]

### 证明

若 `lambda(x)=x`，伴随律给出

\[
x\le F(x).
\]

再与 `F(x)<=x` 合并，由反对称性得 `F(x)=x`。

反过来若 `F(x)=x`，伴随律给出 `lambda(x)<=x`；T01 又给 `x<=lambda(x)`，故 `lambda(x)=x`。∎

所以边界侧向上动力学与前向侧向下动力学方向相反，却指向**同一套 fixed-state skeleton**。

## 5. P024-S3-T03 —— 上向良基序上的有限向上稳定化

状态：`LEAN-CHECKED`。

设 `L:X->X` 单调且向上：

\[
x\le L(x).
\]

若 `X` 具有 `WellFoundedGT`，则普通有限迭代会在有限步后到达初态上方最小的原始不动点。

记所选稳定映射为

\[
\operatorname{coStab}_L(x).
\]

则

\[
\boxed{x\le\operatorname{coStab}_L(x),}
\]

\[
\boxed{L(\operatorname{coStab}_L(x))=\operatorname{coStab}_L(x),}
\]

且对任意满足 `x<=y` 的原始不动点 `y`，

\[
\boxed{
\operatorname{coStab}_L(x)\le y.
}
\]

该稳定映射本身单调、幂等。

它正是 P020 向下稳定定理的严格序对偶。

## 6. P024-S3-T04 —— 稳定化保持伴随关系

状态：`LEAN-CHECKED`。

若同时有 `WellFoundedLT X` 与 `WellFoundedGT X`，并且

\[
\lambda\dashv F,
\qquad
F\le id,
\]

定义

\[
S_\uparrow=\operatorname{coStab}_\lambda,
\qquad
S_\downarrow=\operatorname{stab}_F.
\]

则

\[
\boxed{
S_\uparrow\dashv S_\downarrow.
}
\]

即

\[
\boxed{
S_\uparrow(a)\le b
\iff
a\le S_\downarrow(b).
}
\]

### 证明思路

T02 表明原左右伴随拥有同一个不动点集合。

`S_up(a)` 是该集合中位于 `a` 上方的最小元素；`S_down(b)` 是位于 `b` 下方的最大元素。

若 `S_up(a)<=b`，那么它本身就是 `b` 下方的不动点，故 `S_up(a)<=S_down(b)`，从而 `a<=S_down(b)`。

反之，若 `a<=S_down(b)`，那么 `S_down(b)` 是 `a` 上方的不动点，由最小性得 `S_up(a)<=S_down(b)<=b`。∎

Lean 证明正是通过这种极值不动点刻画完成，并没有假设上下两边逐点稳定所需的步数相同。

## 7. P024-S3-T05 —— 固定动作词继承同一对偶结构

状态：`PROVED`。

设

\[
\lambda_i\dashv F_i,
\qquad
F_i\le id,
\qquad i=1,\ldots,m.
\]

前向词为

\[
W=F_m\circ\cdots\circ F_1,
\]

则其左伴随边界词为

\[
\Lambda=\lambda_1\circ\cdots\circ\lambda_m.
\]

向下映射的复合仍向下，向上映射的复合仍向上，因此

\[
W\le id,
\qquad
id\le\Lambda.
\]

并且

\[
\boxed{
\operatorname{Fix}(W)
=
\bigcap_i\operatorname{Fix}(F_i)
=
\bigcap_i\operatorname{Fix}(\lambda_i)
=
\operatorname{Fix}(\Lambda).
}
\]

向下词的不动点交机制与 P019/P023 已使用的下降链论证相同；向上词只是其上升对偶。这里不另行声称发明新的固定词理论。

只要两个方向分别满足相应终止假设，前向词与边界词就分别选出初态下方最大公共不动点和上方最小公共不动点，并可把 T04 作用到复合伴随上。

## 8. 为什么 T04 不能直接用于 `N_0` 的向上坍缩动力学

自然数存在无限严格上升链

\[
0<1<2<3<\cdots,
\]

所以 `WellFoundedGT N_0` 为假。

因此不能把 T04 当成 `N_0` 上坍缩边界词向上终止的直接证明。

正确的坍缩证明使用更弱的局部机制：

> 对某个具体初始 boundary，其向上轨道单调，并且被一个显式公共不动点从上方界住；相应的有限整数区间不可能容纳无限严格上升轨道。

这已经足够证明坍缩特化，并严格弱于“全局上良基”。

这一区分很重要，因为其他伴随动作可能根本不存在此类上界。补充 02 的反复 floor division 就给出相反例子：其回拉边界轨道 `1,d,d^2,...` 真实无限。

## 9. 坍缩边界算子

对 `p>=1`，回顾

\[
C_p(n)=R_p(n)^p.
\]

定义向上的完全幂选择器

\[
\boxed{
N_p(b)
=
\min\{k^p:k^p\ge b\}.
}
\]

补充 02 已证明

\[
\boxed{N_p\dashv C_p.}
\]

两者的不动点都恰为完全 `p` 次幂。

`C_p` 单调、向下、幂等；`N_p` 单调、向上、幂等。

## 10. P024-S3-T06 —— 坍缩词的边界稳定值是上方最小完全 `L` 次幂

状态：`PROVED`。

取非空指数词

\[
p_1,\ldots,p_m
\]

并记

\[
L=\operatorname{lcm}(p_1,\ldots,p_m).
\]

前向词为

\[
W=C_{p_m}\circ\cdots\circ C_{p_1},
\]

其左伴随边界词为

\[
\Lambda=N_{p_1}\circ\cdots\circ N_{p_m}.
\]

P019 已证明

\[
\boxed{
W^\infty(n)=C_L(n),
}
\]

即 `n` 下方最大的完全 `L` 次幂。

边界侧则有

\[
\boxed{
\Lambda^\infty(b)=N_L(b),
}
\]

即 `b` 上方最小的完全 `L` 次幂。

### 证明

每个 `N_p` 都单调且向上，因此

\[
b\le\Lambda(b)\le\Lambda^2(b)\le\cdots
\]

单调上升。

`N_L(b)` 是完全 `L` 次幂，因此同时是每个 `N_(p_i)` 的不动点，也是 `Lambda` 的不动点。

又因 `b<=N_L(b)` 且 `Lambda` 单调，任意 `k` 都有

\[
\Lambda^k(b)\le N_L(b).
\]

所以轨道被困在有限整数区间

\[
[b,N_L(b)]
\]

中，有限次严格增长后必然稳定。稳定点是所有 `N_(p_i)` 的公共不动点，因此是完全 `L` 次幂；它又不小于 `b`，由 `N_L(b)` 的最小性只能等于 `N_L(b)`。∎

这里没有使用虚假的全局 `WellFoundedGT N_0` 假设。

## 11. P024-S3-T07 —— 稳定坍缩与稳定边界映射构成一个伴随对

状态：`PROVED`。

对任意 `L>=1`，

\[
\boxed{
N_L(b)\le n
\iff
b\le C_L(n).
}
\]

因此

\[
\boxed{N_L\dashv C_L.}
\]

稳定后的前向动力学与边界动力学并不只是“上下对称的两个写法”，而是同一个 Galois connection 的两侧，分别选取上方最小与下方最大公共不动点。

对 T06 的指数词，

\[
\boxed{
\operatorname{stab}(W)=C_L,
\qquad
\operatorname{coStab}(\Lambda)=N_L.
}
\]

这就是 P019 与 P024 的精确结构桥。

## 12. P024-S3-T08 —— 边界词瞬态可依赖顺序，而稳定映射相同

状态：`PROVED BY EXPLICIT WITNESS`。

取指数 `2` 与 `3`，初始 boundary `b=2`，比较两种反复边界词。

一种顺序给出

\[
2\to9\to36\to64,
\]

另一种顺序给出

\[
2\to8\to27\to64.
\]

所以瞬态边界动力学确实依赖顺序。

但

\[
L=\operatorname{lcm}(2,3)=6
\]

且两者都稳定到

\[
\boxed{N_6(2)=64.}
\]

这正是 P019“瞬态词作用可不同、稳定行为由 lcm 控制”的向上版本。

## 13. P024-S3-T09 —— 稳定边界词等价仍是同一个 lcm join 结构

状态：`PROVED`。

T06 表明：任意非空坍缩边界指数词，其稳定映射都精确等于 `N_L`，其中 `L` 是词中全部指数的 lcm。

若两个词有相同 `L`，稳定边界映射完全相同。

反过来，若 `L!=K`，则

\[
N_L(2)=2^L,
\qquad
N_K(2)=2^K,
\]

二者不同。因此

\[
\boxed{
N_L=N_K
\iff
L=K.
}
\]

所以坍缩边界词按稳定等价取商后，与 P019 前向坍缩词一样，由正整数 lcm 类索引。

拼接两个词相当于合并指数要求，稳定类按

\[
\boxed{L\vee K=\operatorname{lcm}(L,K)}
\]

组合。

于是前向与边界侧稳定等价半群拥有同一个 lcm join-semilattice 不变量，而代表元 `C_L` 与 `N_L` 互为伴随。

这里不把 lcm 半格或 closure/interior 对偶宣称为新数学。

## 14. P024-S3-T10 —— 稳定对是同一 fixed skeleton 上的 interior/closure 对

状态：`PROVED`。

对每个 `L>=1`：

- `C_L` 单调、向下、幂等；
- `N_L` 单调、向上、幂等；
- 二者都以完全 `L` 次幂为恰好不动点；
- `N_L ⊣ C_L`。

因此同一套有限信息 skeleton 上自然存在两个规范选择器：

\[
\boxed{
\text{上方最近 fixed state}
\quad\dashv\quad
\text{下方最近 fixed state}.
}
\]

P024 把上侧选择器解释成稳定的未来边界回拉，P019 把下侧选择器解释成稳定前向坍缩。

closure/interior 语言本身属于成熟序理论。

## 15. 可执行与形式化审计

形式化：

- `EnterpriseMath/Order/AdjointReductiveDuality.lean`

Lean 已检查：

- 向下右伴随推出向上左伴随；
- 左右伴随不动点集合相同；
- `WellFoundedGT` 下的有限向上稳定化；
- `coStabilize` 的不动点选择、单调性与幂等；
- 当上下两个方向分别满足良基假设时，稳定伴随 `coStabilize(l) ⊣ stabilize(u)`。

可执行回归：

- `tests/test_p024_adjoint_stabilization_dual.py`

写文档前的独立压力测试包括：

1. 长度 1–5 有限链上的全部单调、向下、右伴随映射；
2. 这些映射上长度最多 3 的数千个固定词；
3. 具有固定拓扑标号的至多 4 元非链有限偏序，其中所有可用的向下右伴随对及短词族；
4. `(2,3)`、`(3,2)`、`(2,4)`、`(4,6)`、`(2,3,5)`、`(3,4,6)` 等坍缩指数族和数百个 boundary；
5. `N_L(b)<=n iff b<=C_L(n)` 的直接有界检查。

这些审计域内没有发现反例。抽象 T01–T04 另外已经通过 Lean；`N_0` 的局部有界 T06–T10 由上面的普通证明支撑，并没有假装 `N_0` 满足 `WellFoundedGT`。

## 16. 前人工作与新颖性边界

以下均为成熟数学，不属于 Enterprise Math 发明：

- Galois connection 与伴随复合；
- closure/interior operator 及 fixed-point 刻画；
- 良基有限稳定化模式；
- 公共完全幂 fixed-point 的 lcm 分类；
- 序对偶。

P008、P019、P020 与现有 source 记录已经覆盖这些结构邻域。

项目当前测试的是下面这条综合解释：

\[
\boxed{
\text{前向向下右伴随动力学}
\longleftrightarrow
\text{向上的未来边界 pullback}
\longrightarrow
\text{nearest-fixed 稳定伴随对},
}
\]

以及把 P019 的稳定坍缩映射 `C_L` 精确识别为 P024 稳定边界伙伴 `N_L` 的右伴随。

历史新颖性继续保持 `NOVELTY_UNVERIFIED`。

## 17. 下一问题

1. 把全局 `WellFoundedGT` 充分条件替换成一个可复用的“局部有界轨道终止”母定理，使其覆盖 `N_0` 而不特化到完全幂；
2. 在 Lean 中进一步形式化坍缩专用的 `N_L ⊣ C_L` 与局部有界稳定化；
3. 把补充 01 的 score-lattice guard 几何与补充 02/03 的非线性伴随 score 演化合并；
4. 研究 boundary-orbit merger count 作为动作语言压缩量，但不得与历史不可逆量 `M_t` 混淆；
5. 判断稳定伴随对何时与 P018 整除精度格上的 precision projection 交换。
