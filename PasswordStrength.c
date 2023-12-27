/*
Author: ServerLite
Date: 12/27/2023
Description: Write a password varification function that validates if a password is strong enough or not.
*/

#include <stdio.h>

#define MinIntegers 1
#define MinSpecialCharacters 1
#define MinCharacterCount 8

#define PASSWORD "dustdog@2"

/*
Output mapping for password
0 = Password is strong
1 = Not enough integers
2 = Not enough special characters
3 = Not enough characters
*/

typedef
struct PasswordInformation {
  int CharacterLength;
  int Integers;
  int Characters;
  int SpecialCharacters;
} PasswordInformation;

int GetStringLength(char text[]) {
  int length = 0;
  while (text[length] != '\0') {
    length++;
  };
  return length;
}

int IsNumber(char character) {
  for (int i=0; i<10; i++) {
    if (i+'0' == character) {
      return 0;
    };
  };
  return 1;
}

int IsSpecialCharacter(char character) {
  char specials[] = "!@#$%^&*()";
  for (int i=0; i<GetStringLength(specials); i++) {
    if (specials[i] == character) {
      return 0;
    }
  };
  return 1;
}

PasswordInformation GetInformation(char text[]) {
  PasswordInformation info;
  info.CharacterLength = GetStringLength(text);
  info.Integers = 0;
  info.SpecialCharacters = 0;
  info.Characters = 0;
  
  for (int i=0; i<info.CharacterLength; i++) {
    if (!IsNumber(text[i])) {
      info.Integers += 1;
    } else if (!IsSpecialCharacter(text[i])) {
      info.SpecialCharacters += 1;
    } else {
      info.Characters += 1;
    }
  };
  return info;
}

int IsPasswordStrong(char password[]) {
  PasswordInformation info = GetInformation(password);

  if (!(info.Integers >= MinIntegers)) {
    return 1;
  } else if (!(info.SpecialCharacters >= MinSpecialCharacters)) {
    return 2;
  } else if (!(info.CharacterLength >= MinCharacterCount)) {
    return 3;
  } else {
    return 0;
  }
}

int main(void) {
  int IsStrong = IsPasswordStrong(PASSWORD);
  printf("%d", IsStrong);
  return 0;
}

