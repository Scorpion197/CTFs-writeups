#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char *argv[]) {

    unsigned int seq[] = {306291429, 442612432, 110107425};

    for (int i = 0; i < 4294967295; i++) {

        srand(i);
        for (int j = 0; j < 3; j++) {

            if (rand() != seq[j])
                break;

            if (j == 2){
                printf("found seed: %d\n", i);
                printf("Next number: %d\n", rand());
                exit(0);
            }
        }
    }
    return 0;
}