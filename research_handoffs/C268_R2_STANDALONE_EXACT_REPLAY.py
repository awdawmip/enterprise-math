#!/usr/bin/env python3
"""C268 author-exact certificate: 6890 leaves, three complete 4D rational boxes.
Model: C195/H168 positive 79-node rational interpolation auxiliary; no native BRC correspondence or independent Driver admission.
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

LEAF={'B':None,'A':5,'C':50,'D':55,'E':56}
ROOTS=[([0,16],["4/543","43/62","18/23","13/16"],["9/613","57/79","38/47","121/147"],"eNqNWMehIyEMbYlQgui/pkVPGRj/vdgwCKGcxuytz9F6W6vtf6K9GGv/zNHX6mvylleTPzV8W/tvbhA9bvgg3xXNYgz6x4gStEACXcPJ4BdwykD8aRhwU2j9423DqYI0xmJ3WiDZFIy2OdvcEOnf7IMmEX72ci+IQXQlfxt0GPBs1GXX975hLfc2gr2VU4ApDoAponjLzzdKhmB0pEvcZ1gslTK/GLj4jwELGaQbO3Ss/IDiAeKZAJvjnYmdMY/HsC0vC2b+GsR3x18vGwiEVBiZJgkoRT9jQUkX+XI8BiiF+SA4SLXTg1xKor4xvKSVWTRQMACShXSKN5Vh9gFTCO/FihuMmM1znJair+j1VdWezEctzu0taRWX+JnJZIhfqd+wg8HbGGaI7/FSYEGpn8F/9qm8uhKwMRVacHcpDDkvKhvdPqwqLmQfcjEPFQj+llxf/baAAPPnkt9VCZKwbIdjOKG6WIGChTjC+uXRbByHP1LPfv60UtJocn52pD3MJrm0uT/9xjyeuJ2sz+vzFUyCgEogTMwkFJumVofALTF7etQWU4QNsjHtNfEGSlY610jKG4JpwS45JQnwCPCwAvE5ZkGedBOXJceapBGFLIrs9K2TpPMrNtSIpYLEc2AD9KcHv3T+82mLYzed/qlb9g3xTbffv9URcn5KeYmMXS1rZc2hXFDuWzyht7tn9wszlwCKK97fF4am76JlSuUHCZmaDs/Ec3/qxVJA8hnPm3jHVwoU6Flz2AE9EsYnHek0Irm6+WGdJ2szHPmKaDeTha/OwsphE5+6B7WDiJSx7trDzwvwhyAOzvH8+nH0oCdFK/Ii5cH6Q5tjZtQptPe/K52rkvkyMsfeUmIpoomYnUJbT5ZYDk5Bvvntlz2e1vgftkjV4OmTc6q1z8t4lRAj1iLhi7JqSV8gXxb0ZT/0S0pPZR6SORT5dooP84uy8/1UMsHY0o/QFfpbUTUl8yq9wG1a9PbKNv4vWBayhzvgdbleXZlkTgS7+RKTth4M3ZfVdP1tclo2L5aWdZ/eTeKTl6RHX3hlFwXRhOF5aaBPRZNo6XCW5nJpauS+UtvL1UpHyocA4xz17YdSBWh70K254e3MPQ/sCyX/cO3/QJp7Ibs5ElaInYVuRPBdJMtaqeg9fLRknUG6qoxS9EVnr/rKcwCkd/4gfULO/yp9qcFUFIvLIluWpN6GblEcsLRRfJju7lKccif/7JWTQI9OJAWhV/Q566jjkVckqm6SrJuqc4CNnNnMZtn4+c+mG83tXQTRSmOL5kv6Pq2grGyCr3QZvehoR4SqHRtJA5p7Trm12RreDcg8BaoVz1kd6KfZiHrxGURjKT1+MqwlPrBG7fOtHZ/DpkgDg6QoArV3Lp2zxdVUV5RPR/8rrgv7RCkZQ6qINKXbAzqjbx01TAC4JldwOcWSJT7NdRfdvPKuxAS+AkM60jC6vtBn5Iq6FT61opbNFTf3fgsCpkOQRk/jtSa3yclaFnlR0ZdpoKiobIXQoXFvegzkRC52FCMgm96VWAUjXsdWY48ZJySprVbXaF2FoxQzoEXH7YnT/Q1ImlxkIWhbsq/jufZgNEuRJdavMWUkI/ZnBdADAoh/WwKgi91dp2GsBVcVeTdmhuhOPcWF32xqip5cBqD8lk42Za5ZBjzSvcXAxTr6z8zNGiK6+vfvsZzFW72IaNYM4ccFGTJI+67k3LWClRhWadtkzgIe95T8M80ddJQggwGAcYigwZFTlgt1himbRAEpmTXzI3KLEKPfS7FLNU5RVrs8A2rBwN2CNaxhSuuuWSqGLGlWhHg/bc6hDiWZDqfCj2RhEC+8wzyX2jdV3owkZIk+8B4cafMIEF7+AxuGgSU=","8693d9b0b2c0d64d88ecb664d5f7b0d5dac908607b10fd5475742dae52c36d9c",3088,int("124257021339851230269272891404511")),
([5,21],["2/271","7/10","53/68","13/16"],["6/409","18/25","4/5","23/28"],"eNqdWAmS3DAI/JKOJ0D+/6UIujlkz2STVG3t2LqABhrkuddYe8wlY08R8X/2ch5FzvCeQ+T8TRs+C8XffIMvxCKfFJtfI3fgZ+f8ebHF59GEDdVhj3g4y+Y+T3r+LV+hevTK9SbfpK9LXs7PqRsbBHIeapxzJzVYNCzUoLDzoFjWpbpFIhoyS2LK8nmHYcsl4ZzdRQ7MT4MSZweeYgt9rCE5R+CxKHDlQf7qZu9lS5btFx6y/EHp1TQ3IQvE8GOLUu80SS5zODzbtvE8aPu6LtCXxZpvomA+t3PuoeEBQh0Jd/HInXppcw8rtSnEiTeEQWzCsV+ANBV2GfIZMyZKGTTluzF2tFmiV2gdb2H0Ft0EfxMq3/wKQbcQyzQdTVUM38fZcB15EsQOsX/2eA6wRFUD2VNM7P38Qz6rJ/t59eA3Z4kglGEzNfREhUa2v2sYU6Qh+CuI5lPozgh9OjEzARlkyYF8gAIJb+X2ekVrAmJ660iUhSkduZrijDbibHmcq4MgFwcAKmpbp+nkdOC/jIUFKIsbC18Meg3ow7rOIUz+OQ4xuNkH1eE/exXJwhPn4UCzMeTmqv3uSDc7wglytkN6lBKcYt7R/ROLfPa5DHF0NFolU6nGGbT4XVTN4sKRXti0nKUVbGXWh1lG5H+lc8ujh8Y6ex15LJng4wNfRgWwFAdwaxihutox1I+AvjxCih9hQnOGlbU41krkIl6YHKEH6l9/GfQwf7KaIBcLb4DvUqiTF5QyL1auEUz14bA4Sm2s6LqFkusK9knHJXdPedXci96dGEHtuaa/rg973umNQtDKTQ9giQaGFB2H/JuM/1H1wDH1g7oANVobqHu9eDRkzESs0DUeI5rzD18hkCrKznrxjBvZRol4rCE2GNb0uWmIn758wNs+SW2QqQ2S//ac3FmJEl50/nJrL+YfvaHffPHdqdrEh1yeZ1sfjgpygwvMGc1JmulXbqFTEvEX3i/n0NMS9NgcAO+sL/DqShVHslPGgPZtymKqrDuX2NmzusoqyvndmdGFf5NC1cypW12NTut5Wqemn/r1dpYd8q8KeDeGzv4nRQgCyv3V30b4vyVW75XJE23+Fpq3smp4AXi8XpmZWVaifsb2alu1at1l5cem+CfkLgEw9GchGUvRDT62rNZGSAfsK1xaKcaEugU8mnAPbQtrNBy5VKtJrVYjs3VRn9X5x+kXNNOo+Fkvo7WZuMEtNohuVbQHr41sCsLcp7He9il3jlbScQLboxixJYAsiedDYX+rHoSWbWa0NH4s6z/VPdMIDfdelh2JLtRZDX6UOAwAyO55ld4WmrDQPike58W1KzUI6r0CoZg2iRWupIC4REkVwa8Lg2glBlsgP9JFIsXvG0JNXedcIZ35fwf0gR9tJVbxdzgcrZtUfh4pkFo3lzcARETvDe/ixLvZs8pWqfDrSHWOLcV5lbIcekRzBFx1DFG7ohTFtceTj8FPLpg1Vn3uyrv/63an8oepyXY64gwttLR0QJhffX3qw5ZMe+LPgNnvaDt8oeCKhrDGZTWvqvy0E0ndGm7mo3IayE4m42YP0MFd9SkpL8J+f/e+JaqXXBlGy9dAfnmM5E1gNLZJvuUHtB76Tq9shOKjAUb8MuMfDIrXB0aqJJoty5QeebNFLTKGA9coCZF3l3ATPnSMZMdfG0vmB0Icn5nZ9sO5mjcuo7g5wnT20Y61q5mfBbZ7zz2d3hmpRjV5qd+gIknBJPgljeDr5Tc4ffV0","aa94685f90c0f3ee2cb6cb939b908eff432302374a52ef7deda9d9cf4b02f5c9",2779,int("769356085001379917978497393182991")),
([18,29],["1/119","12/17","60/77","19/24"],["6/409","28/39","34/43","41/51"],"eNqVVQmSBCEI+xLoE1z+/6WFBGl0eqp2q2b6MhyBoDqmjLX85zeVGU+4iBk/LLMp82cs0fWz8OCrOmQORy5/ML85kLb5B8qXzBfUPTjO/FYmJgcyrQfgQIaVYyZXPbZ/X7Clk5kRPPRSGEeYMYGOZWa5aBc/cdgKLFwrYzOaViLxOjIyPQ0Ft5NZcB7mfnbJkFNli5jBZYCz+zDL9JLOTgzub0I97UwkCR00AJzJIh+kwknVe+BZmbMJkk6v3v2lGRFu8rNfSaJiuNVevMnATc9ZLqi2YtL2Cbjz1u7uMTu7X8ScADHBbVrRsnppAHzqIHTOb0S0dYgrNCBQgb9kiG1Xbr4k8C086mUVkbBoQ32rR9KrWJdmOABdEk1KkuJOcdyiPiR/ik5pkGNE+1utqdV/yfEtSnW+1Jr1DZGxdq3T2kdxntYfunr0u0VW+Vwi6wO4I30qsI0Jqy9tQvaA/jWnUzSfosyQVMuhgNVMPpR47lQvm2oUNn2vVN3erEhqbhlhyH3jggdmfe0n3PSeMWmjw77V7FxcX8h1/XOzspeRfGevD38kY8/MUt6vpVY7S32MHN7v3lwzmulHmXqpQ/3GHtSAHIinknOj8+DIQ8J4/PGwxNlYMb0d6I8Z14nmFrTzz9pM1MCv2Q/JauaB21ihWvYLNlDVsQ==","16c8a54a71145ea5a23c8a6e13d50eff834517e6fc4826394b7497bbaeb5e78f",1023,int("138370912573772422127818574647616"))]

import base64,zlib,hashlib
leaf_total=0;split_total=0
for pair,low,high,packed,tree_sha,expected_count,expected_margin in ROOTS:
    tree=zlib.decompress(base64.b64decode(packed)).decode('ascii')
    assert hashlib.sha256(tree.encode('ascii')).hexdigest()==tree_sha
    assert len(tree)==2*expected_count-1
    lo=tuple(F(x) for x in low);hi=tuple(F(x) for x in high)
    assert all(U[k-1]<lo[d]<hi[d]<U[k+1] for d,k in enumerate(I))
    assert hi[2]<lo[3] and hi[3]<Z
    cursor=[0];margins=[];splits=[0]
    def walk(lo,hi):
        j=cursor[0];assert j<len(tree)
        s=tree[j];cursor[0]+=1
        if s in LEAF:
            k=LEAF[s]
            bound=lower_base(lo,hi) if k is None else lower_shared(k,lo,hi)
            margin=bound.numerator//bound.denominator-Q
            assert margin>0,(pair,j,s,margin)
            margins.append(margin)
            return
        d=int(s);assert 0<=d<4 and lo[d]<hi[d]
        splits[0]+=1;mid=(lo[d]+hi[d])/2
        a=list(hi);a[d]=mid;b=list(lo);b[d]=mid
        walk(lo,tuple(a));walk(tuple(b),hi)
    walk(lo,hi)
    assert cursor[0]==len(tree) and len(margins)==expected_count
    assert splits[0]+1==expected_count and min(margins)==expected_margin
    leaf_total+=len(margins);split_total+=splits[0]
    print('C268_EXACT_ROOT_PASS',pair,'leaves',len(margins),'min_floor_margin',min(margins),flush=True)
assert leaf_total==6890 and split_total==6887
print('C268_AUTHOR_EXACT_PASS',leaf_total,'strict_leaves',split_total,'splits','global_min_floor_margin',min(r[-1] for r in ROOTS))
