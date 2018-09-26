// Compile with -lpthread i.e. gcc scheduler_test.c -lpthread
#define _GNU_SOURCE
#include <sched.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <pthread.h>
#include <error.h>
#include <signal.h>

#define NSEC_PER_SEC 1000000000

pthread_t test_task;

// using clock_nanosleep of librt
extern int clock_nanosleep(clockid_t __clock_id, int __flags, __const struct timespec *__req, struct timespec *__rem);

static inline void tsnorm (struct timespec *ts) {
  while (ts->tv_nsec >= NSEC_PER_SEC) {
    ts->tv_nsec -= NSEC_PER_SEC;
    ts->tv_sec++;
  }
}


static void *test_loop(void *args) {
  struct timespec now,next;
  float current_time, previous_time, diff_time,prev_print_time=0;
  float act_cycle_time;
  float min_cycle_time = 999999, max_cycle_time = 0, avg_cycle_time = 0, sum_cycle_time = 0;
  int cycle_count = 0;

  int cycle_time_ns = 50000;//50us

  printf("Test Loop entered!\n\r");
    clock_gettime(CLOCK_MONOTONIC, &now);
    current_time = (float)now.tv_nsec/1000000.0;
    previous_time = current_time;

    clock_gettime(CLOCK_MONOTONIC, &next);
  while(1)
  {
    //usleep(1000);
    /*next.tv_nsec += cycle_time_ns;
    tsnorm(&next);
    clock_nanosleep(0, TIMER_ABSTIME, &next, NULL);*/

    cycle_count++;
    clock_gettime(CLOCK_MONOTONIC, &now);
    current_time = (float)now.tv_nsec/1000000.0;
    if (current_time < previous_time) previous_time -= 1000;
    if (current_time < prev_print_time) prev_print_time -= 1000;
    diff_time = current_time - previous_time;
    act_cycle_time = diff_time;
    if (act_cycle_time < min_cycle_time) min_cycle_time = act_cycle_time;
    if (act_cycle_time > max_cycle_time) max_cycle_time = act_cycle_time;
    sum_cycle_time += act_cycle_time;
    avg_cycle_time = sum_cycle_time/((float)cycle_count);
    //if (cycle_count % 100 == 0)
    if (current_time > prev_print_time + 100) {
      printf("cycle:%d ptime:%.5f ctime:%.5f act:%.5f min:%.5f avg:%.5f max:%.5f\n\r",cycle_count,previous_time, current_time,act_cycle_time,min_cycle_time,avg_cycle_time,max_cycle_time);
      prev_print_time = current_time;
    }
    previous_time = current_time;
  }
}

static void setup_sched_params(pthread_attr_t *attr, int priority) {
  struct sched_param p;
  int ret;

  ret = pthread_attr_init(attr);
  if (ret)
    error(1, ret, "pthread_attr_init()");

  ret = pthread_attr_setinheritsched(attr, PTHREAD_EXPLICIT_SCHED);
  if (ret)
    error(1, ret, "pthread_attr_setinheritsched()");

  ret = pthread_attr_setschedpolicy(attr, priority ? SCHED_FIFO : SCHED_OTHER);
  if (ret)
    error(1, ret, "pthread_attr_setschedpolicy()");

  p.sched_priority = priority;
  ret = pthread_attr_setschedparam(attr, &p);
  if (ret)
    error(1, ret, "pthread_attr_setschedparam()");
}

int main (void) {
  pthread_attr_t tattr;
  cpu_set_t cpus;
  int cpu=2;// cpu id to run this process on (0=CPU1)

  sigset_t mask;
  int ret, sig;
  sigemptyset(&mask);
  sigaddset(&mask, SIGINT);
  sigaddset(&mask, SIGTERM);
  sigaddset(&mask, SIGHUP);
  sigaddset(&mask, SIGALRM);
  //pthread_sigmask(SIG_BLOCK, &mask, NULL);

  setup_sched_params(&tattr, 90);
  CPU_ZERO(&cpus);
  CPU_SET(cpu, &cpus);
  ret = pthread_attr_setaffinity_np(&tattr, sizeof(cpus), &cpus);
  if (ret)
    error(1, ret, "pthread_attr_setaffinity_np()");

  ret = pthread_create(&test_task, &tattr, test_loop, NULL);
  if (ret)
    error(1, ret,  "pthread_create(display)");

  pthread_attr_destroy(&tattr);

  //__STD(sigwait(&mask, &sig));

  while (1)
    usleep(1000);

  return 0;
}
