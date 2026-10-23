#!/usr/bin/env python3
"""C266 compact standalone exact 3-root / 2034-leaf proof replay.

No third-party imports. The five preorder trees are fixed certificate data, not
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


import base64,zlib
LEAF={'B':None,'A':5,'C':50,'D':55,'E':56}
ROOTS=[{"pair":[4,16],"lo":["2/271","7/10","60/77","4/5"],"hi":["6/409","42/59","11/14","9/11"],"count":581,"margin":"5158902987695659637439900477932651","tree":"c-n1Ki4DXs2wMrr20`q<(%C#ouc~xPc^zVNYO>TKEF@x?D?a!g1IdkKrWh7?HpuF9APNU34Mph+*-?hFpWP}r!q`($9t~2hZ=l8*I3rLtjlrp<=hi}IVy2E9AwCnFg>UG~6n6xim2s<U<G6XLRzMC>HM!JG_Za|P?!3jDR&eH$949W19B0#Hco>gGZrwA@2NK7K3-Dr&gKB+@_mD8R?1DbDtkLug#}cG7g`S;1KT$lpNB1R#;aZ{*GpnH9x}4Um{4lJC(^59B!Jc7VOdpg=7dCZ?G?Yz_&nu>qfpnz}pw&yX+Bmdbk-^O<w&{XrF7b{VPA^vj#b1kj_Ahs@mLTPNZ`&m2)s!h-oBdw6EXjrIo!F~(MIZZiLoyrCt&e?cGWF2eqDvO`Q9xjGRNpKMx~+KqyZtW6ev00jU)kr)>rdLNYTtOo?Xk<DbgZvQMz;6?dvyz$"},{"pair":[16,22],"lo":["1/119","12/17","18/23","13/16"],"hi":["3/205","42/59","21/26","9/11"],"count":698,"margin":"536512712981048045481613993763132","tree":"c-n1Lfsq6u2x|#q2M+z$^pXIpH$QW?t|9>v*yS)RH`t0;9uanSfjHY-!q5L0kY+n}&-1jOXBt;-0(4Cr!qCQBM68vU-P*@Mn=#a49A~Jq^Q7<|AHk<*`b7*n4S9#fO#E}6_!)`mJPRs;dGKQBhbsQC<AP*{tX-QlAU;z?w$BU|LmZ3V0Ah26VpXCm+D(DAWdg!|mMhcbD0P&hZjdP1I>&kWOv!Lli!l(a712?NQw3Pvu&eNIgV_L|M0_aG=Lk?e1m)W*?pwG^AD%m(l;()x#o=`DgG;fjoJxUpWnuA~$NDFebcnkLM<e=QMQ74abynl^&{AY{V-J_65mbVmK`8jG+8|Y9USe>d?P)h|D0Gdjj`AdGDQS-*oCU#)D~KXChc!Po>@Zu&fvaQGM*6s1lFTQ;3bEe|dq%ajjlpa3tNE;pmJ~H}qB_=_MW#1EG4xcrOKsMl6+&o40!|W(7Zx+D&tP}Up~vN(F|`;;-#KV|BlaH-aX?c"},{"pair":[13,28],"lo":["1/123","34/49","18/23","4/5"],"hi":["2/137","7/10","59/74","9/11"],"count":755,"margin":"3046191377545063607211587604835111","tree":"c-mc5ixI^j2wO>DgP!ca(n|tpU+;Q~l}`wu+X_q1412KJvmx-X@vU%Mnb;C4kb;`9kO3E5Q6UWq3ybyd-YuYaj2+k59jk8T>A1Jnk?)F2v*3@QuAE3-PSC`xAapU3ghi2_a9Ro^-|bVT(q0wKU=jPl2fuq`U$Hg><Kjw2QBFF_bdtyr1u4zOV;x<98bYDq)%FT!8)&e_a*$3Axjjth0e~t7AmF-48m=!0Rp3MX9Q*<<gjR*?Q`_a3D?k4jOg$8~>l`*z5BINQobtvcso;DXr}Rs`Rr8NvRecZ~qt!&JxKqVE2NX~kn*R&zP2mahrLP;gVXzBWhsaPPFwR0#ux|MhQVOGX>^@Y)Qxs5%OHlxLd-`w$`H*i@{4%OR35BgNd;6)`^w)c0ne;ux=~dpm4PQo#Bh(Ve!!f}8I5K0#>`BaqbEKcFLE$BwP3L53Xb`%x+8EA4O?`Wq8G%pN^z9lRiLqV><DSG|#V;eYSsrWW<53x}JA&0~2SCmF{%a_knyFhDZsuf^3leD%4wl5DO4P4~*PFqbiIGM`e5;4vi>iG%EQ^P!-VDyW)wy-szTNJM%qw+*I{#AA4-D4*16q_^dj"}]
grandleaf=0;grandsplit=0;allmargin=[]
for r in ROOTS:
    pair=tuple(r['pair']);lo=tuple(F(x) for x in r['lo']);hi=tuple(F(x) for x in r['hi'])
    assert all(U[k-1]<lo[d]<hi[d]<U[k+1] for d,k in enumerate(I))
    assert hi[2]<lo[3] and hi[3]<Z
    tree=zlib.decompress(base64.b85decode(r['tree'].encode())).decode('ascii')
    cursor=[0];margins=[];splits=[0]
    def walk(a,b):
        j=cursor[0];assert j<len(tree)
        sym=tree[j];cursor[0]+=1
        if sym in LEAF:
            k=LEAF[sym]
            lb=lower_base(a,b) if k is None else lower_shared(k,a,b)
            margin=lb.numerator//lb.denominator-Q
            assert margin>0,(pair,j,sym,margin)
            margins.append(margin)
            return
        d=int(sym);assert 0<=d<4 and a[d]<b[d]
        splits[0]+=1;mid=(a[d]+b[d])/2
        lh=list(b);lh[d]=mid;rl=list(a);rl[d]=mid
        walk(a,tuple(lh));walk(tuple(rl),b)
    walk(lo,hi)
    assert cursor[0]==len(tree) and len(margins)==r['count']
    assert splits[0]+1==len(margins) and min(margins)==int(r['margin'])
    print('C266_REMOTE_STANDALONE_ROOT_PASS',pair,len(margins),min(margins))
    grandleaf+=len(margins);grandsplit+=splits[0];allmargin+=margins
assert grandleaf==2034 and grandsplit==2031
assert min(allmargin)==536512712981048045481613993763132
print('C266_REMOTE_STANDALONE_EXACT_PASS',grandleaf,grandsplit,'eight-new-pairs')
