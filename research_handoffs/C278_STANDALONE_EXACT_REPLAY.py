#!/usr/bin/env python3
"""C271 self-contained author exact checker: all 595 C254 two-box hulls.
Only standard-library Fraction. The C195/H168 auxiliary, NOT native GF(2)-BRC.
"""
from fractions import Fraction as F
NUM=(0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 3, 3, 1, 6, 2, 3, 6, 1, 6, 3, 2, 7, 3, 4, 8, 1, 21, 9, 6, 4, 10, 14, 5, 11, 2, 9, 12, 13, 14, 3, 7, 15, 17, 14, 5, 6, 13, 15, 17, 10, 11, 13, 16, 18, 22, 28, 36, 46, 63, 96, 152, 246, 528, 1971, 1)
DEN=(1, 2057, 539, 289, 136, 93, 68, 51, 39, 31, 27, 21, 17, 15, 13, 11, 10, 9, 8, 7, 13, 6, 11, 5, 14, 13, 4, 23, 7, 10, 19, 3, 17, 8, 5, 17, 7, 9, 17, 2, 41, 17, 11, 7, 17, 23, 8, 17, 3, 13, 17, 18, 19, 4, 9, 19, 21, 17, 6, 7, 15, 17, 19, 11, 12, 14, 17, 19, 23, 29, 37, 47, 64, 97, 153, 247, 529, 1972, 1)
BOX_DATA="4/543,43/62,4/5,9/11,9/613,57/79,38/47,121/147;3/407,5/7,60/77,4/5,7/477,18/25,53/67,9/11;3/407,5/7,18/23,4/5,6/409,31/43,87/109,4/5;3/407,5/7,4/5,81/101,7/477,31/43,21/26,76/93;2/271,7/10,60/77,4/5,6/409,42/59,11/14,4/5;2/271,7/10,4/5,13/16,6/409,27/38,4/5,58/71;2/271,12/17,26/33,4/5,3/233,12/17,59/74,4/5;1/135,16/23,18/23,9/11,3/205,5/7,4/5,9/11;1/135,7/10,26/33,4/5,3/283,7/10,27/34,4/5;1/135,7/10,4/5,49/61,2/137,7/10,4/5,31/38;1/135,12/17,4/5,57/71,3/205,12/17,4/5,30/37;1/127,16/23,18/23,4/5,1/106,16/23,4/5,13/16;3/371,7/10,15/19,4/5,2/171,17/24,53/67,4/5;1/123,34/49,15/19,4/5,1/69,7/10,59/74,4/5;1/123,26/37,48/61,4/5,1/78,27/38,15/19,4/5;1/119,19/27,4/5,17/21,3/205,12/17,4/5,69/85;1/119,12/17,18/23,13/16,3/205,12/17,11/14,9/11;1/119,12/17,15/19,13/16,1/74,12/17,15/19,22/27;1/119,5/7,60/77,19/24,1/69,28/39,34/43,41/51;1/119,5/7,18/23,17/21,3/205,5/7,59/74,9/11;1/117,19/27,4/5,21/26,1/85,22/31,4/5,17/21;1/105,7/10,53/68,9/11,3/205,18/25,53/67,23/28;1/105,12/17,4/5,13/16,1/74,42/59,21/26,9/11;1/104,34/49,18/23,4/5,1/69,7/10,34/43,4/5;1/104,34/49,4/5,41/51,1/69,30/43,4/5,22/27;1/103,7/10,27/34,4/5,2/155,22/31,87/109,4/5;1/103,12/17,18/23,21/26,1/86,12/17,18/23,13/16;2/189,7/10,32/41,4/5,3/205,19/27,37/47,4/5;1/93,16/23,18/23,13/16,2/137,7/10,15/19,9/11;1/93,12/17,18/23,19/24,6/409,27/38,15/19,4/5;1/93,12/17,18/23,21/26,1/69,12/17,11/14,17/21;1/93,12/17,19/24,13/16,1/69,12/17,27/34,13/16;1/89,12/17,15/19,21/26,1/69,12/17,15/19,13/16;1/88,12/17,26/33,4/5,3/232,29/41,72/91,4/5;1/77,7/10,26/33,4/5,6/409,12/17,63/79,4/5"
U=tuple(F(a,b) for a,b in zip(NUM,DEN))
Q=2**128; H=2**166; A=F(6912*50000**2,17**2)
Z=F(141421356237309504880,10**20)
I=(5,50,55,56)
J=tuple(k for k in range(79) if k not in I)
assert len(U)==79 and all(U[k]<U[k+1] for k in range(78))
assert U[54]==F(7,9) and U[55]==F(15,19) and U[56]==F(17,21)
assert U[56]-U[54] == F(2,63) < Z-U[56]
D=[]
for item in BOX_DATA.split(';'):
    z=tuple(map(F,item.split(',')))
    assert len(z)==8
    l,h=z[:4],z[4:]
    assert all(U[p-1]<l[d]<=h[d]<U[p+1] for d,p in enumerate(I))
    assert l[2]<l[3] and h[2]<h[3]
    D.append((l,h))
assert len(D)==35
basic_delta=[h[2]-l[3] for l,h in D]
assert [k for k,g in enumerate(basic_delta) if g>0]==[3]
assert [k for k,g in enumerate(basic_delta) if g==0]==[11]
assert basic_delta[3]==F(15,2626)



# C278 author exact positive certification for the whole legal continuous hull.
# Source input above is from frozen C275; all proof decisions below are exact.
import base64, zlib, hashlib, json, argparse
TREE_SHA="f1c4a4578b1dd1cf24f6c98cfef9478a47c66195297991e3231d4b237ceed00a"
TREE=("eNpNlUGCxCAIBFMhjPv/F68CjVyGiiJIJwPP+/1+799zjIVZ+bTiab1PGsLY8/0Eq8C14nkyyL6LnkgtoQP0gU0nm+dNtt"
"nhBV6AVsiVfbNPEBGTVhHapDfRpqLr8kna1Enrk1YnlfLkSUs9550kT0DUlmTfRTm6HL0dS4Rzg59Am9wo3CgoCh0lpbT9"
"NuN3nRuH9VeQ+4vaOXe3bzu+P8F6mngvWqHJ0VaCv7+vyUXre97Bdpmxzl334e/D34e/t79u4baDX6TxhrMRzkY463Coek"
"7178XeXhTViuvAKJRRKKNQRqGMQhmFMgplFIoK5RbKLZRRKKNQRqF0ofv/Ex/EsZ6WeiafV+3Hq3wuRiixNS9RXDKp1ipw"
"KPW8g+0yjTrUgahA8WF+TS4q0cV2mbHOXffh78Pfh7+3f14jvvGbyEYiG4lsJDqv4OJw6dj55QQshfb61BK5q31IF9qyPE"
"3taHKk1aLVYqjFUIuhFkMthloMtRhqMdRCajHUYqjFUIuhFp+NRDYS2Uh0pUPScaXjSseVjiudPqn4op4m/jgzL3538yRH"
"HmfWxe8ZEmjA0QNOlK5nWKT1bWN+ofmF5lcCYc88TVvP8lQezSI0i+hZRM8iahZRsyhsBMwRRI8gkRW5NitKzJoCrex4MT"
"+o+ZE2V8+/mpoa5Fwoa2nPG6J7/kUazwtndPlmuZgi7A+lKdNR6ah0KF102KZy9uOULY9qeVTLo1oe1fJQb2taIus1q7U6"
"r+xqYHQDoxsY1bYE8fdgdK1mGn24+HBxuZjCWUqsFtToSa685y/SVG6uKLomuma0giYvMm1abyqRdGgZQvp/VEEorg==")

def paths():
    raw=zlib.decompress(base64.b64decode(TREE))
    assert hashlib.sha256(raw).hexdigest()==TREE_SHA and raw[-1]==8
    out=[]
    for seg in raw[:-1].split(bytes([8])):
        assert seg and all(0<=v<8 for v in seg)
        out.append(tuple((v//2,v%2) for v in seg))
    return out

def structural_check(ps):
    root={}
    for p in ps:
        n=root
        for edge in p:
            assert "leaf" not in n
            n=n.setdefault(edge,{})
        assert not n
        n["leaf"]=True
    def walk(node):
        if "leaf" in node:
            assert len(node)==1
            return 1,0
        assert len(node)==2
        edges=list(node)
        assert edges[0][0]==edges[1][0] and {edges[0][1],edges[1][1]}=={0,1}
        a,b=walk(node[edges[0]]);c,d=walk(node[edges[1]])
        return a+c,b+d+1
    return walk(root)

def subbox(path):
    lo=[min(D[13][0][d],D[29][0][d]) for d in range(4)]
    hi=[max(D[13][1][d],D[29][1][d]) for d in range(4)]
    assert lo==list(map(F,["1/123","34/49","18/23","19/24"]))
    assert hi==list(map(F,["6/409","27/38","59/74","4/5"]))
    for d,side in path:
        mid=(lo[d]+hi[d])/2
        if side:lo[d]=mid
        else:hi[d]=mid
    return lo,hi

def base_weights():
    w={}
    for j in J:
        u=U[j]; m=F(Q)*A/H/((2-u*u)*(3-u*u))**3
        for r in range(79):
            if r!=j:m*=(Z-U[r])/abs(u-U[r])
        w[j]=m.numerator//m.denominator
        assert w[j]>0
    return w

def factor(j,k,x):
    return (Z-x)/(Z-U[k])*abs(U[j]-U[k])/abs(U[j]-x)

def supporting_line(j,k,l,h):
    t=(l+h)/2
    val=factor(j,k,t)
    slope=val*(-1/(Z-t)-1/(t-U[j]))
    a=val-slope*t
    if a+slope*l>=0 and a+slope*h>=0:
        return a,slope
    endpoint=l if j>k else h
    return factor(j,k,endpoint),F(0)

def fixed_bound(lo,hi,weights):
    corners=[F(0)]*4
    for j in J:
        pref=F(weights[j])
        for d in (0,1):
            endpoint=lo[d] if j>I[d] else hi[d]
            pref*=factor(j,I[d],endpoint)
        a,b=supporting_line(j,55,lo[2],hi[2])
        c,d=supporting_line(j,56,lo[3],hi[3])
        for n,(x,y) in enumerate(((lo[2],lo[3]),(lo[2],hi[3]),(hi[2],lo[3]),(hi[2],hi[3]))):
            corners[n]+=pref*(a+b*x)*(c+d*y)
    return min(corners)

def moving_bound(lo,hi):
    result=F(0)
    for d,k in enumerate(I):
        t=(lo[d]+hi[d])/2
        others=[(r,lo[r] if r<d else hi[r]) for r in range(4) if r!=d]
        if any(t<=e if r<d else t>=e for r,e in others):
            continue  # Zero is always an exact lower bound for positive branch.
        v=F(Q)*A/H/((2-t*t)*(3-t*t))**3
        slope=6*t/(2-t*t)+6*t/(3-t*t)
        for j in J:
            v*=(Z-U[j])/abs(t-U[j])
            slope-=1/(t-U[j])
        for _,e in others:
            v*=(Z-e)/abs(t-e)
            slope-=1/(t-e)
        endpoint=lo[d] if slope>=0 else hi[d]
        result+=max(F(0),v*(1+slope*(endpoint-t)))
    return result

def pair_seam_bound(lo,hi):
    result=F(0)
    for k in (55,56):
        d=I.index(k); lower,upper=lo[d],hi[d]
        mass=F(Q)*A/H/((2-lower*lower)*(3-lower*lower))**3
        for j in J:
            mass*=(Z-U[j])/max(abs(lower-U[j]),abs(upper-U[j]))
        for r in range(4):
            if r==d:continue
            if r<d:
                assert upper>lo[r]
                mass*=(Z-lo[r])/(upper-lo[r])
            else:
                assert hi[r]>lower
                mass*=(Z-hi[r])/(hi[r]-lower)
        result+=mass
    return result

def check(start=0,end=None):
    ps=paths()
    n,m=structural_check(ps)
    assert (n,m)==(267,266)
    if end is None:end=n
    assert 0<=start<end<=n
    w=base_weights()
    counts={"strict_bilinear":0,"strict_seam_two_masses":0,"empty":0}
    min_ratio=None
    cutoff=Q*(1+F(1,1000000))
    for idx in range(start,end):
        lo,hi=subbox(ps[idx])
        if lo[2]>=hi[3]:
            counts["empty"]+=1; continue
        if hi[3]-lo[2]<=F(1,3077):
            bound=pair_seam_bound(lo,hi)
            assert bound>cutoff,("bad seam",idx)
            counts["strict_seam_two_masses"]+=1
        else:
            bound=fixed_bound(lo,hi,w)+moving_bound(lo,hi)
            assert bound>cutoff,("bad bilinear",idx)
            counts["strict_bilinear"]+=1
            if min_ratio is None or bound/Q<min_ratio:min_ratio=bound/Q
    return {"result":"C278_AUTHOR_EXACT_SELF_CONTAINED_PASS",
        "pair":[13,29],"leaves":n,"internal":m,
        "range":[start,end],"counts":counts,
        "minimum_bilinear_ratio_display_only":float(min_ratio) if min_ratio else None,
        "scope":"ALL_LEGAL_CONTINUOUS_HULL","source_admitted":False}

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--start",type=int,default=0)
    parser.add_argument("--end",type=int)
    args=parser.parse_args()
    print(json.dumps(check(args.start,args.end),ensure_ascii=False,indent=2))
