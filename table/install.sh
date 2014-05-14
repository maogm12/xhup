#!/bin/bash

TABLE_ROOT="$HOME/.config/fcitx/table"

CONF="flypy.conf"
TARGET_CONF="$TABLE_ROOT/$CONF"
TARGET_CONF_BAK="$TARGET_CONF.bak"

MB="flypy.mb"
TARGET_MB="$TABLE_ROOT/$MB"
TARGET_MB_BAK="$TARGET_MB.bak"

if [ ! -d "$TABLE_ROOT" ]; then
    mkdir -p "$TABLE_ROOT"
fi

echo "install flypy mb file for fcitx"
if [ -f "$TARGET_CONF" ]; then
    echo "backup existing $TARGET_CONF"
    cp "$TARGET_CONF" "$TARGET_CONF_BAK"
fi

echo "copy $CONF to $TARGET_CONF"
cp "$CONF" "$TARGET_CONF"

if [ -f "$TARGET_MB" ]; then
    echo "backup exitsing $TARGET_MB"
    cp "$TARGET_MB" "$TARGET_MB_BAK"
fi

echo "copy $MB to $TARGET_MB"
cp "$MB" "$TARGET_MB"

echo "restart fcitx"
fcitx -r
