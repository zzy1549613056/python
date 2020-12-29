//
//  main.c
//  test1
//
//  Created by 朱正阳 on 2017/9/4.
//  Copyright © 2017年 朱正阳. All rights reserved.
//

#include <stdio.h>

void insertSort(int a[],int n) {
    int i,j;
    for(i=1;i<n;i++){
        j=i-1;
        int temp=a[i];
        while(j>=0&&temp<a[j]){
            a[j+1]=a[j];
            j--;
        }
        a[j+1]=temp;
    }
}
//直接插入排序

void shellSort(int a[],int n){
    int i,j,temp;
    int d=n/2;
    while(d>=1){
        for(i=d;i<n;i++){
            j=i-d;
            temp=a[i];
            while(j>=0&&a[j]>temp){
                a[j+d]=a[j];
                j-=d;
            }
            a[j+d]=temp;
        }
        d/=2;
    }
}
//希尔排序


void bubbleSort(int a[],int n){
    int i,j,temp;
    for(i=0;i<n;i++){
        for(j=0;j<n-i;j++){
            if(a[j]>a[j+1]){
                temp=a[j+1];
                a[j+1]=a[j];
                a[j]=temp;
            }
        }
    }
}
//冒泡排序

void selectSort(int a[],int n){
    int i,j,min;
    for(i=0;i<n;i++){
        min=i;
        for(j=i;j<n-1;j++){
            if(a[j+1]<a[min])
                min=j+1;
        }
        if(min!=i){
            int temp=a[min];
            a[min]=a[i];
            a[i]=temp;
        }
        
    }
}
//简单选择排序

int partition(int a[],int low,int high){
    int base=a[low];
    while(low<high){
        while(a[high]>=base&&low<high) high--;
        int temp=a[high];
        a[high]=a[low];
        a[low]=temp;
        while(a[low]<=base&&low<high) low++;
        temp=a[low];
        a[low]=a[high];
        a[high]=temp;
    }
    return high;
}

void quickSort(int a[],int low,int high){
    if(low<high){
        int mid=partition(a,low,high);
        quickSort(a,low,mid-1);
        quickSort(a,mid+1,high);
    }
}
//快速排序

//int  main(){
//    int array[9]={2,4,1,23,43,45,23,45,33};
//    int n=9;
//    quickSort(array,0,n-1);
//    for(int i=0;i<n;i++)
//        printf ("%d ",array[i]);
//    printf ("\n");
//    return 1;
//}
