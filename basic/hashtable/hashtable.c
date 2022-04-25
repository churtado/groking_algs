#define MULTIPLIER (37)
#include "hashtable.h"
#include <stdio.h>
#include <stdlib.h>

unsigned long hash(const char *s) {
  unsigned long h;
  unsigned const char *us;

  /* cast s to unsigned const char * */
  /* this ensures that elements of s will be treated as having values >= 0 */
  us = (unsigned const char *)s;
  h = 0;
  while (*us != '\0') {
    h = h * MULTIPLIER + *us;
    us++;
  }
  return h;
}

unsigned long position(char *str) { return hash(str) % HSIZE; }

typedef struct node {
  char *value;
  struct node *next;
} hash_node;

void add(hash_node **array, char *str) {
  unsigned long pos = position(str);

  // is the entry in the table null?
  if (!array[pos]) {
    hash_node *new_node = (hash_node *)malloc(sizeof(hash_node));
    new_node->value = str;
    new_node->next = NULL;
    array[pos] = new_node;
  } else {
    hash_node *current = array[pos];
    while (current->next) {
      current = current->next;
    }
    current->next = (hash_node *)malloc(sizeof(hash_node));
    current->next->next = NULL;
    current->next->value = str;
  }
}

int main() {
  hash_node *table[HSIZE];
  int counts[HSIZE];
  int i = 0;
  for (i = 0; i < HSIZE; i++) {
    table[i] = NULL;
    counts[i] = 0;
  }

  // testing it out
  int length = 0;
  char *snum = NULL;
  for (i = 0; i < 400; i++) {
    length = snprintf(NULL, 0, "%d", i);
    snum = malloc(length + 1);
    snprintf(snum, length + 1, "%d", i);
    add(table, snum);
    // printf("hash@%lu => %s\n", position(snum), table[position(snum)]->value);
    counts[position(snum)]++;
    if (counts[position(snum)] > 1) {
      printf("collision@%lu->%d\n", position(snum), counts[position(snum)]);
    }
  }
  free(snum);
  return 0;
}
