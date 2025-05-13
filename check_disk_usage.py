import psutil
import sys

threshold = 20
alert = False

for part in psutil.disk_partitions(all=False):
    try:
        usage = psutil.disk_usage(part.mountpoint)
        free_percent = 100 - usage.percent
        if free_percent < threshold:
            print(f"Filesystem at {part.mountpoint} has only {free_percent:.2f}% free")
            alert = True
    except PermissionError:
        continue

sys.exit(1 if alert else 0)
