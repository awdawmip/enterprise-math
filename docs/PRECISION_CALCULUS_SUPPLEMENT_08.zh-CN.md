# P018 —— 有限精度证明演算：补充 08

状态：`ACTIVE RESEARCH NOTE`  
范围：伴随投影的 operation defect、carry cocycle、带符号 extension obstruction、mixed-radix precision atlas 与路径平坦性边界  
依赖：P005、P006、P008、P009、P018 第一至第八阶段（主线 T001–T70）  
纪律：群扩张、2-cocycle、coboundary、伴随、mixed-radix arithmetic、braid/coherence 均有成熟前人工作。本文研究这些结构与进取数论有限精度语义的精确接口，不把成熟数学本身据为项目原创。

## 1. 本阶段为什么不是另开支线

P018 已经证明：精度投影不是围绕隐藏实数真值的误差条，而是显式有限状态之间的多对一映射。P008 又证明，对整数尺度嵌入

\[
L_r(a)=ra
\]

与整数商

\[
Q_r(x)=x//r
\]

存在序伴随

\[
L_r\dashv Q_r.
\]

此前 carry、borrow、乘法 carry、幂 carry 被作为跨精度运算中的精确整数事件处理。

本阶段问一个更底层的问题：

> 当 projection 与 operation 不严格交换时，这种“不交换”究竟是偶然算术现象、坐标选择造成的伪影，还是不能被合法表示变换消掉的结构？

答案分成四层：

1. operation defect；
2. defect coherence；
3. representation-change / obstruction；
4. 多路径 precision atlas。

整个推进保留 P005/P006/P008/P009/P012/P017/P018 既有路线，不以新语言替换旧结果。

---

## 2. P018-T71 —— 加法左伴随使右伴随超加

状态：`PROVED / ESTABLISHED ORDER-THEORETIC PATTERN`

设 `A,B` 为有序交换幺半群，加法对序单调。设

\[
l:A\to B
\]

严格保持加法，并存在右伴随

\[
l\dashv u.
\]

则对任意 `x,y in B`，

\[
\boxed{u(x)+u(y)\le u(x+y).}
\]

### 证明

由伴随 counit：

\[
l(u(x))\le x,
\qquad
l(u(y))\le y.
\]

因此

\[
l(u(x)+u(y))
=l(u(x))+l(u(y))
\le x+y.
\]

再用

\[
l(a)\le b\iff a\le u(b)
\]

得到结论。∎

取 `l=L_r`、`u=Q_r`，立刻有

\[
\boxed{Q_r(x)+Q_r(y)\le Q_r(x+y).}
\]

所以整数 floor projection 的超加性不是孤立技巧，而是 P008 伴随结构在加入加法后自动产生的性质。

---

## 3. P018-T72 —— carry 是右伴随投影的精确加法 defect

状态：`PROVED`

固定 `m>=1`，定义

\[
Q_m(x)=x//m,
\qquad
\delta_m(x)=x\bmod m.
\]

写

\[
x=ma+u,
\qquad y=mb+v,
\qquad0\le u,v<m.
\]

定义

\[
\boxed{
\kappa_m(u,v)
=\left\lfloor\frac{u+v}{m}\right\rfloor
\in\{0,1\}.
}
\]

则

\[
\boxed{
Q_m(x+y)-Q_m(x)-Q_m(y)
=\kappa_m(u,v).
}
\]

因此 carry 不是“近似误差”，而是 coarse projection 偏离加法同态的**全部整数缺口**。

对 degree-`q` 精度对象，只需把 `m` 换成 `r^q`，同一结论成立。

---

## 4. P018-T73 —— 标准 carry 满足归一化 2-cocycle 恒等式

状态：`PROVED / PRIOR-ART INSTANCE`

令

\[
D_m=\{0,1,\ldots,m-1\},
\qquad
u\oplus v=(u+v)\bmod m.
\]

则

\[
\boxed{
\kappa_m(u,v)
+
\kappa_m(u\oplus v,w)
=
\kappa_m(v,w)
+
\kappa_m(u,v\oplus w).
}
\]

且

\[
\kappa_m(0,u)=\kappa_m(u,0)=0,
\qquad
\kappa_m(u,v)=\kappa_m(v,u).
\]

### 证明

分别按 `(u+v)+w` 与 `u+(v+w)` 做欧几里得分解。两边最终模 `m` 余数因模加法结合律相同；唯一分解迫使粗系数相同。∎

### 前人边界

carrying 与 2-cocycle / group extension 的联系属于成熟数学。Daniel C. Isaksen 的 *A Cohomological Viewpoint on Elementary School Arithmetic*（American Mathematical Monthly, 2002, DOI `10.1080/00029890.2002.11919915`）明确讨论这一观点。

因此本项目不主张“carry 是 cocycle”为原创。项目要研究的是：这一成熟结构与 P005/P008/P018 的有限精度本体组合后，哪些更一般的 precision defects 能被统一控制。

---

## 5. P018-T74 —— coarse + detail + carry 无损重建自然数加法

状态：`PROVED`

定义

\[
\Phi_m:\mathbb N\to\mathbb N\times D_m,
\qquad
\Phi_m(x)=(Q_m(x),\delta_m(x)).
\]

由欧几里得分解，`Phi_m` 为双射，逆为

\[
\Phi_m^{-1}(a,u)=ma+u.
\]

在 `N x D_m` 上定义 twisted addition：

\[
\boxed{
(a,u)\boxplus(b,v)
=\bigl(a+b+\kappa_m(u,v),\ u\oplus v\bigr).
}
\]

则

\[
\boxed{
\Phi_m(x+y)=\Phi_m(x)\boxplus\Phi_m(y).
}
\]

所以

\[
\boxed{
(\mathbb N,+)
\cong
(\mathbb N\times D_m,\boxplus).
}
\]

`boxplus` 的结合律正由 T73 的 cocycle 恒等式保证。

因此如果底层把状态拆成 coarse/detail 两层，carry 不是实现噪声；删除它会改变加法代数本身。

---

## 6. P018-C08 —— 强迫 coarse projection 成为严格加法同态会丢结构

状态：`COUNTEREXAMPLE / DESIGN WARNING`

任取 `m>1`，令

\[
x=1,
\qquad y=m-1.
\]

则

\[
Q_m(x)=Q_m(y)=0,
\]

但

\[
Q_m(x+y)=Q_m(m)=1.
\]

因此

\[
\boxed{
Q_m(x+y)\ne Q_m(x)+Q_m(y).
}
\]

所以未来的 precision algebra 不能把“所有 coarse projection 都必须严格保持 operation”设成公理。正确方向是保存 defect，并研究其 coherence 与可消除性。

---

## 7. P018-T75 —— 两级 precision chain 的 carry coherence

状态：`PROVED`

考虑两级 ratio `r,s>=1`。对 degree `q` 对象，记

\[
R=r^q,
\qquad S=s^q.
\]

任意 total detail 写成

\[
t_i=S u_i+v_i,
\qquad0\le u_i<R,
\qquad0\le v_i<S.
\]

定义低层 carry

\[
c_S=\kappa_S(v_1,v_2).
\]

则跨总 ratio `RS` 的直接 carry 满足

\[
\boxed{
\kappa_{RS}(t_1,t_2)
=
\left\lfloor
\frac{u_1+u_2+c_S}{R}
\right\rfloor.
}
\]

总余数满足

\[
\boxed{
(t_1+t_2)\bmod(RS)
=
S((u_1+u_2+c_S)\bmod R)
+((v_1+v_2)\bmod S).
}
\]

这说明 direct coarsening 与 staged coarsening 不矛盾：低层 carry 被作为显式整数输入搬运到上一层，再决定是否继续越界。

---

## 8. P018-T76 —— 带符号欧几里得精度分解

状态：`PROVED / ESTABLISHED`

固定 `m>=1`。对每个

\[
z\in\mathbb Z,
\]

存在唯一

\[
q_m(z)\in\mathbb Z,
\qquad
\rho_m(z)\in D_m
\]

使

\[
\boxed{z=mq_m(z)+\rho_m(z).}
\]

这里采用与非负 canonical remainder 配套的 Euclidean/floor quotient，而不是向零截断 quotient。

这与 P006 的纪律一致：带符号状态的 order / quotient convention 必须显式进入数学定义，不能由编程语言默认除法决定。

本构造与 P006 的 `orderRootOdd`、`magnitudeRoot`、`signedMagnitudeCollapse` 是不同维度的问题，不修改它们。

---

## 9. P018-T77 —— 同一个 carry 控制带符号加法 defect

状态：`PROVED`

对 `x,y in Z`，写

\[
x=mq_x+r_x,
\qquad y=mq_y+r_y,
\qquad0\le r_x,r_y<m.
\]

则

\[
\boxed{
q_m(x+y)
=q_m(x)+q_m(y)+\kappa_m(r_x,r_y),
}
\]

并且

\[
\boxed{
\rho_m(x+y)
=(r_x+r_y)\bmod m.
}
\]

所以 carry defect 不是 `N` 的边界现象；在正确 signed quotient 下原样延伸到 `Z`。

---

## 10. P018-T78 —— `Z` 的 coarse/detail/carry 形成 twisted group

状态：`PROVED`

定义

\[
\Phi_m^{\mathbb Z}(z)
=(q_m(z),\rho_m(z)).
\]

并继续使用

\[
(a,u)\boxplus(b,v)
=\bigl(a+b+\kappa_m(u,v),(u+v)\bmod m\bigr).
\]

则

\[
\boxed{
(\mathbb Z,+)
\cong
(\mathbb Z\times D_m,\boxplus)
}
\]

作为群成立。

逆元显式为：

\[
-(a,0)=(-a,0),
\]

而 `0<u<m` 时

\[
\boxed{
-(a,u)=(-a-1,m-u).
}
\]

因为 `u+(m-u)=m` 恰好产生一个 carry，抵消粗坐标的额外 `-1`。

这把 carry/borrow 放进同一个 signed extension algebra，而不是把 borrow 另当成数值误差。

---

## 11. P018-T79 —— carry 是标准 residue extension 的 section defect

状态：`PROVED / ESTABLISHED EXTENSION-THEORY INSTANCE`

考虑短正合列

\[
\boxed{
0
\longrightarrow\mathbb Z
\xrightarrow{\times m}
\mathbb Z
\xrightarrow{\rho}
\mathbb Z/m\mathbb Z
\longrightarrow0.
}
\]

取标准 section

\[
s([u])=u,
\qquad0\le u<m.
\]

section 一般不是群同态，并且

\[
\boxed{
s(u)+s(v)-s(u+v)
=m\kappa_m(u,v).
}
\]

因此

\[
\boxed{
\kappa_m(u,v)
=
\frac{s(u)+s(v)-s(u+v)}{m}.
}
\]

carry 的 cohomological 含义因此是：选定 detail representatives 后，section 偏离群同态的 kernel 坐标。

---

## 12. P018-T80 —— 换 section 只改变一个 coboundary

状态：`PROVED / PRIOR-ART COHOMOLOGY PATTERN`

若换成另一个 section

\[
s'(u)=s(u)+m h(u),
\]

则对应 defect

\[
\kappa'_m(u,v)
=
\frac{s'(u)+s'(v)-s'(u+v)}{m}
\]

满足

\[
\boxed{
\kappa'_m(u,v)
=
\kappa_m(u,v)
+h(u)+h(v)-h(u+v).
}
\]

所以具体 carry table 可以依赖 representation，但合法换 representation 的变化规律严格受控。

从这里开始，precision defect 必须区分：

1. coordinate-dependent defect；
2. change-of-representation law；
3. representation-invariant obstruction。

---

## 13. P018-T81 —— `m>1` 时 carry obstruction 不能全局 strictify

状态：`PROVED / ESTABLISHED GROUP-THEORETIC CONSEQUENCE`

当 `m>1` 时，

\[
0\to\mathbb Z\xrightarrow{\times m}\mathbb Z\to\mathbb Z/m\mathbb Z\to0
\]

不分裂。

### 初等证明

若分裂，则存在群同态 section

\[
s:\mathbb Z/m\mathbb Z\to\mathbb Z.
\]

于是 `s(1)` 应在加法群 `Z` 中具有阶 `m`。但 `Z` torsion-free，除 `0` 外没有有限阶元素，矛盾。∎

因此不存在任何 representatives 选择能让 carry cocycle 在所有输入上恒为零：

\[
\boxed{
\text{carry 可以换坐标，但不能被全局消灭。}
}
\]

这给出一个强底层筛选规则：

> 某个 precision defect 是否应进入基础，不先看公式是否漂亮，而先问它能否在所有合法 representation 下被 strictify；若不能，应寻找真正的 obstruction class。

---

## 14. P018-T82 —— 两级 mixed-radix detail chart 是双射

状态：`PROVED / ESTABLISHED ARITHMETIC`

定义

\[
D_n=\{0,1,\ldots,n-1\}.
\]

对 `r,s>=1` 与 `t in D_(rs)`，唯一有

\[
\boxed{t=su+v,}
\qquad
u\in D_r,
\quad v\in D_s.
\]

于是

\[
\boxed{
\chi_{r,s}:D_{rs}\to D_r\times D_s,
\qquad
\chi_{r,s}(t)=(t//s,t\bmod s)
}
\]

为双射，逆为

\[
\boxed{
\chi_{r,s}^{-1}(u,v)=su+v.
}
\]

这不是隐藏真值：`D_(rs)` 与 `(u,v)` 都是同一个显式有限 detail state 的不同坐标。

---

## 15. P018-T83 —— radix swap 是规范无损 chart transition

状态：`PROVED`

同一个 `t` 还可以按反向 radix 写成

\[
t=ru'+v',
\qquad u'\in D_s,
\quad v'\in D_r.
\]

定义

\[
\boxed{
\tau_{r,s}
=
\chi_{s,r}\circ\chi_{r,s}^{-1}.
}
\]

则

\[
\boxed{
\tau_{r,s}(u,v)
=
((su+v)//r,(su+v)\bmod r).
}
\]

且

\[
\boxed{
\tau_{s,r}\circ\tau_{r,s}
=id.
}
\]

因此两条 refinement route 的 detail 不需要逐坐标一致；它们可以是同一 finite fiber 上的两套整数 chart，只要 transition 可逆且精确。

---

## 16. P018-T84 —— 三因子 radix swap 满足 braid coherence

状态：`PROVED`

对

\[
(a,b,c)\in D_r\times D_s\times D_t,
\]

定义编码

\[
\boxed{N=st\,a+t\,b+c.}
\]

把 radix order `(r,s,t)` 变为 `(t,s,r)` 有两条相邻 swap 路径：

\[
(r,s,t)
\to(s,r,t)
\to(s,t,r)
\to(t,s,r),
\]

以及

\[
(r,s,t)
\to(r,t,s)
\to(t,r,s)
\to(t,s,r).
\]

严格有

\[
\boxed{
(\tau_{s,t}\times id_r)
\circ(id_s\times\tau_{r,t})
\circ(\tau_{r,s}\times id_t)
=
(id_t\times\tau_{r,s})
\circ(\tau_{r,t}\times id_s)
\circ(id_r\times\tau_{s,t}).
}
\]

证明只需注意每一步 swap 都保持整数 `N` 不变，而最终 radix order 相同；mixed-radix 唯一分解迫使终点坐标相同。∎

这把“不同精度分解路线应兼容”提升为严格 chart coherence。

---

## 17. P018-T85 —— P005 gcd/lcm 菱形拥有规范 detail atlas

状态：`PROVED`

令

\[
g=\gcd(a,b),
\qquad
\ell=\operatorname{lcm}(a,b),
\]

写

\[
a=gA,
\qquad b=gB.
\]

则

\[
\gcd(A,B)=1,
\qquad
\ell=gAB.
\]

固定从 `ell` 到 `g` 的 total detail

\[
t\in D_{AB}.
\]

路径

\[
\ell\to a\to g
\]

给出 chart

\[
\chi_{A,B}(t)=(t//B,t\bmod B),
\]

而

\[
\ell\to b\to g
\]

给出

\[
\chi_{B,A}(t)=(t//A,t\bmod A).
\]

二者由

\[
\boxed{
\tau_{A,B}
=
\chi_{B,A}\circ\chi_{A,B}^{-1}
}
\]

规范连接。

因此 P005 diamond 应分两层理解：

\[
\boxed{\text{coarse coordinate 严格交换；}}
\]

\[
\boxed{\text{detail coordinate 可不同，但由可逆 chart transition 精确连接。}}
\]

---

## 18. P018-T86 —— 加法 carry 在 canonical precision diamond 上 flat

状态：`PROVED`

固定 `r,s>=1` 与

\[
t_1,t_2\in D_{rs}.
\]

直接 product-radix carry 为

\[
\boxed{
K_{dir}
=\kappa_{rs}(t_1,t_2)
=\left\lfloor\frac{t_1+t_2}{rs}\right\rfloor.
}
\]

在 `(r,s)` chart 中写

\[
t_i=su_i+v_i.
\]

先有

\[
c_s=\kappa_s(v_1,v_2),
\]

再有

\[
K_{r,s}
=
\left\lfloor
\frac{u_1+u_2+c_s}{r}
\right\rfloor.
\]

由 T75，

\[
K_{r,s}=K_{dir}.
\]

换到 `(s,r)` chart 同理得到

\[
K_{s,r}=K_{dir}.
\]

故

\[
\boxed{
K_{r,s}=K_{s,r}=K_{dir}.
}
\]

局部 carry 在两条路线上的发生位置可以不同，但正确搬运到共同端点以后 defect 一致。

因此：

\[
\boxed{\text{defect 非零}\not\Rightarrow\text{path curvature 非零}.}
\]

---

## 19. P018-T87 —— canonical endpoint defect 的路径曲率自动为零

状态：`PROVED STRUCTURAL BOUNDARY`

考虑 compatible precision system，规范 projection 只依赖起终点，并满足所有 projection path 复合为同一个

\[
\pi_{\lambda\to\mu}.
\]

若 operation `F` 在两个端点定义，并定义

\[
D_F^{\lambda:\mu}(x)
=
\pi^{out}_{\lambda\to\mu}(F_\lambda(x))
-
F_\mu(\pi^{in}_{\lambda\to\mu}(x)),
\]

那么 `D_F^(lambda:mu)` 本身只依赖端点。

所以仅使用 canonical projections 的两条同起终点路径，其 endpoint-defect path difference 必为零。

### 结论

不能仅因局部 defect decomposition 不同就称其为“precision curvature”。那可能只是 chart dependence。

真正可能非零的 holonomy/path obstruction 至少需要：

1. 中间 operation ordering 不同，例如 collapse→project 与 project→collapse；
2. 非规范 lift/reconstruction；
3. operation 随路径改变；
4. 非平凡 defect transport rule。

这把真正的 path-dependence 研究从纯 P005 scale lattice 精确移动到 P009 已经揭示的 typed nonconfluence 与 operation/projection noncommutation。

---

## 20. 对 P008 的反馈：基础不是一次性加满，而是分层扩张

P008 的已证明结论保持不变：

\[
\boxed{
\text{partial order}
+\text{order embedding}
+\text{right adjoint}
}
\]

足以容纳当前 root / quotient / collapse 核心。

本阶段只在需要 operation 时增加第二层：

\[
\boxed{
\text{typed operation}
+\text{precision projection}
+\text{exact defect}
+\text{coherence}.
}
\]

再在需要跨 representation 判别结构真伪时增加：

\[
\boxed{
\text{representation change}
+\text{defect transformation law}
+\text{strictification obstruction}.
}
\]

不把更强结构强塞回 P008。

---

## 21. 对 P006/P009 的反馈：signed semantics 与 typed path 必须继续保留

P006 的不同 signed root semantics 不被本阶段合并。Euclidean signed quotient 是独立坐标层。

P009 的 scale label 也绝不能擦掉，因为：

- carry coherence 依赖具体 ratio；
- radix chart 依赖 factor order；
- 真正 path effect 依赖 operation event 在哪一种 typed scale 上发生。

合理状态至少需要显式保留 `(scale, value, degree)` 或等价类型信息。

---

## 22. 对 P012 的反馈：保留 primitive graph geometry，增加 representation-invariant derived geometry

P012 已证明 primitive adjacency 生成的 shortest-path 自然数距离可形成内生整数度量，这条路线保持为稳固基线。

并行增加：

1. fiber/quotient geometry；
2. exact lattice lift 作为 proof representation；
3. derived geometry 的 chart-change invariance 检验。

任何新 distance 即使整数值，也仍必须证明 metric axioms；不能因“整数化”自动获得几何合法性。

---

## 23. 对 P017 的反馈：保留全部局部路线，同时寻找全局 invariant certificate

P017 的 involution、carry、shell、half-scale、factor precision、threshold-complex 等路线全部保留。

新的问题是：不同 decomposition/anchor/precision axis 是否可以被组织成 chart family？若可以，则寻找：

- change-of-chart law；
- boundary/coboundary correction；
- chart-invariant total certificate；
- 真正不能 strictify 的 obstruction。

因此不再要求每个局部 shell 都有好符号；局部负项可能只是一个 representation 下的分解结果。

---

## 24. Representation switch 的正式纪律

允许

\[
\boxed{
\text{finite-state problem}
\xrightarrow{\text{faithful representation}}
\text{external mathematical language}
\xrightarrow{\text{proof}}
\text{finite-state theorem}.
}
\]

可用 group cohomology、category/adjunction、algebraic geometry、harmonic/spectral methods、convex duality、topology、lattice/coding theory、analysis 等证明语言，但必须：

1. representation map 明确；
2. 所需 faithful/injective/equivalence 性质被证明；
3. 结论能翻回原有限状态；
4. 不把证明空间中的连续体自动升级为自然本体。

---

## 25. 候选底层骨架：Defect-Enriched Precision Atlas

状态：`RESEARCH SYNTHESIS / NOT FROZEN`

当前出现的最小候选分层是：

### Layer 0 —— Order-adjoint core

序、embedding、right adjoint、interior/collapse。

### Layer 1 —— Defect-enriched operations

operation 不必与 projection 严格交换；保存 exact finite defect 与 composition/coherence law。

### Layer 2 —— Defect equivalence / obstruction

区分 coordinate-dependent defect、合法 representation change、coboundary-like 变化与不能 strictify 的 obstruction。

### Layer 3 —— Precision atlas / path coherence

同一 finite detail fiber 允许多个 chart；要求 transition 可逆并满足 composition/braid coherence；区分 chart dependence 与真正 operation-induced path dependence。

### Layer 4 —— Proof/time layers

继续接 P018 predicate certificate/adaptive precision 与 P010/P018 的时间 partition coarsening；目前不宣称时间与精度之间已有 categorical duality。

因此当前候选骨架是：

\[
\boxed{
\text{typed finite states}
+\text{adjoint projections}
+\text{finite detail fibers}
+\text{precision atlas}
+\text{exact defects}
+\text{coherence}
+\text{obstructions}
+\text{proof/time layers}.
}
\]

仍不封板。

---

## 26. 可执行压力测试与形式化入口

本阶段新增/计划接入：

- `EnterpriseMath/Precision/Carry.lean`
- `src/enterprise_math/precision_radix.py`
- `tests/test_precision_radix.py`

Lean 优先验证：

1. T72 additive carry defect；
2. T73 carry cocycle；
3. 后续再形式化 T74/T75 与 T82–T84。

Python 小有限域穷举验证：

1. mixed-radix split/join 互逆；
2. radix swap 互逆；
3. 三因子 braid 两路一致；
4. staged carry = direct product-radix carry；
5. swapped diamond 的 endpoint carry 一致。

计算用于反例搜索与实现核验，不替代理论证明。

---

## 27. 下一阶段开放问题

### P018-Q79 —— 哪些 operation defects 真正形成 cocycle？

加法已经成立。乘法、幂、collapse/refinement defect 不预设答案；寻找正确 coefficient object 或明确反例。

### P018-Q80 —— 最弱的 adjoint + operation 结构

继续削弱 T71 假设，确定交换性、单位元、全加法、antisymmetry 哪些真正必要。

### P018-Q81 —— signed carry 的 Lean 形式化

严格核对 mathlib 的整数 Euclidean division convention，再形式化 T76–T81。

### P018-Q82 —— finite precision atlas 的抽象最小结构

把 `D_(rs) <-> D_r x D_s` 推广为一般 finite fiber chart，不预设必须是整数乘法分解。

### P018-Q83 —— radix braid 的 Lean 形式化

形式化 T82–T84。

### P018-Q84 —— operation-scheduling holonomy

从最小 noncommuting 例子开始：比较 collapse→project 与 project→collapse，在共同 typed endpoint 上定义 path effect，并研究其 chart-change law。

### P018-Q85 —— global certificate 反哺 P017

尝试把 carry、Möbius shell、half-scale、factor precision 的不同分解组织成 atlas；若失败，明确哪些路线不是坐标差异而是真结构差异。

---

## 28. 当前结论

本阶段得到的最重要连续链不是某个单独公式，而是：

\[
\boxed{
\text{right-adjoint laxity}
\to
\text{exact carry defect}
\to
\text{2-cocycle coherence}
\to
\text{section/coboundary change}
\to
\text{non-splitting obstruction}
\to
\text{mixed-radix atlas}
\to
\text{path-flatness boundary}.
}
\]

这给底层逻辑提供了一个比“所有运算都应严格交换”更自然的候选原则：

> **有限精度底层不必消灭 defect；它应保存 defect、控制其换表示规律，并把只有在所有合法 chart 下仍不能消除的差异提升为真正结构。**

同时得到一个防止走偏的负结论：

\[
\boxed{
\text{纯 canonical precision projection 本身是 path-flat 的。}
}
\]

所以真正值得寻找的非零 holonomy 必须来自 operation/projection noncommutation、非规范 lift 或其他真实的路径依赖，而不能仅从“不同路线产生不同局部坐标”中人为制造。