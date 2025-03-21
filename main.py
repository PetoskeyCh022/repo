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
    

  


def main():
  screen = init_game()
  clock = pygame.time.Clock() # Initialize the clock here

  # Define text properties
  text1 = "Salutations Python!"
  font_size1 = 48
  color1 = config.BLACK
  x1, y1 = (200, 250)

  running = True
  while running:
    running = handle_events()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
      y1 -= 10
    if keys[pygame.K_DOWN]:
      y1 += 10
    if keys[pygame.K_LEFT]:
      x1 -= 10
    if keys[pygame.K_RIGHT]:
      x1 += 10
    
    screen.fill(config.WHITE) # Use color from config

    # Draw text on screen using variables
    draw_text(screen, text1, x1, y1, font_size1, color1)

    pygame.display.flip()

    # Limit the frame rate to the specified frames per second (FPS)
    clock.tick(config.FPS) # Use the clock to control the frame rate

  pygame.quit()
  sys.exit()

if __name__ == "__main__":
  main()