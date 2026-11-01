// D25 GH-124/125: direct full F_(3347^2) character and first-moment checks.
// Portable author evidence; not a native Enterprise Math / canonical checkpoint.
// For f_B(x)=x^3+x^2+B*x, evaluate trace=-sum chi(f) and
// S(B)=sum_{f != 0} chi(f)*x/f, using exact F_p[r]/(r^2-2).
#include <cassert>
#include <cstdint>
#include <iostream>
#include <utility>
#include <vector>
using namespace std;
using ll=long long;
constexpr int P=3347;
static int mod(ll a){int z=int(a%P);return z<0?z+P:z;}
struct F {int a,b;};
static F add(F x,F y){return {mod(x.a+y.a),mod(x.b+y.b)};}
static F sub(F x,F y){return {mod(x.a-y.a),mod(x.b-y.b)};}
static F mul(F x,F y){return {mod(1LL*x.a*y.a+2LL*x.b*y.b),mod(1LL*x.a*y.b+1LL*x.b*y.a)};}
static bool equal(F x,F y){return x.a==y.a&&x.b==y.b;}
static F scale(F x,int n){return {mod(1LL*x.a*n),mod(1LL*x.b*n)};}
struct Result {ll trace;F moment;ll nonzero;};
static Result direct(F B,const vector<int>&chi,const vector<int>&inv,const vector<int>&sq,const vector<int>&cube){
    ll count=0,nonzero=0,sum_a=0,sum_b=0;
    for(int a=0;a<P;a++) for(int b=0;b<P;b++) {
        int a2=sq[a],a3=cube[a],b2=sq[b],b3=cube[b];
        int v0=mod(a3+6LL*a*b2+a2+2LL*b2+1LL*B.a*a+2LL*B.b*b);
        int v1=mod(3LL*a2*b+2LL*b3+2LL*a*b+1LL*B.a*b+1LL*B.b*a);
        int n=mod(1LL*v0*v0-2LL*v1*v1);
        int s=chi[n];count+=s;
        if(!s)continue;
        nonzero++;
        int w=mod(1LL*s*inv[n]);
        sum_a+=mod((1LL*a*v0-2LL*b*v1)*w);
        sum_b+=mod((1LL*b*v0-1LL*a*v1)*w);
    }
    return {-count,{mod(sum_a),mod(sum_b)},nonzero};
}
int main(){
    vector<int> chi(P),inv(P),sq(P),cube(P);
    inv[1]=1;
    for(int x=2;x<P;x++)inv[x]=mod(-1LL*(P/x)*inv[P%x]);
    for(int x=0;x<P;x++){sq[x]=mod(1LL*x*x);cube[x]=mod(1LL*x*sq[x]);}
    for(int x=1;x<P;x++){
        int y=x,e=(P-1)/2,z=1;
        while(e){if(e&1)z=mod(1LL*z*y);y=mod(1LL*y*y);e>>=1;}
        chi[x]=z==1?1:-1;
    }
    const F T[3]={{0,2232},{1916,2172},{458,813}};
    const F Z[3]={{9,0},{3207,479},{2251,2893}};
    const F expected_H[3]={{783,0},{841,1147},{49,1370}};
    const F expected_J[3]={{0,1424},{3032,1282},{1689,2223}};
    const F expected_moment[3]={{0,362},{2954,765},{390,679}};
    const F expected_defect[3]={{0,0},{915,1909},{800,620}};
    const int inv8=inv[8];
    for(int k=0;k<3;k++) {
        F B=scale(add(T[k],{1,0}),inv8);
        Result res=direct(B,chi,inv,sq,cube);
        F right={0,0};
        F Hp={expected_H[k].a,mod(-expected_H[k].b)}; // H(T)^p = conjugation
        right=scale(mul(expected_J[k],Hp),16);
        F trace_mod={mod(res.trace),0};
        F hasse_norm=mul(expected_H[k],Hp);
        F defect=sub(res.moment,scale(mul(mul(Z[k],T[k]),trace_mod),2));
        cout<<"origin "<<k<<" B=("<<B.a<<","<<B.b<<")"
            <<" trace="<<res.trace<<" trace_mod="<<trace_mod.a
            <<" H_norm=("<<hasse_norm.a<<","<<hasse_norm.b<<")"
            <<" weighted_S=("<<res.moment.a<<","<<res.moment.b<<")"
            <<" predicted_S=("<<right.a<<","<<right.b<<")"
            <<" defect=("<<defect.a<<","<<defect.b<<")"
            <<" nonzero="<<res.nonzero<<"\n";
        assert(equal(res.moment,right));
        assert(equal(res.moment,expected_moment[k]));
        assert(equal(defect,expected_defect[k]));
        assert(equal(trace_mod,hasse_norm));
        assert(res.nonzero>0);
        if(k==0){assert(res.trace==-6106);assert(res.nonzero==11202406);}
        else assert(res.trace==-6106); // same F_(p^2)-isomorphism class
    }
    cout<<"PASS_GH124_GH125_MARKED_CHARACTER_TRACE_AND_FIRST_JET_3_ORIGINS"<<"\n";
}
