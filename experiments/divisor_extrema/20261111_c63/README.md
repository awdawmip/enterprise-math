# C63 复算说明

从 C63_RESEARCH_NOTE.md 开始阅读。完整证明含附录 A 与 B。balanced-gap 主定理为全 k 的唯一最优和 k≥3 的严格两倍间隔。binary/ 中另有二元间隙第二小值的证明，fiber/ 中是固定逆序数的全部极值词及同步例子。

使用 Python 3.10 或更新版本。证明所用的有理斜率与动态规划只依赖标准库；多项式展开脚本使用 SymPy。复算包附有原 C62 输入，解压后在本目录依次运行：

```bash
python numeric/certify_schedules.py 100 -o numeric/schedule_certificates.json --cut-output numeric/cut63_full.json
python numeric/extend_cut.py > numeric/cut63_extension.json
python global/check_empty_gaps.py
python global/check_gluing.py
python fiber/verify_fibers.py
python binary/check_local_extrema.py
python numeric/verify_against_c62.py inherited/prime_quantum_schedule_extrema_c62.zip
python crosscheck/check_fiber_brc.py inherited/prime_quantum_schedule_extrema_c62.zip
```

numeric/schedule_certificates.json 是对全部安排的下界证书。程序动态保留两个最小下界，对 A 使用原线性分式映射计算准确 TV。cut63_full.json 的 lower 栏存有理数；global/check_gluing.py 读取此栏并乘以证明使用的势函数。97 至 318 的计算向下取整。319 起的全部库存使用闭式，阈值 63、64、318、319 的用途见主文第 3–5 节。数值输出中的十进制显示为近似，判定使用严格有理比较。校验数据和生成脚本按子目录排列。

数学来源为用户提供的 C62 文件与对应的项目记录。活动登记及研究归档与外部独立评审分别记录。
