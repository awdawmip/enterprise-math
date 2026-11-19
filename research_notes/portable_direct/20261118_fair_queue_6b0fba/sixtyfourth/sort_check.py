#!/usr/bin/env python3
"""Integer laws for the minimum three-interval cover and the frozen C++ route."""
import argparse
from collections import Counter
import csv
import hashlib
from itertools import combinations
import json
from math import comb
from pathlib import Path
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory

DRIVER = r'''
#include "holdout.cpp"
#include <set>

using V = balance_sort::Values;
using U = std::uint64_t;
constexpr U BANK = 0x243f6a8885a308d3ULL, COIN = 0x13198a2e03707344ULL;
constexpr U STEP = 0x9e3779b97f4a7c15ULL;

U cover(const V& sorted) {
    U gap1=0, gap2=0;
    for (std::size_t j=1;j<sorted.size();++j) if (sorted[j]>sorted[j-1]) {
        U g=sorted[j]-sorted[j-1]-1;
        if (g>=gap1) { gap2=gap1; gap1=g; }
        else if (g>gap2) gap2=g;
    }
    return U(u128(sorted.back())-sorted.front()+1-gap1-gap2);
}

void run_new(std::size_t n, unsigned banks) {
    unsigned early=0, accepted=0, full=0, over=0, switched=0;
    U budget=brc_sampled_detail::cell_budget(n);
    for (unsigned b=0;b<banks;++b) {
        U seed=BANK ^ (U(n)*STEP) ^ U(b);
        U probe_seed=COIN ^ (U(n)<<32) ^ (U(b)*STEP);
        const V a=balance_sort::make_input(2,n,seed);
        std::array<U,64> sample{};
        std::set<std::size_t> positions;
        brc_probe::Engine draws{probe_seed};
        for(unsigned i=0;i<32;++i) {
            auto lo=i*n/32, hi=(i+1)*n/32;
            auto p=lo+std::size_t(u128(draws())*(hi-lo)>>64);
            while(p==lo || brc_probe::training_position(p,n)) {
                if(++p==hi) p=lo;
            }
            sample[i]=a[lo];sample[32+i]=a[p];
            positions.insert(lo);positions.insert(p);
        }
        if (positions.size()!=64) throw std::runtime_error("sample overlap");
        const bool p32=holdout::fits(sample,32,budget), p64=holdout::fits(sample,64,budget);
        const bool route=holdout::three(a,probe_seed);
        V oracle=a;
        std::sort(oracle.begin(),oracle.end());
        bool truefit=cover(oracle)<=budget;
        if (p64!=route || (p64&&!p32) || (truefit&&!route)) throw std::runtime_error("route mismatch");
        V candidate=a;
        if(route) child_sort<ChildMode::radix>(candidate,probe_seed);
        else offset_radix(candidate,nullptr);
        if(candidate!=oracle) throw std::runtime_error("incorrect sorted result");
        early+=p32; accepted+=p64;full+=truefit;over+=!truefit&&route;switched+=p32&&!p64;
    }
    std::cout<<"new "<<n<<' '<<banks<<' '<<early<<' '<<accepted<<' '<<full<<' '<<over<<' '<<switched<<'\n';
}

void timing(const char* path) {
    std::ofstream out(path);
    out<<"n,bank,round,order,method,ns,input_seed,probe_seed,route\n";
    std::mt19937_64 order(0x24ab10ced71a09f3ULL);
    for (std::size_t n : {20272U,21414U,22416U}) {
        for (unsigned bank=0;bank<9;++bank) {
            U seed=0xa4093822299f31d0ULL^(U(n)*STEP)^bank;
            U probe_seed=0x082efa98ec4e6c89ULL^(U(n)<<32)^(U(bank)*STEP);
            V a=balance_sort::make_input(2,n,seed);
            V oracle=a;std::sort(oracle.begin(),oracle.end());
            bool route=holdout::three(a,probe_seed);
            for(unsigned rep=0;rep<3;++rep) {
                std::array<unsigned,10> methods{0,1,2,3,4,5,6,7,8,9};
                std::shuffle(methods.begin(),methods.end(),order);
                for(unsigned idx=0;idx<methods.size();++idx) {
                    auto method=methods[idx];
                    balance_sort::Clock::time_point sorted,checked;
                    const auto start=balance_sort::Clock::now();
                    {
                        V values=a;
                        if(method<9) balance_sort::run(method,values,probe_seed);
                        else if(holdout::three(values,probe_seed)) child_sort<ChildMode::radix>(values,probe_seed);
                        else offset_radix(values,nullptr);
                        sorted=balance_sort::Clock::now();
                        if(values!=oracle) throw std::runtime_error("timed mismatch");
                        checked=balance_sort::Clock::now();
                    }
                    auto end=balance_sort::Clock::now();
                    out<<n<<','<<bank<<','<<rep<<','<<idx<<','<<method<<','<<balance_sort::ns((sorted-start)+(end-checked))<<','<<seed<<','<<probe_seed<<','<<route<<'\n';
                }
            }
        }
    }
}

int main(int argc,char** argv) {
    for(unsigned f=0;f<5;++f) for(std::size_t n : {16384U,65536U,262144U,1048576U}) {
        for(unsigned b=0;b<3;++b) {
            U input=0x3aa2c625a1c88249ULL ^ n ^ (U(f)<<48) ^ ((b+1)*0xd1b54a32d192ed03ULL);
            U probe=0x964b13fdaa61f8cfULL ^ n ^ (U(b)<<8) ^ (U(f)<<32);
            auto a=balance_sort::make_input(f,n,input);
            std::cout<<"old "<<balance_sort::families[f]<<' '<<n<<' '<<b<<' '
                     <<balance_sort::pilot(a,probe,true)<<' '<<holdout::three(a,probe)<<'\n';
        }
    }
    for(std::size_t n : {16386U,18432U,20272U,20800U,21414U,22000U,22416U,23200U,24000U,24574U,24576U}) run_new(n,192);
    if(argc==2) timing(argv[1]);
}
'''

PINS = {
    "phase5/build.py": "8a282114f9ddc5ed52cb33e1fb19c533778e7287ec2bfe62d8044fbac4ecdad3",
    "phase5/probe.hpp": "f2e9186856ccc583890c13f140cea1aa61e142805de245133f95902faaa2843c",
    "phase6/child.hpp": "33081d93895a7c774889208ee0aaeea56e657cf7dcfee76bfa3cdbd0dffe562b",
    "bench.cpp": "9e2e98e3460b5fc1b4317a5b29bbad0de9c18b39f6dfcb67bf21a518965f7471",
    "holdout.cpp": "13b797dcc29e85af16973bb3566d657c5e9b885c50ce72d19ccaf8d4933a2597",
    "holdout_diag.csv": "9d59e043ac0d5202c2daf802f0e8b6f6a7c866b11d1e1b15913e7000baec424a",
}
N_GRID = [16386, 18432, 20272, 20800, 21414, 22000, 22416, 23200, 24000, 24574, 24576]


def mandatory(available, specified, draws):
    if available < specified:
        return 0
    return sum((-1)**i * comb(specified, i) * (available - i)**draws
               for i in range(specified + 1))


def accept(draws, w, b):
    R = 3 * w
    if b >= R:
        return R**draws
    if b < 2 * w:
        raise ValueError("local critical-window law requires budget >= 2W")
    if b == 2 * w:
        if w < 2:
            raise ValueError("boundary correction assumes W >= 2")
        last = R - w + 1
        regular = comb(w + 4, 5) - 3 * w
        extra = regular * mandatory(last, 6, draws) + 3 * w * mandatory(last, 5, draws)
        return accept(draws, w, b + 1) - extra
    # <=5 distinct target symbols in R-B+5 named symbols.
    targets = R - b + 5
    return sum(comb(targets, i) * mandatory(R - targets + i, i, draws) for i in range(6))


def dp_occupied(draws, R, targets):
    states = [1, 0, 0, 0, 0, 0, 0]
    for _ in range(draws):
        nxt = [0] * 6 + [R * states[-1]]
        for j in range(6):
            nxt[j] += states[j] * (R - targets + j)
            nxt[j + 1] += states[j] * (targets - j)
        states = nxt
    return sum(states[:6])


def small_audit():
    cases = 0
    for w in range(2, 6):
        R = 3 * w
        points = [g * (4*w) + u for g in range(3) for u in range(w)]
        table = Counter()
        for q in range(1, R + 1):
            for support in combinations(points, q):
                # Independent search over 0, 1 or 2 cuts of the sorted support.
                width = support[-1] - support[0] + 1
                usable = range(1, len(support))
                best = width
                for splits in combinations(usable, min(len(usable), 2)):
                    cuts = (0,) + splits + (q,)
                    best = min(best, sum(support[j-1]-support[i]+1 for i, j in zip(cuts, cuts[1:])))
                table[q, best] += 1
        for s in (3, 5, 6, 7, 9, 16, 32, 64):
            for b in range(2 * w, R + 1):
                observed = sum(n * mandatory(q, q, s) for (q, span), n in table.items() if span <= b)
                assert observed == accept(s, w, b)
                if 2 * w < b < R:
                    assert observed == dp_occupied(s, R, R-b+5)
                cases += 1
    return cases


def prefix_number(a, b, places=12):
    "Floor of the exact probability times 10**places."
    return (a * 10**places) // b


def critical():
    w = 4096
    R = 3*w
    qs = {}
    numer32 = []
    numer64 = []
    for s, arr in ((32, numer32), (64, numer64)):
        arr.extend(accept(s, w, b) for b in range(2*w, R+1))
        assert arr == sorted(arr)
        den = R**s
        qs[s] = {q: next(2*w + i for i, a in enumerate(arr) if 100*a >= q*den)
                 for q in (5, 25, 50, 75, 95)}
    diffs = [a32*R**32 - a64 for a32, a64 in zip(numer32, numer64)]
    maximum = max(diffs)
    maximizers = [2*w + i for i, x in enumerate(diffs) if x == maximum]
    assert numer32[0]*R**32 < maximum and maximum > 0
    rows = []
    for n in N_GRID:
        budget = n//2
        A32, A64 = numer32[budget-2*w], numer64[budget-2*w]
        full = accept(n, w, budget)
        denom = R**n
        rows.append({"n": n, "budget": budget,
                     "stage32_pass": prefix_number(A32, R**32),
                     "stage64_pass": prefix_number(A64, R**64),
                     "full_cover_pass": prefix_number(full, denom),
                     "sample_pass_full_cover_fails": prefix_number(A64*R**(n-64) - full, denom),
                     "extra_probes_switch": prefix_number(A32*R**32 - A64, R**64)})
    return {"probability_encoding": "floor(10^12 times exact probability)",
            "models": rows, "pass_percentile_first_budget": qs,
            "checked_budgets_inclusive": [2*w, R],
            "maximum_switch_budgets": maximizers, "maximum_switch": prefix_number(maximum, R**64)}


def read_native(output, evidence):
    old = {}
    new = []
    for line in output.splitlines():
        fields = line.split()
        if fields[0] == "old":
            _, family, n, bank, p1, p3 = fields
            old[family, int(n), int(bank)] = (int(p1), int(p3))
        elif fields[0] == "new":
            n, count, p32, p64, full, false_fit, switched = map(int, fields[1:])
            assert full <= p64 <= p32 <= count and (false_fit, switched) == (p64-full, p32-p64)
            new.append({"n": n, "banks_and_sorted_outputs": count, "first_pass": p32,
                        "both_pass": p64, "all_keys_fit": full, "accepted_full_cover_too_wide": false_fit,
                        "switched_after_extra_probes": switched})
        else:
            raise ValueError(line)
    with (evidence / "holdout_diag.csv").open() as handle:
        expected = {(r["family"], int(r["n"]), int(r["bank"])): (int(r["one_segment"]), int(r["three_segments"]))
                    for r in csv.DictReader(handle)}
    assert old == expected and len(old) == 60
    assert [r["n"] for r in new] == N_GRID and all(r["banks_and_sorted_outputs"] == 192 for r in new)
    return {"original_decisions_replayed": len(old), "new_fixed_4096_width": new,
            "extra_probes_disjoint_and_full_output_checked_each": True}


def original(experiments, evidence, timing_csv):
    phase = experiments / "brc_residual_sort_preflight_20261111_b118ef26c242"
    for name, digest in PINS.items():
        p = (phase if "/" in name else evidence) / name
        assert hashlib.sha256(p.read_bytes()).hexdigest() == digest
    with TemporaryDirectory() as tmp:
        base = Path(tmp)
        for folder in ("phase5", "phase6", "unit"):
            (base / folder).mkdir()
        for name in ("phase5/build.py", "phase5/probe.hpp", "phase6/child.hpp"):
            shutil.copyfile(phase / name, base / name)
        shutil.copyfile(evidence / "bench.cpp", base / "unit/bench.cpp")
        src = (evidence / "holdout.cpp").read_text()
        assert src.count("int main(int argc,char** argv)") == 1
        (base / "unit/holdout.cpp").write_text(src.replace("int main(int argc,char** argv)",
                                                          "int frozen_holdout_entry(int argc,char** argv)"))
        (base / "unit/driver.cpp").write_text(DRIVER)
        binary = base / "run"
        command = [sys.executable, str(base/"phase5/build.py"), str(experiments), "--unit",
                   str(base/"unit/driver.cpp"), "--output", str(binary)]
        compiled = subprocess.run(command, capture_output=True, text=True)
        if compiled.returncode:
            raise RuntimeError(compiled.stderr)
        args = [str(binary)] + ([str(timing_csv)] if timing_csv else [])
        return read_native(subprocess.check_output(args, text=True), evidence)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--experiments", required=True, type=Path, help="unpacked frozen phase 4–7 experiments")
    p.add_argument("--evidence", type=Path, default=Path(__file__).resolve().parents[1] / "sort_evidence")
    p.add_argument("--timing-csv", type=Path, help="optional separate timing output in nanoseconds")
    args = p.parse_args()
    output = {"frozen_sha256": PINS, "exact_small_cases": small_audit(), "critical": critical(),
              "actual_code": original(args.experiments.resolve(), args.evidence.resolve(), args.timing_csv)}
    print(json.dumps(output, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
