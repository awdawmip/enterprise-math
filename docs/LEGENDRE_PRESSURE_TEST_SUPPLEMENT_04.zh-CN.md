# Legendre 压力测试——补充 04

状态：`ACTIVE RESEARCH NOTE`  
范围：从 `2k` 除数阈值精确 Alexander 对偶下降到至多 `floor((k+1)/2)` 的阈值，并建立双侧整数根过滤。  
结论纪律：**本文不声称证明了 Legendre 猜想。**

## 1. 为什么还需要一次对偶

补充 02–03 已经把大 Möbius 尾部改写成有限乘法阈值复形

\[
K(G,T)=\left\{F:\prod_{p\in F}p\le T\right\}
\]

的约化 Euler 特征，并把不能消去的项识别为成熟 quota-complex 理论中的 shell。

但最前沿的负层——1 维 shell——仍然存在。平方盆地比任意 quota complex 多出一个条件：每一个超过 cutoff 的除数，都真实地整除某个状态

\[
k^2<n<(k+1)^2.
\]

本补充利用 combinatorial Alexander duality 提取这部分额外结构。

Alexander 组合对偶本身属于成熟数学。Björner 与 Tancer 给出了有限单纯复形上的标准形式：

\[
\widetilde H_i(K)
\cong
\widetilde H^{|V|-i-3}(K^*).
\]

[SRC-BJORNER-TANCER-2009-ALEXANDER]

项目真正要问的是：当阈值来自平方盆地时，这个 Alexander dual 会精确变成什么。

## 2. L016 —— 大除数余因子下降

状态：`PROVED`

设

\[
k^2<n<(k+1)^2
\]

且 \(b\mid n\)，同时

\[
b>2k.
\]

写成

\[
n=bh.
\]

由于 \(n\le k^2+2k\) 且 \(b\ge2k+1\)，有

\[
h
\le
\left\lfloor
\frac{k^2+2k}{2k+1}
\right\rfloor.
\]

右侧整数商可以按 \(k\) 的奇偶精确化简为

\[
\left\lfloor
\frac{k^2+2k}{2k+1}
\right\rfloor
=
\left\lfloor\frac{k+1}{2}\right\rfloor.
\]

所以

\[
\boxed{
h\le\left\lfloor\frac{k+1}{2}\right\rfloor.}
\]

也就是说，大区域 \(b>2k\) 中的每一个真实除数项，都自带一个已经下降到“根尺度一半以内”的真实整数余因子。

### 截断边的余因子窗口

如果该除数还是 L010 的 shell 边：

\[
b=pc,
\qquad
c\le2k<pc,
\]

则

\[
b=pc\le2kp.
\]

又因 \(n=bh>k^2\)，可得

\[
2kph>k^2.
\]

转成整数关系即

\[
\boxed{2ph\ge k+1.}
\]

因此，每一条 cutoff shell 边都同时带有一个余因子窗口：

\[
\boxed{
2ph\ge k+1,
\qquad
h\le\left\lfloor\frac{k+1}{2}\right\rfloor.
}
\]

这一关系不是一般 threshold complex 自带的；它同时使用了乘法 shell 边和状态位于 \(k^2\) 正上方这一事实。

## 3. L017 —— 精确乘法 Alexander 对偶阈值

状态：`PROVED SPECIALIZATION OF ESTABLISHED ALEXANDER DUALITY`

令

\[
G=\prod_{p\in\mathcal P}p>T\ge1
\]

为平方自由数，并定义

\[
K(G,T)
=
\left\{F\subseteq\mathcal P:
\prod_{p\in F}p\le T
\right\}.
\]

其 Alexander dual 为

\[
K(G,T)^*
=
\{F:\mathcal P\setminus F\notin K(G,T)\}.
\]

对某一面记

\[
d=\prod_{p\in F}p.
\]

其补集乘积就是 \(G/d\)。因此

\[
F\in K(G,T)^*
\iff
\frac{G}{d}>T
\iff
G>Td.
\]

由于全部量都是整数，这恰好等价于

\[
d\le\left\lfloor\frac{G-1}{T}\right\rfloor.
\]

定义

\[
T^*(G,T)
=
\left\lfloor\frac{G-1}{T}\right\rfloor.
\]

于是得到

\[
\boxed{
K(G,T)^*=K(G,T^*).
}
\]

所以 Alexander dual 并没有离开有限乘法阈值复形这一类别。

### Möbius 尾和递推

令

\[
r=|\mathcal P|.
\]

组合 Alexander 对偶给出

\[
\widetilde\chi(K(G,T))
=
(-1)^{r-3}
\widetilde\chi(K(G,T^*)).
\]

利用 L013，把两边约化 Euler 特征都换回 Möbius 尾和：

\[
\boxed{
\sum_{\substack{d\mid G\\d>T}}\mu(d)
=
(-1)^{r-3}
\sum_{\substack{d\mid G\\d>T^*}}\mu(d).
}
\]

同一个恒等式也可以直接通过补除数 \(d\leftrightarrow G/d\) 验证；拓扑形式额外解释了为什么同调维数会发生反转。

## 4. L018 —— 平方盆地半尺度 Alexander 下降

状态：`PROVED`

现在让 \(G\) 是真实状态

\[
n\in(k^2,(k+1)^2)
\]

的横向小素数平方自由支撑，并假定 \(G>2k\)，使大尾部非平凡。取

\[
T=2k.
\]

由于 \(G\) 只是 \(n\) 的若干不同素因子的乘积，因此

\[
G\le n\le k^2+2k.
\]

所以

\[
T^*
=
\left\lfloor\frac{G-1}{2k}\right\rfloor
\le
\left\lfloor\frac{k^2+2k-1}{2k}\right\rfloor.
\]

右侧精确等于

\[
\left\lfloor\frac{k+1}{2}\right\rfloor.
\]

因此

\[
\boxed{
T^*\le\left\lfloor\frac{k+1}{2}\right\rfloor.
}
\]

于是，原本发生在精确大除数阈值 \(2k\) 上的 parity 问题，经 Alexander dual 后被送到一个不超过“根尺度一半”的阈值。

这不是渐近意义上的尺度缩小，而是精确有限整数不等式。

## 5. L019 —— 同调的双侧整数根夹逼

状态：`PROVED FROM ESTABLISHED DUALITY + L015`

令 \(p\) 为支撑中最小素数，令

\[
r=|\mathcal P|,
\]

并假设

\[
\widetilde\beta_s(K(G,T))>0.
\]

L015 已经给出原 shell 的根约束：

\[
p\le R_{s+1}(T).
\]

组合 Alexander 对偶把该同调送到

\[
s^*=r-s-3
\]

维的 \(K(G,T^*)\)。

若 \(s^*\ge0\)，则对偶复形在该维有非零 shell 同调，再次应用 L015 得

\[
p\le R_{s^*+1}(T^*)
=R_{r-s-2}(T^*).
\]

因此

\[
\boxed{
p\le
\min\left(
R_{s+1}(T),
R_{r-s-2}(T^*)
\right)
}
\]

只要 \(r-s-3\ge0\)。

在平方盆地中，L018 进一步给出

\[
\boxed{
p\le
R_{r-s-2}\!\left(
\left\lfloor\frac{k+1}{2}\right\rfloor
\right).
}
\]

这是第二套独立的整数根过滤：它来自“补集支撑”，而不是原 shell face 本身。

## 6. 最前沿的 1 维负层

当前最主要的负拓扑是

\[
s=1.
\]

如果横向支撑有 \(r\ge4\) 个不同素数，且 \(\beta_1>0\)，那么原 shell 给出

\[
\boxed{p\le R_2(2k)},
\]

同时对偶侧给出

\[
\boxed{p\le R_{r-3}(T^*)},
\]

其中

\[
T^*\le\left\lfloor\frac{k+1}{2}\right\rfloor.
\]

因此，支撑规模本身会不断强化对最小素数的约束：

- \(r=4\)：对偶侧只给出一次根/线性约束；
- \(r=5\)：\(p\le R_2(T^*)\)，即在半尺度上再次被平方根压缩；
- \(r=6\)：\(p\le R_3(T^*)\)；
- \(r=7\)：\(p\le R_4(T^*)\)；
- 依此类推。

换言之：

\[
\boxed{
\text{1 维负 shell}
+
\text{支撑越大}
\Longrightarrow
\text{最小素数被压进越低的根壳层}.
}
\]

这比 L015 的单侧根过滤更强。

## 7. 解释

当前 parity 问题已经有三种精确有限表示：

\[
\text{阈值 }2k\text{ 的大 Möbius 尾部}
\longleftrightarrow
\widetilde H_*(K(G,2k))
\longleftrightarrow
\widetilde H_*(K(G,T^*)),
\]

而且

\[
T^*\le\left\lfloor\frac{k+1}{2}\right\rfloor.
\]

第二个复形不是人为添加的辅助对象，而是第一个复形的精确 Alexander dual。L016 又说明，同样的“半尺度”在纯算术中正是每个大除数真实余因子的上界。

也就是说，拓扑对偶和平方盆地因子分解从两个方向描述的是同一次下降。

## 8. 这仍然没有证明什么

Alexander duality 保留信息，本身不可能把一个非零负 Euler 贡献凭空消灭。新杠杆来自平方盆地制造的**尺度不对称**：

\[
2k
\quad\longrightarrow\quad
T^*\le(k+1)/2.
\]

真正剩余的任务，是利用这个更小的对偶阈值，再结合 `根 = cutoff = k` 的自洽条件，证明一般 threshold complex 不成立的新符号、不等式、注入或递推。

下一步优先方向：

1. 分类原始 1 维负 shell 所对应的对偶复形；
2. 用双侧根夹逼证明大支撑负 shell 只能集中在极小的最小素数层；
3. 尝试通过半尺度对偶阈值递归汇总剩余小素数层；
4. 把对偶阈值/余因子状态继续连接到 \(b\le k\) 的小横向差异区。

## 9. 可执行验证

`src/enterprise_math/alexander_descent.py` 与 `tests/test_alexander_descent.py` 在有限范围内检查：

- 精确补阈值确为 \(T^*=\lfloor(G-1)/T\rfloor\)；
- Möbius 尾和满足 Alexander 对偶符号关系；
- shell Betti 秩落到对偶维数 \(r-s-3\)；
- 真实平方盆地支撑满足 \(T^*\le\lfloor(k+1)/2\rfloor\)；
- 每个真实 \(2k\) 以上除数的余因子都不超过该半尺度；
- shell 边余因子同时满足 \(2ph\ge k+1\)；
- 非零 shell 同调同时满足原侧和对偶侧整数根界。

组合 Alexander 对偶的一般定理属于已引用的前人工作；平方盆地半尺度专门化与本文给出的整数不等式均在本文中直接证明。
