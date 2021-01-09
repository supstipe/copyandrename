import os
import shutil

dir_src = "C:\source"
dir_dst = "C:\scans"

i = 1

for dirname in os.listdir(dir_src):
    dirpath = os.path.join(dir_src, dirname)
    if not os.path.isdir(dirpath):
        continue
    for filename in os.listdir(dirpath):
        if filename == "scan.txt":
            src_file = os.path.join(dirpath, filename)
            dst_file = os.path.join(dir_dst, f"scan_{i:03}.txt")
            print("src_file: ", src_file)
            print("dst_file: ", dst_file)
            shutil.copyfile(src_file, dst_file)
            i += 1