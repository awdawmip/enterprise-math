// PREFIX-867 exact finite checker: complete p-bit old-residue-zero fiber.
#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

int half_period(int q) {
    int a=2%q;
    for(int d=1;d<=q;++d) {
        if(a==1 || a==q-1) return d;
        a=(2*a)%q;
    }
    return -1;
}

int main(int argc,char** argv) {
    if(argc!=3) {cerr<<"usage: checker p b\n"; return 2;}
    const int p=stoi(argv[1]),b=stoi(argv[2]);
    if(!((p==19&&b==12)||(p==21&&b==13)||
         (p==23&&b==14)||(p==25&&b==15))) {
        cerr<<"This audited certificate covers p=19,21,23,25 only.\n";
        return 2;
    }
    const int N=1<<p, M=(1<<b)-1;
    const long long T=1LL*N*(p+1);
    vector<int> good;
    for(int q=3;q<=M;q+=2) if(half_period(q)>=p) good.push_back(q);

    vector<int> stamp(M+1,0);
    int epoch=0,first_count=0;
    long long eligible=0, survivors=0;
    for(int q1:good) {
        int m=(N+q1-1)/q1;
        if(1LL*q1*M<T || 1LL*m*(p+1)>M) continue;
        vector<int> valid_q2;
        for(int q2:good) {
            if(1LL*q1*q2<T || q2<m*(p+1)) continue;
            if(1LL*q1*q2/gcd(q1,q2)<N) continue;
            valid_q2.push_back(q2);
        }
        if(valid_q2.empty())continue;
        ++first_count;
        eligible+=valid_q2.size();

        vector<int> fiber;
        fiber.reserve(m*(p+1));
        for(int u=0;u<N;u+=q1) {
            fiber.push_back(u);
            for(int i=0;i<p;++i)fiber.push_back(u^(1<<i));
        }
        for(int q2:valid_q2) {
            ++epoch;
            bool injective=true;
            for(int v:fiber) {
                const int r=v%q2;
                if(stamp[r]==epoch) {injective=false;break;}
                stamp[r]=epoch;
            }
            if(injective)++survivors;
        }
    }

    const int expected_safe=(p==19?1957:p==21?3976:p==23?8046:16188);
    const int expected_first=(p==19?755:p==21?1273:p==23?2035:3064);
    const long long expected_pairs=(p==19?322946:p==21?892960:p==23?2234291:4933967);
    const bool pass=int(good.size())==expected_safe
           && first_count==expected_first
           && eligible==expected_pairs && survivors==0;
    cout<<"{\"schema\":\"PREFIX867_EXACT_ZERO_FIBER_V1\",\"p\":"<<p
        <<",\"excluded_width\":"<<b
        <<",\"ordered_candidate_pairs\":"<<1LL*((M-1)/2)*((M-1)/2)
        <<",\"safe_odd_moduli\":"<<good.size()
        <<",\"eligible_first_moduli\":"<<first_count
        <<",\"eligible_pairs\":"<<eligible
        <<",\"surviving_pairs\":"<<survivors
        <<",\"status\":\""<<(pass?"ALL_EXACT_ASSERTIONS_PASSED":"ASSERTIONS_FAILED")
        <<"\"}\n";
    return pass?0:1;
}
