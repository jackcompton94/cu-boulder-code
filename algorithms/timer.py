import time


def time_it(function, args):
    start_time = time.time()
    function(args)
    stop_time = time.time()
    return stop_time - start_time
