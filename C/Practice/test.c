#include <stdio.h>
int main() {
    int a;
    printf("Please write a number.\n");
    scanf("%d", &a);
    printf("You input: a=%d\n", a);
    for (int i = 0; i < a; i++) {
        printf("i=%d\n", i);
    }
    printf("a github test\n");
    return 0;
}