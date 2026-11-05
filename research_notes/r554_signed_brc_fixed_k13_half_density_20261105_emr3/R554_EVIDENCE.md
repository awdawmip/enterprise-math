# R554 执行证据｜2026-11-05

冻结模型：R462 signed BRC 辅助标量 `H_k(t), D_m(k)`；固定 k=13。Python3、SymPy 1.14.0。精确计算谓词为整数/有理数/有限域等式，候选根盘由数值探索产生后经严格不等式证书核验。

实际运行：`/mnt/data/R554_VERIFY.py`（与本目录独立压缩的验证器实现同一整数模型、同一根盘、同一Rouché/模素数证书；本目录脚本提交后的逐字重跑仍可作为下一次复核）。

```text
R554_RAW_H_PASS identities= 26 Catalan= 742900 p2= 23751
R554_EXACT_ROUCHE_PASS root_disks=25 disjoint_pairs=300 radius=1/1000
dominant_abs_gt=16 other_abs_lt=6 max_Rouche_ratio_lt_1/20= True ratio= 0.03862015663595715
R554_EXACT_MODULAR_CYCLOTOMIC_PASS p=65537 deg_R= 600 q_complete_bound= 720000 gcd_checks= 1173 max_candidate= 2730 runtime_s= 32.126
R554_EXACT_RECURRENCE_PASS 0<=m<=1024 plus= 514 minus= 511 zero= 0 adjacent_changes= 303
R554_FIXED_K13_HALF_DENSITY_EXACT_CERT_PASS
```

本目录精简 Rouché 程序改用半径 1/10000；本地同源精确 Gaussian-rational l1/l∞ 评价，最大右/左比例 0.005295679 < 3/500。两个根隔离半径分别有明确严格检验。

`R554_MODULAR.py` 使用精确 Möbius product 构造分圆多项式，避免高阶 SymPy 单次构造在特定 q 的性能瓶颈。有限域证明范围是全部 `φ(q)≤600` 的 `2≤q≤720000` 候选。

有限零项推论依据 Skolem–Mahler–Lech；不提供最后零项的上界。原生 CLAIM、Result 与独立 Driver 审阅遵守实际 Source 状态。

## 独立原始整数行列式复核

独立用 `[x^r](1-x)(1+x)^{2t}(1+x^2)^{r-t}` 的整数卷积计算 `H_k(t)`，再用 `SymPy Matrix.det(method='berkowitz')` 对 `m=1,...,16` 的原始 Toeplitz–Hessenberg 行列式逐一核验。与独立整数递推全部完全相等：

```text
R554_INDEPENDENT_BERKOWITZ_PASS k=13 m=1..16 signs=
[1,1,1,1,1,-1,-1,-1,1,1,1,1,-1,-1,-1,1,1]
```

此交叉检查从原始整数卷积开始，不调用根盘／有限域代码。检查范围为16个有限阶数；无限阶结论由上文两个精确证书及数学证明支持。
