#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
using i64=std::int64_t;
using u64=std::uint64_t;
using u128=__uint128_t;
static std::string dec(u128 n) { if(n==0) return "0"; std::string s; while(n){s.push_back(char('0'+n%10));n/=10;}std::reverse(s.begin(),s.end());return s; }
static i64 floor_div(i64 z,i64 d) { i64 q=z/d; if(z%d<0) --q; return q; }
static i64 bit_one_prefix(i64 z,int j) {
    i64 h=i64(1)<<j, per=2*h, q=floor_div(z,per), r=z-q*per;
    return q*h+std::max<i64>(0,r-h);
}
static i64 clamp(i64 z,i64 low,i64 high){return std::min(high,std::max(low,z));}
// Count [0,z): high bit h equals hb and lower bit l of t+shift equals lb.
static i64 high_low_prefix(i64 z,int h,int l,int hb,int lb,i64 shift){
    i64 H=i64(1)<<h, per=2*H, q=z/per, r=z%per;
    i64 len=clamp(r-i64(hb)*H,0,H);
    i64 ones=bit_one_prefix(shift+len,l)-bit_one_prefix(shift,l);
    return q*(H/2)+(lb?ones:len-ones);
}
static i64 same_index_prefix(i64 z,int i,int hb,int lb,i64 A){
    i64 H=i64(1)<<i, per=2*H, rA=A%per;
    auto tail=[&](i64 limit)->i64{
        i64 L=i64(hb)*H,R=L+H, total=0;
        for(int m=0;m<=1;m++) {
            i64 X=i64(lb)*H-rA+i64(m)*per;
            i64 Y=X+H;
            total+=std::max<i64>(0,std::min({R,Y,limit})-std::max(L,X));
        }
        return total;
    };
    return (z/per)*tail(per)+tail(z%per);
}
static i64 kernel(int p,i64 A,int i,int j,int eps,int eta){
    i64 N=i64(1)<<p, L=N-A;
    int bi=(eps<0),bj=(eta<0);
    if(i>j) return high_low_prefix(L,i,j,bi,bj,A);
    if(i<j) return high_low_prefix(N,j,i,bj,bi,-A)-high_low_prefix(A,j,i,bj,bi,-A);
    return same_index_prefix(L,i,bi,bj,A);
}
static i64 zero_start_mass(int p,int b){
    i64 n=i64(1)<<p, weight=0;
    for(int d=1;d<p;d++) { int minus=(((i64(1)<<d)-1)%b==0); int plus=(((i64(1)<<d)+1)%b==0); weight+=(p-d)*(minus+plus); }
    return (n/2)*weight;
}
struct Totals{u128 all=0, highpos=0, highnonpos=0, low=0, same=0, zero=0; u64 identities=0;};
static Totals exact(int p,int a,int b){
    i64 n=i64(1)<<p; Totals t;
    t.zero=zero_start_mass(p,b);
    for(i64 A=a;A<n;A+=a) {
        for(int i=0;i<p;i++)for(int j=0;j<p;j++)for(int eps:{-1,1})for(int eta:{-1,1}){
            i64 D=A+i64(eta)*(i64(1)<<j)-i64(eps)*(i64(1)<<i);
            if(D%b!=0)continue;
            i64 c=kernel(p,A,i,j,eps,eta);
            if(c==0)continue;
            t.all+=u64(c); ++t.identities;
            if(i>j && D>0)t.highpos+=u64(c);
            else if(i>j)t.highnonpos+=u64(c);
            else if(i<j)t.low+=u64(c);
            else t.same+=u64(c);
        }
    }
    return t;
}
static u128 brute(int p,int a,int b) {
    int N=1<<p; u128 t=0;
    for(int x=0;x<N;x++)for(int y=x;y<N;y++) {
        if(x%a!=y%a)continue;
        for(int i=0;i<p;i++)for(int j=0;j<p;j++) {
            if(x==y && j<=i)continue;
            if(((x^(1<<i))%b)==((y^(1<<j))%b))t++;
        }
    }
    return t;
}
int main(){
    u64 kc=0;
    for(int p=2;p<=7;p++){
        i64 N=i64(1)<<p;
        for(i64 A=1;A<N;A++)for(int i=0;i<p;i++)for(int j=0;j<p;j++)for(int eps:{-1,1})for(int eta:{-1,1}){
            i64 actual=0;
            for(i64 x=0;x<N-A;x++){
                int b1=(x>>i)&1,b2=((x+A)>>j)&1;
                actual+=(b1==(eps<0) && b2==(eta<0));
            }
            if(kernel(p,A,i,j,eps,eta)!=actual){std::cerr<<"KERNEL ERROR\n";return 1;}
            ++kc;
        }
    }
    u64 bc=0;
    for(int p=2;p<=6;p++)for(int a=3;a<(1<<p)&&a<=11;a+=2)for(int b=3;b<(1<<p)&&b<=11;b+=2){
        auto e=exact(p,a,b); auto v=e.all+e.zero;
        if(brute(p,a,b)!=v){std::cerr<<"TOTAL ERROR: "<<p<<","<<a<<","<<b<<"\n";return 1;}
        ++bc;
    }
    auto v=exact(32,321651,440665);
    std::cout<<"{\n  \"schema\": \"PREFIX918_EXACT_COMPLETE_NAMED_TWO_FLIP_MASS_V1\",\n";
    std::cout<<"  \"kernel_exhaustive_cases\": "<<kc<<",\n  \"whole_model_small_cases\": "<<bc<<",\n";
    std::cout<<"  \"p\": 32, \"a\": 321651, \"b\": 440665,\n";
    std::cout<<"  \"positive_start_gap_parameter_families\": "<<v.identities<<",\n";
    std::cout<<"  \"high_source_first_positive_terminal_gap\": "<<dec(v.highpos)<<",\n";
    std::cout<<"  \"high_source_first_zero_or_negative_terminal_gap\": "<<dec(v.highnonpos)<<",\n";
    std::cout<<"  \"low_source_first_all_terminal_gaps\": "<<dec(v.low)<<",\n";
    std::cout<<"  \"same_source_index_all_terminal_gaps\": "<<dec(v.same)<<",\n";
    std::cout<<"  \"same_start_different_source_bits\": "<<dec(v.zero)<<",\n";
    std::cout<<"  \"positive_start_gap_total\": "<<dec(v.all)<<",\n";
    std::cout<<"  \"all_distinct_unordered_named_two_flip_collisions\": "<<dec(v.all+v.zero)<<"\n}\n";
}
