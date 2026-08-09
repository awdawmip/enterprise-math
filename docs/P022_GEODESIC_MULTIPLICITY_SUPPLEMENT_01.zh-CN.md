# P022 测地线重数补充 01 —— HCP 接触图与测地增长

状态：`ACTIVE RESEARCH NOTE / EXACT INTEGER DERIVATION / NOVELTY UNVERIFIED`  
归属：`program/p022-geometry-v2`  
依赖：`P022_GEODESIC_MULTIPLICITY.*`  
先验边界：HCP coordination sequence 与一般 geodesic growth 都已有成熟研究；在专项 prior-art audit 前不作创新性主张。

## 1. 目标

FCC 与 HCP 是 multiplicity layer 的第一个关键压力测试，因为两种 close packing 在 radius one 都有 coordination number `12`。

因此 nearest-neighbor degree 无法区分；native graph geodesic defect 也无法区分，因为两者都使用各自的无权 shortest-path metric，所以 `Gamma=0` 恒成立。

真正的问题是：

> **最短 witness 的有限重数能否区分两种 close-packed contact graph？**

答案是肯定的：完整 spectrum 在 radius two 已经分离，而 shell-total growth 最终出现不同指数增长率。

## 2. HCP 的纯整数接触图坐标

取顶点

\[
(q,r,k)\in\mathbb Z^3.
\]

固定 `k` 是 triangular lattice，层内六个 primitive moves 为

\[
(\pm1,0),\ (0,\pm1),\ (1,-1),\ (-1,1).
\]

偶数 `k` 为 A 层，奇数 `k` 为 B 层，形成 ABAB stacking。

从偶数层到任一相邻 B 层，三个水平 offsets 为

\[
S_- = \{(0,0),(-1,0),(0,-1)\};
\]

从奇数层到相邻 A 层为

\[
S_+ = \{(0,0),(1,0),(0,1)\}.
\]

所以每个顶点恰有

\[
6+3+3=12
\]

个接触邻居，全过程不需要浮点球心坐标。

## 3. P022-HCP01 —— 本征图距离闭式

定义 triangular distance

\[
h(q,r)=\max(|q|,|r|,|q+r|),
\]

以及到 B 层 base triangle 的距离

\[
\tau(q,r)=\min\{h(q,r),h(q+1,r),h(q,r+1)\}.
\]

### 偶数目标层

若

\[
|k|=2m,
\]

则

\[
\boxed{
d_H(q,r,k)=m+\max(m,h(q,r)).
}
\]

### 奇数目标层

若

\[
|k|=2m+1,
\]

则

\[
\boxed{
d_H(q,r,k)=m+1+\max(m,\tau(q,r)).
}
\]

### 证明

把 cross-layer moves 两两配对。even→odd 的 offset 来自 `S_-`，odd→even 来自 `S_+`。两步之和只能是零或 triangular lattice 的一个 primitive move，所以每两次跨层最多提供一个水平 triangular distance。

偶数层目标至少需要 `2m` 次跨层。若一条路径有 `V` 次跨层、`H` 次层内步，则

\[
h\le H+V/2,
\]

从而总长度 `L=H+V` 同时满足

\[
L\ge2m,
\qquad
L\ge m+h.
\]

下界即 `m+max(m,h)`。使用恰好 `2m` 次单调跨层可以“免费”实现至多 `m` 个 triangular units，剩余水平差再用层内 geodesic moves 补齐，因此达到下界。

奇数层多一个未配对的 A→B step，它落在 `S_-`；剩余配对仍每对最多提供一个 triangular unit，于是

\[
\tau\le H+\lfloor V/2\rfloor
\]

并得到

\[
L\ge2m+1,
\qquad
L\ge m+1+\tau.
\]

同样由单调跨层路径达到。

## 4. 初始 coordination shells

上述距离公式直接给出

\[
1,12,44,96,170,264,380,516,\ldots
\]

作为 radius `0,1,2,...` 的 shell sizes。

这与标准 HCP contact graph 的 coordination sequence 相符，从而也反向验证了当前整数坐标模型。

不过在本研究里，shell cardinality 只是更深结构的第一层 shadow。

## 5. P022-HCP02 —— 两次跨层的生成多项式

定义 triangular Laurent polynomial

\[
A=x+x^{-1}+y+y^{-1}+xy^{-1}+x^{-1}y.
\]

even→odd 与 odd→even 的水平选择多项式分别是

\[
B_-=1+x^{-1}+y^{-1},
\qquad
B_+=1+x+y.
\]

直接相乘：

\[
\boxed{B_-B_+=A+3.}
\]

其图论含义非常直接：

- 两次跨层可以用一种方式产生六个 triangular primitive displacement 中的任意一个；
- 但产生零水平 displacement 有三种不同 witness。

因此系数 `3` 本身就是 Boolean adjacency 看不到的 multiplicity information。

## 6. P022-HCP03 —— endpoint 最短路 coefficient 闭式

geodesic 不会做 vertical backtracking。多做两次跨层花费 2 步，却最多制造 1 个 triangular horizontal unit；一个层内 step 就能以更低代价完成。因此最短路到 layer `k` 必定只用 `|k|` 次同方向跨层。

### 偶数层 `|k|=2m`

令

\[
t=\max(0,h(q,r)-m),
\qquad d=2m+t.
\]

则

\[
\boxed{
g_H(q,r,2m)
=\binom{2m+t}{t}
[x^qy^r](A+3)^mA^t.
}
\]

### 奇数层 `|k|=2m+1`

令

\[
t=\max(0,\tau(q,r)-m),
\qquad d=2m+1+t.
\]

则

\[
\boxed{
g_H(q,r,2m+1)
=\binom{2m+1+t}{t}
[x^qy^r]B_-(A+3)^mA^t.
}
\]

binomial factor 只是在总 geodesic word 中选择 `t` 个层内 steps 的位置，同时保留跨层 steps 的交替顺序以及层内 steps 的相对顺序。

这个 closed coefficient formula 与另一条完全独立的 inward recurrence

\[
g(v)=\sum_{u\sim v,\ d(u)=d(v)-1}g(u)
\]

在 executable reference 中逐点交叉验证。

## 7. P022-HCP04 —— HCP shell-total geodesic count 的纯整数有限和

记 triangular shell 上的总 geodesic words 为

\[
E_j=6\cdot2^j-6
\quad(j\ge1),
\]

从三点 base triangle 向外的对应总量为

\[
O_j=9\cdot2^j-6
\quad(j\ge0).
\]

固定 shell radius `n>=1`，按目标 layer 分拆。

### 非极端偶数层

若 `|k|=2m<n`，层内步数

\[
t=n-2m>0.
\]

为了落在 horizontal shell boundary，`(A+3)^m` 的每个 factor 都必须选非零 triangular displacement；只要有一次选择零，最大可达 horizontal distance 就会少 1。因此 boundary coefficient sum 等价于

\[
A^{m+t}=A^{n-m}.
\]

每一层贡献

\[
\binom n{n-2m}E_{n-m}.
\]

`m>0` 时正负两层各一份；`m=0` 只有中央层。

### 极端偶数层

若 `n=2m`，没有层内步，整个 `(A+3)^m` 都落在 extreme shell；令 `x=y=1` 得到每层

\[
9^m.
\]

### 非极端奇数层

若 `|k|=2m+1<n`，

\[
t=n-2m-1>0.
\]

同样的 boundary argument 把 `(A+3)^m` 限制成 `A^m`，但保留 base-triangle factor `B_-`，所以每层是 `O_{n-m-1}` 乘 interleaving

\[
\binom n{n-2m-1}.
\]

奇数层总有上下两份。

### 极端奇数层

若 `n=2m+1`，`B_-(A+3)^m` 的全部 coefficients 都贡献，总和每层为

\[
3\cdot9^m,
\]

上下两层合计 `6*9^m`。

于是得到完全整数的闭式：

\[
\boxed{
\begin{aligned}
T_H(n)=\;&E_n
+2\sum_{m=1}^{\lfloor(n-1)/2\rfloor}
\binom n{n-2m}E_{n-m}\\
&+2\sum_{m=0}^{\lfloor(n-2)/2\rfloor}
\binom n{n-2m-1}O_{n-m-1}\\
&+\mathbf 1_{2\mid n}\,2\cdot9^{n/2}
+\mathbf 1_{2\nmid n}\,6\cdot9^{(n-1)/2}.
\end{aligned}
}
\]

前几项为

\[
\boxed{1,12,84,384,1524,5592,19812,68808,236628,\ldots}.
\]

## 8. P022-HCP05 —— 固定整数递推与主导增长根

对有限和使用标准 even/odd binomial identities，可得：当 `n>=8`，

\[
\boxed{
\begin{aligned}
T_n={}&10T_{n-1}-35T_{n-2}+42T_{n-3}+28T_{n-4}\\
&-112T_{n-5}+92T_{n-6}-24T_{n-7}.
\end{aligned}
}
\]

初值

\[
T_1,\ldots,T_7
=12,84,384,1524,5592,19812,68808.
\]

characteristic polynomial 精确分解为

\[
\boxed{
(\lambda-3)(\lambda-2)(\lambda-1)
(\lambda^2-2)(\lambda^2-4\lambda+2).
}
\]

最大代数根是

\[
2+\sqrt2,
\]

所以

\[
T_H(n)=\Theta((2+\sqrt2)^n).
\]

真正用于状态计算的仍是上面的整数有限和或整数递推；`2+sqrt2` 这里只是描述增长率的压缩符号。

## 9. P022-HCP06 —— FCC/HCP 的层级分离

前一份 P022 note 已得到 `A_3/FCC`：

\[
T_{FCC}(n)=6\cdot4^n+8\cdot3^n-24\cdot2^n+12,
\]

故主导增长为 `4^n`。

HCP 则是

\[
(2+\sqrt2)^n.
\]

所以 FCC 与 HCP 同时具有：

- radius-one degree `12`；
- 相同三维量级的 polynomial shell growth；
- native graph `Gamma=0`；

但**最短 witness 总重数具有不同指数增长率**。

这是比 coordination number 更深的有限 geometry signature。

## 10. 完整 spectrum 还严格强于 shell total

radius two 时：

### FCC / `A_3`

\[
\{1:12,\ 2:24,\ 4:6\}.
\]

### HCP

\[
\boxed{\{1:18,\ 2:18,\ 3:2,\ 4:6\}.}
\]

两者 total geodesics 都等于

\[
84,
\]

但 spectrum 已经不同。HCP 中

\[
(0,0,2),\qquad(0,0,-2)
\]

各有恰好 3 条 shortest paths，而 `A_3` radius-two shell 中没有 multiplicity `3`。

因此存在严格的信息阶梯：

\[
\text{coordination number}
<
\text{shell size}
<
\text{shell-total geodesic count}
<
\text{geodesic multiplicity spectrum}.
\]

到 radius three，连 shell total 也分开：

\[
T_{FCC}(3)=420,
\qquad
T_{HCP}(3)=384.
\]

## 11. 解释边界

这些结果**不能**推出 FCC 或 HCP 哪个是“真实物理空间”，也不能推出哪一个动态上更优。

它证明的是 P022 需要的一条数学事实：

> **local coordination 相同、Boolean geodesic completeness 相同，不意味着有限 path structure 相同。**

如果未来 dynamics / collision / transport / precision rule 会读取 alternative minimal witnesses 的数量，那么 multiplicity 就成为真正 observable，两种几何在那个 future language 下不再等价。

“这个信息是否必须保留”的一般合法压缩问题仍归 A2/P023；具体几何及其 spectrum 归 P022。

## 12. executable assets

- `src/enterprise_math/p022_hcp_geometry.py`
- `tests/test_p022_hcp_geometry.py`

测试分别交叉验证：

- closed distance vs BFS；
- recursive shortest-path count vs BFS path count；
- Laurent coefficient count vs 前两者；
- endpoint shell sum vs integer finite-sum formula；
- finite-sum formula vs fixed integer recurrence。
