from rembg import remove
from PIL import Image
from pathlib import Path


def get_path() -> list:
    list_of_extensions = ['*.png', '*.jpg']
    all_files = []

    for ext in list_of_extensions:
        all_files.extend(Path('./input_image/').glob(ext))

    return all_files


def remove_background():
    all_files = get_path()
    # print(all_files)
    for i, item in enumerate(all_files):
        input_path = Path(item)
        # print(input_path)
        file_name = input_path.stem

        output_path = f'output_image/{file_name}.png'
        # print(output_path)
        input = Image.open(input_path)
        output = remove(input)
        #
        output.save(output_path)
        # print(i)

def main():
    remove_background()
    # input_path = 'foto_1.png'
    # output_path = 'foto_2.png'
    #
    # input = Image.open(input_path)
    # output = remove(input)
    # output.save(output_path)


if __name__ == '__main__':
    main()
