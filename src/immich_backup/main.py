from immich_backup.immich.api import albums


def main():
    print(albums.get_albums())


if __name__ == "__main__":
    main()
