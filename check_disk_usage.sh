#!/bin/bash
threshold=20
alert=0
while read -r line; do
    use_percent=$(echo "$line" | awk '{print $5}' | tr -d '%')
    mount_point=$(echo "$line" | awk '{print $6}')
    
    if [ "$use_percent" -ge $((100 - threshold)) ]; then
        echo "Filesystem at $mount_point is over threshold with ${use_percent}% used"
        alert=1
    fi
done < <(df -h --output=source,fstype,size,used,avail,pcent,target | tail -n +2)

if [ "$alert" -eq 1 ]; then
    echo "Not enough free space"
    exit 1 
else
    echo "Sufficient free space"
    exit 0 
fi
