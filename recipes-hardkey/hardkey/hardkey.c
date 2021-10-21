#include <stdio.h>
#include <stdlib.h>
#include <linux/input.h>
#include <sys/time.h>

void write_key_event(int code, int value, int fd)
{
  struct input_event key_event;
  
  gettimeofday(&key_event.time, NULL);
  key_event.type  = EV_KEY;
  key_event.code  = code;
  key_event.value = value;
  write(fd, &key_event, sizeof(key_event));
}

int main(void)
{
  write_key_event(KEY_F9, 1, 1);
  write_key_event(KEY_F9, 0, 1);

  exit(EXIT_SUCCESS);
}
