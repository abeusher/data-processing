#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
# import time
import gzip


def parse_modern_business_solutions():
    filename = "f:/data/004_modernbusinessbsolutions/modern_business_solutions.txt.gz"
    file = gzip.open(filename, 'rU')
    # fout = gzip.open('f:/data/004_modernbusinessbsolutions/modern_business_solutions.txt.gz', 'wb')
    fout = open(
        'f:/data/004_modernbusinessbsolutions/filtered_laywers.txt', 'w')
    headers = ['first_name',
               'last_name',
               'gender',
               'address1',
               'city',
               'state',
               'zipcode',
               'email',
               'job',
               'ipv4_address',
               'account',
               'created_at',
               'updated_at',
               ]
    headers_text = '\t'.join(headers)
    fout.write(headers_text + '\n')
    counter = 0
    for line in file:
        counter += 1
        if counter % 250000 == 0:
            print counter
        line = line.strip()
        parts = line.split('\t')
        if len(parts) < 11:
            continue
        if len(parts) == 11:
            parts.extend(['', '', ])
        if len(parts) == 12:
            parts.extend(['', ])
        if len(parts) > 13:
            parts = parts[0:13]
        first_name, last_name, gender, address1, city, state, zipcode, email, job, ipv4_address, inAccountName, createdAt, updatedAt = parts
        if job.find('LAWYER') != -1 or job.find('ATTORNEY') != -1:
            fout.write(line + '\n')
    print counter
    print "All done."
    fout.close()


def main():
    parse_modern_business_solutions()


if __name__ == '__main__':
    main()
