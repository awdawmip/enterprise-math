#include <bits/stdc++.h>
using namespace std;
struct Act{int k;vector<int> supp;};
vector<Act> acts; int n,f,base,powb[12];vector<int> memo;long long calls=0, explored=0, skipped=0;

inline int value(int packed){
    ++calls;
    int& v=memo[packed]; if(v>=0)return v;
    int e[12],live=0;int t=packed;
    for(int i=0;i<n;i++){e[i]=t%base;t/=base;if(e[i]<=f)live|=(1<<i);}
    if(__builtin_popcount((unsigned)live)<=1)return v=0;
    int best=1000000000;explored++;
    for(auto &a:acts){
        bool no_progress=false;
        for(int s:a.supp)if((s&live)==live){no_progress=true;break;}
        if(no_progress){++skipped;continue;}
        int mx=0;
        for(int s:a.supp){
            int np=packed;
            for(int i=0;i<n;i++)if(!(s&(1<<i))&&e[i]<f+1)np+=powb[i];
            int cv=value(np);
            if(cv>mx)mx=cv;
            if(a.k+mx>=best)break;
        }
        if(a.k+mx<best)best=a.k+mx;
    }
    if(best==1000000000){cerr<<"NO GOOD ACTION "<<packed<<"\n";exit(2);}
    return v=best;
}
int main(int argc,char**argv){
    if(argc>1)f=atoi(argv[1]);else f=8;
    cin>>n; if(n!=7){cerr<<"expected seven named hypotheses\n";return 3;}
    base=f+2;powb[0]=1;
    for(int i=1;i<=n;i++)powb[i]=powb[i-1]*base;
    int count;cin>>count;
    for(int i=0;i<count;i++){
        Act a;int z;cin>>a.k>>z;
        for(int j=0;j<z;j++){int s;cin>>s;a.supp.push_back(s);}
        acts.push_back(a);
    }
    memo.assign(powb[n],-1);
    auto ts=chrono::steady_clock::now();int result=value(0);
    cout<<"RESULT "<<result<<" n="<<n<<" f="<<f<<" explored="<<explored
        <<" calls="<<calls<<" skipped="<<skipped
        <<" time="<<chrono::duration<double>(chrono::steady_clock::now()-ts).count()<<"s\n";
    for(auto &a:acts){
        if(any_of(a.supp.begin(),a.supp.end(),[&](int s){return s==((1<<n)-1);})){
            cout<<"ROOT "<<a.k<<" no_progress\n";continue;
        }
        int mx=0;vector<int> bs;
        for(int s:a.supp){
            int np=0;
            for(int i=0;i<n;i++)if(!(s&(1<<i)))np+=powb[i];
            int x=value(np);bs.push_back(x);mx=max(mx,x);
        }
        cout<<"ROOT "<<a.k<<" bound="<<a.k+mx<<" branches=";
        for(auto x:bs)cout<<x<<",";
        cout<<"\n";
    }
}
