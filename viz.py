# viz.py
import matplotlib.pyplot as plt
import numpy as np
from toy_table import OpenAddressingHashTable, ChainingHashTable

def draw_open_table(table: OpenAddressingHashTable, title="Open Addressing"):
    cap = table.capacity
    fig, ax = plt.subplots(figsize=(min(12, cap*0.6), 2.5))
    ax.axis('off')
    ax.set_xlim(0, cap)
    ax.set_ylim(0, 1)
    for i in range(cap):
        rect = plt.Rectangle((i, 0.05), 0.9, 0.9, fill=False)
        ax.add_patch(rect)
        key = table.keys[i]
        val = table.slots[i]
        content = "empty" if key is None else f"{key}\\n{val}"
        ax.text(i + 0.45, 0.55, content, ha='center', va='center', fontsize=9)
    ax.set_title(title)
    plt.tight_layout()
    plt.show()

def demo_open_probing():
    t = OpenAddressingHashTable(capacity=16, probing='linear')
    # force collisions by inserting integers with small modulo behaviour
    for k in range(1, 13):
        t.insert(k, f"v{k}")
    draw_open_table(t, title="Linear probing demo")

if __name__ == "__main__":
    demo_open_probing()
