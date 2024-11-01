import typing as t

from src import shared
from src.enums import State
from src.game_state import GameState
from src.main_menu import MainMenu


class StateLike(t.Protocol):
    def update(self): ...

    def draw(self): ...


class StateManager:
    def __init__(self) -> None:
        self.state_dict: dict[State, StateLike] = {
            State.GAME: GameState,
            State.MAIN_MENU: MainMenu,
        }

        shared.next_state = State.MAIN_MENU
        self.state_obj: StateLike = self.state_dict.get(shared.next_state)()

    def update(self):
        self.state_obj.update()
        if shared.next_state is not None:
            self.state_obj = self.state_dict.get(shared.next_state)()

    def draw(self):
        self.state_obj.draw()
