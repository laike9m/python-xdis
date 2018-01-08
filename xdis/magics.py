"""
Everything you ever wanted to know about Python versions and their
magic numbers. And a little bit more...

by_magic: in this dictionary, the key is a magic byte string like
# b'\x03\xf3\r\n' and its value is a canonic version string, like
# '2.7'

by_version: in this diectionary, the key is a canonic version string like '2.7,
and its value is a magic byte string like b'\x03\xf3\r\n' canonic
name, like '2.7'

magicint2version:  in this dictionary, the key is an magic integer, e.g. 62211,
and the value is its canonic versions string, e.g. '2.7'

PYTHON_MAGIC_INT: The magic integer for the current running Python interpreter
"""

import imp, re, struct, sys
from xdis import IS_PYPY

def add_magic_from_int(magic_int, version):
    magicint2version[magic_int] = version
    versions[int2magic(magic_int)] = version

def int2magic(magic_int):
    """Given a magic int like 62211, compute the corresponding magic byte string
     b'\x03\xf3\r\n' using the conversion method that does this.

    See also dictionary magic2nt2version which has precomputed these values
    for knonwn magic_int's.
    """

    if (sys.version_info >= (3, 0)):
        return struct.pack('Hcc', magic_int, bytes('\r', 'utf-8'), bytes('\n', 'utf-8'))
    else:
        return struct.pack('Hcc', magic_int, '\r', '\n')

def magic2int(magic):
    """Given a magic byte string, e.g. b'\x03\xf3\r\n', compute the
    corresponding magic integer, e.g. 62211, using the conversion
    method that does this.

    See also dictionary magic2nt2version which has precomputed these values
    for knonwn magic_int's.

    """
    return struct.unpack('Hcc', magic)[0]

def __by_version(magics):
    for m, v in list(magics.items()):
        if m not in by_magic:
            by_magic[m] = set([v])
        else:
            by_magic[m].add(v)
        by_version[v] = m
    return by_version

# Documentation for the below variables is above.
by_magic = {}
by_version = {}
magicint2version = {}
versions = {}
PYTHON_MAGIC_INT = magic2int(imp.get_magic())

# The magic word is used to reject .pyc files generated by other
# Python versions.  It should change for each incompatible change to
# the bytecode.
#
# The value of CR and LF is incorporated so if you ever read or write
# a .pyc file in text mode the magic number will be wrong; also, the
# Apple MPW compiler swaps their values, botching string constants.
#
# The magic numbers must be spaced apart at least 2 values, as the
# -U interpeter flag will cause MAGIC+1 being used. They have been
# odd numbers for some time now.
#
# There were a variety of old schemes for setting the magic number.
# The current working scheme is to increment the previous value by
# 10.
#
# Starting with the adoption of PEP 3147 in Python 3.2, every bump in magic
# number also includes a new "magic tag", i.e. a human readable string used
# to represent the magic number in __pycache__ directories.  When you change
# the magic number, you must also set a new unique magic tag.  Generally this
# can be named after the Python major version of the magic number bump, but
# it can really be anything, as long as it's different than anything else
# that's come before.  The tags are included in the following table, starting
# with Python 3.2a0.

# The below is taken from from Python/import.c, importlib/_bootstrap.py and other sources

#                  magic,  canonic version number
add_magic_from_int(11913,  '1.3')
add_magic_from_int(5892,   '1.4')

# 1.5, 1.5.1, 1.5.2
add_magic_from_int(20121,  '1.5')
add_magic_from_int(50428,  '1.6') # 1.6
add_magic_from_int(50823,  '2.0') # 2.0, 2.0.1
add_magic_from_int(60202,  '2.1') # 2.1, 2.1.1, 2.1.2
add_magic_from_int(60717,  '2.2') # 2.2

# Two magics one version!
add_magic_from_int(62011,  '2.3a0')
add_magic_from_int(62021,  '2.3a0')

add_magic_from_int(62041,  '2.4a0')
add_magic_from_int(62051,  '2.4a3')
add_magic_from_int(62061,  '2.4b1')
add_magic_from_int(62071,  '2.5a0')
add_magic_from_int(62081,  '2.5a0') # ast-branch
add_magic_from_int(62091,  '2.5a0') # with
add_magic_from_int(62092,  '2.5a0') # changed WITH_CLEANUP opcode
add_magic_from_int(62101,  '2.5b3') # fix wrong code: for x, in ...
add_magic_from_int(62111,  '2.5b3') # fix wrong code: x += yield

# Fix wrong lnotab with for loops and storing constants that should
# have been removed
add_magic_from_int(62121,  '2.5c1')

# Fix wrong code: "for x, in ..." in listcomp/genexp)
add_magic_from_int(62131,  '2.5c2')

# Dropbox-modified Python 2.5 used in versions 1.1x and before of Dropbox
add_magic_from_int(62135,  '2.5dropbox')

add_magic_from_int(62151,  '2.6a0')   # peephole optimizations & STORE_MAP
add_magic_from_int(62161,  '2.6a1')   # WITH_CLEANUP optimization

# Optimize list comprehensions/change LIST_APPEND
add_magic_from_int(62171,  '2.7a0')

# Optimize conditional branches: introduce POP_JUMP_IF_FALSE and
# POP_JUMP_IF_TRUE
add_magic_from_int(62181,  '2.7a0+1')

add_magic_from_int(62191,  '2.7a0+2') # introduce SETUP_WITH
add_magic_from_int(62201,  '2.7a0+3') # introduce BUILD_SET
add_magic_from_int(62211,  '2.7')     # introduce MAP_ADD and SET_ADD

# Dropbox-modified Python 2.7 used in versions 1.2-1.6 or so of
# Dropbox
add_magic_from_int(62215,  '2.7dropbox')

# PyPy including pypy-2.6.1, pypy-5.0.1 PyPy adds 7 to the corresponding CPython nmber
add_magic_from_int(62211+7, '2.7pypy')

add_magic_from_int(3000,  '3.000')
add_magic_from_int(3010,  '3.000+1')  # removed UNARY_CONVERT
add_magic_from_int(3020,  '3.000+2')  # added BUILD_SET
add_magic_from_int(3030,  '3.000+3')  # added keyword-only parameters
add_magic_from_int(3040,  '3.000+4')  # added signature annotations
add_magic_from_int(3050,  '3.000+5')  # print becomes a function
add_magic_from_int(3060,  '3.000+6')  # PEP 3115 metaclass syntax
add_magic_from_int(3061,  '3.000+7')  # string literals become unicode
add_magic_from_int(3071,  '3.000+8')  # PEP 3109 raise changes
add_magic_from_int(3081,  '3.000+9')  # PEP 3137 make __file__ and __name__ unicode
add_magic_from_int(3091,  '3.000+10') # kill str8 interning
add_magic_from_int(3101,  '3.000+11') # merge from 2.6a0, see 62151
add_magic_from_int(3103,  '3.000+12') # __file__ points to source file
add_magic_from_int(3111,  '3.0a4')  # WITH_CLEANUP optimization
add_magic_from_int(3131,  '3.0a5')  # lexical exception stacking, including POP_EXCEPT)
add_magic_from_int(3141,  '3.1a0')  # optimize list, set and dict comprehensions
add_magic_from_int(3151,  '3.1a0+') # optimize conditional branches
add_magic_from_int(3160,  '3.2a0')  # add SETUP_WITH
add_magic_from_int(3170,  '3.2a1')  # add DUP_TOP_TWO, remove DUP_TOPX and ROT_FOUR
add_magic_from_int(3180,  '3.2a2')  # 3.2a2 (add DELETE_DEREF)

# Python 3.2.5 - PyPy 2.3.4 PyPy adds 7 to the corresponding CPython
# number
add_magic_from_int(3180+7,  '3.2pypy')

add_magic_from_int(3190,  '3.3a0')  # __class__ super closure changed
add_magic_from_int(3200,  '3.3a0+') # __qualname__ added
add_magic_from_int(3220,  '3.3a1')  # changed PEP 380 implementation

# Added size modulo 2**32 to the pyc header
# NOTE: 3.3a2 is our name, other places call it 3.3
# but most 3.3 versions are 3.3a4 which comes next.
# FIXME: figure out what the history is and
# what the right thing to do if this isn't it.
add_magic_from_int(3210,  '3.3a2')
add_magic_from_int(3230,  '3.3a4')  # revert changes to implicit __class__ closure

# Evaluate positional default arg keyword-only defaults)
add_magic_from_int(3250,  '3.4a1')

# Add LOAD_CLASSDEREF; add_magic_from_int locals, f class to override free vars
add_magic_from_int(3260,  '3.4a1+1')

add_magic_from_int(3270,  '3.4a1+2') # various tweaks to the __class__ closure
add_magic_from_int(3280,  '3.4a1+3')   # remove implicit class argument
add_magic_from_int(3290,  '3.4a4')     # changes to __qualname__ computation
add_magic_from_int(3300,  '3.4a4+')    # more changes to __qualname__ computation
add_magic_from_int(3310,  '3.4rc2')    # alter __qualname__ computation
add_magic_from_int(3350,  '3.5')       # 3.5.0, 3.5.1, 3.5.2
add_magic_from_int(3351,  '3.5.3')     # 3.5.3
add_magic_from_int(3361,  '3.6.0a1')   # 3.6.0a1
add_magic_from_int(3370,  '3.6.0a1+1') # 3.6.0a?
add_magic_from_int(3370,  '3.6.0a1+2') #
add_magic_from_int(3372,  '3.6.0a3')   #
add_magic_from_int(3378,  '3.6.0b2')   #
add_magic_from_int(3379,  '3.6.0rc1')  #
add_magic_from_int(3390,  '3.7.0alpha0')

# Weird ones
# WTF? Python 3.2.5 - PyPy 2.3.4  this doesn't follow the rule below

add_magic_from_int(48,     '3.2a2')
add_magic_from_int(112,    '3.5pypy') # pypy3.5-c-jit-latest
add_magic_from_int(1011,   '2.7.1b3Jython') # jython
add_magic_from_int(22138,  '2.7.7Pyston')  # 2.7.8pystem, pyston-0.6.0, pyston-0.6.1


magics = __by_version(versions)

# From a Python version given in sys.info, e.g. 3.6.1,
# what is the "canonic" version number, e.g. '3.6.0rc1'
canonic_python_version = {}

def add_canonic_versions(versions, canonic):
    for v in versions.split():
        canonic_python_version[v] = canonic
        magics[v] = magics[canonic]
        try:
            magics[float(v)] = magics[canonic]
        except:
            pass
        pass


    return

add_canonic_versions('1.5.1 1.5.2', '1.5')
add_canonic_versions('2.0.1', '2.0')
add_canonic_versions('2.1.1 2.1.2', '2.1')
add_canonic_versions('2.2.3', '2.2')
add_canonic_versions('2.3 2.3.7', '2.3a0')
add_canonic_versions('2.4 2.4.1 2.4.2 2.4.3 2.4.5 2.4.6', '2.4b1')
add_canonic_versions('2.5 2.5.1 2.5.2 2.5.3 2.5.4 2.5.5 2.5.6', '2.5c2')
add_canonic_versions('2.6 2.6.6 2.6.7 2.6.8 2.6.9', '2.6a1')
add_canonic_versions('2.7.1 2.7.2 2.7.2 2.7.3 2.7.4 2.7.5 2.7.6 2.7.7 '
                     '2.7.8 2.7.9 2.7.10 2.7.11 2.7.12 2.7.13 2.7.14', '2.7')
add_canonic_versions('3.0 3.0.0 3.0.1',                                '3.0a5')
add_canonic_versions('3.1 3.1.0 3.1.1 3.1.2 3.1.3 3.1.4 3.1.5',        '3.1a0+')
add_canonic_versions('3.2 3.2.0 3.2.1 3.2.2 3.2.3 3.2.4 3.2.5 3.2.6',  '3.2a2')
add_canonic_versions('3.3 3.3.1 3.3.0 3.3.2 3.3.3 3.3.4 3.3.5 3.3.6 3.3.7rc1 3.3.7', '3.3a4')
add_canonic_versions('3.4 3.4.0 3.4.1 3.4.2 3.4.3 3.4.4 3.4.5 3.4.6 3.4.7', '3.4rc2')
add_canonic_versions('3.5.0 3.5.1 3.5.2', '3.5')
add_canonic_versions('3.5.3 3.5.4', '3.5.3')
add_canonic_versions('3.6 3.6.0 3.6.1 3.6.2 3.6.3', '3.6.4', '3.6.0rc1')

add_canonic_versions('2.7.10pypy 2.7.13pypy', '2.7pypy')
add_canonic_versions('2.7.3b0Jython', '2.7.1b3Jython')
add_canonic_versions('3.2.5pypy', '3.2pypy')
add_canonic_versions('3.5.3pypy', '3.5pypy')
add_canonic_versions('3.5.3pypy', '3.5pypy')
add_canonic_versions('2.7.8Pyston', '2.7.7Pyston')
add_canonic_versions('3.7 3.7.0', '3.7.0alpha0')

# The canonic version for a canonic version is itself
for v in versions.values():
    canonic_python_version[v] = v

# A set of all Python versions we know about
python_versions = set(canonic_python_version.keys())

def __show(text, magic):
    print(text, struct.unpack('BBBB', magic), struct.unpack('HBB', magic))

def py_str2float(version):
    """Convert a Python version into a 'canonic' floating-point number which
    that can then be used to look up a magic number.
    A runtime error is raised if "version" is not found.
    """
    if version in magics:
        magic = magics[version]
        for v, m in list(magics.items()):
            if m == magic:
                try:
                    return float(canonic_python_version[v])
                except:
                    try:
                        m = re.match('^(\d\.)(\d+)\.(\d+)$', v)
                        if m:
                            return float(m.group(1)+m.group(2)+m.group(3))
                    except:
                        pass
                    pass
                pass
            pass
    raise RuntimeError("Can't find a valid Python version for version %s"
                       % version)
    return

def sysinfo2float(version_info=sys.version_info):
    """Convert a sys.versions_info-compatible list into a 'canonic'
    floating-point number which that can then be used to look up a
    magic number.  Note that this can only be used for released version
    of C Python, not interim development versions, since we can't
    represent that as a floating-point number.

    For handling Pypy, pyston, jython, etc. and interim versions of
    C Python, use sysinfo2magic.
    """
    vers_str = '.'.join([str(v) for v in version_info[0:3]])
    if version_info[3] != 'final':
        vers_str += '.' + ''.join(version_info)
    if IS_PYPY:
        vers_str += 'pypy'
    else:
        try:
            import platform
            platform = platform.python_implementation()
            if platform in ('Jython', 'Pyston'):
                vers_str += platform
                pass
        except ImportError:
            # Python may be too old, e.g. < 2.6 or implementation may
            # just not have platform
            pass
    return py_str2float(vers_str)


def sysinfo2magic(version_info=sys.version_info):
    """Convert a list sys.versions_info compatible list into a 'canonic'
    floating-point number which that can then be used to look up a
    magic number.  Note that this can raise an exception.
    """

    # FIXME: DRY with sysinfo2float()
    vers_str = '.'.join([str(v) for v in version_info[0:3]])
    if version_info[3] != 'final':
        vers_str += ''.join([str(v) for v in version_info[3:]])

    if IS_PYPY:
        vers_str += 'pypy'
    else:
        try:
            import platform
            platform = platform.python_implementation()
            if platform in ('Jython', 'Pyston'):
                vers_str += platform
                pass
        except ImportError:
            # Python may be too old, e.g. < 2.6 or implementation may
            # just not have platform
            pass

    return magics[vers_str]


def test():
    magic_20 = magics['2.0']
    current = imp.get_magic()
    magic_current = by_magic[ current ]
    print(type(magic_20), len(magic_20), repr(magic_20))
    print()
    print('This Python interpreter has version', magic_current)
    print('Magic code: ', PYTHON_MAGIC_INT)
    print(type(magic_20), len(magic_20), repr(magic_20))
    print(sysinfo2float())
    assert sysinfo2magic() == current

if __name__ == '__main__':
    test()
