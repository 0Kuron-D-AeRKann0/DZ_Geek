# print('Задание 1')
#
# import os
#
# sl = {'my_project':
#           ['settings','mainapp','adminapp','authapp']
#       }
#
# for root, folders in sl.items():
#     if os.path.exists(root):
#         print(root,'соответсвует')
#     else:
#         for folder in folders:
#             cur_dir = os.path.join(root,folder)
#             os.makedirs(cur_dir)
#
# print('Задание 2')
#
# # pip install pyyaml
#
# import os
# import yaml
#
# sl = {'my_project':
#       [{'settings': [
#         '__init__.py','dev.py','prod.py'
#       ],
#       },
#           {'mainapp': [
#               '__init__.py','models.py','views.py', {'tamplates': [{
#                   'mainapp': ['base.html','index.html']}]
#               }]},
#           {'authapp': ['__init__.py','models.py','views,py', {'templates': [{
#               'authapp': ['base.html','index.html']}]
#           }
#                         ]
#            }
#       ]
# }
# f = open('config.yaml','a+')
# f.write(yaml.dump(sl))
# f.close()
#
# with open("config.yaml") as y_file:
#     sl = yaml.safe_load(y_file)
#
#
# def create_data(data):
#     for folder,data_tmps in data.items():
#         if not os.path.exists(folder):
#             os.mkdir(folder)
#         os.chdir(folder)
#         for data_tmp in data_tmps:
#             if isinstance(data_tmp,dict):
#                 create_data(data_tmp)
#             else:
#                 if not os.path.exists(data_tmp):
#                     if '.' in data_tmp:
#                         with open(data_tmp, 'a+') as f:
#                             f.write('')
#     else:
#         os.chdir('../')
#
#
# create_data(sl)
#
# print('Задание 3')
#
# import os
# import shutil
#
# my_dir = 'task3'
# if not os.path.exists(my_dir):
#     os.mkdir(my_dir)
#
# folder = r'my_project'
# files = []
#
# for r,d,f in os.walk(folder):
#     for file in f:
#         if '.html' in file:
#             files.append(os.path.join(r,file))
# for path in files:
#     folder_new = os.path.join(my_dir,os.path.basename(os.path.dirname(path)))
#     if not os.path.exists(folder_new):
#         os.mkdir(folder_new)
#     save_path = os.path.join(folder_new,os.path.basename(path))
#     shutil.copy(path,save_path)
#
# print('Задание 4')
#
# import os
# import sys
#
# size = {}
#
#
# def scan_mem(pth):
#
#     if not os.path.exists(pth):
#         return
#     with os.scandir(pth) as files:
#
#         for node in files:
#
#             if os.path.isfile(node):
#
#                 mem = 10 ** len(str(os.stat(node).st_size))
#                 size[mem] = size.get(mem, 0) + 1
#             elif os.path.isdir(node):
#                 scan_mem(os.path.join(pth, node))
#
#
# if __name__ == "__main__":
#
#     if len(sys.argv) == 2:
#         pth = sys.argv[1]
#     else:
#         pth = os.getcwd()
#
#     scan_mem(pth)
#     print(size)
#
# print('Задание 5')
# 
# import os
# import sys
#
# size = {}
#
#
# def scan_mem(pth):
#
#     if not os.path.exists(pth):
#         return
#
#     with os.scandir(pth) as files:
#
#         for node in files:
#
#             if node.is_file():
#
#                 mem = 10 ** len(str(os.stat(node).st_size))
#
#                 file_extend = os.path.splitext(node)[-1]
#
#                 count, extends = size.get(mem, (0, set()))
#
#                 extends.add(file_extend)
#                 count += 1
#
#                 size[mem] = (count, extends)
#
#             elif node.is_dir():
#                 scan_mem(os.path.join(pth, node))
#
#
# if __name__ == "__main__":
#
#     if len(sys.argv) == 2:
#         pth = sys.argv[1]
#     else:
#         pth = os.getcwd()
#
#     scan_mem(pth)
#     print({ k:(size[k][0], list(size[k][1])) for k in size})