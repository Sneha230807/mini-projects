#include <stdio.h>
#include <string.h>
int main() {
    char secretName[] = "Alex";
    char userGuess[50];
    int attempts = 0;
    printf("Welcome to the Name Guessing Game!\n");
    printf("Can you guess the secret name?\n\n");
    while (1) {
        printf("Enter your guess: ");
        scanf("%20s", userGuess);
        attempts++;
        if (strcmp(userGuess, secretName) == 0) {
            printf("\nCongratulations! You guessed it right!\n");
            printf("The secret name was: %s\n", secretName);
            printf("Total attempts: %d\n", attempts);
            break;
        } else {
            printf("Wrong name! Try again.\n\n");
        }
    }
    return 0;
}
