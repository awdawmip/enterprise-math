# C75 复算

在解压目录使用 Python 3.9 或更高版本及支持 C++17、无符号 128 位整数的 C++ 编译器。Python 复算仅用标准库。运行以下命令可核对记录、两类校准的全部整数多项式系数证书、二次窗口、2 进残差及三状态短路径。不开启 Python 的 -O 选项。

```bash
python3 reproduce.py
```

另可重新逐库枚举 100 个新增库存，将结果逐字节与记录比较。一次只保留一个库存的模值。C++ 代码为 C74 程序的相同字节，区间改由命令行指定。

```bash
c++ -O3 -std=c++17 two_blocks.cpp -o /tmp/c75_two_blocks
/tmp/c75_two_blocks 3001 3100 > /tmp/c75_verified_rows.txt
cmp /tmp/c75_verified_rows.txt finite_c3001_3100.txt
```

`near_sync_controls.py` 按每行夹住同步的两个整数位置查完闭窗口。两个 Newton 证书均有已证明的多项式次数界。有限差分非负、首系数严格正即可推出整个整数半轴的严格正性。各尺寸另存计算摘要，供复算比较。 `check_pointwise.py` 与 `check_macro.py` 对照准确端点、截断中心、残差和导数。两个解析定理的无限量词由相应证明给出。

C74 的模型约定、前件与上下界的固定来源列于 C75_RESEARCH_NOTE.md。提交中的文本与 zip 内各文件相同；SHA256SUMS 是文件的逐项摘要。
