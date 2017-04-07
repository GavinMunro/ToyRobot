#!/usr/bin/env python
#Title           :ToyRobot.py
#Author          :Gavin A.I. Munro
#Date            :5/3/14
#Version         :0.2


class Robot:
    """
    The application is a simulation of a toy robot moving on a square tabletop,
    of dimensions 5 units x 5 units. There are no other obstructions on the table
    surface. The robot is free to roam around the surface of the table but must
    be prevented from falling [off the edge.]
    """

    dirns = ['N', 'E', 'S', 'W']
    # Possible direction for robot to face are
    # North, South, East and West but note the
    # order is Naughty Elephant Squirts Water!

    def __init__(self):
        self.x = None
        self.y = None
        self.f = None

    @property
    def on_table(self):
    # want to ignore all commands if not on table
        return 1 <= self.x <= 5 and 1 <= self.y <= 5

    def place(self, x, y, f):
        if 1 <= x <= 5 and 1 <= y <= 5 and f in ['N', 'S', 'E', 'W']:
            self.x = x
            self.y = y
            self.f = f
        else:
            return False  # Explicit is better than implicit.

    def move(self):  # always moves only one step forward
        if self.on_table:
            if self.f == 'N':
                self.place(self.x, self.y+1, self.f)
            elif self.f == 'S':
                self.place(self.x, self.y-1, self.f)
            elif self.f == 'E':
                self.place(self.x+1, self.y, self.f)
            elif self.f == 'W':
                self.place(self.x-1, self.y, self.f)

    def right(self):
        if self.on_table:
            self.f = self.dirns[(self.dirns.index(self.f) + 1) % 4]
            # Use modulo 4 to make the list of dirns wrap around.
            # The list is ordered N, E, S, W so Right = clockwise

    def left(self):
        if self.on_table:
            self.f = self.dirns[(self.dirns.index(self.f) - 1) % 4]

    def report(self):
        if self.on_table:
            print "Location: ", "(", self.x, ", ", self.y, ")"
            print "Direction: ", "facing ", self.f
        else:
            print "not on table"

    def drive(self, infile="input.txt"):
        """
        "Drive" the robot using input from a file of commands in
        file input.txt in the current directory.
        The commands take the following form:
        PLACE X,Y,F
        MOVE
        LEFT
        RIGHT
        REPORT
        """
        with open(infile) as file1:
            cmd_list = file1.readlines()
            for line in cmd_list:
                if line.strip() != '' and line.strip()[0] != '#':
                    cmd = line.split()
                    if len(cmd) == 2:
                        if cmd[0] != 'PLACE':
                            print "Invalid Command"
                        params = cmd[1].split(',')
                        x = int(params[0])
                        y = int(params[1])
                        f = params[2]
                        self.place(x, y, f)
                    elif len(cmd) == 1:
                        if cmd[0] == 'MOVE':
                            self.move()
                        elif cmd[0] == 'LEFT':
                            self.left()
                        elif cmd[0] == 'RIGHT':
                            self.right()
                        elif cmd[0] == 'REPORT':
                            self.report()
                        else:
                            print "Invalid command"
            print "End Of File"

if __name__ == "__main__":
    iRobot = Robot()
    iRobot.drive()
