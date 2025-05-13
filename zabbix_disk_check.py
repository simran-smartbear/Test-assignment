#!/usr/bin/env python3

import psutil

threshold = 20
for part in psutil.disk_partitions(all=False):
    try:
        usage = psutil.disk_usage(part.mountpoint)
        free_percent = 100 - usage.percent
        if free_percent < threshold:
            print(1)
            exit(0)
    except PermissionError:
        continue
print(0)