#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>
using i64=std::int64_t;
using u64=std::uint64_t;
using u128=__uint128_t;
static std::string dec(u128 n){if(n==0)return "0";std::string s;while(n){s.push_back(char('0'+n%10));n/=10;}std::reverse(s.begin(),s.end());return s;}
static i64 floor_div(i64 z,i64 d){i64 q=z/d;if(z%d<0)--q;return q;}
static i64 bit_one_prefix(i64 z,int j){i64 h=i64(1)<<j,per=2*h,q=floor_div(z,per),r=z-q*per;return q*h+std::max<i64>(0,r-h);}
static i64 clamp(i64 z,i64 low,i64 high){return std::min(high,std::max(low,z));}
static i64 high_low_prefix(i64 z,int h,int l,int hb,int lb,i64 shift){
    i64 H=i64(1)<<h,per=2*H,q=z/per,r=z%per;
    i64 len=clamp(r-i64(hb)*H,0,H);
    i64 ones=bit_one_prefix(shift+len,l)-bit_one_prefix(shift,l);
    return q*(H/2)+(lb?ones:len-ones);
}
static i64 same_index_prefix(i64 z,int i,int hb,int lb,i64 A){
    i64 H=i64(1)<<i,per=2*H,rA=A%per;
    auto tail=[&](i64 limit)->i64{
        i64 L=i64(hb)*H,R=L+H,total=0;
        for(int m=0;m<=1;m++){
            i64 X=i64(lb)*H-rA+i64(m)*per,Y=X+H;
            total+=std::max<i64>(0,std::min({R,Y,limit})-std::max(L,X));
        }
        return total;
    };
    return (z/per)*tail(per)+tail(z%per);
}
static i64 kernel(int p,i64 A,int i,int j,int eps,int eta){
    i64 N=i64(1)<<p,L=N-A;
    int bi=(eps<0),bj=(eta<0);
    if(i>j)return high_low_prefix(L,i,j,bi,bj,A);
    if(i<j)return high_low_prefix(N,j,i,bj,bi,-A)-high_low_prefix(A,j,i,bj,bi,-A);
    return same_index_prefix(L,i,bi,bj,A);
}
static u128 zero_start(int p,int b){
    i64 n=i64(1)<<p,w=0;
    for(int d=1;d<p;d++){
        i64 h=i64(1)<<d;
        w+=(p-d)*((h-1)%b==0);
        w+=(p-d)*((h+1)%b==0);
    }
    return u128(n/2)*w;
}
struct Result{u128 highpos=0,highnonpos=0,low=0,same=0,samestart=0,mixed=0,zerozero=0;int identities=0,mixedfibers=0;};
static Result exact(int p,int a,int b){
    Result out;
    i64 N=i64(1)<<p;
    out.samestart=zero_start(p,b);
    for(i64 A=a;A<N;A+=a){
        i64 L=N-A;
        for(int i=0;i<p;i++){
            i64 h=i64(1)<<i,r=A%(2*h),tau=std::min(r,2*h-r);
            if((A+h)%b==0){out.mixed+=u64(L-tau);out.mixedfibers+=(L>tau);}
            if((A-h)%b==0){out.mixed+=u64(L+tau);out.mixedfibers++;}
            for(int j=0;j<p;j++)for(int eps:{-1,1})for(int eta:{-1,1}){
                i64 D=A+i64(eta)*(i64(1)<<j)-i64(eps)*h;
                if(D%b!=0)continue;
                i64 count=kernel(p,A,i,j,eps,eta);
                if(count==0)continue;
                out.identities++;
                if(i>j && D>0)out.highpos+=u64(count);
                else if(i>j)out.highnonpos+=u64(count);
                else if(i<j)out.low+=u64(count);
                else out.same+=u64(count);
            }
        }
    }
    i64 l=std::lcm(i64(a),i64(b)),q=(N-1)/l;
    out.zerozero=u128(q)*N-u128(l)*q*(q+1)/2;
    return out;
}
static void print(int p,int a,int b){
    Result v=exact(p,a,b);
    u128 tw=v.highpos+v.highnonpos+v.low+v.same+v.samestart;
    std::cout<<"{\n  \"schema\": \"PREFIX925_INDEPENDENT_K_SWEEP_V1\",\n";
    std::cout<<"  \"p\": "<<p<<", \"a\": "<<a<<", \"b\": "<<b<<",\n";
    std::cout<<"  \"zero_zero\": "<<dec(v.zerozero)<<",\n";
    std::cout<<"  \"zero_flip\": "<<dec(v.mixed)<<", \"zero_flip_fibers\": "<<v.mixedfibers<<",\n";
    std::cout<<"  \"flip_flip_highpos\": "<<dec(v.highpos)<<",\n";
    std::cout<<"  \"flip_flip_highnonpos\": "<<dec(v.highnonpos)<<",\n";
    std::cout<<"  \"flip_flip_low\": "<<dec(v.low)<<",\n";
    std::cout<<"  \"flip_flip_same\": "<<dec(v.same)<<",\n";
    std::cout<<"  \"flip_flip_same_start\": "<<dec(v.samestart)<<",\n";
    std::cout<<"  \"positive_flip_flip_fibers\": "<<v.identities<<",\n";
    std::cout<<"  \"flip_flip_total\": "<<dec(tw)<<",\n";
    std::cout<<"  \"all_named_collision_pairs\": "<<dec(tw+v.mixed+v.zerozero)<<"\n}\n";
}
int main(){print(32,464773,304985);}
