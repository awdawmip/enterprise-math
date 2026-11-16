# C76 复算与源材料

在解压目录使用 Python 3.9 或更高版本，以及支持 C++17 和无符号 128 位整数的 C++ 编译器。全部 Python 程序仅依赖标准库。请使用默认的 Python 断言设置。

```bash
python3 reproduce.py
```

上述命令核对归档文件的 SHA-256 并重跑表中所有整数证书。全库存的大区间枚举可用以下命令另行重做，输出按字节与逐库存记录比较。

```bash
c++ -O3 -std=c++17 two_blocks.cpp -o /tmp/c76_two_blocks
/tmp/c76_two_blocks 3101 3200 > /tmp/c76_verified_rows.txt
cmp /tmp/c76_verified_rows.txt finite_c3101_3200.txt
```

| 项目 | 复核对象 |
|---|---|
| check_adjacent、check_center_line、check_center_shape | 两个相邻外库存的割线、真假尾中心差、整数恢复、双解的单调分支 |
| check_tail_invariants、check_edge_slope | 端点倒数比的整数单射和同短首隙两次测量的斜率 |
| check_macro_point、check_macro_rectangle | 分支、并列线与边界，100个闭格用准确分数与整数平方根给外包络 |
| check_macro_alias、check_grid_drift | 连续并列曲线的两侧符号与横截导数，有限库存修正的符号 |
| ray_certificate、check_dyadic、check_polynomial_rays、check_center_anchor | 原整数积的二进赋值、模16的奇单位、完整有限残差、固定比例中心的前三阶系数 |
| check_finite、two_blocks.cpp | 单库存所有词的有限模证书，另用三态完整正分支复算小库存 |

建议先看 C76_RESEARCH_NOTE.md，再依其中的链接进入具体证明。所有百分比区域均按落点比例计。程序不能给出尚未数值化的大库存起点。
