from pydantic.dataclasses import dataclass


@dataclass
class EnvironmentOption:
    doujinshi_api_key: str
    target_folder: str


@dataclass
class ProcessOption:
    mode: int
    ignore_low_similarity: bool
    warn_page_count_mismatch: bool
    rename_file_by_no: bool
    remove_empty_page: bool


@dataclass
class CompressOption:
    mode: int
    remove_folder_after_compress: bool
    make_minimal_archive: bool
    make_more_archive: bool


@dataclass
class ShortcutOption:
    create_doujinshi_shortcut: bool
    create_pixiv_shortcut: bool
    create_twitter_shortcut: bool
    create_custom_shortcut: bool
    custom_shortcut_title: str
    custom_shortcut_address: str


@dataclass
class ScanConfig:
    environment_option: EnvironmentOption
    process_option: ProcessOption
    compress_option: CompressOption
    shortcut_option: ShortcutOption
