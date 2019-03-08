from features import *

if __name__ == "__main__":
    print(top1m.get("google.com"))
    print(top1m.get("google.null"))
    print(top1m.get("http://google.com"))
    print(top1m.get("http://qq.com"))
