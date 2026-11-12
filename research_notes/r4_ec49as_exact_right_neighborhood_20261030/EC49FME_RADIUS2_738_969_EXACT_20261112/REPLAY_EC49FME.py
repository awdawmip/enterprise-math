#!/usr/bin/env python3
"""EC49FME: audit 232 native signed-X6 minima; --run-all recomputes exact C++ DP.
Needs the immutable frozen generator and unmodified EC49FKY C++ solver in sibling
research directories. Pure Python audit needs only the standard library.
"""
import base64,collections,hashlib,itertools,json,subprocess,sys,tempfile,zlib
from pathlib import Path
P=Path(__file__).resolve().parent
ROOT=P.parent
sys.path.insert(0,str(ROOT/"EC49FJD_RELEASE_B11_COMPLETE_20261111"))
from EC49FGW_RADIUS5_SCREEN import PIN,all_words,pref,raw_key
BASE={(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}
E=json.loads((P/"EXACT_VECTOR_EC49FME.json").read_text())
assert E["model_pin"]==PIN=="fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
assert E["global_slice"]==[738,970] and E["count"]==232
raw=zlib.decompress(base64.b64decode(E["rows_zlib_b64"]))
assert hashlib.sha256(raw).hexdigest()==E["raw_rows_sha256"]
lines=raw.decode().splitlines()
assert len(lines)==232
rowints=[tuple(map(int,line.split()[:4])) for line in lines]
assert [r[0] for r in rowints]==list(range(232))
assert collections.Counter(str(r[1]) for r in rowints)==E["histogram"]
assert collections.Counter(str(r[3]) for r in rowints)==E["roots_histogram"]
assert min(r[1] for r in rowints)==98 and max(r[1] for r in rowints)==112
assert [738+r[0] for r in rowints if r[1]==98]==[757,840,922]
cat=list(all_words());labels=sorted(set(label for label,_ in cat))
assert len(cat)==178850 and len(labels)==24
labid={label:i for i,label in enumerate(labels)}
bykey=collections.defaultdict(list);support=collections.defaultdict(int)
for label,word in cat:
    k=raw_key(word);i=labid[label]
    support[k]|=1<<i
    if "--run-all" in sys.argv:
        bykey[k].append((i,pref(word)[-1].hex()))
assert len(support)==94 and BASE.issubset(support)
outside=sorted(set(support)-BASE);old=sorted(BASE);full=(1<<24)-1
allsets=[];drops=[]
for dropped in itertools.combinations(old,2):
    for added in itertools.combinations(outside,2):
        K=sorted(BASE-set(dropped)|set(added))
        covered=0
        for k in K:covered|=support[k]
        if covered==full:
            allsets.append(K);drops.append(dropped)
assert len(allsets)==6315
assert all(drops[i]==((5,3,1),(5,4,1)) for i in range(738,970))
print("EC49FME_VECTOR_AND_CATALOG_PASS",len(lines),len(cat),len(support),len(allsets),flush=True)
if "--run-all" in sys.argv:
    with tempfile.TemporaryDirectory() as td:
        td=Path(td)
        with (td/"input.txt").open("w") as f:
            f.write("232\n")
            for K in allsets[738:970]:
                paths=[r for k in K for r in bykey[k]]
                f.write(str(len(paths))+"\n")
                for i,path in paths:f.write(str(i)+" "+path+"\n")
        cpp=ROOT/"EC49FKY_ONE_KEY_SWAP_84_LOCAL_OPTIMUM_20261112"/"SCAN_7KEY_GENERAL.cpp"
        subprocess.run(["g++","-std=c++17","-O3",str(cpp),"-o",str(td/"scan")],check=True)
        with (td/"input.txt").open("rb") as inp,(td/"output.txt").open("wb") as out:
            subprocess.run([str(td/"scan")],stdin=inp,stdout=out,check=True)
        got=(td/"output.txt").read_bytes()
        assert got==raw,(len(got),len(raw))
        print("EC49FME_ALL_232_EXACT_REPLAY_PASS")
