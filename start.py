import FileUtilityNuke.main as main_mod
reload(main_mod)

if __name__ == "__main__":
    main = main_mod.FileUtilityNuke()
    main.set_ui()