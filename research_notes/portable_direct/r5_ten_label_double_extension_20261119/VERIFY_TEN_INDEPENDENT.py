#!/usr/bin/env python3
"""Independent doubled-endpoint oracle for ten-label R5 pair augmentation.

Executed on the frozen input and local full census:
PASS_TEN_INDEPENDENT pairs 244 checks 492 rare 4
The input and full census files are present in the complete reproduction ZIP.
"""
from pathlib import Path
import csv, functools, hashlib, json, random

root = Path(__file__).parent
raw = (root / "EXACT_R5_ALL_101_BUDGETS.json").read_bytes()
assert hashlib.sha256(raw).hexdigest() == "50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
data = json.loads(raw)
tau = int(json.loads((root / "stages_18.json").read_text())["U"]) - 1
centers = {k: tuple(map(int, data["counts_and_cohorts"][str(k)]["counts"])) for k in range(214,315)}
seed = (0,16,32,48,1,64,17,80)
with (root / "R5_TWO_MORE_F04_RESULTS.csv").open() as f:
    rows = list(csv.reader(f))
assert rows[0] == ["#t","u","class_id","f0","f1","f2","f3","f4"]
records = {(int(r[0]), int(r[1])): tuple(map(int,r[3:])) for r in rows[1:]}
assert len(records) == 30628
rare = {(18,24),(19,25),(22,28),(23,29)}
assert {pair for pair,v in records.items() if v[1]>1680} == rare
rng = random.Random(2026111920)
ordinary = [p for p in records if p not in rare]
choices = sorted(set(rng.sample(ordinary,240)) | rare)

def joint_families(t,u):
    labels = seed+(t,u)
    classes = {}
    for k in centers:
        vals = [centers[k][i] for i in labels]
        endpoints = [2*ni-tau for ni in vals]
        masks = set(sum(1<<j for j,nj in enumerate(vals) if abs(2*nj-y)<=tau) for y in endpoints)
        maximal = tuple(sorted(s for s in masks if not any(s!=z and (s&z)==s for z in masks)))
        if maximal != (1023,):
            if maximal not in classes or k<classes[maximal]: classes[maximal]=k
    return tuple(sorted((price,family) for family,price in classes.items()))

def value(actions, errors):
    f = errors
    @functools.lru_cache(maxsize=None)
    def rec(counter):
        live = sum(1<<j for j,x in enumerate(counter) if x<=f)
        if live.bit_count()<=1: return 0
        options=[]
        for k,family in actions:
            if any((mask&live)==live for mask in family): continue
            worst=0
            for mask in family:
                nxt=tuple(min(f+1,x+(1 if not(mask>>j&1) else 0)) for j,x in enumerate(counter))
                worst=max(worst,rec(nxt))
            options.append(k+worst)
        assert options,(counter,errors)
        return min(options)
    return rec((0,)*10),rec.cache_info().currsize

runs=0
for pair in choices:
    acts=joint_families(*pair)
    limits=(0,1,2) if pair in rare else (0,1)
    for f in limits:
        got,states=value(acts,f)
        want=records[pair][f]
        assert got==want,(pair,f,got,want)
        runs+=1
print("PASS_TEN_INDEPENDENT","pairs",len(choices),"checks",runs,"rare",len(rare),
      "input_sha256",hashlib.sha256(raw).hexdigest())
