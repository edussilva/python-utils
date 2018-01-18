"""
    Get ipv4 and date from access.log
"""

import re


regex = re.compile(r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - (?P<date>\[.*\])')

def match_ip(s):
    m = regex.search(s)
    return {
        'ip': m.group('ip'),
        'date': m.group('date'),
    }


def get_ips(filepath='access.log', resultpath='result.txt'):
    temp = []
    with open(filepath, 'r') as f:
        for line in f:
            try:
                temp.append('{ip} - {date}'.format(**match_ip(line)))
            except:
                pass

    # temp = set(temp)

    with open(resultpath, 'w') as f:
        for line in temp:
            f.write(line + '\n')
