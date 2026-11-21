#!/usr/bin/env python3
"""R284DM: exact r/w four-orbit code for the frozen Port observer (stdlib only)."""
from itertools import product
from collections import Counter
import hashlib
import json

P = 17179869143
D = (1120832, 6, 13, 1651128)
Z = (0, 390139, 394465, 1497639)
SELECT = (0, 1, 2, 4, 5, 6)
FROZEN_SHA256 = "b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4"
G = (0, 1, 64, 65)

def det(L, top):
    u1, a, x, y, u2, w, b, z, u3, g, h, r = L
    t, s = 6-a, 13-b
    u = t*s-x*w
    v = -r*u-z*(t*h+x*g)-y*(w*h+s*g)
    p1, p2 = s*u1+x*u2, t*u2+w*u1
    q1 = -r*p1-u1*z*h+x*z*u3+y*(u2*h+s*u3)
    q2 = -r*p2+t*z*u3+u1*z*g+y*(w*u3-u2*g)
    q3 = u*u3+p1*g+p2*h
    k = (u*D[3]+v,p1*D[3]+q1,p2*D[3]+q2,q3)
    base = D[0]*k[0]-Z[1]*k[1]-Z[2]*k[2]-Z[3]*k[3]-sum(k)
    return base-sum(k[j] for j in range(4) if top & (1<<j))

def frozen_arcs():
    result = []
    for key in range(64):
        lo, hi = [1]*12, [2]*12
        for j, pos in enumerate(SELECT):
            lo[pos] = hi[pos] = 1+((key>>(5-j))&1)
        h = det(hi, 15)
        result.append((h%P, det(lo,0)-h))
    return result

def frozen_words():
    sha = hashlib.sha256()
    out = []
    for upper in product((1,2),repeat=4):
        top=sum((v-1)<<j for j,v in enumerate(upper))
        for lower in product((1,2),repeat=12):
            x=det(lower,top)%P
            out.append(x)
            sha.update(x.to_bytes(8,"big"))
    assert sha.hexdigest()==FROZEN_SHA256
    assert len(out)==len(set(out))==65536
    return out

def arc_dist(x, arc):
    a,w=arc
    d=(x-a)%P
    return 0 if d<=w else min(d-w,P-d)

def verify():
    arcs,words=frozen_arcs(),frozen_words()
    assert len(arcs)==64 and all(0<w<P//2 for _,w in arcs)
    f=[max(arc_dist(x,a) for a in arcs) for x in words]
    assert len(set((f[i],f[i^64]) for i in range(65536)))==65536
    assert len(set((f[i],f[i^1]) for i in range(65536)))==65536
    seen=set()
    distinct_hist=Counter()
    min_offset_hist=Counter()
    twists=Counter()
    key_digest=hashlib.sha256()
    state_encodings=set()
    for base in range(65536):
        if base&65:continue
        values={u:f[base^u] for u in G}
        key=tuple(sorted(values.values()))
        distinct_hist[len(set(key))]+=1
        assert len(set(key))==4
        assert key not in seen
        seen.add(key)
        for number in key:key_digest.update(number.to_bytes(8,"big"))
        m0=min(values,key=values.get)
        min_offset_hist[m0]+=1
        e0=int(f[base]>f[base^64])
        e1=int(f[base^1]>f[base^65])
        twists[e0^e1]+=1
        for u in G:
            i=base^u
            m=m0^u
            assert f[i^m]==key[0]
            state_encodings.add((key,m))
            for t in (1,64):
                assert f[(i^t)^(m^t)]==key[0]
    assert len(seen)==16384
    assert len(state_encodings)==65536
    assert distinct_hist==Counter({4:16384})
    certificate={
        "schema":"R284DM_FOUR_ORBIT_RESIDUAL_CODE_V1",
        "date":"2026-11-22",
        "status":"AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED",
        "frozen_input":{
            "source_repository":"awdawmip/enterprise-math",
            "source_commit":"acba2d8667903434aaa2a10720f43637fcc2421b",
            "source_path":"research_notes/portable_direct/R284CO_spectral_witness_checker.py",
            "source_blob_sha1":"b46e0f682b58e47c27094b4bea6fa4e55119a3ee",
            "ordered_residues_sha256":FROZEN_SHA256,
            "P":P,"D":D,"Z":Z,"SELECT":SELECT},
        "population":{"states":len(words),"arcs":len(arcs),"joint_orbits":len(seen)},
        "checks":{
            "w_two_read_injective":True,"r_two_read_injective":True,
            "four_values_distinct_in_each_orbit":True,
            "unordered_four_value_keys_unique":True,
            "four_orbit_key_sha256":key_digest.hexdigest(),
            "complete_encoded_state_count":len(state_encodings),
            "xor_update_checked_each_state_both_generators":True},
        "statistics":{
            "distinct_values_per_joint_orbit":dict(sorted(distinct_hist.items())),
            "minimum_position_offset_counts":dict(sorted(min_offset_hist.items())),
            "w_pair_orientation_twist_counts":dict(sorted(twists.items()))},
        "method":"Python exact integers, 65536 words times 64 arcs; all 16384 four-state orbits and their 65536 orientations; no floating point",
        "independent_review":"NOT_REVIEWED"}
    return certificate

if __name__=="__main__":
    cert=verify()
    with open("R284DM_joint_orbit_code_certificate.json","w",encoding="utf-8") as out:
        json.dump(cert,out,ensure_ascii=False,indent=2)
        out.write("\n")
    print(json.dumps(cert["checks"],ensure_ascii=False,indent=2))
    print(json.dumps(cert["statistics"],ensure_ascii=False,indent=2))
