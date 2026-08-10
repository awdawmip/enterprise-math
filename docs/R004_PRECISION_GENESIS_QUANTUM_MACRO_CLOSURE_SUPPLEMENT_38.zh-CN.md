# R004 精度起源——补充 38：collision polynomial 的充分性与 depth-shell 出生分解

状态：`PROVED_WIP + EXECUTABLE_REFERENCE + P011-SECOND-ORDER BRIDGE`
父文档：`R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_37.zh-CN.md`

补充 37 已说明计算 bounded program collisions 需要 null code 的哪一层 joint profile。本补充进一步问：完整 collision hierarchy 自己究竟记住了什么，又丢掉了什么。

## 1. Collision polynomial 与 multiplicity histogram 完全等价

固定 readout budget D，令

`N_D(y)=# short primitive programs producing semantic action y`。

定义

`W_k(D)=sum_y binom(N_D(y),k)`，

并包含 `W_0(D)=# semantic labels`。令

`C_D(z)=sum_k W_k(D)z^k`。

则

`C_D(z)=sum_y(1+z)^(N_D(y))`。

记

`h_m(D)=#{y:N_D(y)=m}`。

那么

`W_k(D)=sum_(m>=k)h_m(D)binom(m,k)`。

有限 binomial inversion 给出

`h_m(D)=sum_(k>=m)(-1)^(k-m)binom(k,m)W_k(D)`。

因此固定 depth 上的完整 collision hierarchy 与 short-program fibers 的**无标签 multiplicity histogram** 精确等价。

它比任意固定有限个 moments 更强，但仍弱于 labeled map `y -> N_D(y)`。

## 2. 两个端点

D=0 时只有 zero instruction word，因此一个 semantic label multiplicity 为 1，其余为 0。

binary full depth `D=s` 时所有 coefficient words 都允许。若 semantic map surjective 且 null code size `|C|=2^(s-r)`，每个 semantic action 恰有 `|C|` 条 programs，所以

`W_k(s)=2^r binom(|C|,k)`。

execution-depth filtration 因而从 maximally sparse histogram 走向 uniform full-coset histogram。

## 3. Depth-shell collision 出生分解

令

`A_D(y)=#{e:wt(e)=D,He=y}`。

则

`N_D(y)=N_(D-1)(y)+A_D(y)`。

Vandermonde 直接给：

`W_k(D)-W_k(D-1)`

`=sum_y sum_(j=1)^k binom(A_D(y),j)binom(N_(D-1)(y),k-j)`。

定义 j-new-program birth component：

`J_(k,j)(D)=sum_y binom(A_D(y),j)binom(N_(D-1)(y),k-j)`。

于是

`Delta W_k(D)=sum_(j=1)^k J_(k,j)(D)`。

对 k=2：

- `J_(2,1)=sum_y A_D(y)N_(D-1)(y)`：new programs 撞入 old fibers；
- `J_(2,2)=sum_y binom(A_D(y),2)`：本轮新 depth shell 内部自己出生的 collision。

这是早期 P011 exact collision-growth decomposition 在 primitive-program depth filtration 上的 specialization。

## 4. Transition state 严格强于两个 endpoint histograms

定义

`g_(a,b)(D)=#{y:N_(D-1)(y)=a,A_D(y)=b}`。

则

`J_(k,j)(D)=sum_(a,b)g_(a,b)(D)binom(b,j)binom(a,k-j)`。

但 D-1 与 D 两个 endpoints 的 multiplicity histograms 并不能恢复这个 transition state。

例：previous multiplicities 为 `(0,1,3)`。两种新 shell assignments：

`A=(2,2,1)`，
`A'=(3,1,1)`。

两者都得到相同的新 unlabeled multiplicity histogram `{2,3,4}`，所以两个 depths 上的全部 endpoint `W_k` 都一致。

但 pair collision birth decomposition 不同：

`A:(J_(2,1),J_(2,2))=(5,2)`，
`A':(4,3)`。

两边总 `Delta W_2=7` 一样，但 collision mechanism 不同。

所以即便知道相邻两个 depths 的完整 collision hierarchy，也不能判断 collisions 是怎样出生的。exact unlabeled transition state 是 joint histogram `g_(a,b)`。

## 5. Typed semantic ladder

因此 compiler 又出现一条严格 hierarchy：

1. 单个 `W_k`：一个 collision statistic；
2. 固定 D 的全部 `W_k`：unlabeled multiplicity histogram；
3. 相邻两个 depth 的 endpoint hierarchies：仍不足以恢复 birth mechanism；
4. joint transition histogram `(N_(D-1),A_D)`：精确恢复 unlabeled collision-birth decomposition；
5. labeled semantic map：future 会引用具体 semantic action 时必须保留；
6. primitive-program identity：actual histories/witnesses 本身有语义时必须保留。

这再次说明 equal resource profiles 不能替代 typed semantics。

## 6. 验证

reference module exact 检查了 binomial inversion、Vandermonde birth formula，以及上述“same endpoints / different birth mechanism”反例。

不主张 binomial inversion 或 Vandermonde identity 为新数学；R004 的新增只是把它们固定成 primitive instruction histories 上的 P011/certificate-state 接口。
