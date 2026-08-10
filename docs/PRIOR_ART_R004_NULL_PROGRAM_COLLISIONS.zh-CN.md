# 先行研究——R004 null-program history collision bridge

状态：`RESEARCH PRIOR-ART MAP / NOVELTY_UNVERIFIED`

补充 37 不主张 ordinary/joint/complete-joint/r-fold weight enumerator、Hamming-ball intersection、association-scheme 方法或 perfect-code uniqueness 为新数学。

## 来源

### SRC-R004-JOINT-WEIGHT-CHOIE-DOUGHERTY-KIM-2003

Choie、Dougherty、Kim，*Complete joint weight enumerators and self-dual codes*，IEEE Transactions on Information Theory 49(5), 1275–1282 (2003)，DOI 10.1109/TIT.2003.810649。

该文明确在 genus g 上定义 complete joint weight enumerator。R004 只消费同一成熟思想：多条 codewords 的 coordinate joint patterns 比单条 codeword 的 ordinary weight distribution 携带更多结构。

### SRC-R004-RFOLD-WEIGHT-SIAP-RAYCHAUDHURI-2000

Siap、Ray-Chaudhuri，*On r-fold Complete Weight Enumerator of r Linear Codes*，Contemporary Mathematics 259 (2000)，DOI 10.1090/conm/259/04118。

这是 multi-codeword / r-fold complete weight-enumerator structure 的直接先行工作。

## R004 当前 under-test package

R004 只保留 compiler/P011 bridge：

1. additive ISA 中的 bounded primitive programs 生成 P011 collision spectrum `W_k^prog`；
2. `d_min(C)>2D` 是 null-program quotient 的 exact bounded-history uniqueness gate；
3. ordinary null-code weight enumerator 足以恢复完整 pair-collision curve `W_2(D)`；
4. triangle / second-order joint profile 足以恢复 `W_3(D)`，ordinary enumerator 不够；
5. 一般 `(k-1)`-fold joint coordinate profile 是 `W_k(D)` 的 exact sufficient state。

这套 Enterprise Math packaging 与 selected finite counterexample 的历史 novelty 仍未验证。
