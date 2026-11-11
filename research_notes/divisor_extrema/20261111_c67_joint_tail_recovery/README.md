# C67 复算

[中文研究笔记](C67_RESEARCH_NOTE.md) 给出三尾反演、确定性局部识别、混合等价和额外制备的证明索引。压缩包内 C64、C65、C66、C67 四个相邻目录构成此次复算环境。原三态正权核及 C62、C63 研究记录在 C64/inherited。使用 Python 3.12；交换的多项式因式分解、结式与符号证书使用 SymPy 1.14。原读数全量阈值比较和大叶集模筛还需要 g++ 支持 C++17、IEEE 754 binary64 和无符号 128 位整数。

以下从 C67 目录执行。每项结果 JSON 包含证书范围、准确分数、余数筛或正性系数的核验结果。全量逆查询要逐一比较 9,826,097,651 个保留末叶；其余证明可单独复算。

~~~bash
mkdir -p rerun
MODELDIR=../C64
CHECKDIR="$MODELDIR/checks"
NATIVEDIR="$MODELDIR/inherited"
python exchange/complete_exchange.py --checks "$CHECKDIR" > rerun/complete_exchange.json
python exchange/small_moves.py --c66 ../C66/exchange > rerun/small_moves.json
python exchange/opposite.py > rerun/opposite.json
python joint/mixed_kernel.py --native-root "$NATIVEDIR" > rerun/mixed_kernel.json
python joint/last_gap.py --c64 "$CHECKDIR" > rerun/last_gap.json
python joint/convex_obstruction.py --c64 "$CHECKDIR" > rerun/convex_obstruction.json
python adic/verify_templates.py > rerun/templates.json
python adic/native_witness.py --native-root "$NATIVEDIR" > rerun/native_witness.json
python inverse/upper_frontier.py --checks "$CHECKDIR" --inherited "$NATIVEDIR" --output rerun/upper_frontier.json
python inverse/threshold_count.py --checks "$CHECKDIR" --inherited "$NATIVEDIR" --frontier rerun/upper_frontier.json --output rerun/threshold_count.json
python inverse/singleton_count.py --checks "$CHECKDIR" --inherited "$NATIVEDIR" --frontier rerun/upper_frontier.json --output rerun/singleton_count.json
python inverse/census_threshold.py --checks "$CHECKDIR" --inherited "$NATIVEDIR" --frontier rerun/upper_frontier.json --direct rerun/threshold_count.json --output rerun/census_threshold.json
python inverse/inverse_grid.py --checks "$CHECKDIR" --inherited "$NATIVEDIR" --output rerun/inverse_grid.json
python inverse/native_threshold.py --frontier rerun/upper_frontier.json --grid rerun/inverse_grid.json --output rerun/native_threshold.json
python - <<'PY'
from pathlib import Path
for f in sorted(Path('rerun').glob('*.json')):
    targets=[p for base in ('exchange','joint','adic','inverse') if (p:=Path(base)/f.name).is_file()]
    assert len(targets)==1 and f.read_bytes()==targets[0].read_bytes(), f.name
    print('OK', f.name)
PY
~~~

- [一般库存的相邻交换](exchange/EXCHANGE.md)
- [高库存的确定性重排](adic/RIGID_TEMPLATES.md)
- [最后两隙的全库存识别与分辨率](joint/LAST_GAP.md)
- [两列凸包的边界](joint/CONVEX_OBSTRUCTION.md)
- [原质量混合与双制备反演](joint/PREPARATIONS_AND_MIXTURE.md)
- [原始标量的无界规模反查](inverse/INVERSION.md)
