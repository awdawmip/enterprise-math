#!/usr/bin/env python3
"""Predeclared deterministic weighted-sign BRC continuation, with full trajectories.

No random sampling or independent physical observations are claimed. Degree-two
production BRC is reused for rational early-time validation, and the necessary
fourth-moment extension is kept local to this experiment.
"""
from __future__ import annotations

import argparse
import csv
from fractions import Fraction as F
import gzip
import hashlib
import io
import json
from math import comb
from pathlib import Path
import platform
import sys

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))
from enterprise_math.brc_transport import Affine, EffectHistogram, MomentState, eye

PARAMETERS = ("-1", "-0.75", "-0.6", "-0.51", "-0.5", "-0.49", "-0.4", "-0.3",
              "-0.26", "-0.25", "-0.24", "-0.2", "-0.1", "0", "0.25", "0.5", "1", "2")
HORIZON = 131072
TRAIN_WINDOWS = ((1, 16), (129, 512), (2049, 8192), (8193, 32768))
PRIOR_COMMIT = "46bd4dbe07fa0a7b5b92f612b16b68b70d48e45c"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def numeric_trajectory(p_text, horizon):
    """Long-double positive prefix sums, rounded to binary64 for fits/exports."""
    n = np.arange(1, horizon + 1, dtype=np.longdouble)
    p = np.longdouble(p_text)
    s2 = np.asarray(np.cumsum(n ** (2*p), dtype=np.longdouble), dtype=np.float64)
    s4 = np.asarray(np.cumsum(n ** (4*p), dtype=np.longdouble), dtype=np.float64)
    gamma = -2*s4/s2**2
    return np.asarray(n, dtype=np.float64), s2, s4, gamma


def regime(p_text, n):
    p = F(p_text)
    if p < F(-1, 2):
        return {"name": "plateau", "time_power": 0, "width_power": None,
                "leading_gamma": "-2*zeta(-4*p)/zeta(-2*p)^2",
                "shape": np.ones_like(n)}
    if p == F(-1, 2):
        return {"name": "critical_variance_log", "time_power": 0, "width_power": 4,
                "leading_gamma": "-2*zeta(2)/(log(n))^2",
                "shape": np.log1p(n)**-2}
    if p < F(-1, 4):
        beta = float(4*p+2)
        return {"name": "fractional_time_power", "time_power": beta, "width_power": 4,
                "leading_gamma": "-2*zeta(-4*p)*(2*p+1)^2*n^(-4*p-2)",
                "shape": n**-beta}
    if p == F(-1, 4):
        return {"name": "critical_fourth_log", "time_power": 1, "width_power": 4,
                "leading_gamma": "-log(n)/(2*n)", "shape": np.log1p(n)/n}
    return {"name": "inverse_time", "time_power": 1, "width_power": float(2/(2*p+1)),
            "leading_gamma": "-2*(2*p+1)^2/(4*p+1)/n", "shape": 1/n}


def fit_errors(y, predicted, start, end):
    sl = slice(start-1, end)
    target, pred = y[sl], predicted[sl]
    error = pred-target
    return {"start": start, "end": end, "points": end-start+1,
            "relative_rmse": float(np.sqrt(np.sum(error**2)/np.sum(target**2))),
            "rmse": float(np.sqrt(np.mean(error**2))),
            "max_absolute_error": float(np.max(np.abs(error))),
            "max_absolute_relative_error": float(np.max(np.abs(error/target))),
            "final_prediction_over_observed": float(pred[-1]/target[-1])}


def fit_all(n, s2, s4, y, theoretical):
    neff = s2*s2/s4
    width = np.sqrt(s2)
    shapes = {"constant": np.ones_like(n), "inverse_time": 1/n,
              "inverse_time_squared": 1/n**2, "inverse_neff": 1/neff,
              "theoretical_regime": theoretical["shape"], "inverse_width_squared": 1/s2}
    records = []
    for start, end in TRAIN_WINDOWS:
        sl = slice(start-1, end)
        for name in (*shapes, "free_time_power", "free_width_power"):
            rec = {"candidate": name, "train_start": start, "train_end": end,
                   "train_points": end-start+1}
            if name in shapes:
                shape = shapes[name]
                amplitude = float(np.dot(shape[sl], y[sl])/np.dot(shape[sl], shape[sl]))
                prediction = amplitude*shape
                rec.update(amplitude=amplitude, fitted_exponent=None,
                           fit_objective="unweighted response-space least squares, no intercept")
            else:
                x = np.log(n if name == "free_time_power" else width)
                z = np.log(-y)
                xc, zc = x[sl]-np.mean(x[sl]), z[sl]-np.mean(z[sl])
                slope = float(np.dot(xc, zc)/np.dot(xc, xc))
                intercept = float(np.mean(z[sl])-slope*np.mean(x[sl]))
                amplitude = -float(np.exp(intercept))
                prediction = -np.exp(intercept+slope*x)
                rec.update(amplitude=amplitude, fitted_exponent=-slope,
                           fit_objective="unweighted log(-gamma)-space least squares; sign fixed negative")
            rec["training_metrics"] = fit_errors(y, prediction, start, end)
            rec["heldout_all_later"] = fit_errors(y, prediction, end+1, len(n))
            rec["heldout_next_block"] = fit_errors(y, prediction, end+1, min(4*end, len(n)))
            rec["heldout_far_half"] = fit_errors(y, prediction, len(n)//2+1, len(n))
            records.append(rec)
    return records


def high_precision_checks(p_text, n, s2, s4, gamma):
    """Independent Hurwitz-zeta/digamma finite sum, checked by direct small sum."""
    mp.mp.dps = 80
    p = mp.mpf(p_text)
    def power_sum(exponent, count):
        if exponent == -1:
            return mp.digamma(count+1)+mp.euler
        return mp.zeta(-exponent)-mp.zeta(-exponent, count+1)
    for q in (2*p, 4*p):
        direct = mp.fsum(mp.power(j, q) for j in range(1, 17))
        assert mp.almosteq(direct, power_sum(q, 16))
    rows = []
    for count in (1, 16, 512, 8192, 32768, len(n)):
        ref2, ref4 = power_sum(2*p, count), power_sum(4*p, count)
        refgamma = -2*ref4/ref2**2
        row = {"n": count}
        for key, actual, ref in (("variance", s2[count-1], ref2),
                                 ("sum4", s4[count-1], ref4),
                                 ("gamma4", gamma[count-1], refgamma)):
            relative = float(abs(mp.mpf(float(actual))/ref-1))
            assert relative < 5e-13, (p_text, count, key, relative)
            row[key+"_relative_error"] = relative
            row[key+"_80digit_reference"] = mp.nstr(ref, 80)
        rows.append(row)
    return rows


def exact_checks():
    counts = {"rational_parameter_paths": 0, "brc_degree_two_points": 0,
              "fourth_moment_recurrence_points": 0, "explicit_distribution_points": 0}
    for p in (-1, 0, 1, 2):
        state = MomentState.from_point((0,))
        raw = [F(1), F(), F(), F(), F()]
        dist = {F(): F(1)}
        s2, s4 = F(), F()
        n_float, sum2_float, sum4_float, gamma_float = numeric_trajectory(str(p), 64)
        for n in range(1, 65):
            a = F(n)**p
            packet = EffectHistogram.from_terms(1, [
                (F(1, 2), Affine(eye(1), (sign*a,)), 1) for sign in (-1, 1)])
            state = state.then(packet)
            innovation = [F(1), F(), a*a, F(), a**4]
            raw = [sum((F(comb(k, j))*raw[j]*innovation[k-j]
                        for j in range(k+1)), F()) for k in range(5)]
            s2 += a*a
            s4 += a**4
            assert state.to_matrix() == ((s2, F()), (F(), F(1)))
            assert raw == [F(1), F(), s2, F(), 3*s2*s2-2*s4]
            exact_gamma = (raw[4]-3*raw[2]**2)/raw[2]**2
            assert abs(gamma_float[n-1]/float(exact_gamma)-1) < 5e-13
            counts["brc_degree_two_points"] += 1
            counts["fourth_moment_recurrence_points"] += 1
            if n <= 8:
                nxt = {}
                for value, prob in dist.items():
                    for sign in (-1, 1):
                        target = value+sign*a
                        nxt[target] = nxt.get(target, F())+prob/2
                dist = nxt
                direct = [sum((prob*value**k for value, prob in dist.items()), F())
                          for k in range(5)]
                assert direct == raw
                counts["explicit_distribution_points"] += 1
        counts["rational_parameter_paths"] += 1
    return counts


def export_trajectory(path, p, n, s2, s4, gamma):
    with path.open("wb") as output:
        with gzip.GzipFile(filename="", fileobj=output, mode="wb", mtime=0, compresslevel=6) as binary:
            with io.TextIOWrapper(binary, encoding="utf-8", newline="") as text:
                writer = csv.writer(text, lineterminator="\n")
                writer.writerow(("p", "n", "variance", "sum_fourth_weights", "gamma4", "effective_count"))
                for j in range(len(n)):
                    writer.writerow((p, j+1, format(s2[j], ".17g"), format(s4[j], ".17g"),
                                     format(gamma[j], ".17g"), format(s2[j]**2/s4[j], ".17g")))
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": digest(path),
            "data_rows": len(n), "gzip_mtime": 0}


def summarize_path(p, n, s2, s4, gamma, theory, fits):
    samples = sorted(set([1, 2, 3, 4, 8, 16, 32, 64, 128, 129, 256, 512, 1024, 2048,
                          2049, 4096, 8192, 8193, 16384, 32768, 65536, len(n)]))
    rows = [{"n": j, "variance": float(s2[j-1]), "sum_fourth_weights": float(s4[j-1]),
             "gamma4": float(gamma[j-1]), "effective_count": float(s2[j-1]**2/s4[j-1]),
             "rms_width": float(np.sqrt(s2[j-1]))} for j in samples]
    beta = -float(np.log(abs(gamma[-1]/gamma[len(n)//2-1]))/np.log(2))
    alpha = -float(np.log(abs(gamma[-1]/gamma[len(n)//2-1])) /
                   np.log(np.sqrt(s2[-1]/s2[len(n)//2-1])))
    return {"p": p, "regime": {k: v for k, v in theory.items() if k != "shape"},
            "width_fit_interpretation": ("finite-width trajectory slope; no unbounded-width asymptotic interpretation"
                                         if F(p) < F(-1, 2) else "unbounded RMS width"),
            "samples": rows, "final_dyadic_time_exponent": beta,
            "final_dyadic_width_exponent": alpha,
            "free_time_exponent_by_train": [r["fitted_exponent"] for r in fits
                                             if r["candidate"] == "free_time_power"],
            "free_width_exponent_by_train": [r["fitted_exponent"] for r in fits
                                              if r["candidate"] == "free_width_power"]}


def render_report(out, result):
    lines = ["# 幂权重长时域拟合：18 条确定性轨迹与临界区间", "",
             "日期：2026-10-02（Asia/Shanghai）  ",
             "Researcher-ID：EM-BRCWEIGHT-9D72AC；直接 TASK_RESEARCH，非 Driver 裁定。", "",
             "本轮沿用独立对称符号模型 `X_n=Σ j^p ε_j`，每条轨迹扩展到 `n=131072`。",
             "18 个参数共保存 **2,359,296 个逐时点数值记录**；同一轨迹的时间点相依，",
             "这是声明模型的确定性矩计算，不是 236 万份独立实验、蒙特卡洛样本或真实世界观测。", "",
             "## 定义与解析分区", "",
             "设 `S2=Σj^(2p)`、`S4=Σj^(4p)`、`ell=sqrt(S2)`。独立性给出", "",
             "    Var(X_n)=S2; kappa4=-2*S4; gamma4=-2*S4/S2²=-2/N_eff", "    N_eff=S2²/S4", "",
             "把 `Σj^q` 的收敛、对数和幂次三种情况分别代入，得到下列渐近分区。",
             "这是已声明模型的代数推导；数值拟合用于检验进入渐近区间的速度，不宣称盲发现。", "",
             "| p 范围 | gamma4 的领先项 | 按 RMS 宽度的形态 |", "|---|---|---|",
             "| p < −1/2 | −2 ζ(−4p)/ζ(−2p)² | 宽度有限，残差非零常数 |",
             "| p = −1/2 | −2 ζ(2)/(log n)² | −2 ζ(2) ell^−4 |",
             "| −1/2 < p < −1/4 | −2 ζ(−4p)(2p+1)² n^(−4p−2) | −2 ζ(−4p) ell^−4 |",
             "| p = −1/4 | −log n/(2n) | ell^−4 乘对数修正；领先为 −8 log(ell)/ell^4 |",
             "| p > −1/4 | −2(2p+1)²/[(4p+1)n] | 幂指数 2/(2p+1)，连续依赖 p |", "",
             "因此等幅 p=0 的 ell^−2 是该家族中的一个参数值，p=1 的 ell^−(2/3) 也只是其中一个。",
             "接近临界 p 的有限时拟合不能代替这些分区；即使算到十万步，也可能尚未接近极限指数。", "",
             "## 预声明拟合设计", "",
             "参数：`"+", ".join(PARAMETERS)+"`。训练窗口为 `1..16`、`129..512`、",
             "`2049..8192`、`8193..32768`；每个窗口独立拟合，然后外推至 131072。",
             "每次留出均严格晚于本次训练，但不同拟合的窗口彼此重叠，不能相加为独立验证。",
             "候选为常数、C/n、C/n²、自由时间幂、C/N_eff、对应解析分区形状、自由宽度幂及 C/ell²。",
             "其中 C/ell² 直接对应用户原命题，在首轮数据扫描期间、查看拟合结果前追加；",
             "原七候选在扫描前已声明，不把这个追加候选的源代码时间倒写为扫描前冻结。",
             "固定形状用原响应空间无截距最小二乘；自由幂用 log(−gamma4) 空间最小二乘，符号固定为负。",
             "因此候选的训练目标不同，表格用于外推误差比较，不把训练目标混为同一优化问题。",
             "临界形状使用 log(n+1)，避免训练点 n=1 的 log 奇异；与表中领先渐近式等价但有限值不同。",
             "C/N_eff 使用已知权重计算的未来 N_eff，且 gamma4 由同一恒等式得到；它是结构一致性检查，",
             "不是只凭早期 gamma4 对未知机制的盲预测，也不是独立交叉核验。",
             "另行保存全部晚期区间、随后四倍区间和最远半段的误差，不按留出误差择模后再声称盲验证。", "",
             "误差分母明确为 `relative_RMSE=sqrt(Σ(pred−obs)²/Σobs²)`，求和只跨指定测试窗口；",
             "它是窗口整体归一化误差，并非逐点百分比误差的平均。p<−1/2 时宽度有界，",
             "即使自由宽度幂的数值斜率能计算，也没有无限宽度渐近指数的含义；JSON 已明确标记。",
             "另存最大逐点相对误差、RMSE、",
             "最大绝对误差及终点预测/观测比。零方差未出现，因为首个权重为 1。", "",
             "## 指数稳定性与晚期外推", "",
             "下表自由幂指数 β 对应 `gamma4≈C n^−β`；前三个训练窗口与最后窗口的值都保留。",
             "最后两列为最后训练窗口在 `32769..131072` 的整体相对 RMSE。", "",
             "| p | β：1..16 | β：129..512 | β：2049..8192 | β：8193..32768 | 极限时间指数及修正 | 自由幂误差 | 分区形状误差 |",
             "|---:|---:|---:|---:|---:|---|---:|---:|"]
    for item in result["paths"]:
        p = item["p"]
        fits = result["fits"][p]
        free = next(x for x in fits if x["train_end"] == 32768 and x["candidate"] == "free_time_power")
        reg = next(x for x in fits if x["train_end"] == 32768 and x["candidate"] == "theoretical_regime")
        name = item["regime"]["name"]
        limit = str(item["regime"]["time_power"])
        if name == "critical_variance_log": limit = "0；(log n)^−2"
        if name == "critical_fourth_log": limit = "1；乘 log n"
        betas = " | ".join(f"{x:.6f}" for x in item["free_time_exponent_by_train"])
        lines.append(f"| {p} | {betas} | {limit} | {free['heldout_all_later']['relative_rmse']:.6g} | {reg['heldout_all_later']['relative_rmse']:.6g} |")
    lines += ["", "临界附近出现具体的误导风险：p=−0.49 的极限时间指数为 0.04，",
              "但最后训练段仍拟合为约 0.214；这个自由幂的晚期留出误差只有约 1.90%。",
              "有限时外推相当准确，仍不足以确定极限指数。p=−0.51 最终应为常数，",
              "最后训练段却仍呈约 0.174 的衰减指数；不能把阈值两侧的慢交叉当成新普遍幂律。", "",
              "下表直接比较原命题 C/ell²；训练为 8193..32768，留出为 32769..131072。",
              "p=−0.25 的宽度指数有对数修正，3.615 是窗口拟合值，不是精确渐近指数。", "",
              "| p | 自由宽度幂指数 α | C/ell² 相对 RMSE | 自由宽度幂相对 RMSE |",
              "|---:|---:|---:|---:|"]
    for item in result["paths"]:
        if item["p"] not in ("-0.49", "-0.25", "-0.1", "0", "0.25", "0.5", "1", "2"):
            continue
        last = {r["candidate"]: r for r in result["fits"][item["p"]] if r["train_end"] == 32768}
        lines.append(f"| {item['p']} | {last['free_width_power']['fitted_exponent']:.9f} | "
                     f"{last['inverse_width_squared']['heldout_all_later']['relative_rmse']:.6g} | "
                     f"{last['free_width_power']['heldout_all_later']['relative_rmse']:.6g} |")
    lines += ["", "## 数值完整性与复现", "",
              "长时计算用 NumPy longdouble 的正项累加，再转为 binary64 拟合及 17 位有效数字导出；",
              "gamma4 直接由累积量公式构造，避免对两个 O(n²) 四阶原始矩作灾难性消减。",
              "依赖及 longdouble 精度写在 JSON，不假定跨平台扩展精度和压缩字节完全相同。",
              "独立交叉核验用 mpmath 80 位精度 Hurwitz zeta 差（q=−1 用 digamma）给出有限和，",
              "18 个参数各 6 个时点、每点 3 个量；zeta 算法另与 16 项直接高精度求和核验。",
              "有理权重 p=−1,0,1,2 前 64 步实际调用既有 BRC 的 Affine/EffectHistogram/MomentState：",
              "256 次二阶矩核验；独立四阶原始矩递推 256 次；前 8 步显式分布核验 32 次。",
              "这些检查共享参数和时点，不与 2,359,296 个导出记录相加。生产代码没有修改。", "",
              f"高精度核验最大相对误差：`{result['validation']['maximum_high_precision_relative_error']:.6g}`；阈值 `5e-13`。",
              f"18 个完整 gzip CSV 总计 `{sum(x['bytes'] for x in result['trajectory_files'])}` 字节，",
              "每个 CSV 含 p,n,variance,sum_fourth_weights,gamma4,effective_count；kappa4=−2*sum_fourth_weights，",
              "rms_width=sqrt(variance)，无需重复储存。gzip mtime=0；SHA-256 清单在 weighted_results.json。", "",
              "复现（依赖 numpy、mpmath 及仓库 src）：", "",
              "```bash", "python experiments/brc_long_horizon_fit_20261002_9d72ac/weighted_sweep.py", "```", "",
              "`weighted_results.json` 包含抽样轨迹、全部 576 次拟合、80 位参考值、文件哈希、依赖版本和源文件哈希。",
              f"前轮来源固定为 `{PRIOR_COMMIT}` 的 related_branches.py / RELATED_BRANCHES.md。",
              "工具复用结论：EXTEND_EXISTING_TOOL；既有 T0_BRC 的度二仿射传输实际执行，",
              "能力缺口仅为本实验所需四阶量和长时拟合，不创建新生产工具或理论地位。", "",
              "Researcher-ID: EM-BRCWEIGHT-9D72AC / TASK_RESEARCH", ""]
    (out/"WEIGHTED.md").write_text("\n".join(lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=HERE)
    args = parser.parse_args()
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=True)
    validation = exact_checks()
    files, paths, fits, checks = [], [], {}, {}
    for p in PARAMETERS:
        n, s2, s4, gamma = numeric_trajectory(p, HORIZON)
        theory = regime(p, n)
        path_fits = fit_all(n, s2, s4, gamma, theory)
        safe_p = p.replace("-", "m").replace(".", "d")
        files.append(export_trajectory(out/f"weighted_p_{safe_p}.csv.gz", p, n, s2, s4, gamma))
        paths.append(summarize_path(p, n, s2, s4, gamma, theory, path_fits))
        fits[p] = path_fits
        checks[p] = high_precision_checks(p, n, s2, s4, gamma)
        print(f"p={p:>5} PASS rows={HORIZON} bytes={files[-1]['bytes']}", flush=True)
    validation["high_precision_points"] = len(PARAMETERS)*6
    validation["high_precision_scalar_checks"] = len(PARAMETERS)*6*3
    validation["direct_high_precision_finite_sum_checks"] = len(PARAMETERS)*2
    validation["maximum_high_precision_relative_error"] = max(
        v for rows in checks.values() for row in rows for k, v in row.items() if k.endswith("_relative_error"))
    result = {"schema": "brc-weighted-long-horizon/v1", "status": "PASS",
              "researcher_id": "EM-BRCWEIGHT-9D72AC", "activity_id": "RA-BRCWEIGHT-20261002-9D72AC",
              "source_sha256": digest(Path(__file__)), "prior_source_commit": PRIOR_COMMIT,
              "production_brc_source_sha256": digest(ROOT/"src/enterprise_math/brc_transport.py"),
              "dependencies": {"python": platform.python_version(), "numpy": np.__version__,
                               "mpmath": mp.__version__, "platform": platform.platform(),
                               "longdouble_mantissa_bits": int(np.finfo(np.longdouble).nmant)},
              "design": {"parameters": list(PARAMETERS), "horizon": HORIZON,
                         "train_windows": TRAIN_WINDOWS, "fit_count": len(PARAMETERS)*len(TRAIN_WINDOWS)*8,
                         "inverse_width_squared_registration": "added during first trajectory scan, before inspecting any fitting results; directly tests the user's stated width inverse-square hypothesis",
                         "deterministic_paths": len(PARAMETERS), "exported_timepoints": len(PARAMETERS)*HORIZON,
                         "independent_stochastic_replicates": 0,
                         "relative_rmse_definition": "sqrt(sum_test((prediction-observation)^2)/sum_test(observation^2))",
                         "heldout_status": "predeclared temporal extrapolation; known model; overlapping across fits; not blind discovery",
                         "inverse_neff_status": "structural identity check using declared future weights, not independent prediction"},
              "validation": validation, "high_precision_checks": checks,
              "trajectory_files": files, "paths": paths, "fits": fits}
    (out/"weighted_results.json").write_text(json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False)+"\n", encoding="utf-8")
    render_report(out, result)
    print(json.dumps({"status": "PASS", "timepoints": result["design"]["exported_timepoints"],
                      "fit_count": result["design"]["fit_count"], "validation": validation,
                      "gzip_total_bytes": sum(x["bytes"] for x in files)}, indent=2))


if __name__ == "__main__":
    main()
