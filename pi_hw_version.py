import re


MODEL_DICT = {
    '0002': 'B rev 1.0',

    '0003': 'B rev 1.0',

    '0004': 'B rev 2.0',
    '0005': 'B rev 2.0',
    '0006': 'B rev 2.0',

    '0007': 'A',
    '0008': 'A',
    '0009': 'A',

    '000d': 'B rev 2.0',
    '000e': 'B rev 2.0',
    '000f': 'B rev 2.0',

    '0010': 'B+',
    '0013': 'B+',

    '0011': 'Compute module',

    '0012': 'A+',

    'a01041': 'Pi 2 Model B',
    'a21041': 'Pi 2 Model B',

    '900092': 'PiZero',

    'a02082': 'Pi 3 Model B',
    'a22082': 'Pi 3 Model B',
    
}

def read_cpuinfo(filename='/proc/cpuinfo'):
    """ Function that reads the contents of the passed filename """
    f = open('/proc/cpuinfo', 'r')
    cpuinfo = f.readlines()
    f.close()
    return cpuinfo

def get_hw_version(cpuinfo):
    """Function rertunrning the Revision"""    
    p = re.compile('^Revision\s+:\s(.*)')
    for line in cpuinfo:
        #print line.strip()
        m = p.match(line)
        if m:
            return m.group(1)



def print_pi_hw_version (revision):
    """ gets the Revision and prints the raspbery version in user friendly format"""
    return MODEL_DICT[revision]


if __name__ == "__main__":
    cpuinfo = read_cpuinfo()
    revision = get_hw_version(cpuinfo)
    print (print_pi_hw_version (revision))
    #print get_hw_version()
