#include "lists.h"
#include <stdlib.h>

/**
  * insert_node: Insert a node into a sorted singly linked list
  * @head: A pointer to head pointer of the singly linked list
  * @number: Number to store in the node
  * Return: Pointer to the new node, or NULL if it failed
  */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *current = *head, *previous, *new;

    /* Create a new node that stores @number */
    new = malloc(sizeof(listint_t));
    if (!new)
    {
        free(new);
        return (NULL);
    }
    new->n = number;

    /* If number is smallest, insert at the beginning */
    if (!(*head) || current->n > number)
    {
        *head = new;
        new->next = current;
        return (new);
    }

    /* Insert node at its corresponding location */
    while (current)
    {
        if (current->n > number)
        {
            new->next = current;
            previous->next = new;
            return (new);
        }
        previous = current;
        current = current->next;
    }

    /* If number is largest, insert at end */
    new->next = NULL;
    previous->next = new;
    return (new);
}
