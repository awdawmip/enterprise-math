# 先行研究——R004 covering-code primitive ISA bridge

状态：`RESEARCH PRIOR-ART MAP / NOVELTY_UNVERIFIED`

补充 35 是 compiler bridge，不主张 covering code、covering radius、covering density、length function、parity-check matrix、projective saturating set 或其优化问题是 Enterprise Math 新发明。

## 主要先行来源

### SRC-R004-COVERING-CODE-DAVYDOV-2025

Davydov、Marcugini、Pambianco，*New upper bounds for binary linear covering codes*，arXiv:2511.02542（2025）。

该文明确给出 q-ary Hamming-ball volume、covering radius 的 syndrome/column characterization，以及 `ell_q(r,R)` 作为 fixed codimension / covering radius 下最小 code length 的 length function；同时记录 covering code 与 projective saturating set 的一一对应，并给出新的 infinite-family upper bounds。

R004 只消费这些成熟结构作为 unrestricted additive primitive-ISA backend。

### SRC-R004-SATURATING-DAVYDOV-2018

Davydov、Marcugini、Pambianco，*Classification of minimal 1-saturating sets in PG(v,2), 2<=v<=6*，arXiv:1802.04214（2018）。

该工作给出小 binary radius-2 / 1-saturating sets 的 exhaustive classification，用来约束我们小参数 staircase 的 novelty 表述。

## R004 当前 under-test 的本地 package

R004 只保留下列项目级解释：

1. parity-check columns 对应 primitive additive instructions；
2. code kernel 对应 null-program space；
3. covering radius 对应 worst-case semantic readout depth；
4. covering density 对应 average short-program multiplicity；
5. 标准 length function 对应 primitive storage/readout Pareto backend；
6. 如果 instruction order、side effects、witness identity 或 history-sensitive legality 使 code-kernel word 不再是真正 semantic null program，则该 bridge 必须 fail closed。

one-redundant repetition-line 公式与 normalized 小参数枚举只是 elementary/specialized checks，不是对 covering-code theory 的原创声明。
