from turtle import right, left, forward, penup, pendown, pen, pencolor, setup, goto, shape
from colorsys import hsv_to_rgb

# Global Params
LEVELS = 5 # Number of rewrites
W = 1000 # Screen width (and height for a square)
B = 20 # Border
LEN = (W - 2*B) / (2**LEVELS - 1) # Line Length


debug = lambda lvl, string: print(lvl, string, '\n')

grammar = {
    'A':"+BF-AFA-FB+",
    'B':"-AF+BFB+FA-",
    '+':"+",
    "-":"-",
    "F":"F"
}

def production(string, num):
    for i in range(num):
        string = replacer(string)
    return string

def replacer(string):
    """Production helper function"""
    newStr = ''
    for i in string:
        newStr += grammar[i]
    return newStr

def generateHilbertStringForLevel(n):
    return production("A", n)

hue = 0

def drawLine():
  global hue
  hue += 1
  pencolor(hsv_to_rgb(hue/4**LEVELS,1,1))
  forward(LEN)

# Execute Brains String
ops = {
  'A': lambda : None, # NOP
  'B': lambda : None, # NOP
  '+': lambda : right(90), # Turn from current direction
  '-': lambda : left(90),  # Turn from current direction
  'F': drawLine # Draw line 40 pixels
}


def drawHilbert(string):
  # initialize turtle
  setup(width=W, height=W)
  
  pen(pencolor="pink", pensize=LEN/3, speed=0, shown=False)
  # shape("square")

  penup()
  half = W/2 - 20
  goto(-half, half) #translate the origin from the middle to the upper right
  pendown()

  # draw according to each symbol
  for ch in string:
    ops[ch]()

  
def main():
  string = generateHilbertStringForLevel(LEVELS)
  drawHilbert(string)
  
if __name__ == "__main__":
    main()