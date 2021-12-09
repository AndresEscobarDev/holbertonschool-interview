#!/usr/bin/python3
if __name__ == "__main__":
    pass


def canUnlockAll(boxes):
    length = len(boxes)

    openBoxes = length * [False]
    openBoxes[0] = True
    keys = boxes[0]

    for key in keys:
        if openBoxes[key] is False:
            openBoxes[key] = True
            keys += boxes[key]

    return False not in openBoxes
