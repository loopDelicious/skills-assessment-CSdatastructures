# Part i

# Runtime
# When calculating the Big O notation for a particular algorithm, it’s necessary to consider the length of time it takes 
# for the algorithm to run as the algorithm’s workload approaches the size of infinity. 
# What is the workload of a function that takes in a list of integers and returns a new list of the even integers?
        # new_list = []
        # for item in list:
        #     if item % 2 == 0:
        #         new_list.append(item)
        # O(n) - linear, must run through every item in the list

# Order the following runtimes in ascending order by efficiency as n approaches infinity:
        # O(2^n) - exponential
        # O(n^2) - quadratic
        # O(n log n) - log
        # O(n) - linear
        # O(log n) - log
        # O(1) - constant

# Stacks and Queues
# In the following cases, would a stack or queue be an appropriate data structure?
# The process of loading and unloading pallets onto a flatbed truck
        # Stack (LIFO)
# Putting bottle caps on bottles of beer as they roll down an assembly line
        # QUEUE (FIFO)
# Calculating the solution to this mathematical expression: 2 + (7 * 4) - (3 / 2)
        # Stack (LIFO)
# Describe 2 more examples of when a queue would be an appropriate data structure.
        # Waiting in line at a bank (FIFO), first customer to arrive in line gets helped first
        # Breadth-first search of a tree - pop off and search the first item in the list 
# Describe 2 more examples of when a stack would be an appropriate data structure.
        # Stack of pancakes (LIFO), last pancake placed on the plate gets eaten first
        # Depth-first search of a tree - pop off and search the last item in the list

# Linked Lists
# Given the below linked list, which are the nodes? What is the data for each node? 
# Where is the head? Where is the tail? (Please be as specific as possible — exactly 
#     which parts of the diagram correspond to each part? Arrows? Boxes? Text?)
        # The nodes are the boxes that contain data and pointers.  The data is "Apple",
        # "Berry", "Cherry". The head is the first node (linked list named LLIST).  The 
        # tail is the last node ("Cherry" that points to None). 
# What’s the difference between a doubly and singly linked list?
        # In a singly linked list, every node has a pointer that points to the node directly
        # following.  In a doubly linked list, every node has pointers pointing to the nodes
        # directly preceding and following.
# Why is it faster to append to a linked list if we keep track of the tail as an attribute?
        # If we know which node is the tail, we can append to the end immediately.  If we aren't sure
        # which node is the tail, we must loop through every node to see which one points to None (tail).

# Trees
# Given the above tree, in what order would a Breadth First Search (BFS) algorithm visit each node 
# until finding burrito (starting at food)?
        # BFS works like a queue and searches the first item in the list first.  The nodes would be 
        # searched in this order: start with [food], not there so add children [italian, indian, mexican],
        # pop italian, not burrito so add italian's children [indian, mexican, lasagna, pizza], pop indian, not 
        # burrito so add indian's children [mexican, lasagna, pizza, tikka, saag], pop mexican, not burrito
        # so add mexican's children [lasagna, pizza, tikka, saag, burritos, tacos, enchiladas], pop lasagna, not 
        # burrito so add lasagna's children (None), pop pizza, not burrito, so add pizza's children [tikka, saag,
        # burrittos, tacos, enchiladas, thin, chicago, NY, sicilian], pop tikka (no children), pop saag (no children),
        # pop burrito (burrito found!)
# Given the above tree, in what order would a Depth First Search algorithm visit each node until 
# finding Chicago-style (starting at food)?
        # DFS works like a stack and searches the last item in the list first.  The nodes would be searched
        # in this order:  start with [food], not there so add children [italian, indian, mexican], pop mexican, not 
        # burrito so add mexican's children [italian, indian, burrito, tacos, enchiladas], pop enchiladas (no children),
        # pop tacos (no children), pop burrito (burrito found!)
# How is a binary search tree different from other trees?
        #  In a binary search tree, all nodes to the left of each node is < the current node, and all
        # nodes to the right of each node is > the current node. 

        
