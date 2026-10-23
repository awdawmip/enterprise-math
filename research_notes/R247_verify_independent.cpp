// R247 independent exact one-axis lift of six-axis deterministic positive BRC.
// Other five spatial axes remain identity; all path weights/multiplicities are 1.
#include <boost/multiprecision/cpp_int.hpp>
#include <boost/rational.hpp>
#include <array>
#include <cassert>
#include <deque>
#include <iostream>
#include <map>
#include <string>
#include <utility>
#include <vector>
using Q=boost::rational<boost::multiprecision::cpp_int>;
using Vec=std::vector<Q>;
using Map=std::map<int,Vec>;
struct A {int m,b;};
int bit(int s,int k){return (s>>k)&1;}
int g3(int s){return s ^ (8*(bit(s,2)^bit(s,1)));}
int g2(int s){return s ^ (8*bit(s,0));}
A edge(int s,int g,bool masked){
    if(s==2 || s==4) return {0,0};
    if(g==0 && s==12) return {-1,0};
    if(g==1 && (s==10||s==12) && !masked) return {1,1};
    return {1,0};
}
int next(int s,int g){return g==0?g3(s):g2(s);}
int pair_id(int s){return s==2?0:(s==10?1:-1);}
Vec advance(const Vec& v,int g,bool masked){
    Vec out(10,Q(0));
    for(int i=0;i<2;++i){
        int s=i==0?2:10, t=i==0?4:12;
        int ni=pair_id(next(s,g));
        assert(ni>=0 && next(t,g)==(ni==0?4:12));
        A u=edge(s,g,masked), w=edge(t,g,masked);
        int j=5*i,k=5*ni;
        out[k]  += Q(u.m)*v[j];
        out[k+1]+= Q(u.m)*v[j+1]+Q(u.b)*v[j+4];
        out[k+2]+= Q(w.m)*v[j+2];
        out[k+3]+= Q(w.m)*v[j+3]+Q(w.b)*v[j+4];
        out[k+4]+=v[j+4];
    }
    return out;
}
bool zero_output(const Vec& v){
    Q a(0),b(0),c(0),d(0);
    for(int j=0;j<10;j+=5){a+=v[j];b+=v[j+1];c+=v[j+2];d+=v[j+3];}
    return a==c&&b==d;
}
bool insert(Vec v,Map& B){
    for(const auto& kv:B){int pivot=kv.first; const Vec& row=kv.second;
        if(v[pivot]!=Q(0)){Q scale=v[pivot];for(int j=pivot;j<10;++j)v[j]-=scale*row[j];}
    }
    int pivot=-1; for(int j=0;j<10;++j)if(v[j]!=Q(0)){pivot=j;break;}
    if(pivot<0)return false;
    Q scale=v[pivot];for(Q& x:v)x/=scale;B.emplace(pivot,v);return true;
}
struct Answer{bool equivalent;std::string witness;int rank;int max_word_len;};
Answer solve(bool masked){
    Vec v(10,Q(0));v[0]=v[2]=v[4]=Q(1);
    Map basis; assert(insert(v,basis));
    std::deque<std::pair<Vec,std::string>> pending;pending.push_back({v,""});
    int maxlen=0;
    while(!pending.empty()){
        auto [x,word]=pending.front();pending.pop_front();
        assert(zero_output(x));
        maxlen=std::max(maxlen,(int)word.size());
        for(int g=0;g<2;++g){Vec y=advance(x,g,masked);std::string z=word+(g==0?'3':'2');
            if(!zero_output(y))return {false,z,(int)basis.size(),maxlen};
            if(insert(y,basis))pending.push_back({y,z});
        }
    }
    return {true,"",(int)basis.size(),maxlen};
}
int main(){
    assert(g3(2)==10&&g3(4)==12&&g3(10)==2&&g3(12)==4);
    assert(g2(2)==2&&g2(4)==4&&g2(10)==10&&g2(12)==12);
    Answer d=solve(false),m=solve(true);
    assert(!d.equivalent && d.witness=="323");
    assert(m.equivalent && m.rank==3 && m.max_word_len==1);
    std::cout<<"R247_CPP_EXACT_PASS delayed_witness="<<d.witness
             <<" delayed_prior_rank="<<d.rank<<" masked_invariant_rank="<<m.rank
             <<" reachable_control_pairs=2 ambient_dimension=10\n";
}
