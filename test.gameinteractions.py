import unittest
from unittest.mock import patch, call, Mock

from game_interactions import GameInteractions
from game_state import GameState
from player import Player
from human import Human
from ai import AI

class TestGameInteractions(unittest.TestCase):
    @patch("game_interactions.GameInteractions.request_players")
    @patch("game_interactions.GameInteractions.print_rows")
    @patch("game_interactions.GameInteractions.print_player")
    @patch("player.Player.choose_card")
    @patch("game_state.GameState.play_turn")
    def test_run(self, mock_play_turn, mock_choose_card, mock_print_player, mock_print_rows, mock_request_players):
        mock_request_players.return_value = [Player("Alice", Human()), Player("Bob", AI())]
        mock_choose_card.side_effect = [Card(5), Card(7)]
        mock_play_turn.side_effect = [[], [Card(3), Card(9)]]

        game_state = GameState([])
        game_interactions = GameInteractions(game_state)
        game_interactions.run()

        mock_request_players.assert_called_once()
        mock_print_rows.assert_called_once_with(game_state.rows)
        mock_print_player.assert_has_calls([
            call(game_state.players[0], True),
            call(game_state.players[1], True)
        ])
        mock_choose_card.assert_has_calls([
            call(game_state.players[0], game_state.rows),
            call(game_state.players[1], game_state.rows)
        ])
        mock_play_turn.assert_has_calls([
            call((game_state.players[0], Card(5))),
            call((game_state.players[1], Card(7)))
        ])

    def test_load(self):
        mock_game_state = Mock(spec=GameState)
        game_interactions = GameInteractions(mock_game_state)
        game_interactions.load({"some_data": 42})
        mock_game_state.load.assert_called_once_with({"some_data": 42})

if __name__ == "__main__":
    unittest.main()
