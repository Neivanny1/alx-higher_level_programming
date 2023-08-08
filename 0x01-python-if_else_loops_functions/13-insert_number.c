#include"lists.h"

listint_t *insert_node(listint_t **head, int number) {
    listint_t *new_node, *current, *prev;

    /* Create a new node */
    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return NULL;

    new_node->n = number;
    new_node->next = NULL;

    /* Handle the case when the list is empty */
    if (*head == NULL) {
        *head = new_node;
        return new_node;
    }

    /* Traverse the list to find the right position to insert the number */
    current = *head;
    prev = NULL;
    while (current != NULL && current->n < number) {
        prev = current;
        current = current->next;
    }

    /* Insert the new node at the right position */
    if (prev == NULL) {
        new_node->next = *head;
        *head = new_node;
    } else {
        new_node->next = current;
        prev->next = new_node;
    }

    return (new_node);
}
