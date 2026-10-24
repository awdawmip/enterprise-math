# R269 | 研究3 接续

- 固定问题：仿射效果 G 的有理反表示，在整个偶平移窗口 W_L={(ε,2j):|j|≤L,ε=±1} 上精确判断 k=0 的最小维数。
- 完成结果：对每个 L≥0，r_even(L) 为不小于 L+1 的最小奇数；证明含 Toeplitz 秩下界、偶数 N 的 rational-square obstruction、奇数阶群置换表示上界。
- 真实验证：同提交的 R269_verify_parity_window.js 实际运行，输出 EXACT_EVIDENCE.json；覆盖 L=0..12，无限定理由解析论证承担。
- 来源：GLOBAL_KNOWLEDGE_V1 main@a4331e69229a9558cc5d43300abb842a2d65e744；Enterprise Math main@7c783f61dce5b4442b1b45cbe70e4ab399a653ce；R267 作者侧证明@950c0d72c33132540a5762d73ef6990ef1079c14。
- 不足与范围：这是矩阵系数解码器的完整偶窗口结果，不是实际 R260 可达效果的六控制态下界；原生 R193/P000 保真未证明；Owner/正式 CLAIM/Driver 审查未取得，只有作者侧研究 GitHub 持久化。
- 下一任务：读取原始 R260 精确来源图，固定聚合自动机可比类，推导仅用真实可达 effect-fibre 的受限 Hankel 阻碍，或构造反例。
- GitHub 研究分支的内容不自动成为正式 Source Result、Working Truth、Foundation 或 P000。
