import pygame


class UI:
    def __init__(self, surface):
        # Setup
        self.display_surface = surface
        # Health
        self.health_bar = pygame.image.load("graphics/ui/healthbar.png").convert_alpha()
        self.health_bar_topleft = (52, 38)
        self.bar_max_width = 142
        self.bar_height = 10
        # Coins
        self.coin = pygame.image.load("graphics/ui/coin.png").convert_alpha()
        self.coin_rect = self.coin.get_rect(topleft=(50, 60))
        self.font = pygame.font.Font("graphics/ui/ARCADEPI.TTF", 25)

    def show_health(self, current_health, full_health):
        self.display_surface.blit(self.health_bar, (6, 10))
        current_health_ratio = current_health / full_health
        current_bar_width = self.bar_max_width * current_health_ratio
        health_bar_rect = pygame.Rect(self.health_bar_topleft, (current_bar_width, self.bar_height))
        pygame.draw.rect(self.display_surface, "#dc4949", health_bar_rect)

    def show_coins(self, amount):
        self.display_surface.blit(self.coin, self.coin_rect)
        coin_amount_surf = self.font.render(str(amount), False, "#33323d")
        coin_amount_rect = coin_amount_surf.get_rect(midleft=(self.coin_rect.right + 4, self.coin_rect.centery))
        self.display_surface.blit(coin_amount_surf, coin_amount_rect)
