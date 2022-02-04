import sys

def nest(dept, n):
    if dept <= 0:
        return 0

    for i in range(0, n):
        print(f"dept: {dept}, index: {i}")

    return nest(dept - 1, n)

if __name__ == "__main__":
    dept = int(sys.argv[1])  # for文の回数
    n = int(sys.argv[2])     # １回のfor文で何回回すか

    nest(dept, n)
