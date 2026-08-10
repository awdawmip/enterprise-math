# R004 精度起源——补充 37：null-program history collision hierarchy

状态：`PROVED_WIP + EXECUTABLE_REFERENCE + P011-BRIDGE + PRIOR-ART-BOUNDED`
父文档：`R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_36.zh-CN.md`
Owner branch：`research/r004-precision-genesis-closure-20260810`

补充 35–36 已把 additive net semantic actions 编译成 primitive instructions 与 null-program code。本补充重新引入被 net-effect quotient 擦掉的一层：**哪些 bounded primitive programs 会落到同一个 semantic action。**

这套 collision hierarchy 精确就是 P011 的 `W_k`，只是当前对象换成 primitive-program histories。

## 1. Bounded primitive-program multiplicity

设 `H:F_2^s -> F_2^r`，`C=ker H`，并令

`B_D={e in F_2^s: wt(e)<=D}`。

对 semantic action y：

`N_D(y)=#{e in B_D:H e=y}`。

定义

`W_k^prog(D)=sum_y binom(N_D(y),k)`。

它就是把 P011 collision polynomial 直接作用到 bounded instruction histories。

## 2. Short-program uniqueness gate

两条不同 depth-`<=D` programs e,e' 产生同一 semantic action，当且仅当

`e-e' in C\{0}`。

它们的 difference weight 至多 `2D`。反过来，任何 `wt(c)<=2D` 的 nonzero null codeword 都可以把 support 分成两块，每块大小不超过 D，从而制造两条同 syndrome 的 short programs。

因此：

`全部 depth<=D programs 唯一  <=>  d_min(C)>2D`。

如果同一 ISA 的 covering radius 也不超过 D，则每个 semantic action 恰有一个 short program；这就是 coding language 中的 perfect packing/covering boundary。

Typed 含义：net-effect-only future 可以直接 quotient null programs；path/witness-sensitive future 只有在 relevant bounded histories 唯一，或 history identity 已由其他证书保存时才能这样做。

## 3. W2 精确由普通 weight spectrum 决定

对 nonzero null word c，difference 为 c 的 ordered program pairs 与

`B_D(0) cap B_D(c)`

一一对应。因此

`2 W_2^prog(D)=sum_(0!=c in C)|B_D(0) cap B_D(c)|`。

binary Hamming cube 中该 intersection 只依赖 `w=wt(c)`：

`I_2(s,D,w)=sum binom(w,a)binom(s-w,b)`，

求和条件为

`a+b<=D`,
`w-a+b<=D`。

所以

`W_2^prog(D)=1/2 sum_(0!=c in C)I_2(s,D,wt(c))`。

因此 ordinary null-code weight enumerator 是整个 bounded pair-collision curve 的 exact sufficient state。

## 4. W3 需要更强 state

对 ordered distinct nonzero null words c,d：

`6 W_3^prog(D)=sum_(c,d)|B_D(0) cap B_D(c) cap B_D(d)|`。

binary 情况下，three-ball intersection 完全由 triangle

`(wt(c),wt(d),wt(c+d))`

决定，因为这三个 pairwise distances 恰好决定每个 coordinate 上 `(c_j,d_j)` 属于 `00,10,01,11` 的数量。

所以 null code 的 ordered triangle profile 是 W3 的 exact sufficient state。

## 5. Ordinary weight enumerator / W2 不决定 W3

取两条 length-6、dimension-3 binary null codes：

`C0=<15,20,36>`,
`C1=<9,20,34>`。

集合分别是

`C0={0,15,20,27,36,43,48,63}`，
`C1={0,9,20,29,34,43,54,63}`。

二者 ordinary weight enumerator 完全相同：

`1+3z^2+3z^4+z^6`。

因此全部 W2 curves 也相同；D=1..5 均为

`(3,27,97,178,217)`。

但 W3 不同：

`C0:(1,17,131,318,427)`，
`C1:(0,16,132,319,427)`。

仅 D=1 就已经是 1 vs 0：第一条 code 有一个 semantic fiber 含三条 short programs；第二条只有 pair collisions。

所以：

`ordinary weight spectrum / all pair collisions !=> higher history-collision spectrum`。

两条 code 的 triangle profiles 正好不同，与 W3 公式完全一致。

## 6. 一般 k-fold 公式

令 `c_2,...,c_k` 遍历 ordered、pairwise-distinct nonzero codewords，设 `c_i=e_i-e_1`，则

`k! W_k^prog(D)`

`=sum_(c_2,...,c_k)|B_D(0) cap B_D(c_2) cap ... cap B_D(c_k)|`。

binary code 中，该多球 intersection 由 coordinate-pattern counts

`#{j:(c_(2j),...,c_(kj))=alpha}`

对 `alpha in F_2^(k-1)` 完全决定。

因此 `(k-1)`-fold complete/joint weight profile 是 `W_k^prog(D)` 的 exact sufficient code state。

complete joint 与 r-fold weight enumerator 都是成熟 coding-theory 对象。R004 不主张这些概念为新发明；当前 project-local result 是把它们识别成 P011 bounded program-history collision hierarchy 的自然 state ladder。

## 7. 验证

Executable checks 包括：

- length-5 repetition-null perfect code，D=2：short programs 唯一，`W2=0`；
- S35 rank-5/radius-2 9-column ISA：direct enumeration 给 `W2=21`，与 ordinary-weight formula 精确一致；
- 两条 length-6 counterexample codes：ordinary weight enumerator/W2 相同，但 D=1 时 W3 为 1 vs 0；
- triangle-profile formula 精确重建上述 W3。

此前还在 rank-7/radius-3 11-column covering ISA 上独立检查 pair formula，两条路线均得 `W2=164`。

不声称 fresh full-repository CI。

## 8. 架构后果

covering-code backend 现在有明确 typed semantic ladder：

1. **只问 net effect** -> quotient by null code；
2. **bounded pair-history** -> ordinary null-code weight spectrum 足够；
3. **bounded triple-history** -> triangle / second-order joint profile；
4. **bounded k-history** -> `(k-1)`-fold joint coordinate profile；
5. **full witness/path identity** -> 保留实际 histories 或另一个已证明 sufficient 的 witness representation。

future 要求越高阶的 history distinction，可安全的压缩就越弱。storage/readout scalar optimum 不能替代完整 history-semantic certificate。
