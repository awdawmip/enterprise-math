"""Compile and run the fixed upstream Basilisk vortex test with two mesh indicators."""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
import os
from pathlib import Path
import random
import subprocess
import tempfile
from time import perf_counter
import platform


FILES = {"test/vortex.c":"24a0a9ff91194dad4247978b09d40a2167075b6d86df769b047a5f690f04a0f5",
         "grid/multigrid-common.h":"d958069efd1c2ea3a9aed2b525c32965f506c801e567a1abdc749a0206817622",
         "grid/tree-common.h":"9eaeae56e07d4e0e8556490ad0501b84ea634a41b803e0f78468632b9c9cfa32",
         "navier-stokes/centered.h":"36f6a142f648565200fbd6513f8ff9ec6c3296c0540e70aac140129a582098af"}
NAMES = ("mode level parameter steps t energy momentum_x momentum_y area face_div_max "
         "face_div_integral normal_wall_max adapt_events final_leaves pre_leaf_sum "
         "post_leaf_sum refinements coarsenings pressure_cycles half_pressure_cycles "
         "indicator_parents cleared_score_leaves final_depth adapt_cpu_s observable_cpu_s").split()
INTS = {"mode","level","steps",*NAMES[12:23]}
OUT = Path(__file__).resolve().parent


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def compile_driver(src,work,env):
    for name,digest in FILES.items():
        assert sha(src/name)==digest, name
    upstream=(src/"test/vortex.c").read_text()
    prefix=upstream[:upstream.index("/**\nWe output some statistics")]
    prefix=prefix.replace("#define MAXLEVEL 8","int mode_id = 1, max_level = 8;\ndouble tau = 5e-5;")
    prefix=prefix.replace("int main()\n{","int main(int argc, char ** argv)\n{\n"
                          "  if (argc != 4) return 2;\n"
                          "  mode_id = atoi(argv[1]); max_level = atoi(argv[2]); tau = atof(argv[3]);")
    assert prefix.count("init_grid (1 << MAXLEVEL)")==1
    prefix=prefix.replace("init_grid (1 << MAXLEVEL)","init_grid (1 << max_level)")
    header=(OUT/"amr_events.h").read_text()
    (work/"run.c").write_text(prefix+"\n"+header)
    command=[str(src/"qcc"),"-O2","-disable-dimensions","-grid=quadtree","run.c","-o","flow","-lm"]
    build=subprocess.run(command,cwd=work,env=env,capture_output=True,text=True)
    if build.returncode:
        raise RuntimeError(build.stderr)
    return sha(work/"run.c")


def execute(exe,mode,level,theta,env):
    start=perf_counter()
    proc=subprocess.run([str(exe),str(mode),str(level),str(theta)],cwd=exe.parent,env=env,
                        check=True,capture_output=True,text=True)
    elapsed=perf_counter()-start
    line=next(x for x in proc.stdout.splitlines() if x.startswith("RESULT "))
    fields=line.split()[1:]
    assert len(fields)==len(NAMES),(fields,NAMES)
    result={k:(int(v) if k in INTS else float(v)) for k,v in zip(NAMES,fields)}
    assert abs(result["t"]-1)<1e-12 and abs(result["area"]-1)<1e-12
    assert result["normal_wall_max"] < 1e-14
    times={k:result.pop(k) for k in ["adapt_cpu_s","observable_cpu_s"]}
    return result, dict(wall_s=elapsed,**times)


def tag(mode,level,theta):
    return f"{['uniform','wave','energy'][mode]}_L{level}_{theta:g}"


def replay(src,work,repeats,cost_path,checkpoint=None):
    env=dict(os.environ,BASILISK=str(src),LC_ALL="C",OMP_NUM_THREADS="1")
    env["PATH"]=str(src)+os.pathsep+env.get("PATH","")
    build_hash=compile_driver(src,work,env)
    jobs=[(0,level,0.) for level in [7,8,9]]
    jobs.extend((1,8,x) for x in (2.5e-5,5e-5,1e-4,2e-4))
    jobs.extend((2,8,x) for x in (1e-10,5e-10,2e-9,1e-8,5e-8))
    stats={}
    costs={}
    order=[]
    rng=random.Random(20260910)
    runlist=[(job,0) for job in jobs]
    # Repeat every adaptive setting for the timing controls.
    for r in range(1,repeats):
        runlist.extend((job,r) for job in jobs if job[0]!=0)
    rng.shuffle(runlist)
    saved = {}
    if checkpoint and checkpoint.exists():
        for ln in checkpoint.read_text().splitlines():
            record=json.loads(ln)
            assert record["driver"]==build_hash
            saved[record["key"],record["rep"]]=(record["result"],record["clock"])
    for job,rep in runlist:
        key=tag(*job)
        if (key,rep) in saved:
            result,clock=saved[key,rep]
        else:
            result,clock=execute(work/"flow",*job,env)
            if checkpoint:
                record={"driver":build_hash,"key":key,"rep":rep,"result":result,"clock":clock}
                with checkpoint.open("a") as handle:
                    print(json.dumps(record,sort_keys=True),file=handle)
        if key in stats:
            assert stats[key]==result,key
        stats[key]=result
        costs.setdefault(key,[]).append(clock)
        order.append([key,rep])
    ref=stats[tag(0,9,0.)]["energy"]
    delta=abs(ref-stats[tag(0,8,0.)]["energy"])/ref
    for s in stats.values():
        s["relative_energy_error_to_uniform_9"]=abs(s["energy"]-ref)/ref
    targets={}
    for eps in (0.01,0.003,0.001):
        by_method={}
        for mode in (1,2):
            admissible=[(k,v) for k,v in stats.items() if v["mode"]==mode and
                        v["relative_energy_error_to_uniform_9"]<=eps]
            by_method[str(mode)]=min(admissible,key=lambda x:x[1]["pre_leaf_sum"])[0] if admissible else None
        targets[str(eps)]=by_method
    if cost_path:
        cost_path.write_text(json.dumps({"repetitions_requested_for_adaptive":repeats,"random_seed":20260910,
                                         "run_order":order,"measurements":costs,
                                         "compiler":subprocess.check_output(["gcc","--version"],text=True).splitlines()[0],
                                         "architecture":platform.machine(),"driver_binary_sha256":sha(work/"flow"),
                                         "cpu_model":next((l.split(":",1)[1].strip() for l in Path("/proc/cpuinfo").read_text().splitlines() if l.startswith("model name")),"unreported") if Path("/proc/cpuinfo").exists() else "unreported"},indent=2,sort_keys=True)+"\n")
    return {"upstream_files":FILES,"generated_driver_sha256":build_hash,"results":stats,
            "uniform_8_to_9_relative_gap":delta,"target_minimum_pre_leaf_sum_cases":targets}


def shear_identity():
    checked=[]
    for h in (Fraction(1,2),Fraction(1,4),Fraction(1,8)):
        y=Fraction(3,5)
        kids=[]
        for sx in (-1,1):
            for sy in (-1,1):
                v=y+sy*h/4
                # Frozen 2D bilinear stencil 9,3,3,1 on u_x=y.
                interpolated=(9*y+3*(y+y+sy*h)+(y+sy*h))/16
                assert interpolated==v
                kids.append(v)
        before=h*h*sum(v*v for v in kids)/8
        after=h*h*(sum(kids)/4)**2/2
        assert before-after==h**4/32
        checked.append([str(h),"0",str(before-after)])
    return checked


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--basilisk",type=Path,default=os.getenv("BASILISK"))
    parser.add_argument("--repeats",type=int,default=1)
    parser.add_argument("--cost",type=Path)
    parser.add_argument("--checkpoint",type=Path,help="optional append-only local recovery file")
    args=parser.parse_args()
    if not args.basilisk or not (args.basilisk/"qcc").is_file():
        parser.error("supply --basilisk /path/to/basilisk/src containing built qcc")
    if args.repeats<1:
        parser.error("repeats must be positive")
    with tempfile.TemporaryDirectory(prefix="basilisk-energy-") as tmp:
        evidence=replay(args.basilisk.resolve(),Path(tmp),args.repeats,args.cost,args.checkpoint)
    evidence["affine_shear_h_wavelet_loss"]=shear_identity()
    print(json.dumps(evidence,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
