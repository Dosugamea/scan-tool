import configparser
import shutil

import PySimpleGUI as sg
from scan_struct import (
    CompressOption,
    EnvironmentOption,
    ProcessOption,
    ScanConfig,
    ShortcutOption,
)

ini = configparser.ConfigParser()
ini.read("./config.ini", "UTF-8")

sections = ini.__dict__["_sections"]
if sections == {}:
    shutil.copy("./config.ini.default", "./config.ini")
    ini.read("./config.ini", "UTF-8")

env_option = EnvironmentOption(**ini.__dict__["_sections"]["environment_option"])
process_option = ProcessOption(**ini.__dict__["_sections"]["process_option"])
compress_option = CompressOption(**ini.__dict__["_sections"]["compress_option"])
shortcut_option = ShortcutOption(**ini.__dict__["_sections"]["shortcut_option"])
config = ScanConfig(env_option, process_option, compress_option, shortcut_option)
print(config.process_option)

sg.theme("DarkGrey9")

left_frame = sg.Frame(
    "",
    [
        [
            sg.Text("処理モード"),
        ],
        [
            sg.Radio(
                "1:対象フォルダの子フォルダを監視",
                key="-1-",
                group_id="0",
                default=config.process_option.mode == 1,
            )
        ],
        [
            sg.Radio(
                "2:対象フォルダ内の画像を監視+フォルダ作成",
                key="-2-",
                group_id="0",
                default=config.process_option.mode == 2,
            )
        ],
        [
            sg.Radio(
                "3:既存フォルダをリネーム",
                key="-3-",
                group_id="0",
                default=config.process_option.mode == 3,
            )
        ],
        [
            sg.Text("動作オプション"),
        ],
        [
            sg.Checkbox(
                "画像一致率が80%以下の場合処理しない",
                default=config.process_option.ignore_low_similarity,
                key="-4-",
            )
        ],
        [
            sg.Checkbox(
                "ページ数不一致時警告する",
                default=config.process_option.warn_page_count_mismatch,
                key="-5-",
            )
        ],
        [
            sg.Checkbox(
                "ファイルをページ番号順にリネーム",
                default=config.process_option.rename_file_by_no,
                key="-6-",
            )
        ],
        [
            sg.Checkbox(
                "白紙ページを削除", default=config.process_option.remove_empty_page, key="-7-"
            )
        ],
        [sg.Text("Doujinshi.org APIキー")],
        [
            sg.InputText(
                config.environment_option.doujinshi_api_key,
                key="-INPUTAPI-",
                enable_events=True,
                tooltip="APIキーを入力",
            ),
            sg.FileBrowse(button_text="サイトへ", font=("メイリオ", 8), key="-FILENAME-"),
        ],
        [sg.Text("処理対象フォルダ")],
        [
            sg.InputText(
                config.environment_option.target_folder,
                key="-INPUTTEXT-",
                enable_events=True,
                tooltip="フォルダを選択してください",
            ),
            sg.FileBrowse(button_text="選択する", font=("メイリオ", 8), key="-FILENAME-"),
        ],
    ],
    size=(400, 400),
)

right_frame = sg.Frame(
    "",
    [
        [
            sg.Text("圧縮オプション"),
        ],
        [
            sg.Radio(
                "ZIP", key="-1-", group_id="1", default=config.compress_option.mode == 1
            ),
            sg.Checkbox(
                "圧縮後元フォルダを消去",
                default=config.compress_option.remove_folder_after_compress,
                key="-2-",
            ),
        ],
        [
            sg.Radio(
                "PDF", key="-2-", group_id="1", default=config.compress_option.mode == 2
            ),
            sg.Checkbox(
                "縮小版を作成", default=config.compress_option.make_minimal_archive, key="-3-"
            ),
        ],
        [
            sg.Radio(
                "ZIP + PDF",
                key="-3-",
                group_id="1",
                default=config.compress_option.mode == 3,
            ),
            sg.Checkbox(
                "縮小版を別ファイルに出力",
                default=config.compress_option.make_more_archive,
                key="-4-",
            ),
        ],
        [
            sg.Radio(
                "圧縮しない",
                key="-4-",
                group_id="1",
                default=config.compress_option.mode == 4,
            )
        ],
        [
            sg.Text("ショートカット作成オプション"),
        ],
        [
            sg.Checkbox(
                "Doujinshi.org",
                default=config.shortcut_option.create_doujinshi_shortcut,
                key="-5-",
            )
        ],
        [
            sg.Checkbox(
                "Pixivアカウント(可能なら)",
                default=config.shortcut_option.create_pixiv_shortcut,
                key="-6-",
            )
        ],
        [
            sg.Checkbox(
                "Twitterアカウント(可能なら)",
                default=config.shortcut_option.create_twitter_shortcut,
                key="-7-",
            )
        ],
        [sg.Checkbox("任意ページ", default=config.shortcut_option.create_custom_shortcut)],
        [
            sg.InputText(
                default_text=config.shortcut_option.custom_shortcut_title,
                key="-INPUTPAGEADDRESS-",
                enable_events=True,
                tooltip="任意のページ名",
            ),
        ],
        [
            sg.InputText(
                default_text=config.shortcut_option.custom_shortcut_address,
                key="-INPUTPAGEADDRESS-",
                enable_events=True,
                tooltip="任意のページアドレス",
            ),
        ],
    ],
    size=(380, 400),
)


layout = [
    [left_frame, right_frame],
    [sg.Submit("設定を保存して反映", key="-submit-", size=(98, 2))],
    [sg.Text("処理ログ")],
    [sg.Output(size=(110, 10), key="log")],
]

window = sg.Window("Scan Tool", layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, "Exit"):
        break

window.close()
