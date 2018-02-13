#!/usr/bin/env python

import argparse
import struct

parser = argparse.ArgumentParser(description='Generate ER-301 slices file')
parser.add_argument('-w', '--width', type=int, default=256, help='Slice width in samples')
parser.add_argument('-n', '--number', type=int, default=4096, help='Number of slices')
parser.add_argument('file', nargs=1, help='Output file name')
args = parser.parse_args()


MAGIC = '\xba\xdc\xcd\xab\x07\x00\x00\x00Slices\x00\x00\x00\x00\x00\x00\x00\x00\x00'
NUM = 16 * 16 * 16
WIDTH = 256

with file(args.file[0], 'w') as f:
    f.write(MAGIC)
    f.write(struct.pack('i', args.number))
    for i in xrange(args.number):
        f.write(struct.pack('QQ', i * args.width, 4575657221408423936))
