#include "lists.h"

/**
  * check_cycle - Check if a singly linked list has a cycle in it
  * @list: Head pointer to singly linked list
  * Return: 1 if there is a cycle, or 0 if there is no cycle
  */
int check_cycle(listint_t *list)
{
	listint_t *current = list;

	while (current != NULL)
	{
		if (current->next == list)
		{
			return (1);
		}
		current = current->next;
	}
	return (0);
}
