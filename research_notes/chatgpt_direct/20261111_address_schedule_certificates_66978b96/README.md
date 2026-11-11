# 指定绑定地址与逐槽寿命证据

研究报告从 `REPORT.zh-CN.md` 阅读。当前目录的新代码以 Python 标准库运行。在独立复验包中，本目录是 `schedule/`，父目录还提供未改动的原程序与上轮适配。运行环境为 Python 3.12；不需要第三方 Python 包。

从独立复验包根目录依次执行：

```bash
python3 schedule/certificate_checks.py
python3 schedule/rotation_checks.py
python3 schedule/saturated.py
python3 schedule/planner_checks.py
python3 schedule/kernel_checks.py
```

| 主文件 | 内容与范围 |
|---|---|
| lifetime_certificates.py / certificate_checks.py | 完整身份、任意预定目标和地址的逐准备公式，按兼容全键域进行独立顺序查验、提示失败的回退，以及独立统一最坏递推。只计额外原位读取与已知随键权重，业务常数按原字另加。 |
| lifetime_proof.md / schedule_planner.py / planner_checks.py | 余数接口的按地址置换和按最后阻挡期限合并、容量及静态对抗见证，有限比较实际覆盖见 planner_results.json。 |
| rotation_proof.md / rotation_checks.py | 轮转精确式、不规则写址下闭区间、被停放的便宜键、增加一键时的最短特例，以及给定库存的两费率计算。 |
| saturated.py / saturated_results.json | 初始合法标签恰有一空位：按实际输出序列区分日程必须保留的地址，独立枚举、比较。 |
| kernel_checks.py / kernel_notes.md | 通过既有原业务字实际读位、按目标创建、地址绑定、释放。列出受保护执行和遗漏试验的明确覆盖范围。 |
| *_results.json | 对应控制或原核程序的输出。不同层级或不同初始域的数字勿相加。 |

长日程按轮核对每一个真实业务边界，发放材料只保留可由程序再算的紧凑收据。测试器的旧全表仅用于准备和语义核验；真实路径的控制器只收到位读取布尔及业务写入。私有仓库科学父源与运行文件沿革见 PROVENANCE.json。各文件中相对路径按独立复验包布局解释。
