# P019 补充 03 —— 球形挖除、方向边界与跨维恒等式

状态：`RESEARCH WIP / PROVED COMBINATORIALLY`  
范围：`A_p` primitive graph ball、离散空腔、方向边界、维数递归  
纪律：本文不把 `A_p` 物理解释为已证实自然空间，也不把 graph ball 与连续欧氏球等同。

## 1. 问题

在 `A_3/FCC` 型密堆整数关系空间中挖去一个“球”，观察空腔在不同维数中的体积、边界和方向投影是否由同一套整数规则生成。

先采用 primitive graph distance

\[
d_G(0,x)=\sum_{x_i>0}x_i=\frac12\sum_i|x_i|,
\]

定义 `p` 维 graph ball

\[
B_p(r)=\{x\in A_p:d_G(0,x)\le r\},
\qquad V_p(r)=|B_p(r)|.
\]

这不是声明物理球必须使用 graph distance；后文专门比较 finite-precision radial ball。

## 2. 体积与离散表面

已有 `A_p` 球增长式给出

\[
V_p(r)=\sum_{j=0}^{\min(p,r)}\binom pj^2\binom{r-j+p}{p}.
\]

定义外壳

\[
S_p(r)=V_p(r)-V_p(r-1).
\]

因此对所有维数统一有

\[
\boxed{S_p=\nabla V_p.}
\]

低维展开：

\[
\begin{aligned}
V_1(r)&=2r+1,&S_1(r)&=2,\\
V_2(r)&=3r^2+3r+1,&S_2(r)&=6r,\\
V_3(r)&=\frac{(2r+1)(5r^2+5r+3)}3,&S_3(r)&=10r^2+2,\\
V_4(r)&=\frac{35r^4+70r^3+85r^2+50r+12}{12},
&S_4(r)&=\frac{5r(7r^2+5)}3.
\end{aligned}
\]

所以挖去的 `p` 维体积是 `p` 次整数值多项式，其外壳是 `p-1` 次。

## 3. P019-X01 —— 维数由有限差分深度读出

`A_p` ball generating function 为

\[
\sum_{r\ge0}V_p(r)t^r
=\frac{H_p(t)}{(1-t)^{p+1}},
\qquad
H_p(t)=\sum_{j=0}^{p}\binom pj^2t^j.
\]

由 Vandermonde 恒等式

\[
H_p(1)=\sum_j\binom pj^2=\binom{2p}{p}.
\]

因此 `V_p(r)` 的最高次系数为

\[
\frac1{p!}\binom{2p}{p},
\]

从而

\[
\boxed{\nabla^pV_p(r)=\binom{2p}{p},\qquad \nabla^{p+1}V_p(r)=0.}
\]

于是可以定义一个完全内部的增长维数：

> `dim_growth` = 把球体积反复取有限差分，直到第一次归零之前的最后非零阶数。

对 `A_p`，`dim_growth=p`。

## 4. 真正的空腔表面：被切断的 primitive relations

仅数外壳点还不能代表挖走材料后真正暴露的关系。定义 cut boundary

\[
\partial_E B_p(r)
=\{(x,\alpha):x\in B_p(r),\ \alpha\in\Phi_p,\ x+\alpha\notin B_p(r)\},
\]

其中

\[
\Phi_p=\{e_i-e_j:i\ne j\},
\qquad |\Phi_p|=p(p+1).
\]

记总断边数

\[
E_p(r)=|\partial_EB_p(r)|.
\]

## 5. P019-X02 —— 单方向空腔边界严格等于上一维球

固定一个有向 primitive root

\[
\alpha=e_i-e_j.
\]

定义该方向穿出空腔的断边集合

\[
C_{p,\alpha}(r)=\{x\in B_p(r):x+\alpha\notin B_p(r)\}.
\]

则

\[
\boxed{|C_{p,\alpha}(r)|=V_{p-1}(r).}
\]

### 证明

令

\[
f(x)=\sum_{x_k>0}x_k=d_G(0,x).
\]

加上 `e_i-e_j` 后，`f` 增加 1 当且仅当

\[
x_i\ge0,\qquad x_j\le0.
\]

因此穿出球面的边必有

\[
f(x)=r,\qquad x_i\ge0,\qquad x_j\le0.
\]

把坐标 `i,j` 合并成一个坐标

\[
y_*=x_i+x_j,
\]

其余坐标保持不变。得到 `p` 个整数坐标且总和仍为零，所以 `y\in A_{p-1}`。

设

\[
a=x_i\ge0,\qquad b=-x_j\ge0.
\]

则 `y_*=a-b`，且合并后 graph distance 为

\[
d_G(0,y)=r-\min(a,b)\le r.
\]

故 `y\in B_{p-1}(r)`。

反过来，给定任意 `y\in B_{p-1}(r)`，令

\[
t=r-d_G(0,y)\ge0,
\qquad c=y_*.
\]

唯一拆分

\[
x_i=\max(c,0)+t,
\qquad
x_j=\min(c,0)-t
\]

恢复一个满足 `f(x)=r, x_i\ge0, x_j\le0` 的 `x`，且合并后恰回到 `y`。

因此两集合存在双射。∎

## 6. P019-X03 —— 总空腔边界的跨维恒等式

由于每一个 primitive 方向给出同样多的断边，而方向数为 `p(p+1)`，立即得到

\[
\boxed{E_p(r)=p(p+1)V_{p-1}(r).}
\]

低维为

\[
\begin{aligned}
E_1(r)&=2,\\
E_2(r)&=6(2r+1),\\
E_3(r)&=12(3r^2+3r+1),\\
E_4(r)&=20\frac{(2r+1)(5r^2+5r+3)}3.
\end{aligned}
\]

因此在 `A_3/FCC` 工作模型中

\[
\boxed{E_3(r)=12V_2(r).}
\]

这不是渐近关系：三维 graph-ball 空腔在每一个 primitive 方向上的关系投影，都严格是一份同半径二维 `A_2` ball；12 个 primitive directions 给出总断边数。

## 7. 递归降维链

对一个方向做坐标合并使

\[
A_p\to A_{p-1}.
\]

继续选择兼容 primitive direction 并重复合并：

\[
B_p(r)\to B_{p-1}(r)\to\cdots\to B_1(r)\to B_0(r).
\]

其中规定

\[
V_0(r)=1.
\]

所以同一个空腔有第二个内部维数判据：

> `dim_contract` = 需要多少次 primitive coordinate contraction 才把球降成单点。

对 `A_p`，`dim_contract=p`。

于是当前得到

\[
\boxed{dim_{growth}=dim_{contract}=p.}
\]

维数不再只能由“写了多少个坐标”声明，而可由两个独立的离散操作读出。

## 8. 与 finite-precision radial ball 的对照

若改用

\[
q_p(x)=\frac12\sum_i x_i^2,
\qquad D_p(x)=R_2(q_p(x))
\]

定义径向精度球，则沿 primitive root

\[
\alpha=e_i-e_j
\]

有

\[
q_p(x+\alpha)-q_p(x)=x_i-x_j+1.
\]

这不再是位置无关的常数。因此 radial cavity 的 primitive cut boundary 不满足简单的

\[
E_p(r)=p(p+1)V_{p-1}(r)
\]

形式。

直接整数枚举已经确认：graph-ball 恒等式在 `p=1..5`、多个半径上成立；相同公式对 collapsed-radial ball 失败。

这揭示一个真实张力：

1. graph ball 提供极强的跨维递归与关系投影一致性，但其宏观形状属于有限方向 growth form；
2. collapsed-radial ball 更强调径向均衡，却出现壳层算术振荡与位置相关的穿界代价；
3. P019 后续不应预设二者之一自动拥有全部物理意义，而应寻找 `relation structure + radial precision` 的统一接口。

## 9. 当前解释

本补充最重要的结构发现是：

\[
\boxed{
\text{p-dimensional excavation surface relation}
=
\text{coordination factor}
\times
\text{complete (p-1)-dimensional ball}
}
\]

对 `A_p` graph balls 这是精确整数恒等式。

它与连续几何中“边界降一维”的直觉相似，但这里没有把连续面积、角度、微分或实数半径作为原语。降维是由 primitive relation 的坐标合并双射直接产生。

## 10. 下一步

1. 将 X02/X03 形式化进 Lean，优先证明固定 root direction 的双射；
2. 把 cut boundary 实现为 reference operation，并进行 `p<=6` 的枚举回归；
3. 研究 repeated contraction 是否产生自然的 face/incidence complex，而不是仅有计数链；
4. 对 radial ball 构造对应的 direction-dependent boundary kernel，判断是否可由 `K_m(s,E)` 精确递推；
5. 比较 graph cavity 与 radial cavity 的有限精度各向同性指标；
6. 检索 edge-isoperimetry、root-polytope projection / lattice growth prior art，本文暂不作原创优先性声明。
