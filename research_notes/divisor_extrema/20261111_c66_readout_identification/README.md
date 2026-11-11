# C66 复算

[中文研究笔记](C66_RESEARCH_NOTE.md) 汇总结论及证明链接。下载包包含 C64、C65、C66 三个相邻目录。下列命令从 C66 目录运行。使用 Python 3.12 标准库，大枚举另需支持 128 位整数的 C++17 编译器 g++。其余证书可分别复算。

~~~bash
mkdir -p rerun
C64=../C64/checks
NATIVE=../C64/inherited
export PYTHONPATH="$C64"
python arithmetic/single_readout.py --model "$C64" --full 16 --cut 16 --output rerun/single_readout.json
python arithmetic/native_samples.py --model "$C64" --native-root "$NATIVE" --output rerun/native_samples.json
python arithmetic/inverse_readout.py --model "$C64" --output rerun/inverse_readout.json
python inputs/verify_inputs.py --checks "$C64" --prior ../C65/theory > rerun/inputs.json
python inputs/native_tie.py --native-root "$NATIVE" --certificate inputs/inputs.json > rerun/native_tie.json
python exchange/verify_exchange.py > rerun/exchange.json
python rigidity/verify_rigidity.py --c64 "$C64" > rerun/rigidity.json
python onset/observed_ninth.py --model "$NATIVE/certify_schedules.py" --stocks "$C64/cut_stocks.json" > rerun/observed_ninth.json
python onset/delayed_winner.py > rerun/delayed_winner.json
python - <<'PY'
from pathlib import Path
for f in sorted(Path('rerun').glob('*.json')):
    originals=[p for p in Path('.').glob('*/'+f.name) if p.parent!=f.parent]
    assert len(originals)==1 and originals[0].read_bytes()==f.read_bytes(), f
    print('OK', f.name)
PY
~~~

主枚举以余数排序验证给定素域上没有重合，跨规模归并也检验相邻值。规模 16 的主检验约需 3.5 GB 可用内存；运行时间取决于硬件。每个结果 JSON 记录定理所用的分数、规模、计数或向外舍入的界，大枚举存储汇总和可由代码重建的排序证书。单个逆查询示例为以下命令。

~~~bash
python arithmetic/inverse_readout.py --model "$C64" --H 269335961/264606236 --output inverse_query.json
~~~

- [有限读数区分证书](arithmetic/EXACT_READOUT.md)
- [无界规模的完整逆查询和全局最大值](arithmetic/INVERSE.md)
- [输入并列曲线与测量精度](inputs/INPUT_SEPARATION.md)
- [首隙全尺度解码](rigidity/RIGIDITY.md)
- [局部两隙交换](exchange/EXCHANGE.md)
- [原三尾第九名](onset/OBSERVED_NINTH.md)
- [二分类读数的换位和阶乘四次分差](onset/DELAYED_WINNER.md)
