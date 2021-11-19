#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <linux/input.h>
#include <string.h>
#include <linux/types.h>
#include <linux/input-event-codes.h>
#include <sys/time.h>

enum key_value {
    RELEASE = 0,
    PUSH    = 1,
    REPEAT  = 2,

};

static void write_key_event(__u16 code, __u16 value)
{
    struct input_event key_event = {0};
  
    gettimeofday(&key_event.time, NULL);
    key_event.type  = EV_KEY;
    key_event.code  = code;
    key_event.value = value;
    write(1, &key_event, sizeof(key_event));
}

int main(int argc, char *argv[])
{
    __u16 keycode = KEY_WIMAX;

    printf("keycode=%s value=%s\n", argv[1], argv[2]);

    if (argc < 3) return EXIT_FAILURE;

    if ( strcmp(argv[1], "KEY_F9") == 0 )
        keycode = KEY_F9;
    else if ( strcmp(argv[1], "KEY_F1") == 0 )
        keycode = KEY_F1;
    else if ( strcmp(argv[1], "KEY_F2") == 0 )
        keycode = KEY_F2;
    else if ( strcmp(argv[1], "KEY_F7") == 0 )
        keycode = KEY_F7;
    else if ( strcmp(argv[1], "KEY_F8") == 0 )
        keycode = KEY_F8;
    else if ( strcmp(argv[1], "KEY_F10") == 0 )
        keycode = KEY_F10;
    else if ( strcmp(argv[1], "KEY_F11") == 0 )
        keycode = KEY_F11;
    else if ( strcmp(argv[1], "KEY_F12") == 0 )
        keycode = KEY_F12;
    else if ( strcmp(argv[1], "KEY_PAUSE") == 0 )
        keycode = KEY_PAUSE;
    else
        return EXIT_FAILURE;

    write_key_event(keycode, PUSH);

    exit(EXIT_SUCCESS);
}
