
# 2022.09.07 - hbertini
#

import uos


def get_storage_space():
	# returns nodemcu storage space
    # >>> uos.statvfs('/')
    # (4096, 4096, 348, 329, 329, 0, 0, 0, 0, 255)
    # 
    # so,
    # 4096 * 348 is total space in bytes
    # 4096 * 329 is free space in bytes
    # used space = total - free
    st = uos.statvfs('/')
    return f"Storage usage (bytes): {st[1]*st[3]}/{st[0]*st[2]}"
    