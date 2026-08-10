# R004 精度起源——补充 35：finite-field covering-code primitive ISA 对偶

状态：`PROVED_WIP + EXECUTABLE_REFERENCE + PRIOR-ART REDUCTION BRIDGE`
父文档：`R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_34.zh-CN.md`
Owner branch：`research/r004-precision-genesis-closure-20260810`

补充 34 给出了一个显式 binary storage/update/readout family。现在得到更强边界：unrestricted storage-vs-readout optimization 并不是 R004 新组合问题，而是标准 linear covering-code length problem。

## 1. Parity-check / primitive-ISA 对偶

设 additive semantic action space 为 `F_p^r`，s 条 primitive instructions 是 surjective matrix `H:F_p^s -> F_p^r` 的 columns。instruction word 是 coefficient vector `e in F_p^s`，净 semantic effect 为 `H e`。

定义 **null-program code**：

`C=ker H`。

于是：semantic rank 是 C 的 codimension r；primitive storage 是 code length s；independent null-program 数为 `dim C=s-r`；semantic action y 的最短 primitive readout 是 syndrome/coset `H e=y` 中的 minimum Hamming weight；最坏 readout depth 精确等于 covering radius `R(C)`。

因此 fixed semantic rank r、worst readout depth D 下的最小 primitive storage，就是 q-ary linear covering-code length function `ell_p(r,D)`。

covering code、length function 与 saturating set 都属于先行数学。R004 只保留这个 typed compiler interpretation 与 fail-closed boundary。

## 2. Sphere-covering 下界

support 不超过 D 的 coefficient words 数量为

`V_p(s,D)=sum_(j=0)^D binom(s,j)(p-1)^j`。

覆盖全部 semantic actions 必须满足 `V_p(s,D)>=p^r`。binary 时退化成此前的 `sum binom(s,j)>=2^r`。

## 3. Exact depth-one 端点

若 D=1，每个 nonzero projective semantic direction 都必须有一个 primitive representative：

`ell_p(r,1)=(p^r-1)/(p-1)`。

binary 下即 `2^r-1`。

## 4. Exact one-null-program 区间

若 `s=r+1`，null-program code dimension 为 1。最优 one-dimensional null code 的 nonzero word 必须 full-support；经过 coordinate scaling 可归一化为 repetition line `<(1,...,1)>`。

令 `n=r+1`，其 covering radius 精确是

`R_one-null=n-ceil(n/p)`。

因此在

`(r+1)-ceil((r+1)/p) <= D < r`

整个区间：

`ell_p(r,D)=r+1`。

`D>=r` 时普通 basis 已给 `ell_p(r,D)=r`。binary 特例：只增加一个 redundant primitive，就把最坏 readout depth 降到 `ceil(r/2)`。

## 5. 短程序歧义

radius-D covering ISA 中，depth `<=D` 的 coefficient words 有 `V_p(s,D)` 个，但 semantic actions 只有 `p^r` 个。因此平均 short-program multiplicity 为

`V_p(s,D)/p^r`。

定义纯整数 short-word excess：

`A_word=V_p(s,D)-p^r`。

若 `A_word=0`，每个 semantic action 必须恰有一个 short representation；若大于 0，则该 `(s,D)` covering 中短程序冗余不可避免。

## 6. 小参数 binary exact checkpoints

primary covering-code / saturating-set classifications 给出 semantic ranks 3..7 的 radius-2 exact staircase：

`ell_2(3,2)=4`, `ell_2(4,2)=5`, `ell_2(5,2)=9`, `ell_2(6,2)=13`, `ell_2(7,2)=19`。

R004 独立 normalized enumeration 又检查了 r=5 下界：固定 standard basis 后 `(5,2,8)` 的全部 2,600 个 candidates 都失败，而 9-column construction `[1,2,4,8,16,3,5,6,31]` 的 radius 为 2。

对 `(r,D)=(7,3)`：s=9 的 7,140 个 normalized candidates 全失败；s=10 的 280,840 个全失败；而 `[1,2,4,8,16,32,64,96,57,97,71]` 的 radius 为 3。因此在 declared linear binary ISA model 中 exact finite enumeration 得到 `ell_2(7,3)=11`。不主张这个 numerical value 的历史 novelty。

## 7. 为什么补充 34 不是最优

r=7、D=3 时，k=3 的 local table 要保存 `7+21+35=63` 条 primitives，而 covering-code ISA 只需 11。weight-locality 只是透明 construction，不是 terminal storage optimizer。

## 8. Typed fail-closed 边界

只有当 primitive effects 在 declared finite field 上线性组合、future 只关心最终 net semantic action、instruction ordering 与 intermediate side effects 无关、并且 codeword 真的是 semantic null program 时，covering-code reduction 才合法。

若存在 branch effects、intermediate guards、witness identity、noncommuting operations 或 history-sensitive legality，`ker H` 不能自动视为 null semantics。此时必须回到 generic typed future-language / certificate compiler，不能强行编码成 covering code。

## 9. 研究后果

full additive semantic surface 应直接消费成熟 covering-code / saturating-set constructions 作为 backend。R004 后续不应从头求 `ell_p(r,D)`；真正项目问题是识别哪些 typed future languages 能合法降成 additive ISA、precision birth spectrum 如何与 code columns/null programs 交互，以及 code-derived primitive surfaces 如何进入更大的 Representation Compiler。
