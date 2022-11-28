from rembg import remove
from PIL import Image

def main():
    input_path = 'foto_1.png'
    output_path = 'foto_2.png'

    input = Image.open(input_path)
    output = remove(input)
    output.save(output_path)


if __name__ == '__main__':
    main()
