#!/usr/bin/env python3
"""R284DX: frozen Port full-state six-bit quotient with one threshold exception.
Exact integer exhaustive checker. No external packages or native X6 transfer.
"""
import hashlib
import itertools
import json
from collections import Counter
from pathlib import Path

P = 17179869143
D = (1120832, 6, 13, 1651128)
Z = (0, 390139, 394465, 1497639)
SELECT = (0, 1, 2, 4, 5, 6)
CORE = (0, 1, 2, 4, 5, 6)  # lower positions u1,a,x,u2,w,b
FROZEN_SHA = 'b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4'
Q_TABLE = (
 5640, 5152, 4385, 3898, 5495, 5007, 4240, 3752,
 5413, 4925, 4196, 3708, 5230, 4742, 4014, 3526,
 5494, 4969, 4240, 3714, 5242, 4716, 3987, 3461,
 5267, 4742, 4051, 3525, 4977, 4451, 3760, 3234,
 5139, 4689, 3992, 3542, 4994, 4543, 3847, 3396,
 4912, 4462, 3803, 3352, 4729, 4279, 3620, 3170,
 4993, 4505, 3846, 3358, 4740, 4252, 3593, 3105,
 4766, 4278, 3657, 3169, 4476, 3988, 3367, 2879,
)

def det(L, top):
    u1,a,x,y,u2,w,b,z,u3,g,h,r = L
    t,s = 6-a, 13-b
    u = t*s-x*w
    v = -r*u-z*(t*h+x*g)-y*(w*h+s*g)
    p1,p2 = s*u1+x*u2, t*u2+w*u1
    q1 = -r*p1-u1*z*h+x*z*u3+y*(u2*h+s*u3)
    q2 = -r*p2+t*z*u3+u1*z*g+y*(w*u3-u2*g)
    q3 = u*u3+p1*g+p2*h
    k = (u*D[3]+v,p1*D[3]+q1,p2*D[3]+q2,q3)
    base = D[0]*k[0]-Z[1]*k[1]-Z[2]*k[2]-Z[3]*k[3]-sum(k)
    return base-sum(k[j] for j in range(4) if top & (1<<j))

def arcs():
    out = []
    for label in range(64):
        lo,hi = [1]*12,[2]*12
        for j,pos in enumerate(SELECT):
            lo[pos] = hi[pos] = 1+((label>>(5-j))&1)
        H = det(hi,15)
        out.append((H%P,det(lo,0)-H))
    assert len(out)==64 and all(0<w<P//2 for _,w in out)
    return out

def dist(z,arc):
    a,w = arc
    gap = (z-a)%P
    return 0 if gap<=w else min(gap-w,P-gap)

def core_key(lower):
    return sum((lower[j]-1)<<k for k,j in enumerate(CORE))

def quotient_no_div(T,key):
    Q = Q_TABLE[key]
    return Q-int(key==63 and T<2879*P)

def main():
    A = arcs()
    digest = hashlib.sha256()
    obs_digest = hashlib.sha256()
    min_T,max_T = [10**100]*64,[-10**100]*64
    q_counts = [Counter() for _ in range(64)]
    by_top = [0]*65536
    direct_arc_checks = 0
    for upper in itertools.product((1,2),repeat=4):
        top = sum((v-1)<<j for j,v in enumerate(upper))
        for lower in itertools.product((1,2),repeat=12):
            key = core_key(lower)
            T = det(lower,top)
            quotient = quotient_no_div(T,key)
            residue = T-quotient*P
            assert 0<=residue<P
            assert quotient==T//P and residue==T%P
            digest.update(residue.to_bytes(8,'big'))
            values = [dist(residue,arc) for arc in A]
            winner = max(values)
            labels = tuple(i for i,d in enumerate(values) if d==winner)
            assert len(labels)==1
            obs_digest.update(residue.to_bytes(8,'big'))
            obs_digest.update(bytes([labels[0]]))
            obs_digest.update(winner.to_bytes(8,'big'))
            direct_arc_checks += 64
            min_T[key] = min(min_T[key],T)
            max_T[key] = max(max_T[key],T)
            q_counts[key][quotient] += 1
            index = (top<<12)+sum((v-1)<<i for i,v in enumerate(lower))
            by_top[index] = quotient
    assert digest.hexdigest()==FROZEN_SHA
    assert direct_arc_checks==4194304
    assert all(len(c)==1 and c[Q_TABLE[k]]==1024 for k,c in enumerate(q_counts[:63]))
    assert q_counts[63]==Counter({2878:446,2879:578})
    assert all(by_top[i]==by_top[i^(1<<15)] for i in range(65536))
    assert all(Q_TABLE[k]*P<=min_T[k]<=max_T[k]<(Q_TABLE[k]+1)*P for k in range(63))
    assert 2878*P<=min_T[63]<2879*P<=max_T[63]<2880*P
    return {
      'schema':'R284DX_FULL_FROZEN_PORT_SIX_BIT_QUOTIENT_V1',
      'status':'AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED',
      'source':'awdawmip/enterprise-math@acba2d8667903434aaa2a10720f43637fcc2421b:research_notes/portable_direct/R284CO_spectral_witness_checker.py',
      'source_git_blob_sha1':'b46e0f682b58e47c27094b4bea6fa4e55119a3ee',
      'source_frozen_codeword_sha256':FROZEN_SHA,
      'P':P,'state_count':65536,'core_bits':['u1','a','x','u2','w','b'],
      'key_bit_order':'u1=bit0,a=bit1,x=bit2,u2=bit3,w=bit4,b=bit5',
      'quotient_table':list(Q_TABLE),
      'stable_core_classes':63,'one_threshold_core_class':63,
      'threshold':2879*P,
      'threshold_core_count':1024,'lower_quotient_count':446,'upper_quotient_count':578,
      'all_classes_min_T':min_T,'all_classes_max_T':max_T,
      'all_class_quotient_counts':[{str(q):count for q,count in sorted(c.items())} for c in q_counts],
      'upper_mask_bit3_flip_quotient_invariant':True,
      'direct_integer_arc_checks':direct_arc_checks,
      'ordered_codeword_sha256':digest.hexdigest(),
      'ordered_residue_winner_value_sha256':obs_digest.hexdigest(),
      'all_exact_checks_passed':True,'review':'NOT_REVIEWED'
    }

if __name__=='__main__':
    report = main()
    path = Path(__file__).with_name('R284DX_six_bit_full_quotient_certificate.json')
    path.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({k:report[k] for k in ('state_count','stable_core_classes','threshold','lower_quotient_count','upper_quotient_count','ordered_codeword_sha256','ordered_residue_winner_value_sha256','all_exact_checks_passed')},indent=2))
