import pygame
import sys

pygame.init()
logo = pygame.image.load('assets/images/logo.png')
pygame.display.set_icon(logo)

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BUTTON_WIDTH = 300
BUTTON_HEIGHT = 60
BUTTON_MARGIN = 20
FONT_SIZE = 20
FONT = r"assets\fonts\Pixeled.ttf"
TITLE_FONT_SIZE = 38

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_BLUE = (100, 180, 255)
DARK_BLUE = (60, 140, 220)
HOVER_COLOR = (80, 160, 240)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Life Oversimplified")

# Font - Using a nicer font
font = pygame.font.Font(FONT, FONT_SIZE)
title_font = pygame.font.Font(FONT, TITLE_FONT_SIZE)

# Load background image
background_image = pygame.image.load('assets/images/BG.jpg')
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

class Button:
    def __init__(self, text, x, y):
        self.text = text
        self.rect = pygame.Rect(x, y, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.normal_color = LIGHT_BLUE
        self.hover_color = HOVER_COLOR
        self.current_color = self.normal_color
        self.border_radius = 10 

    def draw(self, screen):
        # Draw button shadow
        shadow_rect = self.rect.copy()
        shadow_rect.y += 4
        pygame.draw.rect(screen, DARK_BLUE, shadow_rect, border_radius=self.border_radius)
        
        # Draw main button
        pygame.draw.rect(screen, self.current_color, self.rect, border_radius=self.border_radius)
        
        # Draw border
        pygame.draw.rect(screen, DARK_BLUE, self.rect, 2, border_radius=self.border_radius)
        
        # Draw text with slight shadow effect
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=(self.rect.center[0],self.rect.center[1] - 2))
        screen.blit(text_surface, text_rect)

    def handle_hover(self, pos):
        if self.rect.collidepoint(pos):
            self.current_color = self.hover_color
        else:
            self.current_color = self.normal_color

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

class SettingsButton:
    def __init__(self):
        self.image = pygame.image.load('assets/images/Settings_icon.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.topright = (SCREEN_WIDTH - 40, 20)  # Adjusted position for better visibility

    def draw(self, screen):
        # Draw black border
        border_rect = self.rect
        border_rect_black = self.rect.inflate(5, 5)
        pygame.draw.rect(screen, BLACK, border_rect_black, border_radius=10)
        pygame.draw.rect(screen, (240,240,240), border_rect, border_radius=10)
        
        screen.blit(self.image, self.rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

def main_menu():
    buttons = [
        Button("PLAY", (SCREEN_WIDTH - BUTTON_WIDTH) // 2, SCREEN_HEIGHT // 1.8 - BUTTON_HEIGHT - BUTTON_MARGIN),
        Button("INSTRUCTIONS", (SCREEN_WIDTH - BUTTON_WIDTH) // 2, SCREEN_HEIGHT // 1.8),
        Button("CODE", (SCREEN_WIDTH - BUTTON_WIDTH) // 2, SCREEN_HEIGHT // 1.8 + BUTTON_HEIGHT + BUTTON_MARGIN)
    ]
    settings_button = SettingsButton()

    while True:
        screen.blit(background_image, (0, 0))

        # Draw title
        title_surface = title_font.render("LIFE OVERSIMPLIFIED", True, BLACK)
        title_rect = title_surface.get_rect(center=(SCREEN_WIDTH // 2, 180))
        screen.blit(title_surface, title_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if settings_button.is_clicked(event.pos):
                    print("Settings button clicked")
                for button in buttons:
                    if button.is_clicked(event.pos):
                        print(f"{button.text} button clicked")

        mouse_pos = pygame.mouse.get_pos()
        for button in buttons:
            button.handle_hover(mouse_pos)
            button.draw(screen)

        settings_button.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main_menu()
