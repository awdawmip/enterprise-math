// AUTHOR-SIDE RESEARCH EXPERIMENT. NOT NATIVE H0/B0, NOT A SOURCE RESULT.
// Exact exhaustive prime-bound experiment for the ORIGINAL weighted 216 sum.
// Compile: g++ -O2 -std=c++17 -Wall -Wextra -pedantic ... -o ...
// Run with a positive bound <= 50000; p^4 must fit signed 64-bit here.
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <stdexcept>
#include <vector>
using u64 = std::uint64_t;
using u128 = unsigned __int128;
using i128 = __int128;

static u64 mul(u64 x, u64 y, u64 mod) { return static_cast<u64>((u128)x*y % mod); }
static u64 inv_mod(u64 a, u64 m) {
    i128 b = m, x = 1, y = 0, old = a;
    while (b != 0) {
        i128 q = old / b;
        i128 tmp = old-q*b; old=b; b=tmp;
        tmp=x-q*y; x=y; y=tmp;
    }
    if (old != 1) throw std::runtime_error("non-unit denominator");
    x %= static_cast<i128>(m);
    if (x < 0) x+=m;
    return static_cast<u64>(x);
}
static std::vector<int> prime_list(int bound) {
    std::vector<bool> prime(bound,true);
    if (bound>0) prime[0]=false;
    if (bound>1) prime[1]=false;
    for (int q=2;q*q<bound;q++) if(prime[q])
        for(int k=q*q;k<bound;k+=q) prime[k]=false;
    std::vector<int> out;
    for(int q=5;q<bound;q++) if(prime[q])out.push_back(q);
    return out;
}
struct Digit {u64 w4, h2, corr4;};
static Digit compute(int pp) {
    u64 p=pp, mod=p*p*p*p;
    std::vector<u64> fact(p,1), ifact(p,1);
    for (u64 k=1;k<p;k++) fact[k]=mul(fact[k-1],k,mod);
    ifact[p-1]=inv_mod(fact[p-1],mod);
    for(u64 k=p-1;k>0;k--) ifact[k-1]=mul(ifact[k],k,mod);
    u64 pow36=1, inv36=inv_mod(36,mod), num=1, w=0;
    for(u64 k=0;k<p;k++) {
        u64 unit=mul(ifact[k],ifact[k],mod);
        unit=mul(unit,ifact[k],mod);
        u64 term=mul(mul(num,unit,mod),pow36,mod);
        w=(w + mul(6*k+1,term,mod))%mod;
        num=mul(mul(mul(num,2*k+1,mod),3*k+1,mod),3*k+2,mod);
        pow36=mul(pow36,inv36,mod);
    }
    u64 h=0;
    {
       std::vector<u64> inv(p,0); inv[1]=1;
       for(u64 k=2;k<=p/3;k++) inv[k]=p-(p/k)*inv[p%k]%p;
       for(u64 k=1;k<=p/3;k++)h=(h+mul(inv[k],inv[k],p))%p;
    }
    u64 expected = p%3==1 ? p : (mod-p);
    if(w % (p*p*p) != expected % (p*p*p))
       throw std::runtime_error("ORIGINAL_p3_FAILED_p="+std::to_string(p));
    u64 actual=(w+mod-expected)%mod; // known divisible by p^3
    if(actual%(p*p*p)!=0)
       throw std::runtime_error("THIRD_DIGIT_DIVISIBILITY_FAILED_p="+std::to_string(p));
    u64 corr=(actual/(p*p*p))%p;
    u64 sign_coefficient=(p%3==1)?(p-5):5;
    u64 predicted=mul(sign_coefficient, mul(inv_mod(6,p),h,p),p);
    if(corr!=predicted)
       throw std::runtime_error("HARMONIC_p4_FAILED_p="+std::to_string(p));
    return Digit{w,h,corr};
}
int main(int argc,char **argv) {
   if(argc!=2){std::cerr<<"provide upper bound (exclusive)\n";return 2;}
   int bound=std::atoi(argv[1]);
   if(bound<8||bound>50000){std::cerr<<"bound must be 8..50000\n";return 2;}
   try {
       auto primes=prime_list(bound);
       int target13=0,target19=0, other_one=0, other_two=0;
       for(int pp:primes){
           Digit d=compute(pp);
           if(pp%24==13)target13++;
           else if(pp%24==19)target19++;
           if(pp%3==1)other_one++;else other_two++;
           if(pp==13||pp==19||pp==373||pp==49999) {
             std::cout<<"fixture p="<<pp<<" Wmodp4="<<d.w4
               <<" H2modp="<<d.h2<<" p4_digit="<<d.corr4<<"\n";
           }
       }
       std::cout<<"PASS_AUTHOR_SIDE_EXACT_BOUNDED_ORIGINAL216 p_min=5 p_exclusive="<<bound
         <<" total_primes="<<primes.size()<<" target_13="<<target13
         <<" target_19="<<target19<<" one_mod3="<<other_one<<" two_mod3="<<other_two
         <<" verified_original_p3_all="<<primes.size()
         <<" verified_harmonic_p4_all="<<primes.size()<<"\n";
   } catch(const std::exception& e){std::cerr<<"FAIL "<<e.what()<<"\n";return 1;}
}
