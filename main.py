import pygame
import sys
import config # Import the config module

def draw_text(screen, text, x, y, font_size, color, font_name=None, bold=False, italic=False):

  if font_name:
    font = pygame.font.Font(font_name, font_size)
  else:
    font = pygame.font.Font(None, font_size)

  font.set_bold(bold)
  font.set_italic(italic)

  text_surface = font.render(text, True, color)
  screen.blit(text_surface, (x, y))

def init_game():
  pygame.init()
  pygame.font.init()

  screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config
  pygame.display.set_caption(config.TITLE)
  return screen

def handle_events():
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      return False
  return True


def draw_rectangle(screen, color, x, y, width, height):
  pygame.draw.rect(screen, color, (x, y, width, height))
    

  


def main():
  screen = init_game()
  clock = pygame.time.Clock() # Initialize the clock here

  text1 = "Jay"
  font_size1 = 5
  color1 = config.BLACK
  x1, y1 = (95, 325)
  width1 = 250
  height1 = 125

  text2 = "Obama"
  font_size2 = 20
  color2 = config.BLUE
  x2, y2 = (400, 100)
  width2 = 400
  height2 = 50

  running = True
  while running:
    running = handle_events()
    value1 = 1
    value2 = 3

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
      y1 -= value1
    if keys[pygame.K_DOWN]:
      y1 += value1
    if keys[pygame.K_LEFT]:
      x1 -= value1
    if keys[pygame.K_RIGHT]:
      x1 += value1
    if keys[pygame.K_w]:
      y2 -= value2
    if keys[pygame.K_s]:
      y2 += value2
    if keys[pygame.K_a]:
      x2 -= value2
    if keys[pygame.K_d]:
      x2 += value2
    
    
    screen.fill(config.WHITE) # Use color from config

    # Draw text on screen using variables
    draw_rectangle(screen, color1, x1, y1, width1, height1)
    draw_rectangle(screen, color2, x2, y2, width2, height2)
    draw_text(screen, text1, x1, y1, font_size1, config.GREEN)
    draw_text(screen, text2, x2, y2, font_size2, config.RED)


    pygame.display.flip()

    # Limit the frame rate to the specified frames per second (FPS)
    clock.tick(config.FPS) # Use the clock to control the frame rate

  pygame.quit()
  sys.exit()

if __name__ == "__main__":
  main()