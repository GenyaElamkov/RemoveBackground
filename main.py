"""
Скрипт обрабатывает фотографии, удаляет фон с фотографий.
Необработанные фотографии располагают в директории input_image.
Обработанные фотографии располагаются в директории output_image.
"""

from rembg import remove
from PIL import Image
from pathlib import Path
from tqdm import tqdm


def get_path() -> list:
    """
    Собирает пути к файлам, где лежат фотографии.
    list_of_extensions - устанавливаются расширения фотографий, которое надо обработать.
    :return list путей расположения фотографий.
    """
    list_of_extensions = ['*.png', '*.jpg']
    all_files = []

    for ext in list_of_extensions:
        all_files.extend(Path('./input_image/').glob(ext))

    return all_files


def remove_background(all_files: list) -> None:
    """
    Удаляет фон с фотографий.
    Сохраняет фотографии в директорию output_path.
    Показывает прогресс бар.
    """

    pbar = tqdm(total=len(all_files))
    for i, item in enumerate(all_files):
        input_path = Path(item)
        file_name = input_path.stem

        output_path = f'output_image/{file_name}.png'

        input_img = Image.open(input_path)
        output_img = remove(input_img)
        output_img.save(output_path)

        pbar.update(1)
    pbar.close()


def main():
    remove_background(get_path())


if __name__ == '__main__':
    main()

# TODO: Сделать test
