# R004 精度宇宙生成 —— Supplement 07：闭式 future-language representation compiler

状态：`PROVED_WIP + EXECUTABLE_CHECKED + PRIOR_ART_SPECIALIZATION + FOUNDATION_FEEDBACK_CANDIDATE`  
父文档：`R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_06.zh-CN.md`  
Owner branch：`research/r004-precision-genesis-closure-20260810`

Supplement 06 已经确立 operation-relative representation 原则：

`count / defect / exponent / repair` 不是一个万能坐标系；只有当声明的 future language 真正能下降到某个 representation 上时，该 representation 才合法。

本补充把这条原则从负边界推进成第一版**闭式 representation compiler**。它不重新拥有 P023 的 generic future-safe quotient，也不重新拥有 P024 的 generic translation-language program，而是解一个明确的有限算术族。

## 1. Prime-power setup

固定 prime `p`、正整数 cap `K`，状态空间为

`X = Z / p^K Z`。

声明 observable 为 capped valuation

`q_K(x)=min(v_p(x),K)`，

其中零 residue 取 level `K`。

给定 future translation language `T subset X`，future signature 为

`Sigma_T(x)=(q_K(x+t))_(t in T)`。

按照 P023，coarsest safe representation 是 `ker(Sigma_T)`。这里真正要解的是：这个 kernel 能不能直接写成算术 normal form，从而不必先跑一次 generic partition refinement。

## 2. Subgroup translation compiler

先取 translation subgroup

`H_s = p^s Z / p^K Z`，

其中 `0<=s<=K`。

### R004-COMP-T01 —— 低 level 不变量

若 `v_p(x)=a<s`，则每个 `t in H_s` 都有 valuation 至少 `s>a`，因此

`v_p(x+t)=a`

对所有允许的 future translations 都成立。

所以在 subgroup threshold 以下，只保留 valuation level 已经足够。

### R004-COMP-T02 —— reachable subgroup 内必须精确

若 `v_p(x)>=s`，写成

`x=p^s u` modulo `p^K`。

每个允许的 translation 都是 `p^s h`，因此

`x+p^s h=p^s(u+h)`。

去掉共同的 `p^s` 后，`h` 遍历 modulo `p^(K-s)` 的全部 residues。完整 translations 会把每个 `u` 精确分开：取 `h=-u` 可让这个 state 到达 capped level `K`，而任意不同 `u'` 在同一个 translation 下不能同时到达该 level。

因此在 `H_s` 内，future-safe quotient 必须保留 exact tail

`u=x/p^s mod p^(K-s)`。

### R004-COMP-T03 —— 闭式最小 token

coarsest future-safe token 为：

当 `v_p(x)<s` 时，

`R_(p,K,s)(x)=("v",v_p(x))`；

当 `v_p(x)>=s` 时，

`R_(p,K,s)(x)=("r",x/p^s mod p^(K-s))`。

第一部分恰有 `s` 个 valuation classes，第二部分恰有 `p^(K-s)` 个 exact subgroup residues，因此

`C(p,K,s)=s+p^(K-s)`。

该 representation 不仅 sufficient，而且 minimal，因为任意两个不同 token 都存在 future translation 可以把它们区分开。

Executable oracle 直接检查 token equality 与完整 future-signature equality 完全一致。

## 3. Translation depth 给出精确指数 repair law

定义 translation depth

`t=K-s`。

允许的 subgroup 大小恰为

`|H_s|=p^t`，

而最小 state complexity 是

`C_(p,K)(t)=K-t+p^t`。

纯 valuation baseline `t=0` 有 `K+1` classes，因此额外 repair cost 为

`E_p(t)=p^t-t-1`。

每再打开一个 translation digit，边际状态成本为

`E_p(t+1)-E_p(t)=(p-1)p^t-1`，

二阶有限差分为

`Delta^2 E_p(t)=(p-1)^2 p^t>0`。

因此 state complexity 对 future translation depth 呈严格离散凸增长。未来能力越深，每多开放一层所需新增状态越昂贵；唯一平坦例外是

`p=2, t=0 -> 1`，

因为 `E_2(1)=0`：二进制第一层 translation digit 不增加 quotient class 数，原因是最高两个 capped valuation classes 已经分别命名该二点 subgroup 的两个 residues。

这是一条 exact finite complexity law，不是 entropy 或 information-theoretic limit theorem。

## 4. CRT product compiler

现在取

`M=prod_i p_i^(K_i)`，

其中 primes 两两不同。Chinese remainder theorem 给出

`Z/MZ ~= prod_i Z/p_i^(K_i)Z`。

令 future translation subgroup 逐 component 分解为 levels `s_i`，等价 depths `t_i=K_i-s_i`。

observable 是各 prime-power component 的 capped valuation vector。因为 state space 与声明的 subgroup language 都按 CRT components 分解，所以 future-signature equality 也是逐坐标的。

因此最小 compiled state 就是各单 prime token 的 tuple，并且

`C_CRT = prod_i [s_i+p_i^(K_i-s_i)]`，

等价地

`C_CRT = prod_i [K_i-t_i+p_i^t_i]`。

分支用多个小 composite moduli 与全部小 subgroup-level 组合，对 literal full future signatures 做了穷举核对。

这是 R004 第一类可以直接从 typed future-language description 写出 state complexity，而不必先枚举 generic quotient 的 compiler family。

## 5. 任意单轴 translation language：p-adic trie compiler

在单 prime-power axis 上，不需要 subgroup closure。

任取非空有限 translation set `T subset Z/p^K Z`，定义 center set

`C=-T mod p^K`。

那么对应 center `c` 有

`q_K(x+t)=min(v_p(x-c),K)`。

按 p-adic digit 顺序读取 residue，也就是从最低位往高位读。两个 residues modulo `p^j` 相同，当且仅当其前 `j` 个 p-adic digits 相同。因此 center set 自然定义一个 occupied p-adic prefix trie。

对 state `x` 只有两种情况。

1. **Center**：`x in C`。它在自己的 signature coordinate 上取值 `K`，因此该 center 必须是 singleton future-safe class。
2. **Trie exit**：`x notin C`。沿 `x` 的低位 prefix 往 trie 中走，只要仍有 center 共享该 prefix 就继续；在唯一最深的 occupied parent prefix 处，`x` 的下一位进入一个没有任何 center 的 child branch。

从同一个 occupied parent 退出的所有 states 拥有完全相同的 future signatures：

- parent 外的 centers 已经在更早 digit 分叉，其 valuation 由 shared parent prefix 决定；
- parent 内的 centers 都在下一 digit 与退出 state 分开，所以 valuation 恰等于 parent depth。

反过来，不同 exit parents 可以由其中一个 parent 下的 center 未来区分；center tokens 彼此也可区分。

所以 coarsest safe representation 精确等于：

`center token OR deepest occupied exit-parent token`。

### R004-COMP-T04 —— 任意 language 的 class-count formula

把 depth `<K` 且至少存在一个 unoccupied child 的 occupied trie node 称为 **deficit node**。那么

`C_T = |C| + # deficit nodes`。

第一项是 exact center leaves；第二项是每个 occupied parent 的全部 empty child branches 合并后形成的一个 wildcard class。

这是有限 p-adic center trie 上的 closed form，不是 normalized measure。

subgroup theorem 立即成为其特殊情形。若 `C=H_s`，前 `s` 层是一条带 empty siblings 的单一路径，而 depth `s` 以下的 subtree 被完全填满，因此 deficit nodes 恰好有 `s` 个：

`C_T=p^(K-s)+s`。

## 6. 相同 action count 可以需要不同 state complexity

Trie theorem 给出新的 negative boundary：

`future action count != representation complexity`。

在 `p=2`、`K=4` 时，仅两个 centers 已经可以有不同 class counts：

- `{0,8}` -> `5` classes；
- `{0,4}` -> `6` classes；
- `{0,2}` -> `7` classes；
- `{0,1}` -> `8` classes。

四个 languages 都只有两个 centers；差别只在 p-adic separation。

对两个不同 centers `c_1,c_2`，令

`r=v_p(c_1-c_2)<K`。

它们的 p-adic trie 共用一条路径直到 depth `r`，下一层分叉。直接数 center leaves 与 incomplete occupied parents 得到：

当 `p=2` 时

`C_2=2K-r`；

当 `p>2` 时

`C_2=2K-r+1`。

统一写成

`C_2=2K-r+1_(p>2)`。

所以 future operations 在 p-adic 意义下越接近、共享低位 digits 越深，它们作为 future distinguishers 越冗余。决定当前最小状态复杂度的是 future-language **geometry**，不只是 cardinality。

## 7. Validation

本补充新增两个 executable compilers：

- `precision_representation_compiler.py` —— subgroup 与 CRT closed forms；
- `precision_translation_trie_compiler.py` —— 任意单 prime translation sets。

Committed regressions 在 bounded families 上把 compiler tokens 与 literal full future signatures 逐一比较。

独立研究穷举另外检查了：

- `Z/2^4 Z` 的全部非空 translation subsets：**65,535 / 65,535** exact；
- `Z/3^2 Z` 的全部非空 translation subsets：**511 / 511** exact；
- 多个小 prime powers 与 composite moduli 的 subgroup / CRT families。

这些是 exact finite validation，不是 Lean proof，也不是 fresh full-repository CI。

## 8. Ownership 与 prior-art 边界

generic theorem

`future language -> coarsest safe quotient = future-signature kernel`

归 P023/FQ-004 上游所有。Translation-language precision 归 P024。p-adic valuation、有限 cyclic p-groups、CRT 与 prefix-tree reasoning 都属于成熟数学。

因此 R004 本轮只主张更窄的 specializations：

- capped valuation + subgroup translations 的 closed-form compiler；
- 精确指数/离散凸 state-cost law；
- CRT product specialization；
- 任意单轴 p-adic trie normal form；
- “相同 action 数可以因 future-language geometry 不同而产生不同 state cost”的负边界。

这组精确 package 的历史 novelty 仍为 `NOVELTY_UNVERIFIED`。

## 9. 下一 frontier

当前 compiler frontier 已经明确拆开。

WIP 层已经解决：

`one p-power axis + arbitrary finite translations -> trie compiler`，

以及

`multiple CRT axes + product-closed translation subgroups -> product compiler`。

仍未解决的是：

> **多个 prime-power axes 上的 correlated、non-product translation language。**

此时 action set 是 CRT product 的一个相关子集，而不是 Cartesian product。独立逐轴 compiler 可能 over-refine，因为某些 future action combinations 根本不会发生。

下一步真正值得研究的是：如何从 correlated finite future operations 自动得到最小 joint repair state，同时又不退回一个不可解释的 generic partition table。
