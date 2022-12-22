### The dual algorithm for the minimum-cost flow problem

##### The minimum-cost flow problem aims to find the cheapest possible way of sending a certain amount of flow through a flow network.

| Variables   | Meaning                                                      |
| ----------- | ------------------------------------------------------------ |
| network     | The flow network, {node1: {node2: [capacity, cost], node3: [capacity, cost], ...}, ...} |
| source      | The source node                                              |
| destination | The destination node                                         |
| f           | The pre-defined amount of flow                               |
| nn          | The number of nodes                                          |
| dis         | List, dis[i\]\[j\] denotes the length of the shortest path from node i to node j |
| path        | List, path\[i\]\[j\] denotes the shortest path from node i to node j |
| flow        | A feasible flow from the source to the destination           |

#### Example

![minimum-cost flow problem example](C:\Users\dell\Desktop\研究生\个人算法主页\The dual algorithm for the minimum-cost flow problem\minimum-cost flow problem example.png)

```python
if __name__ == '__main__':
    test_network = {
        0: {1: [10, 4], 2: [8, 1]},
        1: {3: [2, 6], 4: [7, 1]},
        2: {1: [5, 2], 3: [10, 3]},
        3: {4: [4, 2]},
        4: {},
    }
    s = 0
    d = 4
    f = 10
    print(main(test_network, s, d, f))
```

##### Output

```python
48
```

