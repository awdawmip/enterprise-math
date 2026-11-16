// g++ -O2 -std=c++17 order_certificate.cpp -lgmpxx -lgmp -o order_certificate
#include <gmpxx.h>
#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <vector>
using Q=mpq_class;
using Z=mpz_class;

Q frac(const Z& n, const Z& d) { Q x(n,d); x.canonicalize(); return x; }
Z rising(int n,int k) { Z z=1; for(int j=0;j<k;j++) z*=n+j; return z; }
struct Interval { int w; Q lo,hi,width,score; };
int main(int argc,char**argv) {
    const int end=argc>=2?std::atoi(argv[1]):200;
    const int cutoff=argc>=3?std::atoi(argv[2]):2501;
    const int start=argc>=4?std::atoi(argv[3]):2;
    if(start<2||end<start||cutoff<end) return 2;
    std::vector<Q> a(end+1), y(end+1);
    a[2]=1;y[2]=1;
    Q a_at_cut=1;
    for(int j=3;j<=cutoff;j++){
        a_at_cut*=frac(4*j+5,4*(j+5));
        if(j<=end) { a[j]=a_at_cut; y[j]=y[j-1]*frac(4*j+1,4*(j+1)); }
    }
    const Z C=rising(cutoff+6,15);
    long long tested=0,left_width_ge_right=0,pending=0;
    for(int v=start;v<=end;v++) {
        const Q outrho=frac(4*v+5,v+5)*a_at_cut/a[v];
        const Q P=frac((v+4)*C,28*(4*v+4)*rising(v+5,15));
        const Q D=P/outrho;
        const Z V=rising(v+4,9);
        Q r=frac(4*v+3,v+3);
        std::vector<Interval> words;
        for(int w=v;w>=2;--w) {
            Q tau=r*frac(28*(4*w+2)*rising(w+3,9),(w+2)*V);
            Q x=frac(840,rising(w+2,3)),lo,hi;
            const int coeff_a[3]={3,48,192},coeff_b[3]={15,60,96};
            for(int j=0;j<3;j++) {
                Q tail=y[w]*(x*coeff_a[j]+coeff_b[j])/(32+x*y[w]*coeff_a[j]);
                Q z=(r+tau*tail)/(1+tau*tail);
                if(!j||z<lo)lo=z;
                if(!j||hi<z)hi=z;
            }
            Q width=hi-lo;
            Q score=width/((P+lo)*(D+hi));
            words.push_back({w,lo,hi,width,score});
            if(w>2)r*=frac(4*(w-1)+3,4*(w-1+3));
        }
        // sigma is a triple of strict ranks; use small integers for triple comparisons.
        std::vector<int> idx(words.size()),lowrank(words.size()),hirank(words.size()),wrank(words.size()),srank(words.size());
        std::iota(idx.begin(),idx.end(),0);
        auto rank=[&](Q Interval::*key,std::vector<int>& out) {
           std::sort(idx.begin(),idx.end(),[&](int i,int j){return words[i].*key<words[j].*key;});
           int k=0; for(size_t i=0;i<idx.size();i++){
             if(i && words[idx[i]].*key != words[idx[i-1]].*key) ++k;
             out[idx[i]]=k;
           }
        };
        rank(&Interval::lo,lowrank);rank(&Interval::hi,hirank);
        rank(&Interval::width,wrank);rank(&Interval::score,srank);
        for(size_t j=0;j<idx.size();j++) for(size_t i=0;i<j;i++){
           ++tested;int x=i,z=j;if(lowrank[x]>lowrank[z])std::swap(x,z);
           if(lowrank[x]==lowrank[z] && hirank[x]==hirank[z]) {std::cerr<<"same intervals\n";return 3;}
           if(lowrank[x]==lowrank[z] || hirank[x]>=hirank[z])continue;
           if(wrank[x]>=wrank[z]) {++left_width_ge_right;continue;}
           if(srank[x]>=srank[z]){
               ++pending;std::cerr<<"cross "<<v<<' '<<words[x].w<<' '<<words[z].w<<"\n";
           }
        }
    }
    std::cout<<"start "<<start<<" end "<<end<<" cutoff "<<cutoff<<" pairs "<<tested
             <<" left_width_ge_right "<<left_width_ge_right<<" pending "<<pending<<"\n";
}
