# R004 精度起源——补充 19：Module Cut Compiler 与 dual-matroid instruction bases

状态：`PROVED_WIP + EXECUTABLE_CHECKED + PRIOR_ART_SPECIALIZATION + MODULE_CUT_CLOSED_FORM`  
父文档：`R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_18.zh-CN.md`  
Owner branch：`research/r004-precision-genesis-closure-20260810`

补充 18 给出第一类 arithmetic closed-form obstruction compiler。本补充给出一个 linear/module analogue：完整 carrier-cut clutter 精确变成 representable matroid circuits，而且全部 minimal Carrier Bases 可以直接由 linear algebra 得到，不必再做 generic hypergraph dualization。

## 1. 有限 p-power module world

令

`R=Z/p^K Z`, `X=R^d`，

当前 observation 为

`O_A(x)=A x in R^r`，

其中 `A` 是 `r x d` integer matrix，按 `p^K` 读取。

假设每个 column `A_i` 在 mod `p` 后非零，即至少含一个 unit entry。对每个 coordinate `i`，future generator `Z_i` 把该 coordinate reset 为 0。

## 2. R004-COMP-T35——retained-reset quotient

对 retained reset set `S`，定义

`q_S(x)=(Ax,x|_S)`。

这精确等于唯一最粗 future-safe quotient。

充分性：若 `Ax` 与 retained coordinates 都相同，则任意 retained reset composition 后的 observation 继续相同。

必要性来自

`Ax-A(Z_i x)=A_i x_i`。

因为 `A_i` 有 unit entry，map `x_i -> A_i x_i` 在 `R` 上 injective，因此 current + one-reset observations 可精确恢复 retained coordinate `x_i`。

所以

`Compile_S(P0)=ker q_S`，其中 `P0=ker A`。

全 reset language 下 carrier 为 discrete。

## 3. R004-COMP-T36——hidden injectivity 由 mod p 决定

令 `H` 为 deleted/hidden coordinates。retained quotient 为 discrete，当且仅当 restricted map

`A_H:R^H -> R^r`

injective。

这又当且仅当

`bar A_H=A_H mod p`

的 columns 在 `F_p` 上 linearly independent。

直接证明：若 `bar A_H` independent 而 `A_H v=0` 存在 nonzero `v`，提取所有 coordinates 的最大公共 `p^t` 后得到至少一个 unit coordinate；模 `p` 即产生 `bar A_H` 的 nonzero kernel vector，矛盾。反过来若 `bar A_H c=0` 有 nonzero residue vector，lift 后乘 `p^(K-1)` 即得到 `A_H` 的 nonzero kernel vector。

因此整个 p-power carrier obstruction 已经完全暴露在 residue-field column dependence 中。

## 4. R004-COMP-T37——carrier cuts = matroid circuits

令 `M(A mod p)` 为 `F_p` 上 column matroid。

hidden set `H` carrier-breaking，当且仅当它在该 matroid 中 dependent。因此 inclusion-minimal carrier cuts 精确为

`C_car = Circuits(M(A mod p))`。

## 5. R004-COMP-T38——minimal Carrier Bases = dual-matroid bases

retained reset set `S` 保持 discrete carrier，当且仅当它命中 `M` 的每一条 circuit；等价地，补集 `E\S` 不含 circuit，即 independent。

`S` inclusion-minimal，当且仅当 `E\S` maximal independent，也就是 `M` 的 basis。

所以

`B_C = {E\B : B in Bases(M)} = Bases(M*)`。

因此所有 minimal Carrier Bases 大小相同：

`|S| = d-rank(A mod p)`。

这比 generic cut dualization 更强：一次 Gaussian elimination 找到 column basis `B`，其 complement 就是一个 minimum instruction set；枚举所有 column bases 就得到全部 minimal Carrier Bases。

## 6. 与 representation codimension 的关系

此前 relation-rank compiler 用

`Gamma=K(d-r)`

表示 rank-`r` relation carrier 删除的 exact p-adic digit freedoms。

这里相同的 rank defect 出现在 **instruction layer**：

`instruction_nullity = d-rank(A mod p)`。

两者不能混同：`Gamma` 数的是 p-adic state digits；新 nullity 数的是从当前 linear observation 恢复 exact carrier 需要的 primitive coordinate-reset instructions。但二者都由同一个 residue-field rank defect 控制。

## 7. 例子

- `A=I_d`：无 circuits，carrier 不需要任何 reset instruction。
- one-row equal nonzero columns：全部 pairs 都是 circuits；每个 minimal reset basis 大小 `d-1`。
- `F_2` triangle columns `(1,0),(1,1),(0,1)`：唯一 circuit 是全部三列；任一一个 reset 都是 minimal Carrier Basis。

## 8. Exact validation

独立 exact checks 覆盖 **2,247** 个 p-power matrix systems：`p=2,3`、`K=1,2`、`d=2,3`、1/2 observation rows，且每列 mod `p` primitive。

- **13,320** 个 retained-reset quotient cases 全部匹配 `ker(Ax,x|_S)`；
- **2,247/2,247** minimal carrier-cut families 全部匹配 `A mod p` 的 circuits；
- **2,247/2,247** inclusion-minimal compiler Carrier Basis families 全部匹配 column bases 的 complements。

零 violation。

Executable：`src/enterprise_math/precision_module_cut_compiler.py`；tests：`tests/test_precision_module_cut_compiler.py`。

不主张 fresh full-repository CI 或 canonical-main status。

## 9. Prior-art 边界

matroid circuits=minimal dependent sets、representable/vector matroids、dual matroids、basis complements、finite-field linear algebra，以及 local-ring/Nakayama 型 residue reduction 都是成熟数学。

R004 只主张 compiler bridge：

`p-power linear observation + coordinate resets -> residue-field column matroid -> circuits as carrier cuts -> dual bases as minimal carrier instructions`。

历史 novelty 仍为 `NOVELTY_UNVERIFIED`。

## 10. 架构后果

algebraic cut atlas 现在已经有两种不同 dependency geometry：

- integer weighted binary observation -> minimal non-dissociated supports；
- p-power linear module observation -> representable-matroid circuits。

因此 generic obstruction clutter 不是一种固定 combinatorial species；typed observation/action algebra 决定它应编译成哪种 dependency geometry。

## 11. 下一 frontier

下一步应研究 full language 不必得到 discrete carrier 的 richer module/relation 情形：直接对“保持指定 quotient exponent profile / A3 relation rank”推 cut edges，而不是只研究 exact-state recovery。
