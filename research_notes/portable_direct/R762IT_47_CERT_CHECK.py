#!/usr/bin/env python3
"""R762IT exact replay of 152 47-event Port-Euler witness certificates.
Payload: for each matching, a 2-byte inactive-Port mask and 20 base-4
triple-edge allocations. Decompression transports data only, not proof logic.
"""
from itertools import combinations
import base64, zlib, hashlib

CERT_B85 = """c-lpmJ#O7P5QV83QJ?@8B0&Kvc>xtExr7T>Dc_QeAPdNn-*+g-X#!_LkA`Q?4->-LQ|m34J(m>Y$Ys>LgroPKQto54p89LV)7`?FV(ESKk-L>Xw&EkN;o$dD=WOO|;m_=z=#XMdXUc;Qq;bW|{Rjs~t>=_E8?EMEN9|!r9O=1j&S&{%xre{QYR#CeUl$YhvD3GHhBfl(rVf0J?&=$sBPC;AyK13V&gmXC*wR|zYdvQxt>lxDJ*-Pf7L5*Pw;nmW4G)P9u_sTXwrJ`0lCy_nr9*3{T~}+(_TA2Ngw9#MmmBwNz4)tn&f%?Uj5)b;nfUS!4vPs%`jywPRBQm=$jdtMwVS^uD{;Ki7``M`dv~tiK<PEO$hI8ME?zcHzGj0T##s7u_GX3_yZNgy!}9)DWmC*x%<v&369|^gh4Yy6{t9ceNY%Uw{xM<&r)4eCboO>D>_lsIJJ`H-VATQLhTD~g^%ctKtm|&kv-n`|uWIBJL-5<f{bt9J`pxwP$l&Vt^&9S3Or`dry`^)MbKlozn_Xv{B{l>xUhBH14lMJmF+*kf*P0epldG>;uNBP3`d$-Pj)3i{gD-1!{~@07nLEuHKp9B=XE<PvHh&KORqWf~#Ik4woPE((jB38IEAGZ<m9wCOR6r-Ew20#3j%G;D45_dDUQ8o73MfFs4|xRort<Lj;W{(?H)nv8Vq-6}TE`#M0t``S0g3Ldj&Z<hs57fp3ODBXIM#&`CaZH{v|5v@#}Y;MY?{(++dzHvLwcj1eeGh{t)J-2-?I5c$A?(b->Pb|A#L(!gi-Hx5u?l@T@qVrx<-Dd#gKe=q0TPg892P(D-3VRo2rd}qltgoq9t~RbSCs!)s;U%QjI-T7-hOK9X>mnZw+1eDD$k44Ctkpl>s^6P!m(pW@KLL_DWl|xi{eu3g}FKs4fEnxy?uTP+yCH?KEOOhVyW1Z}5w+VKslhb_ri51Hc$3l1#RIOm$Cm;JQ5>mRnWr0t_uiztv&6rZ%J7`HIa9Kc&M5=$MohQ5I^UPj&y*zpB!4(hSj^ZGUN#8KgpP!8Y&rGP%C@zZ;U?ey688cQKKapRIA?V6V<Crm~>-_M<P7Z_>PUXnr$t{+XVtV~=zIT#kEk>B7<rgSGUa4pomYR@-DXCTXv8{5M$w4q~6?9<-`|;IDmgQk$0}ZZ!mmexNjrg^k3)b+&y8bUS*C46h`>T`uJix>^OMs&~t~@?s4H&Ot*?6(v`WGly^o<jL;w)ZEUjBs&7kA^7I}?ZO<W<{qq<1+R@)eo{_J_6}qn=9T(|HdQTDKSM7D-BaQ$8qY)3u=EDR;GM|;<xV_bIS7SCZpz(o%e+51#10Wb(+oD^t{mC|zZ{W0iLp0xDSze=2D9)n+jEPzki(4tr=?Z7=auA+Y;Wcet5^%Eh1(~&@RLJAQeNwu*=3J&E$ghpci)QTa?4XQjw;l-wsOe7b4b+&1Glr3)6Q!9Ne-!6T5RIZm@dcr;XSJ*PS+Ui1#gr?WZn8WPHKQ41G;_%Wc*caX-~6S4ROb1x->bIzjFw)pJ&;lDY@ia*mUXZWUjZqPv=4{?|;=2cQmdU?!aZ&=}wx=E~Vc7J0K_aQDzREa`$aN^-w@YrOj-~lk3}9iGYr{B4<&4c}?%rG7AqO6Ys$6-qOq=B5#F!GlvMx>3u&$h*kdfV75=E{Rt=28fP_?OXzsM(ww2peC7os#rl1NV}Cl}laU#=Cx=Q&hdPix(Fuz_a|l&Yjrv;K<k&NZG(&+Z`QiFk4m}&1zS*lB9H0CX@T;}W>U<#$;)NXI%B#()^|Oub$sw$mhsAt3;KFr0IV2o-Udahi{y62oFt1^Ba??Crt?E@F-o+)#@9TV>WVum)Q$?}8SM9A_-fra(ae-CFnM30{hoo2@MLk#euGi|!p)O@%vdSUwRUnZ=r5iJ-gIujj;N%ch9*^uIKQDtPhaf*j*Jci#-#OG{new_TOckEEav)}!!VF#5<PJ@SR$S;%Ov;)LsC4>3mdwz^bujyzLzpiCr6gAMZw|o+9;NimB#S!C9D39pQ*}5&mOMH1s5>e}tP&wl4n3Y~Gl%>;huFOI2CTfpzEb)Z8=DVUGC|t(F<*G)OPe!?@^=owNBvjeQ5Mf~CE0HbS*lfjkYlVT&K!adkA~O<hMEE1f3TqW41aVHeV2}ZCh?ap^L@s}E{<=>c~U5#Fij~ysJlbTht)HO#&-@8g)k-QJI38ky|({g1SbAQ<<OX$KmC7EmhCz"""
EXPECTED_SHA256 = "30d13b776c596bc90a78fb62294c6dff070d3b48ff5edba2dbb2daceb809be5a"
P = list(combinations(range(6), 2))
T = list(combinations(range(6), 3))
port_id = {p:i for i,p in enumerate(P)}
E = [[tuple(sorted((port_id[u], port_id[v]))) for u,v in combinations(list(combinations(s, 2)), 2)] for s in T]
MATCHINGS = [m for k in range(4) for m in combinations(range(15), k)
             if len({axis for v in m for axis in P[v]}) == 2*k]
assert len(MATCHINGS) == 76
raw = zlib.decompress(base64.b85decode(CERT_B85))
assert len(raw) == 2*76*22 and hashlib.sha256(raw).hexdigest() == EXPECTED_SHA256
checked = 0
for rep_index, (family,j) in enumerate(((967489, 0), (971528, 3))):
    assert family.bit_count() == 9 and (family>>j)&1
    for idx, matching in enumerate(MATCHINGS):
        offset = (rep_index*76+idx)*22
        inactive = int.from_bytes(raw[offset:offset+2], 'little')
        assert inactive == sum(1<<v for v in matching)
        counts = [3 if (family>>s)&1 else 2 for s in range(20)]
        counts[j] = 1
        deg = [0]*15
        graph = [set() for _ in range(15)]
        for s in range(20):
            code=raw[offset+2+s]
            n = ((code&3), ((code>>2)&3), ((code>>4)&3))
            assert sum(n) == counts[s], (rep_index,idx,s,n,counts[s])
            for q,(u,v) in zip(n,E[s]):
                if q:
                    assert not (inactive>>u)&1 and not (inactive>>v)&1
                    deg[u] += q; deg[v] += q
                    graph[u].add(v); graph[v].add(u)
        active = {v for v in range(15) if not inactive>>v&1}
        assert all(deg[v]>0 and deg[v]%2==0 for v in active)
        assert all(deg[v]==0 for v in range(15) if v not in active)
        seen={min(active)}; todo=list(seen)
        for v in todo:
            for w in graph[v]:
                if w not in seen:seen.add(w);todo.append(w)
        assert seen==active, (rep_index,idx,active-seen)
        assert sum(counts)==47
        checked += 1
assert checked == 152
print('PASS R762IT, 152 exact 47-event certificates; payload SHA256', EXPECTED_SHA256)
