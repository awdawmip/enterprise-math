#!/usr/bin/env python3
from __future__ import annotations
import ctypes.util
import glob
import importlib.util
import json
import shutil
import sys
from fractions import Fraction

REQUIRED_MODULES = ["spectralDNS", "shenfun", "mpi4py", "mpi4py_fft", "pyfftw"]
REQUIRED_COMPILERS = ["mpicc", "mpicxx"]
R10_CASES = [
    {"seed": 91001, "calls": 20, "sparse_calls": 2, "fallback_calls": 18},
    {"seed": 91003, "calls": 20, "sparse_calls": 2, "fallback_calls": 18},
    {"seed": 91007, "calls": 20, "sparse_calls": 1, "fallback_calls": 19},
]


def present_module(name: str) -> bool:
    return importlib.util.find_spec(name) is not None


def route_ceiling(case: dict) -> dict:
    n = int(case["calls"])
    m = int(case["sparse_calls"])
    f = int(case["fallback_calls"])
    assert n == m + f and 0 <= m < n
    # Idealized equal-dense-call-cost ceiling: guards and sparse compute are set to zero;
    # fallback compute is assumed identical to the corresponding dense reference call.
    kernel_speedup = Fraction(n, f)
    alpha_grid = [Fraction(1, 2), Fraction(7, 10), Fraction(9, 10), Fraction(1, 1)]
    total = {}
    sparse_fraction = Fraction(m, n)
    for a in alpha_grid:
        total[str(float(a))] = float(Fraction(1, 1) / (Fraction(1, 1) - a * sparse_fraction))
    return {
        **case,
        "sparse_fraction": float(sparse_fraction),
        "ideal_equal_cost_kernel_speedup_ceiling": float(kernel_speedup),
        "ideal_equal_cost_kernel_speedup_ceiling_exact": f"{kernel_speedup.numerator}/{kernel_speedup.denominator}",
        "total_trajectory_speedup_ceiling_by_dense_nonlinear_fraction_alpha": total,
    }


def main() -> int:
    modules = {name: present_module(name) for name in REQUIRED_MODULES}
    compilers = {name: shutil.which(name) for name in REQUIRED_COMPILERS}
    mpi_headers = glob.glob("/usr/include/**/mpi.h", recursive=True)
    fftw_headers = glob.glob("/usr/include/**/fftw3.h", recursive=True)
    libs = {
        "mpi": ctypes.util.find_library("mpi"),
        "fftw3": ctypes.util.find_library("fftw3"),
    }
    native_ready = (
        all(modules.values())
        and all(compilers.values())
        and bool(mpi_headers)
        and bool(fftw_headers)
        and bool(libs["mpi"])
        and bool(libs["fftw3"])
    )
    ceilings = [route_ceiling(case) for case in R10_CASES]
    out = {
        "schema": "ENTERPRISE_MATH_CFD_NATIVE_HOST_AND_ROUTE_CEILING_R16_V1",
        "python": sys.version.split()[0],
        "native_host_readiness": {
            "required_modules": modules,
            "required_compilers": compilers,
            "mpi_headers": mpi_headers,
            "fftw3_headers": fftw_headers,
            "libraries": libs,
            "native_ready": native_ready,
        },
        "frozen_input_provenance": {
            "source_return": "research_returns/RS-CFD-SPECTRAL-HYBRID-20260910_A11R10_20260921_R10.md@aa054a7ac72a3f78ab7f590291017cbd453ed29f",
            "route_counts_only": True,
        },
        "route_ceiling_analysis": {
            "conditions": [
                "equal dense-reference cost per nonlinear call within each case",
                "fallback compute equals the corresponding dense-reference compute",
                "guard and sparse compute are hypothetically zero for the ceiling",
                "only the nonlinear evaluator is accelerated; all other trajectory work is unchanged",
            ],
            "general_weighted_identity": "S_kernel_ideal <= D_total / D_fallback = 1/(1-w_sparse), where w_sparse is the dense-reference cost share of sparse-eligible calls",
            "general_total_identity": "S_total_ideal <= 1/(1-alpha*w_sparse), where alpha is the dense trajectory fraction spent in the nonlinear evaluator",
            "equal_cost_specialization": "w_sparse=m/N, so S_kernel_ideal<=N/(N-m) and S_total_ideal<=1/(1-alpha*m/N)",
            "cases": ceilings,
        },
        "interpretation": {
            "native_speedup_claim": False,
            "native_host_executed": False,
            "new_bounded_result": "R10 route saturation implies a small idealized speedup envelope even before guard overhead; native A/B/C runs should record paired dense per-call costs to replace the equal-cost specialization with the exact weighted ceiling.",
        },
    }
    print(json.dumps(out, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if all(c["calls"] == c["sparse_calls"] + c["fallback_calls"] for c in R10_CASES) else 1

if __name__ == "__main__":
    raise SystemExit(main())
