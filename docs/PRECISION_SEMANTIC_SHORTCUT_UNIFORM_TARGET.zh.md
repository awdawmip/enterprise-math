# Uniform Semantic Shortcut Language 与 Target-Specific Cache

状态：`RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID：`R-8F3K`

Bounded-support shortcut table 之所以有很大的 binomial storage，是因为它购买了一个**uniform future-language guarantee**，而不是因为某一个 fixed target 天生需要这么多 effects。

## 1. Uniform one-round requirement

固定 k 个 primitive directions 与 shortcut depth d。

要求：

> 每个 support size<=d 的 nonzero semantic effect T，都必须能从 identity 用一次 shortcut application 执行。

从 identity 做一次 application，得到的正是被选中的 primitive shortcut mask。因此每个这样的 T 本身都必须出现在 primitive catalogue 中。

所以 minimum possible catalogue size 精确为：

`sum_(i=1)^d C(k,i)`。

因此 canonical bounded-support shortcut family 对这个 uniform one-round requirement 是**global minimum**。

## 2. Target-specific requirement 可以便宜得多

现在只声明一个 target effect T。

把 T 的 support 分成 size<=d 的 chunks，只存这些 chunk masks。

Catalogue size 与 execution distance 都是：

`ceil(|T|/d)`。

这可以 exact 达到 T，但不会对 unrelated semantic effects 提供 one-round guarantee。

## 3. Sharp k=20,d=3 gap

对 full 20-bit target：

- support<=3 的 uniform one-round language storage：`1350` 个 primitive effects；
- target-specific full-mask cache：`ceil(20/3)=7` 个 primitive effects。

两边相对于各自 declared task 都是 exact 的。

1350-entry table 对 uniform language 不是 overprecision；7-entry table 对 uniform language 也不 sufficient。

## 4. Quantifier placement 会改变 resource minimality

比较：

`对每个 |T|<=d 的 target，都要一轮执行 T`

与

`只对这个 fixed T，用 d-bounded shortcuts 执行`。

第一种 quantifier 覆盖整个 future-effect language，因此强迫所有 local effects 进入 storage；第二种允许 target-adapted basis。

所以 cache minimality 与 earlier fixed-target / all-target reflection/certification 一样，是 future-language relative 的。

## 5. Routing consequence

在优化 shortcut / cache storage 之前，必须先声明 representation 要支持：

- 一个 fixed target；
- 一个 target region；
- 某 complexity bound 下的全部 targets；
- 完整 semantic operation language。

不能把某一种 quantifier pattern 的 storage lower bound 搬到另一种 task 上。

## Owner-local assets

- `src/enterprise_math/semantic_shortcut_uniform_target.py`；
- `tests/test_semantic_shortcut_uniform_target.py`；
- 本双语 note。

## Prior-art / status

Set systems、support masks 与 target-specific / uniform data structures 都是标准既有数学 / CS。本文只拥有 Enterprise Math 的 future-language quantifier interpretation。

无 repository strict CI、无 `EXECUTABLE_CHECKED`、无 canonical claim。`CI_NOT_REQUIRED_FOR_RESEARCH`。Hard block：`NONE`。
