#include "lists.h"

/**
  * is_palindrome - Check if a singly linked list is palindrome
  * @head: Pointer to head pointer of singly linked list
  * Return: 1 if the list is palindrome, or 0 if it is not
  */
int is_palindrome(listint_t **head)
{
	listint_t *start = *head, *tail = *head;
	int start_index, tail_index, length = 0;

	/* Empty list is considered palindorme */
	if (!start)
	{
		return (1);
	}
	/* Calculate list length */
	while (tail != NULL)
	{
		tail = tail->next;
		length++;
	}
	/* Point tail to the first node in the second-half of the list */
	tail = *head;
	tail_index = (length + 1) / 2;
	start_index = tail_index;
	while (start_index--)
	{
		tail = tail->next;
	}
	/* Compare corresponding nodes in first and second half of the list */
	while (tail != NULL)
	{
		start_index = (length - 1) - tail_index;
		while (start_index--)
		{
			start = start->next;
		}
		if (start->n != tail->n)
		{
			return (0);
		}
		tail = tail->next;
		tail_index++;
		start = *head;
	}
	return (1);
}
