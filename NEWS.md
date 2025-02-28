4.1.1 2019-10-29 pre Halloween
==============================

- Fix unmarshaling 3.4+ object_ref bugs.
  A big thanks to Armin Rigo of the PyPy team.
- Add Pypy 3.6+ disassembly, e.g. pypy3.6-7.1.0 and pypy3.6-7.1.1
- Add Python 3.7.5, 2.7.16, 2.7.17rc1, and 2.7.15candidate1 as a valid releases
- convert unmarshal `if` .. `elif` code to a dictionary lookup with function entries
- Handle newer Python importlib - thanks to laike9m

4.1.0 2019-10-12 Stony Brook Ride
=================================

- Add early bytecodes: 1.0, 1.1, 1.2, and 1.6. Going off of pycdc bytecode since this is the only bytecode for these versions I know of
- Fix bug in Python 3.x decompiling 2.x that contains strings with non-ascii characters
- More generally, better handling of non-ascii Python 2 strings in both input and output in Python 3
- pypy 3.6-7.1.0 tolerance

4.0.4 2019-10-02
================

- Add most-recent 3.8 magic number
- Remove some 3.8 invalid escape warnings

4.0.3 2019-7-24  Mueller day
============================

- Support 3.8.0beta2; Code38 type with `posonlyargcount` field
- Add Python versions 3.4.10, 3.7.4 and 3.6.9
- `script` no longer works to install pydisasm; `entry_points` still works
- Add pypy 3.6 opcode formatting for `MAKE_FUNCTION` and `EXTENDED_ARG`
- Add `format_CALL_function` and use it or pypy36
- Start using "blacken" to reformat Python files

4.0.2 2019-6-12  Fleetwood at 65
================================

- To unicode strings in Python 2.x Try to convert to ascii, but if that doesn't work, leave as unicode. (x0ret)
- `BUILD_TUPLE_UNPACK_WITH_CALL` is a vararg


===============
4.0.1 2019-4-30
===============

- Add magics.IS_PYPY3 and correct `is_pypy()`
- disassemble PyPY3 versions correctly

4.0.0 2019-4-09
===============

- Expand is_jump_target to True, 'loop', False. This is the reason for the version bump
- Remove deprecated opcodes_pypyDD.py files. Use opcode_DDpypy instead.
- Fix bug in setting jump offset in wordcode (3.6+) relative jumps.
- Note that this works now in Python 3.8 (dev)
- Add 3.6{,.1}pypy version
- Dry opcodes 3.6 - 3.8

3.9.1 2019-3-28
===================

- Go over list of available Python 	versions
- 3.8.0alpha3 tolerance

3.9.0 2019-3-23
===================

- Correct instruction field `inst_size` in instructions that were build from `EXTENDED_OP` instructions
- Add `has_extended_arg` field in instruction


3.8.9 2018-10-20
====================

- Add magic for 3.6.8, 3.7.2
- Dropbox-hacked bytecode fixes, and some typos (jwilk@jwilk.net)
- Go over stack effects for vararg ops
- Fix CI for pypy
- Work around wheel munging

3.8.8 2018-10-20
=====================
- Add magic for 3.6.7, 3.7.1

3.8.7 2018-07-19
=====================

- Add magic for 3.6.5

3.8.6 2018-07-03 Independence-1
=======================================

- Remove stray print that got into op_imports

3.8.5 2018-07-02 Pre Independence
==========================================

- Add Python 3.7.0 magic and adjustments for its bytecode file reading
- Note Python 3.6.6 version

3.8.4 2018-06-12 When I'm 64
====================================

- Add Python 1.3 opcodes

3.8.3 2018-06-04 MF
=========================

- Fix Python 1.4 opcodes
- Fix misleading error message when failing to open a file
  (courtesy of jeffenstein)

3.8.2 2018-05-18 Paper Tiger
===================================

- Add 2.7.15rc1/candidate1
- Add Python 1.4 opcodes

3.8.1 2018-04-16
====================

- Correct classification of CALL_METHOD
- Add 3.6.5 and 3.7.0beta{2,3}
- Start supporting 3.7

3.8.0 2018-04-04
=====================

- Track 3.7 magic numbers, and interim releases
- a number of varargs opcodes introduced in 3.5 were not marked as such

3.7.0  2018-03-7
====================

License is GPL2.0 only now

- Make it work on bigendian machines
- Add canonic versions up to 3.4.8 and 3.5.5

3.6.11  2018-02-9 pycon2018.co
======================================

- Add version 3.5.5 to canonic_versions

3.6.10 2018-02-3
=====================


- Handle pypy in str2float
- Accomodate broken or incomplete "import platform"
- Pin Hypothesis to 3.0.0 - it has been broken after 3.0.0

3.6.9 2018-01-21
=====================

- Correct improper 3.4.4 setting

3.6.8 2018-01-21
=====================

- Add 3.4.4
- Fix a small bug in load.py
- improve unpack_opargs_wordcode

3.6.7 2018-01-21
=====================

- Add 3.7.0alpha3
- Fix bug in disassembly of 3.6+ from 2.x

3.6.6 2018-01-19
=====================

- Fix a bug in py_str2float for handling 3-place version number
- pydisasm: handle --version properly and invalid files better
- test_pyenvlib.py: can now test >= 3.5.0 (if not Pypy)

3.6.5 2018-01-18
=====================

- Go over 3.5 and 3.6 magics
- test_pyenvlib.py pick up acceptable python versions from
  xdis.magics rather than hardcode it in.

3.6.4 2018-01-08 Samish

- Update magics for 3.3.7, 3.6.4, 3.5.3, and 3.5.4

3.6.3 2017-12-09 Dr. Gecko
=====================

- Add pydisasm --header/--no-header
  option --header shows just the module-level header information
- Add magic.magicint2version
  In this dictionary, the key is an magic integer, e.g. 62211,
  and the value is its canonic versions string, e.g. '2.7'

3.6.2 2017-12-02

- Add canonic 3.2, 3.2a2, in op_imports
- Handle {-,}nan and {-,}inf in bytecode print attributes

3.6.1 2017-11-10
=====================

- Improve --asm option: disambiguate code objects with the same co_name
- Update canonic versions 3.6.3, 3.5.4, etc.
- "std" API now uses get_opcode_module rather than get_opcode()
- Add function extended_arg_val and use it in unpack_opargs_bytecode()
- str2version(): canonicalize version before float
- str2float(): We now at least detect inter-python version magic changes and
  can return something like 3.54 for 3.5.4  This assumes there never will be a 3.51

3.6.0 2017-09-25
=====================

- StdApi now uses std functions and constants from the
  correctly generated opc rather than the standard dis module (moagstar)
- Improve accuracy of opcode stack effects; classify opcodes more correctly
- Regularize opcode names: pypy is at the end now
- Correct writing Python3 bytecode from Python2 and Python2 bytecode from Python 3
- Add function to load from file object
- Add EXTENDED_ARG_SHIFT the number of bit positions EXTENDED_ARGS shifts
  This varies depending on where we are with respect to Python 3.6; similarly
  add ARG_MAX_VALUE, the maixumim integer value an operand field can have before
  needing EXTENDED_ARGS
- add unpack_opargs_bytecode which is similar to unpack_opargs_wordcode of 3.6
  This probably fixes a long-standing but little-noticed bug in Python 2.x disassembly
- cross version compatability bug fixed in code2num()
- Mark NOFOLOW opcodes (RETURN, RAISE)
- Mark conditional opcodes (POP_JUMP_IF...)
- Add len() and getitem() to code types code types to mimic Python3 behavior
- More tests; add appveyor CI testing

3.5.5 2017-08-31
=====================

- Add 3.7 opcodes
- Add optional file parameter on load_file
- add functions code_has_star_arg and code_has_star_star_arg (from uncompyle6)

3.5.4 2017-08-15
=====================

- Add internal switch in findlabels() to show multiple offsets for a
  given line.  This is turned on in pydisasm --xasm mode. Otherwise it
  is off. Sme  programs make use of findlinstart's somewhat misleading
  behavior

- Add methods for selecting from sys.version_info to the right opcode
  module, or canonic Python string or floating-point number.

- Add a notion of a canonic Python version.

- Add magic values for pyston and Jython.

- Some pyston tolerance. More is needed though.


3.5.3 2017-08-12
=====================

Showing all line number bolixes uncompyle6 and the trepan debuggers,
so nuke that for now.

However we show the full deal in pydisasm for asm format.  Here it is
imporant since we recreate the line number table based on information
given in the instructions.  We could and probably should allow showing
all of the line number in the default format as well.  Underneath there
is a parameter to control that.

* Add pypy 3.5.3 magic number


3.5.2 2017-08-09
=====================

- magic to opcode for all known versions we handle
- simpiler import access to opcodes modules
- magic lookup for Python 3.3 is probably more correct more often

3.5.1 2017-07-14
=====================

Overall: Better xasm support, pydisasm improvements

- Was picking up wrong findlabels and findlinestarts in Python 3.5
- Add ARG_MAX_VALUE: the largest operand value before needing EXTENDED_ARG
- Allow lnotab as a dict before code freeze
- pydisasm: don't show Freevars more than once. Do show varnames,
  the combined positional + local vars
- change cmp_op values so they don't have an embedded space
  this helps xasm tokenization of COMPARE_OP's operand
- --asm option fixes
- a frozenset is more appropriate for opcode sets

3.5.0 2017-07-08
=====================

Overall: Support for bytecode assembler (xasm), Better 3.4-3.6 support

- Add --xasm option to pydisasm. This will output a disassembly
  suitable for an assembler, specifically xasm.
- Add magic lookup for 3.4.[0..6] 3.5.[0..2] and 3.6.[0..1]
- Add magic lookup for base versions, e.g. 2.7 or 3.4
- Trap ill-formed python bytecode bettern
- Show timestamp in pydisasm output as it is stored
- Add "optype" field to Instructions. Derived from the has_xxx lists
- Marshaling for Python2 and Python3 code when using cross-version
  is aware that the format for the other type is different.
- Add opcode sets corresponding to the the opcode has_xxx lists.
- Document Code2 and Code3 a little better
- add Code2Compat and Code3Compat to make cross-version Code creation
  easier
- add Code2/Code3 freeze() routine which convert from from a
  programmer-friendly code object to one compacted and ready for
  marshalling or use.
- Correct Python 3.6+ findlinestarts() and findlabels() methods
- Fix _unpack_opargs_wordcode in 3.6
- DRY opcodes more
- Add marshal types that have appeared since Python 3.4 and
  start to implement. More work is needed here.


3.4.0 2017-06-25
=====================

- Add functions in xdis.bytecode:
  has_argument()_, next_offset(), and op_size() functions to
- work with fixed (3.6+) and variable-length (pre 3.6) instructions
- Add magic for pypy3.5

3.3.1 2017-05-18 - Lewis
=====================

Python 3.6 bugs/features
- Fix bug in handling operand of opcode after EXTENDED_ARG
- A general mechanism to handle formatting of instruction operands and use
  that on Python 3.6+ opcode MAKE_FUNCTION FORMAT_VALUE
- Add missing SETUP_ASYNC_WITH opcode
- Test 3.6 on Travis CI
- compile() return value, "code" no longer has a len. Use "code.co_code"

3.3.0 2017-03-18
=====================

- Start supporting Python 3.x dis API functions
  This is largely due to Daniel Bradburn (moagstar)
- Expanded tests, bug fixes, and bug fixes for various versions of Python
  This is largely due to Kirill Spitsyn

3.2.4 2016-12-16
=====================

- add magic for 3.6rc
- Fix Python 3.6 disaseembly of CALL_FUNCTION_EX
- Make magic string values unique
- Note we can now handle Python 2.4 and 2.5

3.2.3 2016-11-6
=====================

- Correct Python 3.0 bytecodes
- Go over other opcodes and add stack manipulation entries.  For
  example, for LIST_APPEND.

3.2.2 2016-11-02
=====================

- Distrbute COPYING.txt
- Correct pypy 3.2 bytecode
- Start adding stack use on opcodes for Python 3.x

- add stack use for Python 2 and Python3 opcodes (incomplete)

3.2.1 2016-10-30
=====================

- Tag pypy 2.6 and 2.7 LOOKUP_METHOD properly
  (bug introduced in 3.2.0. Thanks to alexwlchan of the hypothesis team.)
- Clarification of EXTENDED_ARG in 3.0 and 3.1
- disassemble output size indicates bytes explicitly

3.2.0 2016-10-25
=====================

- Python 3.1 EXTENDED_ARG opcode bug fix
- Python 3.0 opcode fixes
- DRY opcode files
- start noting stack-modification attributes on opcodes and
  use for Python 2.4-2.7
- Remove hasAgumentExtended. It's not used.
- Update Python 3.6 opcodes
- Add magic number for Python 3.6.0b2
- On disassembly Python 3.6 no longer knows what's up in CALL_FUNCTION
- Add Python 2.1 and 3.1 bytecode tests
- Add list2bytecode() and write_bytecode_file() -
  First steps in handling bytecode assembly
- Change licence to GPL 2.0

3.1.0 2016-10-15
=====================

- expose findlabels, and findlinestarts,
- add offset2line routine to give line number for a given offset
- clean up requirements.txt and setup.py

3.0.2 2016-10-09
=====================

- Fix Python 1.5 disassembly bugs
- Add Python 1.3 and 1.4 magics

3.0.1 2016-10-09
=====================

- botched classification of FOR_LOOP in Python 1.5

3.0.0 2016-10-09
=====================

- load_module returns source-code size now.
  This is incompatible with previous (2.x) versions

- add parameter in load_module to omit parsing code,
  just other info (source-code-size, timestamp, magic, etc)

- Disassemble 1.5 bytecodes and test

- fix some Python 1.5 and 2.0 bytecode bugs

2.3.2 2016-10-06
=====================

- Start adding Python 1.5 and 2.0, and 2.1 opcodes
- Disassemble dropbox 2.5
- correct pydisasm name in --help

2.3.1 2016-09-11
=====================

- Add Dropbox magic numbers.
  Decode dropbox's 2.5 bytecode via code (on Python 2.x)
  from https://github.com/rumpeltux/dropboxdec

2.2.3 2016-08-29
=====================

- Fix Python 3.1 opcode bugs

2.2.2 2016-08-26
=====================

- Add Python 3.6 opcodes since 3.6.0.a1
- magics.versions has more detailed version information, e.g. 62121 is 2.5c1
- Add format conversion type (!r, !s, !a) in 3.6 FORMAT_VALUE attribute
- We no longer support Python 3.6.0a1 but only 3.6.0a3
- Update opcode history

2.2.1 2016-08-14
=====================

- Fix 3.6 arg parsing in wordcode
- PyPy 2.7 LOAD_ATTR wasn't marked as a name op
- add python_version attribute to opc
- Doc corrections

2.2.0 2016-08-05
=====================

- Add Python 2.2 bytecodes
- Show Python magic number in disassembly output
- Show compile flags in hex and in proper bit order

2.1.0 2016-07-26
=====================

- better opcode classification hasvargs for non-function calls, e.g. BUILD
- Support 3.6 wordcode

2.0.3 2016-07-26
=====================

- Small instruction print change

2.0.2 2016-07-25
=====================

- Fix some PyPy op classification bugs

2.0.1 2016-07-24
=====================

- PyPy bug fixes. (More probably to come.)
  * pypy 3.x opcodes need to be their own thing
  * classify LOOKUP_METHOD and CALL_METHOD
    (probably will need to classify others too)
  * some PyPy testing tolerance

2.0.0 2016-07-24
=====================

- Support PyPy 2.x and 3.x
  * load() now returns whether we've loaded PyPy. This is an incompatible change
  * added is_pypy(magic_int)

- Support Python 3.6

- Remove uncompyle6's JA and JF: Use standard JUMP_ABSOLUTE and
  JUMP_FORWARD.

- Instructions store whether they have an argument

1.1.7 2016-07-09
=====================

- Fix bug in 2.4 complex type unmarshalling

1.1.6 2016-07-08
=====================

- Fix More Python 2.4 bugs

1.1.5 2016-07-08
=====================

- Add Python 2.4 jrel, jabs sets

1.1.4 2016-07-07
=====================

-  Correct bad python 3.3 magic number

1.1.3 2016-06-27
=====================

- Bug - Python < 2.7 JUMP_IF_{TRUE,FALSE} are
  relative jumps, not absolute

1.1.2 2016-06-24
=====================

- Bug - Python 2.4-2.6 LIST_APPEND doesn't take an extended arg

1.1.1 2016-06-3
=====================

- opcode 2.3 fixes

1.1.0 2016-05-31 Mom
=====================

- Expose needed opcode values and bug fixes
- drop support for running on Python 2.5

1.0.5 2016-05-29
=====================

For Python 2.3-2.5 add pseudo opcodes PJIF PJIT JA
This simplifies code in cross-version tools like uncompyle6

1.0.4 2016-05-28
=====================

Small omissions found by uncompyle6

- export findlinestarts
- correct pydisassemble.py imports
- add 2.4, 2.5 hasArgumentExtended
- add hasjrel, and hasjabs
- Add JUMP_OPs and JPIF, JPIT, JA, JF

1.0.1-1.0.3 2016-05-27
=====================

Minor fixes

- small bugs and make more usable in uncompyle6

1.0.0 2016-05-26 First release
=====================

- Reduce redundancy in opcodes
- Use 3.5.1 disassembly format
- Start to roll in PYPY marshal routines
- support PYPY and be able to run under
  Python 2.5 - 3.5 with opcodes going back to 2.3

See uncompyle6 for past releases/history
