from filedialogs import open_file_dialog, open_folder_dialog, save_file_dialog


def main():
    open_path = open_file_dialog()
    print(open_path)

    save_path = save_file_dialog()
    print(save_path)

    open_folder = open_folder_dialog()
    print(open_folder)


if __name__ == "__main__":
    main()
