# R544 精确运行证据

研究日期：2026-11-05（Asia/Shanghai）。在独立的本地 Python 运行时执行，不使用浮点数作认证断言。原科学输入冻结 R462 signed BRC。代码经 GitHub 远端回读后仍需保留相同 Python/SymPy 环境的可复现性；GitHub 保存和审阅与运行结论分别报告。

`python R544_VERIFY.py`:

```text
R544_EXACT_ROUCHE_PASS
k 6 degree 11 Catalan 132 p2 1365
coefficients P: 1,-18200,159882450,-842486995350,31311782726269500/11,-71002564336246725000/11,110410865769257580515625/11,-10749389748146715098671875,7805592584261393263792734375,-40469701786870541310040682812500/11,1018457650056753113720603466796875,-1390194692327468000228623732177734375/11
max_ratio 0.005696344638018389
dominant_lower 12879917717/2500000 other_upper 4136991/1000
recurrence signchanges_0_to256 71 first_changes [6, 9, 13, 16, 20, 23, 27, 31, 34, 38, 41, 45, 48, 52, 56, 59, 63, 66, 70, 73]
signs_m0_to40 ++++++---++++---++++---++++----+++----+++
```

`python R544_INDEPENDENT.py`:

```text
1 + digits 7
2 + digits 13
3 + digits 19
4 + digits 25
5 + digits 30
6 - digits 36
7 - digits 42
8 - digits 47
10 + digits 60
12 + digits 70
13 - digits 77
16 + digits 94
20 - digits 118
23 + digits 134
R544_INDEPENDENT_RAW_DET_PASS H=B checked 12 determinants 14
```

数学依赖：Toeplitz–Hessenberg 行列式展开、Rouché 定理、有限有理区间计算、非实主导复根 Cesàro 均值。全部11个圆盘和全部55对中心经精确计算覆盖；对无限阶的严格结论依据证明，不依赖 257 项数值样本。
