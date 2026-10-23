#!/usr/bin/env python3
"""C266 independent exact four-variable (0,16) proof replay: 3088 leaves.

No third-party imports. The single preorder tree is fixed certificate data, not
proof authorities: every leaf's rational inequality is recomputed from 79 nodes.
AUTHOR_EXACT, non-native and not independently Driver-admitted.
"""
from fractions import Fraction as F
NUM=(0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 3, 3, 1, 6, 2, 3, 6, 1, 6, 3, 2, 7, 3, 4, 8, 1, 21, 9, 6, 4, 10, 14, 5, 11, 2, 9, 12, 13, 14, 3, 7, 15, 17, 14, 5, 6, 13, 15, 17, 10, 11, 13, 16, 18, 22, 28, 36, 46, 63, 96, 152, 246, 528, 1971, 1)
DEN=(1, 2057, 539, 289, 136, 93, 68, 51, 39, 31, 27, 21, 17, 15, 13, 11, 10, 9, 8, 7, 13, 6, 11, 5, 14, 13, 4, 23, 7, 10, 19, 3, 17, 8, 5, 17, 7, 9, 17, 2, 41, 17, 11, 7, 17, 23, 8, 17, 3, 13, 17, 18, 19, 4, 9, 19, 21, 17, 6, 7, 15, 17, 19, 11, 12, 14, 17, 19, 23, 29, 37, 47, 64, 97, 153, 247, 529, 1972, 1)
I=(5,50,55,56);J=tuple(i for i in range(79) if i not in I)
U=tuple(F(n,d) for n,d in zip(NUM,DEN));Z=F(141421356237309504880,10**20)
A=F(6912*50000**2,17**2);H=2**166;Q=2**128
assert len(U)==79 and all(U[i]<U[i+1] for i in range(78))
B={}
for j in J:
    v=F(Q)*A/H/((2-U[j]*U[j])*(3-U[j]*U[j]))**3
    for r in range(79):
        if r!=j:v*=(Z-U[r])/abs(U[j]-U[r])
    B[j]=v.numerator//v.denominator
    assert B[j]>0

def moving(k,lo,hi,pair=True):
    d=I.index(k);t=(lo[d]+hi[d])/2
    val=F(Q)*A/H/((2-t*t)*(3-t*t))**3
    slope=6*t/(2-t*t)+6*t/(3-t*t)
    for j in J:
        val*=(Z-U[j])/abs(t-U[j]);slope-=1/(t-U[j])
    if pair:
        for p in I:
            if p==k:continue
            dd=I.index(p);e=lo[dd] if p<k else hi[dd]
            val*=(Z-e)/abs(t-e);slope-=1/(t-e)
    return val,val*slope,t

def lower_base(lo,hi):
    total=F(0)
    for j in J:
        v=F(B[j])
        for d,p in enumerate(I):
            e=lo[d] if j>p else hi[d]
            v*=(Z-e)/(Z-U[p])*abs(U[j]-U[p])/abs(U[j]-e)
        total+=v
    for d,k in enumerate(I):
        v,der,t=moving(k,lo,hi,pair=False)
        x=max(F(0),v+der*((lo[d] if der>=0 else hi[d])-t))
        for dd,p in enumerate(I):
            if p==k:continue
            if k<p:x*=(Z-hi[dd])/(hi[dd]-lo[d])
            else:x*=(Z-lo[dd])/(hi[d]-lo[dd])
        total+=x
    return total

def lower_shared(k,lo,hi):
    d=I.index(k);s=(lo[d]+hi[d])/2
    value=F(0);slope=F(0)
    for j in J:
        v=F(B[j])
        for dd,p in enumerate(I):
            if p==k:continue
            e=lo[dd] if j>p else hi[dd]
            v*=(Z-e)/(Z-U[p])*abs(U[j]-U[p])/abs(U[j]-e)
        v*=(Z-s)/(Z-U[k])*abs(U[j]-U[k])/abs(U[j]-s)
        value+=v;slope+=v*(-1/(Z-s)-1/(s-U[j]))
    v,der,_=moving(k,lo,hi)
    value+=v;slope+=der
    value+=slope*((lo[d] if slope>=0 else hi[d])-s)
    for p in I:
        if p==k:continue
        dd=I.index(p);v,der,t=moving(p,lo,hi)
        value+=v+der*((lo[dd] if der>=0 else hi[dd])-t)
    return value


# Strict exact leaf proof and 21 pair inclusions; zlib+base64 is lossless storage,
# verified by SHA256, not a numerical proof or cryptographic theorem check.
import base64,zlib,json,hashlib
TREE=zlib.decompress(base64.b64decode("eNqNWMehIyEMbYlQgui/pkVPGRj/vdgwCKGcxuytz9F6W6vtf6K9GGv/zNHX6mvylleTPzV8W/tvbhA9bvgg3xXNYgz6x4gStEACXcPJ4BdwykD8aRhwU2j9423DqYI0xmJ3WiDZFIy2OdvcEOnf7IMmEX72ci+IQXQlfxt0GPBs1GXX975hLfc2gr2VU4ApDoAponjLzzdKhmB0pEvcZ1gslTK/GLj4jwELGaQbO3Ss/IDiAeKZAJvjnYmdMY/HsC0vC2b+GsR3x18vGwiEVBiZJgkoRT9jQUkX+XI8BiiF+SA4SLXTg1xKor4xvKSVWTRQMACShXSKN5Vh9gFTCO/FihuMmM1znJair+j1VdWezEctzu0taRWX+JnJZIhfqd+wg8HbGGaI7/FSYEGpn8F/9qm8uhKwMRVacHcpDDkvKhvdPqwqLmQfcjEPFQj+llxf/baAAPPnkt9VCZKwbIdjOKG6WIGChTjC+uXRbByHP1LPfv60UtJocn52pD3MJrm0uT/9xjyeuJ2sz+vzFUyCgEogTMwkFJumVofALTF7etQWU4QNsjHtNfEGSlY610jKG4JpwS45JQnwCPCwAvE5ZkGedBOXJceapBGFLIrs9K2TpPMrNtSIpYLEc2AD9KcHv3T+82mLYzed/qlb9g3xTbffv9URcn5KeYmMXS1rZc2hXFDuWzyht7tn9wszlwCKK97fF4am76JlSuUHCZmaDs/Ec3/qxVJA8hnPm3jHVwoU6Flz2AE9EsYnHek0Irm6+WGdJ2szHPmKaDeTha/OwsphE5+6B7WDiJSx7trDzwvwhyAOzvH8+nH0oCdFK/Ii5cH6Q5tjZtQptPe/K52rkvkyMsfeUmIpoomYnUJbT5ZYDk5Bvvntlz2e1vgftkjV4OmTc6q1z8t4lRAj1iLhi7JqSV8gXxb0ZT/0S0pPZR6SORT5dooP84uy8/1UMsHY0o/QFfpbUTUl8yq9wG1a9PbKNv4vWBayhzvgdbleXZlkTgS7+RKTth4M3ZfVdP1tclo2L5aWdZ/eTeKTl6RHX3hlFwXRhOF5aaBPRZNo6XCW5nJpauS+UtvL1UpHyocA4xz17YdSBWh70K254e3MPQ/sCyX/cO3/QJp7Ibs5ElaInYVuRPBdJMtaqeg9fLRknUG6qoxS9EVnr/rKcwCkd/4gfULO/yp9qcFUFIvLIluWpN6GblEcsLRRfJju7lKccif/7JWTQI9OJAWhV/Q566jjkVckqm6SrJuqc4CNnNnMZtn4+c+mG83tXQTRSmOL5kv6Pq2grGyCr3QZvehoR4SqHRtJA5p7Trm12RreDcg8BaoVz1kd6KfZiHrxGURjKT1+MqwlPrBG7fOtHZ/DpkgDg6QoArV3Lp2zxdVUV5RPR/8rrgv7RCkZQ6qINKXbAzqjbx01TAC4JldwOcWSJT7NdRfdvPKuxAS+AkM60jC6vtBn5Iq6FT61opbNFTf3fgsCpkOQRk/jtSa3yclaFnlR0ZdpoKiobIXQoXFvegzkRC52FCMgm96VWAUjXsdWY48ZJySprVbXaF2FoxQzoEXH7YnT/Q1ImlxkIWhbsq/jufZgNEuRJdavMWUkI/ZnBdADAoh/WwKgi91dp2GsBVcVeTdmhuhOPcWF32xqip5cBqD8lk42Za5ZBjzSvcXAxTr6z8zNGiK6+vfvsZzFW72IaNYM4ccFGTJI+67k3LWClRhWadtkzgIe95T8M80ddJQggwGAcYigwZFTlgt1himbRAEpmTXzI3KLEKPfS7FLNU5RVrs8A2rBwN2CNaxhSuuuWSqGLGlWhHg/bc6hDiWZDqfCj2RhEC+8wzyX2jdV3owkZIk+8B4cafMIEF7+AxuGgSU=")).decode("ascii")
BOXES=json.loads(zlib.decompress(base64.b64decode("eNqtk1myhCAMRffit1WXBEJgLZb738YLKq8HkLaHH3GgTk6uYVncTHFepgAJfpqn4BHZVkrg8kweFKfVdmREKm9EodlWnxC07GAC2d1qmwymPZiA8gcwTj8089SDZXB4GyZz6ZLBSuVLPIQasYjgCkNQCFbbrhlEB2QLvlIU5IYQVvjUxWgH0yTex0iCVs6W9vWmTn22oJ99mpxf+egej4XuZejjwU7OQtY9na8pzB9QbGI4PnHSL2y2hL+kWLq1qX1SGKRDTGBI7rVVUOke9dLov9gxpjeUnlg180zQMJTSq1JWwutIyowqyskl1KmVoerPewyiOR+EmIekVEnZv9VeOXDhRlr/ADChKic=")).decode("ascii"))
assert hashlib.sha256(TREE.encode()).hexdigest()=="8693d9b0b2c0d64d88ecb664d5f7b0d5dac908607b10fd5475742dae52c36d9c"
assert hashlib.sha256(json.dumps(BOXES,separators=(',',':')).encode()).hexdigest()=="185982c8cf724acc5af2ecf7876d7c5f56f5682540362232ffd728a434a625ae"
ROOT_LO=("4/543","43/62","18/23","13/16")
ROOT_HI=("9/613","57/79","38/47","121/147")
LEAF={'B':None,'A':5,'C':50,'D':55,'E':56}
EXPECTED_MIN_MARGIN=124257021339851230269272891404511
EXPECTED_LEAVES=3088
assert len(TREE)==2*EXPECTED_LEAVES-1
rootlo=tuple(F(t) for t in ROOT_LO);roothi=tuple(F(t) for t in ROOT_HI)
assert all(U[k-1]<rootlo[d]<roothi[d]<U[k+1] for d,k in enumerate(I))
assert roothi[2]<rootlo[3] and roothi[3]<Z
for i,j,los,his in BOXES:
    blo=tuple(F(t) for t in los);bhi=tuple(F(t) for t in his)
    assert all(rootlo[d]<=blo[d]<=bhi[d]<=roothi[d] for d in range(4)),(i,j)
assert len(BOXES)==21 and len(set((r[0],r[1]) for r in BOXES))==21
position=[0];minimum=[None];leaves=[0];splits=[0];hist={m:0 for m in LEAF}
def walk(lo,hi):
    i=position[0];assert i<len(TREE)
    symbol=TREE[i];position[0]=i+1
    if symbol in LEAF:
        k=LEAF[symbol]
        v=lower_base(lo,hi) if k is None else lower_shared(k,lo,hi)
        margin=v.numerator//v.denominator-Q
        assert margin>0,(i,symbol,margin)
        if minimum[0] is None or margin<minimum[0]:minimum[0]=margin
        leaves[0]+=1;hist[symbol]+=1
        return
    d=int(symbol);assert 0<=d<4 and lo[d]<hi[d]
    mid=(lo[d]+hi[d])/2
    left_hi=list(hi);left_hi[d]=mid
    right_lo=list(lo);right_lo[d]=mid
    splits[0]+=1
    walk(lo,tuple(left_hi));walk(tuple(right_lo),hi)
walk(rootlo,roothi)
assert position[0]==len(TREE)
assert leaves[0]==EXPECTED_LEAVES and splits[0]==EXPECTED_LEAVES-1
assert minimum[0]==EXPECTED_MIN_MARGIN
assert hist['C']==2241 and hist['D']==847
print('C266_STANDALONE_EXACT_PASS',leaves[0],'leaves',splits[0],'splits',len(BOXES),'new_pairs',minimum[0],'integer_margin',hist)
