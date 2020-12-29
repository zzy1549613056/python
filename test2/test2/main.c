//
//  sort2.c
//  test1
//
//  Created by 朱正阳 on 2017/9/4.
//  Copyright © 2017年 朱正阳. All rights reserved.
//

#include <stdio.h>

void shellsort(int a[],int n){
    int i,j,temp;
    int d=n/2;
    while(d>=1){
        for(i=d;i<n;i++){
            j=i-d;
            temp=a[i];
            while(j>=0&&temp<a[j]){
                a[j+d]=a[j];
                j-=d;
            }
            a[j+d]=temp;
        }
        d/=2;
    }
}

int main(){
    int a[10]={2,34,12,32,76,15,23,32,34,67};
    shellsort(a,10);
    for(int i=0;i<10;i++)
        printf("%d ",a[i]);
    return 1;
}
