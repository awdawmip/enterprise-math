# R439 可移植研究交接

原始 signed BRC 辅助模型 r=27 的半无限 Toeplitz PF₄ 完整有限归约已做完，四阶严格认证正 3,772,906,345 项，一至四阶合计3,780,201,126 项，原始五阶负子式为 −4879066184369172962162267144222813070669793907904000000000。因此最大 PF 阶数恰为4。数学论证、误差界和原始证据见本目录证明、源码、JSON 与八份分片日志。

复算：python R439_VERIFY.py；g++ -O3 -march=native -std=c++17 -fno-fast-math R439_PF4_R27_FAST.cpp -o r439fast；依次 ./r439fast 1 5、6 7、8 10、11 13、14 16、17 19、20 22、23 25；逐一和 R439_FAST_<a>_<b>.txt 比较。C++ 对适用 long double 环境检查；若不满足，需用纯整数计算重做四阶判号。

作者 GitHub 身份 awdawmip，规范 GLOBAL_KNOWLEDGE_V1 main@10597c4479f124884878d0d88d9eb657020bf264、Enterprise Math main@fc10280dbc1cb9ef929869cc3379f8bb31bf1d31。Source directed manifest 未授权，控制 Owner 查询 CONTROL_QUOTA；该保存不代表正式任务 CLAIM、Result、独立 Driver Review 或科学接纳，Research-Activity 待登记。

下一问题：r≥29 奇数行首次失去 PF₄ 的确切位置和最小内部稀疏负子式；结合 R432 已证 r≥99 奇数四阶障碍，寻找解析参数判号证书，避免进一步十亿级逐行穷尽。原生 X6/三维切片和更新映射仍需各自保真论证。P000/ACTIVE 世界观未修改。
