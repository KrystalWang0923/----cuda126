import os
from datetime import datetime


def count_images(directory):
    """统计目录下的图片文件"""
    # 支持的图片格式
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.tif', '.webp')

    if not os.path.exists(directory):
        print(f"❌ 错误：路径不存在 - {directory}")
        return

    # 统计信息
    image_files = []
    total_size = 0
    extension_count = {}

    # 遍历目录
    for file in os.listdir(directory):
        if file.lower().endswith(image_extensions):
            file_path = os.path.join(directory, file)
            file_size = os.path.getsize(file_path)

            image_files.append(file)
            total_size += file_size

            # 统计各种格式的数量
            ext = os.path.splitext(file)[1].lower()
            extension_count[ext] = extension_count.get(ext, 0) + 1

    # 输出结果
    print("=" * 60)
    print(f"📁 目录路径: {directory}")
    print(f"📅 统计时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    print(f"🖼️  图片总数: {len(image_files)} 张")
    print(f"💾 总大小: {total_size / 1024 / 1024:.2f} MB")

    if image_files:
        print(f"\n📊 格式分布:")
        for ext, count in sorted(extension_count.items()):
            print(f"   {ext}: {count} 张")

        print(f"\n📋 前10个文件:")
        for i, file in enumerate(image_files[:10]):
            print(f"   {i + 1}. {file}")

        if len(image_files) > 10:
            print(f"   ... 还有 {len(image_files) - 10} 个文件")
    else:
        print("⚠️  该目录下没有找到图片文件")


# 执行统计
image_dir = r'G:\灯检机数据\图片保存\工位1\2023_12_19\相机1\OK\原图'
count_images(image_dir)