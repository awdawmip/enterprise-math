"""Exact reads for the finite marked atlas. No transport or native pilot is run."""
from argparse import ArgumentParser
from ast import Assign, Name, literal_eval, parse
from collections import Counter
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, product
from math import gcd
from pathlib import Path
from zipfile import ZipFile
import json

VFILE="experiments/x6_nonfcc_observer_switch_v42_20260906/check_nonfcc_observer_switch.py"
TASK="research_tasks/RS-BRC-X6-SLICE-CELL-PORT-BRIDGE-20261004-G2.md"
HFILE="experiments/brc_hidden_residual_20261003_fca717/HIDDEN_PLANE.md"
PUB="TP2-99169E1D950AC2D48D06"
RECORD="research_task_records/RS-BRC-X6-SLICE-CELL-PORT-BRIDGE-20261004/"+PUB+".json"
HASHES={VFILE:"b00d3a283b84bf2082eeb0e69b4d750eaf18fd38b90c36f6e1d711eca15763d2",
        HFILE:"fdd80255517589b0fabae26c29d6ce7b971f0d1d73abaee60f0b154273de24d6",
        TASK:"3f66127f6fbeace3096cfa63b75d08a44f836a9d68a12c535c0a249e28a175b6"}
INTAKE="1edf20e5880df29ca865e2249be429361ba6f1e24798cfb1ba6aebf1ec3bdc6d"
WINDOW={
    "5022eecf4aa542b2d7b7b39d9ec17f1a8d6dddc096f03cd5473caaef6d7c2294":
    "be05e209167114cdc140340831ade468ae1d516d212f21c6aaffe37f9317b503",
    "9005cfabd0908dab62ae7564ee6b04e0d8394dd492186e0e797d18de331fbc43":
    "d073018cd2456acced768a50c35fdd3fdc044383517e843450f531817e03d709",
    "dd97e6bd784dfd944149a05f7807c24abfe36f0c05d9f72561f8612566d34275":
    "ef087c9039d82dc4d58614e0fc091a4dd96020760d80e45591c7b0b74a16b807",
    "0163643eeba12bdfa78b8449aec191215a7e828c43c57bd473a758d674dcb2fa":
    "c21b6093295fd689341ceaaffe5e73e4e7193d144cd40faa4dc00b9e2ab8ba17",
    "2607eb40852c2ff267057b9ac8c61b883f7e24780409e9cec5f7ea4a4491a3ed":
    "4a122263f50c1fadec7e46fdf68aa27cf563c83f3e1e56ead68276d447cd683a",
    "84532593c6e4a036fba97d10259f70a1c0b880cdba3de6b4b1fbd995f61707bd":
    "22af1b655240faf9025754d9ecd3ed20da43a4c9e36000472e9de8b85557f5f9",
}
AXES=tuple(range(6))
CHARTS=tuple(combinations(AXES,3))
PARTS=tuple(c for c in CHARTS if 0 in c)


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def cross(a,b):
    return tuple(a[(i+1)%3]*b[(i+2)%3]-a[(i+2)%3]*b[(i+1)%3] for i in range(3))


def fcc(x):
    a,b,c=x
    assert (a+b+c)%2==0
    return ((a+b-c)//2,(a-b+c)//2,(-a+b+c)//2)


def complement(A):
    return tuple(i for i in AXES if i not in A)


def named(A):
    return ''.join(map(str,A))


def readV(V,x):
    return tuple(dot(row,x) for row in zip(*V))


def hdiff(x,A,signs):
    w=[i*j for i,j in zip(x,signs)]
    return tuple(w[i]-w[block[0]] for block in (A,complement(A)) for i in block[1:])


def smith2(a,b):
    d=gcd(*a,*b)
    return (d,gcd(*cross(a,b))//d if d else 0)


def scalar_column(V,S,sg):
    return tuple(sum(sg[i]*V[i][j] for i in S) for j in range(3))


def restricted_cols(V,A,T,convert):
    cols=[]
    for i in T:
        x=tuple(int(j==i) for j in AXES)
        h=hdiff(x,A,(1,)*6)
        cols.append(h+convert(V[i]))
    return list(zip(*cols))


def smith3(M):
    # Determinantal divisors, independent of the blockwise residual reduction.
    d1=gcd(*(a for row in M for a in row))
    d2=gcd(*(a[i]*b[j]-a[j]*b[i] for a,b in combinations(M,2) for i,j in combinations(range(3),2)))
    d3=gcd(*(dot(cross(a,b),c) for a,b,c in combinations(M,3)))
    return (d1,d2//d1,d3//d2)


def decision_depth(labels):
    questions=list(combinations(AXES,2))
    @lru_cache(None)
    def best(indices):
        if len({labels[j] for j in indices})==1:
            return 0
        result=len(PARTS)
        for u,v in questions:
            yes=tuple(j for j in indices if (u in PARTS[j])==(v in PARTS[j]))
            if len(yes) in (0,len(indices)):
                continue
            no=tuple(j for j in indices if j not in yes)
            result=min(result,1+max(best(yes),best(no)))
        return result
    return best(tuple(range(len(PARTS))))


def compute(V):
    star={S for S in CHARTS if dot(cross(V[S[0]],V[S[1]]),V[S[2]])==0}
    assert [named(s) for s in sorted(star)]==['025','034','124','135']
    rows=[]
    positive_charts=Counter()
    positive_ambient=Counter()
    signed=Counter()
    signed_ambient=Counter()
    checked_mod=0
    for A in PARTS:
        B=complement(A)
        table={}
        for flip in product((1,-1),repeat=4):
            signs=[1]*6
            for i,v in zip(A[1:]+B[1:],flip): signs[i]=v
            a=scalar_column(V,A,signs)
            b=scalar_column(V,B,signs)
            pair=smith2(fcc(a),fcc(b))
            ambient=smith2(a,b)
            signed[str(pair)]+=1
            signed_ambient[str(ambient)]+=1
            for m in (2,3,4,5,6,10):
                count=0
                for u,v in product(range(m),repeat=2):
                    # Native source vector in the unreduced six axes.
                    x=[signs[i]*(u if i in A else v) for i in AXES]
                    assert all(d%m==0 for d in hdiff(x,A,signs))
                    if all(c%m==0 for c in fcc(readV(V,x))):count+=1
                assert count==gcd(m,pair[0])*gcd(m,pair[1])
                checked_mod+=1
            if flip==(1,)*4:
                table.update({'partition':[named(A),named(B)],'sums':[a,b],
                              'global_FCC_smith_tail':pair,'global_ambient_smith_tail':ambient})
        special=[]
        for S in CHARTS:
            p=smith3(restricted_cols(V,A,S,fcc))
            q=smith3(restricted_cols(V,A,S,lambda x:x))
            positive_charts[str(p)]+=1
            positive_ambient[str(q)]+=1
            mono=S in (A,B)
            assert p==(1,1,(gcd(*fcc(scalar_column(V,S,(1,)*6))) if mono else 1))
            if q[-1]!=1:special.append([named(S),p[-1],q[-1]])
        table['ambient_nonprimitive_charts']=special
        rows.append(table)
    assert sorted(signed.values())==[6,16,48,90]
    x1=(2,0,0,0,2,2);x2=(0,-1,-1,-1,0,0)
    d=[a-b for a,b in zip(x1,x2)]
    A=(0,4,5)
    assert not any(hdiff(d,A,(1,)*6)) and all(v%5==0 for v in fcc(readV(V,d)))
    signed_kernel=(0,1,0,-1,0,1)
    assert not any(readV(V,signed_kernel))
    assert not any(hdiff(signed_kernel,(0,2,4),(1,1,1,-1,1,1)))
    atlas_gap=(0,1,-1,0,1,0)
    assert not any(readV(V,atlas_gap)) and all(any(hdiff(atlas_gap,A,(1,)*6)) for A in PARTS)
    purestar=[tuple(s for s in (A,complement(A)) if s in star) for A in PARTS]
    calibration={name:decision_depth(labels) for name,labels in [
        ('partition',list(PARTS)),('any_pure_STAR',[bool(x) for x in purestar]),
        ('which_pure_STAR',purestar),('named_025_pure',[((0,2,5) in x) for x in purestar])]}
    assert list(calibration.values())==[4,2,3,2]
    return {'source_native_column_order':['AB','CD','AC','BD','BC','AD'],'marks_STAR':list(map(named,sorted(star))),
            'positive_partition_rows':rows,'positive_chart_pair_counts':dict(positive_charts),
            'ambient_positive_chart_pair_counts':dict(positive_ambient),
            'signed_160_global_FCC_tail_counts':dict(signed),'signed_160_global_ambient_tail_counts':dict(signed_ambient),
            'modular_counts_independently_checked':checked_mod,
            'axis_pair_query_optimal_worst_case':calibration,'mod5_complementary_chart_collision':[x1,x2],
            'integer_signed_zero_collision':signed_kernel,'inherited_FACE_PATH_equal_FCC_difference':atlas_gap}


def main():
    ap=ArgumentParser()
    ap.add_argument('--repo',type=Path,required=True)
    ap.add_argument('--hidden',type=Path,help='pinned HIDDEN_PLANE.md if absent at its historical location')
    ap.add_argument('--intake',type=Path,help='optional authorized frozen source ZIP; no contents are printed')
    ap.add_argument('--out',type=Path)
    args=ap.parse_args()
    source={}
    for rel,digest in HASHES.items():
        p=(args.hidden or args.repo/rel) if rel==HFILE else args.repo/rel
        data=p.read_bytes()
        assert sha256(data).hexdigest()==digest
        source[rel]=data
    header=json.loads(source[TASK].decode().split('ENTERPRISE_MATH_TASK_V1',1)[1].split('-->',1)[0])
    rec=json.loads((args.repo/RECORD).read_text())
    assert rec['publication_id']==PUB and rec['publication_generation']==2
    assert rec['task_id']==header['task_id'] and rec['parent_task_id']==header['parent_task_id']
    assert ('Y=UX=(X_1+X_3+X_5,X_2+X_4+X_6)' in source[HFILE].decode())
    tree=parse(source[VFILE])
    V=next(literal_eval(t.value) for t in tree.body if isinstance(t,Assign) and
           any(isinstance(a,Name) and a.id=='V' for a in t.targets))
    if args.intake:
        assert sha256(args.intake.read_bytes()).hexdigest()==INTAKE
        with ZipFile(args.intake) as z:
            names={sha256(n.encode()).hexdigest():n for n in z.namelist()}
            for key,digest in WINDOW.items():
                assert sha256(z.read(names[key])).hexdigest()==digest
    result=compute(V)
    result.update({'registered_publication':PUB,'source_sha256':HASHES,
                   'public_source_window_bytes':sum(map(len,source.values())),
                   'intake_digest_as_declared_in_taskbook':INTAKE,
                   'published_scientific_status':'NATIVE_PORTS_UNKNOWN; CONDITIONAL_READOUT_ONLY'})
    content=json.dumps(result,sort_keys=True,indent=2)+'\n'
    if args.out:args.out.write_text(content)
    else:print(content,end='')


if __name__=='__main__':
    main()
