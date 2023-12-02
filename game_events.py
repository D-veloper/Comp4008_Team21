import game_play
from game_play import GamePlay
from game_components import GameRects




class GameEvents:
    def __init__(self, game_play: GamePlay, game_surfaces: GameRects):
        self.game_play = game_play
        self.game_surfaces = game_surfaces
        self.selected_rack_tile_index = None
        self.selected_game_board_tile_positions = None # [row,col]
        self.show = True

    def handle_events(self, pos):
        if self.game_surfaces.is_colliding_with_player_rack(pos):
            self.handle_user_player_rack_events(pos)

        elif self.game_surfaces.is_colliding_with_game_board(pos):
            self.handle_game_board_events(pos)

        elif self.game_surfaces.show_button[1].collidepoint(pos):
            self.game_play.toggle_comp_tile_visible()
            self.game_surfaces.update_comp_tiles_surfaces()

        elif self.game_surfaces.draw_tiles_button[1].collidepoint(pos):
            if len(self.game_play.drawn_tiles_from_pool) == 0:
                drawn_tiles = self.game_play.draw_tile_from_pool()
                self.game_surfaces.update_drawn_pool_tiles()

        elif self.game_surfaces.is_colliding_with_drawn_tile(pos):
            self.handle_pool_event(pos)
            self.game_play.reset_draw()
            self.game_surfaces.update_drawn_pool_tiles()
            self.game_surfaces.update_remaining_tiles()

        elif self.game_surfaces.submit_button[1].collidepoint(pos):
            validation = self.game_play.submit_game_state()
            if validation[0]:
                print("true")
            else:
                print("false")


    def handle_user_player_rack_events(self, pos):
        user_tiles = self.game_play.player.get_tiles()
        user_tile_surfaces = self.game_surfaces.player_tiles_surfaces
        for i, tile in enumerate(user_tile_surfaces):
            if tile[1].collidepoint(pos) and user_tiles[i] is not None:
                self.selected_rack_tile_index = i

            elif tile[1].collidepoint(pos) and self.selected_rack_tile_index is not None:
                if user_tiles[i] is None:
                    self.game_play.player.add_tile(user_tiles[self.selected_rack_tile_index], i)
                    self.game_play.player.remove_tile(self.selected_rack_tile_index)
                    self.game_surfaces.update_player_tiles_surfaces()
                    self.selected_rack_tile_index = None

    #           BOARD -> RACK TODO

    def handle_game_board_events(self, pos):
        user_tiles = self.game_play.player.get_tiles()
        game_board_surfaces = self.game_surfaces.game_board_tile_surfaces

        for i in range(len(game_board_surfaces)):
            for j in range(len(game_board_surfaces[i])):
                if game_board_surfaces[i][j][1].collidepoint(pos):
                    if self.selected_rack_tile_index is not None and self.game_play.game_state[i][j] is None:
                        self.game_play.update_game_state(user_tiles[self.selected_rack_tile_index], i, j)
                        self.game_play.player.remove_tile(self.selected_rack_tile_index)
                        self.game_surfaces.update_player_tiles_surfaces()
                        self.game_surfaces.update_game_state_tiles_surfaces()
                        self.selected_rack_tile_index = None
                        self.selected_game_board_tile_positions = None

                    elif self.selected_game_board_tile_positions is not None and self.game_play.game_state[i][j] is None:
                        selected_x,selected_y = self.selected_game_board_tile_positions
                        self.game_play.update_game_state(self.game_play.game_state[selected_x][selected_y], i, j)
                        self.game_play.remove_game_state_tile(selected_x, selected_y)
                        self.game_surfaces.update_player_tiles_surfaces()
                        self.game_surfaces.update_game_state_tiles_surfaces()
                        self.selected_game_board_tile_positions = None

                    elif self.game_play.game_state[i][j] is not None:
                        self.selected_game_board_tile_positions = [i, j]
                        self.selected_rack_tile_index = None


    def handle_pool_event(self, pos):
        selected_index = None
        for i, tile in enumerate(self.game_surfaces.drawn_pool_tiles_surfaces):
            print("here", tile)
            if tile[1].collidepoint(pos):
                for j, tile in enumerate(self.game_play.player.get_tiles()):
                    if tile is None:
                        self.game_play.player.add_tile(self.game_play.drawn_tiles_from_pool[i], j)
                        self.game_surfaces.update_player_tiles_surfaces()
                        selected_index = i

                        if selected_index == 0:
                            self.game_play.pool.update_pool(self.game_play.drawn_tiles_from_pool[1])
                            break
                        else:
                            self.game_play.pool.update_pool(self.game_play.drawn_tiles_from_pool[0])
                            break



