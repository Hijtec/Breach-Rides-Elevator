"""This module implements various performance functions and decorators."""

import cv2


def perf_time(func):
    """Measures a time of a piece of code."""

    def wrapper(*args, **kwargs):
        start = cv2.getTickCount()
        func(*args, **kwargs)
        end = cv2.getTickCount()
        dtime = (end - start) / cv2.getTickFrequency()
        print(f"{func.__name__} took {dtime}s to run")

    return wrapper
