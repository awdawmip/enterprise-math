# C42复算包：非均匀路径与分组配平

2026-10-28；接续C41。先读RESEARCH_NOTE.md，再读results中的准确分数。

运行（Python 3.11+，需要SymPy）：

```sh
python run_checks.py
python scale_and_source_checks.py
```

核心代码biased_paths.py实现固定优先权的不放回因子选择、首项偏好、精确完整累计分布和方差公式。两份检查程序分别验证一般恒等式、分组充要条件、首项不变性、重复尺度留出及初始数。

底层权重调用继承的正有理BRC核，位于inherited/。每条因子词概率为正，负的累计观察不抵消概率。辅助幂分布仅用于自足证明，执行不用连续随机模拟。

正文定理范围：已知恒定路线差及固定准备律；相同优先权分组指参数准确相同。物理路径选择、心跳及机械稳定的对应另需依据。来源、独立审核状态及发布记录见SOURCE_PINS.json、PUBLICATION.json。
