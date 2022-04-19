# Lucky challenge writeup
Lucky was a pwn challenge from the tamuctf 2022. It was a special challenge for me as it didn't involve trivial bugs like stack buffer overflows, format string bugs...etc. 
We were given a binary and its source code which is the following:
```c
#include <stdio.h>
#include <stdlib.h>

void welcome() {
    char buf[16];
    printf("Enter your name: ");
    fgets(buf, sizeof(buf), stdin);
    printf("\nWelcome, %s\nIf you're super lucky, you might get a flag! ", buf);
}

int seed() {
    char msg[] = "GLHF :D";
    printf("%s\n", msg);
    int lol;
    return lol;
}

void win() {
    char flag[64] = {0};
    FILE* f = fopen("flag.txt", "r");
    fread(flag, 1, sizeof(flag), f);
    printf("Nice work! Here's the flag: %s\n", flag);
}

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    welcome();
    srand(seed());

    int key0 = rand() == 306291429;
    int key1 = rand() == 442612432;
    int key2 = rand() == 110107425;

    printf("Key0: %d | key1: %d | key2: %d", key0, key1, key2);
    if (key0 && key1 && key2) {
        win();
    } else {
        printf("Looks like you weren't lucky enough. Better luck next time!\n");
    }
}
```
It basically asks  for an input then initializes the random with a seed (i'll come back to it later) and then compares the values of `key0`, `key1`, `key2`
respectively with `306291429 , 442612432, 110107425`. If all the checks are `true` it prints for us the flag. </br>
After reading source code again and again i was like `this is impossible to solve` since i don't know the seed that generates this sequence `306291429, 442612432, 110107425`.</br>
I opened the binary in gdb, gave it `AAAA` as input and made a breakpoint before the `seed` function exists to try to know how the seed is generated. 
The return value was stored in `eax` so i inspected it with `i r eax` and it was `0x7fff`
