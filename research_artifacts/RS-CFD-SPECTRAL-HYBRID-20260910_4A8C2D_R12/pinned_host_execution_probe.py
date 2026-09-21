#!/usr/bin/env python3
"""Fail-closed capability probe for the pinned spectralDNS serial-host checkpoint.

This probe performs no network access and makes no speedup claim.  It records
whether the Python/runtime/build prerequisites needed to instantiate the pinned
spectralDNS host are already present in the execution environment.
"""
from __future__ import annotations
import ctypes.util
import importlib.util
import json
import os
import platform
import shutil
import sys
from pathlib import Path

MODULES = ("spectralDNS", "shenfun", "mpi4py", "mpi4py_fft", "pyfftw")
HEADER_CANDIDATES = {
    "mpi.h": ["/usr/include/mpi.h", "/usr/local/include/mpi.h"],
    "fftw3.h": ["/usr/include/fftw3.h", "/usr/local/include/fftw3.h"],
}
EXECUTABLES = ("mpicc", "mpicxx", "gcc", "g++")
LIBRARIES = ("fftw3", "fftw3_threads", "mpi")


def first_existing(paths):
    for p in paths:
        if Path(p).exists():
            return p
    return None


def main():
    modules = {name: (importlib.util.find_spec(name) is not None) for name in MODULES}
    executables = {name: shutil.which(name) for name in EXECUTABLES}
    headers = {name: first_existing(paths) for name, paths in HEADER_CANDIDATES.items()}
    libraries = {name: ctypes.util.find_library(name) for name in LIBRARIES}
    runtime_ready = all(modules[name] for name in ("spectralDNS", "shenfun", "mpi4py", "mpi4py_fft"))
    offline_source_build_prereqs = bool(
        executables["gcc"] and executables["g++"] and executables["mpicc"]
        and headers["mpi.h"] and headers["fftw3.h"]
    )
    payload = {
        "schema": "EM_CFD_PINNED_HOST_CAPABILITY_PROBE_V1",
        "python": sys.version,
        "platform": platform.platform(),
        "modules": modules,
        "executables": executables,
        "headers": headers,
        "libraries": libraries,
        "runtime_ready": runtime_ready,
        "offline_source_build_prereqs": offline_source_build_prereqs,
        "native_host_ready": runtime_ready,
        "network_used": False,
        "interpretation": (
            "READY_TO_RUN_PINNED_HOST" if runtime_ready else
            "PINNED_HOST_NOT_INSTANTIABLE_FROM_PRESENT_RUNTIME"
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if runtime_ready else 3


if __name__ == "__main__":
    raise SystemExit(main())
