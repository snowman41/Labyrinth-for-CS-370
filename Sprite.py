import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect

def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
    """ Returns surface with text written on """
    font = pygame.freetype.SysFont("Courier", font_size, bold = True)
    screen, _ = font.render(text = text, fgcolor = text_rgb, bgcolor = bg_rgb)
    return screen.convert_alpha()

class UIElement(Sprite):

    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb, action=None):

        self.mouse_over = False #indicates if mouse is over the element

        #Default image
        default_image = create_surface_with_text(
            text = text,
            font_size = font_size,
            text_rgb = text_rgb,
            bg_rgb = bg_rgb
            )

        #Image that shows when moused-over
        highlighted_image = create_surface_with_text(
            text = text,
            font_size = font_size * 1.3,
            text_rgb = text_rgb,
            bg_rgb = bg_rgb
            )

        #add both images and their rects to lists
        self.images = [
            default_image,
            highlighted_image
        ]

        self.rects = [
            default_image.get_rect(center = center_position),
            highlighted_image.get_rect(center = center_position),
        ]

        self.action = action

        #calls the init method of the parent sprite class
        super().__init__()

    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]


    #Update button based on mouse position
    def update(self, mouse_pos, mouse_up):
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False


    #Draw button state to screen
    def draw(self, screen):
            screen.blit(self.image, self.rect)