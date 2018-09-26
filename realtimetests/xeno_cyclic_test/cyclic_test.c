#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <sys/mman.h>
#include <alchemy/task.h>
#include <alchemy/timer.h>
#include <math.h>


#define CLOCK_RES 1e-9 //Clock resolution is 1 ns by default
#define LOOP_PERIOD 1e7 //Expressed in ticks
//RTIME period = 1000000000;
RT_TASK loop_task;
cpu_set_t cpus;

void loop_task_proc(void *arg)
{
  RT_TASK *curtask;
  RT_TASK_INFO curtaskinfo;
  int iret = 0;

  RTIME tstart, tnow, tlast, tdiff, tdlast;
  int tlat;

  curtask = rt_task_self();
  rt_task_inquire(curtask, &curtaskinfo);
  int ctr = 0;

  //Print the info
  printf("Starting task %s with period of 10 ms ....\n", curtaskinfo.name);

  //Make the task periodic with a specified loop period
  rt_task_set_periodic(NULL, TM_NOW, LOOP_PERIOD);

  tstart = rt_timer_read();

  //Start the task loop
  while(1){
    tnow = rt_timer_read();
    tdiff = (tnow - tlast);
    tlat = tdiff - tdlast;
    printf("Loop count: %d, Loop time: %.5f ms, Latency: %.5f us\n", ctr, tnow/1000000.0, tlat/1000.0);
    ctr++;
    tlast = tnow;
    tdlast = tdiff;
    rt_task_wait_period(NULL);
  }
}

int main(int argc, char **argv)
{
  char str[20];

  //Lock the memory to avoid memory swapping for this program
  mlockall(MCL_CURRENT | MCL_FUTURE);

  printf("Starting cyclic task...\n");

  //Create the real time task
  sprintf(str, "cyclic_task");
  rt_task_create(&loop_task, str, 0, 99, 0);

  /* Set cpu affinity;
     Edit /etc/default/grub to change the line:
        GRUB_CMDLINE_LINUX="isolcpus=6,7"
     then run update-grub
  */
  CPU_ZERO(&cpus);
  CPU_SET(7,&cpus);
  rt_task_set_affinity(&loop_task, &cpus);

  //Since task starts in suspended mode, start task
  rt_task_start(&loop_task, &loop_task_proc, 0);

  //Wait for Ctrl-C
  pause();

  return 0;
}
