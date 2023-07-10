import sys, pygame
from pygame.locals import QUIT

pygame.init()
screen_info = pygame.display.Info()

size = (width, height) = (screen_info.current_w, screen_info.current_h)

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

color = (153, 0, 0)

def main():
  while True:  
    clock.tick(65)
    screen.fill(color)
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit
      
    
    pygame.display.flip()

if __name__ == '__main__':
  main()
      
    