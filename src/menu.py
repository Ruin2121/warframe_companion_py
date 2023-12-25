from enum import Enum
from src.utils import pipify
from src.items.warframes import WARFRAMES_DICT
from os import system, name
from config import LINE_LENGTH
from copy import deepcopy


class MenuContext(Enum):
    MAIN_MENU = 1
    INVENTORY_MENU = 2
    INVENTORY_WARFRAME_SUBMENU = 3


class Menu:
    def __init__(self):
        self.pending_input = False
        self.menu_context = MenuContext.MAIN_MENU

        self.main_menu()

    def main_menu(self):
        self.menu_context = MenuContext.MAIN_MENU
        self.clear()
        self.title_bar("Welcome Operator!")
        print(
            """
            Options:
            Inventory
            """
        )
        self.user_input()

    def inventory_menu(self):
        self.menu_context = MenuContext.INVENTORY_MENU
        self.clear()
        self.title_bar("Inventory")
        print(
            """
            Options:
            Warframes
            """
        )
        self.user_input()

    def inventory_warframe_submenu(self):
        self.menu_context = MenuContext.INVENTORY_WARFRAME_SUBMENU
        self.clear()
        self.title_bar("Warframes")
        self.inventory_submenu_generator(WARFRAMES_DICT)
        self.user_input()

    def user_input(self):
        self.pending_input = True
        while self.pending_input:
            self.user_input_logic()

    def user_input_logic(self):
        decision = input()
        decision = decision.lower()

        match self.menu_context:
            case MenuContext.MAIN_MENU:
                match decision:
                    case "inventory" | "inv":
                        self.inventory_menu()
                    case _:
                        print("Invalid Input!")
                        self.user_input_logic()

            case MenuContext.INVENTORY_MENU:
                match decision:
                    case "warframes" | "war":
                        self.inventory_warframe_submenu()
                    case _:
                        print("Invalid Input!")
                        self.user_input_logic()

            case MenuContext.INVENTORY_WARFRAME_SUBMENU:
                match decision:
                    case _:
                        print("Invalid Input!")
                        self.user_input_logic()

            case _:
                print(
                    "You should never see this message. "
                    "Please report what you did to get here to the developer!"
                )

        self.pending_input = False

    @staticmethod
    def clear():
        _ = system("cls") if name == "nt" else system("clear")

    @staticmethod
    def divider(length=LINE_LENGTH):
        print("#" * length)

    def divider2(self, length=LINE_LENGTH):
        self.divider(length)
        self.divider(length)

    def title_bar(self, text: str):
        self.divider2()
        pipify(text)
        self.divider2()

    def inventory_submenu_generator(self, item_dictionary: dict, columns: int = 4):
        number_of_items = len(item_dictionary)
        number_of_rows = (
            (number_of_items // columns) + 1 if (number_of_items % columns) > 0 else 0
        )
        item_dict_copy = deepcopy(item_dictionary)

        left_of_row_to_be_printed = "###    "
        right_of_row_to_be_printed = "    ###"
        remaining_characters = (
            LINE_LENGTH
            - len(left_of_row_to_be_printed)
            - len(right_of_row_to_be_printed)
        )
        per_column_character_budget = remaining_characters // columns
        self.spacer()
        for row in range(number_of_rows):
            x = 0
            row_to_be_printed = ""
            list_of_keys_to_be_deleted = []
            for key, item in item_dict_copy.items():
                if x >= 4:
                    break
                ext_name = item.external_name
                per_column_remaining_characters = (
                    per_column_character_budget - len(ext_name) - 1
                )
                row_to_be_printed += ext_name if x == 0 else f"# {ext_name}"
                row_to_be_printed += " " * (
                    per_column_remaining_characters + (1 if x == 0 else -1)
                )

                list_of_keys_to_be_deleted.append(key)
                x += 1

            if row + 1 == number_of_rows:
                final_row_remaining = remaining_characters - len(row_to_be_printed)
                row_to_be_printed += " " * final_row_remaining

            for key in list_of_keys_to_be_deleted:
                del item_dict_copy[key]

            print(
                left_of_row_to_be_printed
                + row_to_be_printed
                + right_of_row_to_be_printed
            )
        self.spacer()
        self.divider2()

    @staticmethod
    def spacer():
        x = LINE_LENGTH - 6
        print("###" + " " * x + "###")
