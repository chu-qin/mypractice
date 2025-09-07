#include <stdio.h>
int main() {
    int a;
    printf("Hello, World!\n");
    scanf("%d", &a);
    printf("You input: a=%d\n", a);
    for (int i = 0; i < a; i++) {
        printf("i=%d\n", i);
    }
    return 0;
}