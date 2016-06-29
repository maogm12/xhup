#!/bin/bash

TABLE_ROOT="$HOME/.config/fcitx/table"
PINYIN_ROOT="$HOME/.config/fcitx/pinyin"

CONF="flypy.conf"
TARGET_CONF="$TABLE_ROOT/$CONF"
TARGET_CONF_BAK="$TARGET_CONF.bak"

MB="flypy.mb"
TARGET_MB="$TABLE_ROOT/$MB"
TARGET_MB_BAK="$TARGET_MB.bak"

PYSYM="pySym.mb"
TARGET_PYSYM="$PINYIN_ROOT/$PYSYM"
TARGET_PYSYM_BAK="$TARGET_PYSYM.bak"

if [ $# -eq 0 ]; then
    echo "USAGE: $0 all|table|pinyin"
    echo "      all     Install the mb file to pinyin and table path"
    echo "      table   Install the mb file to table path for table input method"
    echo "      pinyin  Install the mb file to pinyin path for pinyin input method"
    exit
fi

if [ "$1" = "all" ] || [ "$1" = "table" ]; then
    if [ ! -d "$TABLE_ROOT" ]; then
        mkdir -p "$TABLE_ROOT"
    fi


    echo "install xiaohe mb file for table input method"
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
fi

if [ "$1" = "all" ] || [ "$1" = "pinyin" ]; then
    if [ ! -d "$PINYIN_ROOT" ]; then
        mkdir -p "$PINYIN_ROOT"
    fi

    echo "install xiaohe mb file for pinyin input method"
    if [ -f "$TARGET_PYSYM" ]; then
        echo "backup existing $TARGET_PYSYM"
        cp "$TARGET_PYSYM" "$TARGET_PYSYM_BAK"
    fi

    echo "copy $PYSYM to $TARGET_PYSYM"
    cp "$PYSYM" "$TARGET_PYSYM"
fi

echo "restart fcitx"
fcitx -r
