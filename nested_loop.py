#!/usr/bin/env python3
# Created by: maliksalem1
# Created on: Oct 2022
# This program uses nested loops


def main():
    # This is the nested loop function

    counter1 = 0
    counter2 = 0
    counter3 = 0

    # input,process,output
    for counter1 in range(256):
        for counter2 in range(256):
            for counter3 in range(256):
                print("RGB({0},{1},{2})".format(counter1, counter2, counter3))

    print("\nDone.")


if __name__ == "__main__":
    main()