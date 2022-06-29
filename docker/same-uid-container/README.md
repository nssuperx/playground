# ホスト側の UID, GID をdocker image作成時に設定

container registry 等にpushすることは想定していない。

vscodeでアタッチした時もホスト側と同じユーザー名（ユーザーID）でファイルなどを作成できる。

## build

```
docker-compose build --build-arg USER_NAME=$(id -un) --build-arg USER_ID=$(id -u) --build-arg GROUP_NAME=$(id -gn) --build-arg GROUP_ID=$(id -g)
```

## コンテナ起動

```
docker-compose up
```

## シェル使いたい

```
docker exec -it container_name /bin/bash
```

## rootでシェル使いたい

```
docker exec -it -u root container_name /bin/bash
```

aptなどを使いたいときはこれを使う。
