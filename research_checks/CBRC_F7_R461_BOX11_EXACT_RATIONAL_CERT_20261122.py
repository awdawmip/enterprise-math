#!/usr/bin/env python3
"""CBRC F7 exact B=11 rational witness, Python standard library only.
Each certificate triple encodes (abs(x), y+128, increment). For nonaxis,
non-marked coordinates q=(20+increment)/40; absent triples use increment=0.
Original author's frozen model and Result are unchanged. This is not a
native review/admission.
"""
import base64
import hashlib
import zlib
from itertools import product

BOX=11
DEN=40
N=1924
CERT_SHA256="65ec618247976ac8e7624323e052ae5cf51619a10b673b4b58f652635ad82070"
CERT_B85="c-jrkWmlx>fq-Eiw^z#Di=rr;rfFKnlk9%llgwn=n-<)mfWqbAQjR;c_sk@jP4*A&e80|pSEO;p1gyxI6;rTc8duEFidk#LJg-<F6^p83iB>GDiWOVMDz8`*73-p6L$BCU72Bv{hga<4iY%+h!HT@BDB_9|1ZfB+Fqp(3gTWL6(+tcYFsp$%1?B}<(7~brOA4%Tuxf%eD_A$ch5<Hpu%*DZ33eFRRUj)sPJz4v1qzA)lmHxOa00<e0W%m*F*r@(i~(m6oU_4s0T%>Z)ZvnV%N(vsxF+Gcf*TxeO1Q<~HikP8?lPEVFehQ2!UBOs3oHXP3egxsX^6%dnm}k0p$tP)1WhY6qtL8Ca|+GtXhB0uI$Ac+iiuV&XpNwC3);}orh&F>Xj?}+3hfG%RVXJ>o}z+=N)nF(Jce+Z;R%K(5za_Fh48cm&k#Io;yH}x4ZMKxq605MyllfOF1)7W4HIuNye08A!#g_OML3Iap5g++MS)8YmpR^pWCW2>Nz#Ih12SQdNklS$Oi?mT$c#>AIhj*r9+L%)ENWy)kYxv1(a5Sv)+}V*ARB~iTF90n+cvTz$gUz;MskGYF)2_|l%#}78Ie6mM=%`)bd1t*Nhbl#5IQC4G@>&GouzaR(|JV~EOg0Emo>T~>8e535M5Vv!=RgtZs~NJ&>cc|CCw_D12hk40n;L*B}&Vb{;}A{Y#6f<!bSlb11!zhIA)WCWhk4%Y?`nc%4PwZ)7ZRZ3zRJ?wxqLV!B%v(s<SnNty|cJ!8Rq^0&H8c9maMA%PN-RERR@$vLaw5#>$ZGaXt+B2;ifHk3pX1e1h<d<kJS9)%YCc^O7$hzNq+;<jab$D88!mH7j2ye8b?IoNp<<qw`(Jvy$f&&m&&cc?t5e;CqPg6Mg{2AQVGH40ADp#i$ZvNTi_{XJP`0NhmT%Ole|9iCHG*n3$JhL5W38EK#v+5i3ryY7uKntXsu~E;bFZMa8xdyHaGa$O)0>qJTw_h!PZKA@-QqH{}qL!&r_Oa*W9|kmF2FN|^z23d?CBXPBHNa!!*AQZ7=t<dDlst|+-`lWUq>*W?C}o2J}Sa$A=>Qtl#|RWiq9UdjTJMIcL1mZ97ua$m>;C=Y=eglb5t5vWFi8q-u7sBx$!fSP0~gVmH!(^SoHH7nGdQuACbP_-!45>v~DTG7<1L#-KVovRI{Hig=<sco)yG_@;K4y!y<1w$3FDiKu%Y7eP>pbmsOq}m|WhJZFqwNa_1i8f)^GMY9;v}vx*Fm2Y*=7qMPv_(@}(zRu!tq5(EX=_ex-J)$sZOhQMb#2F~?Q$(kw7k#?Kr14xjI=$V?PKi#YKKBQ;(9;S2Y^0E^kJZn0DTndV^ANb`lP03s6NH?X`#<(`mE6Bgg&q73tV3m`V!ZdxxOOwRi&@#`ns-f82YBrx0JrE={pX6*P&-^dQR61R4+2Ug!MAj_mF-7^+QcR62<^DhOjZhj4@=SfiZ!NNp572F~y8&Y|JoYPB-S6v7j4^nz6);Wp1nhV^tVy+*sF*4c*wZ7~6)iql{g<k(EZyFp9t^VPj7j`_MQ*#vwM2kZ~-{eqjz^b6A)o&>SOX8kpnIoG{HvVrIBG#ms47&M0%1n{(Wp*USaYTtw!Q#axEw3N}}zxhBkY)7;R^O=WHw=C&|*baPiXvsN=_n0aLuuvwyJnV5Uj+(+ht%{;>9F}CzW%OJK4Q_Co^j3G;!TgHiHf>|almJG8@LCdtT%qq*Aw9M<41#Ve1Ela?%3@t0fvL-C+$g*KtHkoBhv+Nj_UEPv3Ejen*>y`qt6p5t_E&H0~09y`;<p@~*IG!MDAF%dg>xi(XfpuKBPH^j_ux6-r3R<V7bw*lerFBkP=b3duSQmwL30ar1bp=^hfpra7*QIqsSU070OIWuJ>yBpK)va0Gn$xU#%~~+6McrC*Sog4XpI8r|^$=Q*fb|$!Pq3{I*aom|2-}8%Z4}$as4b0c<J>mEZIi^7!L}*QHe=dmg>BBT%^S7_Zd-)5C2CtGwsmIPpten6+fue|W!p7vS>2Yi*z&rqAZ<lvD+ybf*bb5Hh}w>k?UdMifW24P`=EV**oTOH1l!ZPeO%Zln0=DlGtxe#?9-ZkM%ZV$eNMB_WBUTPFB1C_wl7orDzL9(`v$jfYW6K=-`4Cq(!Q(gS(iPh?0Kub!0kodUefGkZr_vk17tsh_9I|FhV~O=KLw5+;ONJWLGBpljuGk@C5|!dNGr!UaZE7Bq~XX&$F%O4;f`6;F((}J)Uf~@i_EbE9LvzLf*otjv4I_%*s-NKwxwgobnF60)^Ox>M_zXnOh=J9O4w0Wj(zGlB#vY1IKhrn<T!)QZs_dc&R*#3N6sPa9H!1Oi!+U!<H|X~os-O&F`ZL}bDBG6bmy#a&JpK4cP>EZqI51%=Q4J#0_Qq(ZV=}tac)WHHg)bu=dN^Sr88%7<~3(QI*SfxNjl5Yxo0@{x$}TJkCF2PI!~qZ47vKCYe=|;v1^35Mwx3&xYEisPF)k+HL1BW&^4u8)4FR$bImH(9C6J<*8+1bA=f%_ZDQ9JbZtx5j&kj4uAJt|Yp#OnDoR(0yY_@@AG!{p>yWrkpz9R7&amqoySur&2fF*9djPu!xqAq^N057zxW{yNTDiwH_XKlK>h6qiPwDPy>7J49S>c`&?s?%}fbK=&UPA6o=H8<2ZR+0P?p@{1GIvh7^SZmB+(qRsY3{Oe?@{-@av#{-hsb>--6zz2Cf(=IeE~ha(9_R71JE-lJVV4Y%sivYGe$gV<r!C=3Dc9&JyXIntvoZzGb=oE$TLqpi@>u6JsZ@sB|O{EvqL?*!jsiKdFm->o}$%LGCgJN*@K>a={ew@L+CkXo>S;K$DRx9?Zn<L?CnF|e(D{--a+ggLf&EE9Z}v<-8&|{Y27<+cqer4r0LB_@09RPbMFlH&YIpi=$%L21?t@d-Yw|emfjue-DTb^_vW}auXzi?TNK`s^p-X6p7QQf?}79lGVc-b9uw~g^qwQ{1@iSt-vIXwGT#vK4MX3E<{Ra{G0m5jzH#B3K)y-t%Lw0;;hPq|8R46SzB%TbC%$dw+rhqF=F3uFPWlRlugH8Q<tq!{p78Ah-+}NQV&5_Joe<w8_IDzG7xwose=qj;5r04S4>12A^baBbu<(ya|ER@3ru=E<ALsrF>7SJTjOL#b{%Pf(k^WiepJV=Q?%(15UFpv<e~$X|)L#((qUkSTe_8nVH2=QoKVbet?my!GW8^=f{xj;o5dKRX=!Ai88t4ImUJ>Y5fk7S^=7A9v7?puB5lEYX2^E+mfs6`FiNG`u%(B214eW@(E(~O4AV&jv9w_oa$qbauz@7~3i@*U29P+>s2^{0VDGQv#zy%Ckkzj`icH>|V3ije)9}o7E-~b2?ir|nfIIMyrGC0bEV_GoHgX3Cof(9o=Fk=R%U~n1-XIO9>1b1L?mjtssm{Y+#3l?~=NP{I2EbGBN5!}~<2YT?32aj0rm<CU9@DvBnQ1Ai;uTZFqg?dD&7l!(9s2_y}?4dyx8nTCmMQB8XMvc&z78*B06Ff9&3uSm{3WlaZXd8xhVJOQ(IUdTZP(g%BBvclmJu|egLI*f>2t!9abWB1gD0GTKXFPNPLYE|Tjl-{DxC4i~V7MEFdqlXGhWk*s-wY4n@SqVMlHp+$9+BZu86Feiv<#2)@PrngWZ?`7PpR-O4rgIFC&GCVE~s!(giAPFX5l>&-q*qhIDDwWM<RU8!Y3?zO2TI{d=A1FAbdq4Z(yX8M!NM#FN^fc$N-HD%E*w64C|2*Ei$S_(pqHP5}A;Z42ooVBnKmT5h;jBQIC{SWRFJnS>%934r$~FMvhtJghozb<eWw>VB``-u1WMYj&`DG7mIe&Xb+0^(r6!w_Veg~hz_dgkP#i0(GeLP<<T(}O<SYmEIPrXlOUP_(JYDPcr=fq1sN^kXi1NjadZzy_i^+<L=R>3NJWo%^n^!GS@aA=&q?%xM=veWYZ|>Fu?`mNM6oUz>%p;J9_uq>12Q(K$A&~~SjI+FY|M<MX>44@CU`7|VtEiNpjc7HN;FnRu{{*qN3jDMJEXBA8asxu6A?SL#?El;g2yg->`KP2LF_G!chGnjj(4+o50Ce<cpr@SllXuZAC&PS5+COA5fvXb;$tkH7V&W!&y#q8$BQ^#lJPQ&@A3FPjvuo45sn}0@e>|D<?%BXKd12v7Qck?D;d8Lm2YHaC#&q%DtlOEFRSd=D+hSxpsXBXmBV`FsH_}=m1$8~AeALtS=K7|S>*w)JY<zewDOo#p5V$;z4DA!o}<bOP<bgUuVv*8tb7L&?I7_|BwmBW8<^;ziB6X2;)!mW=mCjdl;~55evueZi9wMVQi)+bF(MPAFfqmwMVcs)L>VXcL}DK$4n*RJCXP|!ge6Wz;!GsYdEx>mE=l6blelJy8<u#>tJ*=;YgE-Ct2%L2m#pgHRlTsPPgeEIssUCtD5{3+RU@KmlvR~bRT)(6(W(Plb;zrZSk*D9Iw4hOvg({xUBIeKP<17$u5r~3s`{h+4pzN~$rmKqE|V`&@-<DqfyoY$>}1I<lI(`b9-8ds$v&LyXUPGa9CRdyNOBk@M|iS~lY2C|50eKXdB~DSBza7eCm?ysl4mG+E|M2Ad5M!(TJjnuZ&>mjs(t~g+hO%9QT;}%?f})DxVl@f?iJO2w7Oqa50L6Xt$LVN@AK+It@?;oA8XYor23pxU$E*+Tzv(quX*(itbWU?-=pdeAoZN2Ucgj4Oud4s*CO?Xr#fh=6Q{aJsvD$wP^y=u`c$f)rv_wdkfnxLY9FT#K<W^tj<nP<N}Z6@8BCp{)CEpmiqsWNU5nHWPrc=-cPRA%)x0D%uVBq<t)>Ilbi$f0UeiNrdPPm2s_Ex71GMIV)*R8AW3A?d)tri&Gf;DZYc4^}6{)#KH8-l}t*CiNYTo0TkGS?3t9_1YU-H^lwDvWveM4$Hcx@M|?FO|yu(ns#_VL<&TsuH&4`J;QsXeB(C!+S0)}Eo-b69(cYp+o4HLbnTYv0n^cdYh3sQrlR+Ev|4RQF2Ny`goTqOP0Q^~kzjS=UGE`c>Vrs5_x`r>gFZ)t!^NOI&va>TW>YTeI#Ru6wW5eSmeJX#G=C|BTc>hxIQ&eLJmxN$X$H`q#Yv4XW>e^<B8WTh;fd`d(4rC+d$${VA$H)9TMb{ROMPLiN|E{sz>)rS<P*{d-pbf!BWo4bNf23)#>P8eWQqSFqtVZs?#5U0Or8Z0OM%dSyc&Y&gLUXQbg=HC&*EE8Or-G`!~xA85lz(eN2GKEaJoW#co__#8IAz>V#o@ug^dg&SYv#tzijDI2>~W4G4W!y3<6<2h}-kd2q5@d`IyqsAN1_zpI{hm9XZ<44%|88$ruP0wJ{bJ5hUHN8SjZ(L0sps7<fb*ZLq(sVAGE^yN&Yq}Oq?`hKq*z{30eZoy&aPwo*{De0@rOnSl^9$VEPMTkm=GU<K4Q}ob&7F?sF4=rRnlEwlm2AES%{RRHEogoZn?LgAPqg_nX#NG<dV+5~!?#}WTd(D<4((PazjZ@zy#=>EkXs+&txx#YXLjos*z#DmJi#r`c*_gg(hgc)f|ggX<uz(~BU?H|%Oz;J0xj3L<%YDp1ugGr%LmZ%iMM<PEnnd6NAUJzc>4*s{gmB)E^fDj+pqZT*WmUWdHXHB{T|)^2ycJJxBrm8fZM-<)`z6^k!XF4Tc5zzr?B-oY<&S*+d=C~*!l{$z80<5r1c$ZeUDl{kk*f&^)qk%0$P88cOHT}kKmoh@Xix-=NY;4g4}s2@4QEMK7u=+;GHk{&L8Gic;`3R_A_XE2-+TzwkM$NDQ<fP+n&R=cGUI~w!Ot|??Bso)b@e2eIjjNP}{G#?Kg1uA-ek*-F-^#KF4=ofV=Jd?t6OoBe?q+-u(sK{SDsz2fFt&xc3m<dyMZrA@`o5d(XkW5B%OIbni2|_XXbj1>gG(-1`T(|1-G%h~Iz0?mr{<KfwDR!Tn#s{ePkdKfwn-;|CA%gGczmWBT9;c<>ZF_y`|-q7S~12fw1P{tmzT8GrSVef0=@^%#Hk6o2&@ef2N!^-tjIzq79&vacV3uOEZ2zo2h^BH#Qhzj;Ky`2~LSPw?%J=-Z#rw~xTLztV62LBIVM`tC>g-A~}VzvJ&7;_rTg-~AJQ_dEFhZ{YhM@%R4%-~SGN_#6D;C-lSb@P~iHKmC>c>3`9mf5d<O9sc>>@Gt)Z|MFMxm;ZqO`aksF{{jCGIbOn$"

def decode():
    buf=zlib.decompress(base64.b85decode(CERT_B85))
    assert len(buf)==3*N and hashlib.sha256(buf).hexdigest()==CERT_SHA256
    out={}
    for j in range(0,len(buf),3):
        a,shift,n=buf[j:j+3]
        b=shift-128
        key=(a,b)
        assert b!=0 and key not in ((2,1),(1,-1)) and 1<=n<=24 and key not in out
        out[key]=20+n
    assert len(out)==N
    return out

def check():
    table=decode()
    def q40(x,y):
        if x==0 and y==0:return 0
        if y==0:return DEN
        key=(abs(x),y)
        if key in ((2,1),(1,-1)):return 20
        return table.get(key,20)
    max_abs=0
    saturating=0
    checked=0
    for a,b,c,d in product(range(-BOX,BOX+1),repeat=4):
        k=a-2*b-c+2*d
        D40=q40(a+k,b+k)+q40(c-k,d-k)-q40(a,b)-q40(c,d)
        assert -20<=D40<=20, ((a,b,c,d),D40)
        checked+=1
        if abs(D40)>max_abs:
            max_abs=abs(D40)
            saturating=1
        elif abs(D40)==max_abs:
            saturating+=1
    assert checked==23**4==279841 and max_abs==20
    print("PASS B=11:",checked,"inputs;",N,"overrides; max |40D| =",max_abs,
          "saturations =",saturating,"certificate SHA256 =",CERT_SHA256)

if __name__=="__main__":check()
