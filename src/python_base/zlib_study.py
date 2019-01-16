# -*- coding=utf-8 -*-
import zlib

def zlib_compress_dict(data):
    return zlib.compress(data).encode("base64")


def zlib_decompress_dict(data):
    return zlib.decompress(data.decode("base64"))

if __name__ == '__main__':
    my_dict = '{"a":"aaa", "b":"bbb", "c":"ccc"}'
    result = zlib_compress_dict(my_dict)
    print result
    origin = zlib_decompress_dict(result)
    print origin
