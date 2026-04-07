(base) madsottendal@MacBook-Pro-tilhrende-Mads-2 09_software_security_iii % ./address AAAAAAAAAAAAAAA BBBBBBBBBBBBBBB
What's your name?
jimothy
============== Moin jimothy ==============
Do you like pointers?
no
WTF???
address(35636,0x1fba23100) malloc: *** error for object 0x16bad2334: pointer being freed was not allocated
address(35636,0x1fba23100) malloc: *** set a breakpoint in malloc_error_break to debug
zsh: abort      ./address AAAAAAAAAAAAAAA BBBBBBBBBBBBBBB
(base) madsottendal@MacBook-Pro-tilhrende-Mads-2 09_software_security_iii % ./address_asan AAAAAAAAAAAAAAA BBBBBBBBBBBBBBB
What's your name?
himothy
=================================================================
==35901==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x6020000000d4 at pc 0x000102c45b78 bp 0x00016d71a150 sp 0x00016d719900
WRITE of size 5 at 0x6020000000d4 thread T0
    #0 0x102c45b74 in strcpy+0x510 (libclang_rt.asan_osx_dynamic.dylib:arm64e+0x4db74)
    #1 0x1026e6da0 in hello address.c:21
    #2 0x1026e779c in main address.c:69
    #3 0x18f395d50  (<unknown module>)

0x6020000000d4 is located 0 bytes after 4-byte region [0x6020000000d0,0x6020000000d4)
allocated by thread T0 here:
    #0 0x102c4cc04 in malloc+0x94 (libclang_rt.asan_osx_dynamic.dylib:arm64e+0x54c04)
    #1 0x1026e6d90 in hello address.c:19
    #2 0x1026e779c in main address.c:69
    #3 0x18f395d50  (<unknown module>)

SUMMARY: AddressSanitizer: heap-buffer-overflow (libclang_rt.asan_osx_dynamic.dylib:arm64e+0x4db74) in strcpy+0x510
Shadow bytes around the buggy address:
  0x601ffffffe00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x601ffffffe80: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x601fffffff00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x601fffffff80: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x602000000000: fa fa fd fa fa fa fd fd fa fa fd fd fa fa 00 06
=>0x602000000080: fa fa 00 fa fa fa 00 00 fa fa[04]fa fa fa fa fa
  0x602000000100: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x602000000180: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x602000000200: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x602000000280: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x602000000300: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
==35901==ABORTING
zsh: abort      ./address_asan AAAAAAAAAAAAAAA BBBBBBBBBBBBBBB
(base) madsottendal@MacBook-Pro-tilhrende-Mads-2 09_software_security_iii % ./thread 10000 40
there are 1186 primes up to 10000
(base) madsottendal@MacBook-Pro-tilhrende-Mads-2 09_software_security_iii % ./thread_tsan 10000 40
==================
WARNING: ThreadSanitizer: data race (pid=36625)
  Read of size 8 at 0x00016b25a2d0 by thread T3:
    #0 thread_function thread.c:33 (thread_tsan:arm64+0x1000039d8)

  Previous write of size 8 at 0x00016b25a2d0 by thread T2 (mutexes: write M0):
    #0 thread_function thread.c:36 (thread_tsan:arm64+0x100003a04)

  Location is stack of main thread.

  Mutex M0 (0x00016b25a2d8) created at:
    #0 pthread_mutex_init <null>:124789328 (libclang_rt.tsan_osx_dynamic.dylib:arm64e+0x3181c)
    #1 main thread.c:60 (thread_tsan:arm64+0x100003b54)

  Thread T3 (tid=5589825, running) created by main thread at:
    #0 pthread_create <null>:124789328 (libclang_rt.tsan_osx_dynamic.dylib:arm64e+0x309d8)
    #1 main thread.c:69 (thread_tsan:arm64+0x100003bc8)

  Thread T2 (tid=5589824, finished) created by main thread at:
    #0 pthread_create <null>:124789328 (libclang_rt.tsan_osx_dynamic.dylib:arm64e+0x309d8)
    #1 main thread.c:69 (thread_tsan:arm64+0x100003bc8)

SUMMARY: ThreadSanitizer: data race thread.c:33 in thread_function
==================
there are 1229 primes up to 10000
ThreadSanitizer: reported 1 warnings
zsh: abort      ./thread_tsan 10000 40
(base) madsottendal@MacBook-Pro-tilhrende-Mads-2 09_software_security_iii % ./undefined 36 6
36
6
no overflow happened :)
42
success
p = 0x16d3c21c0
s = 328350
(base) madsottendal@MacBook-Pro-tilhrende-Mads-2 09_software_security_iii % ./undefined_ubsan 36 6
36
6
no overflow happened :)
42
success
p = 0x16d6f6180
s = 328350