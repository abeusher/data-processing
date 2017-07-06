#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
# import time
import gzip
import json


def upper_list(input_list):
    output_list = []
    for item in input_list:
        new_item = item.upper()
        output_list.append(new_item)
    return output_list


def parse_modern_business_solutions():
    filename = "f:/data/004_modernbusinessbsolutions/modbsolutions.txt.gz"
    file = gzip.open(filename, 'rU')
    # fout = gzip.open('f:/data/004_modernbusinessbsolutions/modern_business_solutions.txt.gz', 'wb')
    fout = open(
        'f:/data/004_modernbusinessbsolutions/modern_business_solutions.txt', 'w')
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
        if counter % 50000 == 0:
            print counter
        line = line.strip()
        data = json.loads(line)
        first_name = data.get('first_name', 'UNKNOWN').upper()
        last_name = data.get('last_name', 'UNKNOWN').upper()
        gender = data.get('gender', 'UNKNOWN')
        address1 = data.get('address1', 'UNKNOWN')
        city = data.get('city', 'UNKNOWN')
        state = data.get('state', 'UNKNOWN')
        zipcode = data.get('zip', 'UNKNOWN')
        email = data.get('email', 'UNKNOWN')
        job = data.get('job', 'UNKNOWN')
        ipv4_address = data.get('ip', 'UNKNOWN')
        inAccountName = data.get('inAccountname', 'UNKNOWN')
        createdAt = data.get('createdAt', {})
        createdAt = createdAt.get('$date', 'UNKNOWN')
        updatedAt = data.get('updatedAt', {})
        updatedAt = updatedAt.get('$date', 'UNKNOWN')
        output_list = [
            first_name, last_name, gender, address1, city, state, zipcode, email, job, ipv4_address, inAccountName, createdAt, updatedAt
        ]
        output_list = upper_list(output_list)
        output_text = '\t'.join(output_list)
        fout.write(output_text + '\n')
    print counter
    print "All done."
    fout.close()


def main():
    parse_modern_business_solutions()


if __name__ == '__main__':
    main()
