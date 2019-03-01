import os

def getFileList(path):
    swift_files=[]
    dirs=[]
    lists=os.listdir(path)
    for li in lists:
        if os.path.isdir(path+'/'+li):
            dirs.append(path+'/'+li)
        else:
            if '.png' not in li or '.jpg' not in li:
                swift_files.append(path+'/'+li)

    for i in range(0,10):
        for di in dirs:
            lists = os.listdir(di)
            for li in lists:
                if os.path.isdir(di +'/'+ li):
                    dirs.append(di +'/'+ li)
                else:
                    if '.png' not in li or '.jpg' not in li:
                        swift_files.append(di+'/'+li)

    swift_files=list(set(swift_files))
    for sw in swift_files:
        print(sw)
    print('文件个数', len(swift_files))
    return swift_files

def getImageNames(path):
    images_name=[]
    dirs = []
    lists=os.listdir(path)
    for li in lists:
        if os.path.isdir(path+'/'+li):
            if '.imageset' in path+'/'+li:
                images_name.append(path+'/'+li)
            else:
                dirs.append(path+'/'+li)

    for i in range(0, 4):
        for di in dirs:
            lists = os.listdir(di)
            for li in lists:
                if os.path.isdir(di +'/'+ li):
                    if '.imageset' in di + '/' + li:
                        images_name.append(di + '/' + li)
                    else:
                        dirs.append(di + '/' + li)

    images_name=list(set(images_name))

    used_img_names=[]
    for im in images_name:
        name=im.split('/')[-1].replace('.imageset','')
        used_img_names.append(name)
        print(name)

    return used_img_names


def check_img(files,images):
    usedImgs=[]
    unusedImgs=[]
    for img_name in images:
        img_is_used = False
        for file_path in files:
            if 'Assets.xcassets' in file_path:
                continue
            codes=[]
            try:
                f = open(file_path)  # 返回一个文件对象
                line = f.readline()
                while line:
                    line = f.readline()
                    codes.append(str(line))
                f.close()

            except FileNotFoundError:
                continue
            except UnicodeDecodeError:
                continue

            for code in codes:
                if img_name in code:
                    img_is_used = True

        if img_is_used:
            print(img_name,'正在使用')
            usedImgs.append(img_name)
        else:
            print(img_name, '未使用')
            unusedImgs.append(img_name)

    usedImgs=list(set(usedImgs))
    unusedImgs=list(set(unusedImgs))

    print('正在使用的有')
    for us in usedImgs:
        print(us)
    print('个数', len(usedImgs))

    print('\n\n')

    print('未使用的有')
    for unus in unusedImgs:
        print(unus)
    print('个数',len(unusedImgs))


if __name__ == '__main__':
    print('Xcode 未使用图片资源检测')
    print('请输入项目地址（绝对路径）')
    project_path=input()
    print('请输入 Assets.xcassets 地址（绝对路径）')
    images_path = input()
    print('检索文件中')
    check_img(getFileList(project_path),getImageNames(images_path))
