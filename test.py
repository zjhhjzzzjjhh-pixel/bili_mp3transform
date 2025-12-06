import os


def remove_leading_zeros(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
    if data.startswith(b'000000000'):
        data = data[9:]
    return data


def process_directory(C:\Users\fjqmx\Desktop\3\M4S文件\人渣反派1-10 M4s, C:\Users\fjqmx\Desktop\3\MP3音频):
    if not os.path.exists(C:\Users\fjqmx\Desktop\3\MP3音频):
        os.makedirs(C:\Users\fjqmx\Desktop\3\MP3音频)

    for filename in os.listdir(C:\Users\fjqmx\Desktop\3\M4S文件\人渣反派1-10 M4s):
        if filename.endswith('.m4s'):
            file_path = os.path.join(C:\Users\fjqmx\Desktop\3\M4S文件\人渣反派1-10 M4s, filename)
            data = remove_leading_zeros(file_path)

            # 将处理后的数据另存为新的文件
            output_filename = filename.replace('.m4s', '.mp3')
            output_path = os.path.join(C:\Users\fjqmx\Desktop\3\MP3音频, output_filename)
            with open(output_path, 'wb') as output_file:
                output_file.write(data)


# 使用示例
input_directory = 'D:/m4smp3/m4s'  # 替换为你的输入文件夹路径
output_directory = 'D:/m4smp3/mp3'  # 替换为你的输出文件夹路径
process_directory(input_directory, output_directory)

