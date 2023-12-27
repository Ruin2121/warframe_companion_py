from copy import deepcopy
from enum import Enum
from os import system, name
from sys import exit

from config import LINE_LENGTH
from src.base_classes.item import Item
from src.enumerations.warframes import Warframes
from src.items.warframes import WARFRAMES_DICT
from src.utils import pipify


class MenuContext(Enum):
    MAIN_MENU = 1
    INVENTORY_MENU = 2
    INVENTORY_WARFRAME_SUBMENU = 3
    ITEM_SUBMENU = 4


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

    def item_submenu(self, item_class: type[Item]):
        self.menu_context = MenuContext.ITEM_SUBMENU
        self.clear()
        self.title_bar(item_class.external_name)

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

                    case "exit" | "quit":
                        exit()

                    case _:
                        print(
                            "Invalid Input! If you think this is an error, please report this to the developer."
                        )
                        self.user_input_logic()

            case MenuContext.INVENTORY_MENU:
                match decision:
                    case "warframes" | "war":
                        self.inventory_warframe_submenu()

                    case "back":
                        self.main_menu()

                    case "exit" | "quit":
                        exit()

                    case _:
                        print(
                            "Invalid Input! If you think this is an error, please report this to the developer."
                        )
                        self.user_input_logic()

            case MenuContext.INVENTORY_WARFRAME_SUBMENU:
                match decision:
                    case ash if ash == Warframes.ASH.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.ASH])
                    case ash_prime if ash_prime == Warframes.ASH_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.ASH_PRIME])

                    case atlas if atlas == Warframes.ATLAS.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.ATLAS])
                    case atlas_prime if atlas_prime == Warframes.ATLAS_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.ATLAS_PRIME])

                    case banshee if banshee == Warframes.BANSHEE.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.BANSHEE])
                    case banshee_prime if banshee_prime == Warframes.BANSHEE_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.BANSHEE_PRIME])

                    case baruuk if baruuk == Warframes.BARUUK.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.BARUUK])
                    case baruuk_prime if baruuk_prime == Warframes.BARUUK_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.BARUUK_PRIME])

                    case caliban if caliban == Warframes.CALIBAN.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.CALIBAN])

                    case chroma if chroma == Warframes.CHROMA.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.CHROMA])
                    case chroma_prime if chroma_prime == Warframes.CHROMA_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.CHROMA_PRIME])

                    case citrine if citrine == Warframes.CITRINE.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.CITRINE])

                    case dagath if dagath == Warframes.DAGATH.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.DAGATH])

                    case ember if ember == Warframes.EMBER.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.EMBER])
                    case ember_prime if ember_prime == Warframes.EMBER_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.EMBER_PRIME])

                    case equinox if equinox == Warframes.EQUINOX.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.EQUINOX])
                    case equinox_prime if equinox_prime == Warframes.EQUINOX_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.EQUINOX_PRIME])

                    case excalibur if excalibur == Warframes.EXCALIBUR.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.EXCALIBUR])
                    case excalibur_prime if excalibur_prime == Warframes.EXCALIBUR_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.EXCALIBUR_PRIME])

                    case excalibur_umbra if excalibur_umbra == Warframes.EXCALIBUR_UMBRA.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.EXCALIBUR_UMBRA])
                    case excalibur_umbra_prime if excalibur_umbra_prime == Warframes.EXCALIBUR_UMBRA_PRIME.value.lower():
                        self.item_submenu(
                            WARFRAMES_DICT[Warframes.EXCALIBUR_UMBRA_PRIME]
                        )

                    case frost if frost == Warframes.FROST.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.FROST])
                    case frost_prime if frost_prime == Warframes.FROST_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.FROST_PRIME])

                    case gara if gara == Warframes.GARA.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.GARA])
                    case gara_prime if gara_prime == Warframes.GARA_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.GARA_PRIME])

                    case garuda if garuda == Warframes.GARUDA.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.GARUDA])
                    case garuda_prime if garuda_prime == Warframes.GARUDA_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.GARUDA_PRIME])

                    case gauss if gauss == Warframes.GAUSS.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.GAUSS])

                    case grendel if grendel == Warframes.GRENDEL.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.GRENDEL])
                    case grendel_prime if grendel_prime == Warframes.GRENDEL_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.GRENDEL_PRIME])

                    case gyre if gyre == Warframes.GYRE.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.GYRE])

                    case harrow if harrow == Warframes.HARROW.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.HARROW])
                    case harrow_prime if harrow_prime == Warframes.HARROW_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.HARROW_PRIME])

                    case hildryn if hildryn == Warframes.HILDRYN.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.HILDRYN])
                    case hildryn_prime if hildryn_prime == Warframes.HILDRYN_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.HILDRYN_PRIME])

                    case hydroid if hydroid == Warframes.HYDROID.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.HYDROID])
                    case hydroid_prime if hydroid_prime == Warframes.HYDROID_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.HYDROID_PRIME])

                    case inaros if inaros == Warframes.INAROS.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.INAROS])
                    case inaros_prime if inaros_prime == Warframes.INAROS_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.INAROS_PRIME])

                    case ivara if ivara == Warframes.IVARA.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.IVARA])
                    case ivara_prime if ivara_prime == Warframes.IVARA_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.IVARA_PRIME])

                    case khora if khora == Warframes.KHORA.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.KHORA])
                    case khora_prime if khora_prime == Warframes.KHORA_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.KHORA_PRIME])

                    case kullervo if kullervo == Warframes.KULLERVO.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.KULLERVO])

                    case lavos if lavos == Warframes.LAVOS.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.LAVOS])

                    case limbo if limbo == Warframes.LIMBO.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.LIMBO])
                    case limbo_prime if limbo_prime == Warframes.LIMBO_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.LIMBO_PRIME])

                    case loki if loki == Warframes.LOKI.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.LOKI])
                    case loki_prime if loki_prime == Warframes.LOKI_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.LOKI_PRIME])

                    case mag if mag == Warframes.MAG.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.MAG])
                    case mag_prime if mag_prime == Warframes.MAG_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.MAG_PRIME])

                    case mesa if mesa == Warframes.MESA.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.MESA])
                    case mesa_prime if mesa_prime == Warframes.MESA_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.MESA_PRIME])

                    case mirage if mirage == Warframes.MIRAGE.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.MIRAGE])
                    case mirage_prime if mirage_prime == Warframes.MIRAGE_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.MIRAGE_PRIME])

                    case nekros if nekros == Warframes.NEKROS.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.NEKROS])
                    case nekros_prime if nekros_prime == Warframes.NEKROS_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.NEKROS_PRIME])

                    case nezha if nezha == Warframes.NEZHA.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.NEZHA])
                    case nezha_prime if nezha_prime == Warframes.NEZHA_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.NEZHA_PRIME])

                    case nidus if nidus == Warframes.NIDUS.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.NIDUS])
                    case nidus_prime if nidus_prime == Warframes.NIDUS_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.NIDUS_PRIME])

                    case nova if nova == Warframes.NOVA.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.NOVA])
                    case nova_prime if nova_prime == Warframes.NOVA_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.NOVA_PRIME])

                    case nyx if nyx == Warframes.NYX.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.NYX])
                    case nyx_prime if nyx_prime == Warframes.NYX_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.NYX_PRIME])

                    case oberon if oberon == Warframes.OBERON.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.OBERON])
                    case oberon_prime if oberon_prime == Warframes.OBERON_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.OBERON_PRIME])

                    case octavia if octavia == Warframes.OCTAVIA.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.OCTAVIA])
                    case octavia_prime if octavia_prime == Warframes.OCTAVIA_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.OCTAVIA_PRIME])

                    case protea if protea == Warframes.PROTEA.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.PROTEA])

                    case qorvex if qorvex == Warframes.QORVEX.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.QORVEX])

                    case revenant if revenant == Warframes.REVENANT.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.REVENANT])
                    case revenant_prime if revenant_prime == Warframes.REVENANT_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.REVENANT_PRIME])

                    case rhino if rhino == Warframes.RHINO.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.RHINO])
                    case rhino_prime if rhino_prime == Warframes.RHINO_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.RHINO_PRIME])

                    case saryn if saryn == Warframes.SARYN.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.SARYN])
                    case saryn_prime if saryn_prime == Warframes.SARYN_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.SARYN_PRIME])

                    case sevagoth if sevagoth == Warframes.SEVAGOTH.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.SEVAGOTH])

                    case styanax if styanax == Warframes.STYANAX.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.STYANAX])

                    case titania if titania == Warframes.TITANIA.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.TITANIA])
                    case titania_prime if titania_prime == Warframes.TITANIA_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.TITANIA_PRIME])

                    case trinity if trinity == Warframes.TRINITY.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.TRINITY])
                    case trinity_prime if trinity_prime == Warframes.TRINITY_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.TRINITY_PRIME])

                    case valkyr if valkyr == Warframes.VALKYR.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.VALKYR])
                    case valkyr_prime if valkyr_prime == Warframes.VALKYR_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.VALKYR_PRIME])

                    case vauban if vauban == Warframes.VAUBAN.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.VAUBAN])
                    case vauban_prime if vauban_prime == Warframes.VAUBAN_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.VAUBAN_PRIME])

                    case volt if volt == Warframes.VOLT.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.VOLT])
                    case volt_prime if volt_prime == Warframes.VOLT_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.VOLT_PRIME])

                    case voruna if voruna == Warframes.VORUNA.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.VORUNA])

                    case wisp if wisp == Warframes.WISP.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.WISP])
                    case wisp_prime if wisp_prime == Warframes.WISP_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.WISP_PRIME])

                    case wukong if wukong == Warframes.WUKONG.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.WUKONG])
                    case wukong_prime if wukong_prime == Warframes.WUKONG_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.WUKONG_PRIME])

                    case xaku if xaku == Warframes.XAKU.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.XAKU])

                    case yareli if yareli == Warframes.YARELI.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.YARELI])

                    case zephyr if zephyr == Warframes.ZEPHYR.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.ZEPHYR])
                    case zephyr_prime if zephyr_prime == Warframes.ZEPHYR_PRIME.value.lower():
                        self.item_submenu(WARFRAMES_DICT[Warframes.ZEPHYR_PRIME])

                    case "back":
                        self.inventory_menu()

                    case "exit" | "quit":
                        exit()

                    case _:
                        print(
                            "Invalid Input! If you think this is an error, please report this to the developer."
                        )
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
                if x >= columns:
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
