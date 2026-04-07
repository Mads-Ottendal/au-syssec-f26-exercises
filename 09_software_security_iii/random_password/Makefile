CC = afl-clang-fast
CFLAGS = -g -O0 -Wall -Wextra

SDK := $(shell xcrun --sdk macosx --show-sdk-path)

.PHONY: clean

random_password: random_password.c
	$(CC) $(CFLAGS) -isysroot $(SDK) -o random_password random_password.c

clean:
	rm -f random_password