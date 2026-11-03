Water Jug Problem – Artificial Intelligence

Aim

To solve the Water Jug Problem using Artificial Intelligence and demonstrate how a goal state can be reached from an initial state using valid operations.

Problem Statement

We are given two water jugs:

- A 4-litre jug
- A 3-litre jug

Initially, both jugs are empty. The objective is to measure exactly 2 litres of water using only the two jugs.

Operations

The following operations can be performed:

1. Fill a jug completely.
2. Empty a jug completely.
3. Pour water from one jug into another until the source jug is empty or the destination jug is full.

State Representation

A state is represented as:

"(x, y)"

Where:

- "x" = amount of water in the 4-litre jug
- "y" = amount of water in the 3-litre jug

Initial State: "(0, 0)"

Goal State: "(2, 0)" or any state containing exactly 2 litres.

Solution

The following sequence reaches the goal state:

Step| 4-Litre Jug| 3-Litre Jug| Operation
1| 0| 0| Initial State
2| 0| 3| Fill 3-litre jug
3| 3| 0| Pour 3-litre jug into 4-litre jug
4| 3| 3| Fill 3-litre jug
5| 4| 2| Pour water into 4-litre jug until full
6| 0| 2| Empty 4-litre jug
7| 2| 0| Pour 2 litres into 4-litre jug

Algorithm

1. Start with both jugs empty.
2. Fill the 3-litre jug.
3. Pour its contents into the 4-litre jug.
4. Fill the 3-litre jug again.
5. Pour water into the 4-litre jug until it becomes full.
6. Empty the 4-litre jug.
7. Transfer the remaining 2 litres into the 4-litre jug.
8. Stop when the goal state is reached.

Result

The Water Jug Problem is successfully solved by applying state-space search and valid water-transfer operations. Exactly 2 litres of water are measured.

Concepts Used

- Artificial Intelligence
- State Space Representation
- Initial State and Goal State
- Production Rules
- Search Algorithms
