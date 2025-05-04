import Arithmatics

def main():
    print("Enter first Number : ")
    No1 = int(input())

    print("Enter Second Number : ")
    No2 = int(input())

    ans = Arithmatics.Multiplication(No1,No2)

    print("Multiplication is : ",ans)

if __name__ == "__main__":
    main()