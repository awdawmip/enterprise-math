# C65 复算

从 [C65 中文研究笔记](C65_RESEARCH_NOTE.md) 开始。下载包中的 C65 和 C64 是相邻目录。从 C65 目录运行以下命令，使用 Python 3.12 和标准库。输出写入本地 rerun 目录，保留原始证书以便比较。

~~~bash
mkdir -p rerun
C64=../C64/checks
MODEL=../C64/inherited/certify_schedules.py
export PYTHONPATH="$C64"
python tv/tv_eight.py --c64 "$C64" --model "$MODEL" --output rerun/tv_eight.json
python tv/tv_ninth.py --c64 "$C64" --model "$MODEL" --output rerun/tv_ninth.json
python tv/check_high3500.py
python tv/native_ranks.py --c64 "$C64" --native-root ../C64/inherited --output rerun/native_ranks.json
python obs/observed_eight.py --model "$MODEL" --stocks "$C64/cut_stocks.json" --output rerun/observed_eight.json
python obs/readout_limits.py --model "$MODEL" --output rerun/readout_limits.json
python theory/verify_germs.py --model "$C64" --max-cut 10 > rerun/germs.json
python theory/verify_probe.py > rerun/probes.json
python locality/locality.py > rerun/locality.json
python locality/examples.py --c64 "$C64" --output rerun/examples.json
python - <<'PY'
from pathlib import Path
for result in sorted(Path("rerun").glob("*.json")):
    originals = [p for p in Path(".").glob("*/" + result.name) if p.parent != result.parent]
    assert len(originals) == 1 and originals[0].read_bytes() == result.read_bytes(), result
    print("OK", result.name)
PY
~~~

完整前八的有限部分采用动态规划给所有未保留词建立严格界，覆盖每个 $2\le k\le64$，而非在这些规模全部逐词展开。对于 $k\ge65$，可在 63 对库存处对全部输入区间统一比较，所有提前偏离的库存另有全域下界。germs.json 检验的是给定截面的全部后缀。展示小数用严格区间向外取整，表中相对代价极限为近似值。

原版 BRC 核取自 [项目提交 de41b8c](https://github.com/awdawmip/enterprise-math/tree/de41b8cd9e6b0ea52345d5f669af924f9379318a/src/enterprise_math)。仓库内 C63 模型位于 experiments/divisor_extrema/20261111_c63/numeric/certify_schedules.py。下载包还附有 [C63 唯一最优性证明](../C64/inherited/C63_NOTE.md)、[C64 三尾前四名](../C64/OBSERVED_RANKS.md)、[C64 固定 TV 名次](../C64/STABILIZATION.md)及[高段千倍分离证明](../C64/HIGH_1000.md)。仓库中的对应固定版本可从 C65 主文末尾进入。
