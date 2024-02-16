#Writing below code to make the random password generator
import random 
lowercharacters = "abcdefghijklmnopqrstuvwxyz";
uppercharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
numbers = "0123456789";
symbols="!@#$%^&*()?/";
all = lowercharacters+uppercharacters+numbers+symbols;

length = 8;
password = "".join(random.sample(all, length));
print("Enter 8 digit password")
print("You password is: " + password);

