#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - runs forever
 * Return: 0
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - entry point
 * Return: 0
 */

int main(void)
{
	int	child;
	pid_t	pid;

	child = 0;
	while (child < 5)
	{
		pid = fork();
		if (!pid)
			break;
		printf("Zombie process created, PID: %i\n", (int)pid);
		child++;
	}
	infinite_while();
	return (0);
}
