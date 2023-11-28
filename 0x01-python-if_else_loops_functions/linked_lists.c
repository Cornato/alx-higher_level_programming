#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - print_listint
 * @h: pointer
 * Return: number
 */
size_t print_listint(const listint_t *h)
{
	const listint_t *curr;
	unsigned int n;

	curr = h;
	n = 0;
	while (curr != NULL)
	{
		printf("%i\n", curr->n);
		curr = curr->next;
		n++;
	}

	return (n);
}

/**
 * add_nodeint_end - add_nodeint_end
 * @head: pointer
 * @n: num
 * Return: 0
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
	listint_t *nas;
	listint_t *cur;

	cur = *head;

	nas = malloc(sizeof(listint_t));
	if (nas == NULL)
		return (NULL);

	nas->n = n;
	nas->next = NULL;

	if (*head == NULL)
		*head = nas;
	else
	{
		while (cur->next != NULL)
			cur = cur->next;
		cur->next = nas;
	}

	return (nas);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
	listint_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}
