// PREFIX274 independent finite integer ordered-pair BRC cross-check.
// Candidate Stage46 Grover coin: d*C_ji = 2-d*[i==j].
// This is NOT original Stage46 source import or native physical evolution.
#include <cassert>
#include <iostream>
#include <map>
#include <vector>
#include <numeric>
using namespace std;

static long long binom(int n,int k){long long r=1;for(int j=1;j<=k;++j)r=r*(n-j+1)/j;return r;}
static vector<long long> signature(int d,const vector<int>& s){
    vector<long long> result;
    for(int j=0;j<d;++j){
        long long pair_mass=0, amplitude=0;
        for(int i=0;i<d;++i){
            long long ci=2-d*(i==j);
            amplitude+=ci*s[i];
            for(int k=0;k<d;++k){
                long long ck=2-d*(k==j);
                pair_mass+=ci*ck*s[i]*s[k]; // labelled signed ordered pairs
            }
        }
        assert(pair_mass==amplitude*amplitude);
        result.push_back(pair_mass); // exactly d^3 times normalized port intensity
    }
    long long sum=accumulate(result.begin(),result.end(),0LL);
    assert(sum==1LL*d*d*d);
    return result;
}
static vector<int> flip_first(vector<int> s){s[0]=-s[0];return s;}
int main(){
 for(int d=1;d<=12;++d){
    map<vector<long long>,int> one;
    map<pair<vector<long long>,vector<long long>>,int> two;
    for(int bits=0;bits<(1<<(d-1));++bits){
        vector<int> s(d,1);
        for(int j=1;j<d;++j)s[j]=((bits>>(j-1))&1)?-1:1;
        auto p=signature(d,s),q=signature(d,flip_first(s));
        ++one[p];++two[{p,q}];
    }
    int orbit_count=1<<(d-1);
    int predicted=orbit_count-(d%2==0?binom(d,d/2)/2:0);
    auto homogeneous=vector<long long>(d,1LL*d*d); // d^3*(1/d)
    int special=1+(d%2==0?binom(d,d/2)/2:0);
    assert((int)one.size()==predicted);
    assert(one[homogeneous]==special);
    assert((int)two.size()==(d==2?1:orbit_count));
    cout<<"d="<<d<<" orbits="<<orbit_count<<" one="<<one.size()<<" fiber="<<special<<" two="<<two.size()<<" PASS\n";
 }
 cout<<"INDEPENDENT_CPP_SIGNED_ORDERED_PAIR_BRC_PASS\n";
}
