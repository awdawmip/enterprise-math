# P019 —— 离散黑洞视界：整数精度、因果壳层与边界计数

状态：`ACTIVE RESEARCH NOTE / PHYSICAL INTERPRETATION TESTING`  
Issue：`#46`  
范围：Schwarzschild 型径向因果结构的整数重写；有限精度视界盆地；P018 precision 接口；P012 型内禀壳层；P011 fiber 接口  
依赖：P007 离散除法、P011 collision spectrum、P012 内禀离散几何、P018 有限精度证明演算  
纪律：本文证明的整数命题与“自然中的黑洞真的由该模型描述”是两类不同结论。后者仍是物理假说。

## 0. 本阶段结论

本阶段得到九个数学结论和两个明确反例/边界：

1. Schwarzschild 核心比值可以重写为整数 precision observation
   `q_lambda(n;h)=floor(lambda |n-h|/n)`；
2. 当 `lambda | mu` 时，高精度 observation 精确投影到低精度 observation；
3. `q_lambda=0` 的视界 fiber 是一个可写出端点的有限整数区间；
4. 该零 fiber 随数值 precision 增大而嵌套收缩，并且在 `lambda>=h+1` 时恰好成为 `{h}`；
5. 用平方 precision `lambda=sigma^2` 再施加整数平方根，得到离散外部钟速壳层；某些钟速层可以完全为空；
6. 在已解析视界上，一个只记录 primitive outward direction 的整数更新具有严格的 `外部向外 / 视界固定 / 内部向内 / 中心吸收` 四段相图；
7. 标准轴 `Z^d` 的 L1 壳层可由一维核重复卷积得到，并有精确闭式；
8. 在 `d=3` 基准几何中，resolved horizon 壳层基数为 `4h^2+2`，outgoing shell expansion 在外/界/内分别为正/零/负；
9. 视界零 fiber 的 cardinality 同时是一个 P018 ambiguity multiplicity，并给出 P011 collision spectrum 的局部二项式贡献；但 precision ambiguity 与 forward-time history merging 必须严格区分。

两个反例/边界是：

- `mu>lambda` 并不足以保证完整 observation partition refinement；整除链才给出规范 projection；
- 离散钟速不一定逐级出现，`h=1,sigma=3` 时 `clock=1` 整层为空。

## 1. 外部连续理论只作为匹配目标

Schwarzschild 外部常用无量纲因子

\[
f(r)=1-\frac{r_s}{r}=\frac{r-r_s}{r}.
\]

在 ingoing Eddington–Finkelstein 型坐标中，径向部分可以写成不要求 `1/f` 的 horizon-regular 形式；在常见 `c=1` 约定下，径向 outgoing null branch 的符号结构由 `f` 控制：外部为正、视界为零、内部为负。

P019 不把该连续表达作为内部定义。它只把下面三个外部结构当成重建目标：

1. `r=r_s` 是因果相位边界；
2. horizon-regular 表示不需要把 `1/f` 的 Schwarzschild 坐标发散当成物理无穷大；
3. 三维 Schwarzschild 黑洞的经典/半经典边界量具有面积型二次尺度。

外部来源尚未写入 `sources.json`；在 source-registry gate 完成前，本文件保持 Draft/Research Note 性质。候选主来源见第 14 节。

## 2. 整数径向状态与一般 precision observation

固定一个有类型的长度单位，把正径向状态写成

\[
n\in\mathbb N_{>0},
\]

把 Schwarzschild 型边界状态写成

\[
h\in\mathbb N_{>0}.
\]

这里暂不规定 `h` 如何由质量、`G`、`c` 与单位尺度得到；那是后续量纲校准问题。

对整数 precision

\[
\lambda\in\mathbb N_{>0},
\]

定义

\[
\boxed{
q_\lambda(n;h)
=
Q_n\!\left(\lambda |n-h|\right)
=
\left\lfloor\frac{\lambda |n-h|}{n}\right\rfloor.
}
\]

方向不混进非负幅度，另记

\[
\epsilon(n;h)=\operatorname{sgn}(n-h).
\]

需要带方向时使用

\[
F_\lambda(n;h)=\epsilon(n;h)q_\lambda(n;h).
\]

内部 primitive 是整数乘法、绝对值、次序与 P007 型整数商；不保留隐藏分数。

## 3. P019-T01 —— 整除 precision 的精确 projection

状态：`PROVED`

若

\[
\lambda\mid\mu,
\qquad
r=\mu/\lambda,
\]

则对任意 `n,h>0`：

\[
\boxed{
q_\mu(n;h)//r
=
q_\lambda(n;h).
}
\]

### 证明

令

\[
A=\lambda |n-h|,
\qquad
q=q_\lambda(n;h).
\]

整数商定义给出

\[
nq\le A<n(q+1).
\]

乘以正整数 `r`：

\[
n(rq)\le rA<n(rq+r).
\]

而 `rA=\mu|n-h|`，所以

\[
rq
\le
q_\mu(n;h)
<
rq+r.
\]

因此

\[
q_\mu(n;h)//r=q.
\]

即得。∎

这使 `q_lambda` 在 precision divisibility chain 上直接满足 P018 的相容 forgetting-map 结构：

\[
O_\lambda
=
\pi_{\mu\to\lambda}\circ O_\mu,
\qquad
\pi_{\mu\to\lambda}(x)=x//(\mu/\lambda).
\]

所以这里不是仅仅借用“精度”一词；它确实进入 P018 已证明的 finite observation / partition framework。

## 4. P019-C01 —— 数值更大的 precision 不自动意味着 partition refinement

状态：`COUNTEREXAMPLE`

不能把 `mu>lambda` 直接升级为 P018 refinement。

取

\[
h=1,
\qquad
\lambda=4,
\qquad
\mu=9,
\qquad
n_1=3,
\qquad
n_2=4.
\]

则

\[
q_4(3;1)=2,
\qquad
q_4(4;1)=3,
\]

但

\[
q_9(3;1)=q_9(4;1)=6.
\]

因此 fine-looking 数值 `9` 反而合并了在 `4` 下可区分的两个 observation value。不存在由 `q_9` 的 image 到 `q_4` 的单值 projection 能同时恢复这两个状态。

所以必须区分：

- **数值 precision order** `lambda<=mu`；
- **P018 partition refinement order**；
- **整除 precision chain** `lambda|mu`。

T01 只对第三种给出完整 observation refinement。

## 5. P019-T02 —— 零可分辨视界 fiber 的精确区间

状态：`PROVED`

对

\[
\lambda\ge2,
\]

定义

\[
H_\lambda(h)
=
\{n>0:q_\lambda(n;h)=0\}.
\]

整数商为零当且仅当

\[
\lambda |n-h|<n.
\]

分别处理 `n<h` 与 `n>h`，得到同一个开区间条件：

\[
\boxed{
\frac{\lambda h}{\lambda+1}
<
n
<
\frac{\lambda h}{\lambda-1}.
}
\]

不把分数作为内部状态时，端点直接写成整数：

\[
\boxed{
L_\lambda(h)
=
(\lambda h)//(\lambda+1)+1,
}
\]

\[
\boxed{
U_\lambda(h)
=
(\lambda h-1)//(\lambda-1).
}
\]

因此

\[
\boxed{
H_\lambda(h)
=
\{L_\lambda(h),\ldots,U_\lambda(h)\}.
}
\]

其 radial fiber multiplicity 为

\[
\boxed{
W_\lambda(h)
=U_\lambda(h)-L_\lambda(h)+1.
}
\]

它是一个真实有限整数 fiber，而不是“无限精确视界附近的误差带”。

## 6. P019-T03 —— 零 fiber 的普通单调嵌套与精确 singleton 阈值

状态：`PROVED`

若

\[
2\le\lambda\le\mu,
\]

则

\[
\boxed{
H_\mu(h)\subseteq H_\lambda(h).
}
\]

证明只需注意

\[
\mu|n-h|<n
\Longrightarrow
\lambda|n-h|<n.
\]

这里的 zero-fiber nesting 只使用数值次序，不要求 `lambda|mu`。但它只说明**零 fiber** 收缩，不能替代 C01 对完整 partition refinement 的反例。

更强地：

\[
\boxed{
H_\lambda(h)=\{h\}
\iff
\lambda\ge h+1.
}
\]

### 证明要点

`h+1` 是最近的外侧整数状态。它不再落入零 fiber 当且仅当

\[
\lambda|(h+1)-h|\ge h+1,
\]

即

\[
\lambda\ge h+1.
\]

该条件也自动排除最近内侧 `h-1`，其余状态离 `h` 更远。反向若 `lambda<h+1`，则 `h+1` 仍与 `h` 同属零 fiber。∎

因此“视界由厚盆地解析为一个唯一壳层”不是极限语言，而存在一个有限整数终点：

\[
\boxed{\lambda_*=h+1.}
\]

## 7. P019-T04 —— 平方 precision 下的离散外部钟速壳层

状态：`PROVED`

为了匹配外部 `sqrt(f)` 的结构，选平方 precision

\[
\lambda=\sigma^2,
\qquad
\sigma\ge2,
\]

并只在静态外部 `n>=h` 定义

\[
\boxed{
K_\sigma(n;h)
=
R_2\!\left(q_{\sigma^2}(n;h)\right).
}
\]

由整数根刻画：

\[
K_\sigma(n;h)=k
\]

当且仅当

\[
\boxed{
k^2n
\le
\sigma^2(n-h)
<
(k+1)^2n.
}
\]

对

\[
0\le k\le\sigma-2,
\]

候选壳层端点为

\[
L_k
=
\left\lceil
\frac{\sigma^2h}{\sigma^2-k^2}
\right\rceil,
\]

\[
U_k
=
\left\lceil
\frac{\sigma^2h}{\sigma^2-(k+1)^2}
\right\rceil-1.
\]

内部实现只使用正整数 ceiling division。

若

\[
L_k>U_k,
\]

则该 clock level **完全为空**。

最外层 `k=sigma-1` 从

\[
L_{\sigma-1}
=
\left\lceil
\frac{\sigma^2h}{2\sigma-1}
\right\rceil
\]

开始并延伸到任意大的有限 `n`。

对任意有限 `n>=h`：

\[
q_{\sigma^2}(n;h)<\sigma^2,
\]

故

\[
\boxed{K_\sigma(n;h)<\sigma.}
\]

所以“满速状态 `sigma`”不会在有限半径上出现；这里不需要引入 `n->infinity` 作为内部完成对象。

## 8. P019-C02 —— Clock level 可以跳级

状态：`COUNTEREXAMPLE TO CONTIGUOUS-CLOCK ASSUMPTION`

取

\[
h=1,
\qquad
\sigma=3.
\]

则

\[
K_3(1;1)=0,
\]

而

\[
q_9(2;1)=4,
\qquad
K_3(2;1)=2.
\]

直接从 `0` 跳到 `2`。

`k=1` 的候选区间满足

\[
L_1=2,
\qquad
U_1=1,
\]

因此为空。

这不是数值误差；它是“先做整数 quotient basin，再做整数 root basin”复合后真实出现的层级缺口。

## 9. P019-T05 —— Resolved horizon 的 primitive outgoing causal phase

状态：`PROVED INSIDE THE MODEL`

定义 primitive outgoing step

\[
s_\lambda(n;h)
=
\begin{cases}
+1,&q_\lambda(n;h)>0\text{ 且 }n>h,\\
0,&q_\lambda(n;h)=0,\\
-1,&q_\lambda(n;h)>0\text{ 且 }0<n<h,\\
0,&n=0.
\end{cases}
\]

并令

\[
U_\lambda(n;h)=n+s_\lambda(n;h).
\]

当

\[
\lambda\ge h+1,
\]

T03 给出唯一零状态 `h`，于是：

\[
\boxed{
n>h\Rightarrow U_\lambda(n)=n+1,
}
\]

\[
\boxed{
n=h\Rightarrow U_\lambda(n)=h,
}
\]

\[
\boxed{
0<n<h\Rightarrow U_\lambda(n)=n-1,
}
\]

并按定义

\[
\boxed{U_\lambda(0)=0.}
\]

所以：

- 外部 primitive outgoing direction 增大半径；
- resolved horizon 是固定壳层；
- 内部即使取“outgoing”分支，未来步也严格减小半径；
- 任意内部状态 `n` 在恰好 `n` 个 primitive step 后到达 `0`。

这与 Eddington–Finkelstein radial null branch 的**符号结构**对应，但 P019 当前只重建了方向相位，不声称重建了完整 GR null geodesic、affine parameter 或局部光速。

## 10. P019-T06 —— `Z^d` 标准轴 L1 壳层由一维核生成

状态：`PROVED`

在 P012 型标准轴 `Z^d` benchmark 中，以 primitive axis adjacency 定义 L1 半径。

记精确半径 `r` 的状态数为 `S_d(r)`。

对 `r=0`：

\[
S_d(0)=1.
\]

对 `r>=1`：

\[
\boxed{
S_d(r)
=
\sum_{j=1}^{\min(d,r)}
2^j
\binom dj
\binom{r-1}{j-1}.
}
\]

### 组合证明

若一个点恰有 `j` 个非零坐标：

1. 从 `d` 个坐标中选择 `j` 个：`binom(d,j)`；
2. 每个非零坐标选择正负号：`2^j`；
3. 把总 L1 半径 `r` 分成 `j` 个正整数：`binom(r-1,j-1)`。

对所有可能 `j` 求和即得。∎

等价地，一维壳层核

\[
a_1(0)=1,
\qquad
a_1(r)=2\ (r>0)
\]

的普通生成函数为

\[
A_1(z)=\frac{1+z}{1-z},
\]

而

\[
\boxed{A_d(z)=A_1(z)^d.}
\]

所以 P019 在这里精确实现了当前“高维由低维核重复卷积生成”的维度提升路线。

## 11. P019-T07 —— 三维壳层、闭球与 outgoing expansion 三段符号

状态：`PROVED`

把 T06 代入 `d=3`，对 `r>=1`：

\[
\boxed{S_3(r)=4r^2+2.}
\]

闭球状态数为

\[
\boxed{
V_3(r)
=
\frac{4r^3+6r^2+8r+3}{3},
}
\]

右侧分子总可被 `3` 整除；内部实现使用整数除法。

定义 outgoing shell expansion

\[
\Xi_{\lambda,d}(n;h)
=
S_d(U_\lambda(n;h))-S_d(n).
\]

在 `d=3` 且 `lambda>=h+1` 时：

### 外部 `n>h`

\[
\Xi
=
S_3(n+1)-S_3(n)
=
8n+4
>0.
\]

### 视界 `n=h`

\[
\boxed{\Xi=0.}
\]

### 内部 `2<=n<h`

\[
\Xi
=
S_3(n-1)-S_3(n)
=
-8n+4
<0.
\]

对 `n=1`，因为 `S_3(0)=1`：

\[
\Xi=1-6=-5<0.
\]

因此整个 resolved 模型得到严格符号结构：

\[
\boxed{
\text{outside}:\Xi>0,
\qquad
\text{horizon}:\Xi=0,
\qquad
\text{inside}:\Xi<0.
}
\]

这与 trapped/marginal/untrapped 语言存在结构对应，但这里的 `Xi` 是**离散壳层 cardinality 差**，不是把连续 null expansion 标量偷偷取整。

## 12. P019-T08 —— Thick horizon boundary cardinality 与维度 `d-1` 次增长

状态：`PROVED / INTERPRETATION TESTING`

有限 precision 下，零视界不是一个壳层而是径向集合

\[
H_\lambda(h)=\{L_\lambda,\ldots,U_\lambda\}.
\]

在标准轴 L1 benchmark 中定义其总边界状态数

\[
\boxed{
A_{d,\lambda}(h)
=
\sum_{r=L_\lambda(h)}^{U_\lambda(h)}S_d(r).
}
\]

当 `lambda>=h+1`：

\[
\boxed{
A_{d,\lambda}(h)=S_d(h).
}
\]

由 T06，固定 `d` 时 `S_d(r)` 的最高次项来自 `j=d`：

\[
2^d\binom{r-1}{d-1}.
\]

所以 resolved boundary cardinality 具有 `r^(d-1)` 阶增长。

特别在 `d=3`：

\[
\boxed{A_{3,\lambda}(h)=4h^2+2.}
\]

这说明“边界自由度随半径平方增长”可以在一个完全整数、无 `pi` 的 L1 benchmark 中出现。

但必须保持边界：标准轴 `Z^3` 的壳层是八面体型而非连续旋转对称球面。`4h^2+2` 目前只能称为 **L1 benchmark boundary-state law**，不能称为物理 Schwarzschild 面积，也不能直接等同 Bekenstein–Hawking entropy。

真正值得保留的结构信号是指数：

\[
\boxed{\text{d-dimensional intrinsic shell cardinality has degree }d-1.}
\]

系数与精确对称性取决于最终选择的 primitive geometry。

## 13. P019-T09 —— 视界零 fiber 同时接入 P018 ambiguity 与 P011 collision spectrum

状态：`PROVED FINITE-FIBER STATEMENT`

对固定 `h,lambda>=2`，`q_lambda(h;h)=0`，所以 `h` 的 observation fiber 正好是

\[
[h]_\lambda=H_\lambda(h).
\]

因此 P018 ambiguity multiplicity 为

\[
\boxed{
A_\lambda(h)=W_\lambda(h).
}
\]

由 T03，随数值 `lambda` 增大：

\[
A_\lambda(h)
\]

单调不增；在有限 terminal threshold

\[
\lambda\ge h+1
\]

时

\[
\boxed{A_\lambda(h)=1.}
\]

若在一个包含完整零 fiber 的有限 radial domain 上，把 `q_lambda` 当作 observation map，则其输出 `0` 的 fiber 对 P011 第 `k` 阶 collision spectrum 的局部贡献是

\[
\boxed{
J_k^{(0)}
=
\binom{W_\lambda(h)}{k}.
}
\]

### 必须区分 precision 与 time

这里的 `W_lambda` 首先表示：**同一个 terminal radial state set 在当前 observation 下有多少状态仍不可区分。**

提高 precision 可以让该 ambiguity 下降。这是 P018 的 partition refinement 方向。

只有再加入额外物理假说：“自然真的把整个 `H_lambda` 通过一个 forward transition 合流成同一状态”，这个 fiber 才成为 P010/P011 意义上的历史合流并受 time-monotonicity 约束。

因此本阶段禁止写：

`precision zero fiber = physical entropy production`。

当前严格关系只能写：

\[
\boxed{
\text{same finite fiber combinatorics, different semantic direction.}
}
\]

## 14. Reciprocal、事件视界与中心边界

Schwarzschild diagonal coordinates 中出现 `1/f`。若只把外部对照的 `f` 映成 `q_lambda`，在 resolved horizon 有

\[
q_\lambda(h;h)=0.
\]

P007/P018 已经提醒：多对一 projection/quotient 的 coarse state 不拥有规范 inverse lift。因此在整数语义中，对该零状态直接要求 `1/q` 首先应被视为**未定义/非规范逆恢复请求**，而不是必须把某个“真实无穷数”加入基本状态。

这与 horizon-regular Eddington–Finkelstein 表示避免 `1/f` 的事实形成有价值的结构对应。

但还不能由此推出“Schwarzschild coordinate singularity 已被 P019 解释”。真正的 coordinate-invariant 重建仍是开放问题。

另外必须区分：

- `n=h>0`：`q_lambda` 定义良好，值为 `0`；
- `n=0`：原始定义要求除以 radial state `0`，不在定义域。

所以事件视界与中心在当前算术里是两类不同边界。

`U_lambda(0)=0` 只是为了给 primitive dynamics 加一个吸收边界条件，并没有消除原始 `q_lambda` 在中心未定义这一事实。

## 15. 物理反证与未完成门槛

P019 只有在通过下面的门槛后，才可能从“整数 toy model / structure match”升级为物理模型。

### F1 —— 旋转各向同性

标准轴 `Z^3/L1` 明显只有离散有限对称群。若把它直接当真实空间，会产生 preferred-direction signal。P016 已把这种效应列为重要 kill-test 类别。

所以 `4h^2+2` 目前是 benchmark，不是最终空间本体。

### F2 —— 坐标协变性

当前 `n,h` 是显式 radial coordinate state。必须给出不依赖特定 Schwarzschild/Eddington–Finkelstein 坐标选择的因果图或 invariant 定义，否则模型仍可能只是一次坐标重写。

### F3 —— 定量 redshift / geodesic recovery

T04 只构造了 discrete clock states，T05 只保留 outgoing sign。必须进一步给出可与 gravitational redshift、light propagation、orbit、lensing 等比较的无隐藏实数定量预言。

### F4 —— 质量—视界量纲接口

尚未定义

\[
M,G,c,\text{unit scale}
\longmapsto h.
\]

这一接口必须使用显式 typed units / integer scale，不得把 `2GM/c^2` 作为隐藏实数先算完再取整。

### F5 —— 自由落体穿越视界

外部 GR 中自由落体观察者不会在 horizon 遇到局部物理奇点。P019 必须能够表达这一点，否则“零 observation”可能错误地制造实体墙。

### F6 —— Einstein dynamics

本阶段没有重新推导 Einstein field equations，也没有给出离散曲率—能量关系。

### F7 —— 黑洞热力学

`S_3(h)=4h^2+2` 只证明 boundary state cardinality 的平方增长。没有证明：

- Bekenstein–Hawking 系数 `1/4`；
- Planck-area normalization；
- thermodynamic entropy；
- Hawking temperature；
- generalized second law。

### F8 —— 量子与信息问题

没有推导 Hawking radiation、Page curve、unitarity 或 information loss。

### F9 —— Charged / rotating / dynamical horizons

Schwarzschild 只是第一压力测试。Reissner–Nordström、Kerr、collapse/merger/dynamical horizon 必须单独检验；不能假定本结构自动延伸。

## 16. 外部来源候选与 source-registry gate

在 Draft 阶段已核实以下 primary/domain sources，进入 review-ready 前必须写入 `sources.json` 与 `lineage.json` 并使用正式 `SRC-*`：

1. Dennis Philipp, Volker Perlick, *Schwarzschild radial perturbations in Eddington-Finkelstein and Painlevé-Gullstrand coordinates*, arXiv:1503.08361 —— horizon-regular coordinate context；
2. Jacob D. Bekenstein, *Black Holes and Entropy*, Phys. Rev. D 7, 2333 (1973), DOI `10.1103/PhysRevD.7.2333` —— black-hole entropy/area historical benchmark；
3. S. W. Hawking, *Particle creation by black holes*, Commun. Math. Phys. 43, 199–220 (1975), DOI `10.1007/BF02345020` —— Hawking radiation and generalized entropy benchmark。

这些来源只支持外部 GR/thermodynamics benchmark，不支持 Enterprise Math 的物理解释为真。

Source-registry status：`OPEN REVIEW-READINESS GATE`。

## 17. 本阶段 theorem / counterexample ledger

- `P019-T01`：divisible precision observation projection —— `PROVED`
- `P019-C01`：numeric precision increase need not refine the full partition —— `COUNTEREXAMPLE`
- `P019-T02`：exact zero-horizon fiber interval and width —— `PROVED`
- `P019-T03`：zero-fiber nesting and singleton threshold `lambda>=h+1` —— `PROVED`
- `P019-T04`：external integer clock-shell characterization —— `PROVED`
- `P019-C02`：clock levels can be skipped —— `COUNTEREXAMPLE`
- `P019-T05`：resolved primitive causal phase and finite interior absorption —— `PROVED INSIDE MODEL`
- `P019-T06`：general `Z^d` L1 shell count / convolution lift —— `PROVED`
- `P019-T07`：`Z^3` shell/ball formulas and expansion-sign phase —— `PROVED`
- `P019-T08`：finite-thickness boundary count and `d-1` degree law —— `PROVED`; physical interpretation `TESTING`
- `P019-T09`：horizon zero fiber as P018 ambiguity and local P011 collision contribution —— `PROVED FINITE-FIBER STATEMENT`

Executable checks：`src/enterprise_math/black_hole.py` 与 `tests/test_black_hole.py`。

## 18. 下一阶段

按优先级推进：

1. 完成 source registry / lineage，解除 review-readiness gate；
2. 把 T01–T09 中纯整数部分送入 Lean，优先 T01、T02、T03、T06；
3. 以 P018 product precision 研究 radial precision 与其他物理 precision axis 的组合；
4. 构造 coordinate-free causal graph 版本，把“horizon”定义为 outgoing reachability / expansion 的结构边界，而不是 radial coordinate 特例；
5. 用 Reissner–Nordström 的整数二次多项式作为第二压力测试，研究双 horizon、extremal 与无 horizon 三相；
6. 再进入 Kerr，重点检验旋转/各向同性是否直接击穿当前 primitive geometry；
7. 只有前述结构经受住压力测试后，才研究 boundary cardinality 与 P011 collision spectrum 是否能形成黑洞 entropy 的候选整数前体。

P019 当前不是黑洞理论的完成，而是第一次把“时间变慢—因果空间收敛—有限精度视界”从语言直觉压缩成一组可以逐条证明、逐条反驳、逐条做实验接口的整数命题。
