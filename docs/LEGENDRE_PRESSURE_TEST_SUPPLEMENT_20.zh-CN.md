# Legendre 压力测试 — 补充 20

状态：`PROVED RESEARCH NOTE`  
范围：完整 lower-band exact-window / realized-shell root collision 分类，以及精确最小 repair  
依赖：P017 L054–L055、P023-S8 admissibility-filtered image separation、P023-S9 task-refinement repair calculus  
纪律：本补充证明的是 square-basin lower-band shell structure，不声称证明 Legendre 猜想。

## 1. 从最终不碰撞继续推进

L055 证明了一个强 envelope statement：从 `k>=9` 起，不同 lower-band **exact-window** root images 两两不交。真实 least-prime-shell images 是其子集，因此直接继承该结论。

进一步重读证明可以发现：其中排除 `r>=5` 的部分并未使用 `k>=9`，对 `(p,r)=(2,3)` 排除 `s>=8` 的部分也没有使用。因此整个家族里所有可能的 exact-window collision 都会被压缩到 7 个有限 `k`。

随后 realizability filter 会再删除这 3 个 surviving window collisions 中的一个。

## 2. 记号

对 prime `p<=k`，记 raw cofactor window

\[
W_p(k)=
\left[
\left\lfloor\frac{k^2}{p}\right\rfloor+1,
\left\lfloor\frac{k(k+2)}p\right\rfloor
\right]
\]

以及 exact-window root image

\[
G_p^{\rm win}(k)=\{R_2(q):q\in W_p(k)\}.
\]

真实 least-prime shell cofactor set 为

\[
Q_p^{\rm sh}(k)=
\{n/p:\ k^2<n<(k+1)^2,\ \operatorname{spf}(n)=p\},
\]

其 realized root image 为

\[
G_p^{\rm sh}(k)=\{R_2(q):q\in Q_p^{\rm sh}(k)\}.
\]

始终有

\[
G_p^{\rm sh}(k)\subseteq G_p^{\rm win}(k).
\]

## 3. L056-A —— exact-window root collisions 的完整分类

状态：`PROVED`。

对不同 lower-band primes `p<r`，

\[
G_p^{\rm win}(k)\cap G_r^{\rm win}(k)\ne\varnothing
\]

当且仅当

\[
\boxed{
(k,p,r,s)
=
(5,2,3,3),
(6,2,3,4),
(8,2,3,5).
}
\]

### 所有 r>=5 都不可能

L055 从共同 exact-window root `s` 推出必要条件

\[
k^2<p\,s(s+2),
\qquad
rs^2\le k^2+2k,
\qquad
k^2<r(s+1)^2.
\]

对 `r>=5` 又进一步得到

\[
2s^2<(3r-3)s+r+1.
\]

同一份 L055 证明依次排除 `r>=11`、`r=7`、`r=5`，这些步骤均不使用 `k>=9`。因此任何 exact-window collision 都必须满足

\[
(p,r)=(2,3).
\]

### 剩余 (2,3) 情形只有有限个

对 `(2,3)`，L055 得到

\[
k^2<2s(s+2),
\qquad
3s^2\le k^2+2k,
\]

并且在不使用 `k>=9` 的情况下证明 `s<=7`。于是 `k<=11`。又因为 prime 3 只有在 `k>=5` 才进入 lower band，剩下

\[
k=5,6,7,8,9,10,11.
\]

精确窗口逐一给出：

- `k=5`: `G_2^win={3,4}`, `G_3^win={3}`；
- `k=6`: `G_2^win={4}`, `G_3^win={3,4}`；
- `k=7`: `{5}` 对 `{4}`；
- `k=8`: `{5,6}` 对 `{4,5}`；
- `k=9`: `{6,7}` 对 `{5}`；
- `k=10`: `{7}` 对 `{5,6}`；
- `k=11`: `{7,8}` 对 `{6}`。

因此恰好只剩上述三个 window collisions。∎

## 4. L056-B —— realized-shell root collisions 的完整分类

状态：`PROVED`。

对不同 lower-band least-prime shells，

\[
G_p^{\rm sh}(k)\cap G_r^{\rm sh}(k)\ne\varnothing
\]

当且仅当

\[
\boxed{
(k,p,r,s)
=
(5,2,3,3)
\quad\text{或}\quad
(8,2,3,5).
}
\]

### k=5 与 k=8 确实可实现

`k=5` 时，

\[
26=2\cdot13,
\qquad
27=3\cdot9
\]

都位于 `(25,36)`，最小素因子分别为 2、3，而且两个 cofactor 的 root 都是 3。

`k=8` 时，

\[
66=2\cdot33,
\qquad
75=3\cdot25
\]

都位于 `(64,81)`，最小素因子分别为 2、3，而且两个 cofactor 的 root 都是 5。

### k=6 被 admissibility 过滤掉

`W_3(6)=[13,16]` 中唯一产生 root 4 的 `p=3` cofactor 是 `q=16`。但

\[
3q=48
\]

的最小素因子是 2，所以 `q=16` 并不属于真实 `p=3` shell。真实 `p=3` cofactors 都是奇数并停留在 root 3。

因为任何真实 shell image 都是 exact-window image 的子集，L056-A 已经保证不存在其他可能 collision。∎

## 5. 真实 root coordinate 的局部 split multiplicity

把 coarse quotient 取为只保留 `R_2(q)`，target 则同时保留 root 与 least-prime shell identity。

L056-B 给出任意真实 root fiber 内 shell labels 数的精确最大值：

\[
\boxed{
\max_s m_k(s)=
\begin{cases}
2,&k\in\{5,8\},\\
1,&k\ge4,\ k\notin\{5,8\}.
\end{cases}}
\]

`k=6` 的 window overlap 不贡献任何真实 split，因为其冲突状态不可实现。

## 6. L057 —— 精确最小 root-shell repair alphabet

状态：`PROVED`。

由 P023-S9-T03，任何把 actual root 升级为 `(root,shell)` 的 repair coordinate，其最小 alphabet 大小恰好就是最大局部 split multiplicity。因此

\[
\boxed{
R_{\min}(k)=
\begin{cases}
2,&k\in\{5,8\},\\
1,&k\ge4,\ k\notin\{5,8\}.
\end{cases}}
\]

所以整个 lower-band 家族中，真正必须增加一个 binary state 的只有两个平方盆地。∎

## 7. 一个统一且有信息的 p=2 feature

定义

\[
\boxed{
\beta_k(q)=
\mathbf 1\!\left[
q>\left\lfloor\frac{k(k+2)}3\right\rfloor
\right].
}
\]

对所有 `k>=4` 的真实 lower-band states，这个 bit 恰好等于“least prime 是否为 2”的指示器。

### 对 p>=3

若 `q` 属于真实 `p>=3` shell，则必有 `q in W_p(k)`，所以

\[
q\le
\left\lfloor\frac{k(k+2)}p\right\rfloor
\le
\left\lfloor\frac{k(k+2)}3\right\rfloor.
\]

故 `beta_k(q)=0`。

### 对 p=2

所有 `q in W_2(k)` 满足

\[
q\ge\left\lfloor\frac{k^2}{2}\right\rfloor+1.
\]

当 `k>=4` 时，

\[
\frac{k(k+2)}3\le\frac{k^2}{2},
\]

于是

\[
q>\left\lfloor\frac{k(k+2)}3\right\rfloor.
\]

所以 `beta_k(q)=1`。因此在真实 lower-band states 上

\[
\boxed{\beta_k(q)=1\iff \operatorname{spf}(n)=2.}
\]

∎

## 8. 有信息的 feature 不等于必要 repair

统一 bit `beta_k` 即使在 root coordinate 已经能够区分所有 shells 时，也仍然可以告诉我们 `p=2` 与否。

例如 `k=6`，真实状态上两个 bit 值都存在，所以 `beta_6` 确实有信息；但 L056-B 已证明没有任何真实跨 shell root collision，因此

\[
R_{\min}(6)=1.
\]

常数 repair 已经足够。

所以

\[
\boxed{
\text{informative feature}
\neq
\text{task-necessary repair}.
}
\]

必要精度要看**当前 coarse fibers 在目标 task 下是否真的被继续切分**，不能按某个 feature 能泄露多少额外信息来衡量。

## 9. L057-C —— 一个规范的最小 repair coordinate

定义 task-minimal repair

\[
\boxed{
\rho_k(q)=
\begin{cases}
\beta_k(q),&k\in\{5,8\},\\
0,&\text{其他情形}.
\end{cases}}
\]

则对所有 `k>=4`，状态

\[
\boxed{
\widetilde R_k(q)=(R_2(q),\rho_k(q))
}
\]

都能恢复 lower-band least-prime shell label。

在 `k=5,8`，两个 repair symbols 正好拆开唯一真实冲突 shell fibers；其他所有 `k` 上 root 本来就已分离真实 shells，`rho_k` 只使用一个常数 symbol。因此它对每个 `k>=4` 都达到 L057 的最小下界。∎

统一 `beta_k` 仍然是方便的充分 decoder feature，但在不需要 repair 的地方不再称为 minimal。

## 10. 纠偏后的 precision hierarchy

lower-band 路线现在有五个严格不同的层：

1. exact cofactor `q`：从 `k>=4` 起恢复 shell identity；
2. actual root + task-minimal repair `rho_k`：对所有 `k>=4` 恢复 shell identity；
3. actual root alone：只在 `k=5,8` 失败，其 sharp eventual threshold 仍为 `k>=9`；
4. exact-window root image：额外产生 `k=6` 假 collision，小值 collision set 为 `5,6,8`；
5. L052 扩大 candidate pairs：统一不交要到 `k>=15`。

所以每放松一层状态语义，都可能凭空制造额外资源竞争。

## 11. 对数论递归的反哺

真实 lower-band 跨 shell ambiguity 已经完全局域到两个有限盆地，不应再贡献任何渐近 multiplicity penalty。

从 `k>=9` 起，甚至更强地说对所有 `k>=4` 除 `5,8` 外，root alone 已经识别 least-prime shell。如果统一实现仍携带 `beta_k`，它只是可选信息，而不是数学上必要的 precision。

P017 剩余困难因而继续被推向 shell 内 root many-to-one、`p`-rough cofactor capacity、high-band large-prime structure，以及 mirror/CRT compression。

## 12. 可执行规范

- `src/enterprise_math/p017_root_shell_repair.py`
- `tests/test_p017_root_shell_repair.py`

可执行层使用真实 `first_factor_shell` states，而不是 raw cofactor window 中的全部整数。测试固定真实 collision set `{5,8}`、`k=6` window-only collision 的消失、统一 `p=2` feature、最小 repair profile 与 adaptive minimum repair coordinate。

有限枚举只用于 regression；L056-A/L056-B/L057 的依据是上面的普通证明。
