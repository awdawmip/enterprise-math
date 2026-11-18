// R749SUO exact certificate: 2<=M<=N, N default 10000.
// Build: g++ -O3 -std=c++17 R749SUO_SIGN_DIVISOR_CERT.cpp -o suo && ./suo
#include <algorithm>
#include <cassert>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <set>
#include <stdexcept>
#include <vector>
using namespace std;
using ll=long long;
struct Winner {int a,u,v,d,q;};
struct Bucket {ll score=-1; vector<Winner> winners;};
int invmod(int a,int m) {
    int b=m,x=1,y=0;
    while(b){int k=a/b; a-=k*b;swap(a,b);x-=k*y;swap(x,y);}
    if(a!=1)throw runtime_error("noninvertible");
    x%=m; return x<0?x+m:x;
}
void update(Bucket &b, Winner w){
    ll s=1LL*w.u*w.a*w.d; // oriented u>=v
    if(s>b.score){b.score=s;b.winners.clear();}
    if(s==b.score)b.winners.push_back(w);
}
struct Check {ll score;set<int> qs;int oriented_ties;};
Check brute(int M){
    ll p=-1;set<int> qs;int ties=0;
    for(int a=1;a<=M;a++)for(int d=1;d<=M;d++){
        int prod=a*d-1;
        if(prod<=0)continue;
        for(int u=1;u<=M;u++){
            if(prod%u)continue;
            int v=prod/u; if(v<1||v>M)continue;
            int q=u+v-a-d; if(q==0)continue;
            ll t=1LL*max(u,v)*a*d;
            if(t>p){p=t;qs.clear();ties=0;}
            if(t==p){qs.insert(q);if(u>=v)ties++;}
        }
    }
    return {p,qs,ties};
}
void printvec(const vector<int>& v){
    cout<<"[";
    for(size_t i=0;i<v.size();i++)cout<<(i?",":"")<<v[i];
    cout<<"]";
}
int main(int argc,char** argv){
    int N=argc>1?atoi(argv[1]):10000;
    if(N<120||N>10000)throw runtime_error("range 120..10000");
    vector<Bucket> buckets(N+1);
    ll count=0;
    for(int u=1;u<=N;u++)for(int a=1;a<=N;a++){
        if(gcd(u,a)!=1)continue;
        ll dmax=min((ll)N,((ll)N*u+1)/a);
        if(u==1){
            for(int d=1;d<=dmax;d++){
                int v=a*d-1;if(v<1||v>u)continue;
                int q=u+v-a-d;if(q==0)continue;
                update(buckets[max({a,u,d})],{a,u,v,d,q});count++;
            }
            continue;
        }
        int d=invmod(a,u);
        int lower=(u+a)/a;
        if(d<lower)d+=((lower-d+u-1)/u)*u;
        for(;d<=dmax;d+=u){
            int v=(1LL*a*d-1)/u;
            if(v<1||v>u)continue;
            int q=u+v-a-d;
            if(q==0)continue;
            if(1LL*(u-a)*(u-d)!=1LL*u*q+1)
                throw runtime_error("determinant identity error");
            update(buckets[max({a,u,d})],{a,u,v,d,q});count++;
        }
    }
    vector<int> near_div(N+2,0);
    for(int x=2;x*x<=N+1;x++)
        for(int n=x*x;n<=N+1;n+=x)near_div[n]=x;
    ll full_peak=-1, plus_peak=-1;
    vector<Winner> full_winners;
    int plus_labeled_ties=0;
    int checked_sieve=0, checked_brute=0, mixed=0;
    vector<int> negative, Q2, mixed_M;
    for(int M=2;M<=N;M++){
        Bucket &b=buckets[M];
        if(b.score>full_peak){full_peak=b.score;full_winners=b.winners;}
        else if(b.score==full_peak){full_winners.insert(full_winners.end(),b.winners.begin(),b.winners.end());}
        set<int> qset;
        for(auto &w:full_winners)qset.insert(w.q);
        if(qset.count(-1))negative.push_back(M);
        if(qset.count(2))Q2.push_back(M);
        if(qset.size()>1){mixed++;mixed_M.push_back(M);}
        if(M<=120){
            auto ref=brute(M);
            if(ref.score!=full_peak||ref.qs!=qset||ref.oriented_ties!=(int)full_winners.size())
                throw runtime_error("brute comparison failed for M="+to_string(M));
            checked_brute++;
        }
        int n=M+1,x=near_div[n];
        if(x>=2){
            int y=n/x,v=n-x-y;
            if(v>=1){
                ll score=1LL*(n-1)*(n-x-1)*(n-y-1);
                int lbl=(x==y?2:4);
                if(score>plus_peak){plus_peak=score;plus_labeled_ties=lbl;}
                else if(score==plus_peak)plus_labeled_ties+=lbl;
            }
        }
        if(M>=116){
            if(qset!=set<int>{1}||full_peak!=plus_peak||2*(int)full_winners.size()!=plus_labeled_ties)
                throw runtime_error("sieve/complete optimizer disagreement M="+to_string(M));
            checked_sieve++;
        }
    }
    vector<int> expected_negative={2,3,4,5,6,7,9,10,13,16,21,22,33,37,46,61,86,115};
    if(negative!=expected_negative||Q2!=vector<int>{58,93}||mixed_M!=vector<int>{5,6,7,9})
        throw runtime_error("unexpected finite sign spectrum");
    cout<<"{\n  \"record\":\"R749SUO\",\n  \"status\":\"PASS\",\n";
    cout<<"  \"finite_M_domain\":\"2.."<<N<<"\",\n";
    cout<<"  \"oriented_noncanonical_candidates\":"<<count<<",\n";
    cout<<"  \"negative_optimal_Q_M\":";printvec(negative);cout<<",\n";
    cout<<"  \"positive_and_negative_tied_M\":";printvec(mixed_M);cout<<",\n";
    cout<<"  \"Q_equals_2_optimal_M\":";printvec(Q2);cout<<",\n";
    cout<<"  \"independent_direct_brute_checked_M\":"<<checked_brute<<",\n";
    cout<<"  \"independent_divisor_sieve_checked_M\":"<<checked_sieve<<",\n";
    cout<<"  \"sieve_checked_scores_and_labeled_maximizer_counts\":true,\n";
    cout<<"  \"infinite_extension\":\"analytic S_C+2 and negative-defect lower bound for M>=9999\",\n";
    cout<<"  \"scientific_scope\":\"auxiliary_labeled_two_port_WBRC_feedback_only\"\n}\n";
}
