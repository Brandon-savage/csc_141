import sys
from time import sleep
import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        # Full-screen window
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        rect = self.screen.get_rect()
        self.settings.screen_width = rect.width
        self.settings.screen_height = rect.height
        pygame.display.set_caption("Alien Invasion")

        # Game stats and scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.bg_color = (50, 0, 230)
        self.game_active = False

        # Play button
        self.play_button = Button(self, "Play")

        # Game objects
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        # Create alien fleet
        self._create_fleet()

        # Background music
        pygame.mixer.music.load(self.settings.main_music)
        pygame.mixer.music.set_volume(0.8)
        pygame.mixer.music.play(-1)

    def _create_fleet(self):
        """Create the fleet of aliens."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _start_game(self):
        self.game_active = True
        self.bullets.empty()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _update_bullets(self):
        self.bullets.update()

        # Remove old bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()
        print(len(self.bullets))

    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            self.stats.level += 1
            self.sb.prep_level()

    def _update_aliens(self):
        """Check if the fleet is at an edge, then update positions."""
        self._check_fleet_edges()
        self.aliens.update()

        # Check for ship-alien collision
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Check if aliens reach bottom
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            self.bullets.empty()
            self.aliens.empty()

            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Check if any aliens reach the screen bottom."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_play_button(pygame.mouse.get_pos())

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p and not self.game_active:
            self._start_game()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)

        if button_clicked and not self.game_active: 

            self.stats.reset_stats()
            self.game_active = True

            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            self.bullets.empty()
            self.aliens.empty()

            self._create_fleet()
            self.ship.center_ship()

            pygame.mouse.set_visible(False)

    def _update_screen(self):
        self.screen.fill(self.bg_color)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()
        self.aliens.draw(self.screen)

        self.sb.show_score()

        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()