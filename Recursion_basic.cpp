#include<iostream>
using namespace std;
void prnt(int x,int n){
    if(x>n){
        return ;
    }
    cout<<x<<endl;
    prnt(x+1,n);
}

int main(){
    int x,n;
    cin>>x>>n;
    prnt(x,n);
    return 0;
}
