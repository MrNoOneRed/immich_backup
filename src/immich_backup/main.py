from immich_backup.immich.client import immich


def main():
    albums = immich.albums.get_all_albums()
    print(albums)


if __name__ == "__main__":
    main()
