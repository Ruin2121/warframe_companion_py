from enum import Enum
from src.utils import pipify
from src.items.warframes import WARFRAMES_DICT
from src.enumerations.warframes import Warframes
from os import system, name
from config import LINE_LENGTH


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
        print(  # This is not a good solution, ideally find an automatic method
            f"""###
###    {WARFRAMES_DICT[Warframes.ASH].external_name}                     #  {WARFRAMES_DICT[Warframes.IVARA_PRIME].external_name}    #  {WARFRAMES_DICT[Warframes.TITANIA_PRIME].external_name}
###    {WARFRAMES_DICT[Warframes.ASH_PRIME].external_name}               #  {WARFRAMES_DICT[Warframes.KHORA].external_name}          #  {WARFRAMES_DICT[Warframes.TRINITY].external_name}
###    {WARFRAMES_DICT[Warframes.ATLAS].external_name}                   #  {WARFRAMES_DICT[Warframes.KHORA_PRIME].external_name}    #  {WARFRAMES_DICT[Warframes.TRINITY_PRIME].external_name}
###    {WARFRAMES_DICT[Warframes.ATLAS_PRIME].external_name}             #  {WARFRAMES_DICT[Warframes.KULLERVO].external_name}       #  {WARFRAMES_DICT[Warframes.VALKYR].external_name}
###    {WARFRAMES_DICT[Warframes.BANSHEE].external_name}                 #  {WARFRAMES_DICT[Warframes.LAVOS].external_name}          #  {WARFRAMES_DICT[Warframes.VALKYR_PRIME].external_name}
###    {WARFRAMES_DICT[Warframes.BANSHEE_PRIME].external_name}           #  {WARFRAMES_DICT[Warframes.LIMBO].external_name}          #  {WARFRAMES_DICT[Warframes.VAUBAN].external_name}
###    {WARFRAMES_DICT[Warframes.BARUUK].external_name}                  #  {WARFRAMES_DICT[Warframes.LIMBO_PRIME].external_name}    #  {WARFRAMES_DICT[Warframes.VAUBAN_PRIME].external_name}
###    {WARFRAMES_DICT[Warframes.BARUUK_PRIME].external_name}            #  {WARFRAMES_DICT[Warframes.LOKI].external_name}           #  {WARFRAMES_DICT[Warframes.VOLT].external_name}
###    {WARFRAMES_DICT[Warframes.CALIBAN].external_name}                 #  {WARFRAMES_DICT[Warframes.LOKI_PRIME].external_name}     #  {WARFRAMES_DICT[Warframes.VOLT_PRIME].external_name}
###    {WARFRAMES_DICT[Warframes.CHROMA].external_name}                  #  {WARFRAMES_DICT[Warframes.MAG].external_name}            #  {WARFRAMES_DICT[Warframes.VORUNA].external_name}
###    {WARFRAMES_DICT[Warframes.CHROMA_PRIME].external_name}            #  {WARFRAMES_DICT[Warframes.MAG_PRIME].external_name}      #  {WARFRAMES_DICT[Warframes.WISP].external_name}
###    {WARFRAMES_DICT[Warframes.CITRINE].external_name}                 #  {WARFRAMES_DICT[Warframes.MESA].external_name}           #  {WARFRAMES_DICT[Warframes.WISP_PRIME].external_name}
###    {WARFRAMES_DICT[Warframes.DAGATH].external_name}                  #  {WARFRAMES_DICT[Warframes.MESA_PRIME].external_name}     #  {WARFRAMES_DICT[Warframes.WUKONG].external_name}
###    {WARFRAMES_DICT[Warframes.EMBER].external_name}                   #  {WARFRAMES_DICT[Warframes.MIRAGE].external_name}         #  {WARFRAMES_DICT[Warframes.WUKONG_PRIME].external_name}
###    {WARFRAMES_DICT[Warframes.EMBER_PRIME].external_name}             #  {WARFRAMES_DICT[Warframes.MIRAGE_PRIME].external_name}   #  {WARFRAMES_DICT[Warframes.XAKU].external_name}
###    {WARFRAMES_DICT[Warframes.EQUINOX].external_name}                 #  {WARFRAMES_DICT[Warframes.NEKROS].external_name}         #  {WARFRAMES_DICT[Warframes.YARELI].external_name}
###    {WARFRAMES_DICT[Warframes.EQUINOX_PRIME].external_name}           #  {WARFRAMES_DICT[Warframes.NEKROS_PRIME].external_name}   #  {WARFRAMES_DICT[Warframes.ZEPHYR].external_name}
###    {WARFRAMES_DICT[Warframes.EXCALIBUR].external_name}               #  {WARFRAMES_DICT[Warframes.NEZHA].external_name}          #  {WARFRAMES_DICT[Warframes.ZEPHYR_PRIME].external_name}
###    {WARFRAMES_DICT[Warframes.EXCALIBUR_PRIME].external_name}         #  {WARFRAMES_DICT[Warframes.NEZHA_PRIME].external_name}
###    {WARFRAMES_DICT[Warframes.EXCALIBUR_UMBRA].external_name}         #  {WARFRAMES_DICT[Warframes.NIDUS].external_name}
###    {WARFRAMES_DICT[Warframes.EXCALIBUR_UMBRA_PRIME].external_name}   #  {WARFRAMES_DICT[Warframes.NIDUS_PRIME].external_name}
###    {WARFRAMES_DICT[Warframes.FROST].external_name}                   #  {WARFRAMES_DICT[Warframes.NOVA].external_name}
###    {WARFRAMES_DICT[Warframes.FROST_PRIME].external_name}             #  {WARFRAMES_DICT[Warframes.NOVA_PRIME].external_name}
###    {WARFRAMES_DICT[Warframes.GARA].external_name}                    #  {WARFRAMES_DICT[Warframes.NYX].external_name}
###    {WARFRAMES_DICT[Warframes.GARA_PRIME].external_name}              #  {WARFRAMES_DICT[Warframes.NYX_PRIME].external_name}
###    {WARFRAMES_DICT[Warframes.GARUDA].external_name}                  #  {WARFRAMES_DICT[Warframes.OBERON].external_name}
###    {WARFRAMES_DICT[Warframes.GARUDA_PRIME].external_name}            #  {WARFRAMES_DICT[Warframes.OBERON_PRIME].external_name}
###    {WARFRAMES_DICT[Warframes.GAUSS].external_name}                   #  {WARFRAMES_DICT[Warframes.OCTAVIA].external_name}
###    {WARFRAMES_DICT[Warframes.GRENDEL].external_name}                 #  {WARFRAMES_DICT[Warframes.OCTAVIA_PRIME].external_name}
###    {WARFRAMES_DICT[Warframes.GRENDEL_PRIME].external_name}           #  {WARFRAMES_DICT[Warframes.PROTEA].external_name}
###    {WARFRAMES_DICT[Warframes.GYRE].external_name}                    #  {WARFRAMES_DICT[Warframes.QORVEX].external_name}
###    {WARFRAMES_DICT[Warframes.HARROW].external_name}                  #  {WARFRAMES_DICT[Warframes.REVENANT].external_name}
###    {WARFRAMES_DICT[Warframes.HARROW_PRIME].external_name}            #  {WARFRAMES_DICT[Warframes.REVENANT_PRIME].external_name}
###    {WARFRAMES_DICT[Warframes.HILDRYN].external_name}                 #  {WARFRAMES_DICT[Warframes.RHINO].external_name}
###    {WARFRAMES_DICT[Warframes.HILDRYN_PRIME].external_name}           #  {WARFRAMES_DICT[Warframes.RHINO_PRIME].external_name}
###    {WARFRAMES_DICT[Warframes.HYDROID].external_name}                 #  {WARFRAMES_DICT[Warframes.SARYN].external_name}
###    {WARFRAMES_DICT[Warframes.HYDROID_PRIME].external_name}           #  {WARFRAMES_DICT[Warframes.SARYN_PRIME].external_name}
###    {WARFRAMES_DICT[Warframes.INAROS].external_name}                  #  {WARFRAMES_DICT[Warframes.SEVAGOTH].external_name}
###    {WARFRAMES_DICT[Warframes.INAROS_PRIME].external_name}            #  {WARFRAMES_DICT[Warframes.STYANAX].external_name}
###    {WARFRAMES_DICT[Warframes.IVARA].external_name}                   #  {WARFRAMES_DICT[Warframes.TITANIA].external_name}
"""
        )
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

    @staticmethod
    def divider2(self, length=LINE_LENGTH):
        self.divider(length)
        self.divider(length)

    @staticmethod
    def title_bar(self, text: str):
        self.divider2()
        pipify(text)
        self.divider2()
