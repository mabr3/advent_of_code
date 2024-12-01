import time

def timer(func):
    def inner(args, *kwargs):
        start_time = time.time()
        res = func(args, *kwargs)
        time_elapsed = time.time() - start_time
        print(f"{func.__name__} took {time_elapsed*1000} milliseconds")
        print(f"Result for {func.__name__} is {res}")

    # TODO write to CSV or to README in md table -- col lang, row day, part
    return inner

@timer
def test(a=1):
    print("BLABLA")
    return 1


def main():
    test(10)

if __name__ == '__main__':
    main()
