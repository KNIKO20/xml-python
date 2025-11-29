from menu import Menu


TITLE1 = """                                                                                                              
█████▄ ██ █████▄ ██     ██ ▄████▄ ██████ ██████ ▄█████ ▄████▄ 
██▄▄██ ██ ██▄▄██ ██     ██ ██  ██   ██   ██▄▄   ██     ██▄▄██ 
██▄▄█▀ ██ ██▄▄█▀ ██████ ██ ▀████▀   ██   ██▄▄▄▄ ▀█████ ██  ██ 
                                                              
"""
mainMenu = Menu(title=TITLE1)

# mainMenu.show_submenu()
# mainMenu.select_option(int(input("Selecciona una opcion: ")))


mainMenu.show_windows_menu()
