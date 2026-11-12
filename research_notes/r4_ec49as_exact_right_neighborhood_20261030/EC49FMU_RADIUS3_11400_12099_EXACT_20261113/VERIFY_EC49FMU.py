#!/usr/bin/env python3
"""Verify EC49FMU exact-vector bytes, 24 native-prefix witness and optional frozen replay."""
from pathlib import Path
from collections import Counter,defaultdict
import json,base64,zlib,hashlib,subprocess,sys,importlib.util

D=Path(__file__).resolve().parent
d=json.loads((D/"EXACT_DATA_EC49FMU.json").read_text())
assert d["frozen_scientific_pin"]=="fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
c=zlib.decompress(base64.b64decode(d["cost_uint8_zlib_base64"]))
assert len(c)==d["count"]==700 and d["source_window"]==[11400,12099]
assert hashlib.sha256(c).hexdigest()==d["cost_uint8_sha256"]
assert min(c)==d["exact_minimum"]==118 and max(c)==d["exact_maximum"]==196
assert [11400+i for i,v in enumerate(c) if v==118]==d["argmin"]==[11511]
assert sum(v==196 for v in c)==d["maximum_occurrences"]==21
W=d["constructive_11511"]; words=W["operation_words"]
assert len(words)==W["label_count"]==24 and W["cost"]==118
STEPS={"a":(-1,-1),"c":(1,2,-1,-2),"d":(2,1,-2,-1),"e":(3,1,1,-3),"f":(1,-1),"g":(2,-2)}
labels=set(); roots=defaultdict(set); union=set()
for h,s,word in words:
    assert len(word)==h and all(z in STEPS for z in word)
    labels.add((h,s));p=b""
    for op in word:
        for signed_step in STEPS[op]:
            p+=bytes((signed_step+4,))
            roots[p[0].hex()].add(p);union.add(p)
assert len(labels)==24 and len(union)==118
assert {k:len(v) for k,v in roots.items()}==W["root_costs"]=={"05":42,"06":52,"07":24}
raw=D/"EXACT_NATIVE_OUTPUT_11400_12099.txt"
if raw.exists():
    assert hashlib.sha256(raw.read_bytes()).hexdigest()==d["raw_700_line_sha256"]
    rows=[line.split() for line in raw.read_text().splitlines()]
    assert len(rows)==700 and [int(row[0]) for row in rows]==list(range(11400,12100))
    assert bytes(int(row[1]) for row in rows)==c
    assert {str(k):v for k,v in Counter(int(row[3]) for row in rows).items()}==d["root_count_histogram"]
else:
    print("RAW_ROWS_NOT_LOCAL: compact cost vector and constructive prefix witness verified")
for filename,sha_field in (("master_and_radius3_cases.txt","frozen_master_sha256"),("cases.json","frozen_cases_sha256"),("scan_cached_radius3.cpp","solver_cpp_sha256"),("EC49FGW_RADIUS5_SCREEN.py","generator_py_sha256"),("EC49FGJ_SEVEN_KEY_94_WITNESSES.json","catalog_original_witness_sha256")):
    p=D/filename
    if p.exists(): assert hashlib.sha256(p.read_bytes()).hexdigest()==d[sha_field],filename
generator=D/"EC49FGW_RADIUS5_SCREEN.py"
cases=D/"cases.json"
if generator.exists() and cases.exists():
    sys.path.insert(0,str(D))
    from EC49FGW_RADIUS5_SCREEN import all_words,raw_key,PIN
    assert PIN==d["frozen_scientific_pin"]
    catalogue=set(all_words())
    assert len(catalogue)==178850
    allkeys=sorted({raw_key(word) for _,word in catalogue})
    assert len(allkeys)==94
    case_data=json.loads(cases.read_text())
    assert len(case_data["cases"])==38169 and case_data["cases"][11511]==W["seven_key_indices"]
    allowed={allkeys[i] for i in W["seven_key_indices"]}
    for h,s,word in words:assert ((h,s),word) in catalogue and raw_key(word) in allowed
    print("FROZEN_CATALOGUE_AND_SEVEN_KEYS_WITNESS_PASS")
else:
    print("FROZEN_CATALOGUE_NOT_LOCAL: legal-word generator replay available with companion archive")
if "--recompute" in sys.argv:
    cpp=D/"scan_cached_radius3.cpp"
    master=D/"master_and_radius3_cases.txt"
    assert cpp.exists() and master.exists(),"Original pinned C++ and master input required for independent full recomputation"
    exe=D/"scan_recompute"
    subprocess.run(["g++","-O3","-std=c++17",str(cpp),"-o",str(exe)],check=True)
    with master.open("rb") as f:
        p=subprocess.run([str(exe),"11400","12100"],stdin=f,stdout=subprocess.PIPE,check=True)
    rows=[line.split() for line in p.stdout.decode().splitlines()]
    assert len(rows)==700 and bytes(int(row[1]) for row in rows)==c
    assert hashlib.sha256(p.stdout).hexdigest()==d["raw_700_line_sha256"]
    print("COMPLETE_ORIGINAL_CPP_EXACT_RECOMPUTATION_PASS")
print("EC49FMU_VERIFY_PASS",len(c),min(c),[11400+i for i,v in enumerate(c) if v==118],len(labels),len(union))
