/*
**    blink.c -    blink gpiochip0 line 3 with delay given by either
**                 the command line or the default (NSPERIOD)
*/

#include <stdio.h>
#include <unistd.h>
#include <gpiod.h>

#define NSPERIOD    200000000ULL    /* output period in ns */

int 
main(int argc, char *argv[])
{
    struct gpiod_chip *output_chip;
    struct gpiod_line *output_line;
    struct timespec delay = {0, NSPERIOD};
    struct timespec rem;
    int line_value = 0;
    int ret = 0;

    if (argc == 2)
        delay.tv_nsec = atoll(argv[1]);

    /* open /dev/gpiochip0 */
    output_chip = gpiod_chip_open_by_number(0);
    if(output_chip == NULL)
    {
	printf("gpiod_line_request_output ret=%d\n", ret);
	return -1;
    }
    
    /* work on pin 3 */
    output_line = gpiod_chip_get_line(output_chip, 3);
    if(output_line == NULL)
    {
	printf("gpiod_chip_get_line ret=%d\n", ret);
	return -1;
    }

    /* config as output and set a description */
    ret = gpiod_line_request_output(output_line, "blink", GPIOD_LINE_ACTIVE_STATE_HIGH);
	printf("gpiod_line_request_output ret=%d\n", ret);

    for (int i = 0; i < 10; i++)
    {
        line_value = !line_value;
        ret = gpiod_line_set_value(output_line, line_value); 
	printf("gpiod_line_set_value ret=%d\n", ret);
	nanosleep(&delay, &rem);
    }
    gpiod_line_release(output_line);
    gpiod_chip_close(output_chip);
    
    return 0;
}

