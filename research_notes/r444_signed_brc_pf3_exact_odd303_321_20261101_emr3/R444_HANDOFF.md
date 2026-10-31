# R444｜可移植研究接续

核心结论：对 r=303,305,...,321 十行，已用任意精度整数完成 51,158,275 个 Schur/LR 归约子式全正检验，另有十个精确四阶负子式，因此十行 PF3\PF4。证据属于作者侧计算机辅助证明，尚待独立审阅。

所用已有程序（直接复用、未更改其数学定义）：
- R443_GENERATE.py 和 R443_PF4_WITNESS.py，固定参考 enterprise-math@81f4e314fa9dae6fbde8e0182ff1df4526b8025f，目录 research_notes/r443_signed_brc_pf3_odd203_301_20261101_emr3。
- R441 的 Schur/LR 有限完备归约，固定参考 enterprise-math@8fba98f1654ef4050ccc562be1ec197c01f31a47，目录 research_notes/r441_signed_brc_schur_lr_full_pf4_20261101_emr3。

复现：把上述 R443 两个 Python 文件与本目录的 R444_PF3_INTEGER.cpp、R444_SPOTCHECK.py 置于同一可写目录。
1. python3 R443_GENERATE.py 303 321 （生成 R443_INPUTS.txt；输出 10行、3110个等式；哈希见 R444_EVIDENCE.json）
2. head -n 5 R443_INPUTS.txt > rows_303_311.txt；tail -n 5 R443_INPUTS.txt > rows_313_321.txt。
3. g++ -O3 -std=c++17 R444_PF3_INTEGER.cpp -o r444_exact。
4. ./r444_exact rows_303_311.txt > check_A.txt；./r444_exact rows_313_321.txt > check_B.txt。两次程序必须返回退出码0及 R444_PF3_EXACT_PASS；预期 SHA256 分别 ebd494381817e5d036ff0b45c2dbaef0477c004b578f0d1a3304c9d00363d6ac、82521b629817a9325b78ac9293cecd42fdf1970f467ad478e686da95b134f57f。
5. python3 R443_PF4_WITNESS.py （读取 R443_INPUTS.txt，得到十个负证；文件 SHA256=c410552e48409dc00af994182234cffcc49ffcd3c5380c128ca5781bf052c538）。
6. python3 R444_SPOTCHECK.py （1,250个独立三阶交叉检验）。

R444_EXACT_STDOUT.txt 是两次成功运行的原始 stdout 顺序拼接；原始独立输出文件的哈希见证据 JSON。当前已完成集合 303—321 无需重复研究。下一个判别单元：在 r≥323 中查首个三阶负子式，或建立全部奇数 r≥99 三阶 Schur 行列式随 Catalan 参数的统一符号证明。

控制边界：本轮 GitHub 写入只用于保全作者侧材料，正式 RA/CLAIM/Result/Driver review 由当前授权角色及 Source 原生回执办理；P000 和 ACTIVE 世界观不变。signed 标量 Toeplitz 正性不能直接归到原生 X6。
