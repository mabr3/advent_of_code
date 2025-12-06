import time


def reader(day, strip=True):
    with open("/".join(__file__.split("/")[:-2]) + f"/inputs/{day}.txt", "r") as f:
        if strip:
            lines = [i.rstrip("\n") for i in f.readlines()]
        else:
            lines = [i for i in f.readlines()]
    return lines


def timer(func):
    def inner(args, *kwargs):
        start_time = time.time()
        res = func(args, *kwargs)
        time_elapsed = time.time() - start_time
        print(f"{func.__name__} took {time_elapsed * 1000} milliseconds")
        print(f"Result for {func.__name__} is {res}")
        return res

    # TODO write to CSV or to README in md table -- col lang, row day, part
    return inner
