#include <bits/stdc++.h>
using namespace std;
struct Row { int a,b,t,T,i,j,I,J; bool operator<(const Row& x)const{return tie(a,b,t,T,i,j,I,J)<tie(x.a,x.b,x.t,x.T,x.i,x.j,x.I,x.J);} };
int main(int argc,char**argv){
    int p=argc>1?atoi(argv[1]):19;
    int k=argc>2?atoi(argv[2]):21;
    if (p!=19 || k!=21) { cerr << "independent checker is scoped to Q19 and k=21\n"; return 2; }
    int H=1<<(p-1),L=H+1,U=2*H-1;
    vector<vector<Row>> named(7); long long seen_left=0;
    for(int a=L;a<=U;a+=2){
        unordered_map<int,vector<pair<int,int>>> right;
        right.reserve(p*p*2);
        int sourceB=(k+2)*a,sourceA=k*a;
        for(int I=0;I<p;I++)for(int J=0;J<p;J++){
            int y=(sourceB^(1<<J))-(1<<I);
            if(y>0)right[y].emplace_back(I,J);
        }
        for(int i=0;i<p;i++)for(int j=0;j<p;j++){
            int x=(sourceA^(1<<j))-(1<<i);
            if(x<=0)continue;
            int low=max(1,(x+U-1)/U), high=min(2*k,x/L);
            for(int t=low;t<=high;t++){
                if(x%t)continue;
                int b=x/t;
                if(b<L||b>U||!(b&1)||b==a)continue;
                seen_left++;
                for(int m=0;m<=6;m++){
                    auto it=right.find((t+m)*b);
                    if(it==right.end())continue;
                    for(const auto [I,J]:it->second)named[m].push_back({a,b,t,t+m,i,j,I,J});
                }
            }
        }
    }
    for(int m=0;m<=6;m++){
        sort(named[m].begin(),named[m].end());
        string fn="PREFIX971_RAW_Q"+to_string(p)+"_K"+to_string(k)+"_M"+to_string(m)+".csv";
        ofstream file(fn);
        set<pair<int,int>> pairs;
        for(auto r:named[m]){
            pairs.insert({r.a,r.b});
            file<<r.a<<","<<r.b<<","<<r.t<<","<<r.T<<","<<r.i<<","<<r.j<<","<<r.I<<","<<r.J<<"\n";
        }
        cerr<<"m="<<m<<" named="<<named[m].size()<<" pairs="<<pairs.size()<<"\n";
    }
    cerr<<"seen_left="<<seen_left<<"\n";
    return 0;
}
