#!/usr/bin/python
"""Computes the smallest number of edges that need to be added to an adjacency list to complete a tree."""

import sys

argc = len(sys.argv)
data_file_loc = "test_data"
usage = """tree.py [data file]
Computes the smallest number of edges that need to be added to an adjacency l
ist to complete a tree."""

def num_trees(adjacencies, field):
    trees = []
    for adjacency in adjacencies:
        if adjacency[0] not in field or adjacency[1] not in field:
            tree_ptr1 = None
            tree_ptr2 = None
            for tree in trees:
                if adjacency[0] in tree:
                    tree_ptr1 = tree
                if adjacency[1] in tree:
                    tree_ptr2 = tree
            if tree_ptr1 == tree_ptr2:
                print("cycle found")
                continue
            if tree_ptr1 and tree_ptr2:
                for thing in tree_ptr2:
                    tree_ptr1.append(thing)
                trees.remove(tree_ptr2)
            elif tree_ptr1:
                tree_ptr1.append(adjacency[1])
                field.remove(adjacency[1])
            elif tree_ptr2:
                tree_ptr2.append(adjacency[0])
                field.remove(adjacency[0])
        else:
            trees.append([adjacency[0], adjacency[1]])
            field.remove(adjacency[0])
            field.remove(adjacency[1])
    return len(trees) + len(field) - 1

if __name__ == "__main__":
    if argc > 2:
        print(usage)
        sys.exit(1)
    if argc == 2:
        data_file_loc = sys.argv[1]
    try:
        data_file = open(data_file_loc)
        nodes = range(1, int(data_file.readline()) + 1)
        adjacency_list = []
        for line in data_file:
            adjacency_list.append((int(line.split()[0]), int(line.split()[1])))
        data_file.close()
    except IOError, error:
        print(usage)
        print(error)
        sys.exit(1)
    except ValueError:
        print("Malformed data file")
        sys.exit(1)
    print(num_trees(adjacency_list, nodes))
