# ReplicaLoop.
# ReplicaLoop

**ReplicaLoop** is an educational Python project demonstrating the concept of **self-replication**.

> **Important:** This project is a controlled simulation. It must use a fixed replication limit and should not be modified to continuously consume disk space, memory, processes, or other system resources.

## What It Demonstrates

ReplicaLoop demonstrates how a program can:

* Locate its own source file.
* Create copies of that file.
* Repeat the operation a controlled number of times.
* Stop automatically after reaching a safety limit.

## Example

The demonstration can be configured with a limit such as:

```python
MAX_COPIES = 4
```

The program then creates four copies and stops.

## Terminology

This behavior is commonly described as **self-replication**.

A malicious program that uses uncontrolled replication to exhaust storage or other resources can be considered a **resource-exhaustion attack** or, depending on its implementation, a type of **self-replicating malware**.

ReplicaLoop itself is intended only as a programming and security-learning demonstration.

## Safety

Do not configure the program for unlimited real file creation or process creation. An uncontrolled loop can consume available disk space or system resources and may make the computer unusable.

For experimentation, use:

* A fixed copy limit.
* A temporary directory.
* Small test files.
* Automatic cleanup.
* A virtual machine or sandbox when studying malware behavior.

## Suggested Project Structure

```text
ReplicaLoop/
├── replication_demo.py
└── README.md
```

## License

Educational use only.
