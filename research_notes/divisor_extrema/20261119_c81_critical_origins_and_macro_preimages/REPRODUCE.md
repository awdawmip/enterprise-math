# 复算 C81

相邻库存的准确原 H(0,1) 与归一谱使用以下已固定的项目版本。[C78](https://github.com/awdawmip/enterprise-math/tree/24881e361378245e45f27919836ca1c9db48d04f/research_notes/divisor_extrema/20261116_c78_nearby_stock_precision) · [C79](https://github.com/awdawmip/enterprise-math/tree/9d76acb849471e4b8c411a5de04066679abca8d8/research_notes/divisor_extrema/20261116_c79_critical_window_geometry) · [C80](https://github.com/awdawmip/enterprise-math/tree/441853d82f262cceb29b631c737d67b9b79910f9/research_notes/divisor_extrema/20261118_c80_critical_offsets_and_thresholds)

解压后在 C81 目录中执行。Python 3、NumPy、Matplotlib、mpmath 和支持 128 位整数的 C++17 编译器足以重建所有结果。下列命令的 replay 文件均可重新生成。

1. 检查发布文件和六重原像的有理端点。

   ~~~sh
   sha256sum -c SHA256SUMS
   python check_six.py
   ~~~

2. 复核宏观单原像区域。每次向外包围；报告采用四档的最大档。独立程序可在 region_check 下运行，读取该目录的 REGION_CHECK.md。plot_region.py 使用认证方格及解析面积画出宏观源域。

   ~~~sh
   python certify_region.py 32 64 128 256 --output replay_regions.json
   cmp replay_regions.json region_cells.json
   python plot_region.py
   ~~~

3. 复核全体格原点的极值、积分与方差分解。独立原始三态路径校验覆盖 c=4,6,8 的全部 1,146 个原点矩形。另有 48 组合成目录。

   ~~~sh
   cd profile
   g++ -O3 -std=c++17 phase_slabs.cpp -o phase_slabs
   python check_components.py
   python check_native.py
   python phase_components.py 32 48 64 512 768 1024 --output replay.json
   cmp replay.json phase_components.json
   cd ..
   ~~~

4. 复核逐条安排的状态及抵消比例。单独的 c=8 原始模型检查包含 28 个标签、841 个格原点矩形，另有 203 个能逐格穷举的合成目录。

   ~~~sh
   cd individual
   g++ -O3 -std=c++17 individual.cpp -o individual
   python test_individual.py
   python test_native_origins.py
   python individual.py 8 16 24 32 64 128 256 512 1024 --output replay.json
   cmp replay.json individual_profiles.json
   python check_common_counts.py
   ~~~

region_cells.json 与逐目录的其他 JSON 保存整数格号、严格向外的数值包围或逐格编号。有限扫描与连续极限证明是两种独立证据。所有临界结论的参数与量词见 C81_RESEARCH_NOTE.md、REGULAR_SHEETS.md 及 NEAR_AND_FAR.md。
