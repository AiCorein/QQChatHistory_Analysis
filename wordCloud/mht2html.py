import email, email.message
import os

"""
将 mht 文件转化为 html 文件
"""

def convert(filename):
    mht = open(filename, "rb")
    print("转化中...\n")
    a = email.message_from_bytes(mht.read())			
    parts = a.get_payload()
    if not type(parts) is list:
        parts = [a]

    for p in parts:
        if not os.path.exists('./works'):
            os.mkdir('./works')
        open('./works/records.html', "wb").write(p.get_payload(decode=True))
        print("完成转化.\n")

if __name__ == "__main__":
    convert('./records.mht')