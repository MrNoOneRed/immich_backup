from immich_backup.immich.client import immich
from immich_backup.immich.models.albums import GetAllAlbumsQuery
from immich_backup.immich.models.search import SearchAssetsRequest


def main():
    albums = immich.albums.get_all_albums(GetAllAlbumsQuery(name="Celisiowo"))

    for album in albums:
        data = immich.search.search_assets(
            request=SearchAssetsRequest(album_ids=[album.id])
        )

        for item in data.assets.items:
            print(item.original_file_name)


if __name__ == "__main__":
    main()
