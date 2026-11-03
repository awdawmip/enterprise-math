# R499 → 下一研究单元
Date: 2026-11-03. Mode: TASK research, author-side durable draft. Source: frozen R462 pin `18783e01e3646c72b7aab3b16d3f565e83e6446f`.

**已完成且不重做**：R499 在 R498 之后将 s=3,m=22 的 Toeplitz 行列式完全分类：
D22>0 for 1<=k<=5 and k>=9; D22<0 for 6<=k<=8.
Exact polynomial degree 43, normalizing factor G22, full 44-coefficient shifted sign witness at k=9, all 8 finite boundary values, reproducible checker and evidence are stored in this folder.
Scientific evidence state: author-side exact computer-assisted proof; not an authenticated Result or independent Driver acceptance. P000 and worldview unchanged.

**下一独立单元**：用相同冻结 p_t(k) 及 Hessenberg 递推求 s=3,m=23 的本原多项式，验证正因子整除、寻找严格移位系数证书并完整穷举有限前缘。若单次移位系数证书不足，采用有理 Sturm 分离或 Bernstein 区间证书，而非猜测无限符号。对固定 k=2 的生成函数 1/(1-84z+2205z²-25725z³) 单独研究根与秩振荡，区分有限参数和统一参数结论。

**持久来源**：PR #1708 当前分支的 R499_PROOF.zh-CN.md、R499_VERIFY.py、R499_EVIDENCE.json。复用更早 R498 证明与其证据（commit `2cc1acfcdf28e0d73aa1d2d1fba2e2a13c424bf7`）。活跃 Owner 查询与原生会话启动需根据本轮真实回执独立核对；本稿不授予 CLAIM、Result 或 Review。
