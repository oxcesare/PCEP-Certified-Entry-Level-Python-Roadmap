def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

def main():
    countdown(2)
    countdown(3)

if __name__ == '__main__':
    main()