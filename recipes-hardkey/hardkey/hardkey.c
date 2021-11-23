#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <linux/input.h>
#include <string.h>
#include <sys/time.h>

void write_key_event(int code, int value)
{
    struct input_event key_event;
  
    gettimeofday(&key_event.time, NULL);
    key_event.type  = EV_KEY;
    key_event.code  = code;
    key_event.value = value;
    write(1, &key_event, sizeof(key_event));
}

int main(int argc, char *argv[])
{
    int keycode = KEY_WIMAX;
    int value = 0;

    if (argc < 3) return EXIT_FAILURE;

    value = atoi(argv[2]);

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

    write_key_event(keycode, value);

    exit(EXIT_SUCCESS);
}
