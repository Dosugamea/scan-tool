import PySimpleGUI as sg

sg.theme("DarkGrey9")

left_frame = sg.Frame(
    "",
    [
        [
            sg.Text("処理モード"),
        ],
        [sg.Radio("1:対象フォルダの子フォルダを監視", key="-1-", group_id="0")],
        [sg.Radio("2:対象フォルダ内の画像を監視+フォルダ作成", key="-2-", group_id="0")],
        [sg.Radio("3:既存フォルダをリネーム", key="-3-", group_id="0")],
        [
            sg.Text("動作オプション"),
        ],
        [sg.Checkbox("画像一致率が80%以下の場合処理しない", default=False)],
        [sg.Checkbox("ページ数不一致時警告する", default=False)],
        [sg.Checkbox("ファイルをページ番号順にリネーム", default=False)],
        [sg.Checkbox("白紙ページを削除", default=False)],
        [sg.Text("Doujinshi.org APIキー")],
        [
            sg.InputText(
                "APIキーを入力",
                key="-INPUTAPI-",
                enable_events=True,
            ),
            sg.FileBrowse(button_text="サイトへ", font=("メイリオ", 8), key="-FILENAME-"),
        ],
        [sg.Text("処理対象フォルダ")],
        [
            sg.InputText(
                "フォルダを選択してください",
                key="-INPUTTEXT-",
                enable_events=True,
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
            sg.Radio("ZIP", key="-1-", group_id="1"),
            sg.Checkbox("圧縮後元フォルダを消去", default=False),
        ],
        [
            sg.Radio("PDF", key="-2-", group_id="1"),
            sg.Checkbox("縮小版を作成", default=False),
        ],
        [
            sg.Radio("ZIP + PDF", key="-3-", group_id="1"),
            sg.Checkbox("縮小版を別ファイルに出力", default=False),
        ],
        [sg.Radio("圧縮しない", key="-4-", group_id="1")],
        [
            sg.Text("ショートカット作成オプション"),
        ],
        [sg.Checkbox("Doujinshi.org", default=False)],
        [sg.Checkbox("Pixivアカウント(可能なら)", default=False)],
        [sg.Checkbox("Twitterアカウント(可能なら)", default=False)],
        [sg.Checkbox("任意ページ", default=False)],
        [
            sg.InputText(
                "任意のページ名",
                key="-INPUTPAGEADDRESS-",
                enable_events=True,
            ),
        ],
        [
            sg.InputText(
                "任意のページアドレス",
                key="-INPUTPAGEADDRESS-",
                enable_events=True,
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
    if event in (sg.WIN_CLOSED, "Exit"):
        break

window.close()
