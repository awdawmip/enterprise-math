"""Compile against the original fourth-phase reproduction bundle, without editing its files."""
import argparse
import hashlib
from pathlib import Path
import subprocess
import sys

here = Path(__file__).resolve().parent
p = argparse.ArgumentParser(description=__doc__)
p.add_argument("source_root", type=Path, help="extracted phase-four bundle (directory with BUNDLE_MANIFEST.json)")
p.add_argument("--sanitize", action="store_true")
p.add_argument("--unit", type=Path, help="alternative translation unit with its own main")
p.add_argument("--output", type=Path)
args = p.parse_args()
base = args.source_root.resolve()
build = here / "build"
build.mkdir(exist_ok=True)
parts = ("expanded", "local", "sampled", "robust", "adaptive", "selection", "certified")
dirs = {}
for name in parts:
    matches = list(base.glob("brc_residual_sort_" + name + "_*"))
    if len(matches) != 1:
        raise ValueError(f"Expected one {name} source directory in {base}")
    dirs[name] = matches[0]
prior = dirs["certified"]
prep = [sys.executable, str(prior / "prepare_frozen_include.py"), "--output-dir", str(build)]
for name in ("selection", "adaptive", "robust", "sampled"):
    prep += ["--" + name + "-source", str(dirs[name] / f"{name}_bench.cpp")]
subprocess.run(prep, check=True, stdout=subprocess.DEVNULL)
source = (prior / "certified_bench.cpp").read_bytes()
assert hashlib.sha256(source).hexdigest() == "d5466c4d5c418d23323d3b2f6c92b210a9221ca9f4c9297e71adbb2e08218303"
signature = b"int main(int argc,char** argv)"
assert source.count(signature) == 1
(build / "certified_frozen_include.hpp").write_bytes(source.replace(signature,b"int certified_frozen_entry(int argc,char** argv)"))
defs = {"BASE_SOURCE": dirs["expanded"] / "pure_bench.cpp", "LOCAL_KERNELS": dirs["local"] / "local_kernels.hpp"}
for name in ("sampled", "robust", "adaptive", "selection"):
    defs[name.upper()+"_SOURCE"] = build / (name + "_frozen_include.hpp")
flags = ["-std=c++20", "-Wall", "-Wextra", "-march=native"]
flags += (["-O1", "-g0", "-fsanitize=address,undefined", "-fno-omit-frame-pointer"] if args.sanitize else ["-O3", "-DNDEBUG"])
flags += [f'-DBRC_{name}="{path}"' for name, path in defs.items()]
for folder in (build, here, *dirs.values()):
    flags += ["-I", str(folder)]
binary = args.output or build / ("bench_sanitized" if args.sanitize else "bench")
subprocess.run(["g++", *flags, str(args.unit or here / "bench.cpp"), "-o", str(binary)], check=True)
