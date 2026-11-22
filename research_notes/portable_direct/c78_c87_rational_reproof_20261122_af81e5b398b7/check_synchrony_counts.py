from fractions import Fraction as Q
from check_discrete_jets import F
import json

def rho(k,n,s): return 4*F(k,n)/F(k,s-1)

def qceil(x,den=10**6): return str(Q((x.numerator*den+x.denominator-1)//x.denominator,den))

def main():
    a=Q(4782969,31457280)
    assert a==2/(256*15*Q(2,3)**14)
    assert a*Q(5,4)*Q(50,9)<=Q(11,10)
    assert a*Q(5,4)*Q(5225,256)<=4
    assert 256*Q(2,3)**15<Q(15,16)**4
    assert 256*Q(1,2)**9<Q(15,16)**4
    assert Q(9405,512*16**2)<Q(1,10)
    assert Q(195,32*8**2)<Q(1,10)
    assert Q(2,9)*Q(4,3)*Q(50,9)==Q(400,243)
    assert Q(2,9)*Q(4,3)*Q(325,48)==Q(325,162)
    deltas=[Q(1,d) for d in (16,32,64,256,1024)]
    H=Q(0); harmonic={}
    for c in range(1,65):
        H+=Q(1,c);harmonic[c]=H
    trials=0;rows=[];max_out=Q(0);max_in=Q(0)
    for delta in deltas:
        partial_in=0
        for c in range(2,65):
            partial_in+=sum(abs(rho(3,c,w)-1)<=delta for w in range(2,c+1))
            if c<16:continue
            bad_v=[v for v in range(2,c+1) if abs(rho(5,c,v)-1)<=delta]
            count_out=sum(v-1 for v in bad_v)
            out_bound=(c-1)*(Q(11,10)*delta*c+1+Q(4,c))
            in_bound=Q(200,243)*delta*c*(c+1)+c+21+Q(325,162)*harmonic[c]
            tighter_in=Q(200,243)*delta*c*(c+1)+c+14+Q(325,162)*harmonic[c]
            assert count_out<=out_bound
            assert partial_in<=in_bound
            assert partial_in<=tighter_in
            # Check the intermediate containing interval bounds on actual bad points.
            for v in bad_v:
                u=Q(8*v+21,8*c+29)
                eps=Q(50,9)*delta+Q(5225,256*c*c)
                assert u>Q(2,3) and abs(256*u**15-1)<=eps
            for w in range(2,c+1):
                if abs(rho(3,c,w)-1)<=delta:
                    u=Q(8*w+11,8*c+19)
                    eps=Q(50,9)*delta+Q(325,48*c*c)
                    assert u>Q(1,2) and abs(256*u**9-1)<=eps
            max_out=max(max_out,Q(count_out)/out_bound)
            max_in=max(max_in,Q(partial_in)/in_bound)
            trials+=1
            if c in (16,32,64):
                rows.append({"c":c,"delta":str(delta),"N_out":count_out,"N_in":partial_in,
                             "out_bound_upper":qceil(out_bound,1000),
                             "in_bound_upper":qceil(in_bound,1000)})
    out={"status":"PASS","arithmetic":"fractions.Fraction",
         "c_range_inclusive":[16,64],"deltas":[str(x) for x in deltas],
         "full_inventory_parameter_cases":trials,
         "max_actual_to_bound_upper":{"out":qceil(max_out),"in":qceil(max_in)},
         "examples":rows,
         "scope":"Direct finite rho counts; universal proof checked separately in SYNCHRONY_COUNT_CHECK.md"}
    print(json.dumps(out,indent=2))
if __name__=="__main__":main()

