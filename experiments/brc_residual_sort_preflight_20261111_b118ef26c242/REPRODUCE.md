# 复现步骤

本包包含本次三轮实现、实际原始计时、诊断、整数概率脚本、计时之外的结构诊断，以及固定在 46352a6399b785a169d997fbfedc5043c5fe6f7f 的第四轮原复现包。运行环境为 Linux、g++ 14.2.0、C++20、Python 3，性能运行使用 -O3 -march=native。绘图还使用 matplotlib。

从本包根目录运行以下命令，CPU 编号可替换成当前进程允许的一个物理执行位置。基准应串行运行。指定新的输出目录可保留随包的原始数据。

```bash
mkdir -p recovered/src
unzip -oq baseline_phase4.zip -d recovered/src
python3 phase5/build.py recovered/src
taskset -c 0 phase5/build/bench replay5
python3 phase5/summarize.py replay5
python3 phase6/build6.py recovered/src
taskset -c 0 phase6/build/bench6 replay6
python3 phase6/summarize6.py replay6
python3 phase7/build7.py recovered/src
taskset -c 0 phase7/build/bench7 replay7
python3 phase7/summarize7.py replay7
python3 gaps/run.py recovered/src
bash phase7/verify.sh recovered/src
bash phase5/verify.sh recovered/src
bash phase6/verify.sh recovered/src
bash phase5/sweep.sh recovered/src
```

第五轮输入编号为 0–7，第六轮使用 32–39，第七轮使用 64–71，生成器、固定种子和打乱算法顺序都写在相应的 bench.cpp 或 bench6.cpp 内。每种方法对同一数组运行五次。各输入先取五次计时中位数，再取八组输入的中位数。bank_pairs.csv 提供相同输入上的速度比和胜出次数。每轮的 timings.csv 保存每次计时（纳秒），nodes.csv 保存独立诊断。每次实际排序都与标准排序的完整数组逐项核对，计时剔除答案核对，包含输入复制和临时数据析构。

运行概率计算的方法见 theory3 中两份中文推导和 Python 脚本。两份理论的概率条件是理想均匀候选位置；实际程序用固定伪随机种子便于重放。plot_results.py 从本包所附结果重建 results.png。

验证脚本各自运行优化及 ASan/UBSan 两种构建。当前沙箱的 LeakSanitizer 退出检查与宿主跟踪冲突，复跑使用 ASAN_OPTIONS=detect_leaks=0，同时保留 AddressSanitizer 和 UndefinedBehaviorSanitizer。第四轮旧入口被适配为普通函数时编译器会提示缺少显式 return，新的测试没有调用那个适配入口。
