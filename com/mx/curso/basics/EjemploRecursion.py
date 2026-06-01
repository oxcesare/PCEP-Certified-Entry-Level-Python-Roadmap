def print_n_times(string, n):
    if n > 0:
        print(string)
        print_n_times(string, n-1)

def main():
    print_n_times("hola", 3)

if __name__ == "__main__":
    main()